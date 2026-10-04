# Motion benchmarks (dated) and how to cite them

Two rules before any number leaves this file:

- Never blend PLG and sales-led metrics into one figure. Benchmarking a PLG funnel against sales-led win-rate medians is called out as the single most common benchmarking error in this field.
- Report by source with its date and sample, never a blended average. The same metric diverges irreconcilably across sources because their respondent populations differ.

## Efficiency degraded across 2022-2026 - date every figure

The post-2022 efficiency era moved every headline metric the wrong way. A motion plan graded against pre-2022 folk benchmarks will look broken while performing at today's median.

| Metric                        | Earlier          | Later                            | Source                                                           |
| ----------------------------- | ---------------- | -------------------------------- | ---------------------------------------------------------------- |
| CAC payback (median B2B SaaS) | 14 months (2023) | 18 months (2024)                 | Benchmarkit 2025 SaaS Performance Metrics, n≈936                 |
| AE quota attainment           | 66% (2022)       | 51% (2024) → 48% (2026)          | Bridge Group AE reports (n=172 in 2024; n=158 in 2026, 10th ed.) |
| AE win rate (median)          | 23% (2022)       | 19% (2024)                       | Bridge Group 2024                                                |
| Win rate (cross-check)        | 29% (2021)       | 19% (2025)                       | Ebsta x Pavilion 2025                                            |
| Sales cycle                   | -                | +3-4 weeks on average, 2024-2025 | ICONIQ                                                           |

Attainment is also the canonical example of irreconcilable sources for the same period: Bridge Group 51% vs KeyBanc/Sapphire 75-85% vs RepVue ~43% (Q3 2024) - different populations (consulting-client survey vs venture-backed self-report vs 100K+ anonymous reps). Report the range.

## CAC payback

- KeyBanc/Sapphire 2024 (15th annual, n≈104, median $26M ARR): ~20 months new-only, ~23 months fully loaded. The "new-only" vs "fully-loaded (new+expansion)" scope changes the number materially - confirm scope before comparing two cited figures.
- By ACV tier (Benchmarkit 2024): low-ACV (≤$5K) recovers in roughly 9 months, high-ACV ($100K+) closer to 24. Payback lengthens with deal size because absolute CAC and cycle length rise faster than ACV.
- By motion (operator sources, directional): PLG 8-12 months, sales-led SMB 6-12, enterprise sales-led 18-24 (accepted specifically when NRR exceeds 120%). Payback tolerance is a joint function of motion and retention quality, never payback alone.

## Cycle length and its weak link to deal size

Bridge Group 2024 overall median: 5 months. Band detail, triangulated from Gong/Ebsta/6sense/Norwest secondary aggregators (directional):

- <$5K-$10K: ~25-40 days.
- <$25K: ~90 days.
- $25K-$100K: ~90-180 days.
- $100K+: 3-9+ months, regularly 6-12.

Deal size explains only ~27% of cycle-length variance (HockeyStack regression, 54 B2B SaaS companies, R²=0.268) - the rest is process quality, buyer intent and data quality.

## Rep economics

Bridge Group 2024 AE report (n=172, median $24M revenue, $47K ACV):

- Median quota: $800K.
- Median OTE: $190K on a 53:47 split.
- Quota:OTE: ~4.2x.
- Ramp: ~5.7 months average (SMB 3-4, mid-market 4-6, enterprise 6-9+).

- **Quota vs actual are two different measures.** The commonly conflated "$328K-$800K new ARR per AE" range spans quota assigned (Bridge Group $800K; KeyBanc/Sapphire $750K median) versus actual new ARR booked (KeyBanc/Sapphire 2024 median $328K). Always say which one a cited figure is.
- **Fully-loaded AE cost has no surveyed benchmark - only operator heuristics.** David Sacks: fully-loaded AE cost ≈ 25% of the AE's sales, plus 15-25% sales overhead. FLG Partners enterprise model: a $300K-OTE field AE closing $1.5M carries ~$745K sales-department expense, ~$1.0M with allocated marketing. A synthesized mid-market direct fully-loaded cost lands roughly $240K-$300K+ before SDR/SE/RevOps allocation. Label every such number a modeled estimate.

## Self-serve and PLG conversion

