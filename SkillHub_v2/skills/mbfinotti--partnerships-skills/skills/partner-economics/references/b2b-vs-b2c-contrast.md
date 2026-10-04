# B2B vs B2C Partner Economics

## What is identical

The method does not change: attributable revenue minus fully-loaded partner cost, against partner CAC, over a lifetime, adjusted for incrementality. Never rebuild the method per side; only re-parameterize it.

The discipline rules carry over too:

- Sourced/influenced separation.
- Margin-based LTV.
- Incrementality never assumed.
- Benchmarks labeled by evidence class.

One structural note worth knowing: the B2B channel/alliance literature and the B2C affiliate/creator literature are two largely separate practitioner bodies that do not cross-cite each other. Expect no shared vocabulary between a channel chief and an affiliate manager describing the same math.

## What genuinely differs

| Dimension                | B2B channel/alliance                                                                                                                                                                                                                                                                                                                                                                       | B2C affiliate/creator                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Unit of analysis         | Partner firm; few, large, negotiated                                                                                                                                                                                                                                                                                                                                                       | Creator/publisher; thousands, self-serve                                   |
| Money flow               | Discount off list, rebates, MDF, marketplace fees, royalties                                                                                                                                                                                                                                                                                                                               | CPA per action or revenue share on recurring                               |
| Deal economics floor     | Two thresholds, not one: a VAR/SI's own margin starts covering their acquisition and delivery around ~$20K ACV, but the vendor can only fund the full reseller/SI motion from ~$50K. Referral/MSP motions work down to ~$5K ACV. All blog-tier and unaudited; `mbfinotti/partnerships-skills@partner-channel-program` owns the ACV band table - cite it rather than restating a floor here | Works at any price point; per-action payout scales down                    |
| Ramp and enablement cost | 6-12+ months of double cost, certification, dedicated headcount                                                                                                                                                                                                                                                                                                                            | Near zero; activation is instant, enablement is a creative kit             |
| Attribution              | Deal registration, CRM opportunity tagging, fixed window, one partner per deal                                                                                                                                                                                                                                                                                                             | Cookie/attribution window per action; last-click disputes; fraud screening |
| Concentration            | A handful of partners carry the channel                                                                                                                                                                                                                                                                                                                                                    | Power law with a very long tail of near-zero earners                       |
| Contract shape           | Negotiated agreements, exclusivity, clawback, MDF commitments                                                                                                                                                                                                                                                                                                                              | Standardized terms accepted at signup; testable at scale                   |
| Lifecycle review         | JBP + QBR, relationship-bound                                                                                                                                                                                                                                                                                                                                                              | Automated dashboards; cohort-level review, not per-partner meetings        |

## The effective-rate trap, per side

- B2B: margin stacking. Each tier's markup compounds (Spengler's double marginalization); a two-tier structure must be modeled as one stack end to end, or the end price silently goes uncompetitive.
- B2C: stated vs effective revenue share. Practitioners warn the effective rev-share rate typically runs **20-40% below the stated rate** after deductions - refunds, chargebacks, fraud reversals, non-qualifying actions (vendor/practitioner source; label it, but the direction is well-attested). Model payouts on the effective rate, never the headline rate.

## Parameter defaults when modeling B2C

- Revenue mechanics: SaaS affiliate 20-30% recurring share; ecommerce 10-15% of first order; lead-gen/fintech $50-200 flat CPA (vendor benchmark class - label in the memo).
- Cost stack shrinks but does not vanish: platform/tracking fees, fraud losses, payment costs, creative production, and program-management time replace MDF and enablement.
- Incrementality bites harder, not softer: coupon and cashback affiliates are the textbook case of attributed-but-not-incremental volume - the Blake/Nosko/Tadelis lesson applies with full force. Model incrementality by affiliate segment, not for the program as a whole.
- Per-partner modeling only pays for the head of the distribution: model a top creator or publisher individually the way B2B models a reseller; handle the long tail at cohort level.

## Hybrid cases

- An agency that both refers B2B deals and runs affiliate links: model the two flows separately - they carry different attribution rules, different effective rates, and different incrementality profiles. One blended number hides which motion works.
- A B2B vendor paying influencers/creators for developer or SMB reach: use the B2C mechanics (per-action payout, effective-rate discounting, fraud screening) even though the product is B2B - the money flow, not the buyer, decides the model.
