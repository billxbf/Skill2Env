# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Command-line entry point for skill2env."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from rich.console import Console
from rich.progress import BarColumn, Progress, TextColumn, TimeElapsedColumn
from rich.table import Table

from .batch import BatchConfig, BatchRunner, create_batch_tracker, discover_skills
from .generator import (
    DEFAULT_MODEL,
    DEFAULT_REASONING_EFFORT,
    DEFAULT_TASKS_PER_SKILL,
    MAX_TASKS_PER_SKILL,
    REASONING_EFFORTS,
    ContainerizedCodexRunner,
    GeneratorError,
)
from .submit import SubmitError, submit_tasks
from .tracker import RunTracker, default_runs_root, new_run_id


console = Console()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="skill2env")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser(
        "generate",
        description=(
            "Plan N independent problems per Skill, build each into a Harbor task, and keep "
            "the ones that pass Oracle/NOP acceptance."
        ),
    )
    generate.add_argument(
        "path",
        type=Path,
        help="A Skill directory, a SKILL.md, or a directory scanned recursively for SKILL.md",
    )
    generate.add_argument(
        "-n",
        "--tasks",
        type=int,
        default=DEFAULT_TASKS_PER_SKILL,
        help=f"Problem proposals (and tasks) per Skill (default: {DEFAULT_TASKS_PER_SKILL})",
    )
    generate.add_argument(
        "-o", "--out", type=Path, default=Path("output"), help="Output root (default: ./output)"
    )
    generate.add_argument(
        "-j",
        "--workers",
        type=int,
        default=4,
        help="Concurrent Codex agents, and separately concurrent acceptance runs (default: 4)",
    )
    generate.add_argument("--model", default=DEFAULT_MODEL, help=f"default: {DEFAULT_MODEL}")
    generate.add_argument(
        "--effort",
        choices=REASONING_EFFORTS,
        default=DEFAULT_REASONING_EFFORT,
        help=f"Reasoning effort (default: {DEFAULT_REASONING_EFFORT})",
    )
    generate.add_argument(
        "--resume",
        action="store_true",
        help="Skip Skills already finished by a previous run into the same output root",
    )

    submit = subparsers.add_parser(
        "submit",
        description=(
            "Publish generated tasks to the Harbor hub registry "
            "(https://hub.harborframework.com). Requires 'harbor auth login'."
        ),
    )
    submit.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Task directories or corpus roots (scanned recursively for task.toml)",
    )
    submit.add_argument(
        "--org",
        help="Rewrite the task package org before publishing (task.name becomes <org>/<task>)",
    )
    submit.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Registry tag to apply (repeatable); 'latest' is always added",
    )
    submit.add_argument(
        "--public",
        action="store_true",
        help="Publish publicly (default: private to the publishing org)",
    )
    submit.add_argument(
        "--concurrency",
        type=int,
        default=None,
        help="Maximum concurrent uploads (harbor publish default: 50)",
    )
    submit.add_argument(
        "--dry-run",
        action="store_true",
        help="List the tasks that would be published and exit",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> None:
    args = build_parser().parse_args(argv)
    if args.command == "generate":
        _run_generate(args)
    elif args.command == "submit":
        _run_submit(args)


def _run_generate(args: argparse.Namespace) -> None:
    if not 1 <= args.tasks <= MAX_TASKS_PER_SKILL:
        raise SystemExit(f"-n/--tasks must be between 1 and {MAX_TASKS_PER_SKILL}")
    if args.workers < 1:
        raise SystemExit("-j/--workers must be positive")
    source = args.path.expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"path does not exist: {source}")
    output_root = args.out.expanduser().resolve()
    run_dir = (default_runs_root() / new_run_id()).resolve()
    specs = discover_skills(source, output_root, run_dir)
    if not specs:
        raise SystemExit(f"no SKILL.md found under: {source}")

    runner = ContainerizedCodexRunner(
        model=args.model,
        reasoning_effort=args.effort,
        auth_json=Path(os.environ.get("CODEX_HOME", "~/.codex")) / "auth.json",
        max_parallel_workers=args.workers,
    )
    try:
        with console.status("Preparing generator image (latest Codex CLI)..."):
            runner.prepare()
    except GeneratorError as exc:
        raise SystemExit(f"generator setup failed [{exc.code}]: {exc}") from exc
    except KeyboardInterrupt:
        raise SystemExit(130)

    config = BatchConfig(
        input_root=source,
        output_root=output_root,
        run_dir=run_dir,
        model=runner.model,
        reasoning_effort=runner.reasoning_effort,
        codex_version=str(runner.codex_version),
        generator_image=str(runner.image),
        tasks_per_skill=args.tasks,
        max_parallel_workers=args.workers,
        resume=args.resume,
    )
    tracker = create_batch_tracker(config, specs)
    runner.tracker = tracker
    console.print(
        f"[bold]{len(specs)}[/bold] skill(s) × [bold]{args.tasks}[/bold] task(s) · "
        f"{runner.model} ({runner.reasoning_effort}) · codex {runner.codex_version}\n"
        f"[dim]run state and logs: {run_dir}[/dim]"
    )
    try:
        summary = _run_batch_with_progress(config, specs, runner, tracker)
    except KeyboardInterrupt:
        raise SystemExit(130)
    _print_summary(summary, output_root, run_dir)
    if not summary.get("retained_tasks"):
        raise SystemExit(2)
    if not summary.get("acceptance_gate", {}).get("passed", False):
        raise SystemExit(1)