- Trial-to-paid conversion by type: free trials roughly 4-6%, freemium ~3-5%, time-limited trials 8-12%, reverse trials ~2x freemium. The spread across samples (one source cites freemium closer to 12%) signals these are not one homogeneous metric across products.
- Sales-assisted PQL conversion: 15-35%, with multiple sources converging on 20-30% PQL-to-close vs roughly 3-10% for MQLs - the core economic justification for a sales-assist layer. Vendor-cited and directional; validate against your own cohorts.
- Free-trial/POC conversion is the fastest-improving stage: roughly 50% in ICONIQ 2026 data (up ~14 points year-over-year); ICONIQ 2025 (205 GTM execs) found AI-native $100M+ companies converting trial-to-paid at 56% vs 32% for others - product category now drives conversion as much as motion design.

## Retention and efficiency by motion

- NRR by ACV segment (SaaS Capital / Optifai cross-references): enterprise (>$100K) ~118%, mid-market ($25K-$100K) ~108%, SMB (<$25K) ~97%. PLG-SMB NRR is structurally lower because SMB churn is higher: a segment effect, not a motion-quality signal. Never benchmark a PLG company against enterprise NRR medians. ChartMogul (n≈2,100-2,500) reports median venture-backed NRR ~106%; SaaS Capital 2026 (n=1,000+) reports median NRR 103%, GRR 91%.
- Expansion now drives ~40% of growth for $15M-30M+ ARR companies (ChartMogul 2024), up from ~30% in 2021.
- Rule of 40 diverges by motion: PLG companies scored 34 vs 20 for sales-led (Benchmarkit 2024) - consistent with PLG's lower CAC and faster payback trading against its lower NRR ceiling at the SMB end. Never read it in isolation.
- Magic number: KeyBanc/Sapphire 2024 median 0.7 (a 0.90 figure circulates only in secondary aggregation - flag, don't pick); top quartile 1.0-2.0+.
- Pricing shifted under the motions: usage-based pricing reached 51% of public SaaS by 2026 (from 27% in 2021); pure per-seat fell to 28% from 51% (Bessemer State of the Cloud 2026).

## Decision thresholds

- CAC payback trending past 24 months → fix the motion economics before raising further.
- Magic number below 0.5 for two consecutive quarters → cost-of-sales inefficiency.
- NRR below 100% for an enterprise vendor → structural problem, not noise.
- A sales hire that cannot model ~4x its fully loaded cost in incremental revenue → do not make it (the "juice worth the squeeze" floor; see the transition playbooks file).

## Source catalogue

| Source                                    | Publishes                                      | Sample / currency                                                                                       |
| ----------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Bridge Group                              | AE/SDR metrics & comp                          | n=172 (2024); n=158 (2026, 10th ed.)                                                                    |
| Benchmarkit (Ray Rike)                    | SaaS metrics segmented by GTM motion           | n≈936 (2024) - most granular by motion                                                                  |
| KeyBanc / Sapphire                        | Private SaaS survey (ex-Pacific Crest)         | n≈104 (2024), median $26M ARR                                                                           |
| ICONIQ Growth                             | State of GTM / Software                        | ~205 GTM execs (2025); 150+ companies (2026)                                                            |
| ChartMogul                                | Retention / NRR trends                         | n≈2,100-2,500                                                                                           |
| SaaS Capital                              | Private-company survey                         | n=1,000+ (2025, 14th ed.); bootstrapped skew                                                            |
| Bessemer (BVP)                            | State of the Cloud, PLG-to-enterprise playbook | public Cloud Index + portfolio                                                                          |
| Growth Unhinged (Kyle Poyar) / High Alpha | PLG benchmarks, pricing                        | OpenView wound down in 2024; its PLG franchise migrated here - do not cite OpenView as a live publisher |
| Winning by Design                         | Revenue Architecture / Bowtie                  | framework, not a survey                                                                                 |
| ProductLed (Wes Bush)                     | self-serve benchmarks, SLG-to-PLG transitions  | methodology + report                                                                                    |
| Runa Capital ROSS Index                   | trending commercial open-source                | quarterly since Q2 2020, GitHub-star methodology                                                        |

Some 2026-dated figures exist only in secondary blogs citing a primary report; where a figure appears solely in a secondary aggregator, flag it rather than silently picking one.
