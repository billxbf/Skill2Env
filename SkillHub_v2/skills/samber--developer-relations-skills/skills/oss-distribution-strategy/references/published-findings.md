# Published findings on OSS distribution

The studies and policies behind this skill's figures, with what each establishes and what it does not. Cite the limitation alongside the number whenever you use one - a maintainer is spending scarce hours on the advice.

## 1. How developers select dependencies

**Larios Vargas et al., ESEC/FSE 2020** (DOI 10.1145/3368089.3409711) - 16 interviews plus 115 survey respondents, 26 selection factors ranked. Share rating each factor "highly influential": maturity/stability 62%, usability 55%, documentation 51%, license 45%, active maintenance 44%, security 39%, time/budget 39%, risk assessment 38%, performance 32%, popularity 30%, community activeness 30%, well-tested 11%.

The authors themselves call the low security ranking surprising. One interviewee states the gap directly: _"Checking security vulnerabilities is important, but I do not check it up-front."_

- **Establishes** - what practitioners say they weigh.
- **Does not establish** - what drives adoption.

Treat it as an argument for making stability, usability, documentation and license _visible_, not as a ranking of channels.

**Go Developer Survey 2025** (go.dev/blog/survey2025, published 2026-01-21, 5,739 respondents) - "Finding trustworthy Go modules and packages" is the third-most-reported frustration at 26%. Read as evidence that trustworthy-module discoverability is an unmet need addressable through documentation quality and social proof, not through a campaign.

**Stack Overflow Developer Survey 2024** (65,000+ respondents) - technical documentation and Stack Overflow itself are the top learning resources; online resources are cited by 80%+.

## 2. What visible signals actually do

**Borges and Valente, _Journal of Systems and Software_ 2018** (arXiv:1811.07643) - survey of 791 developers. Three out of four consider a project's star count before using or contributing to it; 36.7% starred a repository specifically _because_ they were already using it.

- **Establishes** - stars are a checked social-proof signal and visible usage converts into stars.
- **Does not establish** - that stars cause adoption; the same study documents social-media promotion driving star growth.

**Trockman et al., ICSE 2018** - npm ecosystem study. Repository badges are used by 31.0% of packages; adding a first badge produces only a small, non-sustained popularity bump. Read as evidence against badge-stacking as a growth tactic.

## 3. Dependency-graph structure

**Wittern et al., MSR 2016** - only 27.5% of npm packages are depended upon by any other package; 80%+ of packages have at least one direct dependency.

**Decan, Mens and Grosjean, _Empirical Software Engineering_ 2019** (DOI 10.1007/s10664-017-9589-y) - dependency networks grow super-linearly, so an early position inside a growing hub compounds.

**Kikas et al., MSR 2017** - JavaScript transitive dependencies grew 60% in 2016 alone.

**deps.dev (Google Open Source Insights)** - coverage and its closed-source-invisibility caveat are in `channel_catalog.md` § 7.

## 4. Supply-chain signals and adoption

**No causal link to adoption** - the link from OpenSSF Scorecard scores, artifact signing or SLSA provenance to increased downloads or adoption is unestablished, and nothing here should be presented as proving it.

The Scorecard literature measures something else: Zahan et al., "Do Software Security Practices Yield Fewer Vulnerabilities?" (arXiv:2210.14884, ICSE-SEIP 2023) and "OpenSSF Scorecard: On the Path Toward Ecosystem-wide Automated Security Metrics" (arXiv:2208.03412) study vulnerability reduction and adoption breadth, never download effects.

Sigstore's own figures - 3,800+ projects and 500M+ downloads of provenance-enabled package versions during the April-September 2023 beta - are raw totals with no control group, and maturity and funding confound every apparent correlation. Independent sampling in February 2026 found only 76 of 1,059 npm packages carried provenance. On download counts as a trust signal: ReversingLabs documents download pumping, and the Shai-Hulud npm worm (November 2025) backdoored 796 packages.

