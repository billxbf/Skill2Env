# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Minimal must-have static checks for creator-authored Harbor tasks.

Static validation is intentionally thin: the Harbor Oracle/NOP acceptance run is
the authoritative quality gate. These checks only stop (a) material that must
never ship (Codex credentials, private source provenance) and (b) states that
would make the Harbor acceptance run itself meaningless (missing required files,
shell syntax errors, verifier material baked into the environment image).
Small imperfections in generated data are tolerated by design.
"""

from __future__ import annotations

import math
import os
import re
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

from .models import ContractError, CreatorResult, SkillBundle
from .task_config import HarborTaskConfigError, validate_harbor_task_toml


REQUIRED_FILES = (
    "instruction.md",
    "task.toml",
    "environment/Dockerfile",
    "tests/rubric.md",
    "tests/hint.md",
    "tests/test.sh",
    "solution/solve.sh",
)
REQUIRED_DIRECTORIES = ("environment", "tests", "solution")
RUBRIC_SECTIONS = ("## Good Signals", "## Negative Signals")
MIN_INSTRUCTION_QUOTE_CHARS = 20
MIB_BYTES = 1024 * 1024
DEFAULT_MAX_TASK_SIZE_MIB = 128

# Names the environment image must never ingest: doing so leaks the verifier,
# the reference solution, or private creator state to the solving agent.
PRIVILEGED_NAMES = {
    "instruction.md",
    "rubric.md",
    "hint.md",
    "task.toml",
    "tests",
    "solution",
    "creator-result.json",
}

# Public names that would corrupt grading or leak private creator state.
# Everything else (stray logs, extra helper dirs) is tolerated.
FORBIDDEN_PUBLIC_NAMES = {
    "creator-result.json",
    "reward.txt",
    "reward.json",
}


class PostCheckError(ContractError):
    def __init__(self, errors: Sequence[str]):
        self.errors = list(errors)
        super().__init__("; ".join(self.errors))


@dataclass
class PostCheckReport:
    ok: bool
    checks: Dict[str, bool] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class TaskPostChecker:
    """Check structure, shell syntax, rubric and hint shape, Harbor schema validity, and privacy."""

    def check(
        self,
        task_dir: Path,
        *,
        bundle: SkillBundle,
        creator_result: CreatorResult | None = None,
    ) -> PostCheckReport:
        task_dir = task_dir.resolve()
        report = PostCheckReport(ok=False)
        errors: List[str] = []

        self._check_structure(task_dir, errors)
        report.checks["structure"] = not errors
        if errors:
            report.errors = errors
            return report

        dockerfile = _read_text(task_dir / "environment" / "Dockerfile", errors)

        before = len(errors)
        self._check_task_toml(task_dir / "task.toml", errors)
        report.checks["task_toml"] = len(errors) == before

        before = len(errors)
        self._check_shell(task_dir / "tests" / "test.sh", errors)
        self._check_shell(task_dir / "solution" / "solve.sh", errors)
        report.checks["scripts"] = len(errors) == before

        before = len(errors)
        self._check_rubric(task_dir / "tests" / "rubric.md", errors)
        report.checks["rubric"] = len(errors) == before

        before = len(errors)
        self._check_hint(task_dir / "tests" / "hint.md", errors)
        report.checks["hint"] = len(errors) == before

        if creator_result is not None:
            before = len(errors)
            self._check_verification_map(task_dir / "instruction.md", creator_result, errors)
            report.checks["verification_map"] = len(errors) == before

        before = len(errors)
        self._check_privacy(task_dir, dockerfile, bundle, errors)
        report.checks["privacy"] = len(errors) == before

        report.errors = errors
        report.ok = not errors
        return report

    @staticmethod
    def _check_structure(task_dir: Path, errors: List[str]) -> None:
        if not task_dir.is_dir():
            errors.append(f"task directory missing: {task_dir}")
            return
        for relative in REQUIRED_FILES:
            path = task_dir / relative
            if not path.is_file() or path.is_symlink():
                errors.append(f"required regular file missing: {relative}")
        if (task_dir / "rubric.md").exists():
            errors.append("root rubric.md is not allowed; use tests/rubric.md")
        for directory in REQUIRED_DIRECTORIES:
            path = task_dir / directory
            if not path.is_dir() or path.is_symlink():
                errors.append(f"required regular directory missing: {directory}")

        for root, directories, files in os.walk(task_dir, followlinks=False):
            root_path = Path(root)
            for name in directories + files:
                path = root_path / name
                relative = path.relative_to(task_dir)
                if path.name in FORBIDDEN_PUBLIC_NAMES:
                    errors.append(f"private/generated artifact is public: {relative}")
                if not path.is_symlink():
                    continue
                try:
                    subtree = task_dir / relative.parts[0]
                    path.resolve(strict=True).relative_to(subtree)
                except (OSError, RuntimeError, ValueError):
                    errors.append(f"symlink escapes its task subtree or is broken: {relative}")

    @staticmethod
    def _check_task_toml(path: Path, errors: List[str]) -> None:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"cannot read task.toml: {exc}")
            return
        try:
            validate_harbor_task_toml(text)
        except HarborTaskConfigError as exc:
            errors.append(str(exc))

    @staticmethod
    def _check_shell(path: Path, errors: List[str]) -> None:
        try:
            syntax = subprocess.run(
                ["bash", "-n", str(path)], capture_output=True, text=True, timeout=10
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            errors.append(f"cannot statically validate {path.name}: {exc}")
        else:
            if syntax.returncode != 0:
                errors.append(f"invalid Bash in {path.name}: {syntax.stderr.strip()}")

    @staticmethod
    def _check_rubric(path: Path, errors: List[str]) -> None:
        """Require the two rubric sections, in order, each with at least one bullet."""
        text = _read_text(path, errors)
        headings = [
            (index, line.strip())
            for index, line in enumerate(text.splitlines())
            if line.startswith("## ")
        ]
        names = [heading for _, heading in headings]
        if names != list(RUBRIC_SECTIONS):
            errors.append(
                f"tests/rubric.md must contain exactly the sections {list(RUBRIC_SECTIONS)} "
                f"in order; found {names}"
            )
            return
        lines = text.splitlines()
        bounds = [index for index, _ in headings] + [len(lines)]
        for (start, heading), end in zip(headings, bounds[1:]):
            if not any(line.lstrip().startswith(("- ", "* ")) for line in lines[start + 1 : end]):
                errors.append(f"tests/rubric.md section {heading!r} has no bullet entries")

    @staticmethod
    def _check_hint(path: Path, errors: List[str]) -> None:
        """Require one plain prose paragraph."""
        text = _read_text(path, errors).strip()
        if not text:
            errors.append("tests/hint.md is empty")
        elif re.search(r"\n\s*\n", text):
            errors.append("tests/hint.md must be a single paragraph")
        elif re.search(r"^\s*(#|[-*] |\d+[.)] |```)", text, re.M):
            errors.append("tests/hint.md must be plain prose without headings, lists, or code")

    @staticmethod
    def _check_verification_map(
        path: Path, creator_result: CreatorResult, errors: List[str]
    ) -> None:
        """Every verified metric must cite a verbatim instruction.md sentence."""
        instruction = _normalize_prose(_read_text(path, errors))
        for entry in creator_result.verification_map:
            quote = _normalize_prose(entry.instruction_quote)
            if len(quote) < MIN_INSTRUCTION_QUOTE_CHARS:
                errors.append(f"verification_map[{entry.metric}] quote is too short to trace")
            elif quote not in instruction:
                errors.append(
                    f"verification_map[{entry.metric}] quote is not in instruction.md: "
                    f"{entry.instruction_quote[:120]!r}"
                )

    @staticmethod
    def _check_privacy(
        task_dir: Path,
        dockerfile: str,
        bundle: SkillBundle,
        errors: List[str],
    ) -> None:
        for line in _dockerfile_logical_lines(dockerfile):
            if not re.match(r"^\s*(COPY|ADD)\b", line, re.I):
                continue
            lowered = line.casefold()
            if ".." in line:
                errors.append("Dockerfile COPY/ADD cannot use parent paths")
            if any(
                re.search(
                    rf"(?:^|[/\s\[\"']){re.escape(name)}(?:[/\s\]\"']|$)",
                    lowered,
                )
                for name in PRIVILEGED_NAMES
            ):
                errors.append(f"Dockerfile may ingest privileged task material: {line.strip()}")

        private_patterns = [
            (token, re.compile(re.escape(token), re.I))
            for token in (bundle.source_path, bundle.digest)
            if token
        ]
        for path in task_dir.rglob("*"):
            if not path.is_file() or path.is_symlink():
                continue
            relative = path.relative_to(task_dir)
            if path.name.casefold() == "auth.json" or ".codex" in path.parts:
                errors.append(f"task may contain Codex credentials: {relative}")
                continue
            # task.toml legitimately records the bundle digest in its metadata.
            if path.name != "task.toml":
                for _, pattern in private_patterns:
                    if _text_file_matches(path, pattern):
                        errors.append(f"task contains private source provenance: {relative}")
                        break


def completed_task_size_bytes(task_dir: Path) -> int:
    """Sum regular-file sizes in a completed public task without following symlinks."""
    total = 0
    for root, _, files in os.walk(task_dir, followlinks=False):
        root_path = Path(root)
        for name in files:
            path = root_path / name
            if not path.is_symlink() and path.is_file():
                total += path.stat().st_size
    return total


def reward_passes(value: Any) -> bool:
    """True when every numeric reward leaf equals 1 (a full pass)."""
    leaves = list(_numeric_leaves(value))
    if not leaves:
        raise ValueError("reward contains no numeric values")
    return all(math.isclose(item, 1.0, abs_tol=1e-9) for item in leaves)


def reward_mean(value: Any) -> float:
    """Mean over numeric reward leaves; used to gate NOP free partial credit."""
    leaves = list(_numeric_leaves(value))
    if not leaves:
        raise ValueError("reward contains no numeric values")
    return sum(leaves) / len(leaves)


def _numeric_leaves(value: Any) -> Iterable[float]:
    if isinstance(value, bool):
        return
    if isinstance(value, (int, float)):
        number = float(value)
        if not math.isfinite(number):
            raise ValueError("reward values must be finite")
        yield number
    elif isinstance(value, dict):
        for item in value.values():
            yield from _numeric_leaves(item)
    elif isinstance(value, list):
        for item in value:
            yield from _numeric_leaves(item)


def unmapped_reward_metrics(reward: Any, creator_result: CreatorResult) -> List[str]:
    """Reward keys the creator did not trace to the instruction (reward.txt is one metric)."""
    keys = list(reward) if isinstance(reward, dict) else []
    if keys == ["reward"]:
        return []
    mapped = {entry.metric for entry in creator_result.verification_map}
    return sorted(key for key in keys if key not in mapped)


def _normalize_prose(value: str) -> str:
    """Casefold and collapse whitespace and Markdown emphasis so quotes match prose."""
    value = re.sub(r"[`*_]", "", value)
    return " ".join(value.split()).casefold()


def _read_text(path: Path, errors: List[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        errors.append(f"cannot read {path.name}: {exc}")
        return ""


def _text_file_matches(path: Path, pattern: re.Pattern[str]) -> bool:
    overlap = ""
    try:
        with path.open("r", encoding="utf-8") as handle:
            while chunk := handle.read(64 * 1024):
                value = overlap + chunk
                if pattern.search(value):
                    return True
                overlap = value[-256:]
    except (OSError, UnicodeDecodeError):
        return False
    return False


def _dockerfile_logical_lines(value: str) -> List[str]:
    logical: List[str] = []
    current = ""
    for line in value.splitlines():
        stripped = line.rstrip()
        current += stripped[:-1] + " " if stripped.endswith("\\") else stripped
        if not stripped.endswith("\\"):
            logical.append(current)
            current = ""
    if current:
        logical.append(current)
    return logical
