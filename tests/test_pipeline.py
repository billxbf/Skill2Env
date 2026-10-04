# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Docker-free tests: fake planner/creator runner and fake Oracle/NOP auditor."""

from __future__ import annotations

import json
import random
import shutil
from pathlib import Path

import pytest

from skill2env.axes import COMPLEXITY_TURNS, sample_axes
from skill2env.batch import BatchConfig, BatchRunner, create_batch_tracker, discover_skills
from skill2env.buildaudit import BuildAuditReport
from skill2env.generator import CreationRun, GeneratorError
from skill2env.models import ContractError, CreatorResult, Plan, Proposal
from skill2env.prompts import creator_prompt, planner_prompt
from skill2env.task_config import validate_harbor_task_toml, write_authoritative_task_toml
from skill2env.validation import TaskPostChecker
from skill2env.bundle import load_skill_bundle


RUBRIC = """## Good Signals
- Reproduces the failure before changing code.

## Negative Signals
- Patches the symptom in the test instead of the cause.
"""


def proposal_dict(index: int) -> dict:
    return {
        "id": f"Problem {index}",
        "title": f"Problem {index}",
        "capability": "root-cause tracing",
        "environment": "a small repository with a flaky test",
        "artifacts": [
            {"url": "https://github.com/example/repo", "revision": "abc", "description": "repo"},
            {"description": "malformed lead without url or path"},
        ],
        "problem": "find the polluting test",
        "skill_approach": "bisect the test order",
        "good_behaviors": ["reproduces first"],
        "bad_behaviors": ["adds sleeps"],
    }


class FakeRunner:
    def __init__(self, proposals: int, *, fail_variant: int | None = None):
        self.proposals = proposals
        self.fail_variant = fail_variant
        self.created: list[tuple[str, str]] = []

    def plan(self, bundle, *, count, state_dir):
        data = {"proposals": [proposal_dict(i % 2) for i in range(self.proposals)]}
        return Plan.from_dict(data, limit=count)

    def create(self, bundle, *, task_name, variant_index, state_dir, proposal, axes):
        if variant_index == self.fail_variant:
            raise GeneratorError("codex_failed", "boom")
        self.created.append((proposal.id, axes.complexity))
        workspace = Path(state_dir) / "workspaces" / task_name
        task = workspace / task_name
        for sub in ("environment", "tests", "solution"):
            (task / sub).mkdir(parents=True, exist_ok=True)
        (task / "instruction.md").write_text("Fix the flaky test.\n")
        (task / "environment" / "Dockerfile").write_text("FROM python:3.12-slim-bookworm\n")
        (task / "tests" / "test.sh").write_text("#!/bin/bash\necho 1 > /logs/verifier/reward.txt\n")
        (task / "tests" / "rubric.md").write_text(RUBRIC)
        (task / "solution" / "solve.sh").write_text("#!/bin/bash\ntrue\n")
        result = CreatorResult.from_dict({"description": "Fix a flaky test"})
        return CreationRun(workspace, task, result, transcript="", prompt="prompt")


class FakeAuditor:
    def audit(self, task_dir, *, audit_dir):
        return BuildAuditReport(status="accepted", task_digest="d" * 64)


def make_skill(root: Path) -> Path:
    skill = root / "skills" / "debugging"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: debugging\ndescription: debug\n---\nBody\n")
    return root / "skills"


def run_batch(tmp_path: Path, runner: FakeRunner, tasks: int):
    source = make_skill(tmp_path)
    out, run_dir = tmp_path / "out", tmp_path / "run"
    specs = discover_skills(source, out, run_dir)
    config = BatchConfig(
        input_root=source,
        output_root=out,
        run_dir=run_dir,
        model="m",
        reasoning_effort="high",
        codex_version="0",
        generator_image="img",
        tasks_per_skill=tasks,
        max_parallel_workers=2,
    )
    tracker = create_batch_tracker(config, specs)
    batch = BatchRunner(config, specs, runner, tracker)
    batch.auditor = FakeAuditor()
    return batch.run(), out, tracker


