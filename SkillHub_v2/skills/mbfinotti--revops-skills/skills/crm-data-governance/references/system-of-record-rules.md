# Per-Field System of Record

## Designation is per field, not per system

Each field has exactly one authoritative writer; every other copy is explicitly derived. "Bidirectional sync between two systems with no designated authority is not integration; it is a race condition that produces silent overwrites" (RevOps Books) - and the root cause of most "the data is wrong" escalations.

Example map (RevOps Training) showing the per-field grain:

| Field           | Writes                                          | Reads                         |
| --------------- | ----------------------------------------------- | ----------------------------- |
| Account owner   | CRM                                             | Marketing automation, billing |
| Contract value  | Billing system                                  | CRM, warehouse                |
| Lifecycle stage | Marketing automation until SQL, then CRM        | Everything else               |
| Product usage   | Product database                                | CRM, success tools            |
| Industry        | Enrichment provider - overwrites manual entries | CRM                           |

Two patterns worth copying: authority can **hand over at a defined milestone** (lifecycle stage), and enrichment **can** be the designated authority for a specific field (industry) - a deliberate, documented exception to "never let enrichment overwrite", not a violation of it.

For each canonical entity, account, contact, opportunity, contract, subscription, invoice, product, keep a one-page record with:

- Business definition.
- Canonical system.
- Named owner.
- Replication strategy plus freshness SLA.
- Drift-detection method.
- Edge cases.
- Last-reviewed date.

When a data dispute closes, update the map - "closing the dispute without updating the map guarantees the same dispute recurs."

## Write precedence

- Default: **authoritative-source-wins per field**. Last-write-wins alone oscillates under rapid alternating updates and silently discards valid changes ("updates mysteriously reverting"); use recency only as a tie-breaker inside the authoritative system.
- **Blank never overwrites populated**, regardless of recency - a low-risk, auto-resolvable rule.
- Free-text fields (notes, context): append or concatenate, never destructive replacement.

## Replication patterns

Every governed field's sync declares one of three. This is the largest integration-cost fork in the spec, so rank it before assigning fields to it, not after. Value is freshness at the moment a decision reads the field; effort is integration engineering, standing operation, and reversibility.

- efficiency: `scheduled pull > reconciliation-only > real-time push`
- value: `real-time push > scheduled pull > reconciliation-only`
- effort: `real-time push > reconciliation-only > scheduled pull`
- compliance cost: `real-time push > scheduled pull > reconciliation-only`

Compliance cost tracks how far each pattern extends the processing map:

- Continuous push replicates personal data into another system's live store and needs a residency and processing-agreement review before it ships.
- A scheduled pull moves the same data on a scope that stays narrowable and pausable.
- Reconciliation can compare hashes and move no values at all.

1. **Scheduled pull** - value: freshness measured in hours, which is enough for every field a human reads before deciding (catalogs, analytics aggregates, firmographics). Effort: an hour to a day on a native connector or a scheduled job; the standing job is watching it run.
2. **Reconciliation-only** - value: the only pattern that _detects_ silent divergence rather than preventing it, and the only one that fits an unchangeable legacy integration. It buys nothing if nobody reads the diff. Effort: a day to build the comparison, then a standing job of human triage every cycle - which is why it costs more than scheduled pull despite moving no data.
3. **Real-time push** - value: the highest, and the only pattern that holds for a field triggering action the moment it changes (identity, owner, stage, entitlement, consent withdrawal). Effort: a week to a quarter of integration engineering, then a standing job of retries, ordering, replay, and someone on call when the queue backs up. Poorly reversible: downstream automation starts assuming the latency and breaks when a later change removes it.

Default: scheduled pull for every governed field, on the cadence its freshness SLA demands. Move a field up to real-time push when being one sync cycle stale changes an action rather than a report - a lead routed to the wrong owner, a stage change that fires automation, a consent withdrawal that cannot sit a batch behind.

