# Worked Metric Trees

Three worked trees and one negative example. Use the one matching the user's model as the shape to imitate - the specific metrics and owners always come from the Interview, never copied wholesale.

## Table of Contents

- [Tree 1 - B2B subscription SaaS (sales-led, Series B)](#tree-1---b2b-subscription-saas-sales-led-series-b)
- [Tree 2 - B2C subscription (D2C, repeat-revenue weighted)](#tree-2---b2c-subscription-d2c-repeat-revenue-weighted)
- [Tree 3 - usage-based variant (what changes from Tree 1)](#tree-3---usage-based-variant-what-changes-from-tree-1)
- [Negative example - a "tree" that isn't one](#negative-example---a-tree-that-isnt-one)

## Tree 1 - B2B subscription SaaS (sales-led, Series B)

Top metric: **Net New ARR** (additive decomposition). NRR is reviewed beside it as the exec-level retention composite.

```
Net New ARR  [owner: CRO | additive]
= New Logo ARR + Expansion ARR − Churned ARR − Contraction ARR

├── New Logo ARR  [owner: VP Sales | multiplicative]
│   = Leads × Lead-to-Opp Conversion × Win Rate × Avg Deal Size
│   ├── Qualified Pipeline  [owner: VP Marketing]
│   │   guardrail: SQL-to-opportunity conversion
│   │   └── activity leaves: campaign-sourced leads, outbound
│   │       meetings booked (daily, team-owned)
│   ├── Win Rate  [owner: VP Sales]
│   │   guardrail: net price realization / discount depth
│   └── Avg Deal Size  [owner: VP Sales + product pricing steward]
│       guardrail: sales cycle length
├── Expansion ARR  [owner: VP Customer Success | funnel/ratio]
│   = Expansion-eligible base × Expansion rate
│   guardrail: churn rate (or NPS) - upsell pressure must not
│   damage retention
└── Churned + Contraction ARR  [owner: VP Customer Success | additive]
    ├── Gross churn  [team: CS managers]
    │   leading input: health-score coverage of at-risk base
    └── Contraction (seat/plan downgrades)  [kept separate: netting
        expansion against contraction destroys information - two
        firms with identical net growth can have opposite dynamics]
```

Reconciliation checks that make this a tree and not a list:

- The additive top ties out to the ARR waterfall finance reports; a widening unexplained gap between the tree's ARR and recognized revenue is a model defect to investigate.
- Pipeline Coverage = Qualified Pipeline / Revenue Target rides as a ratio node under New Logo ARR; required coverage is the inverse of win rate (25% win rate → 4x, 33% → 3x). Never cite 3x as a law - it is derived from the business's own close rate.
- Cycle-time chain: outbound meetings move same-day; conversion rates move within a quarter's cohorts; Net New ARR moves within the reporting period.

Altitude slices:

- board: Net New ARR, NRR, cash
- exec: the four drivers plus efficiency ratios
- each VP's team: its own branch to activity level

No level exceeds seven metrics.

## Tree 2 - B2C subscription (D2C, repeat-revenue weighted)

Top metric: **Contribution margin from retained cohorts** (the model's honest replacement for NRR - there is no contracted base, so "recurring" is behavioral, not committed).

```
Cohort Contribution Margin  [owner: GM/Head of Growth | multiplicative]
= Active Subscribers × Avg Orders per Subscriber × CM2 per Order

├── Active Subscribers  [owner: Growth | additive]
│   = Starting base + New subscribers − Cancellations
│   ├── New subscribers  [owner: Acquisition lead]
│   │   guardrail: CM3 per acquired cohort (CAC-inclusive margin) -
│   │   stops volume buying at negative unit economics
│   └── Cancellation rate  [owner: Retention lead]
│       leading inputs: cohort curve shape (curves must flatten;
│       great ones smile - a curve decaying to zero means no PMF),
│       first-order-to-second-order conversion
├── Orders per Subscriber  [owner: Retention lead]
│   guardrail: refund/return rate
└── CM2 per Order  [owner: Ops/Finance steward | additive stack]
    = Net sales − COGS − variable fulfillment/payment/returns
    (CM1 → CM2 → CM3 gets less flattering and more honest going
    down; a returning customer has near-zero CAC, so CM3 ≈ CM2 -
    retention resets the waterfall)
```

Model-specific notes:

- Prefer cohort curves and contribution-margin LTV over point-estimate LTV formulas: LTV's inputs (ARPU, churn, CAC) are interdependent, so the formula's certainty is dangerous (Bill Gurley's 2012 critique).
- DAU/MAU enters this tree only if usage frequency genuinely drives retention for the product; category medians run far below the famous 50% (e-commerce ~10%, per Gainsight), and low-frequency-but-valuable products are wrongly declared broken by it.
- Repeat purchase rate below ~20% of customers signals over-dependence on acquisition - a stage-gate trigger to reweight the tree toward retention branches.

## Tree 3 - usage-based variant (what changes from Tree 1)

Keep Tree 1's shape; swap the atoms where commitment is absent:

- Top metric becomes **consumed revenue growth**, with **RPO (remaining performance obligations)** and **committed-vs-consumed ratio** as first-class sibling nodes - the standard complements or replacements for ARR/NRR in consumption businesses (Snowflake and Twilio decline to report ARR at all).
- The retention branch tracks NRR on consumed revenue with its method disclosed (Snowflake uses a trailing-two-year cohort), plus credit burndown as the leading input under it.
- Add a seasonality annotation to the top node: consumption dips (holidays, tax season) are not health degradation, and the framework must say so or every December triggers a false alarm.
- Disclose in the definition stub whether overage/variable revenue enters NRR - an active, named debate (SaaS Metrics Standards Board), not a settled convention; whichever choice, apply it consistently.

## Negative example - a "tree" that isn't one

```
Company scoreboard (as found at a real-shaped Series A):
- ARR: $6.2M          - NPS: 41
- MQLs: 1,840/qtr     - Win rate: 24%
- Pipeline: $8.1M     - NRR: 103%
- Website sessions    - Churn: "improving"
- CAC: $9K            - Rule of 40: 31
```

Every number is individually defensible; the set fails every structural test:

- No parent/child math anywhere - nothing reconciles, so when ARR misses, nobody can say which number drove it.
- Pipeline sits beside win rate with no coverage ratio connecting them to target - the two can both look fine while the quarter fails.
- MQLs and sessions are unqualified volume metrics with no quality pair - marketing can hit both while down-funnel conversion collapses.
- Churn reported as an adjective, NRR without its GRR pair: 103% NRR over a weak GRR can mask a quarter of the base churning under expansion (a healthy NRR−GRR gap runs 15-25 points; a large gap on a low GRR is an expansion mask, not health).
- CAC with no payback or margin basis stated, Rule of 40 with no disclosure of which profit measure - the same figure can score 45 on FCF and 30 on EBITDA and both be "right".
- Nothing is owned; everything is reviewed by everyone, which is nobody.

The fix is not more metrics - it is Tree 1's structure applied to the metrics already here, with roughly a third of them struck by the stage gate.
