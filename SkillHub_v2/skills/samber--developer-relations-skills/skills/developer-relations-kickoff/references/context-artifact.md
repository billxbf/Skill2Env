# Context artifact

`devrel-context.md` lives at the project root and is committed with the project when the project lives in git. One file, versioned, readable by teammates. It is what makes the next session a warm start.

## Template

```markdown
# DevRel context

_Last updated: YYYY-MM-DD_

## Product and audience

- Product: what it is, and what a developer does with it.
- Adoption motion: individual self-serve / organization buys / both / non-commercial OSS.
- Primary segment, secondary segment, anti-segment (from `samber/developer-relations-skills@developer-segmentation` if it has run).

## Program

- Funded driver: adoption / sales enablement / enablement / product input / ecosystem / contributor community / employer brand.
- Pillar mix: advocacy, marketing, enablement, community - with rough weight each.
- Stage and team: who does this work and for how many hours a week.

## Surfaces owned

- Docs: URL, generator, who can merge.
- Repositories: which ones are public and who maintains them.
- Community: venue and rough size.
- Events: what is committed this year.
- Content: where it publishes and who reviews it.

## Measurement

- Metrics currently reported, and where each number comes from.
- Known blind spots.

## State

- In flight: work started and not finished.
- Decided: settled calls, not to be re-litigated.
- Open: live questions.
- Constraints: budget, hours, review bottlenecks, legal or security gates.

## Stakeholders

- Name or role - decision rights on what.

## Session log

- YYYY-MM-DD - session goal → skill routed to → what changed here.
```

## Worked example (excerpt)

```markdown
## Product and audience

- Product: an open-source Go library for typed job queues; a hosted control plane is planned but unbuilt.
- Adoption motion: individual self-serve today; the hosted plane will introduce an organization buyer.
- Primary segment: backend engineers at 10-200 person product companies already running Postgres.
  Anti-segment: data engineers looking for a workflow orchestrator - written off deliberately.

## Program

- Funded driver: contributor community, with adoption second. No revenue attached yet.
- Pillar mix: community 50%, enablement 30%, advocacy 20%, marketing 0%.
- Stage and team: one maintainer, roughly six hours a week, no budget.

## State

- In flight: CONTRIBUTING rewrite started 2026-08-14, good-first-issue queue still empty.
- Decided: Apache-2.0, DCO not CLA, no Discord before 500 stars.
- Open: whether v1 ships before or after the hosted plane.
- Constraints: maintainer hours only; no engineering support for docs.

## Session log

- 2026-08-21 - "nobody contributes" → `samber/developer-relations-skills@oss-contributor-onboarding` → added constraints, decided DCO.
```

## Negative example - what not to write

```markdown
## Program

- Goals: grow the community, increase adoption, improve docs, more content, better metrics,
  build a brand, get to 10k stars, launch a Discord, speak at more conferences.
- Constraints: we should be careful with time.
- Decided: TBD
```

- Every goal is claimed, so none is prioritized and every activity scores identically.
- The constraint is unfalsifiable, so no skill can plan against it.
- `TBD` in a decided field means the next session re-asks a question that was probably already answered out loud.

Write the number of hours, name the one driver, and leave a field out entirely rather than filling it with a placeholder.
