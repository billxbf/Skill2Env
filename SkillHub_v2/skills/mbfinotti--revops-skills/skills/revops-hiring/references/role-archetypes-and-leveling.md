# Role Archetypes and Leveling

No survey-backed RevOps competency matrix or leveling standard exists - the field lacks one, and that absence is a finding, not an omission. Everything below is practitioner opinion from named sources; attribute it when you reuse it.

## The five tracks

RevOps Co-op's "The 5 RevOps Career Tracks" (revopscoop.com) is the de facto archetype taxonomy:

- **Analyst** - assesses large datasets, connects data to business problems, gathers stakeholder requirements. "Your goal isn't just to understand the data, but how the data relates to the problems you're trying to solve."
- **Systems Manager / Administrator** - configures system changes against business priorities, translates requirements into system outputs, owns data quality and implementations. "Systems are a means to acquiring business data that can support good decision-making."
- **Enablement** - trains teams on systems and process, surfaces what top reps do, feeds requirements back to ops.
- **Deal Desk** - analyzes contract data, recommends pricing, balances sales need against compliance. Sits at the intersection of sales, legal, finance, and RevOps; owns quote-to-cash and pricing governance. Close to a B2B-only archetype.
- **Project Manager** - runs initiatives and prioritization; the source frames it as the natural feeder into ops manager and director roles.

For hiring, compress these into three profiles:

- **Systems**: builds and maintains the stack.
- **Analyst**: turns data into answers.
- **Strategist / business partner**: designs process and owns cross-team agreements.

Most failed RevOps hires are a mismatch on this axis rather than a competence failure.

## The profile-choice test

First a scope check, not a ranking - three jobs that are not this hire:

- **Single-function pain**: confined inside one function is Sales Ops, Marketing Ops, or CS Ops, not RevOps - "Hire RevOps when revenue problems cross team boundaries."
- **Marketing ops**: owns the marketing automation platform and lead routing and usually reports to marketing; the handoff to RevOps "lives in the field mapping and the data sync between the two systems".
- **BizOps**: a different job entirely - board decks, market sizing, M&A diligence, often with no CRM access.

Then choose how to close the gap. This is the first and most consequential decision in the engagement - whether to open a requisition at all - so make it here, ranked, before any scorecard exists. Ranked by value returned per hour the hiring manager and panel spend, best ratio first:

- efficiency: fractional operator > scoped agency project > in-house specialist > in-house strategist
- your effort to get someone working: in-house strategist > in-house specialist > scoped agency project > fractional operator
- calendar to first useful output: in-house strategist > in-house specialist > scoped agency project == fractional operator
- reversibility cost, hardest to unwind first: in-house strategist > in-house specialist > scoped agency project > fractional operator
- value at 12 months: in-house strategist > in-house specialist > scoped agency project == fractional operator

Ties:

- Agency and fractional tie on calendar because neither needs a requisition, an approval, or a notice period - both start inside a week.
- They tie again at 12 months because neither leaves compounding capability behind; the artifacts stay, the judgment walks out with the contract.

| Option                                                 | Buys you                                                                                                                    | Your effort                                                                 | Reversibility                                                               |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Fractional operator                                    | Senior judgment on the diagnosis itself, part-time - the answer when the pain is capacity or you sit below the ARR floor    | An hour of calls to start, then a standing hour a week to direct            | Near-zero - a notice period, no backfill                                    |
| Scoped agency project                                  | One bounded fix shipped - an implementation, a migration, a cleanup - with no headcount                                     | A week to scope and select, then a standing review slot while it runs       | A quarter - the contract term, plus whatever they built is now yours to run |
| In-house specialist (systems or analyst, per the pain) | Standing capacity inside the archetype the pain points at; the ticket queue and the reporting stop being someone's side job | A quarter of manager and panel hours to hire, then a standing job to manage | A quarter or more to unwind, and it is a person                             |
| In-house strategist / business partner                 | Cross-team process ownership and agreements nobody else has standing to enforce                                             | A quarter of hours to hire, a quarter to ramp, then a standing job          | Worst on the page - hardest to unwind, most visible when it fails           |

