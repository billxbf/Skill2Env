# Ratio, span, and attrition benchmarks

All figures below are B2B SaaS survey data (mostly self-reported by company leaders, disclosed n) - directional planning inputs, not physical constants. None of them transfer to B2C; calibrate B2C designs on the org's own historicals.

## SDR:AE ratio - contested, and why

**There is no single correct published number.** Treat the ratio as an output of the org's own funnel math (worked derivation in this skill's `topology-transition-cases.md`, linked from SKILL.md), with the figures below as sanity bands only.

**The real trend (Bridge Group longitudinal series, biennial since 2007):**

- 2014: 1 SDR per 3.9 AEs.
- 2016: 1:2.5.
- 2018: 1:2.6.
- 2025: 1:2.4 (1:2 is the single most common model, covering 31% of teams).

The 2025 edition covers 351 B2B companies, 78% North America, 83% SaaS, median revenue $47M.

**The apparent contradiction:** a separate 2026 breakdown (WinsAbove) puts the median at 0.8 SDRs per AE, with enterprise at 1.8:1, SMB at 0.4:1, and PLG-heavy orgs under 0.2:1 - a materially different headline from Bridge Group's. Both can be honestly published because five factors distort any comparison:

1. **Segment mix** - enterprise inbound runs thin (~1:3-1:4, the AE self-prospects and multithreads directly); SMB/outbound runs rich (~1:1.5-1:2).
2. **Inconsistent SDR/BDR labeling** - the dominant convention treats SDR as inbound and BDR as outbound, but major sources invert it, and only ~25% of companies formally separate the roles. ~34% of Bridge Group's 2025 sample split outbound into two roles; real combined ratios run ~22% higher than the headline figure.
3. **Hybrid AEs** - at companies under $20M ARR, 41% of sampled "AEs" carried part-SDR responsibilities in 2025, suppressing the apparent need for dedicated SDRs.
4. **Offshore/outsourced SDR capacity** is often excluded from published headcounts.
5. **AI SDR tooling** entered Bridge Group's survey as a category for the first time in 2025 (1% of respondents) and is already depressing net SDR hiring.

**Practical sequencing:**

1. Set the ratio by motion first (bands: 1:1.5-1:2 SMB/outbound, 1:2-1:2.5 mixed SaaS, 1:3-1:4 enterprise inbound).
2. Define BDR vs SDR explicitly and decide whether hybrid AEs, offshore, and AI SDRs count in the denominator.
3. Only then compare against Bridge Group 2025 (1:2.4), never against pre-2016 figures.

## Span of control

| Benchmark                    | Figure                                                                                                         | Source                  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------- |
| AEs per frontline manager    | median 7, stable since 2015, rising with revenue                                                               | Bridge Group AE reports |
| SDRs per first-line leader   | median 6.4 (2025), down from 8 in 2021-2023; 3.6 at sub-$5M companies vs 8.1 at $500M+                         | Bridge Group 2025       |
| General sales span guideline | 6-10 direct reports; first-line average 8.5, observed range 2-38                                               | Alexander Group, Umbrex |
| Player-coach coaching time   | as little as 14-16% of time coaching, vs ~28% best practice and 40-60% for dedicated managers                  | Alexander Group         |
| First-manager tipping point  | 2 reps consistently at quota, typically ~$1M-$2M ARR; favor a hungry Director/player-coach over a premature VP | SaaStr (Jason Lemkin)   |
| Assembly-line spans          | ~1 manager per 6-8 reps per stage                                                                              | practitioner guidance   |
| Pod spans                    | ~1 manager per 4-6 pods (roughly 12-25 reps), pod leads as player-coaches inside each unit                     | practitioner guidance   |

Widening span without stronger manager enablement reliably degrades coaching, slows ramp, and raises attrition. Dell's 2025 reorg (VPs minimum 15 reports, directors minimum 20 sellers) is deliberate AI-era delayering - a counter-example to study, not a benchmark.

## Attrition, ramp, and tenure

| Metric           | SDR (Bridge Group 2025)                                                               | AE (Bridge Group 2024/2026)      |
| ---------------- | ------------------------------------------------------------------------------------- | -------------------------------- |
| Annual attrition | ~39-40% total, nearly two-thirds involuntary; significantly higher below $20M revenue | ~30-32% (11-12% involuntary)     |
| Ramp time        | ~3 months                                                                             | ~6.2 months (2026 edition)       |
| Tenure           | ~1.9 years median (2025 - the highest since the early 2010s)                          | ~2.8 years (up from 2.2 in 2022) |
| Quota attainment | 60% of SDRs at quota (2025 - lowest on record)                                        | 48% (2026), down from 66% (2022) |

