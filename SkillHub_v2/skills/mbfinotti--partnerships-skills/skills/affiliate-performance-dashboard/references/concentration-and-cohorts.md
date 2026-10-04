# Concentration and Cohorts

Portfolio-health analysis: who actually drives the program, and whether the partner base is renewing itself. Provenance tags as in the metric catalogue.

## Computing top-N concentration

- Rank partners by validated attributed revenue for the period; top-N% share = revenue from the top N% of _active_ partners / total program revenue. Use the spec's active definition for the denominator population.
- Compute top-1%, top-5%, top-10% shares plus the absolute top-5-partner share; recompute quarterly on the same definitions so the trend is real.
- Put the top-partner share on the executive view - concentration is a board-level risk, not an operator detail.

## Published concentration figures - calibration only

| Claim                                                              | Source type                               |
| ------------------------------------------------------------------ | ----------------------------------------- |
| Top 10% of active affiliates drive ~71% of revenue                 | [SYNTH] 2026 aggregator, no raw data      |
| Top 5-10% generate 80-90% of revenue                               | [SYNTH] multiple managed-program datasets |
| Top 1% generate 25-50x the median affiliate's revenue              | [VENDOR] operator data                    |
| 95% of sales from 5% of affiliates                                 | [VENDOR] Pareto framing                   |
| Top-1% share by vertical: ecommerce 28%, B2B SaaS 31%, iGaming 62% | [VENDOR] aggregate of trade/analyst data  |

- Working threshold: **top 5 partners over 50% of revenue is a concentration problem**; losing one super-affiliate can cut program revenue 15-25% [VENDOR]. Adopt the threshold as a review trigger, then re-band it from the program's own quarters [DERIVE].
- Response to a breach is partner development in the next tier down and top-partner retention work - not throttling the top partners.

## Lifecycle stages

- Track partners through recruit -> activate -> produce -> grow. Industry practice follows these stages, but the four-word chain is informal shorthand, not a branded framework - never present it as one.
- Stage conversion metrics:
  - Recruits per month.
  - Conversion-to-active within 90 days.
  - Producers (repeat converters).
  - Growers (rising validated revenue quarter over quarter).
- Conversion-to-active-within-90-days bands [VENDOR]:
  - Healthy programs: 40-60%.
  - Struggling programs: below 20%.
  - Typical activation: around 10%, with top programs above 50%.

  Wide spread = derive the program's own band [DERIVE].

## Cohorting by recruitment month

- Rows = recruitment month; columns = months since recruitment; cells = share active, share with a first conversion, and cumulative validated commission.
- Cohorts answer what a snapshot cannot: whether recent recruiting classes activate faster or slower than older ones, and whether an activation push actually worked.
- Cohort at month granularity - day-level cohorts are too small to show any trend.

## Tail activation and partner-type mix

- Tail activation: share of below-median partners recording a first conversion in the period. A dead tail means recruiting is filling a leaky bucket.
- Time-boxed reality check: a partner with no conversion after 60 days has ~3.7% lifetime probability of ever converting [SYNTH, directional] - concentrate activation effort inside the first 60 days.
- Partner-type mix: share of validated revenue by promotional method (content, coupon, cashback/loyalty, sub-network, influencer, email, PPC). A rising checkout-adjacent share is an incrementality-review trigger, not a fraud verdict.
- Count sub-networks as one credited entity with their own mix breakdown - counting a sub-network's members as many partners distorts both concentration and active-partner counts.
