---
# Draft — a decision candidate (WIP), and the ONLY template: a record is born a draft,
# and `promote` is the only door into accepted/ (it mints the counter and flips status).
# Filename:  AAAA-kebab-title.md  (AAAA = the 4 UPPERCASE letters of `id` below).
# Promotion, linking, and validation are the decision-records skill's job.
# Write the ruling, not the debate: cite the argument (References), don't restate it.
# Delete a section with nothing to say — padding, not length, is what to trim — and a
# record that keeps growing is usually several rulings sharing a file.
id: ABCD                          # REQUIRED: 4 UPPERCASE letters, a mnemonic of the topic
title: Short imperative title
type: architecture                # an open lowercase slug (architecture, product, security, …)
status: draft                     # draft | under-review
date: YYYY-MM-DD
deciders: [trung]
summary: One sentence describing the decision.
tags: []                          # e.g. [access-control, retrieval, orchestrator]
relates_to: []                    # related record IDs — counters and/or draft IDs
supersedes:                       # a decision this replaces, or blank
superseded_by:                    # ID that replaces this, or blank
---

# {id} — {title}

## Context

The tension that forces a decision, in a few sentences, as it actually is. Don't sanitize, and don't
narrate history the References already carry.

## Decision

The decision in one or two sentences, active voice ("We will …"). Binding once promoted and
`accepted` — course changes only by supersession.

## Rationale

Only what the Decision doesn't already imply — why this over the alternatives. Delete the section
when it would just repeat the Decision.

## Alternatives considered

Only options genuinely argued — never pad the table. Delete the section when nothing else was on the
table.

| Option | Why not |
| :----- | :------ |
| …      | …       |

## Consequences

What this makes better, worse, or riskier — one list, only lines someone will act on. Open questions
and pending follow-up rulings live here too.

- …

## References

Records by ID (e.g. `0001`, `TIER`), threads, memos, sources — where the full argument lives. Delete
the section when there are none.
