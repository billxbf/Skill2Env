# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One planner call per Skill, one creator call per proposal, then host acceptance."""

from __future__ import annotations

import contextlib
import json
import random
import shutil
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from .axes import TaskAxes, sample_axes
from .buildaudit import TaskAuditor
from .bundle import BundleError, load_skill_bundle
from .generator import DEFAULT_TASKS_PER_SKILL, AgentRunner, GeneratorError
from .models import ContractError, GenerationRecord, Plan, Proposal, SkillBundle
from .output import (
    append_jsonl,
    format_task_name,
    publish_task,
    write_corpus_manifest,
    write_creator_state,
)
from .task_config import write_authoritative_task_toml
from .tracker import RunTracker
from .validation import (
    DEFAULT_MAX_TASK_SIZE_MIB,
    MIB_BYTES,
    TaskPostChecker,
    completed_task_size_bytes,
)


@dataclass
class PipelineConfig:
    skill_path: Path
    output_dir: Path
    state_dir: Path
    tasks_per_skill: int = DEFAULT_TASKS_PER_SKILL
    max_parallel_workers: int = 1
    max_task_size_mib: int = DEFAULT_MAX_TASK_SIZE_MIB
    write_manifest: bool = True


class SkillPipeline:
    def __init__(
        self,
        config: PipelineConfig,
        runner: AgentRunner,
        *,
        auditor: TaskAuditor,
        post_checker: Optional[TaskPostChecker] = None,
        tracker: Optional[RunTracker] = None,
        audit_slots: Optional[threading.Semaphore] = None,
        rng: Optional[random.Random] = None,
    ):
        self.config = config
        self.runner = runner
        self.auditor = auditor
        self.post_checker = post_checker or TaskPostChecker()
        self.tracker = tracker
        # Harbor Oracle/NOP runs build images; the batch shares one cap across skills.
        self.audit_slots = audit_slots
        self.rng = rng

    def run(self) -> Dict[str, object]:
        cfg = self.config
        cfg.output_dir.mkdir(parents=True, exist_ok=True)
        cfg.state_dir.mkdir(parents=True, exist_ok=True)
        records_path = cfg.state_dir / "records.jsonl"
        records_path.unlink(missing_ok=True)

        record = self._run_skill()
        append_jsonl(records_path, record.to_dict())
        summary = summarize_records([record], requested=1)
        _write_json(cfg.state_dir / "summary.json", summary)
        if cfg.write_manifest:
            write_corpus_manifest(cfg.output_dir, record.attempts)
        return summary

    def _run_skill(self) -> GenerationRecord:
        started = time.monotonic()
        source_path = self.config.skill_path.expanduser().resolve()
        record = GenerationRecord(
            skill_id=source_path.name or "skill",
            provider="local",
            source_path=str(source_path),
            status="failed",
            stage="ingest",
        )
        try:
            bundle = load_skill_bundle(source_path)
            record.skill_id = bundle.id
            record.provider = bundle.provider
            record.source_path = bundle.source_path
            record.bundle_digest = bundle.digest
        except BundleError as exc:
            record.reason_code = exc.code
            record.reason = str(exc)
            self._finish_jobs("failed", "ingest", str(exc), include_planner=True)
            return _finish_record(record, started)

        record.stage = "plan"
        self._update_job("planner", 0, "running", "planning", "Planner started")
        try:
            plan = self.runner.plan(
                bundle, count=self.config.tasks_per_skill, state_dir=self.config.state_dir
            )
        except (GeneratorError, ContractError, OSError, ValueError) as exc:
            code = exc.code if isinstance(exc, GeneratorError) else "planner_failed"
            record.reason_code = code
            record.reason = str(exc)
            self._update_job("planner", 0, "failed", "failed", str(exc))
            self._finish_jobs("failed", "failed", "Planner failed")
            return _finish_record(record, started)
        _write_json(self.config.state_dir / "planner" / "plan.json", plan.to_dict())

        count = len(plan.proposals)
        self._update_job(
            "planner", 0, "succeeded", "complete", f"{count} proposal(s)"
        )
        self._finish_jobs("skipped", "skipped", "Planner wrote fewer proposals", start=count)
        if count == 0:
            record.status = "skipped"
            record.stage = "complete"
            record.reason_code = "no_proposals"
            record.reason = plan.notes or "planner found no acceptable terminal task"
            return _finish_record(record, started)

        record.stage = "create"
        record.attempts = self._run_proposals(bundle, plan)
        record.generator_invocations = 1 + count
        record.task_dirs = [
            str(attempt["path"]) for attempt in record.attempts if attempt["status"] == "retained"
        ]
        statuses = [str(attempt["status"]) for attempt in record.attempts]
        failures = "; ".join(
            f"{attempt['proposal_id']} [{attempt['reason_code']}]: {attempt['reason']}"
            for attempt in record.attempts
            if attempt["status"] != "retained"
        )
        record.stage = "complete"
        if all(status == "retained" for status in statuses):
            record.status = "retained"
        elif "retained" in statuses:
            record.status = "retained_partial"
            record.reason_code = "attempt_not_retained"
            record.reason = failures
        elif all(status == "infra_failed" for status in statuses):
            record.status = "infra_failed"
            record.reason_code = "registry_unavailable"
            record.reason = failures
        else:
            record.status = "failed"
            record.reason_code = "generation_failed"
            record.reason = failures or "no task was retained"
        return _finish_record(record, started)

    def _run_proposals(self, bundle: SkillBundle, plan: Plan) -> List[Dict[str, object]]:
        proposals = plan.proposals
        all_axes = sample_axes(len(proposals), rng=self.rng)
        task_names = [format_task_name(bundle.id) for _ in proposals]
        attempts: Dict[int, Dict[str, object]] = {}
        executor = ThreadPoolExecutor(
            max_workers=min(self.config.max_parallel_workers, len(proposals)),
            thread_name_prefix="skill2env-creator",
        )
        futures = {
            executor.submit(
                self._run_variant,
                variant=variant,
                bundle=bundle,
                proposal=proposal,
                axes=all_axes[variant],
                task_name=task_names[variant],
            ): variant
            for variant, proposal in enumerate(proposals)
        }
        try:
            for future in as_completed(futures):
                variant = futures[future]
                try:
                    attempt = future.result()
                except (GeneratorError, ContractError, RuntimeError, OSError, ValueError) as exc:
                    code = exc.code if isinstance(exc, GeneratorError) else "creation_failed"
                    attempt = _attempt(
                        task_names[variant], variant, proposals[variant], all_axes[variant],
                        status="failed", reason_code=code, reason=str(exc),
                    )
                    self._update_job("creator", variant, "failed", "failed", str(exc))
                attempts[variant] = attempt
        except KeyboardInterrupt:
            cancel_all = getattr(self.runner, "cancel_all", None)
            if callable(cancel_all):
                cancel_all()
            for future in futures:
                future.cancel()
            if self.tracker is not None:
                self.tracker.cancel_nonterminal("Generation interrupted")
            raise
        finally:
            executor.shutdown(wait=True, cancel_futures=True)
        return [attempts[index] for index in sorted(attempts)]

    def _run_variant(
        self,
        *,
        variant: int,
        bundle: SkillBundle,
        proposal: Proposal,
        axes: TaskAxes,
        task_name: str,
    ) -> Dict[str, object]:
        if self.tracker is not None and self.tracker.cancelled:
            raise GeneratorError("cancelled", "Batch generation was interrupted")

        def fail(stage: str, reason: str, *, status: str = "failed", digest=None):
            self._update_job("creator", variant, "failed", stage, reason)
            return _attempt(
                task_name, variant, proposal, axes,
                status=status, reason_code=stage, reason=reason, digest=digest,
            )

        self._update_job(
            "creator", variant, "running", "creating",
            f"Creator started ({proposal.id})",
        )
        run = self.runner.create(
            bundle,
            task_name=task_name,
            variant_index=variant,
            state_dir=self.config.state_dir,
            proposal=proposal,
            axes=axes,
        )
        private_dir = write_creator_state(
            self.config.state_dir,
            task_name=task_name,
            transcript=run.transcript,
            prompt=run.prompt,
            proposal=proposal,
            axes=axes,
        )
        try:
            self._update_job("creator", variant, "running", "validating", "Static host checks")
            write_authoritative_task_toml(
                run.task_dir,
                task_name=task_name,
                bundle=bundle,
                proposal=proposal,
                axes=axes,
            )
            size_bytes = completed_task_size_bytes(run.task_dir)
            limit_bytes = self.config.max_task_size_mib * MIB_BYTES
            if size_bytes > limit_bytes:
                self._retain_rejected_candidate(run.task_dir, private_dir)
                return fail(
                    "task_too_large",
                    f"completed task size {size_bytes} bytes exceeds "
                    f"{self.config.max_task_size_mib} MiB",
                )
            post_check = self.post_checker.check(run.task_dir, bundle=bundle)
            _write_json(private_dir / "post-check.json", post_check.to_dict())
            if not post_check.ok:
                self._retain_rejected_candidate(run.task_dir, private_dir)
                return fail("static_validation_failed", "; ".join(post_check.errors))

            self._update_job("creator", variant, "running", "accepting", "Harbor Oracle and NOP")
            slots = self.audit_slots if self.audit_slots is not None else contextlib.nullcontext()
            with slots:
                audit = self.auditor.audit(run.task_dir, audit_dir=private_dir / "acceptance")
            _write_json(private_dir / "audit.json", audit.to_dict())
            if not audit.ok:
                self._retain_rejected_candidate(run.task_dir, private_dir)
                return fail(
                    audit.reason_code or audit.status,
                    "; ".join(audit.errors),
                    status="infra_failed" if audit.status == "infra_failed" else "failed",
                    digest=audit.task_digest,
                )

            self._update_job("creator", variant, "running", "publishing", "Publishing task")
            published = publish_task(
                candidate=run.task_dir,
                output_dir=self.config.output_dir,
                task_name=task_name,
            )
            self._update_job("creator", variant, "succeeded", "complete", str(published))
            return _attempt(
                task_name, variant, proposal, axes,
                status="retained", path=str(published), digest=audit.task_digest,
            )
        finally:
            shutil.rmtree(run.workspace, ignore_errors=True)

    @staticmethod
    def _retain_rejected_candidate(task_dir: Path, private_dir: Path) -> None:
        destination = private_dir / "candidate"
        if destination.exists():
            shutil.rmtree(destination)
        shutil.move(str(task_dir), destination)

    def _update_job(
        self, phase: str, variant: int, status: str, stage: str, message: str
    ) -> None:
        if self.tracker is None:
            return
        job_id = self.tracker.job_id_for(self.config.state_dir, phase, variant)
        if job_id is not None:
            self.tracker.update_job(job_id, status=status, stage=stage, message=message)

    def _finish_jobs(
        self,
        status: str,
        stage: str,
        message: str,
        *,
        start: int = 0,
        include_planner: bool = False,
    ) -> None:
        """Close creator slots from ``start`` onward (and optionally the planner job)."""
        if self.tracker is None:
            return
        if include_planner:
            self._update_job("planner", 0, status, stage, message)
        variant = start
        while True:
            job_id = self.tracker.job_id_for(self.config.state_dir, "creator", variant)
            if job_id is None:
                return
            self.tracker.update_job(job_id, status=status, stage=stage, message=message)
            variant += 1


