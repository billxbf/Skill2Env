# Published CAC/ROAS benchmarks - provenance, figures, folklore

Every CAC/ROAS benchmark in circulation is either a vendor's client sample or a self-reported survey. There is no neutral, audited, industry-wide CAC or ROAS benchmark, and no standards body defines what enters the CAC numerator. Quote provenance with the number or do not quote the number.

## The evidence contract

Before citing any external figure in a report, attach all four fields - publisher, year, sample, and the metric variant it measured - plus the publisher's commercial interest when it has one. A figure missing any of these is quoted as "unverified" or dropped.

## Publishers worth naming

Rows run best-first, ordered by what a citation from each tier is worth:

- value: platform-instrumented vendor data > large self-reported surveys > agency client analytics > consultancy and AI-generated summary pages
- effort: all == (roughly an hour of sourcing per figure, whichever tier) - only value separates them, so never settle for a lower tier to save time

Platform-instrumented data is measured rather than recalled, but every tier is skewed to that publisher's own customer base: more credible is not neutral. The bottom tier is not a weaker source, it is not a source - trace the figure to the named publisher underneath it or drop it (see Circular citation below).

| Source                                                           | Type                    | Sample                                                          | Measured or self-reported    | Commercial interest                                             |
| ---------------------------------------------------------------- | ----------------------- | --------------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------- |
| Triple Whale 2025                                                | platform-instrumented   | 18,000+ ecommerce brands                                        | measured                     | analytics vendor                                                |
| Polar Analytics 2026                                             | platform-instrumented   | thousands of Shopify brands, 16 industries                      | measured                     | analytics vendor                                                |
| Varos / Billo 2025-2026                                          | platform-instrumented   | thousands of campaigns; Billo: 80,000+ Meta video ads (H2 2025) | measured                     | benchmarking vendors                                            |
| Benchmarkit (Ray Rike), 2025 B2B SaaS Performance Metrics Survey | survey                  | 583 participants; per-metric n = 21-149                         | self-reported                | advisory/data vendor                                            |
| Aleph x Benchmarkit 2026 SaaS & AI Survey                        | survey                  | 342 companies (198 reported CAC payback), CY-2025 actuals       | self-reported                | FP&A vendor                                                     |
| Gartner CMO Spend Survey 2025                                    | survey                  | 402 CMOs, majority >$1B revenue, fielded Feb-Mar 2025           | self-reported                | independent research                                            |
| High Alpha (formerly OpenView) 2024 SaaS Benchmarks              | survey                  | 800+ companies                                                  | self-reported                | VC/studio                                                       |
| KeyBanc/KBCM, SaaS Capital                                       | surveys                 | large private SaaS panels                                       | self-reported                | bank / lender to SaaS                                           |
| First Page Sage, CAC by industry                                 | agency client analytics | 120+ B2B and 103 B2C clients, Jan 2022-Aug 2025                 | measured, non-representative | SEO agency; **self-disclosed 75% organic / 25% paid weighting** |

This ordering is a default that a variant match overrides: a tier-1 figure measuring a different variant is worth less than a tier-2 figure measuring the user's own. Check the variant before the tier.

OpenView ceased new investments in December 2023. Its SaaS Benchmarks Report moved to High Alpha (with Paddle). Cite 2024+ editions under the new owner.

## B2C / ecommerce figures

- Median ecommerce ROAS **2.04** - Triple Whale 2025, 18,000+ brands, vendor-instrumented. Far below the folk 4:1. Median paid-social ROAS 1.86-1.93x across ~35,000 brands in the same vendor's earlier dataset.
- By channel: paid search median ~4.5x, Meta 2.2-2.8x, TikTok ~1.4x rising to ~2.25x with value optimisation - Varos / Billo, 2025-2026, platform-instrumented campaign samples.
- Seasonality large enough to invert a verdict: Toys & Games ROAS 1.46 in July vs 2.90 in December - Billo, H2 2025, 80,000+ Meta video ads. Black Friday / Cyber Monday can collapse per-order contribution margin 40-60% (Luca, vendor analysis).
- CAC and conversion by revenue tier (Polar Analytics 2026, thousands of Shopify brands):
  - the $5M-$20M revenue tier shows the worst CAC efficiency
  - $100M+ brands post the highest conversion rates at 6.29%
