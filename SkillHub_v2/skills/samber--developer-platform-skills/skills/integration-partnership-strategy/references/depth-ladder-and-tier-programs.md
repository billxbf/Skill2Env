# Depth ladder, platform tier programs, and certification obligations

## The five-rung depth ladder

| Depth rung                   | Who owns the customer   | Commercial model                                                                                                        | Product/roadmap commitment                         |
| ---------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Referral                     | Vendor                  | Referral fee/commission                                                                                                 | None                                               |
| Reseller/VAR                 | Partner (transacts)     | Margin/discount; recurring commission around 30%/yr is a common market rate                                             | Low; services wrap                                 |
| Co-sell/integration alliance | Shared                  | Sourced/influenced revenue share, joint pipeline                                                                        | Medium; an integration built and maintained        |
| Co-build/strategic alliance  | Shared, deep            | Joint GTM investment, shared pipeline targets                                                                           | High; joint roadmap (12-18 months at the deep end) |
| OEM/embed                    | Partner owns end-to-end | Licensing fee or roughly 10-30% rev-share of the partner's revenue from the powered feature; minimum commitments common | Deep; product embedding plus roadmap commitment    |

OEM vs. white-label: true OEM couples licensing with product embedding and a roadmap commitment. White-label hides the vendor brand but typically lacks that roadmap commitment, so treat it as its own category, not a synonym.

Cloud-marketplace co-sell (AWS/Azure/GCP transaction layer) is a distinct motion this ladder doesn't capture. Handle it as a channel decision, not a depth rung.

## Graduation triggers

What promotes a partner to a deeper rung (synthesized industry practice, not one canonical source):

- **Proven repeatable joint economics** - the partner already sources or influences pipeline at a rate that justifies deeper investment.
- **The three-fit test** (Forecastable): product fit, commercial fit, and operational fit must line up on the same side simultaneously. If any one is missing, the deeper motion underperforms regardless of contract terms.
- **Customer pull** - joint customers demanding a deeper, productized integration.
- **Strategic necessity** - competitive or platform dynamics that make deeper embedding defensive.

## Tier structures across seven major platforms

The 2024-2026 period was a heavy restructuring wave across nearly every major platform. Verify current tier names against each platform's official docs before acting. Many third-party guides still describe deprecated tiers.

| Platform                         | Tier names (current)                                          | Basis for tiering                                         | Notable requirements/benefits                                                                                                               |
| -------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Salesforce (ISV)                 | Registered → Exploration → Build → Select → Summit            | Journey stage / commercial relationship, quarterly review | $999 one-time security-review fee per app, ~$150/yr listing, 15% rev share (25% for OEM); Select/Summit unlock co-marketing and GTM support |
| HubSpot (App/Technology partner) | partner → rising → leading → premier (+ invite-only Catalyst) | Customer value, influenced revenue, quality               | Free to join; list with an integration plus 3 active users; quarterly tier-up on influenced-revenue submissions                             |
| Shopify (Technology Track)       | Registered → Plus → Premier → Platinum (top tier invite-only) | Performance requirements                                  | Certified Technology Partner Program replaced the prior program in Dec 2025; Platinum gets roadmap influence                                |
| Atlassian (Marketplace)          | Silver → Gold → Platinum                                      | Cloud sales thresholds + security/trust + support SLA     | Silver $150K / Gold $750K / Platinum $3M cloud sales; Gold+ needs SOC 2 Type 2 or ISO 27001; annual July review                             |
| Microsoft (MAICPP)               | Solutions Partner designations → Advanced Specializations     | Points-based Partner Capability Score                     | Replaced Gold/Silver competencies; ISV Success program, Azure credits, co-sell                                                              |
| ServiceNow (Build)               | Registered → Select → Premier → Elite (+ Access tier)         | Certification depth, outcomes, pipeline                   | Jan 2026 overhaul for AI agents; simplified fees; Store visibility                                                                          |
| Zendesk (Technology Partner)     | Tiered by engagement/investment                               | Proactive engagement + marketplace investment             | Free to join; Solutions Architect consultation at higher tiers                                                                              |

**Deprecation warning, worked example**: in July 2024 Salesforce retired its legacy Trailblazer-Score ISV tiers (Base/Ridge/Crest/Summit) for the five-stage journey model above - yet many third-party guides still describe the old names. Citing them dates the strategy and misroutes the partner team. HubSpot's separate Solutions Partner program (sold and managed recurring revenue - a different program from the technology/app track above) uses Gold → Platinum → Diamond → Elite, gated on roughly 75-80% gross revenue retention at the top tiers, with thresholds rising in 2027.

## Certification programs you join: the recurring-renewal comparison

Certification is what a vendor joins on someone else's platform, as opposed to any tier program it runs for its own partners. Four named programs:

| Program                              | Platform           | Core requirement                                                                                                 | Renewal/revocation                                                                                                                          |
| ------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Built for NetSuite (BFN)             | Oracle NetSuite    | BFN questionnaire, positive customer references, live product demo to the SDN team                               | Must be renewed every major NetSuite release (twice yearly); revocable anytime standards lapse                                              |
| AppExchange Security Review          | Salesforce         | Mandatory code and behavioral audit (CRUD/FLS enforcement, secure auth, external-endpoint scans, data-flow docs) | $999/submission, 6-9 weeks initial plus 2-3 weeks per resubmission; roughly half of first submissions fail; ongoing per-release obligations |
| Slack Marketplace / Works with Slack | Slack (Salesforce) | OAuth flows/scopes/tokens, UI framework compliance, enterprise readiness, developer certification                | Certification-maintenance modules required each release                                                                                     |
| Atlassian Cloud Fortified            | Atlassian          | SOC 2 Type 2 or ISO 27001, bug-bounty participation, <24h support response, third-party-validated trust center   | Annual review; Atlassian commits to 6 months' notice before new requirements                                                                |

**The pattern, stated once**: the recurring-renewal design is deliberate - platforms use it to keep their ecosystem safe and current as their own product changes - but it creates an ongoing engineering carrying-cost for the joining vendor. Budget it as standing work in integration-engineer headcount, never as a launch-phase project cost that finishes.