**Working rule** - present trust work as risk mitigation and procurement enablement. The Scorecard-above-7 target is a self-set passing posture for enterprise review: a procurement bar, not an adoption forecast.

**Regulatory dates** - EU Cyber Resilience Act reporting obligations begin September 2026; SBOM technical documentation is enforceable from December 2027. Both bind manufacturers, not upstream maintainers. OpenSSF states upstream participation is voluntary and must not shift legal obligation onto project communities; Christopher "CRob" Robinson (OpenSSF) frames the realistic risk as reputational and operational, predicting a wave of fix-request pressure from manufacturers facing penalties.

## 5. Maintainer capacity

**Tidelift maintainer survey 2024** (400+ maintainers) - 60% of maintainers are unpaid, and paid maintainers are 55% more likely to implement critical security and maintenance practices. Paid vs. unpaid adoption rates for four practices:

- Signed releases with published provenance: 50% vs 28%.
- Reproducible builds: 77% vs 47%.
- Two-factor auth: 76% vs 68%.
- Static analysis: 75% vs 59%.

This is the capacity constraint the whole plan is built around - unpaid time is the binding resource, and trust work competes directly with everything else.

## 6. Frameworks this skill builds on

**Bullseye** - Gabriel Weinberg and Justin Mares, _Traction_ (Portfolio, 2015). Nineteen channels brainstormed in an outer ring, tested cheaply in a middle ring, then concentrated on one inner-ring channel. The two adaptations in SKILL.md step 2 - hours as the budget, and a foundation ring for set-once channels - are this skill's, not the authors'.

**Awareness → Activation → Engagement → Retention**, with time to first successful use as the activation metric, is the common DevRel measurement frame; swyx (Shawn Wang) argues the North Star should be monthly active developers, with newsletter signups as an honest proxy (swyx.io/measuring-devrel).

**11th Annual State of Developer Relations Report (2024)**:

- Content marketing remains the most effective outreach tactic.
- SEO/PPC effectiveness dropped to 4.9% from 10% in 2023.
- Teams not measuring at all fell to 7.3% from 9%.

**Crossing the Chasm** - Geoffrey A. Moore (1991; 3rd edition 2014). Imported only for the reference catch-22 in step 4. The rest of its apparatus (beachhead selection, whole product, bowling-pin expansion) is a product go-to-market method, not a distribution-channel method, and is deliberately left out.

## 7. Hub and marketplace policies

The mechanics described in `channel_catalog.md` § 11 come from each vendor's own documentation, which is perishable and can change without notice. Re-read the live page before planning around any detail. Sources, in the order the catalog table lists them: `github.com/dbt-labs/hubcap`, `developer.hashicorp.com/terraform/registry/modules/publish`, `docs.airbyte.com/integrations/connector-support-levels`, `grafana.com/legal/plugins/`, and `huggingface.co/docs/hub/models-download-stats` for the download-counting rules.

## 8. Limits on what to claim

- **No channel-level claim here is causal.** How much of a project's adoption came from which channel stays unmeasured; every claim in this skill is either mechanical (what the surface does) or inferential (what evaluators say they weigh).
- **JetBrains State of Developer Ecosystem** (2025, 24,534 respondents) covers tooling and language adoption - do not cite it for discovery-channel claims.
- **Homebrew's numeric notability thresholds are still live, just relocated.** The 30 forks / 30 watchers / 75 stars rule moved from `Acceptable-Formulae.md` to a separate `Package-Acceptance-Policy.md` page (confirmed via direct fetch of Homebrew/brew's current source, 2026-09), which also adds a rule not previously known: self-submissions by the repository's own owner need 3x the threshold - 90 forks, 90 watchers, or 225 stars. Both metrics apply to the canonical upstream repository only, never a mirror or fork. Cite the current page, not the old one.
- **Three of this skill's five pass thresholds are self-set baselines**, marked as such in `SKILL.md`: defensible construction, not measured benchmarks.
