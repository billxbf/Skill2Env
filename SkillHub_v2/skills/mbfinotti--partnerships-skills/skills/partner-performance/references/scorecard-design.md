# Partner Scorecard Design

## The four scorecard models

Partner measurement has four established approaches. PRM vendors rebrand often (Allbound became Channelscaler, Zift became Unifyr) and the concepts outlive the product names. Verify any vendor implementation before citing it to a user.

- Five-category engagement taxonomy, described by Unifyr/Zift, Kris Blackmon.
- Maturity-staged KPI taxonomy, described by PartnerStack.
- Continuous leveling model, described by Channelscaler.
- Four-step partner attribution journey, described by Forrester, Kathy Contreras.

## Dimension menu with metric definitions

Pick 4-6 dimensions; more get ignored. Fill those slots in efficiency order - decisions the dimension settles per hour of data plumbing - and stop when the slots run out. Each metric below is category-generic; map it to whatever CRM/PRM/LMS the program runs.

- efficiency: sourced revenue > pipeline > engagement > capability > customer outcomes > influenced revenue
- value: sourced revenue > customer outcomes > pipeline > capability > engagement
- effort: customer outcomes > influenced revenue > capability > engagement > pipeline == sourced revenue

Sourced revenue and pipeline tie on effort because both read from the same deal-registration records the program already keeps - approved registrations for one, their stage history for the other - so neither adds a data source. They do not tie on value, and sourced revenue leads.

Customer outcomes is what this order starves: second on value, first on effort, fifth on the ratio. It waits for a second pass that most programs never run, and it is the only dimension that catches a partner selling well to customers who then churn. Promote it when partner-sourced retention lags direct, or when tier benefits are being tied to customer success rather than volume.

Influenced revenue sits last on efficiency and jumps to first the moment non-transacting partners are in scope - without it they have nothing to score.

The order is a default, not a law. Re-rank it against the program: an LMS already joined to partner records makes capability near-free.

Delete rather than defer what the program rules out, and say in the spec that the dimension was deleted:

- A PRM with no portal logging removes engagement.
- A program with one transacting partner type removes influenced revenue.

A dimension left in the menu unbuilt gets read later as a metric that exists.

**Revenue (lagging)** - sourced is near-zero effort where deal registration is enforced; influenced costs a quarter of attribution work plus finance sign-off

- **Partner-sourced revenue**: closed revenue from deals the partner originated, evidenced by an approved deal registration. Never blend with influenced.
- **Partner-influenced revenue**: revenue the partner touched but did not originate. Cap influence credit so attributed revenue never exceeds actual revenue; track it as its own KPI. Forrester's attribution work (Kathy Contreras, 2025-09-09, analyst blog) argues sourced-only measurement undercounts non-transacting partners - treat the attribution model as an upstream input to this dimension.

**Pipeline (leading)** - near-zero effort wherever deal registrations are already logged in the PRM

- **Deal-registration approval rate**: approved registrations ÷ submitted. A falling rate signals declining deal quality or rules confusion.
- **Pipeline velocity**: time-in-stage of registered deals vs the program median. Slowing velocity precedes a revenue miss by one or two quarters.
- **Time-to-first-deal**: signup to first registered (or closed - pick one and state it) deal. The per-partner activation signal in PartnerStack's taxonomy (vendor taxonomy).

**Engagement (leading)** - an hour where portal logs and the MDF ledger export cleanly, a week where they do not

- **Portal/program engagement**: logins, content usage, campaign participation - from program systems only.
- **MDF utilization**: claimed vs allocated funds, tied to documented campaigns. Unclaimed MDF is a disengagement signal, not savings.

**Capability (leading)** - about a week, and most of it is joining LMS credentials to partner records

- **Certified headcount**: individuals holding a _current_ certification - count credentials, not course enrollments.

**Customer outcomes (lagging)** - a quarter, because renewal and CSAT records have to be joined back to the sourcing partner and defended to finance

- **Partner-driven retention/CSAT**: renewal rate or CSAT of customers the partner sourced or services - separates partners who sell well from partners whose customers stay.

## Weighting guidance

- Sum weights to 100%; state each as a number, not "high/medium".
- Keep revenue-class dimensions at or below ~50% so leading indicators can actually move the score - a revenue-only score is a rearview mirror.
- Weights are self-set, never copied from a published standard - no vendor publishes numbers:
  - Unifyr/Zift calls sales metrics "the most visible and telling" but gives no numbers (vendor blog).
  - PartnerStack prioritizes by program maturity, not weight (vendor taxonomy).
- Every weight is the user's design decision - write the reason next to it.

## Target + red-flag pattern

Give every KPI two numbers, never one:

- **Target**: what a healthy partner of that type and tier achieves.
- **Red-flag floor**: the value that triggers the underperformance ladder - not just a yellow cell.

A target alone hides decay; a partner can drift for quarters below "good" without ever crossing a line anyone acts on. Both numbers are user-set, treat them as design decisions, not industry-standard thresholds.

## Measurement windows

- Match the revenue window to the sales cycle: rolling 12 months smooths lumpy enterprise deals; a quarterly window suits high-velocity motions.
- Score activity metrics (registrations, engagement, certifications) on the current quarter - they are the early-warning layer.
- State the window on every KPI; two people computing the same metric over different windows will dispute the score.

## Gameability checks

- Reject self-reported pipeline, partner-attested activity, and logo counts - the documented gaming vectors.
- Accept only data recorded by program-owned systems (CRM, PRM, LMS, MDF ledger) that the program can defend in a partner dispute.
- Test each metric: "could a partner improve this number without improving the underlying behavior?" If yes, drop or redesign it.

## Scoring non-transacting partner types

Give each type its own track - never a blanked-out revenue scorecard. Each list below is in efficiency order: build left to right and stop when the track has enough dimensions to decide with. Counts the program already records come first; attributed revenue comes last everywhere, because attribution costs a quarter and invites the very dispute the scorecard exists to settle.

- **ISV/tech partners**: integration attach rate on closed deals > joint-solution certifications > integration adoption/health among shared customers > capped influenced revenue.
- **Referral partners**: accepted referrals > referral-to-opportunity conversion > sourced pipeline value > referral quality (win rate of referred deals, which needs a year of closed history before it means anything).
- **Advisory/SI partners**: co-delivered implementations > certified consultant headcount > implementation CSAT > capped influenced revenue.

Attach rate, accepted referrals and co-delivered implementations lead their tracks because each settles the same decision the composite settles for a reseller - is this partner producing - at near-zero plumbing cost. Re-rank per program:

- Product telemetry the team cannot query demotes attach rate and integration health below certifications.
- An attribution model already agreed with finance promotes influenced revenue to the front of every track.

## Negative example - a scorecard that fails

Illustrative; every listed flaw is a real anti-pattern:

- 14 metrics, no weights - nobody knows what matters, so nothing moves.
- "Pipeline" is partner-self-reported - inflated every quarter before review.
- One blended "partner revenue" number - sourced and influenced indistinguishable, finance rejects it.
- Targets only, no red-flag floors - decline is visible but never actionable.
- No data source or owner per metric - three teams compute three different scores.
- One identical scorecard for resellers and ISVs - every ISV scores zero on revenue and disengages.
