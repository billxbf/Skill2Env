# Benchmarks and Figure Grading

Partner-economics benchmarks graded by how much weight each one carries. Almost every widely repeated figure in this domain is vendor marketing or practitioner rule-of-thumb rather than research, so most of them sit low on the evidence ladder.

- Quote nothing from this file without its evidence-class label; prefer the best-attributed rows.
- When a number the user needs is not here and cannot be verified, write "unverified, user-supplied" in the memo. Never invent one.

Evidence-class ladder, strongest first: peer-reviewed → vendor/platform documentation → industry survey (named, disclosed sample) → analyst (beware vendor-commissioned) → vendor benchmark/blog → untraceable.

## Best-attributed numbers: prefer these

| Benchmark                                                    | Value                                           | Source                                                         | Evidence class                                                                                                                                                                                                                                               |
| ------------------------------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Cloud marketplace listing fee                                | ~3% public SaaS; 1.5-3% private offers          | AWS documentation, 2024; Azure/GCP in the same band            | Vendor documentation: the most reliable numbers in this domain                                                                                                                                                                                               |
| Channel CAC per $1 new ACV                                   | $0.53                                           | 2014 Pacific Crest / KeyBanc Private SaaS Survey               | Industry survey; the companion "$1.02 field sales" figure does not appear in the published write-up                                                                                                                                                          |
| Partners terminated or dormant within 12 months              | 70% (29% terminated + 41% stopped selling)      | CRN Research 2025 Partner Journey Study                        | Industry survey; full methodology not public                                                                                                                                                                                                                 |
| Channel-majority retention gap                               | ~3pp lower revenue retention vs direct-majority | SaaS Capital survey, Aug 2019, 700+ private B2B SaaS companies | Industry survey: named, disclosed sample and date                                                                                                                                                                                                            |
| Channel incentives meeting their goals                       | 14%                                             | Forrester 2016 survey                                          | Analyst survey                                                                                                                                                                                                                                               |
| eBay brand-keyword clicks retained after halting paid search | 99.5%                                           | Blake, Nosko & Tadelis 2015, Econometrica                      | Peer-reviewed: the incrementality anchor                                                                                                                                                                                                                     |
| Alliance failure within 24 months                            | 48% of 1,592 alliances (1993-1997)              | Dyer, Kale & Singh 2004, HBR, citing empirical studies         | Academic-adjacent: but one point inside a 20-80% published spread that turns on how failure is defined. Quote it with the spread and the definition, never as the rate; `mbfinotti/partnerships-skills@alliance-prioritization` owns this number's treatment |

## Usable with labels: vendor/practitioner class

| Benchmark                         | Value                                                                    | Evidence class and caveat                                                                     |
| --------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Partner CAC advantage vs direct   | 20-40% lower typical; "up to 50%" claimed                                | Vendor/practitioner; only the Pacific Crest survey has a disclosed dataset behind any variant |
| VAR gross margin                  | 25-35% (20-40% outer band)                                               | Convergent across independent vendor blogs; unaudited                                         |
| Distributor margin                | 8-15%                                                                    | Vendor/practitioner                                                                           |
| Deal-registration margin uplift   | +5 to +15pp over base tier discount                                      | Convergent blog-tier; moderately trustworthy rule of thumb                                    |
| OEM royalty                       | 1-10% of license revenue                                                 | Vendor/practitioner, wide variance                                                            |
| Affiliate rates                   | SaaS 20-30% recurring; ecommerce 10-15% first order; fintech $50-200 CPA | Vendor benchmark (affiliate-platform vendors)                                                 |
| Partner activation rate           | 30-50% typical; <20% unmanaged                                           | Vendor benchmark (PRM vendor)                                                                 |
| MDF unused                        | ~60% quarterly                                                           | Vendor survey (worldwide channel survey); the "$50B/half unused" figure cites no source       |
| Partner ROI / payback health line | >3x ROI, CAC payback <120 days                                           | Practitioner blog benchmark, unaudited                                                        |
| Ecosystem services multiplier     | $6.40-$7.13 services per $1 platform revenue                             | Analyst, vendor-commissioned (Canalys/Omdia for AWS et al.): directional and interested       |
| MSP managed-services gross margin | 45-60%; top quartile >60%                                                | Vendor benchmark (Service Leadership Index, subscription data)                                |
| Effective B2C rev-share vs stated | 20-40% below stated rate after deductions                                | Vendor/practitioner                                                                           |

## Untraceable: flag or omit, never quote as fact

- **"80% of channel revenue comes from 20% of partners"** and **"only 11% of partners hit incentive goals"**: originate from a media-company blog citing nothing. Widely repeated, never sourced. The direction (heavy concentration) is credible; the specific figures are not.
- **"Most partners never transact"**: circulating variants span "<30% ever generate a deal" to "80% generate zero revenue," none traceable to an original study. The best-attributed adjacent number is the CRN 70% churn/dormancy figure above.
- Partner-sourced win-rate deltas (+46% sourced, +99% influenced, −11% time-to-close): repeated across vendor content with no traceable methodology.
- "Channel sales up to 50% lower CAC than field sales" as a flat claim: traces loosely to Pacific Crest but is quoted far beyond what that survey supports.

## Genuinely unsettled: say so

- Incrementality vs cannibalization: the academic literature documents both synergy and substitution depending on channel and product. There is no default answer; that is why the workflow forces an explicit incrementality step.
- Sourced-vs-influenced reporting: practitioners agree they must be tracked separately, but whether influenced revenue deserves board-level weight is an active industry debate, not a settled rule.
- The partner-CAC-advantage magnitude: real but range-disputed; anchor on the $0.53 survey figure and label everything else.