def _attempt(
    task_name: str,
    variant: int,
    proposal: Proposal,
    axes: TaskAxes,
    *,
    status: str,
    reason_code: Optional[str] = None,
    reason: Optional[str] = None,
    path: Optional[str] = None,
    digest: Optional[str] = None,
) -> Dict[str, object]:
    return {
        "task_name": task_name,
        "variant": variant,
        "proposal_id": proposal.id,
        "status": status,
        "reason_code": reason_code,
        "reason": reason,
        "path": path,
        "digest": digest,
        "axes": axes.to_dict(),
    }


def summarize_records(records: List[GenerationRecord], *, requested: int) -> Dict[str, object]:
    counts: Dict[str, int] = {}
    attempts: List[Dict[str, object]] = []
    invocations = 0
    for record in records:
        counts[record.status] = counts.get(record.status, 0) + 1
        attempts.extend(record.attempts)
        invocations += record.generator_invocations
    retained = sum(1 for attempt in attempts if attempt.get("status") == "retained")
    failed = any(record.status in {"failed", "infra_failed"} for record in records) or any(
        attempt.get("status") in {"failed", "infra_failed"} for attempt in attempts
    )
    return {
        "schema_version": "4.0",
        "requested_skills": requested,
        "terminal_records": len(records),
        "status_counts": counts,
        "retained_tasks": retained,
        "generator_invocations": invocations,
        "failures": [
            {"skill": record.skill_id, "reason_code": record.reason_code, "reason": record.reason}
            for record in records
            if record.status not in {"retained"}
        ],
        "attempts": attempts,
        "acceptance_gate": {
            "all_retained_tasks_host_accepted": retained > 0,
            "no_generation_failures": not failed,
            "passed": retained > 0 and not failed,
        },
    }


def _finish_record(record: GenerationRecord, started: float) -> GenerationRecord:
    record.elapsed_seconds = round(time.monotonic() - started, 3)
    return record


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
