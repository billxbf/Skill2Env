# Routing detail - sales-skills collection

Route only from the declared scopes below. Every exclusion here comes from the skill's own description, not from inference.

Nothing in this file is ranked, and nothing in it should be. Scope is a match test, not a ratio. Ranking lives in the kickoff's short-list and routine set, where several skills compete for one session (see `mbfinotti/sales-skills@sales-kickoff` § 4 and § 7).

The collection sits at two altitudes. The nine skills under Planning-altitude signals decide the frame - motion, ICP, market size, segments, tiers, topology, quota, coverage, comp.

The eighteen under Execution-altitude signals work inside whatever those decisions produced. Settle the altitude first: a wrong-altitude route is the most common misroute here, because the same vocabulary appears on both sides.

## Table of Contents

- [Execution-altitude signals](#execution-altitude-signals)
- [Planning-altitude signals](#planning-altitude-signals)
- [Boundary pairs](#boundary-pairs)
- [Ordered chains](#ordered-chains)
- [Sibling repository recommendations](#sibling-repository-recommendations)
- [Coverage gaps (v1)](#coverage-gaps-v1)

## Execution-altitude signals

The kickoff's § 3 table says when to route to each execution skill, and Boundary pairs below settles every head-to-head collision between them. What neither carries is the exclusion that is nobody's territory - the thing a skill refuses that no sibling picks up. Those are here; treat a task landing on one as a coverage gap, not a re-route.

- `sales-outreach-personalization` never invents a signal - it ranks signals the user supplies, with a confidence and recency label on each.
- `cold-email-deliverability` covers hygiene and compliance only, never spam-filter evasion of any kind.
- `cold-call-opener` stops at the first 5-30 seconds: the rest of the call (demo, close) and voicemail scripts are covered nowhere in the collection.
- `sales-discovery-questions` ships a do-not-ask list alongside the question set; it never grades a call that already happened.
- `sales-objection-handling` will call a deal dead when the objection is a real constraint rather than script around it.
- `meddpicc-scorecard` scores one described deal - never a whole pipeline, and it never touches a CRM.
- `deal-red-flags` reads one deal's free-text notes, never a pipeline export.
- `deal-value-calc` never elicits the raw figures from the buyer; it labels every number buyer-supplied, benchmark, or rep-assumed.
- `sales-call-review` grades one tape and stops - ongoing coaching plans and manager 1:1 frameworks are a coverage gap.
- `sales-hiring` excludes sourcing, job ads and applicant tracking; `sales-career` excludes job searching, auto-applying and resume file generation.
- `sales-radar` answers what to read or follow and nothing operational.
- `sales-kickoff` routes; it never performs a sibling's job itself.

## Planning-altitude signals

### `mbfinotti/sales-skills@sales-motion`

- Also here: PLG/self-serve, sales-led, hybrid, channel and developer-led motions judged on ACV, time-to-value, buyer-vs-user separation, TAM shape and procurement friction; founder-led exit, PLG-adds-sales layering, enterprise shift, channel build; ranked free-to-paid conversion levers and the gates between motions.
- Not here: running a cadence, writing copy, or working one deal inside a motion already chosen; the org chart that carries the motion (`sales-org-structure`); the pay mix it implies (`sales-comp-design`).

### `mbfinotti/sales-skills@sales-icp-definition`

- Also here: firmographic, technographic and behavioral criteria; hard disqualifiers and anti-ICP; the weighting ladder (equal, analyst-defined, regression-based); a retro-scoring pass against closed-won history; founder-led discovery when no history exists; drift checks.
- Not here: scoring or grouping accounts against the finished ICP (`sales-account-segmentation`), counting the market (`sales-market-sizing`), contact-level lead behaviour (`mbfinotti/revops-skills@lead-scoring`), one deal's fit.

### `mbfinotti/sales-skills@sales-market-sizing`

- Also here: bottom-up build from account counts and ACV, top-down scoping, triangulation between methods, source-tier selection and rigor, sanity checks, the standing model when sizing recurs; B2B and B2C.
- Not here: the ICP criteria that filter SAM (`sales-icp-definition`), organizing or ranking the accounts inside the number (`sales-account-segmentation`), TAM-to-headcount conversion (`sales-org-structure`).

### `mbfinotti/sales-skills@sales-account-segmentation`

- Also here: fit×readiness two-axis scoring and quadrant plays, firmographic and technographic layers, whitespace mapping and gap pipeline, a per-segment motion map, the calibration pass that keeps scores honest.
- Not here: deriving the ICP beneath the fit score (`sales-icp-definition`), tier cutoffs and per-tier service levels (`sales-account-tiering`), executing the territory carve (`sales-org-structure`), contact-level scoring (`mbfinotti/revops-skills@lead-scoring`).

### `mbfinotti/sales-skills@sales-account-tiering`

- Also here: how many tiers and where the cutoffs sit, tier naming, the capacity cap and coverage model per tier (pods, exec sponsorship, QBR cadence, SLA-encoded differentiation), the score-to-tier bridge, tier-health dials, re-tiering cadence.
- Not here: building the fit score itself (`sales-account-segmentation`), the ICP beneath it (`sales-icp-definition`), the org topology the caps interact with (`sales-org-structure`).

### `mbfinotti/sales-skills@sales-org-structure`

- Also here: pods vs functional split, verticals, hunter/farmer split, SDR:AE ratio, manager span of control, TAM-to-headcount math, the frontline-manager hire, staged transitions between topologies.
- Not here: recruiting humans into the seats (`sales-hiring`), the pay mechanics the topology depends on (`sales-comp-design`), the quota those seats carry (`sales-quota-setting`), the motion the topology serves (`sales-motion`).

### `mbfinotti/sales-skills@sales-quota-setting`

- Also here: top-down target vs bottom-up capacity reconciliation, ramp-adjusted effective capacity, over-assignment, ramp relief schedules, territory-potential weighting, fair-share allocation, attainment-distribution validation and re-baselining triggers.
- Not here: the comp plan paying against the quota (`sales-comp-design`), sizing the pipeline it implies (`sales-pipeline-coverage-modeling`), the account criteria feeding territory potential (`sales-account-segmentation`, `sales-account-tiering`), forecast reliability (`mbfinotti/revops-skills@sales-forecast-diagnostic`).

### `mbfinotti/sales-skills@sales-pipeline-coverage-modeling`

- Also here: raw multiplier, stage-weighted and conversion-inversion methods; segment coverage bands, seasonality indexing, the credibility adjustment, the coverage gap and its four levers with the point of no return.
- Not here: deriving the quota being covered (`sales-quota-setting`), auditing a live pipeline's hygiene or stale deals (`mbfinotti/revops-skills@sales-pipeline-hygiene`), diagnosing why a forecast misses (`mbfinotti/revops-skills@sales-forecast-diagnostic`).

### `mbfinotti/sales-skills@sales-comp-design`

- Also here: base/variable mix by role, accelerators and decelerators, thresholds and caps, draws, spiffs, crediting and split rules, plan documents and governance, mid-cycle change handling.
- Not here: setting the quota the plan pays against (`sales-quota-setting`), the topology whose splits it prices (`sales-org-structure`), OTE positioning in a specific offer (`sales-hiring`).

## Boundary pairs

Where two or more siblings collide on keywords, decide from these declared-scope boundaries. The first block is altitude collisions - the most common misroute in this collection.

- **`sales-motion` vs the outbound and copy skills** - which motion the company runs, and the gates for changing it → `sales-motion`. Executing touches inside a motion already chosen → `sales-outbound-sequence` and the per-channel copy skills.
- **`sales-icp-definition` vs `sales-account-segmentation` vs `sales-account-tiering`** - three planning skills that all sound like "targeting". Who qualifies at all, and the weighted criteria that decide it → ICP. How the qualifying accounts get scored, grouped and ranked → segmentation. Where the cutoffs sit and what service level each group gets → tiering. Each consumes the one before it and never re-derives it.
- **`sales-market-sizing` vs `sales-account-segmentation`** - sizing counts the market; segmentation organizes and ranks what is inside it. "How big is this" → sizing. "Which of these first" → segmentation.
- **`sales-quota-setting` vs `sales-pipeline-coverage-modeling`** - quota-setting produces the number a rep carries; coverage modeling sizes the pipeline that number implies and diagnoses the gap. "What should the quota be" → quota-setting. "Do we have enough pipeline for it" → coverage modeling.
- **`sales-org-structure` vs `sales-comp-design` vs `sales-hiring`** - the seats and reporting lines → org-structure. The money paid inside those seats → comp-design. Finding and ramping a human for one → hiring. A hunter/farmer split spans the first two: the split itself is org-structure, its credited tails and rewritten commission agreements are comp-design.
- **`sales-quota-setting` vs `sales-comp-design`** - the target → quota-setting. What attainment against it pays, and the accelerator curve above it → comp-design. "Reps are sandbagging" is neither: it is `mbfinotti/revops-skills@sales-forecast-diagnostic`.
- **`sales-pipeline-coverage-modeling` vs `mbfinotti/revops-skills@sales-pipeline-hygiene`** - is there enough pipeline, modelled against win rates → coverage modeling. Is the pipeline that exists clean and current → the revops sibling.
- **sales-hiring vs sales-career** - THE most confusable pair; mirror images of the same role knowledge. Decide by who is asking: someone filling a seat (scorecard, interview loop, work sample, ramp plan) → hiring. Someone taking a seat (interview prep, skill-gap roadmap, offer evaluation) → career. On ambiguous phrasing ("SDR interview questions", "30-60-90 plan"), ask "are you hiring for this role, or interviewing for it?" before routing. Both skills self-detect the wrong audience and point across.
- **meddpicc-scorecard vs deal-red-flags** - both answer "is this deal real", over different inputs. A structured pass against the eight named elements with a verdict band → meddpicc-scorecard. An unstructured sweep of free-text notes for named risk patterns, quoting fragments → deal-red-flags.
- **meddpicc-scorecard vs deal-champion-mapping** - meddpicc scores the whole deal (champion is one element of eight); champion-mapping builds the full stakeholder graph with per-person confidence. "Score this deal" → meddpicc. "Who is the real decision maker / are we single-threaded" → champion-mapping.
- **deal-champion-mapping vs deal-red-flags** - single-threading appears in both. Mapping who the people are and what proves each role → champion-mapping. Sweeping the notes for the full red-flag set, of which single-threading is one → deal-red-flags.
- **sales-call-review vs sales-meeting-recap** - same call, opposite jobs. Judging how the rep performed → call-review. Writing what was agreed and what happens next → meeting-recap.
- **cold-call-opener vs sales-discovery-questions** - the first 30 seconds → cold-call-opener; everything asked after the prospect agrees to keep talking → sales-discovery-questions.
- **sales-objection-handling vs negotiation-concession-planner** - an objection already voiced, needing a spoken response → objection-handling. Preparing what may be traded before the negotiation call → concession-planner.
- **sales-objection-handling vs deal-value-calc** - "your price is too high" as a rebuttal need → objection-handling. Building the arithmetic and narrative that justify the price → deal-value-calc.
- **deal-value-calc vs negotiation-concession-planner** - value-calc quantifies what the deal is worth to the buyer; concession-planner prices what we may give and what we require back.
- **cold-email-subject-line-tester vs cold-email-deliverability** - spam words inside the subject line only → subject-line-tester. Authentication, sender reputation, body mechanics, legal compliance, "going to spam" → deliverability.
- **sales-outbound-sequence vs the copy skills** - sequence owns which touch on which day and the stop rules; it never writes copy. Copy splits by channel: subject line → subject-line-tester, phone opener → cold-call-opener, personalization angle → sales-outreach-personalization.
- **sales-outreach-personalization vs cold-email-subject-line-tester** - choosing the angle and proving the signal → personalization. Turning a chosen angle into scored subject-line variants → subject-line-tester.
- **sales-radar vs everything else** - "newsletter", "podcast", "community", "who to follow", "stay current" → radar; any operational task → never.

## Ordered chains

Propose a chain only when the task genuinely decomposes this way; never fabricate a sequence. Each chain is listed in dependency order, not efficiency order - a later link consumes what the earlier one produces, so there is no ratio to rank.

Planning chains:

- `sales-icp-definition` → `sales-market-sizing` → `sales-account-segmentation` → `sales-account-tiering` - decide who qualifies, count how many of them exist, score and group them, then set the cutoffs and the coverage each group gets. Sizing a market before the ICP filters it produces a number nobody can act on.
- `sales-motion` → `sales-org-structure` → `sales-comp-design` - the motion decides which seats exist at all, the topology defines them, and the plan prices the behaviour inside them. Re-comp before re-org whenever both are moving.
- `sales-quota-setting` → `sales-pipeline-coverage-modeling` → `sales-comp-design` - derive the number, size the pipeline it implies, then design what attainment against it pays. A comp plan built on a quota no pipeline can cover pays for a miss.
- `sales-account-segmentation` → `sales-quota-setting` - territory potential comes from the segment model; quotas weighted on unsegmented accounts distribute the target by headcount rather than by opportunity.

Execution chains:

- `sales-outreach-personalization` → `cold-email-subject-line-tester` → `cold-email-deliverability` → `sales-outbound-sequence` - find the angle, turn it into subject lines, verify the sending setup will not bury them, then decide the touch pattern that carries them.
- `cold-call-opener` → `sales-discovery-questions` → `sales-call-review` - script the first 30 seconds, prepare what to ask once they stay on, then grade the recording against both.
- `deal-champion-mapping` → `meddpicc-scorecard` → `deal-red-flags` - establish who the people actually are, score the deal on that evidence, then sweep the notes for what the score assumed.
- `deal-value-calc` → `negotiation-concession-planner` → `sales-objection-handling` - quantify what the deal is worth before deciding what to trade, and rehearse the spoken rebuttals last.
- `sales-discovery-questions` → `sales-meeting-recap` - the questions asked determine what the recap can honestly restate.

## Sibling repository recommendations

Both siblings below are `mbfinotti`-owned, fully built, and installable independently - recommend, never require. Route by task shape, not by keyword collision with the tables above.

### `mbfinotti/revops-skills` - CRM/pipeline-tactical

Recommend when the task is about the CRM record, pipeline mechanics, or funnel-wide reporting rather than one rep's execution or the sales plan above it:

- Lead assignment or prioritization logic → `lead-routing`, `lead-scoring`
- Stage integrity or a stale-deal sweep across many deals → `pipeline-stage-definition-audit`, `sales-pipeline-hygiene`
- Non-standard deal approval chains → `deal-desk-approval`
- Forecast reliability - sandbagging, stage inflation → `sales-forecast-diagnostic`
- Field ownership and source-of-truth rules for shared data → `crm-data-governance`, `revenue-data-governance-strategy`
- Post-sale health, churn signals, sales-to-CS handoff → `customer-health-score`, `customer-churn-signals`, `sales-to-cs-handoff`
- Funnel model design, drop-off tracing, metric trees, board reporting → `revenue-funnel`, `revenue-leakage`, `revenue-kpi-framework`, `revenue-reporting`

The boundary against this repo's planning skills is ownership of the decision, not seniority: the sales plan (motion, ICP, segments, tiers, org, quota, coverage, comp) is sales-skills; the systems, data and reporting that instrument it are revops-skills.

### `mbfinotti/partnerships-skills` - macro channel/partner-strategy plus affiliate/influencer/referral ops

Recommend when the task is about a partner, channel, or program-level relationship rather than a direct-sold deal. Boundary against `sales-motion`: whether to run a channel motion at all is sales-motion; designing the program once that is decided is partnerships-skills.

- Partner ecosystem, channel program, or tier design → `partner-ecosystem`, `partner-channel-program`, `partner-tiering`
- Co-selling rules or channel conflict resolution → `co-selling-strategy`, `partner-channel-conflict`
- Partner enablement, alliance/marketplace prioritization, partner economics or performance → `partner-enablement`, `alliance-prioritization`, `partner-marketplace-strategy`, `partner-economics`, `partner-performance`
- Affiliate program terms, commission structure, recruitment, onboarding, fraud detection, payout audit, performance dashboard → the `affiliate-*` skills
- Influencer/creator sourcing, outreach, negotiation, campaign brief, measurement → the `influencer-*` skills
- Customer refer-a-friend incentive design or abuse guardrails → `referral-incentive-design`, `referral-abuse-guardrails`

Give the specific sibling skill name when the task maps cleanly to one; name the repo alone when it only maps to the general territory.

## Coverage gaps (v1)

No skill in the collection or its two siblings above covers these. Name the gap; never promise or invent a skill:

Execution side:

- Voicemail scripts (cold-call-opener explicitly excludes them)
- Full-call talk tracks beyond the opener and the discovery block (demo delivery, closing sequences)
- Ongoing coaching plans and manager 1:1 frameworks (sales-call-review grades one tape and stops)
- Social selling / LinkedIn personal-brand content for a rep
- Sales methodology selection (MEDDIC vs Challenger vs SPIN vs Sandler) - the collection ships one MEDDPICC scorecard, not a methodology comparison
- Prospect list building and contact-data sourcing
- Proposal, contract, and redline drafting
- Rejection resilience and rep mindset work

Planning side - motion, ICP, sizing, segmentation, tiering, org, quota, coverage and comp are all covered; these are not:

- Territory-carve methodology - how territories are cut by geography, industry or account list (segmentation and tiering rank accounts; neither draws the boundaries)
- Rep capacity and headcount modeling against a revenue target, including attrition and ramp
- Competitive positioning and battlecard content at the strategic level
- Pricing and packaging alignment to motion and segment
- GTM sequencing - which segments, products or regions to attack in which order
- Vertical prioritization and win-rate benchmarking against segment norms
