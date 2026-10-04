# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Serializable contracts for task creation and run bookkeeping."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List, Optional


class ContractError(ValueError):
    """Raised when generated data violates a skill2env contract."""


@dataclass(frozen=True)
class FileRecord:
    path: str
    size: int
    sha256: str
    kind: str
    line_count: int = 0


@dataclass
class SkillBundle:
    id: str
    provider: str
    source_path: str
    root: Path
    entry_document: str
    name: str
    description: str
    license: str
    files: List[FileRecord]
    digest: str

    def provenance(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "provider": self.provider,
            "path": self.source_path,
            "entry_document": self.entry_document,
            "license": self.license,
            "bundle_digest": self.digest,
            "files": [asdict(item) for item in self.files],
        }


@dataclass(frozen=True)
class Artifact:
    """One public (``url``) or Skill-bundled (``path``) source suggested by the planner."""

    description: str
    url: Optional[str] = None
    path: Optional[str] = None
    revision: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Any) -> "Artifact":
        if not isinstance(data, dict):
            raise ContractError("artifact must be an object")
        description = _string(data.get("description", ""), "artifact.description")
        url = _optional_text(data.get("url"))
        path = _optional_text(data.get("path"))
        if not description or not (url or path):
            raise ContractError("artifact requires a description and a url or path")
        return cls(
            description=description,
            url=url,
            path=path,
            revision=_optional_text(data.get("revision")),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {key: value for key, value in asdict(self).items() if value is not None}


@dataclass(frozen=True)
class Proposal:
    """One independent problem proposal written by the planner for one creator."""

    id: str
    title: str
    capability: str
    environment: str
    problem: str
    skill_approach: str
    good_behaviors: tuple[str, ...]
    bad_behaviors: tuple[str, ...]
    artifacts: tuple[Artifact, ...] = ()

    @classmethod
    def from_dict(cls, data: Any) -> "Proposal":
        if not isinstance(data, dict):
            raise ContractError("proposal must be an object")
        values = {
            key: _required_string(data, key)
            for key in ("id", "title", "capability", "environment", "problem", "skill_approach")
        }
        good = _text_tuple(data.get("good_behaviors"))
        bad = _text_tuple(data.get("bad_behaviors"))
        if not good or not bad:
            raise ContractError("proposal requires good_behaviors and bad_behaviors")
        artifacts = []
        for item in data.get("artifacts") or ():
            try:
                artifacts.append(Artifact.from_dict(item))
            except ContractError:
                continue  # A malformed lead is dropped, not fatal.
        return cls(
            **values,
            good_behaviors=good,
            bad_behaviors=bad,
            artifacts=tuple(artifacts),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "capability": self.capability,
            "environment": self.environment,
            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
            "problem": self.problem,
            "skill_approach": self.skill_approach,
            "good_behaviors": list(self.good_behaviors),
            "bad_behaviors": list(self.bad_behaviors),
        }


@dataclass(frozen=True)
class Plan:
    """The planner's decomposition of one Skill into independent proposals."""

    skill_scenario: str
    notes: str
    proposals: tuple[Proposal, ...]

    @classmethod
    def from_dict(cls, data: Any, *, limit: int) -> "Plan":
        """Keep well-formed proposals (at most ``limit``) and make their ids unique."""
        if not isinstance(data, dict) or not isinstance(data.get("proposals"), list):
            raise ContractError("proposals.json must be an object with a proposals list")
        proposals: List[Proposal] = []
        seen: set[str] = set()
        rejected: List[str] = []
        for index, item in enumerate(data["proposals"]):
            try:
                proposal = Proposal.from_dict(item)
            except ContractError as exc:
                rejected.append(f"proposal {index}: {exc}")
                continue
            slug = _slug(proposal.id) or f"proposal-{index + 1}"
            unique, suffix = slug, 2
            while unique in seen:
                unique, suffix = f"{slug}-{suffix}", suffix + 1
            seen.add(unique)
            proposals.append(replace(proposal, id=unique))
            if len(proposals) >= limit:
                break
        if rejected and not proposals:
            raise ContractError("; ".join(rejected))
        return cls(
            skill_scenario=_optional_text(data.get("skill_scenario")) or "",
            notes=_optional_text(data.get("notes")) or "",
            proposals=tuple(proposals),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "skill_scenario": self.skill_scenario,
            "notes": self.notes,
            "proposals": [proposal.to_dict() for proposal in self.proposals],
        }


@dataclass(frozen=True)
class CreatorResult:
    """Private metadata written by the creator next to the task it built."""

    description: str
    required_tools: List[str] = field(default_factory=list)
    expected_artifacts: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CreatorResult":
        if not isinstance(data, dict):
            raise ContractError("creator result must be an object")
        unknown = set(data) - {"description", "required_tools", "expected_artifacts"}
        if unknown:
            raise ContractError(f"creator result has unknown fields: {sorted(unknown)!r}")
        description = _required_string(data, "description")
        required_tools = _string_list(data, "required_tools")
        expected_artifacts = _string_list(data, "expected_artifacts")
        if any(
            not PurePosixPath(artifact).is_absolute() or ".." in PurePosixPath(artifact).parts
            for artifact in expected_artifacts
        ):
            raise ContractError("expected artifacts must be absolute environment paths")
        return cls(
            description=description,
            required_tools=required_tools,
            expected_artifacts=expected_artifacts,
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class GenerationRecord:
    skill_id: str
    provider: str
    source_path: str
    status: str
    stage: str
    reason_code: Optional[str] = None
    reason: Optional[str] = None
    bundle_digest: Optional[str] = None
    task_dirs: List[str] = field(default_factory=list)
    attempts: List[Dict[str, Any]] = field(default_factory=list)
    generator_invocations: int = 0
    elapsed_seconds: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _required_string(data: Dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{key} must be a non-empty string")
    return value.strip()


def _string(value: Any, key: str) -> str:
    if not isinstance(value, str):
        raise ContractError(f"{key} must be a string")
    return value.strip()


def _optional_text(value: Any) -> Optional[str]:
    return value.strip() if isinstance(value, str) and value.strip() else None


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")[:48].strip("-")


def _text_tuple(value: Any) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()
    return tuple(item.strip() for item in value if isinstance(item, str) and item.strip())


def _string_list(data: Dict[str, Any], key: str) -> List[str]:
    """Optional list of unique non-empty strings; a missing key means empty."""
    value = data.get(key, [])
    if not isinstance(value, list):
        raise ContractError(f"{key} must be a list")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ContractError(f"{key} must contain only non-empty strings")
    result = [item.strip() for item in value]
    if len(result) != len(set(result)):
        raise ContractError(f"{key} must not contain duplicates")
    return result
