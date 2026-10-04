# Disclosure ladder

The five rungs a project can climb, what each one buys, what it obligates, and how real projects have positioned themselves.

## Contents

- [The rungs](#the-rungs)
- [Choosing a rung](#choosing-a-rung)
- [Reference positions](#reference-positions)
- [The ratchet](#the-ratchet)

## The rungs

| Rung                   | What you publish                                                                | What it buys                                       | What it obligates                                                       |
| ---------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------- |
| 1. Shipping log        | Releases, merged work, fixes                                                    | Proof of life; adoption confidence                 | Keep shipping, or the silence is visible                                |
| 2. Decisions           | Architecture choices, rejected options, scope cuts, license and pricing changes | Technical credibility; fewer "why did you…" issues | Explain the next reversal too                                           |
| 3. Failures            | Outages, bad releases, wrong bets, postmortems                                  | The highest trust-per-word available               | Publish the uncomfortable ones, not only the flattering ones            |
| 4. Operational metrics | Downloads, installs, contributors, response times, uptime                       | Momentum evidence a buyer or contributor can check | A baseline you will be compared against forever                         |
| 5. Financials          | MRR/ARR, churn, salaries, runway, sponsorship income                            | Maximum attention; sponsorship and hiring pull     | Publishing the bad quarters; legal review; changed negotiating position |

Rungs are cumulative in practice: nobody publishes revenue while hiding releases.

## Choosing a rung

The default ranking lives in `SKILL.md` step 2 - efficiency: `shipping log > decisions-and-failures essays > open-startup dashboard`. The list below is not a second order; it is the set of conditions under which the stated outcome overrides that default.

- **Want adoption?** Rungs 1-2. Evaluators want evidence the project is alive and thought through.
- **Want contributors?** Rungs 1-3. Visible reasoning and visible failure are what convince a stranger they could help.
- **Want sponsors or funding?** Rungs 3-4, and rung 5 only if the numbers argue for you. Sponsors fund a project whose need and trajectory are legible.
- **Want a hiring or credibility signal for yourself?** Rungs 2-3 carry it; metrics rarely do.
- **Selling to companies?** Rung 4 helps procurement (maturity, responsiveness); rung 5 can hurt if the numbers look small next to an incumbent.

Two constraints override the preference:

1. **Capacity.** Rung 3 needs writing time when things are going badly - exactly when there is least of it.
2. **Consent.** Rungs 4-5 usually involve data belonging to co-founders, investors, employees or customers. Get agreement before the first publication, not after the first complaint.

## Reference positions

Verified 2026-08-26.

- **Buffer** (`buffer.com/open`) - the widest published set in practice: monthly active users, MRR, ARR, ARPU, monthly shareholder updates, individual and executive salaries, support response times and satisfaction, public roadmap, time-off policy. Stated purpose: "to build trust, hold us accountable to a high standard, and push our industry forward."
- **Ghost** (`ghost.org/about`) - a live financial feed: ARR, monthly run rate, net churn, active customers, monthly requests, GitHub stars, install count, framed as accountability for a non-profit organization.
- **Baremetrics Open Startups** (`baremetrics.com/open-startups`) - a directory of companies publishing monthly revenue; rung 5 as a shared benchmark rather than a solo dashboard.
- **Plausible** (`plausible.io/about`) - deliberately lower: fully public AGPLv3 source ("the code is public and auditable"), milestone-only revenue disclosure, no live financial dashboard. Accountability through auditable code rather than a metrics feed.

Plausible is the counter-example worth quoting to anyone who thinks building in public means publishing revenue: a project can be radically transparent about how it works and reticent about how much it makes.

## The ratchet

Published numbers cannot be unpublished, and two effects follow.

- **Silence reads as bad news.** A dashboard that goes stale after a bad quarter tells the story anyway, in the least flattering form. Only publish a metric you are willing to publish while it declines.
- **Climbing down costs more than never climbing.** Removing a salary or revenue page invites the question of what changed. Choose the rung the project can hold through a bad year - not the one that performs best this month.

Rungs 1-3 are recoverable: nobody audits whether a postmortem appeared last quarter. Rungs 4-5 are not.