Route the two in-house rows by pain:

- Reporting-trust pain wants the analyst.
- An admin and configuration backlog wants the systems specialist.
- Cross-boundary alignment and process design wants the strategist.

Price the in-house rows against the bands and the fully-loaded multiplier in Compensation input below, and their calendar against Timelines below - but decide the ranking on hours and reversibility, never on the salary figure. Money answers "can we fund this"; the ranking answers "should we do this at all".

- **Default**: the in-house specialist matching the diagnosed archetype, once the company is past the fractional floor (roughly $3M ARR) and the sales team is past about five reps.
- **Move up** to the strategist when the pain genuinely crosses team boundaries _and_ a VP-or-C-level sponsor is committed in writing - without the sponsor that row fails exactly as the negative worked example does.
- **Move down** to fractional or agency when the pain is capacity, when the fix is one bounded project, or when you sit below the floor.

**What this order starves**: the in-house strategist - highest value at 12 months, worst ratio in the first two quarters. Twelve to sixteen weeks to fill plus one to three months to ramp puts the first structural change a quarter and a half out, with revenue-level outcomes at 12+ months. Promote it anyway when cross-team agreements are the actual product you need: a contractor or an agency can map a process, but neither can hold another team to it once the engagement ends.

**Delete, do not demote** - then name the rows you removed and why:

- A hiring freeze or unapproved headcount deletes both in-house rows outright. Rank the remaining two; a requisition parked at the bottom of a list reappears as scope three weeks later.
- Below roughly $3M ARR the same rule deletes them - the sourced guidance is to stay fractional, not to hire junior.
- An agency already retained deletes the agency row into "you already have this", and the rest re-rank around what it does not cover.

**Re-rank against what you already know about this company:**

- An in-house recruiter or a warm bench roughly halves the in-house rows' effort and promotes them.
- A fifth ops hire onto an existing team ramps far faster than a first hire with no documentation and no predecessor, promoting them again.
- A manager with no free hours this quarter demotes them whatever the stage.

The ordering is a default, not a law - it shifts with context and with who executes it.

## Level ladder

The most concrete public leveling frame is Kory White's four-rung ladder (pulserevops.com, 2026 - a single detailed practitioner source, not a standard):

| Level    | A normal Tuesday                                                                                   | Must-haves                                                                                   | Resume anti-signal                                                                |
| -------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Analyst  | Dashboards, ad-hoc analysis, data hygiene, ticket queue, pipeline reports                          | Intermediate SQL, CRM admin cert, spreadsheets, one BI tool                                  | "Strategic thinker driving transformation" at analyst level                       |
| Manager  | Owns forecast cadence, territory and quota planning, one workflow end to end; manages 1-2 analysts | Advanced SQL, deeper platform cert, a transformation layer, forecast math, change management | "Owned full RevOps function" at a 50-person Series A                              |
| Director | Stack roadmap, vendor contracts, data architecture; leads 3-8 people                               | Architecture thinking, vendor management, comp-plan design, hiring                           | "Built our entire data warehouse from scratch" - should be deciding, not building |
| VP       | Co-owns the number with the CRO, board narrative, org design                                       | Revenue-model architecture, board communication, P&L literacy                                | "Hands-on with the CRM daily" - signals weak delegation                           |

Generic HR bands (entry 0-2 years / mid 2-5 / senior 5-8 / staff-lead 8-12 / principal-director 12+) are a starting frame only; reconcile them with the archetype actually being hired.

No efficiency ranking across these rungs, deliberately: the level is set by the scope of the problem you diagnosed, not chosen for its ratio, and ordering rungs against each other would be false precision dressed as a recommendation. The one ordering that is real between them is calendar - see Timelines.

## First hire vs Nth hire

Practitioner consensus places the first dedicated ops hire between Series A and Series C:

