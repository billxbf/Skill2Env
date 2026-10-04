# Context artifact - `revops-context.md`

One versioned file at the project root, committed with the project when it lives in git. Its existence is the cold/warm signal; its content is what the warm start reads instead of re-interviewing. Keep every field short - this file is read at every session start, so bloat taxes every session.

## Template

```markdown
# RevOps context

- **Updated**: <date> (session <n>)
- **Revenue motion**: <B2B sales-led | B2B PLG | B2C-transactional | mixed - one line of nuance>
- **CRM / system of record**: <which system is authoritative for what; who owns it day-to-day; who signs off on changes>
- **Stage set**: <current pipeline stages, one line, with a flag if definitions are contested>
- **In-flight work**: <what is being built or fixed right now, one line per item>
- **Decided**: <closed decisions, one line each - off the table>
- **Open**: <live questions, one line each>
- **Constraints**: <freeze windows, admin capacity, compliance frames, and the date the result must land by>
- **Horizon and effort ceiling**: <one-off fix | standing system - plus the hours per week, admin access and sign-off actually available>
- **Stakeholders**: <name/role → decision role: decides | consulted | informed>

## Session log

- <date> - <session goal> → <skill(s) used> → <outcome in one line>
```

## Worked example

```markdown
# RevOps context

- **Updated**: 2026-03-14 (session 4)
- **Revenue motion**: B2B sales-led, mid-market; PLG tier launching Q3
- **CRM / system of record**: CRM authoritative for deals and contacts; billing system authoritative for ARR. Owned day-to-day by Priya (RevOps analyst); changes signed off by the VP Sales.
- **Stage set**: 6 stages; exit criteria for stages 3-4 contested (rep-activity-based)
- **In-flight work**: stage exit-criteria rewrite (draft with VP Sales)
- **Decided**: keep single pipeline for both segments; no new custom fields until governance rules land
- **Open**: whether forecast categories move to buyer-evidence gating this quarter
- **Constraints**: change freeze last week of each quarter; result must land before Q1 close 2026-03-31
- **Horizon and effort ceiling**: standing system; one admin at ~4h/week; schema changes need VP Sales sign-off
- **Stakeholders**: VP Sales → decides; CFO → consulted (forecast changes); CS lead → informed

## Session log

- 2026-02-20 - map pipeline problems → pipeline-stage-definition-audit → 4 of 6 stages flagged rep-activity-based
- 2026-03-01 - draft new exit criteria → pipeline-stage-definition-audit → draft sent to VP Sales
- 2026-03-14 - pre-close hygiene pass → sales-pipeline-hygiene → 23 deals flagged, dispositions assigned
```

Why this works:

- Every field answers a question the next session would otherwise ask.
- The log line names goal, skill, and outcome so re-routing can build on it.
- Contested items are flagged, not silently smoothed over.

## Negative example - do not produce this

```markdown
# RevOps context

We are a fast-growing company modernizing our revenue operations across the
entire customer lifecycle. Our goal is operational excellence and alignment
between sales, marketing, and customer success. We use several tools. There
have been many discussions about the pipeline and various stakeholders have
opinions. Next steps: continue improving processes and revisit priorities.

## Notes

- Meeting happened on Tuesday, went well
- Figure out the CRM situation at some point
- Lots of ideas about scoring, routing, forecasting, dashboards, hiring...
```

Why this fails:

- No field answers a concrete question (which system is authoritative? who signs off? what is decided?), so the next session must re-interview anyway - the artifact exists but the start is still cold.
- "Various stakeholders have opinions" names no one and no decision role.
- The idea dump routes nowhere.
- Vague aspiration ("operational excellence") displaces the facts the router actually needs.

## Update rules

- Patch changed fields; never rewrite the whole file each session.
- Append exactly one session-log line per session, before the session ends.
- Move an item from **Open** to **Decided** only when the stakeholder with the _decides_ role has signed off - record who.
- Keep a separate ADR-style decision log only when contested decisions genuinely accumulate; until then the Decided/Open lists are the record.
