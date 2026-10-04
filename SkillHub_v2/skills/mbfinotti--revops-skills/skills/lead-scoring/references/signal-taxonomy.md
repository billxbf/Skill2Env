# Signal Taxonomy

Fit and engagement stay separate scores end to end. Blending them into one number loses the routing distinction that justifies scoring at all: high-fit/low-engagement is a cold prospect worth nurturing; low-fit/high-engagement is noise worth deprioritizing. Fit without intent is a cold prospect; intent without fit is noise.

## Fit signals - can they buy

Explicit data from forms and enrichment. Stable, so they never decay. Their usefulness is bounded by enrichment coverage, not by cleverness of the point values.

| Bucket             | Signals                                                                         | Notes                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Firmographic (B2B) | Industry, employee count, revenue band, geography, funding stage                | Strongest single gate at high ACV                                                                                  |
| Demographic        | Job title, seniority, department, buying-committee role                         | Normalize titles before scoring; "Head of" != VP everywhere                                                        |
| Technographic      | Uses complementary tool; uses a competitor; uses the tool this product replaces | Competitor usage is positive fit (they understand the category) but often an exclusion for outreach - decide which |
| B2C fit            | Age band, location, purchase history, account tenure                            | Same axis, consumer-grade inputs; identical mechanics                                                              |

## Engagement signals - are they about to buy

Behavioral data, first-party. Rank by proximity to a purchase decision, not by ease of tracking.

| Tier                       | Signals                                                                                                                                              | Typical points (100-pt scale) |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| High intent                | Demo request, contact-sales form, trial start, pricing page 2+ visits, integration/API docs, ROI calculator                                          | +15 to +30                    |
| Medium                     | Webinar attendance, comparison page, case study 2+, multiple sessions in a week                                                                      | +8 to +15                     |
| Low                        | Single blog visit, newsletter click, single email click                                                                                              | +1 to +5                      |
| Vanity - score 0 or near-0 | Email opens (structurally unreliable since mail-privacy proxies fire them automatically), single content download, homepage-only visit, social likes | 0-2, hard-capped              |
| Negative                   | Careers-page-only visitor (job seeker)                                                                                                               | -30                           |

A diligent newsletter reader - or an automated inbox opening everything - must never be able to accumulate enough vanity points to look like a buyer. Hard-cap each low-tier category's total contribution so accumulation cannot substitute for intent.

## Third-party intent data

Real but noisy; treat as a layer, never a qualifier on its own.

- It is account-level: it identifies a company researching a topic, not a person ready to talk.
- Independent precision testing puts leading providers' topic-match accuracy in the low-to-high 80% range - a "surge" is a probability, not an intent; plenty of surges are an analyst building a market map.
- Use it to break ties and prioritize outreach among already-fit accounts, or to trigger monitoring. Never let a third-party signal alone push a lead across the MQL threshold.
- Privacy: third-party behavioral data carries the heaviest consent burden (GDPR profiling, browser third-party-cookie blocking already covers roughly a third of traffic).

## Exclusions vs negative points

Exclude absolute disqualifiers outright rather than assigning negative points - negative scoring rarely nets out cleanly against genuine engagement. A competitor employee browsing the pricing page daily will out-engage any fixed penalty.

**Exclusion list (suppressed from scoring and from the sales queue):** competitor email domains, students and .edu addresses (unless education is the market), existing customers, unsubscribes and spam complaints, hard bounces, internal test accounts.

**Negative points (soft demotions, not disqualifiers):** personal email address in a B2B motion (-10; relax for SMB), consultant/agency title (-10, may be evaluating for a client), IC-only contact at enterprise ACV (-15), invalid phone (-10).

## Decay

Engagement decays; fit does not - a job title does not go stale on its own. Without decay, every contact accumulates points indefinitely and stale contacts end up looking as hot as active ones. That decay must exist is not a choice; which mechanism delivers it is. Ranked by value per unit of effort, effort being admin config, engineering to build and run a recompute, and how much of the model reps can still explain afterwards:

- efficiency: tiered brackets > percentage per period > threshold reset
- value (stale points removed without forgetting a live buyer): percentage per period > tiered brackets > threshold reset
- effort: percentage per period > tiered brackets > threshold reset

| Mechanism             | Worked example                                                                                       | Effort                                                                                               |
| --------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Tiered brackets       | 0-30 days = 100% of points, 31-60 = 75%, 61-90 = 50%, older = context only (40 pts -> 30 -> 20 -> 0) | An hour - most scoring tools ship step rules natively, and a rep can read the bracket off the record |
| Percentage per period | An event worth 10 points at 50%/month decay contributes 5 after one month, ~0 after two              | A week to build a scheduled recompute over per-event history, then a standing job                    |
| Threshold reset       | Any score above 50 resets to 50 after 45+ days of inactivity                                         | Near-zero - one rule on the composite score, no per-event history needed                             |

Default to tiered brackets: near the smooth version's accuracy at admin-config effort, and auditable by the rep looking at the record. The threshold reset is last on efficiency despite being the cheapest, which is the whole point of ranking by ratio - it truncates a dormant record's score and never distinguishes a 60-day-old pricing visit from a 6-day-old one.

What this order starves: percentage-per-period decay, first on value and first on effort. Promote it where engagement carries the majority of the score and the decision window is days, not quarters (PLG and B2C), because bracket edges are too coarse there. Where the platform cannot store per-event timestamps, delete both brackets and percentage decay and say so - the threshold reset is then the only mechanism available, not the recommended one.

How fast to decay each signal is genuinely contested, and this one gets no ranking: it would be false precision, because the answer is set by the sales cycle rather than by any value/effort ratio. The rate that is correct on a 14-day PLG cycle is the rate that kills a nine-month enterprise deal. One camp decays high-intent actions fastest (pricing visits to zero in 15-30 days - heat matters only while fresh) and low-intent slowly (60-90 days); another never decays explicit hand-raises (a demo request stays actionable until a rep works it).

Choose by sales-cycle length: decay engagement to zero at roughly 1-2x the median cycle, and keep hand-raises undecayed until worked. Over-aggressive decay silently kills slow-burn enterprise deals - the model forgets the buyer before the committee finishes deciding.

## PLG and B2C product-usage signals

Same two-axis structure; the engagement axis is fed by product analytics instead of marketing touches. Everything above about caps, exclusions, and decay applies unchanged.

| Signal                                                                         | Typical points | Why it predicts                                                                             |
| ------------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------- |
| Activation milestone completed                                                 | +20            | Experienced the core value ("aha moment")                                                   |
| Core feature used 3+ times                                                     | +20            | Habit forming, not a tourist                                                                |
| Invited a teammate                                                             | +20, no decay  | Expansion inside the account; strongest PQL signal                                          |
| Hit a usage/plan limit                                                         | +15            | Concrete upgrade pressure                                                                   |
| Connected an integration                                                       | +15            | Workflow lock-in                                                                            |
| Daily-active streak                                                            | +10 to +20     | Sustained engagement                                                                        |
| B2C transactional: cart abandonment, repeat product-page visits, wishlist adds | trigger-grade  | Propensity signals that expire in hours - act on them near-real-time, not in a weekly batch |

Two PLG/B2C-specific rules:

- **Keep the fit layer even when usage dominates.** The classic PQL mistake routes high-usage, low-fit free users (students, consumers on a business product) to sales. A thin fit gate - work-email domain, company size band - filters them at near-zero cost.
- **Speed replaces committee dynamics.** With no buying group, one user's behavior qualifies the lead, and the decision window is days or minutes. Rescore at least daily, trigger instantly on threshold, and shorten every decay horizon accordingly.
