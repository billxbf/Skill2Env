# Subject Line Test Design

How to turn a scored variant set into a test that produces a trustworthy decision. Benchmarks cited here are vendor-published and not independently audited - use them to calibrate expectations, not as targets.

## Hypothesis

Write it before drafting any variant, in this form:

> Because [observation], we believe [change] will [effect] for [audience]. We'll know when [metric].

- Weak: "Let's test a new subject line."
- Strong: "Because replies stall when subjects sound vendor-written, we believe a plain-noun internal-style subject will raise reply rate for ops leaders. We'll know when reply rate over 200+ sends per variant beats the control."

A hypothesis that cannot lose is not a hypothesis. If no result could prove it wrong, rewrite it.

## One variable, no peeking

- Test exactly one variable: the subject-line angle (or, in B2C, the subject+preheader pair as one unit). Hold sender name, send time, body, and audience constant.
- Pre-commit to sample size and duration before launch. Checking results early and stopping on an apparent winner manufactures false positives - the most common way subject tests go wrong.
- Never change a variant mid-test. A changed variant is a new test.

## Sample size and duration

Practitioner rules of thumb - useful floors, but not real power calculations, and say so to the user:

- Outbound: 200+ sends per variant for a subject-line test; 500+ per variant for a send-time test.
- List-based ESP campaigns: ~20% of the list split across test variants, winner to the remainder. On a small list this can still be underpowered.

A real power calculation needs four inputs:

- Baseline rate for the decision metric.
- Minimum detectable effect.
- Significance level (95%).
- Statistical power (80%).

- efficiency: `rule-of-thumb floor > power calculation`. The floor costs near-zero and is right often enough to plan around; the calculation costs an hour and needs a baseline rate the user may not have yet.
- Promote the power calculation when the list is large enough that the extra sends are free, or when the decision is expensive enough that shipping an underpowered result would cost more than the hour.

- Duration: at least one full week to cover day-of-week effects; 2-4 weeks is typical.
- More variants multiply the sample: 3 variants need ~1.5x the total, 4 need ~2x. At low volume, cap the test at 2-3 variants and park the rest.
- Send-timing note - the one documented B2B/B2C split: B2B avoids weekends; B2C should test weekends.

## Metric choice - the decision that breaks most tests

- Open rate has been distorted since 2021: mail-privacy features pre-fetch tracking pixels through proxies, registering phantom opens the recipient never made. Treat open rate as directional only.
- B2B cold decision metric: reply rate, positive reply rate, or meetings booked. Never call a winner on opens alone.
- B2C lifecycle: open rate is still usable as the primary read, but pair it with a downstream metric (click or conversion) so a "winner" that attracts opens and repels action gets caught.

Which of the three to actually decide on, in B2B cold:

- trust: `meetings booked > positive replies > replies > opens`
- measurement effort: `meetings booked > positive replies > replies == opens`
  - Reply count and open count are both auto-tallied in the same sequencer report.
  - Classifying replies as positive needs a human pass over each one.
  - Meetings need the CRM wired to the sequencer, an hour of setup once.
- efficiency: `replies > positive replies > meetings booked > opens`

Default to raw reply rate: auto-counted, and trustworthy enough to call a subject-line winner. Promote positive replies when reply volume is high enough that "not interested" replies could carry the win, and meetings booked when the sequencer already writes to the CRM. Opens lose on efficiency despite costing nothing, because an untrustworthy metric buys no decision at any price.

## Guardrails - stop the test if these degrade

- Unsubscribe rate: keep under 0.5%.
- Spam-complaint rate: keep under 0.1%.
- Bounce rate: any significant rise means a list or sending problem, not a subject-line result.

A variant that wins the decision metric while tripping a guardrail loses.

## Calibration benchmarks (vendor-published; trust direction, not magnitude)

| Context       | Metric          | Average                 | Good                                                                       |
| ------------- | --------------- | ----------------------- | -------------------------------------------------------------------------- |
| B2B cold      | Open rate       | ~27.7%                  | 40-45% (excellent 50%+) - per outbound-agency and prospecting-tool figures |
| B2B cold      | Reply rate      | 4-5.8%                  | 5-10% - down from 7-8% in 2020-2022; expect continued decline              |
| B2C lifecycle | Open rate       | 20-40% by sequence type | -                                                                          |
| B2C lifecycle | Unsubscribe     | -                       | under 0.5%                                                                 |
| Both          | Spam complaints | -                       | under 0.1%                                                                 |

## Test plan template

Deliver and log every test in this shape:

- **Hypothesis:** the falsifiable statement above.
- **Variants:** IDs and angles from the scorecard (all at or above the quality gate).
- **Split:** e.g. 50/50, or 20% of list for the test with winner to remainder.
- **Sample per variant:** the pre-committed number, and whether it came from a rule of thumb or a power calculation.
- **Duration:** start date, end date, minimum one full week.
- **Decision metric:** the single metric that calls the winner.
- **Guardrails:** unsubscribe, complaints, bounce - with stop thresholds.
- **Result:** winner / loser / inconclusive, with the numbers. An honest inconclusive is a valid outcome; do not torture it into a winner.
- **Next hypothesis:** what this result suggests testing next - one variable, taken from the ranked test queue in the pattern library, or an explicit "volume does not support another test".