- Most commonly Series A at 25-50 employees, once the sales team passes about five reps.
- One source gives $2M-$8M ARR with $4-5M as the sweet spot, and recommends staying fractional below roughly $3M ARR - the source behind the fractional floor the profile-choice test deletes the in-house rows below.
- Above the floor, the dominant profile advice for a first hire - which is how the ranking's in-house specialist row reads at Series A - a "strategic generalist who understands the GTM motion and is willing to perform tactical CRM tasks", 4+ years, at least one end-to-end CRM implementation owned.
- Series B splits the generalist into specialists; at ten-plus people the role becomes leader-of-leaders.

Reporting line:

- A CRO line works at Series A and early B.
- Territorial fights at scale favor a COO or CEO line from Series C onward.

On the generalist question, GTMnow's practitioners: "[Invest in] being a generalist... with a few areas of specialty" (Jen Igartua); the underrated skill is "process-driven advice... define and map GTM processes and workflows" (Asia Corbett).

## Compensation input

Rank sources before quoting - `source trust: survey-backed > recruiter placement data > job-scrape and algorithmic estimates`.

- The sources disagree materially - show the conflict, never average it away.
- Quote every figure with source and date; never invent a band for a geography a source does not cover (UK/EU public data is too thin to anchor on).
- This is scoping input only - offer terms need HR/legal review.

| Source (date)                                                             | Method                       | Key figures (US)                                                                                                  |
| ------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| RevOps Co-op / BoostUp 2025 Compensation & Impact Report (Nov 2024)       | Survey, 1,200+ professionals | Median across all levels $129,155; roughly $100K OTE at 0-50 employees vs $162K at 1,000+                         |
| RevOps Co-op 2026 Salary Report                                           | Survey plus panel commentary | Entry $85K-$125K; director and leaders $187K-$300K+ total                                                         |
| Betts Recruiting (2024)                                                   | Recruiter placements         | Manager base $100K-$160K under 3 years; $150K-$235K at 3+ years                                                   |
| GTMnow (updated Jul 2026; underlying dataset not independently confirmed) | Reported averages            | Specialist $77.7K ($62-99K); Analyst $90.2K ($73-113K); Manager $128.2K ($102-163K); Director $216.4K ($171-279K) |
| Glassdoor (2025)                                                          | Crowd-sourced scrape         | Overall median ~$114K; Manager ~$128K; Director ~$187K                                                            |

Structure:

- RevOps variable is a target bonus tied to company performance, not commission - roughly 5-10% of total for ICs, 15-25% at manager and above.
- SF/NY/Boston carry a 15-30% premium; the remote discount has narrowed to roughly 5-10%.
- Fully-loaded cost rule of thumb: base × 1.30-1.40 plus equity.

Funding the req, from RevOps Co-op:

- "Your company is going to try to provide you with the absolute minimum money required to hire a human."
- "An aspirational hire is a risk to you as a hiring manager on multiple levels" - underfunding produces either a struggling junior or an aspirational title the company cannot support.

## Timelines

Time to fill and time to productivity run inverse (startup-planning source, generic not RevOps-specific):

| Level     | Time to fill | Time to productivity |
| --------- | ------------ | -------------------- |
| Junior    | 6-8 weeks    | 4-6 months           |
| Mid       | 8-12 weeks   | 2-4 months           |
| Senior    | 12-16 weeks  | 1-3 months           |
| Executive | 16-24 weeks  | 3-6 months           |

- time to fill, longest first: executive > senior > mid > junior
- time to productivity, longest first: junior > executive > mid > senior
- total calendar to first useful output, longest first: executive > junior > senior == mid

The two axes disagree, and that is the whole point: senior hires take longest to find and ramp fastest, so the junior req that looks quick to fill is not the quick option once ramp is counted. Mid and senior tie on total calendar - roughly two quarters each - because senior's extra month of search buys back a month of ramp. Budget the req timeline and the ramp plan against the total, never against time-to-fill alone.
