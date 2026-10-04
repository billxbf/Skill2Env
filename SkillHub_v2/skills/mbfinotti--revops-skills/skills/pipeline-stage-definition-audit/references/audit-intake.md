# Audit Intake

Look at the data before talking to anyone - it doesn't negotiate. Then interview to explain what the data shows.

## Artifact checklist

Collect before judging any stage:

- Stage list with each stage's written definition, exactly as documented. No written definitions is itself a Critical finding - record it, don't reconstruct silently.
- Stage-change history export (from-stage, to-stage, date, actor) for the trailing 2-4 quarters.
- Forecast-category mapping per stage.
- Required fields per stage, validation rules, and every automation or workflow keyed to a stage value (these break during migration if unaudited).
- 20-30 recent closed-won and closed-lost deals, with loss reasons if captured.
- Current open deals per stage (count and value).
- Close-date change history, if the system tracks it.
- Pipeline inventory: how many pipelines exist and which motions share one. Multiple motions sharing one stage list is a common root cause.
- Any published process documentation. Benchmark it against what a complete stage document contains - GitLab's public commercial sales handbook is the exemplar structure: per stage, a definition, who's involved, typical activities, system/validation-rule enforcement, exit criteria, and cross-links to adjacent process docs (qualification framework, forecasting definitions).

How to collect it:

- **System queryable directly:** pull these first-hand and confirm the pull with the user.
- **Otherwise:** request exports and work from samples.

### When the full set is unobtainable

The stage list with its written definitions is a gate, not a menu item - without it there is nothing to audit, and its absence is itself the Critical finding. Rank only what remains, by evidence of subjective staging bought per export the user has to go and obtain:

- value (evidence strength, most first): `stage-change history > closed deal samples > stage-keyed automations and validation rules > forecast-category map > close-date change history > open-deal counts per stage`
- effort (most first): `stage-change history > stage-keyed automations and validation rules > close-date change history > closed deal samples > forecast-category map > open-deal counts per stage`
- efficiency (best first): `closed deal samples > forecast-category map > stage-change history > open-deal counts per stage > stage-keyed automations and validation rules > close-date change history`

What this order starves is the stage-change history export. It carries the per-rep variance split, the single sharpest evidence that definitions are applied subjectively, and it is also the export an admin is slowest to produce. A ratio therefore defers it, and the audit ends up arguing subjectivity from anecdote.

Promote it to first whenever the trigger symptom is managers disagreeing on staging or a forecast miss nobody can explain: those two questions have no answer without it.

Strike the automation and validation-rule inventory from the request list, and say it is struck, when the Interview has already ruled out any migration rung: it is remediation input, not audit evidence, and requesting it anyway spends the admin's goodwill on work that will not ship.

## Interview guide

Interview after the first data pass, so questions target observed anomalies. Three reps minimum, plus managers, the admin/RevOps owner, and finance.

**Reps (3+, plus a walkthrough of 2+ recently won deals each):**

- Walk me through this won deal: what did the buyer actually do, in order, from first conversation to signature?
- At each stage move, what made you decide it was time? What evidence did you have?
- Which stage do you find ambiguous - where could this deal have sat in either of two stages?
- Which fields do you fill in because they're required rather than because they're true?

**Sales managers:**

- Where do pipeline reviews break down - which stages trigger the longest debates?
- Which forecast categories do reps misuse, and in which stages?
- Which fields are usually blank? Where do deals stall by segment?
- For a sample of 10 open deals: without conferring with the deal owner, is each deal correctly staged? (This seeds the inter-rater baseline.)

**RevOps / CRM admin:**

- What is keyed to stage values today - automations, validation rules, dashboards, integrations?
- What happened the last time stages changed? What broke?
- How does the system record stage history, and does duration reporting count re-entries?

**Finance:**

- How is CRM stage data consumed in the forecast that reaches leadership - direct, or reconciled in a separate rollup?
- What would need to be true for finance to trust stage-weighted pipeline directly?

## Ownership map

Confirm before proposing changes - a correct fix with no approver ships never:

- **RevOps** (or Sales Ops where no RevOps function exists) typically owns the definitions and governance layer.
- **Sales leadership** sponsors outcomes and adoption expectations; it does not administer the picklist.
- **CRM admin/IT** owns technical implementation and validation rules.
- **Finance** consumes stage data for the official forecast and must sign off on anything that changes forecast-category rollups.
- **Marketing Ops / CS Ops** own the handoff points feeding the first stage and following closed-won.

Ask explicitly: who approves a stage-definition change here? If no one can answer, record it as a governance finding - the audit's recommendations need an owner and an approval path to land.