- First Page Sage ecommerce CAC $86 (combined organic + paid, 75% organic-weighted agency-client data, Jan 2022-Aug 2025).

## B2B / SaaS figures

- CAC payback median (three panels, presented as a conflict, never averaged - they disagree because panels and definitions differ):
  - **18 months in 2024**, up from 14 in 2023 (Benchmarkit 2025, 583 participants)
  - **16 months FY2025**, top quartile ≤6, bottom quartile ≥24 (Aleph x Benchmarkit 2026, 198 of 342 reporting)
  - **20 months in 2024**, down from 25 in 2022 (KeyBanc)
- CAC payback by ACV segment (Benchmarkit 2025/2026, replacing generic working bands with a measured, segmented one - ACV predicts payback better than any other single attribute): sub-$5K ACV ~11 months; $10K-25K ACV ~12 months; $25K-50K ACV ~14 months; mid-market ~14-18 months; $50K-100K ACV ~22 months; above $100K ACV 18-24 months; above $250K ACV ~24 months. A below-median number at high ACV is not automatically a red flag - weigh it against net revenue retention, since high NRR can justify a longer upfront acquisition period.
- New CAC Ratio: median **$2.00 of S&M spend per $1.00 of new-customer ARR** in 2024, up 14% YoY, 4th quartile $2.82 (Benchmarkit 2025). Uses the SaaS Metrics Standards Board convention: New CAC Ratio = total S&M expense ÷ new-customer ARR - a convention, not an accounting standard.
- LTV:CAC medians: 3.2:1 (Optifai, N=939, Q2 2025-Q1 2026) and 3.6:1 (Benchmarkit 2025) - the "observed median near 3" is descriptive, not evidence for the 3:1 rule.
- CAC by vertical (First Page Sage, organic-weighted client data, Jan 2022-Aug 2025) - organic CAC runs roughly half of paid in most B2B verticals, so remember the sampling bias before comparing a paid-heavy account to any of these:
  - B2B SaaS $239 combined ($205 organic / $341 paid)
  - construction $281
  - cybersecurity $387
  - financial services $784
  - real estate $791
  - education $1,143
  - fintech enterprise $14,772
- Cost per SQL $1,357 average vs cost per lead $198 average in the same 2024 dataset (First Page Sage) - the gap between the two is the point.
- Marketing budget (Gartner 2025, n=402, mostly >$1B-revenue firms) - descriptive of what large firms _do_, not what any firm _should_ spend:
  - 7.7% of company revenue, down from 9.5% three years prior
  - paid media 30.6% of marketing budget

## Attribution inflation (context for platform-reported ROAS)

- Observational/platform attribution overstated true lift by factors of ~7.0, 9.5, and 7.6 for upper/mid/lower-funnel outcomes vs randomized ground truth - Gordon, Zettelmeyer, Bhargava & Chapsky 2019, Marketing Science 38(2), 15 Facebook RCTs, ~500M user-experiment observations.
- Account audits show Meta and Google jointly claiming 150-200% of real revenue via double-counting - AdBeacon, vendor client audits (indicative, not audited).
- Global iOS tracking opt-in sat near 38% in Q1 2026 (Adjust benchmark, reported via SignalSeal), so most mobile attribution is modelled rather than deterministic - another reason a platform figure is a claim, not a measurement.

## Why cross-report comparison is unsound