What this order starves: real-time push. It is the best data quality on the page and the worst ratio, so efficiency demotes it every round. A program that only ever picks the cheap rung ships fields that are right on a report and wrong in the workflow acting on them.

The condition above promotes it; so does an integration platform already running - where an event bus or iPaaS is in place, the marginal effort of one more real-time field collapses and the ranking flips.

Delete, don't demote: no integration engineering capacity in the plan deletes real-time push from the menu outright, and every field that needed it becomes an explicitly accepted staleness risk recorded in the spec. A pattern parked at the bottom silently reappears as scope. Treat this ordering as a default that shifts with context and with who executes it.

## Enrichment write strategies

Three write modes compete for the same enrichment budget. Value is correct coverage at read time; effort is review load, schema work, and whether the replaced value can be recovered.

- efficiency: `augment > append > overwrite`
- value: `overwrite > augment > append`
- effort: `overwrite > append > augment`
- compliance cost: `overwrite > augment == append`

1. **Augment** (fill blanks only, never replace populated) - value: coverage on fields that held nothing, which is where enrichment's return actually sits, and it destroys nothing. Effort: near-zero - the provider meters per record either way, and augment adds no review load. Reversible: a source-stamped value can be blanked back out.
2. **Append** (add alongside, for multi-value fields like tech stack) - value: context a consumer still has to reconcile; it informs a decision rather than making one. Effort: an hour of schema work for the multi-value field plus value dedupe.
3. **Overwrite** (replace a populated value) - value: the highest, and unique - the only mode that can correct a stored value that is wrong, which augment can never do. Effort: the worst - human review on the identity and downstream-trigger tiers, a provenance stamp, and field history retained, because without history the replaced value is simply gone.

Augment and append tie on compliance cost because both are additive: the pre-enrichment value survives, so a provenance or erasure request can still be answered from the record. The vendor lawful-basis review they trigger is identical too - it attaches to ingesting third-party data at all, not to how the value is written. Overwrite alone destroys that answer.

Default: augment across the whole governed set. Move a field up to overwrite only when the provider is definitionally authoritative for it and the stored value carries no verification stamp - the Industry row above is exactly that case, a documented exception rather than a violation of "never let enrichment overwrite".

What this order starves: overwrite. It is the only mode that fixes a field where reality moved underneath the stored value - a rep-typed employee count, an industry recorded before a rename - and it loses every efficiency round. Promote it where field history is already retained on the governed set, which restores reversibility and collapses its effort.

Delete, don't demote: no documented lawful basis or consent for third-party enrichment of personal data deletes overwrite on those fields - and usually enrichment of them altogether - rather than ranking it last. A CRM with no multi-value field type deletes append.

The four tiers below are not a ranked menu and must not be read as one: every governed field sits in exactly one tier, so ordering them would be false precision. The tier decides which modes a field may use; the ranking above decides which of the allowed modes to reach for first.

| Tier               | Fields                              | Rule                                                                    |
| ------------------ | ----------------------------------- | ----------------------------------------------------------------------- |
| Identity           | Company name, primary email, domain | Human review always - they determine entity match                       |
| Downstream-trigger | HQ country, employee count, funding | Human approval - a wrong value silently alters automation               |
| Proprietary        | Rep notes, relationship history     | Never-touch; excluded from enrichment writes entirely                   |
| Supplementary      | Industry tags, social URLs          | Auto-apply above a confidence threshold (0.80-0.95, practitioner range) |

## Sync-loop ("flapping") detection

- Track a last-synced timestamp per record per integration. If both systems changed a record since the last sync, flag a conflict - never blind-apply either side.
- Resolve by risk tier: **low** (formatting differences, blank-vs-populated) auto-resolve; **medium** (differing values on non-critical fields) resolve and log; **high** (deletions, identity mismatches, governed critical fields) block and alert a human.
- Log every sync operation - source, target, fields changed, conflict status - so flapping shows up as a pattern in the log, not as user complaints.
