# ROI and Incrementality

How to tell caused revenue from claimed revenue. Last-click reporting credits every touched sale; incrementality measures what the program _caused_.

Every conversion is one of three:

- **Incremental**: created by partner exposure.
- **Non-incremental**: would have happened anyway.
- **Cannibalized**: shifted from another channel.

## Instruments, ranked by efficiency

Four instruments answer the same question at wildly different strengths and costs. Effort is analyst hours and the coordination a test needs, never a media budget; compliance cost is the review each one triggers and how hard it is to walk back.

- efficiency: `new-to-file screen > commission-reduction test > geo-lift test > holdout test`
- value: `holdout test > geo-lift test > commission-reduction test > new-to-file screen`
- effort (most first): `holdout test > geo-lift test > commission-reduction test > new-to-file screen`
- compliance cost (most first): `commission-reduction test > holdout test > geo-lift test > new-to-file screen`

Value and effort run in exactly the same order, which is the whole decision: the ratio picks the weakest instrument that still settles the live question, not the most defensible one. Start at the top and stop as soon as the answer changes what you would do.

- **New-to-file screen.** Standing, near-zero once the metric is on the dashboard: net-new customers are less likely to be captured demand. Limits: identity resolution and cross-device loss corrupt the join, and a customer on a second device reads as new. A proxy calibrates suspicion; only a test answers the question.
- **Commission-reduction test.** Step a checkout-adjacent partner's rate down; performance staying flat through reductions implies the conversions were non-incremental [VENDOR]. A week to run, near-zero to analyze - and the highest compliance cost here, because it unilaterally changes a partner's economics: check the notice and rate-change clauses in the program terms first, and expect the relationship damage to outlast the test. Run it before repricing coupon/cashback partners.
- **Geo-lift / matched-market test.** Pause or vary the program in matched geographies when user-level randomization is unavailable. A quarter, mostly waiting for enough periods to read. Defensible externally as a market decision, so it carries the least contractual exposure of the three tests.
- **Holdout / lift test.** Withhold partner exposure from a randomized 5-10% of traffic and compare conversion against the exposed group [VENDOR]. The gold standard; needs user-level scale and engineering to suppress exposure cleanly. Partners can end up uncredited for traffic they drove, which is a program-terms and network-policy question before it is a statistics question - disclose the design rather than running it quietly.

**What the efficiency order starves: the holdout test.** It is the only design that yields an incremental number finance will accept, and it loses every ratio round. Promote it when a repricing or budget decision worth more than the build is blocked on the answer, when user-level scale exists, and when the program's incrementality is already contested - a proxy will not end that argument.

Deleted, not demoted: running any test at all on a program too small for its arm to reach significance. Below that scale the answer is noise dressed as evidence; stay on the new-to-file screen and the partner-type mix, and say so in Open items.

Re-rank against what is already there: an experimentation platform already running product holdouts collapses the holdout test's effort to a week, and a program already split across matched markets makes geo-lift the cheapest real test rather than the second-costliest.

Lift-test data suggests that when cannibalization occurs, revenue usually redistributes to top-of-funnel content partners rather than to other channels [VENDOR] - cutting a low-incrementality partner rarely destroys the demand.

## Last-click failure modes

- Checkout-adjacent partners - coupon, cashback, browser extensions - sit at the last click and collect credit on demand other channels created. Last-click-only program ROI systematically inflates them and starves content partners.
- Reference case: the Honey browser extension.
  - The Honey browser extension (acquired by PayPal) injected its own affiliate cookie at checkout, overriding creators' earlier attribution.
  - A widely-viewed exposé published December 21, 2024 made it the canonical example; PayPal defended the practice as "industry-standard last-click attribution".
  - Google's Chrome Web Store policy update of March 11, 2025 now bars extensions from inserting affiliate links "when no discount, cashback, or donation is provided".
  - Litigation and network removals followed into 2025-2026.
- The lesson for the spec: a dashboard whose ROI is last-click-only cannot distinguish that pattern from genuine performance. Pair ROI with new-to-file share by partner and schedule incrementality tests for checkout-adjacent partner types.
- Route the response correctly: low incrementality is a repricing decision (commission-structure territory), and attribution manipulation is a fraud-rule decision (fraud-detection territory). The dashboard surfaces the signal; it decides neither.

## Sourced vs influenced

- Report partner-sourced and partner-influenced revenue as two separate, capped numbers. Never sum them; a deal qualifying for both counts as sourced only.
- Influenced revenue is a directional advocacy metric, not bookable channel revenue - cap it visually (its own tile, never inside a revenue total).

## The one big published study - cite only with its caveat

- CJ Affiliate (2019) [VENDOR]:
  - 46% higher shopper-to-customer conversion for affiliate-exposed shoppers.
  - 29% higher spend per customer.
  - 88% higher revenue per shopper.
  - Sample: 20.2M shoppers (1.1M affiliate-exposed vs 19.1M not), September 2018 data.
- Caveat travels with the numbers: it is vendor-published marketing using an observational test/control split, not a randomized holdout. Use it to justify running a real test, never as the program's own incrementality figure.

## Specifying ROI on the dashboard

- Net program contribution = `attributed net revenue - (validated commission + network fees + agency fees + placement fees)`. This is the headline profitability number; keep it on the top view.
- State the attribution basis on the ROI tile itself (e.g. "last-click, 60-day cookie") - an ROI number without its attribution basis is unreproducible.
- Show attributed ROAS and attributed ROI as distinct rows with distinct denominators: ROAS = `attributed revenue / spend`; ROI = `(attributed revenue - cost) / cost x 100`. Same numerator, different denominators - presenting one and labelling it the other is the most common tile error.
