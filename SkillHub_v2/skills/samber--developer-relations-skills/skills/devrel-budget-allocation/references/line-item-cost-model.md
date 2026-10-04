# Line item cost model

What each pillar's line really costs, in cash and in hours. Use this while pricing candidate lines in step 2. The hours column is the one that decides whether a line is fundable; the cash column is the one that gets approved.

## Contents

- The two-number rule
- Events
- Content
- Community
- Documentation, tooling and enablement
- Education and certification
- OSS sponsorship and funding
- Paid distribution
- Documented setup costs and latencies
- Fully loaded hour rate

## The two-number rule

Every line carries a cash figure and an hours figure. Derive hours from named people, never from a team average - "engineering will review it" is not a funded reviewer.

Count hours across the whole life of the line: preparation, delivery, and the follow-up load that arrives afterwards. Follow-up is the systematically missing column. A conference produces a week of replies, a popular post produces a support queue, a community launch produces a permanent moderation shift.

## Events

Cash: sponsorship fee, paid add-ons, booth build and shipping, swag, printing, prizes and credits, travel, accommodation, per diem for every attendee, event-specific landing page or promo infrastructure.

Hours: pitch and package negotiation, booth design, pre-event promotion, travel days, on-site days for every staffer, 48-hour follow-up, and the post-event review. Staff time at loaded cost is the line most teams omit and the one that most often doubles the true total.

Opportunity cost: what those engineer-days would otherwise have shipped. Record it as a note even if it never enters the table.

## Content

Cash: agency or freelance fees, editing, illustration and diagrams, video production and editing, stock and licensing, hosting and CDN, syndication or placement fees.

Hours per piece - count in passes, not in drafts: research, drafting, writing code that actually runs, technical review by someone who can dispute the claims, edits, assets, publishing, then promotion and replies. Estimate per format; a changelog entry, a checkpointed tutorial and a benchmark post differ by an order of magnitude.

The scarce resource is the reviewer, not the writer. A plan that assumes unlimited review capacity stalls in the review column, where nothing has visibly slipped yet.

## Community

Cash: platform licence or tier, moderation and analytics tooling, swag and recognition, community-event or meetup costs, contractor moderation cover.

Hours: daily presence and answering, moderation and incident handling, program management for champions or ambassadors, onboarding new members, reporting. Community is the pillar with the highest ratio of recurring hours to cash - a platform that costs little per month can consume a half-time person indefinitely.

Exit cost is unusually high: a community that is wound down or migrated damages trust in a way a cancelled sponsorship does not.

## Documentation, tooling and enablement

Cash: docs platform or hosting, search, versioning and preview infrastructure, sandbox or playground compute, SDK release automation, code-sample CI minutes, technical writing contractors.

Hours: writing, engineering review, sample maintenance across languages, keeping every sample running in CI, and the per-release update tax. This pillar's cost is dominated by maintenance, not creation, and the maintenance is unavoidable - stale docs and broken samples actively cost trust rather than fading quietly.

## Education and certification

Cash: authoring tools, lab or sandbox platform, video production, exam platform, proctoring, item development, translation.

Hours: curriculum design, content authoring, subject-matter review, item writing and review, per-release realignment when the product changes, learner support. Certification adds permanent obligations: item security, cheating response and recertification cycles, all of which recur every year the credential exists.

## OSS sponsorship and funding

Cash: monthly or annual sponsorships, one-off grants, foundation memberships, bounties. Note that some platforms enforce an invoice minimum for procurement-routed payments, which sets a floor on any line that must go through purchase orders.

Hours: dependency-graph selection, maintainer contact and diligence, invoicing and vendor onboarding, renewal reviews, and internal reporting on what the money bought.

Two motions cost very differently: breadth (small amounts across many dependencies, largely automatable) and depth (larger judgement-based amounts to a few load-bearing projects, entirely manual).

- effort, heaviest first: `depth > breadth` - depth is days of diligence and a standing relationship; breadth is a setup pass and near-zero after it.
- value: `depth > breadth` - depth buys a named maintainer who answers; breadth buys coverage and goodwill.
- efficiency: `breadth > depth` - so a program ranked on ratio alone never funds depth. Promote depth when a single project carries the product's critical path, or when the driver is supply-chain exposure rather than goodwill.

## Paid distribution

Cash: sponsored newsletters, podcast reads, developer-network placements, search or social ads, retargeting.

Hours: creative production, list vetting, tracking setup, reading results. The distinguishing property is decay: paid distribution stops working the day it stops being paid, so it belongs in the campaign horizon, never in the compounding one.

## Documented setup costs and latencies

From a published account of scaling developer content production with an agency (Matt Jarvis, Snyk, developerrelations.com case study):

- ~6 months of the DevRel director's own time to build the pipeline before it produced at volume.
- 8-9 weeks from conception to publication once a third party wrote the piece.
- Modelled per-piece impact used in that program: ~1,000 sessions for deeper technical pieces, ~500 for introductory ones.

Read: outsourcing raises throughput but adds a fixed setup cost and a two-month latency. Fund it where the goal is volume and compounding, never where the goal is a dated launch beat.

## Fully loaded hour rate

If the organisation publishes a loaded cost per hour, use it. If not:

1. Take salary plus employer costs and overhead.
2. Divide by realistic working hours.
3. State the assumption in the document.

The number matters less than applying the same one to every line - the purpose is comparability between options, not accounting accuracy.

Last resort, when no salary figure is available either: the multiplier circulating in startup headcount planning is **1.3-1.4× base salary** fully loaded, built from payroll taxes plus a per-head allowance for benefits and for workspace, equipment and software. It is a rule of thumb and it is US-shaped; employer social charges in much of Europe push the real multiplier higher. Use it only with the sentence "this multiplier is a rule of thumb, not a benchmark" attached, and replace it with the finance team's own figure the moment one exists.

Where a program's budget excludes salaries - the majority case - keep the hours column anyway and total it separately. The salary budget belongs to a different owner, but the capacity constraint is the same either way.
