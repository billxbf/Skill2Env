# Metric spine by business model

## Table of Contents

- [Selecting the spine](#selecting-the-spine)
- [B2B contract subscription](#b2b-contract-subscription)
- [Usage / consumption-based](#usage-consumption-based)
- [PLG / self-serve](#plg-self-serve)
- [B2C / transactional / marketplace](#b2c-transactional-marketplace)
- [Stage tiering](#stage-tiering)
- [Contested definitions to lock before first ship](#contested-definitions-to-lock-before-first-ship)
- [On benchmarks](#on-benchmarks)

## Selecting the spine

The cap is the whole problem. Five to six metrics, eight absolute, means every metric admitted is another one refused - so rank candidates by decisions changed per unit of production cost, never by how standard the metric looks on a board deck.

Production cost here means analyst hours to compute, whether the systems already emit the data, how much reconciliation against finance it drags in, and how often the thing must be rebuilt. Never a currency amount.

Default order for B2B contract subscription:

- **efficiency (build first)**: pipeline coverage > win rate > recurring-revenue waterfall > retention pair (NRR/GRR) > attainment distribution > growth-plus-margin > acquisition payback > bookings/billings/recognized lines
- **value (decisions changed)**: waterfall > retention pair > coverage > payback > attainment distribution > win rate > growth-plus-margin > bookings/billings/recognized lines
- **production cost (highest first)**: payback > waterfall > bookings/billings/recognized lines > retention pair > attainment distribution == coverage == win rate > growth-plus-margin
- **compliance cost (highest first)**: recognized revenue == any figure already circulated externally > every other spine metric

Ties, justified:

- Attainment, coverage and win rate are each one query against the CRM the team already keeps, an hour, no finance dependency, rebuilt by re-running the same query. Genuinely equal cost, not an undecided call.
- Recognized revenue and an externally circulated figure tie on compliance cost because both bind the report to the auditor's basis: correcting either is a re-issue and a notice, not a footnote. Every other spine metric is an internal management number that a dated dictionary entry can redefine.

Placements worth the argument:

- Payback costs more than the waterfall because it needs everything the waterfall needs _plus_ marketing and sales spend attributed by period and segment, from a system RevOps usually does not own.
- The waterfall places third on efficiency only because its cost is shared: build it once and the retention pair, the miss decomposition, and the bridge in every future report come nearly free. Scored alone it would sit below attainment.
- Growth-plus-margin is the cheapest row on the page - finance already produces both inputs - and still near the bottom, because an arithmetic composite of two numbers the board already has changes almost no decisions by itself.
- Bookings/billings/recognized sits last as a _printed spine row_, not as work: reconcile all three every period regardless (workflow step 4), and print all three only when the bases diverge materially - multi-year contracts, ramped deals, heavy services.

Default rung: coverage, win rate, waterfall, retention pair, attainment distribution - five metrics, one finance dependency. Move up one rung when a spend-allocation decision is actually on the table this period, or a fundraise or board question turns on efficiency rather than growth.

**What this order starves**: acquisition payback and cohort retention curves - the two metrics that most change strategy and cost the most to produce. A spine picked purely on ratio ends up all velocity and no durability, which reads healthy right up to the quarter the base stops holding. Promote both when the company is past early venture, a fundraise sits within two quarters, or a warehouse already models revenue by cohort - that last one collapses their cost and promotes them automatically.

**Delete, do not demote**, when the user's data rules a metric out:

- No stable customer identity across billing and CRM, or history shorter than the retention window: delete the retention pair and cohort curves. Report the movement bridge and state that retention is not yet measurable.
- No spend attributable by period and segment: delete payback rather than shipping a blended one.
- No quota-carrying sales team: delete attainment distribution.
- Single-year contracts, no ramps, no services: delete the bookings/billings/recognized lines from the printed spine.

A ruled-out metric parked at the bottom of a menu reappears as scope the week before the board meeting.

**Re-rank, do not apply.** This order is a default, not a law - it shifts with context and with who executes it. Re-rank against everything already known about the user:

- An existing revenue model in the warehouse promotes every cohort metric.
- A board deadline landing inside the finance close demotes everything needing certification.
- An analyst team of one caps the spine at five single-system metrics.

The Interview's three scoping questions (deadline, one-off versus compounding asset, effort ceiling) decide most of this before any metric is chosen.

Standing rules, independent of the ranking:

- Same spine, same order, every period - trend readability beats novelty.
- A metric enters only by replacing one, and the swap is footnoted.
- Every spine metric must answer a question the audience will act on; a metric nobody would change a decision over is appendix material.
- Prefer bridges over nets (show the movements, not just the delta) and distributions over averages (attainment bands, deal-size spread, cohort curves).

## B2B contract subscription

Rows in efficiency order; take the first five or six that survive the deletion rules above.

| Metric                                                                                                  | Question it answers                                     | Production cost                                                                                                                      | Definition traps to lock                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pipeline coverage (unweighted) with weighted pipeline as a separate line                                | Is next period's number backed by enough real pipeline? | An hour; CRM close dates only, no finance dependency; re-run each period                                                             | Scope to deals with close dates inside the period, renewals stripped; never divide weighted pipeline by target - the coverage multiple already discounts risk, doing both discounts twice; derive the multiple from own close rates, not a circulating rule of thumb |
| Win rate (count and dollar-weighted)                                                                    | Are we converting, and does it differ by deal size?     | Near-zero; the same CRM query set as coverage                                                                                        | Denominator is decided deals only (won + lost); count vs. dollar divergence is itself a finding; in concentrated books show the rate with and without the largest deal                                                                                               |
| Recurring-revenue waterfall (beginning + new + expansion + reactivation - contraction - churn = ending) | Where did growth actually come from?                    | A standing job: every movement classified at contract level, monthly, tied to finance at close - and the input four other rows reuse | Never net expansion against contraction; monthly resolution (a quarterly bridge hides offsetting months); exclude one-time fees and services from the recurring base                                                                                                 |
| Net and gross revenue retention (trailing-12)                                                           | Does the existing base grow or shrink on its own?       | Near-zero once the waterfall exists; a week standalone                                                                               | Fixed starting cohort, new customers excluded; gross retention capped at 100%; state the window - point-in-time monthly retention is too volatile to report alone                                                                                                    |
| Quota attainment distribution                                                                           | Is the number carried by the team or by two reps?       | An hour; needs current quota per rep alongside the CRM record                                                                        | Report share at/above 100%, 70-100%, below 70%, and top-two-rep concentration - never the mean alone                                                                                                                                                                 |
| Growth-plus-profitability read (e.g. growth rate + margin)                                              | Is the growth/efficiency trade healthy?                 | Near-zero arithmetic, but gated on the finance close                                                                                 | Name the profit measure used (operating, EBITDA-style, free-cash-flow) - the choice moves the score materially; keep it constant across periods                                                                                                                      |
| Acquisition payback (gross-margin adjusted)                                                             | How fast does acquisition spend return?                 | A standing job: spend attributed and lagged from a system RevOps rarely owns, gross margin certified by finance                      | Use subscription gross margin only; lag the spend to the period that generated the revenue; split new-logo from expansion - blending hides a segment burning cash                                                                                                    |
| Bookings / billings / recognized revenue                                                                | What was committed vs. invoiced vs. earned?             | A week per period; the deferred-revenue tie is the reconciliation itself                                                             | State total-contract vs. annualized basis - multi-year totals inflate 2-3x against annualized; the three only tie via the change in deferred revenue                                                                                                                 |

## Usage / consumption-based

Keep the waterfall shape but treat the recurring base as behavioral, not contractual.

- **efficiency (build first)**: commitment/overage mix > consumption-based net retention > seasonality split > revenue run-rate
- **value**: consumption net retention > commitment/overage mix > seasonality split > revenue run-rate
- **production cost (highest first)**: consumption net retention > seasonality split > commitment/overage mix > revenue run-rate

Run-rate is the cheapest line available and still last: annualizing a recent period manufactures a contractual-looking number the business does not have, and no decision hangs on it. Delete the seasonality split when the history is shorter than two comparable cycles - without the prior year it is a guess dressed as a control, not a lower-ranked option.

- Commitment vs. overage mix, and utilization against committed capacity - straight from the billing system, an hour, no finance dependency. These are the leading indicator pipeline coverage plays in contract businesses.
- Consumption-based net retention (same-cohort revenue vs. its prior-year revenue), with the comparison window written into the dictionary - a week to build, near-zero after, and the only line that says whether usage is deepening or decaying.
- Seasonality split: separate seasonal consumption dips from health degradation before reporting either; a holiday-quarter dip reported as churn is a false alarm that costs credibility.
- Revenue run-rate (annualized recent period) with the annualization basis stated, only where the audience requires one; some usage businesses decline to report a recurring-revenue figure at all - if so, say so rather than manufacturing one.

## PLG / self-serve

The subscription spine applies, plus the funnel that feeds it.

- **efficiency (build first)**: self-serve vs. sales-assisted revenue split > conversion-to-paid cohort rate > activation rate > engagement ratio
- **value**: conversion-to-paid > self-serve/assisted split > activation > engagement ratio
- **production cost (highest first)**: activation rate == conversion-to-paid rate > engagement ratio > self-serve/assisted split

Activation and conversion tie on cost because both need the same build: product events joined to the billing record with cohort identity preserved. Once that join exists, both are near-free; neither exists before it. The self-serve/assisted split leads on efficiency only when a motion flag already sits on the revenue record - if it does not, that is a field-ownership fix first, and it drops behind the funnel rates for this cycle.

- Signups, activation, conversion to paid, expansion - each as a cohort rate, never a cumulative count.
- Self-serve vs. sales-assisted revenue split, because the two motions carry different payback and retention profiles and blending them hides both.
- Delete the engagement ratio outright where the product's natural frequency is low. A valuable low-frequency product measured against a daily/monthly ratio looks broken and invites exactly the wrong decision; remove it rather than reporting it last.

## B2C / transactional / marketplace

- **efficiency (build first)**: volume / net revenue / take rate as three lines > repeat purchase rate > cohort retention curves > contribution-margin layers
- **value**: cohort retention curves > contribution-margin layers > take rate > repeat purchase rate
- **production cost (highest first)**: contribution-margin layers > cohort retention curves > repeat purchase rate > the three volume lines

**What this order starves**: cohort curves and the deepest contribution-margin layer - the two that actually decide acquisition spend. Promote both whenever spend allocation is the decision on the table: retained customers collapse the acquisition layer, which is why retention resets the economics, and any margin layer above the acquisition line always flatters.

- Gross transaction volume, net revenue, and take rate as three separate lines - volume is not revenue, and conflating them overstates the business. Near-zero cost from the payment or ledger record.
- Repeat purchase rate over a stated window - an hour once customer identity exists; the window changes the answer materially, so the dictionary must fix it.
- Cohort retention curves with shape commentary: a curve decaying to zero, a curve that flattens, and a curve that ticks back up are three different businesses. A week to build the order history keyed to customer identity, near-zero after.
- Contribution-margin layers (product margin, then after variable fulfillment/payment/returns, then after acquisition cost): report the deepest layer, not the most flattering one. A standing job - fulfillment, payment and returns costs allocated per order, reconciled with finance.
- Delete cohort curves and repeat purchase rate when orders carry no stable customer identity (guest checkout, no accounts); report the three volume lines and contribution margin instead of a curve built on a guess.
- Delete any single lifetime-value constant rather than ranking it: inputs are interdependent and churn is behavioral, so the number is fragile in exactly the direction that flatters.

## Stage tiering

Stage deletes candidates; it does not reorder them.

- **Pre-institutional / earliest**: acquisition cost, conversion, retention signal, runway. Delete efficiency composites and attainment distribution from the menu entirely - the data to compute them honestly does not exist yet.
- **Early venture**: restore the retention pair, payback, sales-cycle and win-rate reads as the motion stabilizes.
- **Growth and later**: the full menu, ranked as above.
- Resist audience pressure to report a later stage's metrics than the data supports - an unstable metric reported to look mature restates within two quarters.

## Contested definitions to lock before first ship

Lock only the definitions touching a metric that survived selection; the rest are next cycle's work, not this one's. Write each resolution into the dictionary - every one of these is a known fight, and the only wrong answer is changing the rule between periods.

1. Reactivation: returning churned customers as new business or a separate row.
2. Netting: same-product within-period up/down movements net; cross-product movements book separately.
3. Recurring-base exclusions: one-time fees, services, variable usage in or out.
4. Contract basis: total-contract vs. annualized bookings; ramped deals at year-one or full-ramp value.
5. Retention window and cohort: trailing-12 vs. point-in-time; which segments/product lines the base includes.
6. Win-rate denominator: decided-deals-only, and period assignment by decision date.
7. Coverage scope: in-period close dates only, renewals excluded, unweighted.
8. Payback basis: margin adjustment, spend lag, new-logo vs. blended.
9. Profitability measure in any growth-plus-margin composite.
10. Repeat-purchase / retention measurement window (consumer and transactional models).

## On benchmarks

External benchmark figures age fast and shift by segment, price point, and motion. Derive every threshold (coverage multiple, healthy retention, payback target) from the team's own history first; when an external figure is quoted, date it and name its source in the deck, and never present it as a law.
