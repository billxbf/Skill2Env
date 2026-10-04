# Worked Examples

Fictional companies; structures follow the Output Shape in SKILL.md, condensed.

## Example 1 - Enterprise deal pipeline (B2B sales-led)

```
STAGE DEFINITION AUDIT - Northbeam Analytics "Enterprise" pipeline, 2026-03
Pipeline type    : deal pipeline; sales-led, $60-150k ACV, ~120-day cycle
Stage inventory  : 8 stages, definitions in a 2022 slide deck reps have not seen;
                   forecast-category map exists but unreviewed since then
Per-stage verdict:
  1 Discovery Scheduled -> "intro call booked"            -> FAIL -> Critical
  2 Discovery Done      -> "discovery call held"          -> FAIL -> Critical
  3 Demo Delivered      -> "demo completed"               -> FAIL -> Critical
  4 Champion Identified -> "rep confirmed champion"       -> FAIL -> High
  5 Proposal Sent       -> "proposal emailed"             -> FAIL -> Critical
  6 Verbal Commit       -> "buyer said yes verbally"      -> FAIL -> Medium (buyer
                            act, but unrecorded and unwitnessable)
  7 Contract Sent       -> "contract emailed"             -> FAIL -> Critical
  8 Closed Won/Lost     -> signature / loss reason        -> PASS
Buying-job map   : stages 1-3,5,7 map to no buying job (rep tasks); Validation and
                   Consensus Creation have no stage at all - the two jobs where
                   enterprise deals actually die
Diagnostics      : Proposal Sent holds 47% of open pipeline value (own-history
                   expected ~20%); conversion decay non-monotonic (stage 5->6
                   converts 18%, 4->5 converts 92% - stage 4 is a pass-through);
                   per-rep stage-4->5 conversion ranges 55-95% (subjectivity flag,
                   practitioner-consensus reading); median 71 days in Proposal Sent
Findings         : 7 records, ordered by Remediation Order (top: 5 criterion
                   rewrites, near-zero each, retiring 4 Critical and 1 High)
Remediation      : rung 1 first - rewrite all 5 rep-activity criteria as buyer acts
                   against existing fields; e.g. stage 5's exit becomes "buyer's
                   evaluation lead confirmed in writing the proposal matches their
                   authored requirements" + "buyer security review complete (doc
                   attached)" + "mutual plan co-signed with dates". Rung 3: two of
                   those criteria need an evidence-link field that does not exist.
                   Rung 4 last - collapse 8 stages to 6, deactivate-and-add, re-map
                   forecast categories for all 6, inventory of 14 stage-keyed
                   automations attached. Redefinition not promoted: stages 6 and 8
                   survive as anchors and the motion is single. Pilot with the 6-rep
                   mid-market team for one cycle, stage values frozen beforehand
Measurement      : baselines frozen 2026-03; inter-rater sample (2 managers x 15
                   deals) at day 30/60/90; conversion re-read after one full cycle
                   (~Q4 2026)
```

## Example 2 - Transaction pipeline (high-velocity, sales-assisted PLG)

```
STAGE DEFINITION AUDIT - Loopdesk "Inside Sales" pipeline, 2026-03
Pipeline type    : transaction pipeline; $2.4k ACV, 12-day cycle; self-serve funnel
                   exists separately and is OUT OF SCOPE - kept as a distinct
                   reporting construct, not merged
Stage inventory  : 5 stages, definitions in the team wiki; forecast map present
Per-stage verdict:
  1 New Signup Assigned -> "trial account routed to rep"       -> PASS (entry gate,
                            machine-recorded)
  2 Activated           -> "buyer completed setup + invited a
                            teammate" (product events)         -> PASS
  3 Demo Booked         -> "rep booked a demo"                 -> FAIL -> High
  4 Quote Accepted      -> "buyer accepted quote in portal"    -> PASS
  5 Closed Won/Lost     -> payment method charged / lapsed     -> PASS
Buying-job map   : compressed by design - Solution Exploration and Validation
                   collapse into stage 2's product events; appropriate for the
                   motion, noted rather than flagged
Diagnostics      : aging measured in days not weeks (median stage 3 dwell: 6 days,
                   flags at >9, derived from own p90); stage 3 skip rate 38% -
                   deals that skip it convert BETTER (7-day cohorts), evidence the
                   stage adds friction without information
Findings         : 2 records. Top: stage 3 is rep activity AND the motion's data
                   says it is optional - rung 1 replaces it with "buyer requested a
                   call or asked a pricing question in-app" (buyer-initiated,
                   logged); rung 4 cuts it outright
Remediation      : cut chosen over rewrite - re-ranked, not defaulted: 5 reps and a
                   12-day cycle make the migration an afternoon's work rather than a
                   quarter's, which promotes the cut above the rewrite, and the skip
                   data says the rewrite would preserve a stage carrying no
                   information. 4-stage candidate structure;
                   deactivate-and-add; no MAP or security-review criteria imported
                   from enterprise practice. Pilot deleted, not deferred: a 5-rep
                   team cannot spare a parallel definition - big-bang with two weeks
                   of review-cadence support instead
Measurement      : one full cycle = ~2 weeks, so conversion re-read at day 30;
                   inter-rater check replaced by automated-event spot audit (most
                   criteria are machine-recorded)
```

## Negative example - an audit done wrong

A consultant audits a 7-stage pipeline and, in one afternoon:

1. **Renames** "Demo Scheduled" to "Solution Validation" directly on the live picklist. The damage to before/after reporting is permanent:
   - Every historical record keeps the old label in stage history.
   - Every report spanning the change now shows two labels for one stage.
   - Three stage-keyed workflows silently stop firing.
2. Replaces the stages with **"MEDDIC 1" through "MEDDIC 6"**. The pipeline now tracks scorecard completion, not buyer position - nobody can answer "where is this buyer in their purchase?", and the qualification data lost its per-dimension fields in the process.
3. Sets a stale-deal threshold of exactly 14 days "because the industry standard is 14 days" - a vendor blog number presented as a constant, with no look at the pipeline's own dwell-time distribution.
4. Skips the forecast-category re-map. The quarter's forecast rollup silently drops the renamed stages' weighted value; finance discovers it at quarter close.
5. Declares success at day 14 because field-fill rate rose from 60% to 95%. A quarter later, per-rep conversion variance is unchanged - reps fill the fields to pass validation and stage on optimism exactly as before.

Every step above violates a rule this skill states:

- Deactivate-and-add, never rename or delete.
- Stage ≠ scorecard.
- Provenance-tag thresholds and derive them from the pipeline's own data.
- Re-map forecast categories after any change.
- Never measure success by compliance rate.
