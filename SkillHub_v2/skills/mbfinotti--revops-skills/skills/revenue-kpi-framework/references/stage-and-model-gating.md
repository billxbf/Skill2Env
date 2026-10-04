# Stage and Business-Model Gating

The two gates every candidate metric passes before entering the framework, plus published examples and the rules for citing benchmark figures.

## Stage gate - what appears, what recedes

Governing rule:

- early-stage: a pass on efficiency metrics, not on retention
- late-stage: a pass on growth rate, not on efficiency

| Stage              | Metrics that appear                                                        | Metrics that recede / premature                   |
| ------------------ | -------------------------------------------------------------------------- | ------------------------------------------------- |
| Pre-seed / Seed    | Activation, engagement, early retention (Day 7/30), qualitative PMF signal | Rule of 40, burn multiple, unit-economics theater |
| Series A           | Growth rate, logo churn, early CAC payback, LTV:CAC baseline               | Profitability                                     |
| Series B           | NRR, fully-loaded LTV:CAC, gross margin by segment                         | Pure activation as a headline                     |
| Series C+ / Growth | Rule of 40, burn multiple, FCF margin, magic number                        | Vanity growth rate alone                          |
| Late / Pre-IPO     | Everything, with consistency; RPO for consumption models                   | -                                                 |

Application: strike premature metrics from the framework with a scheduled entry trigger ("NRR enters when 4 quarters of cohort data exist"), rather than silently omitting them. A struck metric with no re-entry condition disappears forever.

## Model gate - which conventions apply at all

ARR/NRR conventions were built for committed monthly subscriptions; they degrade as commitment weakens. Each model's anchor metrics:

| Model                   | Core retention anchor               | Core growth anchor                         | Convention notes                                    |
| ----------------------- | ----------------------------------- | ------------------------------------------ | --------------------------------------------------- |
| Seat subscription SaaS  | NRR/GRR on MRR                      | New + Expansion ARR                        | ARR conventions work cleanly                        |
| Usage/consumption       | NRR on consumed revenue; RPO        | Consumption growth, committed vs. consumed | ARR breaks; Snowflake/Twilio decline to report it   |
| Hybrid (base + overage) | Committed-base retention            | Net new committed + overage                | Must disclose overage treatment in NRR              |
| PLG / self-serve        | Activation, free-to-paid conversion | Product-qualified leads/accounts           | North Star is usage-based                           |
| Sales-led B2B           | Pipeline coverage, win rate         | New logo ARR                               | Funnel decomposition dominates the tree             |
| Marketplace             | GMV retention, liquidity            | GMV with take rate                         | GMV without take rate is vanity; revenue = the take |
| B2C transactional/D2C   | Cohort curves, repeat purchase rate | New-customer contribution margin           | CM1/CM2/CM3 stack is the efficiency spine           |

(The PLG and marketplace rows are common-practice defaults rather than a published standard - confirm them against the user's own economics.)

Required method disclosures per metric definition stub, wherever methods genuinely diverge:

- **NRR**: cohort method or formula method - the cohort method misses recently acquired customers' retention; the two are not comparable, and public "NDR" filings vary by which segments enter the base.
- **NRR with usage revenue**: whether overage/variable revenue is included - if significant and included, NRR becomes a revenue metric rather than a recurring-revenue metric (SaaS Metrics Standards Board's own framing). Either choice is defensible; silence is not.
- **ARR**: exclusions (one-time fees, services, variable usage) - annualizing a month containing services overstates ARR.
- **Rule of 40**: which profit measure (EBITDA, FCF, GAAP operating margin) - the same company can score 45 and 30 simultaneously.
- **Win rate**: denominator (all decided deals in the period) and whether count-based or dollar-weighted.
- **NRR pairing**: always present NRR with GRR - a healthy gap runs 15-25 points; NRR above 100% over GRR below 85% is an expansion mask hiding base churn.

## Published North Star examples

Illustrations for the top-of-tree discussion, not benchmarks - the attached figures are company-reported anecdote, not audited statistics:

- Spotify - time spent listening
- Airbnb - nights booked
- Slack - messages sent (teams past ~2,000 messages rarely churned)
- Facebook (early) - users adding seven friends in ten days
- Amplitude - weekly learning users sharing a learning consumed by 2+ people
- Netflix (2005) - customers queuing 3+ DVDs in their first session
- GitLab - run-rate revenue as North Star, Net ARR as the single KPI reviewed at every board meeting (the one published counter-example to "revenue is a poor North Star"; it works there because the full KPI cascade beneath it is public and owned)

Note the pattern: nearly all are leading usage proxies for revenue, one level out of direct reach.

## Benchmark citation rules

When the framework cites external figures to sanity-check a metric's range:

- Cite survey, sample size, and year with every figure. Sources differ by definition, segmentation, and vintage; blending them produces a number no survey ever published.
- Expect disagreement between surveys as normal (e.g. 2024-2025 median private-SaaS ARR growth reported anywhere from ~19% to ~25% depending on sample) - pick one source per figure and name it.
- Treat vendor-published claims ("build a tree in 90 minutes and find 3 conflicts", "X% revenue lift") as marketing; the underlying discipline can be sound while the quantified promise is unaudited.
- The 2021-2025 shift is the trend context for any efficiency figure: efficiency displaced growth as the primary lens.

- CAC payback tolerance: tightened from 18-24 months toward 12-15
- burn multiple: from ~3x tolerated to sub-1.5x expected
- NRR medians: compressed roughly 10 points across cohorts

Present any single-year figure as a point on this line, not a timeless constant.

## Altitude ladder detail (adapt per business)

A finer scaffold than the SKILL.md table for orgs with all six levels. The cadence structure (WBR/MBR/QBR rhythm) is Amazon's documented operating practice; the metric-to-altitude mapping is a starting point, not a rule:

| Altitude      | Primary metrics                                          | Cadence         |
| ------------- | -------------------------------------------------------- | --------------- |
| IC / daily    | Activity counts, input leaves                            | Daily           |
| Team          | Conversion rates, stage velocity, one owned driver input | Weekly (WBR)    |
| Department    | Driver metrics (New ARR, NRR, coverage)                  | Weekly/Monthly  |
| Function head | Composite drivers, efficiency ratios                     | Monthly (MBR)   |
| Executive     | North Star, Rule of 40, burn multiple, NRR               | Quarterly (QBR) |
| Board         | ARR growth, Net ARR, cash, Rule of 40                    | Quarterly       |

Review norms that make the cadence real:

- metrics shown with trend context (Amazon's WBR uses 6-week and 12-month views)
- owners present insights rather than reading numbers
- plan changes carry deliberate friction, a plan alterable monthly is not a plan the quarterly tier can test against