def _run_batch_with_progress(
    config: BatchConfig,
    specs: List[Any],
    runner: ContainerizedCodexRunner,
    tracker: RunTracker,
) -> Dict[str, object]:
    """Run the batch while rendering one overall progress line from tracker state."""
    progress = Progress(
        TextColumn("[bold cyan]generating[/bold cyan]"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total} jobs"),
        TextColumn("[dim]{task.fields[detail]}[/dim]"),
        TimeElapsedColumn(),
        console=console,
    )
    task_id = progress.add_task(
        "generate", total=len(tracker.manifest["jobs"]), detail="starting"
    )

    def on_status(payload: Dict[str, Any]) -> None:
        jobs = payload.get("jobs", {})
        running = [job_id for job_id, job in jobs.items() if job.get("status") == "running"]
        planning = sum(1 for job_id in running if ":planner:" in job_id)
        counts = payload.get("counts", {})
        retained = sum(
            1
            for job_id, job in jobs.items()
            if ":creator:" in job_id and job.get("status") == "succeeded"
        )
        detail = (
            f"planning {planning} · creating {len(running) - planning} · "
            f"retained {retained} · "
            f"failed {counts.get('failed', 0) + counts.get('cancelled', 0)}"
        )
        progress.update(task_id, completed=int(payload.get("terminal_jobs", 0)), detail=detail)

    tracker.on_status = on_status
    try:
        with progress:
            return BatchRunner(config, specs, runner, tracker).run()
    finally:
        tracker.on_status = None


def _print_summary(summary: Dict[str, Any], output_root: Path, run_dir: Path) -> None:
    attempts = list(summary.get("attempts", []))
    attempt_counts: Dict[str, int] = {}
    for attempt in attempts:
        status = str(attempt.get("status"))
        attempt_counts[status] = attempt_counts.get(status, 0) + 1
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_row("skills", _format_counts(summary.get("status_counts", {})))
    table.add_row("tasks retained", f"[green]{summary.get('retained_tasks', 0)}[/green]")
    table.add_row("tasks rejected", _format_counts(
        {key: value for key, value in attempt_counts.items() if key != "retained"}
    ) or "0")
    table.add_row("output", str(output_root))
    table.add_row("run state", str(run_dir))
    console.print(table)
    failures = [item for item in summary.get("failures", []) if isinstance(item, dict)]
    for item in failures[:10]:
        reason = " ".join(str(item.get("reason") or "").split())
        console.print(
            f"  [red]✗[/red] {item.get('skill')} [{item.get('reason_code')}] {reason[:200]}"
        )
    if len(failures) > 10:
        console.print(f"  … {len(failures) - 10} more in {run_dir / 'summary.json'}")


def _format_counts(counts: Dict[str, Any]) -> str:
    return ", ".join(f"{key} {value}" for key, value in sorted(counts.items()))


def _run_submit(args: argparse.Namespace) -> None:
    if args.concurrency is not None and args.concurrency < 1:
        raise SystemExit("--concurrency must be positive")
    try:
        returncode = submit_tasks(
            args.paths,
            org=args.org,
            tags=args.tag,
            public=args.public,
            concurrency=args.concurrency,
            dry_run=args.dry_run,
        )
    except SubmitError as exc:
        raise SystemExit(f"submit failed: {exc}") from exc
    if returncode != 0:
        raise SystemExit(returncode)


if __name__ == "__main__":
    main()
