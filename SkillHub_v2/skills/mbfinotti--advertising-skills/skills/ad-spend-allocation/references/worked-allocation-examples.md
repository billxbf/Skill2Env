# Worked allocation examples

Illustrative numbers - recalibrate every figure against the account's own data. What matters is the shape of the reasoning, not the amounts.

## Worked example 1 - B2C e-commerce, $60K/month, monthly reweight

Context from interview: 55% contribution margin → break-even ROAS ≈ 1.82. Measurement maturity 9/15 (no incrementality tests - all marginal estimates are directional proxies, plan says so). Approver: head of growth, max one-cycle movement 20% of total.

Gates: all five current lines clear payback; Google brand search flagged at the data-basis gate - its 11x is platform-reported, and brand search is the canonical incrementality offender, so it is capped pending a holdout test rather than trusted.

| Line              | Current     | Proposed    | Rationale (marginal evidence)                                                                                    | Expected effect                                         | Uncertainty                      | Rollback threshold                 | Verify |
| ----------------- | ----------- | ----------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------- | ---------------------------------- | ------ |
| Meta prospecting  | $24,000     | $28,000     | Penetration 18% → headroom; last +15% step held CPA within 8% of target                                          | +55-70 orders/mo                                        | Medium - stepped-increment proxy | Blended MER < 2.6 for 2 wks        | Day 30 |
| Meta retargeting  | $12,000     | $9,500      | 34% of Meta spend on retargeting inflates blended ROAS; pool refill depends on prospecting                       | Blended ROAS dips, total orders flat-to-up              | Medium                           | New-customer orders -10%           | Day 30 |
| Google non-brand  | $10,000     | $12,500     | Lost impression share (budget) 41% → budget-responsive headroom                                                  | +18-25 orders/mo                                        | Low-medium                       | CPA > 1.3x target                  | Day 30 |
| Google brand      | $8,000      | $5,000      | Platform 11x untrusted (data-basis gate); holdout test commissioned this cycle                                   | Revenue impact expected minimal if near-non-incremental | High - that is why the test      | Tracked branded-search revenue -8% | Day 45 |
| TikTok experiment | $6,000      | $5,000      | Bounded test, cycle 2 of 3: hypothesis "CPA within 1.5x Meta's marginal CPA"; decision date day 60; stop if > 2x | Learning, not volume                                    | High, bounded                    | Spend cap only                     | Day 60 |
| **Total**         | **$60,000** | **$60,000** | Fixed total - sums exactly                                                                                       |                                                         |                                  |                                    |        |

Sequence check:

- Commitments reserved: none.
- Proven marginal contributors protected: Meta prospecting, Google non-brand.
- Experiment bounded: TikTok.
- No idle contingency.
- Defunded lines are the weakest _marginal_ opportunities (saturating retargeting, unverified brand search), not the worst average performers.

Largest single move is 37% of the brand line but 5% of the total; step sizes on growing lines held to 15-25%.

## Worked example 2 - B2B SaaS, $150K/quarter, quarterly resplit

Context: $28K ACV, sales cycle ~100 days → this quarter's reallocation reads leading indicators (cost per SQL, pipeline created, penetration), never last quarter's closed-won. Break-even CPL = $28,000 × 12% lead-to-close ≈ $3,360; target CPL set at $1,800 by the profitability policy owner.

Signal driving the resplit: demand capture (search + review sites) produces 62% of pipeline on 40% of budget - pipeline share exceeds budget share and search lost-IS (budget) is 35%, so capture is under-funded at the margin. LinkedIn demand creation sits at 31% 30-day penetration of a 42,000-person audience → hold band; more budget there buys the same people again.

| Line (stage)                       | Current      | Proposed     | Rationale                                                                                                                         | Rollback threshold                 | Verify |
| ---------------------------------- | ------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------ |
| Demand capture - search            | $45,000      | $58,000      | Pipeline share > budget share; lost-IS(budget) 35%                                                                                | Cost/SQL > 1.4x baseline           | Day 45 |
| Demand capture - review sites      | $15,000      | $18,000      | Same signal; category floor still cleared                                                                                         | Cost/SQL > 1.5x baseline           | Day 45 |
| Demand creation - LinkedIn         | $60,000      | $50,000      | 31% penetration = hold band; creative supply caps absorbable budget at ~$50K (10 proven ads × $5K)                                | Pipeline created -20% over 60 days | Day 60 |
| Accelerate (retargeting open opps) | $12,000      | $12,000      | Small audience, saturated; protected as proven                                                                                    | -                                  | -      |
| Revive (closed-lost) experiment    | $18,000      | $12,000      | Cycle 1 read weak: cost/SQL 2.1x baseline, but sample below 3x target CPL of spend → reduced, not killed; decision date at day 75 | Stop if > 2.5x at decision date    | Day 75 |
| **Total**                          | **$150,000** | **$150,000** |                                                                                                                                   |                                    |        |

Note what did _not_ happen: LinkedIn was not cut for having the worst average cost per SQL - its penetration band and creative-supply ceiling set the cut, and the money followed the strongest marginal signal (capture), not the biggest pipeline stage in absolute terms.

## Negative example - annotated

The tempting plan that fails review. Same B2C account as example 1:

> "Google brand is our best performer at 11x ROAS, so we're doubling it to $16K. Meta prospecting is only 2.1x, so we're cutting it to $12K and moving the rest into retargeting (4.8x). TikTok never beat Meta, so it's dead. New split effective Monday."

Line by line:

- **"Best performer at 11x"** - average, platform-reported, and brand search: three flags at once. Platform reporting overstates 1.75-2.97x, and brand search is the classic near-non-incremental line (19x → 5.7x under one published test). No incrementality evidence was even requested.
- **"Doubling it"** - a 100% step. Default increments are 15-20%; nothing here derives a larger step from account history or blast radius.
- **"Only 2.1x, so cut"** - defunds on _average_ ROAS. Prospecting at 18% penetration is plausibly the account's best _marginal_ line; the plan never asks.
- **"Moving the rest into retargeting (4.8x)"** - retargeting's high average is partly credit for demand prospecting created. Over-funding it inflates blended ROAS now and starves the pool; total conversions drop weeks later, after this plan is declared a success.
- **"TikTok never beat Meta, so it's dead"** - compared the experiment to Meta's _average_ efficiency. The right comparison is Meta's marginal efficiency - the last dollars this plan is (correctly or not) moving around. It also kills a bounded test before its decision date on a below-evidence-floor sample.
- **"Effective Monday"** - no owner, no expected effect, no uncertainty, no verification date, no rollback threshold. Not a change packet; unauditable and irreversible by design.
- Structural: the amounts are also not shown to sum to the fixed total, and no gate (payback, measurement maturity, floors, data basis) ran at all.
