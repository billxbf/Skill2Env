# Ranking Methods

How to rank candidate signals by predictive strength without a data science team - and when to escalate to one. Every method that survives the deletion rules below runs in a spreadsheet or a few queries.

## Which method first

Run the methods in this order and stop when the register clears its Pass Threshold - each later one refines the ordering of signals the earlier ones already found, and none of them finds a signal the backtest missed:

`backtest + lift > retention curves > WoE/IV > logistic regression == Cox`

Value and effort rank these identically, so one line carries both axes. Effort in orders of magnitude, all of it analyst hours on data that already exists - no new instrumentation:

| Method                         | Effort                                                                       | What the effort buys                                                                       |
| ------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Backtest + lift (§1-2)         | a week to assemble the churned-account list once, then an hour per candidate | The shippable register: which signals precede churn and by how much                        |
| Retention curves (§3)          | an hour, on the same pull                                                    | Where the curves diverge, which estimates lead time - the attribute lift alone cannot give |
| WoE/IV (§4)                    | an hour per candidate, most of it binning judgment                           | A strength band that separates two candidates the lift numbers tie                         |
| Logistic regression / Cox (§8) | a week to fit, then a standing job to refit as the book turns over           | Exposes a candidate that only looked strong because it co-moves with a stronger one        |

Logistic regression `==` Cox because they consume the same labeled dataset, carry the same refit burden, and differ only in what they model - churn probability versus time-to-churn - not in how much churn either lets you catch earlier.

Delete, do not demote, a method the user's constraints rule out - a method parked at the bottom of a list gets attempted anyway, and its output is confidently wrong rather than obviously missing:

- **Fewer than ~50 churned accounts in 12-24 months**: drop WoE/IV, logistic regression, and Cox from the menu entirely. Report the backtest numbers as directional.
- **Nobody will refit the model after ship**: drop logistic regression and Cox at any sample size. An unrefitted model decays into a signal ranking that describes a book that no longer exists.
- **A hard date inside the next renewal cycle**: drop everything below retention curves. The first two methods answer "which signals ship" on their own.

Small samples are the norm - a 3% monthly churn book of 300 accounts produces roughly a hundred churns a year. A thin sample blocks only the math below WoE/IV; the spreadsheet stack still ships a defensible register, and produces the labeled dataset a data team will want anyway.

This ordering is a default, not a law.

Re-rank it against what you already know about the user:

- An in-house analyst who fits models weekly moves regression up two rungs.
- A book with 2,000 churned accounts and no lead-time question makes retention curves the first stop rather than the second.

## 1. Backtest against known churned accounts

Pull every churn from the period. For each, reconstruct the candidate signal's state at 30, 60, and 90 days pre-churn (120-180 for enterprise motions).

A predictive signal was already firing at those checkpoints on most churned accounts; a signal still green at 60-90 days pre-churn on most of them is a blind spot regardless of how sensible it sounds. This same pull doubles as the survivorship-bias check on any existing health score.

## 2. Churn-rate lift over base rate

The workhorse. Requires both groups - accounts that showed the signal and churned, and accounts that showed it and did not. Computing only on churned accounts yields coverage, not lift; the distinction is the most common mistake in this exercise.

```
base rate B = churned accounts / all active accounts, per outcome window
signal rate S = churned among signal-showing accounts / all signal-showing accounts
lift = S / B
```

Report in the canonical phrasing: "of accounts showing X, N% churned within the window, vs base rate B%." Also record the false-alarm side (signal-showing accounts that retained) - a 5x-lift signal firing on half the book floods whatever intervention capacity exists.

## 3. Cohort / retention-curve comparison

Split accounts into cohorts by signal presence at a point in time (or by onboarding month, plan tier, segment), then plot % still active at 30/60/90/180/365 days per cohort and compare the curves. This is the practitioner analogue of Kaplan-Meier survival analysis: it handles still-active accounts naturally instead of discarding them, and shows _when_ churn accelerates, not just whether.

A widening gap between signal-present and signal-absent curves is the visual form of lift; the point where the curves diverge estimates lead time. If statistical tooling exists, the log-rank test formalizes whether two curves genuinely differ.

## 4. Weight of Evidence / Information Value

Borrowed from credit-risk scoring; spreadsheet-computable univariate ranking, no model training required.

Per candidate variable: bin it (e.g. days-since-last-login into 0-13 / 14-29 / 30+), then per bin compute the share of all churned accounts and the share of all retained accounts falling in that bin:

```
WoE(bin) = ln( %of_churned_in_bin / %of_retained_in_bin )
IV = sum over bins of (%of_churned_in_bin - %of_retained_in_bin) x WoE(bin)
```

Interpretation bands, by convention (credit-scoring practice, not a law):

| IV         | Predictive strength |
| ---------- | ------------------- |
| < 0.02     | Not useful          |
| 0.02 - 0.1 | Weak                |
| 0.1 - 0.3  | Medium              |
| 0.3 - 0.5  | Strong              |

An IV far above this scale is a leakage warning: the "signal" is probably a consequence of the churn decision already made (a tripwire), not a leading indicator.

WoE/IV also:

- Handles missing values without imputation (missingness itself can be scored as a bin, often informative).
- Works on categorical and continuous variables alike.

## 5. Lead time and coverage - ranked attributes, not footnotes

For every churned account that fired a signal, record days between first fire and churn; the median is the signal's lead time. Coverage is the share of all past churned accounts that fired it.

Rank on the triple, lift x lead time x coverage, because each fails alone:

- A high-lift tripwire with 3 days of lead time is un-actionable.
- A 90-day-lead signal catching 8% of churns is trivia.
- Broad coverage at 1.2x lift is noise.

## 6. Divide that value score by what the signal costs to stand up

The triple is the value axis only. Complete the ratio with the effort of emitting the signal at all:

- Engineering work to instrument it.
- Data latency before it fires.
- The standing maintenance of whatever keeps it alive.

Two signals with identical lift are not the same decision when one is a query against yesterday's login table and the other needs a product event stream that does not exist. Score both, then order candidates by value per unit of effort.

Take the per-category effort estimates and the resulting default build order from the signal taxonomy reference rather than re-deriving them here; that file is where the candidate list is chosen, so the ordering lives beside the choice. Record the call in the register's `effort` line, so a later reader can see that a signal ranked below a weaker one because it cost a quarter of engineering time, not because it predicted worse.

## 7. Once any scoring model exists: precision/recall, not accuracy

Churners are a rare class, so accuracy is misleading - predicting "nobody churns" scores in the 90s on most books.

Evaluate with:

- Precision: of flagged accounts, how many churned.
- Recall: of churned accounts, how many were flagged.
- PR-AUC: when comparing model versions.

On small samples use k-fold cross-validation rather than a single train/test split - one split can give a misleading read either direction.

## 8. Logistic regression and Cox - only when the deletion rules above left them standing

- **Logistic regression** ranks signals by coefficient contribution to churn probability, controlling for the others - it exposes candidates that only looked strong because they co-move with a stronger one.
- **Cox proportional hazards** is the multivariate extension of the retention-curve comparison: it ranks covariates by their effect on time-to-churn while handling still-active accounts.
