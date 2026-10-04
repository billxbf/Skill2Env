# Boundary rules

What never gets published, what needs a deliberate call, and the check that runs before every post.

## Contents

- [Hard blocks](#hard-blocks)
- [Grey zones](#grey-zones)
- [Pre-publish check](#pre-publish-check)
- [Publishing bad news](#publishing-bad-news)

## Hard blocks

**Unpatched vulnerabilities.** Coordinated disclosure is the ecosystem norm: the initial report stays private and full details are published only once a fixed version exists. Nothing about an unfixed weakness goes public - not a commit message, not a "chasing a weird bug" post, not a livestream of the fix. After the fixed release ships, say plainly that it contains a security fix, so downstream users know to upgrade rather than treating it as an optional patch.

**Customer and user data.** Named customers, logos, per-account usage, screenshots containing real accounts - every one needs explicit permission, including inside an aggregate dashboard.

**Employee data.** Individual salaries, performance, health, departures. Open-salary models work because a published formula is applied to roles with everyone's consent; they are not a license to disclose facts about a person.

**Material non-public information.** With outside investors, an acquisition process, or a public-company parent, disclosing revenue, forecasts or customer counts is a legal question before it is a marketing one. Route it through counsel.

**Third-party confidential material.** Partner architecture, unreleased vendor features, NDA'd terms, embargoed private-beta content.

**Live incidents, before the facts are established.** Status updates belong on a status page; analysis belongs in a postmortem once causes are confirmed. Public mid-incident speculation creates a second incident.

**Team conflict.** Airing internal disagreement damages the people in it and deters contributors, and teaches the audience nothing transferable.

## Grey zones

These need an explicit decision, recorded in the charter, not a reflex.

**Unshipped features and dates.** The named risk is the Osborne effect: customers canceling or deferring orders for the current product after a premature announcement of its successor. The Osborne Computer Corporation announced prototype successors in 1983; dealers canceled orders for the shipping machine, and sales collapsed.

If a roadmap is published anyway, publish it with explicit non-commitment language, following GitHub's public roadmap:

- "is subject to change, especially further out on the timeline"
- "does not represent a commitment, guarantee, obligation or promise to deliver any product or feature, or to deliver any product and feature by any particular date"
- customers should not rely on it for purchasing decisions

Copy that pattern: direction and sequencing in public, dates only for work already shipping.

**Revenue as a solo maintainer.** Publishing income attracts sponsorship and entitlement in the same motion ("you earn this much, fix my issue"). Decide whether the funding upside outweighs the shift in support expectations, and pair any disclosure with a published statement of what maintenance the money does and does not buy.

**Competitive strategy.** Describing what you built is usually safe. Describing why it wins, where the moat is, and what you will build next hands a plan to a better-resourced competitor.

**Hiring, layoffs, departures.** Legally constrained in most jurisdictions and involving people who never opted into the practice. Announce facts the people involved have approved, and nothing else.

**Numbers that look small.** Not a risk category on its own - small honest numbers with a trajectory beat vague claims. The risk is publishing one flattering slice and being asked for the rest.

## Pre-publish check

Run four questions against every post, including replies written in a hurry:

1. Does this expose an unfixed security weakness, directly or by hint?
2. Does this contain a third party's data, name, or confidential material without consent?
3. Does this commit us to a date, number, or feature we do not control?
4. Would this sentence be a problem if a competitor, a journalist, or a hostile commenter quoted it alone?

Any yes means rewrite or delay. A disclaimer does not neutralize a yes.

## Publishing bad news

Bad news published on your own terms is the highest-value content the practice produces; the same news extracted by someone else is the most damaging.

- Publish once, in full, in one place, and link every reply to it rather than relitigating in threads.
- Lead with impact on the reader, then cause, then what changes - never the reverse order.
- Say what is not yet known and when the next update lands, then meet that date.
- Skip blame of individuals, vendors, or contributors; systemic description survives scrutiny, personal attribution does not.
- Never post a correction as a reply to a stale post: publish it at the same prominence as the original claim.
