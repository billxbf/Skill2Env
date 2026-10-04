# Signal taxonomy

Classify each supplied signal into one category. The category sets the typical inference, where confirmation usually lives, what it costs to source, and how fast the signal goes stale. Freshness windows are practitioner heuristics, not measured thresholds - a signal outside its window is not banned, it just scores low on recency and needs a reason to survive ranking.

Categories appear in the efficiency order set in SKILL.md § Signal taxonomy - replies bought per minute of sourcing - so the first one you can confirm is usually the one to use. That order is a default: re-rank it against the tools the user already licenses, the size of their account list, and how many minutes per prospect they actually have.

**B2B efficiency**: hiring == leadership change > product and launch news > community and review activity > tooling change > public content and speaking > funding and financial. Relationship and mutual connection sits outside the order - highest value, and the only cost that lands on someone else's calendar.

Cost lines below use orders of magnitude only: near-zero, an hour, a week, a standing job. Nothing finer than that is real, and no ranking here depends on a precise minute count.

## Table of Contents

- [B2B signals](#b2b-signals)
- [B2C signals](#b2c-signals)
- [Interpretation principles](#interpretation-principles)

## B2B signals

### Hiring and job postings

- **Look for**: open roles in the function the offer serves, a hiring surge, a first-ever hire for a capability.
- **Surfaces in**: careers pages, job boards, professional networks.
- **Cost to source**: near-zero - one dated lookup on a page the account publishes about itself.
- **Typical inference**: the team is scaling into exactly the problems that come with scale - onboarding, process breakage, tooling ceilings.
- **Freshness**: while the posting is live, roughly 30-60 days.

### Leadership and role changes

- **Look for**: a new executive in the buying function, a former champion moving companies, a promotion into budget authority.
- **Surfaces in**: professional-network profiles and announcements, press releases, the user's own records.
- **Cost to source**: near-zero - a profile check, or a field the user's own records already hold.
- **Typical inference**: new leaders re-evaluate tooling and want early wins; a moved champion is warm context at the new account and churn risk at the old one.
- **Freshness**: strongest inside 30-90 days of the change taking effect.

### Product and launch news

- **Look for**: a launch, market or geographic expansion, rebrand, pricing change, new integration.
- **Surfaces in**: company blog and changelog, press, launch platforms.
- **Cost to source**: near-zero - the account publishes it and dates it for you.
- **Typical inference**: a strategic bet is live and the supporting workload just changed shape.
- **Freshness**: strongest inside ~60 days of the announcement.

### Community and review activity

- **Look for**: a question in a professional community, a review of a competitor or adjacent tool, a public feature request.
- **Surfaces in**: forums, review platforms, issue trackers, community spaces.
- **Cost to source**: near-zero per prospect once you know which venue your buyers use - but a standing job to monitor those venues, paid once for the whole segment and unaffordable for a rep on a daily activity quota.
- **Typical inference**: stated pain in their own words - the highest-value B2B signal when it names the exact job the offer does, because it replaces your inference with theirs.
- **Compliance cost**: a venue-norm judgement before every use. Engage where a reply is normal for that venue; never turn a public post into an uninvited private message, and never contact anyone off a personal-distress post.
- **Freshness**: strongest inside ~30 days.

### Technology and tooling changes

- **Look for**: adopting or dropping a tool, a migration, a competitor removed from the stack.
- **Surfaces in**: technology-detection services, job postings naming tools, engineering blogs, integration pages.
- **Cost to source**: near-zero with a detection service already licensed; an hour of inference from job postings and engineering blogs without one. Licensing one promotes this category several places up the order.
- **Typical inference**: active evaluation is happening or just finished - friction with the old tool or gaps in the new one are current.
- **Freshness**: strongest inside ~90 days of the change.

### Public content and speaking

- **Look for**: a post, article, podcast appearance, or conference talk by the prospect themselves.
- **Surfaces in**: professional networks, company blog, event agendas, podcast feeds.
- **Cost to source**: near-zero for a post you can read in a minute; an hour for a talk or podcast you have to watch end to end before you can cite it honestly.
- **Typical inference**: the topic they chose to speak on is a live priority; their own words are the safest vocabulary to mirror.
- **Rule**: cite the specific piece. "Loved your talk" without naming which one reads as fake and fails the swap test - which is why the hour is not optional once you claim to have watched it.
- **Freshness**: weeks for a post; a flagship talk can hold for a few months.

### Funding and financial events

- **Look for**: a raised round, acquisition or divestiture, IPO, major layoff, publicly reported results.
- **Surfaces in**: press coverage, company announcements, funding databases, professional-network posts.
- **Cost to source**: near-zero to spot the headline, an hour to qualify it down to what the money actually funds - and only the second version is an angle.
- **Typical inference**: new budget and new pressure to show growth - or, for layoffs, cost pressure and consolidation of tooling.
- **Why it ranks last**: the headline reaches every seller at once, so the unqualified version is the most-sent and least-differentiated angle in outbound. The event alone is not the angle; the problem it creates is.
- **Freshness**: strongest inside ~90 days.

### Relationship and mutual-connection signals

- **Look for**: a shared contact who can vouch, a past colleague, event overlap, a prior touch in the business's own records.
- **Surfaces in**: professional networks, the user's CRM record or inbox history, event attendee context.
- **Cost to source**: near-zero to spot, an hour or a week to activate - and the cost lands on the mutual connection's calendar, not yours, which is why it loses efficiency rounds despite topping the value axis.
- **Typical inference**: a warmer path exists than cold outreach - the ask can be bigger or the intro routed through the mutual.
- **Promote it anyway when**: the account is named and strategic, the deal is big enough that one warm intro outruns a quarter of cold touches, or a cold attempt has already failed.
- **Freshness**: relationship signals decay slowly, but a prior touch older than a couple of quarters needs acknowledging as such.

## B2C signals

First-party only: these exist inside a direct customer relationship and its marketing consent. See the B2B and B2C section of SKILL.md for the consent divergence. Third-party-sourced consumer behavioural data is deleted from this taxonomy, not ranked at the bottom of it - the consent basis does not exist, so it is never a fallback when first-party data is thin.

**B2C efficiency**: purchase behaviour == lifecycle stage > browsing and engagement > loyalty and advocacy.

Purchase and lifecycle tie because both fire off an event the business already records with a timestamp: near-zero effort per customer once the flow exists, and each carries its own timing, which is the whole angle. Browsing ranks below them because it needs an interpretation judgement on every use (the creepiness line). Loyalty ranks last against an acquisition or conversion goal because it serves a different ask class - promote it to the top when the goal is expansion or advocacy instead.

Every B2C category carries the same compliance cost: a marketing-consent check before the send, and no way to unsend. Cost to source is near-zero per customer across all four; the effort is the standing job of keeping the trigger data and the flows live.

### Purchase behaviour

- **Look for**: first purchase, repeat purchase, category jump, order-value change, abandoned cart.
- **Typical inference**: replenishment timing, complementary need, or a decision stalled at checkout.
- **Freshness**: cart signals decay in hours-to-days; replenishment windows follow the product's own cycle.

### Lifecycle stage

- **Look for**: signup age, trial or subscription window, renewal date, dormancy after activity, usage milestone.
- **Typical inference**: a decision point is approaching (convert, renew, lapse) - timing is the whole angle.
- **Freshness**: defined by the lifecycle event itself.

### Browsing and engagement

- **Look for**: repeated views of a product or pricing page, wishlist additions, email clicks, search terms on the business's own property.
- **Typical inference**: active consideration of a specific item or plan.
- **Caution**: reference the interest, not the surveillance. "Still thinking about [product]?" lands; "we saw you view this 11 times" is the creepy-over-familiarity failure mode.

### Loyalty and advocacy

- **Look for**: points thresholds, tier changes, a review left, a referral made.
- **Typical inference**: an engaged customer worth an expansion, reward, or advocacy ask - a different ask class than acquisition.

## Interpretation principles

- **Recency dominates**: a signal from this week outweighs a stronger-sounding one from last quarter. Timestamp everything.
- **Clusters beat singles**: two independent signals pointing the same way (hiring plus a tooling change) justify a firmer inference than either alone. A cluster of two near-zero-cost signals beats one expensive signal on both axes at once - build it before paying for the expensive one.
- **Absence is a signal only inside an existing relationship**: a paying customer gone quiet is a churn-risk signal; a stranger's silence means nothing.
- **Match altitude to seniority**: company-level signals for executives, team- and person-level signals for managers and ICs (Jason Bay, via 30MPC).
