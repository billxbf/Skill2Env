# Approval Matrix Design

Provenance tags used throughout this reference:

- `[practitioner]` - published practitioner/consultancy source (Umbrex deal-desk playbook, RevOps Co-op, SBI Growth - operator series, not standards bodies).
- `[illustrative]` - single vendor blog or example, not a benchmark.
- `[derive]` - must come from the user's own deal data.

Level counts and thresholds vary per company: treat every number below as a default to calibrate, never an industry constant.

## The five governed levers [practitioner]

The matrix governs five concession levers, not just price:

- Price/discount
- Payment terms and billing
- Services inclusion and delivery commitments
- Contract risk (liability, remedies)
- Security/privacy commitments

Governing only discount is a named failure mode: concessions migrate to the ungoverned levers, where they are harder to see and cost more. Translate every non-price concession into an equivalent economic value so approvers can compare it to discount (a net-90 term, a free implementation, an uncapped SLA credit all have a price).

## Dimensions beyond discount %

- Deal size (ACV or TCV band) - a 30% discount on a $5K deal and on a $500K deal are different decisions.
- Segment: industry, company size, region, channel. Build eligibility fences per segment so approvals are comparable like-for-like and cross-segment arbitrage is blocked [practitioner].
- Motion: new business vs renewal vs expansion - each gets its own corridor; renewal discounts compound forever.
- Term length and product line - fold into deal type at intake; a multi-year ask changes the economics of the same headline %.
- Margin impact - the truest dimension when per-deal margin is computable; discount % is its proxy.

## Tiers and the auto-approve floor

Modal practice is 3-4 tiers [practitioner, convergent across sources - descriptive of common practice, not a standard]:

| Tier | Meaning                       | Typical approver                            | Analyst load per deal             |
| ---- | ----------------------------- | ------------------------------------------- | --------------------------------- |
| 0    | Within policy - auto-approved | Nobody; quote tool applies rules            | none                              |
| 1    | Managed exception             | Sales manager or deal desk analyst          | minutes                           |
| 2    | Material exception            | Sales VP + Finance (or deal desk lead)      | an hour, plus two calendars       |
| 3    | Executive exception           | CRO/CFO level, jointly for the largest asks | an hour, plus executive calendars |

The auto-approve floor is list price or a low single-digit discount, applied by the quote tool [practitioner]. Every deal it absorbs into tier zero costs no analyst time at all, so where the floor sits decides the desk's entire workload. Three ways to place it.

Lead with the win-rate derivation - it is the only floor that survives being challenged by a rep.

- discount the floor actually stops: win-rate derivation > distribution percentile > illustrative placeholder
- effort: win-rate derivation > distribution percentile == illustrative placeholder
- reversibility cost: illustrative placeholder > distribution percentile == win-rate derivation

**Win-rate derivation** [derive]. Plot win rate by discount band over 2+ quarters of closed deals and set the floor where extra discount stops buying win rate. An hour of analysis once the data exists, and the number is defensible band by band when sales pushes back.

**Distribution percentile** [derive]. Set the floor at a chosen percentile of the historical discount distribution. Near-zero effort, but it encodes what reps already did as policy - it describes past behaviour, creep included, rather than what worked.

**Illustrative placeholder** [illustrative]. Ladders seen in the wild, to hold the slot for one cycle and never to ship as policy:

- <10% auto / 10-20% manager / 20%+ VP
- 10-20% manager / 20-40% VP / 40%+ desk review / multi-year to Finance+Legal

Ranking these two against each other would be false precision - neither is evidence, both are stand-ins.

- Distribution percentile == placeholder on effort: at order-of-magnitude granularity both are near-zero, one query against data the desk already pulls, versus none.
- Distribution percentile == win-rate derivation on reversibility: both leave an audit trail that can be re-derived and re-defended. The placeholder cannot be defended, so it gets renegotiated deal by deal and only ever ratchets down.

Deleted, not demoted: the circulating 15% / 25% / above-25%-to-CRO+CFO ladder. Treat it as fabricated, not as a placeholder to rank below the others.

What this order starves: the win-rate derivation, the only defensible method, loses whenever the data is not there yet - and two quarters is the stated minimum. Promote it the moment 2+ quarters of closed-won and closed-lost carry discount fields, whatever the deadline. Every quarter run on a placeholder floor sets the level reps come to expect, and raising a floor later costs political capital that setting it right never did.

Escalation overrides bypass the % ladder wherever the floor sits: deal size above a set band, any custom terms, public-reference or marquee-logo commitments [illustrative].

## Hard floors

- In most B2B software the binding hard floor is a policy margin floor, not a cost floor: marginal cost is near zero, so the cost floor sits far below any price anyone would accept, and only a declared minimum-margin policy actually binds [practitioner].
- Exception: AI/inference-heavy and other usage-scaling-COGS products have real, growing marginal cost - there the cost floor rises and binds again [single-source but economically sound; verify against the user's own unit costs].
- The floor is approver-independent: no tier waives it. Set it per product family when COGS differs by line; a company-wide number is [derive], never the circulating "75% gross-margin floor" (a repeated number, not a benchmark).

## Prohibited regardless of approver

No tier may approve these; they can only be considered at all with an explicit give-get trade, and then only by Legal plus the commercial lead jointly [practitioner]:

- MFN / best-price guarantees, retroactive rebates, broad benchmarking-publication rights.
- Open-ended price holds without defined scope, term, and expiration.
- Uncapped liability or consequential damages outside a pre-approved carve-out list.
- Commitments to build: net-new functionality, integrations, or timelines not pre-approved by Product and Delivery.

The give-get discipline generalizes: never concede anything without getting something priced in return (longer term, larger volume, upfront payment, a reference).

## Strategic vs tactical

Classify discounts:

- Tactical: routine competitive pressure, stays inside standard bands.
- Strategic: market entry, marquee logo, named-competitor displacement, executive-approved and logged with its rationale.

Caution from practitioner discussion: if 40% of deals claim to be strategic, nothing is [illustrative phrasing; the mechanism is sound].

## Threshold calibration and recalibration

- Initial anchors must be observable at quoting time and reflect true economics: deviation from the price corridor, pocket-margin floor, total concession value across all levers [practitioner].
- Derive, don't import [derive]:
  - Pull 2+ quarters of closed deals.
  - Plot discount distribution by segment and win rate by discount band.
  - Set the auto-approve floor where extra discount stops buying win rate.
  - Set tier boundaries at natural breakpoints in the distribution.
  - Sanity-check that the top tier catches the deals leadership actually wants to see.
- Recalibration inputs [practitioner]:
  - Exception analytics: which types drive cycle time and rework, and what should become standard.
  - Leakage events: policy vs executed-outcome deviations, tagged by cause.
  - Late-discovery rate: non-standard terms surfacing after proposal, an intake gap.
- Cadence [practitioner]:
  - Daily: queue management.
  - Weekly: cycle-time percentiles and exception volume.
  - Monthly: exceptions forum producing a change backlog with owners and dates.
- Two quarters of data minimum before judging approval-pattern changes [practitioner].

## Circulating numbers to refuse

Never present as fact; each circulates unattributed:

- 75% gross-margin floor
- 1 deal-desk FTE per $40M ARR
- 35% mid-market / 70% enterprise deal-desk hit rates
- Stripe-attributed "customers at 30%+ discount churn at 4.2x"
- Gartner-attributed "90% of B2B purchases AI-intermediated by 2028"

A related but distinct claim, discount-negotiating customers churning at roughly 2x, is a practitioner claim (ProfitWell lineage), usable only when labeled as such.
