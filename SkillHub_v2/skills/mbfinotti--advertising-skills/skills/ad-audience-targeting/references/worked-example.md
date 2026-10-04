# Worked examples - audience targeting plans

Two filled-in plans in the output shape (one B2B, one B2C), then a negative example annotated with what is wrong. Companies and numbers are illustrative composites, not real accounts.

## Table of Contents

- [Example 1 - B2B: compliance-training SaaS](#example-1-b2b-compliance-training-saas)
- [Example 2 - B2C: DTC skincare brand](#example-2-b2c-dtc-skincare-brand)
- [Negative example - what a bad plan looks like](#negative-example-what-a-bad-plan-looks-like)

## Example 1 - B2B: compliance-training SaaS

**Context from the clarifying questions:** sells safety-compliance training to mid-market manufacturers (200-2,000 employees, US). ACV $18k, sales-led. Conversion = demo booked; target CPA $220. Current volume: ~6 demos/week. Assets: 1,400-contact customer CRM list, ~9,000 site visits/month, 2,300 engaged followers. Budget $12,000/month (~$400/day). Addressable universe: ~28,000 accounts / ~190,000 relevant titles. No regulated category.

### 1. ICP summary (evidence-backed)

- Attributes: manufacturing industry; 200-2,000 employees; US; EHS/operations leadership roles. Evidence: closed-won analysis of 74 customers (CRM export, last 24 months).
- Signals: hiring for safety/EHS roles (why now: new leader builds the program); recent OSHA-citation press mentions; pricing-page visit. Evidence: 9 of last 20 closed-won accounts had posted an EHS role within 90 days of first touch (CRM + job-board cross-check, dated).
- Broad-vs-layered verdict: **layered.** 6 conversions/week is far below learning thresholds, and a ~190,000-person universe is too small for algorithmic expansion to help.

### 2. Tier table

| Tier                                                                                      | Defining signal (evidence)                                                                                | Est. size                        | Exclusions applied | Test budget/day | Success criterion                                                     |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------ | --------------- | --------------------------------------------------------------------- |
| First-party: engagers + site visitors                                                     | 90-day site visitors + 365-day content engagers (analytics)                                               | ~14,000                          | E1, E2, E3         | $80             | ≤$180 cost/demo                                                       |
| Retargeting pool (sized here; sequence → mbfinotti/advertising-skills@retargeting-funnel) | Pricing/feature-page visitors, 30 days                                                                    | ~1,900                           | E1, E2, E3         | $50             | ≤$150 cost/demo                                                       |
| Signal-triggered account list                                                             | Accounts with fresh EHS hiring or citation signal, refreshed weekly, ≤90-day signal age (CRM cross-check) | ~1,100 accounts / ~8,000 members | E1, E2, E3, E4     | $90             | ≥2× demo rate of the firmographic tier                                |
| Firmographic prospecting (professional network)                                           | Function: EHS/ops + manager-and-above seniority, manufacturing, 200-2,000 employees (closed-won analysis) | ~160,000 after exclusions        | E1, E2, E3, E4     | $180            | ≤$260 cost/demo after 4 weeks; lead quality ≥ current channel average |

Rows sit in the default efficiency order, no re-rank applied. Note that budget runs the opposite way - the firmographic tier takes the largest share precisely because it is the least efficient and the slowest to read, so it needs the most spend to say anything. Efficiency orders the testing, not the budget split.

Tiers deliberately absent, with reasons:

- Broad/algorithmic: universe too small; the trap is the algorithm expanding past the real market.
- Interest/affinity: no interest maps to "buys compliance training"; no evidence.
- Lookalike: seed exists, but the universe is small enough that firmographic targeting already covers it. Revisit if the firmographic tier saturates; seed selection would go to mbfinotti/advertising-skills@lookalike-audience-seeds.

Budget check: $400/day total. Demo at $220 CPA can't hit ~50 events/week on this budget, so all tiers optimize to a higher-funnel proxy event (qualified landing-page action, ~$45 effective CPA, ~55/week plausible at full budget) with demos tracked as the true KPI offline.

### 3. Exclusion matrix

| Exclusion list                   | Source                          | Applied to             |
| -------------------------------- | ------------------------------- | ---------------------- |
| E1 Customers                     | CRM upload, refreshed monthly   | All tiers              |
| E2 Employees + known competitors | Company exclusion list          | All tiers              |
| E3 Booked demos, 90 days         | CRM upload, weekly              | All tiers              |
| E4 Higher-intent tiers           | First-party + retargeting pools | Both prospecting tiers |

Post-exclusion size re-check: all tiers remain above the platform floor (smallest: retargeting at ~1,900).

### 4. Test sequence

1. Weeks 1-2: first-party + retargeting tiers only (fastest signal, cheapest evidence). Variable isolated: audience; one proven creative set.
2. Weeks 2-6: add both prospecting tiers at fixed per-tier budgets. Variable isolated: firmographic vs. signal-triggered audience, same creative.
3. Week 6: promote/hold/kill per the stated criteria. Kill = $440 spent per tier-week at 50%+ worse cost/proxy than the best tier, or delivery stalled.
4. On promote: scale ≤20%/week; revisit the lookalike tier only if the firmographic tier reaches ~35% audience penetration.

### 5. Compliance notes

None triggered. Note kept in plan: never target or infer health conditions of workers even though the product is safety-adjacent.

### 6. Review cadence

- Overlap audit before any new tier.
- Weekly floor check during weeks 1-6.
- Signal list refreshed weekly (90-day expiry enforced).
- Customer/demo exclusion uploads weekly-monthly as listed.
- Full plan review quarterly or when the ICP evidence changes.

## Example 2 - B2C: DTC skincare brand

**Context:** AOV $58, conversion = purchase, target CPA $29 (blended). Mature account: ~420 purchases/week. Assets: 92,000-customer list, ~310,000 site visits/month, large engaged social audience. Budget $150,000/month (~$5,000/day). Universe: tens of millions. No regulated category.

### 1. ICP summary

- Attributes: women 25-45, US/CA/UK, skincare-involved buyers. Evidence: customer survey (n=1,800) + purchase data.
- Signals: cart abandonment, product-page depth, seasonal spikes (gifting periods), repeat-purchase window at 60 days. Evidence: analytics cohort report.
- Broad-vs-layered verdict: **broad-first.** Conversion data is dense (420/week ≫ threshold) and the universe is huge. Explicit layers are kept for (a) research into who responds, (b) retargeting, (c) the parallel test control.

### 2. Tier table

| Tier                                                                                             | Defining signal (evidence)                                           | Est. size        | Exclusions applied | Test budget/day | Success criterion                                                        |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ---------------- | ------------------ | --------------- | ------------------------------------------------------------------------ |
| Broad/algorithmic prospecting                                                                    | None - delivery model on purchase signal                             | Tens of millions | E1, E2, E3         | $2,900          | ≤$29 blended CPA                                                         |
| Lookalike (top-LTV seed; seed selection → mbfinotti/advertising-skills@lookalike-audience-seeds) | Resemblance to top-quartile-LTV buyers, seed refreshed every 45 days | Millions         | E1, E2, E3         | $900            | Within 15% of broad tier CPA; else fold into broad                       |
| Interest control (research instrument)                                                           | Skincare/beauty interest cluster (survey evidence)                   | ~8M              | E1, E2, E3         | $400            | Not judged on CPA alone - reports segment response for creative planning |
| First-party: lapsed customers                                                                    | 60-180 days since last purchase (purchase data)                      | ~38,000          | E2 only            | $300            | ≤$18 cost/repeat purchase                                                |
| Retargeting pool (sized here; sequence → mbfinotti/advertising-skills@retargeting-funnel)        | Site visitors 30 days + cart abandoners 7 days                       | ~95,000          | E1, E2             | $500            | ≤$14 CPA; watched for incrementality, not celebrated for ROAS            |

Rows are deliberately re-ranked away from the default order. This account already runs a mature retargeting pool and a 92,000-customer list, so the warm tiers need no proving and the whole open question sits on the cold side - cold tiers therefore lead both the table and the test sequence. The default order still governs any account without that head start.

Retargeting + lapsed = $800/day = 16% of spend - inside the 15-25% band; alarm threshold documented at 40%.

### 3. Exclusion matrix

| Exclusion list                | Source                      | Applied to                          |
| ----------------------------- | --------------------------- | ----------------------------------- |
| E1 Purchasers, 30 days        | Customer list, synced daily | All prospecting tiers + retargeting |
| E2 Employees                  | List upload                 | All tiers                           |
| E3 Retargeting + lapsed pools | First-party audiences       | Broad, lookalike, interest tiers    |

### 4. Test sequence

Ordered by the re-rank stated under the tier table, not by the default order.

1. Weeks 1-4: broad vs. lookalike vs. interest control at fixed per-tier budgets, identical creative. One variable: audience.
2. Week 4 decision: lookalike within 15% of broad → merge into broad and reassign budget; interest control never killed on CPA (it is the research instrument) but capped at ~8% of spend.
3. Winners move to algorithmic budget pooling; scale ≤20%/week, the widely treated (not platform-documented) learning-reset threshold.
4. Quarterly: a geo-holdout on the retargeting pool to estimate incrementality - reported retargeting ROAS is treated as inflated until tested.

### 5. Compliance notes

None triggered. EU expansion flagged: consent banners will cut tracked signal. Re-verify tier sizes and switch to server-side conversion feeds before extending the plan to the EU.

### 6. Review cadence

- Overlap audit before any new tier.
- Seed refresh every 45 days.
- Exclusion syncs daily/weekly as listed.
- Creative fatigue watch handed to mbfinotti/advertising-skills@ad-creative-fatigue.
- Full review quarterly.

## Negative example - what a bad plan looks like

The same B2B company as Example 1, planned badly:

| Tier                     | Definition                                                    | Budget/day |
| ------------------------ | ------------------------------------------------------------- | ---------- |
| "Ops leaders"            | 12 stacked interests + job titles + age 30-55 + 3 metro areas | $40        |
| "Safety pros"            | 9 stacked interests, overlapping the above                    | $40        |
| "Manufacturing interest" | Broad interest category, no exclusions                        | $40        |
| Lookalike                | Seed = all page followers                                     | $40        |
| Retargeting              | All site visitors 180 days, same offer as prospecting         | $180       |
| "Coverage" tier          | Competitor-brand interest, est. 800 people                    | $20        |

Why it fails, line by line:

- **Every tier is below the funding floor.** $40/day against a $220 CPA is ~1-2 conversions/week per ad set; nothing exits learning. Six fragments where two consolidated tiers would work.
- **Interest stacking as precision theater.** 12 interests + demographics + geo shrinks the audience and raises cost without touching the actual lever (creative and offer). The ICP knowledge fed filters instead of messaging.
- **No exclusion matrix.** Tiers 1-3 overlap heavily and bid against each other; customers and open opportunities see prospecting ads.
- **Junk seed.** Page followers are engagement-selected, not purchase-selected; the lookalike inherits that bias.
- **Retargeting at 50% of spend, same offer.** Inflated blended ROAS while the prospecting refill starves - and the users it "converts" were largely converting anyway.
- **"Coverage" tier below the platform floor.** 800 people will not deliver; it exists to look thorough, not to work.
- **No evidence column, no success criteria, no kill rule.** Nothing here can be audited, promoted, or killed on data - the plan cannot fail visibly, which means it cannot be fixed.
