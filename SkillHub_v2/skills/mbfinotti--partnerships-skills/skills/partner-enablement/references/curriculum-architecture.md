# Curriculum Architecture

What to build, for whom, in what order. All sequencing guidance here is practitioner consensus from channel practitioners and PRM-vendor sources - internally consistent, not independently validated.

Every ordering below is a default, not a law. Each assumes a vendor building from nothing with roughly one enablement person, and each shifts with who executes it.

Re-rank against what you already know about this user before reciting any of it:

- an existing demo environment collapses the demo row's effort
- an already-technical partner base moves the technical domain up
- direct-sales collateral that adapts cleanly (adapts - never recycled) cuts the sales rows

Effort is stated as build time in orders of magnitude - an hour, a week, a quarter, a standing job - never as a budget figure, which goes stale faster than the ordering it justifies.

## Table of Contents

- [The four training domains](#the-four-training-domains)
- [Role-based tracks](#role-based-tracks)
- [Depth varies by partner type](#depth-varies-by-partner-type)
- [Build order](#build-order)
- [Two content audiences](#two-content-audiences)
- [Distribution rules](#distribution-rules)
- [Negative example: the recycled direct-sales programme](#negative-example-the-recycled-direct-sales-programme)

## The four training domains

Order investment by deals unblocked per build hour, not by which domain is easiest to write:

1. **Sales** - value proposition, ideal customer profile, objection handling, competitive positioning. A week of adaptation; the only domain without which no deal happens at all.
2. **Product** - features, use cases, architecture, integration capabilities. A week per partner type; unblocks a credible discovery conversation, and the other three assume it.
3. **Technical** - implementation, configuration, troubleshooting, support workflows, hands-on labs. A quarter, and it comes off a real engineer's calendar rather than the enablement owner's.
4. **Certification** - a validation layer over the other three, not a fourth body of content. A standing job once launched, plus the only compliance exposure in this file: a marketed credential is a public capability claim, needs legal or brand sign-off, and is hard to withdraw once partners advertise it. Whether to certify at all, and what each certification gates, is decided at workflow step 8.

- value: sales > technical > product > certification
- effort: certification > technical > product > sales
- efficiency: sales > product > technical > certification

Technical outranks product on value and still loses to it on efficiency, purely on build cost - and that gap is exactly how the documented imbalance forms. Programs habitually over-invest in sales and marketing content and under-serve technical roles because efficiency is the only axis they ever compute. A partner whose engineers cannot implement will stop selling regardless of how good the pitch deck is.

Move technical to second the moment the base contains an SI, an MSP, or any partner who delivers rather than refers. Certification is last on every axis until a deal proves a gate is needed; where none of the three certify-at-all conditions holds, delete it from the build list rather than parking it at the bottom, or it silently reappears as scope.

## Role-based tracks

Distinct personas inside a partner organization need distinct tracks - one-size-fits-all onboarding wastes every persona's time. Build them in this order, highest deals unblocked per build hour first:

| Role                                 | Track focus                                                                   | Build effort                                          | What it unblocks                                                                               |
| ------------------------------------ | ----------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Partner sales rep                    | Pitch, ICP, qualification, objection handling, battlecard, deal registration  | a week                                                | every registered deal; no row below matters until this exists                                  |
| Executive sponsor                    | Economics of the partnership, roadmap, tier progression - short, not a course | an hour: a slide and a call                           | the sponsor's decision to point their reps' selling time at you rather than a competing vendor |
| Solutions architect / pre-sales      | Demo mastery, architecture, integration docs, sandbox/labs                    | a week, then a standing job to keep the sandbox alive | partners showing the product without you on the call                                           |
| Delivery / implementation consultant | Implementation playbooks, configuration, support workflows                    | a quarter                                             | partner-delivered projects, and the second deal from the same partner                          |
| Partner marketer                     | Co-brandable campaign kits, messaging guardrails, MDF mechanics               | a week per kit, recurring                             | partner-sourced pipeline instead of vendor-sourced                                             |

- value: sales rep > pre-sales > delivery > partner marketer > executive sponsor
- effort: delivery > pre-sales == partner marketer > sales rep > executive sponsor
- efficiency: sales rep > executive sponsor > pre-sales > delivery > partner marketer

Pre-sales and partner marketer tie on effort because both are a week that never ends - one maintains a sandbox, the other reprints kits every campaign; they do not tie on value, and pre-sales wins that axis outright. The executive sponsor track is the sharpest disagreement on the list: last on value, second on efficiency, and the one most often skipped, because an hour of slides looks too small to schedule.

The efficiency order starves the delivery track: third on value, first on effort, so a ratio demotes it every time and the partner who was sold to never gets implemented for. Promote it above pre-sales the moment partners deliver the work themselves, or the moment second deals from an existing partner matter more than first deals from new ones - a botched first implementation costs that partner's whole future pipeline, which no efficiency ranking prices in.

A role that does not exist in the partner base gets deleted from this menu, not demoted - a referral-only base has no delivery consultant to train, and that track is a quarter spent on nobody. Every customer-facing role that does exist still gets a track (pass threshold 3); the ranking decides which one exists first, never which one is skipped.

## Depth varies by partner type

Standardize core messaging; vary depth by type and maturity with modular paths. Build shallow-and-many before deep-and-few unless the base is already skewed to the deep end:

| Partner type        | Depth needed                                                      | Build effort   | What it unblocks                                                                                   |
| ------------------- | ----------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------- |
| Referral            | ~30-minute product overview plus a clean handoff mechanic         | an hour        | referred opportunities across a wide, low-commitment base                                          |
| Reseller            | Full sales track plus deal-registration discipline                | a week         | transacting partners; reuses the sales-rep track almost unchanged                                  |
| MSP                 | Operations and support depth a transactional reseller never needs | a quarter      | recurring managed revenue - same product, different enablement, because the business models differ |
| SI / implementation | Multi-day technical training and labs                             | a standing job | large delivered projects, and partners building a practice on you                                  |

- value per partner: SI > MSP > reseller > referral
- effort: SI > MSP > reseller > referral
- efficiency: referral > reseller > MSP > SI

The value and efficiency orders invert exactly, which is the whole decision: depth costs most where it pays most per partner, so the answer is set by how many partners of each type the base actually holds, not by which type sounds most strategic. What that inversion starves is the SI track - highest value per partner, highest effort, dead last on efficiency, and therefore never built by a program that ranks on the ratio alone. Promote it when a handful of SIs carry more revenue than the whole referral base, or when an SI is building a delivery practice on you and will take that practice to a competitor if the training does not exist.

Confirm a technical partner profile exists in the base before building for it - and where it does not, delete those tracks from the plan rather than scheduling them late. Roughly 18 months of enablement, recruitment, and tier structure built for a partner profile that turned out not to exist is a documented practitioner outcome, and a deferred track is what it looks like on the way there.

## Build order

Design backwards from the first deal: the curriculum's mandatory core is only what a partner needs to identify a qualified opportunity, hold a credible discovery conversation, and submit a deal registration. Everything else is post-first-deal, delivered as the deal progresses ("just-in-time").

| #   | Asset                                           | Build effort                                          | What it unblocks                                                                                            |
| --- | ----------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1   | First sales play + battlecard                   | a week, adapted - never recycled from direct sales    | the partner opening a conversation at all; every row below assumes it                                       |
| 2   | Deal-registration walkthrough                   | an hour: a screen recording of the portal flow        | the registered deal itself, the partner's margin on it, and the attribution behind every KPI in the program |
| 3   | Pitch deck / one-pager, co-brandable            | a week                                                | the partner running the meeting in their own brand voice instead of rebuilding the deck themselves          |
| 4   | Demo script + self-guided demo environment      | a quarter to stand up, a standing job to keep current | partners demoing without you on the call - the most commonly reported gap in channel programs               |
| 5   | Pre-sales technical track                       | a quarter                                             | technically qualified opportunities, and architecture questions answered without escalation                 |
| 6   | Implementation/delivery track and certification | a standing job                                        | delivered projects, and the credential that gates tier or co-sell economics                                 |

- value: sales play > demo environment > deal-reg walkthrough > pitch deck > pre-sales technical > implementation/certification
- effort: implementation/certification > demo environment > pre-sales technical > sales play == pitch deck > deal-reg walkthrough
- efficiency: deal-reg walkthrough > sales play > pitch deck > demo environment > pre-sales technical > implementation/certification

Sales play and pitch deck tie on effort because they are the same week of writing, by the same person, off the same source material - they do not tie on value, and the play ships first.

The demo environment is what this order starves: second on value, second on effort, fourth on efficiency, and simultaneously the most commonly reported gap in channel programs - the ratio and the field's own complaint list disagree here, and the ratio is what usually wins. Promote it above the pitch deck as soon as deals stall at the demo stage or partners keep pulling a vendor rep onto calls, because at that point every deal in flight is paying its build cost weekly.

The table is ordered by efficiency with one dependency override: the sales play leads because the rows beneath it have nothing to sell without it. The walkthrough is the highest ratio on the list - one hour of screen recording standing between a partner and the registration that pays them - so it ships in that same first week rather than fourth, where practitioner build orders habitually leave it. Rows 1-3 are the first-deal path; rows 4-6 are post-first-deal and get built while partners are already transacting.

A minimum viable program targeting the middle-tier partner can launch in roughly 4-8 weeks (PRM-vendor rule of thumb). A hard deadline compresses to rows 1-3 and nothing else; an effort ceiling under a week per asset deletes rows 4-6 from this cycle rather than scheduling them, and the roadmap says so explicitly instead of listing them as planned.

## Two content audiences

- **Internal to the partner**: battlecards, playbooks, training courses, FAQ - never seen by customers.
- **Prospect-facing, used by the partner with their customers**: case studies, how-to content, co-branded collateral, email templates.

The repeatedly stated caveat: availability is not the problem, usability is. Prospect-facing content must be customizable and co-brandable, or partners rebuild it themselves - and rebuilt content drifts off-message.

## Distribution rules

- Everything lives in the partner portal, on demand, with role-based access. Partners will not dig through email attachments for a battlecard; the approved version must be the easiest one to reach.
- Curate ruthlessly. Dumping hundreds of documents into a portal is the documented "content dump" failure - identify the small fraction that drives revenue, retire the rest.
- Let partners request assets they don't see; the request log is your build backlog, ranked by requests against the build effort each request implies - a repeatedly requested one-pager outranks a single request for a lab.
- Every asset class gets an owner and a scheduled refresh; content current at launch and never refreshed actively misleads partners, and it loses deals quietly because partners trust it.

## Negative example: the recycled direct-sales programme

The best-documented failure mode in the field, sourced to analyst channel research (Forrester/SiriusDecisions roundtables and reports):

A vendor "launches" partner enablement by exporting its internal sales-enablement library into the partner portal: the direct-sales pitch deck, the internal objection doc, rep onboarding videos, comp-plan-flavoured talk tracks. Result, as documented: lackluster content usage, failed messaging, underperforming recruitment and onboarding. Why it fails structurally: direct-sales content assumes the seller is a paid employee of the vendor, selling only this product, with internal systems access and a manager enforcing the motion.

A partner rep is none of these:

- they ration time across competing vendors
- need a margin story the internal deck never mentions
- cannot access internal tools the content references
- speak to their own customer base in their own brand voice

The fix is not better distribution of the same assets; it is adaptation per role and partner type, plus partner-only assets (margin calculator, co-brandable versions, deal-registration mechanics) that have no direct-sales equivalent. Treat any asset inherited unchanged from direct-sales enablement as a defect in the roadmap.
