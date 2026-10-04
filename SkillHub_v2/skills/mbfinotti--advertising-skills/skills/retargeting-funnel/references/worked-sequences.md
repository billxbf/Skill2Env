# Worked retargeting sequences

Three end-to-end examples: a B2C e-commerce sequence, a B2B SaaS sequence, and a broken sequence with the diagnosis. Figures are illustrative composites, not client data - the method is the point.

## Contents

1. B2C e-commerce: mid-priced skincare store
2. B2B SaaS: sales-assisted analytics platform
3. Negative example: a plausible-looking sequence that fails

## 1. B2C e-commerce: mid-priced skincare store

### Data pulled

- Traffic: 220k monthly sessions - 55% content/landing, 30% product pages, 9% cart or checkout start, 6% other. ~2,600 purchases/month.
- Cart abandonment 72% (near the widely cited ~70% e-commerce average from Baymard Institute's meta-analysis).
- Time-lag report: 52% of purchases within 1 day of first visit, 81% within 7 days, 93% within 21 days, 99% within 45 days.

### Boundaries chosen

The 80th converter percentile lands at ~7 days → hot-window edge = 7 days. The tail to 21 days holds another 12% of converters → warm window 8-21 days. Beyond 45 days almost nobody converts from the original visit, so anything longer is win-back, not conversion retargeting.

### Stages

| Stage           | Inclusion rule                                             | Window                 | Message intent / offer rung                                                          | Concepts |
| --------------- | ---------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------ | -------- |
| S1 Hot-cart     | Cart or checkout start, no purchase                        | 0-7 d                  | Reminder: show the exact item; no incentive                                          | 3        |
| S2 Warm-product | Product-page view, no cart                                 | 0-14 d                 | Social proof: reviews, UGC, before/after                                             | 3        |
| S3 Objection    | Union of S1/S2 members aged past their window, no purchase | 8-21 d                 | Objection handling: shipping, returns, guarantee                                     | 3        |
| S4 Last-call    | Any of the above, no purchase                              | 22-45 d                | Incentive + urgency - the only discount rung                                         | 3        |
| S5 Replenish    | Purchasers                                                 | 30-90 d after purchase | Post-purchase cross-sell/refill (separate budget; not part of the conversion ladder) | 3        |

### Exclusions

- `RTG_CART_0-7` excludes `EXCL_PURCH_180`.
- `RTG_PRODUCT_0-14` excludes `RTG_CART_0-7` and `EXCL_PURCH_180`.
- `RTG_OBJECTION_8-21` excludes both fresher stages and `EXCL_PURCH_180`.
- `RTG_LASTCALL_22-45` excludes all above and `EXCL_PURCH_180`.
- `RTG_LASTCALL` additionally excludes `EXCL_REPEAT_ABANDON` (3+ abandonments, no purchase, 90 d) so serial abandoners cannot farm the discount.
- Converter exclusion window: 180 days (repurchase cycle ~60-90 days; 180 gives margin without choking prospecting).

### Size check (after exclusions)

Cart pool: ~9% of 220k sessions ≈ deduplicated ~11k people/month; minus purchasers ≈ 8k over 7 days ≈ ~1.9k - clears the ~1,000 practical floor. S3 and S4 inherit aged members and also clear. All five stages ship.

### Caps

- S1: no platform cap field on the conversion objective. Cap-proxy: act at frequency >6/week or CTR −20% vs 7-day baseline.
- S2-S4: proxy 4-5/week.
- S5: 2/week.
- Review cadence: every 2-3 days for S1, weekly for the rest.

### Measurement

- Per-stage: spend, reach, frequency, CTR, CPM, platform CPA, new-vs-returning share.
- Blended: monthly revenue ÷ total marketing spend, trended.
- Incrementality: 15% audience holdout on S1 and S4 (the two stages carrying the strongest "would have bought anyway" risk) for 6 weeks. Decision rule: if S1's holdout-measured lift is indistinguishable from zero, fold S1's budget into prospecting regardless of its platform ROAS.

## 2. B2B SaaS: sales-assisted analytics platform

### Data pulled

- Traffic: 38k monthly sessions - 60% blog/content, 22% feature pages, 8% pricing, 3% trial start. ~85 closed-won deals/quarter.
- CRM sales-cycle report (used as the lag source - the pixel cannot see a 4-month cycle): median first-touch-to-close 74 days. 80th percentile ~110 days.
- No discount is ever offered (question 7: no).

### Boundaries chosen

80th percentile ≈ 110 days → the "active evaluation" horizon is ~120 days, not 30. Pixel-based windows beyond ~30 days undercount Safari/iOS users, so stages past 30 days are built from CRM-list audiences (uploaded contacts and accounts), refreshed weekly.

### Stages

| Stage                  | Inclusion rule                            | Window / source                      | Message intent                                                                   | Concepts |
| ---------------------- | ----------------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------- | -------- |
| S1 High-intent         | Pricing view or trial start               | 0-14 d, pixel                        | Proof: named-customer case study                                                 | 3        |
| S2 Evaluators          | Feature-page view, no pricing view        | 0-30 d, pixel                        | Objection handling: security, integrations, comparison                           | 3        |
| S3 Open-deal air cover | CRM deals in evaluation/proposal          | List, weekly refresh                 | ROI content, analyst comparison - aimed at the buying committee, not one visitor | 3        |
| S4 Direct ask          | S1/S2 members aged 15-120 d, no open deal | List (CRM-matched) + pixel remainder | Direct demo ask; lower-friction fallback: tailored assessment                    | 3        |

No discount rung exists. The ladder ends on the hardest direct ask.

### Exclusions

Each stage excludes all deeper/fresher stages. Every stage excludes `EXCL_CUSTOMERS` (all current customers, list-based, no expiry) and `EXCL_CLOSEDLOST_90` (closed-lost under 90 days - sales asked for a cooling-off period). Naming: `RTG_PRICING_0-14`, `RTG_FEATURE_0-30`, `RTG_DEAL_LIST`, `RTG_ASK_15-120`.

### Size check (after exclusions)

Pricing pool: 8% of 38k ≈ ~2.4k dedup/month → over 14 days ≈ ~1.1k, minus customers/open deals ≈ ~900. On a 300-minimum professional platform this clears. On a 1,000-floor platform it does not, so S1 runs only where the floor allows, and elsewhere S1 and S2 are merged (`RTG_INTENT_0-30`).

This collapse is recorded in the plan, not improvised later. S3 has ~140 open-deal accounts - below every social floor as a company list, so it runs on the professional platform (account targeting) only.

### Caps

- Professional platform: no cap on the objective used. Cap-proxy ~3/person/week via an engagement-based rotation exclusion. Creative refreshed every 2-3 weeks because small pools build frequency fast.
- Other channels: proxy 4/week.

### Measurement

- Per-stage KPIs plus pipeline metrics: influenced opportunities, cost per engaged account, account penetration on S3.
- Blended: quarterly pipeline ÷ paid spend.
- Incrementality: hold out a random 20% of the S3 account list for one quarter, and compare opportunity creation between held-out and targeted accounts. Decision rule: S3 survives only if targeted accounts open opportunities at a meaningfully higher rate.

## 3. Negative example: plausible-looking but broken

A DTC supplements brand (60k sessions/month, ~700 orders) ships this:

| Stage | Audience          | Window  | Offer                 | Cap      |
| ----- | ----------------- | ------- | --------------------- | -------- |
| A     | All site visitors | 0-30 d  | 10% off, urgency copy | none set |
| B     | Product viewers   | 0-30 d  | 10% off, urgency copy | none set |
| C     | Cart abandoners   | 0-30 d  | 15% off               | none set |
| D     | Past buyers       | 0-180 d | 15% off "come back"   | none set |

Looks like a funnel - four tiers, deeper stages get bigger discounts. Five faults:

1. **No mutual exclusion.** Every cart abandoner is simultaneously in A, B and C: three ad sets bid on the same user in the same auctions, inflating CPM against themselves - and the platform reports each stage's "conversions" from the same purchase.
2. **No converter suppression on A-C.** A buyer stays in "all visitors" for 30 days and keeps seeing 10%-off ads for what they bought at full price - brand damage plus pure waste. Stage D then _targets_ buyers with a discount they did not need.
3. **Discount on every rung.** The first touch a first-day visitor sees is a coupon. Within weeks, abandonment rises: customers learn that abandoning triggers 15%. The ladder trains the behaviour it exists to fix.
4. **Identical windows regardless of depth, never checked against lag data.** The brand's own time-lag report (never pulled) shows 85% of orders convert within 4 days. Days 5-30 of stages A-C mostly re-serve people who were never going to convert from that visit, while there is no stage at all for the 0-4-day window where conversion actually happens.
5. **No caps, no size check.** Stage C holds ~600 people after dedup - under the practical floor. It underdelivers erratically, and the users it does reach see the ad 15+ times a week. No measurement plan exists beyond platform ROAS, which looks excellent, because stages A-D are collectively claiming credit for most of the 700 orders that direct and email traffic would have produced anyway.

**The repair** is the skill's workflow in miniature:

1. Pull the lag report and set the hot edge at 4 days.
2. Collapse to three stages (hot 0-4 cart/checkout, warm 0-14 product-view, last-call 15-30).
3. Make each stage exclude deeper/fresher ones and all purchasers (180 d).
4. Move the discount to last-call only and exclude repeat abandoners from it.
5. Set cap-proxies with decay signals.
6. Schedule a 15% holdout on the hot stage before trusting any ROAS number it reports.
