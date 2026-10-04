# Worked example: two-axis fit×readiness scoring grid

A worked pass for a fictional mid-market data-integration vendor ("Nortida", ~$40K ACV, sales-led with a self-serve entry tier). Every weight below is a directional convention adapted from published practitioner rubrics - calibrate against the user's own closed-won base before routing anything on it.

## The fit axis (0-100, slow-moving)

Built from the ICP's criteria plus the chosen signal layers. The firmographic breakdown follows a published 100-point rubric's proportions (15/10/10/5 inside a 40-point firmographic block); the rest is reweighted to Nortida's layers.

| Dimension             | Points    | Scoring notes                                                                                                                                                    |
| --------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Industry vertical     | 15        | Full points for the two verticals holding 70% of trailing-12-month ARR                                                                                           |
| Employee count        | 10        | Full points in the 200-1,000 band the closed-won analysis surfaced                                                                                               |
| Revenue band          | 10        | Proxy for budget; sourced from enrichment, refreshed quarterly                                                                                                   |
| Geography             | 5         | Serviceable regions only                                                                                                                                         |
| Technographic         | 25        | Runs a cloud warehouse (+15); runs a displaceable legacy ETL tool (+10)                                                                                          |
| JTBD / pain-point fit | 20        | Evidence the account has the job the product is hired for: relevant job postings, a stated integration project, a trigger event (funding, regulation, migration) |
| Growth signals        | 15        | Headcount growth, new market entry - expansion pressure on data infrastructure                                                                                   |
| **Deductions**        | up to -25 | Competitor multi-year contract just signed (-15) · regulated data residency the product can't meet (-10, from the ICP's disqualifiers)                           |

## The readiness axis (0-100, decaying)

Updates continuously; every signal carries an expiry so the axis decays back toward zero without fresh evidence.

| Signal                                         | Points | Expiry  |
| ---------------------------------------------- | ------ | ------- |
| Third-party intent surge on category keywords  | 30     | 30 days |
| Pricing/docs page visits (first-party)         | 25     | 30 days |
| Self-serve workspace activated (product usage) | 25     | 90 days |
| Relevant hiring (data engineering roles)       | 20     | 90 days |

## The grid and the quadrant plays

| Account           | Fit | Readiness | Quadrant  | Play                                                                 |
| ----------------- | --- | --------- | --------- | -------------------------------------------------------------------- |
| Meridian Foods    | 91  | 82        | high/high | Route to AE now, full sequence, exec touch                           |
| Cardell Logistics | 88  | 31        | high/low  | Nurture: 1:few ABM, quarterly check for trigger events               |
| Ostrow Media      | 62  | 89        | low/high  | Qualify hard before spending AE time; steer to self-serve entry tier |
| Byrne & Klee LLP  | 34  | 12        | low/low   | Disqualify; automated touch only                                     |

The play differs per quadrant - that is the entire argument for two axes. High-fit/low-readiness accounts are the long-term pipeline; low-fit/high-readiness accounts are where reps waste quarters chasing enthusiasm the economics never reward. If low-fit/high-readiness accounts keep _closing well_, that is not a scoring bug - it is an ICP drift signal to route upstream.

## Calibration pass (never optional)

Score the last 12 months of closed-won and closed-lost deals on the draft fit axis. Nortida's pass: 74% of closed-won ARR landed in the top fit quartile, and top-quartile accounts converted at roughly 3x the bottom half - the model health test passes.

If high scorers do not convert materially better than low scorers, reweight and re-run before anything routes on the score. Re-run this calibration once or twice a year, and check the cohort-bias trap each time: if the closed-won base is still dominated by the founding customer type, adjacent growth segments are being systematically under-scored.

## Negative example: the blended score

The tempting shortcut is one composite: fit and readiness averaged into a single 0-100. Then Meridian-style and Ostrow-style accounts converge on the same number: a 90-fit/35-readiness account and a 65-fit/88-readiness account both read as "≈78/100" and get worked identically, even though one needs patient nurture and the other needs hard qualification.

The blend erases exactly the information that changes the play, and reps learn to ignore the number within a quarter.

- Keep the axes separate.
- If a routing rule genuinely needs one number, multiply fit × readiness so only accounts strong on both dominate.
- Keep the two sub-scores visible on the record.
