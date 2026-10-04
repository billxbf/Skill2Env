# Remediation and Rollout

Sequence the fixes by the efficiency order in SKILL.md § Remediation Order, which already carries the axes, the rungs, and what the order starves - severity grades a finding's value, not its queue position. This file supplies the mechanics each rung has to execute. Write the new exit criteria before touching any stage name - definitions first, names after; names often stop mattering once criteria are right.

## Migration mechanics - the rule that protects history

**Deactivate and add. Never rename or delete an existing stage value.**

In most CRMs, opportunity stage history is immutable and every historical record references the stage value it carried at the time. Renaming a value makes before/after reports show mismatched labels forever; deleting one can destroy historical reporting outright. There is no undo. The safe sequence:

1. Inventory everything keyed to stage values: automations, validation rules, workflows, dashboards, report filters, integrations, forecast-category mappings. Renamed or removed values break these silently.
2. Create the new stage values alongside the old ones; map old-to-new on paper first.
3. Move open deals to the new values; deactivate (never delete) the old values so no new deal can enter them.
4. Re-check the forecast-category mapping for **every** stage - new and surviving - after the change. A missed re-map skews forecast rollups while every stage name looks correct.
5. Update dashboards and reports; export/back up report definitions before the change.
6. Time the cutover for a low-traffic period, never end of quarter.

## Historical comparability

Full restatement of history is effectively blocked by platform mechanics (immutable stage history; systems that stamp stage changes at migration time, not the original date), so most teams get a **cutover date** by default. Make it deliberate:

- Document the cutover date and annotate every dashboard that spans it.
- Add a bridge field ("legacy stage" or "definition version") on open deals so cross-era cohorts can still be compared.
- Report old-definition and new-definition cohorts separately until the old cohort closes out; never blend them in one conversion number.

## Forecast rebaselining

Stage-weighted pipeline computed under new definitions is a different quantity. Capture the last old-definition forecast as a frozen baseline, tell finance the series restarts at cutover, and expect one to two periods where accuracy comparisons are noisy before the new series stands alone.

## Training and rollout

- Communicate the new criteria to reps _before_ they see them live - a criterion first encountered as a validation error gets resented, then gamed.
- Build the exit criteria into the recurring pipeline review agenda. Criteria that never come up in reviews get ignored; reps attend to what managers inspect.
- Set 30/60/90-day adoption checkpoints under either rollout shape.
- Re-run the inter-rater sample (Pass Threshold in SKILL.md) at each checkpoint; agreement is the earliest trustworthy signal, long before conversion data matures.

### Pilot versus big-bang

No strong published guidance exists for stage changes specifically - say so rather than inventing one. The ordering below is derived from the migration mechanics above, not from a source.

- value (risk avoided and time to a trustworthy signal, most first): `pilot > big-bang` - the pilot reads inter-rater agreement on one team after a single cycle, which is the earliest trustworthy signal available, and it confines a wrong criterion to that team's deals instead of the whole pipeline's.
- effort (most first): `pilot > big-bang` - the pilot runs two definitions at once behind a definition-version field, splits reporting for its length, and cuts over twice.
- efficiency (best first): `pilot > big-bang`, but only under the freeze condition below; without it the two invert.

Pilot when a team can be spared **and** its findings can be absorbed as wording changes only. Freeze the stage values before the pilot starts. A pilot whose findings force a second picklist change inside the same year costs more than the error it caught: it breaks the trend series twice, and the second break lands on data the first one already restarted.

Delete the pilot from the plan, rather than ranking it second, when no team can be spared - an organisation that cannot staff a parallel definition does not have a slower option, it has one option. Say the pilot is deleted and why, then plan a single big-bang cutover with heavy review-cadence support for a quarter. A pilot left in the plan as a nice-to-have returns as an expectation nobody resourced.

This ordering is a default, not a law, and shifts with who executes it.

- **Dedicated CRM admin:** makes the two cutovers cheap and widens the pilot's lead.
- **Pipeline small enough to re-stage by hand:** removes most of the pilot's advantage, because the whole migration is already reversible in an afternoon.

## What goes wrong

- Stage-keyed automations fire wrong or not at all because the inventory in step 1 was skipped.
- The forecast-category re-map is missed and rollups skew for a quarter before anyone notices.
- Reports spanning the cutover blend old and new cohorts into one meaningless conversion line.
- Success gets declared on logging-compliance metrics at day 14; conversion data a quarter later shows nothing changed.
- The team relapses: criteria drift back to opinion because reviews stopped inspecting them. Schedule the quarterly inter-rater re-check as a standing calendar item, not an intention.

## Optional integration note (vendor-specific)

Skip this section unless the user's platform is known. On every platform, the deactivate-and-add rule applies unchanged.

- **Salesforce:** Opportunity Stage History is retained indefinitely and cannot be selectively disabled or edited. The Stage picklist carries a Forecast Category mapping per value. Stage Duration in Opportunity History reports counts only a stage's first occurrence.
- **HubSpot:** system deal-stage timestamps cannot be backdated (migrated records stamp at migration time; use custom date properties per milestone). Moving deals across pipelines breaks time-in-stage continuity.
- **Pipedrive:** per-stage probability and rotting-days settings need explicit review after any stage change.
