# Framework Selection

The four named frameworks, what each actually is, and the fit tables that narrow the choice. Remember the caveat from SKILL.md: the frameworks differ less than their marketing suggests - the real variance is unit of analysis, post-sale scope, and exit-criteria rigor. Selection buys a vocabulary and access to a benchmark pool.

## The Four Named Frameworks

**Demand Waterfall lineage (SiriusDecisions, now Forrester).**

- 2006: introduced as the Demand Generation Waterfall.
- 2012: re-architected, adding stages for inbound, teleprospecting, and sales-sourced leads.
- 2017: rebuilt around the _demand unit_, the buying group rather than the individual lead - "Prioritized Demand" replaces the marketing-qualified lead with a marketing-qualified account scored at the group level.

Seven stages run from Target Demand (TAM by firmographics) through progressively qualified demand to Pipeline Opportunity (close date and dollar value assigned) and Closed. It is the closest thing B2B has to a standard pre-sale waterfall, and a common language between marketing and sales leadership.

Misapplied when the company still qualifies leads individually: forcing demand-unit stages onto single-threaded deals adds reporting overhead without the account-based motion that justifies it.

**B2B Revenue Waterfall (Forrester, 2021+).** The current successor adds the opportunity mix: the Targeted stage carries targeted accounts, each holding one or more targeted opportunities typed as new-business, renewal, cross-sell, or upsell, so conversion rate and cost can be evaluated per opportunity type and resources allocated against the mix. This is the version with genuine post-sale coverage via opportunity type, fitting multi-product enterprise B2B where renewal/upsell/cross-sell are material.

Forrester itself warns organizations over-rotate on tooling for this migration when the real requirement is aligning process, data, and programs across teams. Do not recommend the swap below roughly 3-4 stakeholders per deal.

**TOFU/MOFU/BOFU.** Shorthand for the top three stages of the Awareness/Consideration/Conversion/Loyalty/Advocacy marketing funnel; TOFU carries the most volume and lowest conversion. A content and demand-gen planning lens (a commonly cited B2B SaaS content-spend mix is roughly 50/30/20 across the three), never a CRM stage model - making it double as the pipeline's stage set conflates marketing funnel stages with buyer-verifiable sales milestones.

**Bowtie (Winning by Design; 2023 "Bowtie Standard" adds a Prioritization stage).** Extends the funnel with an equally weighted post-sale half: acquisition/pipeline/close on the left, onboarding/adoption/expansion on the right, knotted at closed-won. The case for it: in recurring-revenue businesses growth increasingly comes from the right side, since expansion is 40%+ of new ARR above $50M.

Maps to five touch models (No/Low/Medium/High/Dedicated Touch) so one stage set flexes by motion. Misapplied on one-time-purchase or low-NRR businesses with no post-sale expansion economics to instrument.

## Motion Fit

| Motion                | Stage count | Unit                           | Framework fit                                                 |
| --------------------- | ----------- | ------------------------------ | ------------------------------------------------------------- |
| No-touch / PLG        | 3-4         | User, then account             | Growth-loop/pirate-metrics lens plus a product-qualified gate |
| Low-touch assisted    | 4-5         | Account (PQA)                  | Bowtie left side compressed, PQL/PQA gate                     |
| Mid-touch (SDR to AE) | 5-7         | Lead, then opportunity         | 2012 Demand Waterfall or Bowtie                               |
| High-touch enterprise | 6-8         | Buying group, then opportunity | B2B Revenue Waterfall                                         |
| Channel / partner-led | Mirror set  | Partner-sourced opportunity    | Separate pipeline, never extra stages                         |

5-7 stages cover most mid-market and enterprise motions; an eighth stage for long legal/security review is the exception. Prospecting activity belongs outside the pipeline entirely.

## Revenue-Model Fit

- **Subscription** - Bowtie or a Forrester waterfall both work; revenue books at commit, so the pre-sale stage set carries the planning weight.
- **Usage/consumption-based** - extend past close into the ramp as first-class stages: commit, first production workload, ramp curve, steady-state run rate, each with its own conversion and time metric. Customers use the product before revenue books, and that gap is where reporting breaks.
- **Marketplace/take-rate** - two funnels (supply and demand) with a liquidity constraint between them. No mainstream framework handles this; the model is custom by necessity, and the deliverable should say so.

## Scaling by Company Stage

| Dimension          | Pre-PMF / Seed                              | Series A-B                          | Series C+ / public                                     |
| ------------------ | ------------------------------------------- | ----------------------------------- | ------------------------------------------------------ |
| Stage count        | 4-5                                         | 5-6                                 | 6-8, separate pipelines per motion                     |
| Unit               | Contact                                     | Lead, then opportunity              | Buying group, then opportunity                         |
| Conversion source  | Benchmarks and judgment, labeled as guesses | Own data, wide confidence intervals | Own data, segmented, cohort-based                      |
| Post-sale modeling | None                                        | Onboard + renewal                   | Full post-sale side with expansion mix                 |
| Governance         | Founder decides                             | Named owner, quarterly review       | Funnel council, versioned definitions, data dictionary |

The dominant early-stage failure is premature complexity - a 10-stage pipeline modeling a future enterprise process. Add a stage only when an operational need forces it.

## PLG Unit Choice: PQL vs PQA

A product-qualified lead is user-centric - one person's product activity. A product-qualified account is a group of connected users showing purchasing potential as a whole.

Individual users swiping a card for $25-50/month are not where large PLG organizations earn the bulk of revenue, so a PQL-only model systematically misdirects sales capacity. Segment PQLs into at least three buckets by what the account needs next, starting with hand-raisers who actively want to talk to sales.

## The MQL vs Buying-Group Call

The buying-group evidence is real. Forrester's 2023 Buyers' Journey Survey found:

- 93% of B2B buyers in a group of 2+
- 71% of B2B buyers in a group of 4+

The strongest published outcome (a Forrester client story, read as a vendor case) reports multi-contact opportunities 8x likelier to advance and a 17% higher closed-won rate.

The counter-case is underweighted: where decisions are made by an individual or small group and cycles are short, the MQL remains a practical operating model. The migration is a costly data-model change, not a metric rename - below roughly 3-4 stakeholders per deal the individual-lead model is simpler and loses little.

The MQL is a bad goal but an acceptable state.
