# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Host-sampled presentation axes for one task.

The planner owns WHAT a task tests (its problem proposal); the host only
samples HOW it is presented and how big it is. Four axes shape instruction.md
alone (tone, expertise, personality, context_detail); two shape the
environment (complexity, environment_noise). None of them may change what the
verifier accepts.
"""

from __future__ import annotations

import random
from dataclasses import asdict, dataclass
from typing import Mapping, Sequence


TONES: Mapping[str, str] = {
    "first_person_ask": "a first-person request explaining what the requester needs and why",
    "imperative_brief": "a short, direct imperative brief",
    "ticket_snippet": "an issue-tracker ticket with a title, short body, and acceptance notes",
    "chat_message": "an informal chat message to a colleague",
    "example_driven": "a request anchored on one concrete example of the desired outcome",
}

EXPERTISE: Mapping[str, str] = {
    "novice": "new to the domain; describes symptoms and goals in plain words, not jargon",
    "practitioner": "works in the domain; uses standard terminology accurately",
    "expert": "deep domain expert; precise, assumes shared vocabulary, skips basics",
}

PERSONALITIES: Mapping[str, str] = {
    "terse": "says only what is necessary",
    "meticulous": "careful and precise; spells out hard constraints",
    "impatient": "under time pressure and wants the result quickly",
    "friendly": "warm and conversational",
    "skeptical": "doubts easy answers and wants results that hold up",
}

CONTEXT_DETAILS: Mapping[str, str] = {
    "minimal": "states the goal and hard constraints only; the solver discovers the rest",
    "moderate": "adds the relevant background a requester would naturally mention",
    "rich": "adds background plus observed symptoms, prior attempts, or why it matters",
}

# Complexity is the expected number of tool-calling turns (one shell command or
# file edit per turn) a competent terminal agent needs from the pristine state.
COMPLEXITY_TURNS: Mapping[str, str] = {
    "easy": "5-10",
    "medium": "10-20",
    "hard": "20+",
}

ENVIRONMENT_NOISE: Mapping[str, str] = {
    "clean": "only material relevant to the problem",
    "realistic": "the incidental files, history, and data a real workspace of this kind carries",
    "noisy": "realistic workspace plus plausible distractors: stale notes, unrelated logs or data, "
    "and near-miss files the solver must recognize as irrelevant",
}

_WEIGHTS: Mapping[str, Sequence[int]] = {
    "tone": (4, 3, 3, 2, 2),
    "expertise": (2, 5, 3),
    "personality": (2, 3, 2, 2, 1),
    "context_detail": (3, 4, 3),
    "environment_noise": (2, 5, 3),
}


def complexity_label(level: str) -> str:
    """Human-readable tag such as ``medium (solvable in 10-20 turns)``."""
    turns = COMPLEXITY_TURNS.get(level)
    return f"{level} (solvable in {turns} turns)" if turns else level


@dataclass(frozen=True)
class TaskAxes:
    complexity: str
    environment_noise: str
    tone: str
    expertise: str
    personality: str
    context_detail: str

    def to_dict(self) -> dict[str, str]:
        value = asdict(self)
        value["complexity"] = complexity_label(self.complexity)
        return value

    def glossary(self) -> list[tuple[str, str, str]]:
        """``(axis, value, meaning)`` rows for the creator brief."""
        catalogs = {
            "complexity": {
                level: f"a competent agent needs {turns} tool-calling turns"
                for level, turns in COMPLEXITY_TURNS.items()
            },
            "environment_noise": ENVIRONMENT_NOISE,
            "tone": TONES,
            "expertise": EXPERTISE,
            "personality": PERSONALITIES,
            "context_detail": CONTEXT_DETAILS,
        }
        return [
            (axis, value, catalogs[axis].get(value, ""))
            for axis, value in asdict(self).items()
        ]


def sample_axes(count: int, *, rng: random.Random | None = None) -> list[TaskAxes]:
    """Sample one axis set per task; complexity is stratified across the skill's tasks."""
    rng = rng if rng is not None else random.SystemRandom()
    levels = list(COMPLEXITY_TURNS)
    complexities: list[str] = []
    while len(complexities) < count:
        cycle = levels[:]
        rng.shuffle(cycle)
        complexities.extend(cycle)

    def pick(axis: str, catalog: Mapping[str, str]) -> str:
        return rng.choices(list(catalog), weights=_WEIGHTS[axis], k=1)[0]

    return [
        TaskAxes(
            complexity=complexities[index],
            environment_noise=pick("environment_noise", ENVIRONMENT_NOISE),
            tone=pick("tone", TONES),
            expertise=pick("expertise", EXPERTISE),
            personality=pick("personality", PERSONALITIES),
            context_detail=pick("context_detail", CONTEXT_DETAILS),
        )
        for index in range(count)
    ]