Hunter roles carry structurally higher attrition than farmer roles independent of management quality (Forrester's hunter/farmer transition research; AM/CSM roles are lower-turnover and base-heavy). A widely repeated older figure - SDR tenure ~14 months - predates the 2022-2024 labor-market shift and is stale; use the 1.9-year median.

Expansion ownership at maturity: only ~26-27% of companies still leave expansion with the AE; CSMs/AMs own it at ~46-50%. 59% of companies run 3+ distinct lifecycle roles (SDR/AE/AM-CSM), rising to 67% excluding sub-$5M companies; companies above $50M revenue are 1.8x as likely to run 3+ roles.

## Per-rep productivity medians (Bridge Group 2025, Operatix)

- SDR meetings-held quota: global median 10/month (introductory 16, fully-qualified 9).
- SQLs/opportunities per SDR: median 6/month - down 43% since 2018.
- Pipeline sourced per SDR: $3.78M/year (a circulating "~$3M" figure is stale 2021-era data).
- Outbound SDR reality check: ~15 meetings booked/month, ~20% dropout, ~12 held (Operatix, 500+ campaigns).
- 74% of AE pipeline is sourced by marketing, inbound SDRs, and outbound SDRs combined; 68% of companies use SDRs, and high-growth companies are twice as likely to.

## AI headcount effects, 2025-2026 - evidence MIXED, treat as provisional

- **The cut side:** Emergence Capital's Beyond Benchmarks 2025 (with Benchmarkit; 560+ venture-backed B2B software companies) found 36% decreased SDR/BDR headcount in the prior year - the steepest cut of any sales role - vs 25% for AEs and 14% for Sales Engineers. SDR internal promotion rates fell from 34% (2020) to 16% (2024).
- **The shape shift:** AE headcount is growing faster than SDR headcount industry-wide - practitioners call it the move "from a pyramid to a diamond." This is one genuine driver of the SDR:AE ratio's continued drift, not just a definitional artifact.
- **The counter-signal:** AI-native companies more than doubled SDR headcount in H1 2026 even as broader digital-native SDR hiring fell ~21% year over year - the cuts concentrate in traditional motions, not the whole market. AI SDR tooling was 1% of Bridge Group's 2025 sample: too early to read as settled.
- **What would settle it:** quota attainment recovering above ~55% (would point to quota/ratio loosening, not AI substitution, as the driver), or AI SDR productivity proving out at scale (would confirm durably higher AE:SDR ratios). Until one of those lands, present any AI-driven org design as a pilot with a rollback path, never as the new steady state.

## Named frameworks behind the topologies

- **Aaron Ross, _Predictable Revenue_** - origin of the Assembly Line and the SDR role itself (Salesforce, early 2000s). The book's "$100M" attribution is Ross's own claim, not independently audited.

  His own caveats:
  - The model needs enough pipeline volume to fund dedicated prospectors.
  - SDRs make no economic sense below ~$4K ACV.
  - Most adopters "don't go far enough" - partial adoption is the norm.

- **Jacco van der Kooij, Winning By Design** - origin of the Pod and _Blueprints for a SaaS Sales Organization_. The Bowtie's published ratio benchmarks sit behind a paid tool - cite the framework, not a specific number. Reader critique worth keeping: the book underweights the pod's trade-offs.

  The Bowtie model ties org shape to go-to-market touch level, in order:
  - No-touch.
  - Low.
  - Medium.
  - High.
  - Dedicated.

- **Mark Roberge, _The Sales Acceleration Formula_** - the "first hire is a builder, hires 5-30 are a repeatability problem" logic that assembly-line scaling depends on (HubSpot, $0 to $100M ARR).
- **Jason Lemkin (SaaStr) and Brett Queener** - "hire two reps, not one" (A/B-test whether success is the rep or the process), first sales leader after 2 reps hit quota, and the ~25-AE floor before a hunter/farmer split.

## Sources

- Bridge Group SDR (2025, n=351) and AE (2024 n=172; 2026 n=158) research reports.
- Alexander Group benchmark database.
- Emergence Capital / Benchmarkit "Beyond Benchmarks 2025".
- WinsAbove 2026 SDR:AE breakdown.
- Operatix outbound campaign data.
- Forrester "Account Transition: Hunter to Farmer" (paywalled - turnover-asymmetry claim only).
- SaaStr (Jason Lemkin).
- Aaron Ross, _Predictable Revenue_.
- Jacco van der Kooij / Winning By Design.
- Mark Roberge, _The Sales Acceleration Formula_.
- The CRO Report sales-org structure guide.
