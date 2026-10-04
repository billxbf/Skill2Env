# Validation, KPIs, Recalibration, Governance

If the model does not beat no-scoring at predicting opportunity conversion, it is decoration. Everything in this file exists to test and keep testing that claim.

## Backtest method

1. Retro-score 6-12 months of historical leads whose outcome is known; exclude leads too young to have resolved (younger than one median sales cycle).
2. Bucket into score bands - deciles on the composite, or grid cells if using the two-axis grid.
3. Compute opportunity conversion per band. Expect a roughly monotonic curve; an inversion (a lower band converting better) points at a mis-weighted signal - find it before shipping.
4. **Lift** = top-band conversion / overall unscored baseline conversion. Pass floor: **>= 2x** (this skill's practical floor - the published practitioner rule only demands beating the baseline at all, but a thin edge on clean historical data will not survive live noise).
5. **False negatives**: share of closed-won deals that scored below threshold. Above ~10-15% means the model ignores a real buying path (partner referrals, events, product-led entry) - add the path, don't lower the bar.
6. **Spot-check holdout**: manually score a handful of known records - a recently accepted MQL, a recent closed-won, a recent closed-lost, a competitor contact, a high-engagement/poor-fit contact, an existing customer. Each must land where a human would put it; the competitor and the customer must be excluded, not merely low.

## KPI set

| KPI                                        | Definition                                   | Healthy signal               | Reliability note                                                                                             |
| ------------------------------------------ | -------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Top-band lift vs unscored baseline         | Top band conversion / all-leads conversion   | >= 2x, stable                | The decisive test                                                                                            |
| Sales acceptance rate                      | Accepted MQLs / delivered MQLs               | >= 60%                       | Practitioner convention, not a researched constant; rejection above 25-30% means the model lacks real buy-in |
| MQL-to-SQL conversion                      | SQLs / MQLs                                  | Trend inside the same funnel | Never benchmark cross-company - definitions differ (see below)                                               |
| False-negative rate                        | Closed-won deals below threshold             | Trending toward 0            | The cheapest early-warning signal a model has drifted                                                        |
| Score distribution                         | % of active database above threshold         | Stable over time             | Upward creep is the inflation alarm                                                                          |
| MQL-to-opportunity / pipeline contribution | Opportunities and pipeline from scored leads | The number to report upward  | Reporting raw MQL volume instead is what triggers the Goodhart spiral                                        |

## Benchmark claims and their reliability

Quote these with their flags; several widely-cited numbers are folklore.

| Claim                                                          | Number                     | Reliability                                                                                                                                                                  |
| -------------------------------------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Respond in 5 minutes = 21x/100x more likely to qualify"       | 2007                       | Single vendor phone-outreach study from 2007, not a randomized trial; treat as an aggressive target for hand-raisers, not a universal law                                    |
| "Fewer than 1% of MQLs convert to deals"                       | <1%                        | Genuine named-analyst Forrester blog, but rests on an uncited "our research"; rhetorical ammunition, not a planning number                                                   |
| PQL conversion advantage                                       | 5x                         | Real published figure (OpenView 2020 survey, 150+ SaaS companies); the 5-10x variants in circulation are inflated restatements                                               |
| Lead scoring case study: leads to sales -52%, conversions +79% | 2012                       | Named published source (MarketingSherpa/Bersin) but quarter-over-quarter figures, routinely misquoted with qualifiers stripped                                               |
| MQL-to-SQL "benchmarks"                                        | 13%-45%                    | The spread is definitional variance, not performance variance - two companies can both be right at 13% and 42%. Compare scored vs unscored cohorts inside one funnel instead |
| Data floor for predictive scoring                              | ~500-1,000 closed outcomes | Convergent practitioner guidance plus vendor-documented minimums; reliable as an order of magnitude                                                                          |

## Recalibration cadence

Models are "one-time build, ongoing drift" by default - the cadence is what prevents it.

- **Weekly**: score distribution vs threshold (the inflation alarm).
- **Monthly**: conversion by band; per-signal driver check.
- **Quarterly**: full reanalysis on multi-quarter cohorts; re-derive weights from the updated won/lost data. PLG and high-volume B2C teams run this monthly - more data, faster drift.
- **v2 review**: booked at launch for 60 days out, before v1 ships. Non-negotiable; "we'll revisit it later" is how models freeze.
- **Off-cycle triggers**: ICP change, product launch or pricing change, score inflation (MQL volume rising while conversion falls), a cluster of false negatives, sales acceptance dropping below the agreed floor.

## Governance and versioning

- **One accountable owner**, one source of truth - marketing ops at SMB/mid-market, RevOps at enterprise scale. Shared ownership is how models rot unnoticed.
- **Document the matrix**: every signal with its points, decay, cap, rationale, and evidence; plus the list of every system feeding signals into the score.
- **Version every change** with date, author, reason, and expected effect; announce changes to sales before they land. A rep who cannot interrogate why a lead scored what it did stops acting on scores - keep the per-lead score breakdown visible in the CRM, and keep a feedback path for reps to flag scores that look wrong.
- **Consent (EU-facing teams)**: behavioral lead scoring is profiling under GDPR. Document the lawful basis, time-bound consent where used, and make consent status visible to sales before outreach.
