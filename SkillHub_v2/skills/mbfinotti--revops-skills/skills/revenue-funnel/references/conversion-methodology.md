# Conversion Assumption Methodology

How the conversion register's numbers get derived, why the vocabulary matters, and what external benchmarks are actually good for.

## Cohort vs Milestone: the Distinction Most Models Get Wrong

- **Win rate** is a _period_ metric: of opportunities that closed in a period, what share were won.
- **Close rate** is a _cohort_ metric: of opportunities created in a period, what share are ultimately won.
- **Pipeline conversion rate** is a _snapshot_ metric: the rate at which a point-in-time pipeline converts to revenue.

A single worked case (from a Kellogg planning course) shows how much the reported number depends on which measure and analysis type is picked, for the same underlying business:

- Narrow win rate: 50%
- Broad win rate: 43% vs 29%
- Close rate: 30% vs 20%

The true value only emerges once open opportunities reach terminal state. Reporting a "conversion rate" without its basis invites exactly this confusion, which is why the register's basis column is mandatory.

**Decompose the close rate over time, not just in aggregate.** Knowing a cohort eventually closes 40% of its qualified leads is less useful than knowing the timing: derive average in-quarter, first-quarter, and second-quarter close shares, ideally from 6-8 matured cohorts rather than 2. Without the decomposition, lead generation cannot be phase-lagged into bookings - a plan can be arithmetically correct while being temporally wrong.

**The lag breaks naive coverage math.** With a 30-day sales cycle, quarterly pipeline coverage is close to meaningless: roughly two-thirds of the pipeline needed to close during the quarter has not been created yet when the quarter starts.

## Deriving Historical Rates

1. Sweep stale records first: across one vendor's customer base, more than 10% of pipeline sat 12+ months without a change to stage, close date, or amount. Rates computed over that population flatter the funnel.
2. Window: every unit that _entered_ a stage over 4-8 quarters, divided into those that eventually reached the next stage. Entries, never current occupancy - occupancy undercounts slow movers already past the stage.
3. Segment before trusting: a blended rate hides exactly the differences (source mix, price point, opportunity type) that separate two funnels in the same industry. Minimum viable segmentation set is motion x segment (SMB/MM/ENT) x source (inbound/outbound/partner/PLG) x opportunity type (new/renewal/upsell/cross-sell) - four dimensions, and sample size is the real constraint. Pick the two highest-variance dimensions, hold the rest blended until volume supports splitting.
4. Opportunity type moves rates more than most teams model: new-business acquisition shows the longest cycles and lowest conversion (low single digits at the opportunity level in some published figures). Retention/expansion converts faster and far more often (healthy retained share cited around 75-85% at the engage stage). At $50-100M ARR, 58% of new ARR comes from existing customers, 67% above $100M - a pre-sale-only model governs a third of the business at that scale.

## What External Benchmarks Are For

Benchmarks trigger investigation; they never set targets. The variance across publishers is definitional incompatibility, not noise - no two sources define MQL or SQL identically, and most do not disclose whether a rate is cohort- or milestone-based. One widely cited report drew ~106 participants split 5 ways - roughly 20 per cell, which supports no real assumption. Commonly cited B2B SaaS ranges, for the sanity-check role only:

- Visitor-to-lead: 1-5%
- Lead-to-MQL: 15-30%
- MQL-to-SQL: 30-50% (wider practitioner range centers nearer 13-15%)
- SQL-to-opportunity: roughly 42-75%, depending on source
- Opportunity-to-won: 15-30%

A stage far outside these bands earns a hypothesis and a look, nothing more.

| Source type                                            | Good for                                             | Caveat                                             |
| ------------------------------------------------------ | ---------------------------------------------------- | -------------------------------------------------- |
| Practitioner surveys (e.g. Benchmarkit)                | Breadth across categories                            | Self-reported; definitions vary by respondent      |
| Long-running banker surveys (e.g. KeyBanc)             | Time series since 2010                               | Small n, lagged publication                        |
| Forrester / SiriusDecisions                            | Standardized definitions enable real peer comparison | Paywalled; requires adopting their stage set       |
| Motion-segmented lifecycle benchmarks (Bowtie-aligned) | Post-sale coverage                                   | Vendor-adjacent                                    |
| VC portfolio reports                                   | Expansion economics                                  | Portfolio selection bias                           |
| Vendor blog "20XX benchmarks" posts                    | Nothing reliable                                     | Frequently circular citations with no primary data |

## Re-benchmarking Cadence

- **Weekly** - operational monitoring only; no assumption changes.
- **Monthly** - recompute cohort rates as cohorts mature; flag drift beyond the register's tolerance band.
- **Quarterly** - re-ratify assumptions in the funnel council; version the model.
- **Trigger-based re-baseline** - ICP change, pricing change, new segment, motion change, comp-plan change, or stage-definition edit invalidates history. Reset the baseline; never blend old and new data into one number.

Validation to run alongside the cadence:

- Backtest the last 4 quarters of plan against actuals per stage.
- Hold out the most recent complete cohort rather than fitting on everything.
- Reconcile bottom-up against top-down and force the gap to be named.

Planning runs top-down and bottom-up meeting in the middle - the named gap is what surfaces an input shortfall quarters before it becomes a revenue miss.