- **Definitional mismatch.** Benchmarkit, First Page Sage, KeyBanc, and Triple Whale each use materially different numerators, customer definitions, and attribution scopes. Comparing your blended CAC to a published paid CAC measures the definitions.
- **Survivorship and self-selection.** Survey respondents opt in, failed companies are absent, and a VC or lender panel is a portfolio, not a market.
- **Disclosed sampling bias.** First Page Sage weights its blend 75% organic because it is an SEO agency - its own methodology note says so. A 90%-paid business cannot compare to it directly.
- **Small n.** Several Benchmarkit metrics rest on n = 21-43 (Blended CAC Ratio n=43, Expansion CAC Ratio n=21). Report medians and quartiles, never a point estimate.
- **Circular citation.** Many recent consultancy and AI-generated benchmark pages cite each other in loops. Trace a figure to a named publisher with a stated sample, or drop it.

## Folklore - full origins list

None of these traces to a study. Name the origin when a user quotes one, and put the business's own break-even next to it.

| Rule                                                                                 | Originator                                                                                                                   | Evidence status                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3:1 LTV:CAC                                                                          | David Skok (Matrix Partners), ~2011-2013, "SaaS Metrics 2.0"                                                                 | Self-admitted guess - on record at SaaStr: "I guessed at that number, after visiting many, many SaaS companies."                                                                                                                                         |
| 12-month CAC payback                                                                 | David Skok, 2011                                                                                                             | Rule of thumb tied to 2011 fundraising conditions; never empirically validated.                                                                                                                                                                          |
| 4:1 (4x) ROAS                                                                        | No traceable author; often misattributed to a 2016 Nielsen study                                                             | The Nielsen analysis names no universal 4:1 and stresses category variance. 4:1 is break-even at a 25% contribution margin (1 ÷ 0.25), retroactively declared a target.                                                                                  |
| MER > 4, rising to 5-8 at scale                                                      | Taylor Holiday (Common Thread Collective)                                                                                    | Stated heuristic, never measured across a sample.                                                                                                                                                                                                        |
| CAC ≈ 25% of gross profit                                                            | Taylor Holiday (CTC, 2022), "fuel profit" framing                                                                            | Same status.                                                                                                                                                                                                                                             |
| SaaS Magic Number 0.75                                                               | Rory O'Driscoll (Scale VP) anecdote, ~2005; popularised by Lars Leckie, 2008                                                 | Single-anecdote origin; Benchmarkit 2025 reports a 0.90 median.                                                                                                                                                                                          |
| "Spend 5-10% of revenue on marketing"                                                | US Small Business Administration "general rule", ~2013                                                                       | Folklore; contradicted by the SBA's own measured ~1% actual small-business ad spend. The descriptive ~7.7% is Gartner measuring large-company behaviour.                                                                                                 |
| 3x pipeline coverage                                                                 | Unattributed sales folklore                                                                                                  | Silently assumes a 33% win rate; needs ~4x at 25%, 4-7x for enterprise.                                                                                                                                                                                  |
| 3-12 month payback working band (18 at enterprise)                                   | Practitioner-reported across paid acquisition, superseded above by Benchmarkit's measured ACV-segmented figures for B2B SaaS | Keep this row only for non-SaaS paid-acquisition businesses the segmented table doesn't cover; recalibrate against the business's own cohorts and cash position.                                                                                         |
| 2-3x ROAS as "good and achievable" (Google Ads)                                      | Jyll Saskin Gales, ex-Google, "What is a Good ROAS in Google Ads?"                                                           | Stated heuristic explicitly conditioned on the business's own margin and LTV, not a study - she frames "good" as "profitable, more money out than in," never a fixed number.                                                                             |
| LTV of at least $10K, and a $5K/month minimum budget, to justify LinkedIn Ads at all | AJ Wilcox (B2Linked), "How Much Do LinkedIn Ads Cost?"                                                                       | Stated practitioner heuristic, not a measured benchmark - paired with his own observed CPC range ($8-14, up from $6-8 in 2020 and $2 in 2011) and the claim that LinkedIn's cost-per-SQL runs under half of Facebook's despite the higher front-end CPC. |

The circularity to watch for: a blog post quoting a _descriptive_ survey median (Gartner's 7.7%, Benchmarkit's 18-month payback) as a _prescriptive_ target. Descriptive averages describe what a panel did. They carry no claim about what this business should do.