def test_end_to_end_retains_every_proposal(tmp_path):
    runner = FakeRunner(proposals=3)
    summary, out, tracker = run_batch(tmp_path, runner, tasks=3)
    assert summary["retained_tasks"] == 3
    assert summary["acceptance_gate"]["passed"]
    # Duplicate planner ids are made unique.
    assert sorted(pid for pid, _ in runner.created) == ["problem-0", "problem-0-2", "problem-1"]
    # Complexity is stratified: three tasks cover all three levels.
    assert sorted(level for _, level in runner.created) == sorted(COMPLEXITY_TURNS)
    task_dirs = sorted(out.glob("debugging/task_*"))
    assert len(task_dirs) == 3
    config = validate_harbor_task_toml((task_dirs[0] / "task.toml").read_text())
    assert config.metadata["proposal_id"].startswith("problem-")
    assert config.metadata["complexity"].endswith("turns)")
    status = json.loads((tracker.root / "status.json").read_text())
    assert status["counts"] == {"succeeded": 4}  # planner + 3 creators


def test_fewer_proposals_and_creator_failure(tmp_path):
    runner = FakeRunner(proposals=2, fail_variant=1)
    summary, _, tracker = run_batch(tmp_path, runner, tasks=4)
    assert summary["retained_tasks"] == 1
    assert not summary["acceptance_gate"]["passed"]
    assert summary["status_counts"] == {"retained_partial": 1}
    status = json.loads((tracker.root / "status.json").read_text())
    assert status["counts"] == {"succeeded": 2, "failed": 1, "skipped": 2}


def test_zero_proposals_skips_skill(tmp_path):
    summary, _, _ = run_batch(tmp_path, FakeRunner(proposals=0), tasks=2)
    assert summary["status_counts"] == {"skipped": 1}
    assert summary["retained_tasks"] == 0


def test_planner_failure_fails_skill(tmp_path):
    class BrokenPlanner(FakeRunner):
        def plan(self, bundle, *, count, state_dir):
            raise GeneratorError("planner_contract_failed", "no proposals.json")

    summary, _, _ = run_batch(tmp_path, BrokenPlanner(proposals=1), tasks=2)
    assert summary["status_counts"] == {"failed": 1}
    assert summary["failures"][0]["reason_code"] == "planner_contract_failed"


def test_plan_parsing():
    plan = Plan.from_dict({"proposals": [proposal_dict(0), {"id": "x"}]}, limit=5)
    assert len(plan.proposals) == 1
    assert len(plan.proposals[0].artifacts) == 1
    with pytest.raises(ContractError):
        Plan.from_dict({"proposals": [{"id": "x"}]}, limit=5)
    with pytest.raises(ContractError):
        Plan.from_dict({"workflows": []}, limit=5)


def test_sample_axes_stratifies_complexity():
    axes = sample_axes(6, rng=random.Random(0))
    assert sorted(a.complexity for a in axes) == sorted(list(COMPLEXITY_TURNS) * 2)


def test_rubric_check(tmp_path):
    runner = FakeRunner(proposals=1)
    source = make_skill(tmp_path)
    bundle = load_skill_bundle(source / "debugging")
    proposal = Plan.from_dict({"proposals": [proposal_dict(0)]}, limit=1).proposals[0]
    run = runner.create(
        bundle, task_name="task_x", variant_index=0, state_dir=tmp_path,
        proposal=proposal, axes=sample_axes(1)[0],
    )
    axes = sample_axes(1)[0]
    write_authoritative_task_toml(
        run.task_dir, task_name="task_x", bundle=bundle,
        creator_result=run.result, proposal=proposal, axes=axes,
    )
    checker = TaskPostChecker()
    assert checker.check(run.task_dir, bundle=bundle).ok
    rubric = run.task_dir / "tests" / "rubric.md"
    rubric.write_text("## Must-do\n- x\n")
    report = checker.check(run.task_dir, bundle=bundle)
    assert not report.checks["rubric"]
    rubric.write_text("## Good Signals\n\n## Negative Signals\n- y\n")
    assert any("no bullet" in e for e in checker.check(run.task_dir, bundle=bundle).errors)


def test_prompts_render(tmp_path):
    bundle = load_skill_bundle(make_skill(tmp_path) / "debugging")
    assert "exactly 4 proposals" in planner_prompt(bundle=bundle, count=4)
    proposal = Proposal.from_dict(proposal_dict(0))
    text = creator_prompt(
        bundle=bundle, task_name="task_x", proposal=proposal, axes=sample_axes(1)[0]
    )
    assert "## Good Signals" in text and '"capability": "root-cause tracing"' in text
    assert "{" not in text.split("## Problem proposal")[0]  # no unformatted placeholders
