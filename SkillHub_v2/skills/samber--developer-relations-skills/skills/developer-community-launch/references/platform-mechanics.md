# Venue mechanics

Contents: the four venue classes → named-vendor mechanics → verification rules → the one-venue rule. The class ranking itself lives in the skill body, where the choice is made.

Vendor pricing, limits and features change often. Treat every figure here as a starting point to re-verify on the vendor's own pricing or documentation page before putting it in a recommendation, and say when it was last checked.

## The four venue classes

Rows sit in the skill body's efficiency order - outcome bought per hour of standing moderation presence. The ordering, the per-class trade-offs and the constraints that delete a class live there; this file only carries what the classes are made of and which vendor implements them. Never re-rank them here.

| Class                    | Shape                               | Standing presence            | Wins on                                                                 | Loses on                                                      |
| ------------------------ | ----------------------------------- | ---------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------- |
| Forge-native discussions | threads attached to the repository  | an hour a week, batched      | no extra account, sits next to the code, indexed and exportable         | thinner community feel, ties the audience to one forge        |
| Rented public space      | subreddit, Q&A site, ecosystem chat | an hour a week of showing up | existing traffic, no seeding, no hosting, host absorbs moderation       | no ownership, host's rules, no member data                    |
| Owned async forum        | threaded, indexed pages             | an hour a day                | public search traffic, durable answers, ownership, per-instance pricing | slower velocity, higher effort per post, you hold member data |
| Owned real-time chat     | synchronous, channel-based          | a standing job               | immediacy, culture, low join friction, fastest feedback loop            | searchability, archive value, always-on expectation           |

The primary outcome promotes a class above its default rank:

- Support deflection with durable answers → async forum or forge-native discussions.
- Fast-moving product feedback and founder presence → real-time chat, and only if continuous presence is staffed.
- Contributor recruitment for an open-source project → forge-native discussions first; a separate venue only once discussion volume outgrows the repository.
- Awareness with no staffing → rented public space; participate rather than launch.

## Named-vendor mechanics

Listed in the same class order, best ratio first.

**GitHub Discussions** (forge-native):

- "a collaborative communication forum for the community around an open source or internal project"; discussions "do not need to be tracked on a project and are not related to code".
- Supports categories, polls and marking comments as answers, and converts both ways with issues.
- Any authenticated user who can see the repository can post. Creating categories, pinning and deleting need write permission; marking answers or locking needs triage permission.
- Zero extra account for an audience already on the forge, which makes it the cheapest first venue for an open-source project.
- Source: <https://docs.github.com/en/discussions/quickstart>.

**Rented public spaces** (subreddits, Q&A sites, ecosystem chats) - no hosting or seeding cost and existing traffic, but the host owns moderation policy, the archive and the member relationship, and the space can change its rules or disappear. Use to validate demand before owning a venue, and to reach an audience that would never join a vendor's room.

**Discourse** (owned async forum):

- Open source and free to self-host. Hosted plans listed at $100/month (Pro) and $500/month (Business), plus a free exploration tier.
- Cost is per instance, not per member: the opposite scaling shape from per-seat chat.
- Threaded, indexed, exportable.
- Best fit when answers have a long half-life and search traffic is an acquisition channel; the cost is a slower, higher-effort posting culture.
- Source: <https://www.discourse.org/pricing>.

**Discord** (owned real-time chat):

- Free at any member count, so cost does not scale with growth.
- Community features (rules screening, welcome and onboarding flows, announcement channels, forum-style channels, server insights) are opt-in per server.
- Real-time by default with weak public searchability.
- Discovery and partner-program requirements sit on support pages that block automated fetching; verify manually before promising discovery reach.
- Best fit is a large, informal, hobbyist or ecosystem audience.
- Free to open, and it is the standing presence, not the price, that decides whether it can be kept alive.

**Slack** (owned real-time chat):

- Free plan keeps 90 days of message history and up to 10 apps, with 1:1 external messaging only. Paid plans are per user per month (Pro listed around €8.25 monthly, €6.75 annual at the time of check).
- Two consequences: the free tier deletes the archive that makes a community searchable, and per-seat pricing makes an open community structurally expensive as it grows.
- Best fit is a bounded B2B customer community where members are familiar with the client and the archive matters less than immediacy.
- Source: <https://slack.com/pricing>.

## Verification rules

1. Re-check pricing, free-tier limits and history retention on the vendor's own page before recommending; quote the check date in the brief.
2. Check export and data-portability claims specifically - the ability to leave decides how reversible the choice is.
3. Check moderation tooling against the staffing floor: continuous-presence venues need more hours than the owner may have.
4. Check accessibility constraints for the audience's region, employer network policies and language support before committing.

## The one-venue rule

Running two owned venues before either reaches critical mass splits the same conversation volume in two and makes both look dead. Pick one primary venue. Give any second surface a distinct, non-overlapping job - announcements only, or long-form Q&A only - and say so publicly, so members know where to post.
