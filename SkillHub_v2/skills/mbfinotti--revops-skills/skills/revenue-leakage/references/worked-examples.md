# Worked Examples

Three examples: a B2B sales-led reconciliation, a self-serve/PLG reconciliation, and a report done wrong. Numbers are illustrative shapes, not benchmarks - every real report derives its rates from the user's own data.

## Example 1 - B2B sales-led: the qualification handoff

Mid-market funnel, one quarter's entry cohort of 400 qualified-marked leads, average deal value $18,000, historical accepted-to-close conversion 22%.

Reconciliation at the qualified -> accepted transition:

```
entered:                     400
advanced (accepted):         250
rejected with reason code:    60
disqualified (bad fit):       30
still open, in 5-day window:  10
residual (unexplained):       50   = 12.5% of entered
```

Classification of the 50-record residual, from owner and activity history:

- 20 records: passed while the receiving owner's territory was vacant. No fallback owner existed. Zero activity ever occurred. **Real leak** (ownership vacuum).
- 18 records: the pass happened as a chat message; the receiving team worked them, 6 closed, but the system never recorded acceptance. **Data-capture gap** - the funnel worked, the data did not. Instrumentation fix, no dollar figure.
- 12 records: rejected verbally in a pipeline meeting, never coded. **Data-capture gap** on the rejection path (a missing reason code, not a lost deal).

Sizing the real leak: 20 records x $18,000 x 22% onward conversion x 0.7 age haircut (cohort is a quarter old; haircut stated as an assumption from the team's own re-engagement outcomes) = **$55,440 recoverable, tagged "estimated"**. The gross figure ($360,000 of "lost pipeline") never appears.

Register entry:

```
rank 1 | qualification handoff - ownership vacuum | 20 records, owner history:
territory vacant, no fallback | real leak | $55,440 (estimated) |
owner: revenue operations | fix: fallback owner + escalation on unaccepted
records past 5 days | fix class: routing fallback + alert/escalation
```

It ranks first on effort-adjusted dollars, not on dollars alone: both fix classes are one configuration change in the system that already holds the records, so a larger leak needing a handoff redesign would still sit below it. Say that adjustment out loud above the register rather than leaving the reader to infer it from the row order.

## Example 2 - self-serve/PLG: payment failure

Subscription product, one month's cohort of 900 renewal charges, average subscription $95/month.

Reconciliation at the charge -> renewed transition:

```
entered (charges attempted):  900
succeeded:                    810
failed -> recovered:           18
failed -> cancelled by user:    9
failed -> in retry, in window: 12
residual (unexplained):        51   = 5.7% of entered
```

Classification: billing-system event history shows all 51 were payment failures whose subscriptions ended with no retry and no recovery message - the failure event was never wired to any recovery sequence. **Real leak** (involuntary churn with no dunning path). The mechanism is technical, not human - no rep owns these records, which is exactly why the leak was invisible.

Sizing: 51 subscriptions x $95 x 6 recoverable months (user's own reactivation data shows recovered payers retain ~6 months) x 55% achievable recovery (derived from the 18 recovered organically plus the user's processor retry data; tagged "estimated") = **$15,988 recoverable/cohort-month, tagged "estimated"**.

Note what is identical to Example 1: the reconciliation arithmetic, the classification step, and the recoverable (not gross) sizing. Only the leak site and the evidence type changed.

## Example 3 - the report done wrong (negative example)

A leakage report for the same B2B funnel that would fail this skill's Pass Threshold:

> "Analysis of the pipeline snapshot found 130 leads that did not convert: 60 rejected, 30 disqualified, and 40 stalled deals worth $720,000 in lost pipeline. Additionally, 85 open deals are stale (>30 days). Recommendation: sales must follow up faster. Total revenue leakage: $720,000+."

Every defect, named:

- **Counts disqualification as leakage.** The 60 rejected-with-reason and 30 disqualified records left legitimately and were recorded; including them inflates the finding and burns trust with sales.
- **Sizes gross, not recoverable.** $720,000 is the face value of stalled deals, not what a fix would recapture; finance will discount the entire report.
- **Snapshot, not cohort.** "130 leads that did not convert" mixes vintages; the residual is arithmetic noise.
- **No classification.** The 40 stalled deals were never checked against activity history - some progressed unrecorded (capture gap), some were dead-but-open (no-decision), some genuinely leaked. One number hides three different fixes.
- **Hygiene drift.** The stale-deal count is an input signal presented as a finding, with no records-to-dollars link.
- **No ranking anyone can act on.** One blended total, no fix class, no effort axis. The reader's question is never "what did we lose" but "which of these do I do first with the hours I have", and a single gross figure answers neither.
- **Blames people, not the process.** "Sales must follow up faster" names no owner, no system defect, no fix - and the owner history was never pulled to justify the blame.
