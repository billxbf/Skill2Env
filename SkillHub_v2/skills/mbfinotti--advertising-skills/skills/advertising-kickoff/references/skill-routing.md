# Routing detail - advertising-skills collection

Route only from the declared scopes below. Every "do not route here" line comes from the skill's own description, not from inference. The collection is 31 skills: the 30 siblings below plus the kickoff itself.

Nothing here is ranked, by design: scope is a match test, not a ratio. Ranking lives in SKILL.md § 4 and § 7, where skills do compete for one session.

## Table of Contents

- [Per-skill signals](#per-skill-signals)
- [Boundary pairs and clusters](#boundary-pairs-and-clusters)
- [Ordered chains](#ordered-chains)
- [Coverage gaps (v1)](#coverage-gaps-v1)

## Per-skill signals

### `mbfinotti/advertising-skills@ad-account-diagnostic`

- Route here: find the root cause of an underperforming paid ad account across tracking, structure, targeting, creative, bidding/budget, offer, external forces; "why are my ads underperforming", "my CPA went up", "ROAS dropped", "should I increase my budget", campaign structure review.
- Do not route here: it executes no changes and stops at the account boundary - page fixes, consolidation, creative, and budget moves hand off to siblings.

### `mbfinotti/advertising-skills@ad-copy-variants`

- Route here: turn one value proposition into genuinely distinct static/text ad copy variants (headline, primary text, description, CTA), labelled by angle, awareness stage, formula, version; search ad headline sets; ML asset-pool surfaces.
- Do not route here: video scripts, creative briefs, test design, landing-page audits.

### `mbfinotti/advertising-skills@ad-format-fit`

- Route here: given objective + platform, flag ad formats that are a poor fit or commonly misused before launch (objective doesn't expose them, wrong funnel stage, team can't produce them); post-launch, separate a format problem from a creative or targeting problem; pre-launch format QA with launch blockers.
- Do not route here: channel choice, creative briefing, copywriting, test design.

### `mbfinotti/advertising-skills@ad-swipe-file`

- Route here: collect competitors' currently-running ads into a categorized, queryable library and convert it into ranked creative test hypotheses; "what ads are my competitors running", competitor ad library teardown, creative inspiration.
- Do not route here: briefs and test design - it stops at ranked hypotheses.

### `mbfinotti/advertising-skills@advertising-career`

- Route here: the candidate side - skill-gap roadmap on the junior→mid→senior→lead ladder, prep for the five interview formats, NDA-safe portfolio, certifications, agency vs in-house vs freelance, promotion and pay conversations.
- Do not route here: the hiring side; it does not find or submit job applications.

### `mbfinotti/advertising-skills@advertising-hiring`

- Route here: the hirer side - rung decision, outcome scorecard, 2-3 round interview loop with question bank, time-boxed work sample, 30-60-90 ramp with staged spend authority.
- Do not route here: sourcing candidates, posting jobs, applicant tracking, writing offers, or the candidate side.

### `mbfinotti/advertising-skills@advertising-radar`

- Route here: a personalised, time-budgeted watch list of paid-advertising sources - podcasts, newsletters, ad-platform release notes, communities, events, people to follow - plus how to keep it fresh.
- Do not route here: any operational advertising task. Route here only when the ask is what to _read/follow/stay current on_, never how to _do_ something.

### `mbfinotti/advertising-skills@ad-attribution-gap`

- Route here: quantify and explain the discrepancy between ad platform reporting, an analytics tool, and the source of truth (CRM or order system); classify each unit of gap as timing, definitional, or unexplained residual; "the numbers don't match", "is this reporting gap normal".
- Do not route here: fixing tracking, or picking an attribution model - it measures the gap and names its causes.

### `mbfinotti/advertising-skills@ad-audience-targeting`

- Route here: turn an ICP and buying signals into a layered targeting plan - cold/broad, interest, in-market, lookalike, first-party, retargeting tiers - sized against platform floors, budgeted to the learning threshold, sequenced, with exclusion rules; broad vs layered; audience overlap between campaigns.
- Do not route here: building seed lists; designing retargeting message sequences.

### `mbfinotti/advertising-skills@ad-bidding-strategy`

- Route here: the bidding policy per platform and goal - manual vs automated, cost-goal vs value/return-goal, when to switch, how to set and move the target, evaluation window, rollback trigger; "target CPA or target ROAS", "delivery collapsed after I changed the target", bid cap vs cost cap, portfolio bid strategy.
- Do not route here: tracking spend pacing, splitting budgets across campaigns, picking channels, repairing conversion tracking.

### `mbfinotti/advertising-skills@ad-budget-pacing`

- Route here: track daily/weekly spend against an already-set budget and flag under- or over-pacing; pacing ratio, projected period spend, required daily spend, false-alarm gate, cause diagnosis; "am I on pace", burn rate.
- Do not route here: setting the budget, kill thresholds, CAC/ROAS benchmarking, scale-up planning. It flags and recommends; it never changes budgets or bids.

### `mbfinotti/advertising-skills@ad-buyer-group-mapper`

- Route here: map the likely buying committee for an offer/deal size/industry and give each role a messaging angle plus the ad-targeting proxy (job function + seniority, account list, account-level intent); B2B committees and multi-decider household purchases; whether per-role targeting beats one broad message.
- Do not route here: building or sizing ad audiences, seed lists, retargeting sequences, ad copy, or mapping named contacts on one live deal.

### `mbfinotti/advertising-skills@cac-roas-benchmark`

- Route here: compute CAC and ROAS family metrics from real data and judge spend health against a three-reference ladder (own break-even, own trailing history, provenance-labeled external benchmarks); returns healthy / watch / unhealthy / insufficient evidence; "is my CAC too high", "what should my ROAS be".
- Do not route here: setting targets as policy, reallocating budget, diagnosing why an account underperforms.

### `mbfinotti/advertising-skills@ad-campaign-consolidation`

- Route here: evaluate a fragmented account and recommend which campaigns/ad sets to merge, which splits to preserve, and how to migrate without resetting learning; "too many ad sets", "stuck in learning", "budget spread too thin", restructure my ad account.
- Do not route here: executing the merge - it plans only.

### `mbfinotti/advertising-skills@conversational-ad-copy`

- Route here: adapt ad messaging for conversational and AI-answer ad surfaces - the one-shot ad occupying a single response slot inside an assistant reply or answer-engine result; verbatim vs model-rewritten placements, recommendation register, grounding and disclosure, quotability gate.
- Do not route here: feed/search copy variants, video scripts, test design.

### `mbfinotti/advertising-skills@ad-conversion-tracking`

- Route here: pre-launch checklist verifying conversion events are configured, firing once, and deduplicated, ending in a GO / NO-GO; tag debug, browser/server dedup, value and currency, consent handling, test-data exclusion; "is my tracking working".
- Do not route here: writing or installing tracking code; post-launch cross-platform reconciliation hands off to `mbfinotti/advertising-skills@ad-attribution-gap`.

### `mbfinotti/advertising-skills@ad-creative-brief`

- Route here: turn a campaign goal plus an audience insight into a structured brief a designer, video editor, or UGC creator executes - messaging angle, hook directions, art direction, specs, testing intent, handoff/revision loop; variants for static, short-form video/UGC, and responsive text ads.
- Do not route here: the finished asset; the ad copy itself (`mbfinotti/advertising-skills@ad-copy-variants`) or shot-by-shot creator scripts (`mbfinotti/advertising-skills@ugc-ad-scripts`).

### `mbfinotti/advertising-skills@ad-creative-fatigue`

- Route here: decide whether a running creative is genuinely wearing out or a confounder explains the decline (budget change, learning reset, audience saturation, CPM inflation, seasonality, tracking breakage); returns a verdict with confidence and the cheapest remedy; "frequency is climbing", "should I kill this ad".
- Do not route here: producing replacement creative.

### `mbfinotti/advertising-skills@ad-creative-test-plan`

- Route here: design a **pre-launch** creative test - decision, falsifiable hypothesis, isolation level, test cells and per-cell budgets, required sample/spend/duration, pre-registered kill/scale rules, and a per-cell read standard (Powered / Directional / Not testable as designed).
- Do not route here: reading results after the fact - that belongs to `mbfinotti/advertising-skills@ad-creative-fatigue`.

### `mbfinotti/advertising-skills@ad-hook-analyzer`

- Route here: score and force-rank the **openings** of candidate video ads before launch, from script, transcript, storyboard, shot list, or a described cut; four hard gates, seven banded dimensions, ranked shortlist within the batch; "which hook should I test", first 3 seconds, thumbstop.
- Do not route here: writing scripts; it returns a ranking, never an absolute performance prediction.

### `mbfinotti/advertising-skills@paid-landing-page-audit`

- Route here: audit a landing page receiving paid traffic - message match, above-the-fold clarity, form friction, trust, speed, mobile, policy risk - and return a prioritised fix list with evidence classes; "my ads get clicks but no conversions", post-click experience.
- Do not route here: implementing anything; it stops at the click.

### `mbfinotti/advertising-skills@lookalike-audience-seeds`

- Route here: select and size the seed customer list behind a lookalike/similar/value-based audience - which customers, how many, whether the **matched** count clears the platform floor; RFM and value-based selection, negative-selection pass, privacy/consent gate, fallback ladder; "my lookalike isn't working", match rate.
- Do not route here: platform upload and tier layering - it ends at the seed spec.

### `mbfinotti/advertising-skills@paid-media-scaling`

- Route here: decide when a proven campaign has earned a budget **increase**, the step size, the ramp over weeks/months, and how to avoid collapse; readiness gates, hold periods, vertical vs horizontal scaling, rollback triggers; "we doubled the budget and ROAS collapsed", "we hit a scaling ceiling".
- Do not route here: splitting a fixed total, daily pacing, setting max-CAC/min-ROAS policy, choosing bid strategies, per-ad creative kill/scale calls.

### `mbfinotti/advertising-skills@ad-negative-keywords`

- Route here: build and maintain negative keyword lists from search term reports - n-gram query mining, match types, exclusion level (account, shared list, campaign, ad group), review cadence, overblocking guard; needs a search term report export or query data.
- Do not route here: positive keyword research or bid strategy.

### `mbfinotti/advertising-skills@ad-platform-selection`

- Route here: decide which paid channel **families** fit a business's economics, audience, funnel stage, and budget at campaign setup - affordability gate (allowable CAC, payback), disqualifier pass, fit scoring, funding-floor check, channel test design; "where should I spend a new ad budget".
- Do not route here: splitting ongoing budgets, setting bids, pacing spend, designing creative tests.

### `mbfinotti/advertising-skills@ad-spend-guardrails`

- Route here: set the org's top-level spend guardrails as written **policy** - max allowable CAC, min ROAS/MER floor, kill-switch thresholds, counter-metrics, who owns them and who may override, re-baselining cadence, derived from contribution margin, payback, cash runway.
- Do not route here: monitoring daily pacing, benchmarking current CAC/ROAS, splitting budget across channels, choosing bid strategies, planning a scale-up.

### `mbfinotti/advertising-skills@retargeting-funnel`

- Route here: design a multi-stage retargeting sequence from the site's own funnel data - recency windows, behavioural-depth tiers, per-stage message and offer ladder, mutually exclusive audiences and exclusions, per-stage frequency caps; "we keep showing ads to people who already bought".
- Do not route here: building the campaigns inside an ad platform - it produces a stage-by-stage plan.

### `mbfinotti/advertising-skills@ad-spend-allocation`

- Route here: split a **fixed total** budget across campaigns, platforms, funnel stages, and audiences by expected marginal return - the monthly/quarterly allocation decision; gates before splitting, marginal-return proxies, step sizing, allocation-plan artifact.
- Do not route here: tracking daily spend against an already-set budget, choosing bid strategies, setting max-CAC/min-ROAS policy, picking channels at setup, raising the total budget.

### `mbfinotti/advertising-skills@thought-leadership-ads`

- Route here: plan a campaign promoting an executive's or founder's **existing organic posts** as paid person-fronted ads - post selection, sequencing, audience and exclusions, permission and governance, budget, measurement; B2B trust-layer and B2C founder-led.
- Do not route here: drafting the featured person's content.

### `mbfinotti/advertising-skills@ugc-ad-scripts`

- Route here: turn a product brief and audience into UGC-style short-form video ad **scripts** a creator can film - hook, body, CTA, 3-5 hook variants per concept as spoken line + on-screen text + opening visual, delivery notes, disclosure lines; B2C creator scripts and B2B founder-led / EGC / testimonial formats.
- Do not route here: scoring existing hooks, static ad copy variants, full creative briefs, fatigue calls, test design.

### `mbfinotti/advertising-skills@advertising-kickoff`

- Route here: project start, periodic check-in, "which advertising skill do I need", re-routing mid-project. This skill routes; it never performs a sibling's job itself.

## Boundary pairs and clusters

Where siblings collide on keywords, decide from these declared-scope boundaries. The first three are mandatory disambiguations - run them before routing any task that touches their keywords.

**Hirer vs candidate (mirror images).** `mbfinotti/advertising-skills@advertising-hiring` and `mbfinotti/advertising-skills@advertising-career` cover the same role knowledge from opposite sides of the table. Ask who is asking before routing: someone recruiting → hiring; someone being recruited → career. If the wrong one was picked, say so and hand over.

**Budget cluster - six skills, six different objects.** Decide by which decision is actually on the table:

- `mbfinotti/advertising-skills@ad-budget-pacing` - the budget already exists; is today's spend on pace against it? (daily/weekly tracking, alerts)
- `mbfinotti/advertising-skills@ad-spend-allocation` - the total is fixed; how do we split it across campaigns/platforms/stages? (marginal return)
- `mbfinotti/advertising-skills@paid-media-scaling` - a campaign proved out; do we raise the **total** spend, by how much, how fast?
- `mbfinotti/advertising-skills@ad-spend-guardrails` - what CAC ceiling / ROAS floor / kill-switch is the **policy** everything else must respect, and who may override it?
- `mbfinotti/advertising-skills@cac-roas-benchmark` - is current spend healthy? (measure and verdict, against break-even, own history, external benchmarks)
- `mbfinotti/advertising-skills@ad-bidding-strategy` - which bid **policy** per platform/goal, and what target?

Quick tests:

- "am I on pace" → `mbfinotti/advertising-skills@ad-budget-pacing`
- "which campaign gets more of the same money" → `mbfinotti/advertising-skills@ad-spend-allocation`
- "can we spend more overall" → `mbfinotti/advertising-skills@paid-media-scaling`
- "what are we allowed to spend per customer" → `mbfinotti/advertising-skills@ad-spend-guardrails`
- "is this CAC good" → `mbfinotti/advertising-skills@cac-roas-benchmark`
- "manual or tCPA" → `mbfinotti/advertising-skills@ad-bidding-strategy`

**Creative cluster - six skills, sequential stages of one creative lifecycle:**

- `mbfinotti/advertising-skills@ad-creative-brief` - goal + insight → a brief a designer/editor/creator executes (direction, not the asset)
- `mbfinotti/advertising-skills@ugc-ad-scripts` - the spoken shot-level script for short-form video
- `mbfinotti/advertising-skills@ad-copy-variants` - static/text copy variants for A/B testing
- `mbfinotti/advertising-skills@ad-hook-analyzer` - scores and ranks **openings** of candidate videos before launch
- `mbfinotti/advertising-skills@ad-creative-test-plan` - designs the **pre-launch** test that will run them
- `mbfinotti/advertising-skills@ad-creative-fatigue` - reads a **running** creative's decline and gives a verdict

Quick tests:

- "brief my designer" → `mbfinotti/advertising-skills@ad-creative-brief`
- "write the video script" → `mbfinotti/advertising-skills@ugc-ad-scripts`
- "write the headlines" → `mbfinotti/advertising-skills@ad-copy-variants`
- "which of these openings should I test" → `mbfinotti/advertising-skills@ad-hook-analyzer`
- "how much budget/how long for this test" → `mbfinotti/advertising-skills@ad-creative-test-plan`
- "is this ad worn out" → `mbfinotti/advertising-skills@ad-creative-fatigue`

**Audience cluster.**

- `mbfinotti/advertising-skills@ad-audience-targeting` plans the layered tiers (and explicitly excludes seed building and retargeting messaging)
- `mbfinotti/advertising-skills@lookalike-audience-seeds` picks and sizes the seed list feeding one of those tiers
- `mbfinotti/advertising-skills@retargeting-funnel` designs the staged retargeting messages and windows
- `mbfinotti/advertising-skills@ad-buyer-group-mapper` decides which **roles** to reach and with what angle, before any audience is sized

**Tracking vs attribution.** `mbfinotti/advertising-skills@ad-conversion-tracking` is pre-launch verification of one account's events (GO/NO-GO), and its own scope hands post-launch reconciliation across platform, analytics, and source of truth to `mbfinotti/advertising-skills@ad-attribution-gap`.

**Diagnostic vs its handoffs.** `mbfinotti/advertising-skills@ad-account-diagnostic` localises the failing layer and stops at the account boundary. Once it names the layer, route on:

- fragmentation → `mbfinotti/advertising-skills@ad-campaign-consolidation`
- post-click → `mbfinotti/advertising-skills@paid-landing-page-audit`
- creative decay → `mbfinotti/advertising-skills@ad-creative-fatigue`
- wasted queries → `mbfinotti/advertising-skills@ad-negative-keywords`
- tracking → `mbfinotti/advertising-skills@ad-conversion-tracking`
- bid policy → `mbfinotti/advertising-skills@ad-bidding-strategy`

**Channel vs format.** `mbfinotti/advertising-skills@ad-platform-selection` chooses the channel family before any campaign exists; `mbfinotti/advertising-skills@ad-format-fit` chooses the format **within** a chosen platform for a stated objective.

**Feed copy vs conversational copy.** Both write copy. Feed, search, and social placements → `mbfinotti/advertising-skills@ad-copy-variants`. A single response slot inside an AI assistant reply or answer-engine result → `mbfinotti/advertising-skills@conversational-ad-copy`.

**Swipe file vs brief.** `mbfinotti/advertising-skills@ad-swipe-file` ends at ranked competitor-derived hypotheses; `mbfinotti/advertising-skills@ad-creative-brief` turns a chosen hypothesis into executable direction.

**Radar vs everything else.** Anything containing "newsletter", "podcast", "community", "who to follow", "release notes", or "stay current" → `mbfinotti/advertising-skills@advertising-radar`; every operational ask routes elsewhere.

## Ordered chains

Propose a chain only when the task genuinely decomposes this way; never fabricate a sequence. Each chain is listed in dependency order, not efficiency order - a later link consumes what the earlier one produces, so there is no ratio to rank.

- `mbfinotti/advertising-skills@ad-platform-selection` → `mbfinotti/advertising-skills@ad-format-fit` → `mbfinotti/advertising-skills@ad-conversion-tracking` → `mbfinotti/advertising-skills@ad-creative-test-plan` - launching a new channel: pick it, pick producible formats, prove tracking, then design the first test.
- `mbfinotti/advertising-skills@ad-spend-guardrails` → `mbfinotti/advertising-skills@cac-roas-benchmark` → `mbfinotti/advertising-skills@ad-spend-allocation` → `mbfinotti/advertising-skills@paid-media-scaling` → `mbfinotti/advertising-skills@ad-budget-pacing` - the budget stack: set policy, measure health against it, split the total, decide whether to raise it, then track daily.
- `mbfinotti/advertising-skills@ad-swipe-file` → `mbfinotti/advertising-skills@ad-creative-brief` → `mbfinotti/advertising-skills@ugc-ad-scripts` / `mbfinotti/advertising-skills@ad-copy-variants` → `mbfinotti/advertising-skills@ad-hook-analyzer` → `mbfinotti/advertising-skills@ad-creative-test-plan` - competitor hypotheses become direction, then assets, then a ranked shortlist, then a powered test.
- `mbfinotti/advertising-skills@ad-account-diagnostic` → the named layer's skill - never run the layer skills in parallel before the diagnostic localises the failure.
- `mbfinotti/advertising-skills@ad-buyer-group-mapper` → `mbfinotti/advertising-skills@ad-audience-targeting` → `mbfinotti/advertising-skills@lookalike-audience-seeds` - decide which roles matter, structure the tiers, then build the seed behind the lookalike tier.
- `mbfinotti/advertising-skills@ad-conversion-tracking` → `mbfinotti/advertising-skills@ad-attribution-gap` - verify events before launch; reconcile reported numbers after.
- `mbfinotti/advertising-skills@ad-creative-fatigue` → `mbfinotti/advertising-skills@ad-creative-brief` → `mbfinotti/advertising-skills@ugc-ad-scripts` / `mbfinotti/advertising-skills@ad-copy-variants` - a wear-out verdict is what justifies new creative.

## Coverage gaps (v1)

No skill in the collection covers these. Name the gap; never promise or invent a skill:

- Positive keyword research and keyword expansion (`mbfinotti/advertising-skills@ad-negative-keywords` builds exclusions only).
- In-platform execution of any kind - every skill in this collection plans, audits, or decides; none builds or changes campaigns.
- Creative production itself: design, filming, editing, casting, creator sourcing.
- Incrementality testing (holdout, geo-lift) and media mix modeling.
- Cross-channel budgeting beyond paid ads (email, organic, content, events).
- Post-signup activation and onboarding drop-off.
- Ad policy appeals, disapprovals, and account suspension recovery.
- Product feed / catalog management for shopping and retail media.
