# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Host-sampled instruction axes for one task.

The planner owns WHAT a task tests (its problem proposal) and the creator owns
how the world and verifier are built. The host only samples how the requester
phrases instruction.md. No axis may change what is required or verified.
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
    "novice": "new to the domain; describes goals and symptoms in plain words, not jargon",
    "practitioner": "works in the domain; uses standard terminology accurately",
    "expert": "deep domain expert; precise, assumes shared vocabulary, skips basics",
}

PERSONALITIES: Mapping[str, str] = {
    "terse": "says only what is necessary",
    "meticulous": "careful and precise",
    "impatient": "under time pressure and wants the result quickly",
    "friendly": "warm and conversational",
    "skeptical": "doubts easy answers and wants results that hold up",
}

_CATALOGS: Mapping[str, Mapping[str, str]] = {
    "tone": TONES,
    "expertise": EXPERTISE,
    "personality": PERSONALITIES,
}
_WEIGHTS: Mapping[str, Sequence[int]] = {
    "tone": (4, 3, 3, 2, 2),
    "expertise": (2, 5, 3),
    "personality": (2, 3, 2, 2, 1),
}


@dataclass(frozen=True)
class TaskAxes:
    tone: str
    expertise: str
    personality: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    def glossary(self) -> list[tuple[str, str, str]]:
        """``(axis, value, meaning)`` rows for the creator brief."""
        return [
            (axis, value, _CATALOGS[axis].get(value, ""))
            for axis, value in asdict(self).items()
        ]


def sample_axes(count: int, *, rng: random.Random | None = None) -> list[TaskAxes]:
    """Sample one independent instruction-axis set per task."""
    rng = rng if rng is not None else random.SystemRandom()

    def pick(axis: str) -> str:
        return rng.choices(list(_CATALOGS[axis]), weights=_WEIGHTS[axis], k=1)[0]

    return [
        TaskAxes(tone=pick("tone"), expertise=pick("expertise"), personality=pick("personality"))
        for _ in range(count)
    ]
