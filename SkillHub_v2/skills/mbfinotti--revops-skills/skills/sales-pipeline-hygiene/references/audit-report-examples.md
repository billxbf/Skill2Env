# Worked Examples

Three condensed examples: a B2B audit, a high-velocity audit, and an audit done wrong. Company names and numbers are illustrative, invented for these examples - not sourced benchmarks.

## Example 1 - B2B Mid-Market Audit

Context: sales-led pipeline, ~90-day cycle, 240 open deals, monthly audit being introduced before a QBR, ridden on the existing biweekly pipeline review.

```
PIPELINE HYGIENE AUDIT - Mid-market pipeline, as-of 2026-03-31
Definitions   : meaningful activity = stage/close date/amount change
                (ORM definition; last-activity as second trigger);
                stale multiplier 1.5-2.0x mid-market medians; inactivity
                flag 30-45d (DealHub range); legal/procurement exempt
Stale layer   : $8.1M open pipeline -> <90d: $5.2M / 90-180d: $1.6M /
                180-365d: $0.9M / >365d: $0.4M; headline coverage 3.8x ->
                3.6x excluding >365 bucket; stale value 36% of pipeline ->
                amnesty day scheduled BEFORE enforcement (over the
                20-30% line)
Summary       : 240 deals audited; 61 flagged (25%)
Exception list (excerpt):
  Deal            Owner  Flags                     Evidence                Decided disposition        Disp. owner  Reason
  Northwind ERP   J.R.   stale(51d in Eval,        no stacked signal moves Close lost: "dropped       J.R.         no answer to "what has
                         median 24d), 2nd push     since Feb 9; single-    follow-up"                              to happen"; single-thread
                                                   threaded
  Contoso Add-on  M.K.   2nd push (crossed         in legal since Mar 20;  Re-date 2026-04-18, date   M.K.         evidence moving; stated
                         quarter boundary)         champion responsive     updated in CRM same day                 reason logged on push
  Fabrikam Pilot  M.K.   missing next step         deal active, field      Keep + next step "pilot    M.K.         data gap, not deal decay
                                                   blank                   review call Apr 7"
  8 early-stage   T.S.   dibs pattern (no          created w/ no contact   Ownership to territory     Sales mgr    claim-only records
  records                meaningful change since   or next step            rules; records closed
                         creation)                                         "never a real opp (audit)"
Field gaps    : next step 58% populated vs 90-95% target (feeds Monday
                prioritization); amount 92%; loss reason 41% (feeds
                win/loss) -> fix: 2 fields un-required (cap 5-7),
                stage-gated validation rule on close date + amount
Push report   : 0 pushes 71% / 1 push 17% / 2+ 12%; all second-push deals
                reviewed by manager with stacked-signal evidence; 3
                quarter-boundary pushes, all with stated reasons
Remediation   : push-counter field added; loss-reason list rebuilt to 7
                codes w/ definitions; amnesty day Apr 3
Communication : rules memo sent Apr 2 (before first flag); exception list
                published 12h before Apr 6 pipeline review; execs excluded
                from rep sessions; outcome summary to sales org Apr 10
KPIs          : stale value 36% -> target <25% next audit; next-step 58% ->
                75% (own baseline, self-set); slipped-deal
                rate 24% -> <20%; pass: 3 of 4 criteria met; re-audit Apr 30
```

## Example 2 - High-Velocity / B2C-Adjacent Audit

Context: inside-sales transactional pipeline, 9-day median cycle, ~1,800 open deals, weekly aggregate audit - deal-by-deal review replaced by rules, per the high-velocity pattern.

```
PIPELINE HYGIENE AUDIT - Velocity pipeline, as-of week 14
Definitions   : meaningful activity = field change (identical to B2B - this
                does not vary by motion); ~1.5x stage medians of 1-3d
                (derived, 8 weeks history); inactivity flag 14d;
                push tolerance: any second date = escalation (9-day cycle
                makes a second push a cycle restart)
Method        : aggregate rules, exception-based; SLA age caps per stage
                proportional to cycle length; SLA breach -> auto-tag for
                manager review (never auto-close); scheduled auto-close
                only on the pre-qualified entry stage, referencing
                last-activity date, approved by sales leadership
Summary       : 1,812 deals; 496 tagged; bulk dispositions below $2K value
                threshold, conversations above it; 48h manager override
                window on every deal
Dispositions  : 371 bulk close-lost "aged out (audit cleanup)" (9 pulled
                back by managers in the window); 74 re-dated with evidence;
                51 kept with next step
Field gaps    : phone-validated flag 71% vs 90% target - the only
                completeness field this team's routing actually reads
KPIs          : freshness 66% -> 84% post-audit; 88% zero-push; stale value
                12% (under the 20-30% line - no amnesty needed); weekly
                cadence confirmed; pass threshold met
```

Note what did _not_ change from Example 1:

- The meaningful-activity definition.
- Classify-don't-delete.
- Validation-rules-over-required-fields.
- The override window.
- The coaching posture.

What changed:

- The unit of analysis (aggregate rules, not deal-by-deal).
- The automation degree (auto-tag plus limited pre-qualified auto-close).
- The thresholds' absolute size.

## Negative Example - The Audit Done Wrong

Context: same mid-market pipeline as Example 1, run by a new ops hire the quarter before.

What happened:

- Defined stale by logged activity: any deal with a call or email in the last 30 days passed. Reps kept dead deals "fresh" with a weekly logged voicemail; the stale layer survived the audit untouched while genuinely worked-but-slow enterprise deals got flagged.
- One flat 30-day stage threshold across segments - it flagged half of Evaluation (median 24d, so 30d is normal there) and almost nothing in the SMB motion (median 6d, where 30 days is four cycles).
- Computed "average days-in-stage" on the whole book, dead tail included, so the resulting thresholds were flattened by zombies and flagged almost nothing.
- No announcement, no amnesty despite ~40% of value being stale. Reps discovered the rules when 130 deals were mass-closed overnight, loss reason bulk-set to "Price" (first dropdown option).
- 40 records were deleted outright "to keep reporting clean". They aged out of the recycle bin; conversion baselines and two reps' win rates were permanently corrupted.
- Tied a spiff to field completion. Completeness hit 97% in two weeks - next steps read "n/a", amounts defaulted to $10,000, and every close date landed on the last day of the quarter. At quarter end, reps mass-pushed dates with no reason required, and the forecast rolled over intact.
- Success was reported as "496 hygiene issues resolved in 3 days" - clearance speed, no KPI baseline, no follow-up audit scheduled.

What it caused: reps kept real deal notes in a private spreadsheet and updated the CRM only under pressure - the audit made the data _worse_. Loss analysis showed a fictional pricing crisis. The next quarter's forecast used corrupted baselines and quarter-stuffed close dates.

Each mistake maps to a rule in this skill:

- Define meaningful activity on field changes, not logged touches.
- Segment the thresholds.
- Exclude the stale layer before computing baselines.
- Amnesty before enforcement when the stale share is high.
- Communicate before enforcing.
- Classify with honest codes, never delete, never bulk-set a reason.
- Never tie comp to field completion.
- Require stated reasons on period-boundary pushes.
- Grade on KPI movement, not clearance speed.
