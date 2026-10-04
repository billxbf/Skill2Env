# Tier ladders, rewards and sponsorware

Real published ladders, what each one is actually selling, a weak ladder with its diagnosis, the sponsorware rules, and a filled brief.

## Contents

- Ladder 1: project at ecosystem scale (Vue.js)
- Ladder 2: individual maintainer selling placement (Sindre Sorhus)
- Ladder 3: individual maintainer selling content (Caleb Porzio)
- Weak ladder and diagnosis
- Reward catalogue by delivery cost
- Sponsorware rules
- Filled ladder section

## Ladder 1: project at ecosystem scale (Vue.js)

| Tier                   | Price/month          | Reward                                                                                   |
| ---------------------- | -------------------- | ---------------------------------------------------------------------------------------- |
| Global Special Sponsor | custom, limited to 1 | above-the-fold logo on the homepage, plus a shoutout from an account with 320k followers |
| Platinum               | $2,000               | prominent logo on the homepage, in the docs sidebar and in the core READMEs              |
| Gold                   | $500                 | large logo on the homepage and in the core READMEs                                       |
| Silver                 | $250                 | medium logo in `BACKERS.md`                                                              |
| Bronze                 | $100                 | small logo in `BACKERS.md`                                                               |
| Generous Backer        | $50                  | name listed above other individual backers                                               |
| Individual Backer      | $5                   | name listed                                                                              |

What it sells: **attention it demonstrably owns**. Every tier is a placement, ordered by how many people see it. Scarcity is used once, at the top.

Individuals are served by two cheap tiers at the bottom and never mixed with the company ladder.

Do not copy this shape onto a project with no homepage traffic - the ladder works because the placements are worth the money.

## Ladder 2: individual maintainer selling placement (Sindre Sorhus)

| Tier     | Price/month | Reward                                                                                                        |
| -------- | ----------- | ------------------------------------------------------------------------------------------------------------- |
| $5 / $10 |             | sponsor badge on profile                                                                                      |
| $50      |             | name in the "Top Supporter" section of a thanks page                                                          |
| $100     |             | company logo on one chosen repository, plus the thanks page                                                   |
| $200     |             | logo on two chosen repositories                                                                               |
| $800     |             | logo on Awesome Node.js (20k views/month) and Awesome Electron (6k views/month), plus two chosen repositories |
| $1,000   |             | logo on the main Awesome list (60k views/month), plus the above                                               |

What it sells: **an ad rate card with published traffic numbers**. Naming the monthly views is what turns a donation request into something a marketing budget can approve. Logo placements exclude text and UTM parameters - a boundary worth copying, since it keeps the repository from becoming an ad unit.

## Ladder 3: individual maintainer selling content (Caleb Porzio)

Two tiers only: **$7** with no perks ("just say thanks"), and **$14/month** unlocking private screencasts. He tested $9 before settling on $14. Result at the time of writing: 535+ sponsors, $112,680/yr, having gone from roughly $40k to over $100k in about three months once the screencast tier launched.

What it sells: **an ongoing content subscription**, renewed with each release. Three of his conclusions transfer directly:

- "You can build the greatest tool on the internet, but it means nothing if no one's paying attention to you." The audience precedes the offer.
- "If people have the option of paying $1-5/mo. instead of >$14, they will pay the lesser amount." Never place a partial-perk tier just below the converting tier.
- Name tiers for the buyer - "The Agency" implies business use; "Platinum" implies nothing.

## Weak ladder and diagnosis

```
$1    -  Thank you!
$5    -  Thank you + your name in the README
$10   -  Your name in the README, bigger
$25   -  Name in README + I'll answer your questions faster
$50   -  All of the above + monthly 1:1 call + logo somewhere
```

Everything wrong with it, in order of damage:

1. **No company tier.** The top price is $50; the companies depending on this project cannot buy anything, and $50 clears no procurement process.
2. **A 1:1 call at $50.** At 40 sponsors that is a working week per month, sold at a rate no consultant would accept. It is the first thing to break, in public.
3. **"Faster answers" sold at $25.** Priority _outcomes_ cannot be delivered honestly and poison the review queue for everyone else.
4. **Four tiers selling the same reward at different sizes.** Nothing distinguishes $5 from $10 except font size, so everyone picks $5.
5. **"Logo somewhere."** A benefit an approver cannot evaluate is a benefit nobody buys.
6. **Prices that cannot be raised.** On GitHub Sponsors these five are permanent until retired and replaced.

Rewritten:

- $5: name in BACKERS.md.
- $25: name + thanks-page listing.
- $250: logo in the README (traffic: N/month).
- $1,000: logo in README and docs, quarterly office hours.
- $4,000: the above plus 48-hour security triage and named upgrade support.

## Reward catalogue by delivery cost

| Cost at 10x sponsors | Rewards                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------ |
| Near zero            | name in `BACKERS.md`, README or docs logo, sponsor badge, thank-you post, release-notes mention              |
| Bounded              | private repository per tier, quarterly group office hours, early access to releases, sponsor-only newsletter |
| A second job         | monthly 1:1 calls, per-sponsor content, bespoke integrations, guaranteed response times without a contract   |
| Never sell           | roadmap control, merged pull requests, priority outcomes, exclusivity over the project's direction           |

Apply the test to every reward before it is published: _what does this cost every month at ten times today's sponsor count?_ Anything in row three either becomes a priced retainer with a written scope, or it does not ship.

## Sponsorware rules

Sponsorware: release new work **to sponsors first**, then open-source it at a published threshold (a sponsor count, an amount, or a date). Documented to have added $11k/yr within days for one maintainer, and repeated successfully by others in the same ecosystem.

- **Publish the release trigger up front and honour it.** A threshold that keeps moving costs more goodwill than the revenue is worth.
- **Gate convenience, never necessity.** Tutorials, templates, early access and tooling are fair game. The core library, its security fixes, and the documentation needed to use it are not.
- **Keep a genuinely useful free path**, linked from the docs - it is the discovery route into the paid tier.
- **Ship on a cadence.** A one-off gated release buys one month of sponsorship; a batch shipped with each release buys a subscription.
- **Budget production time**, and check licence and employer constraints before gating anything derived from work someone else owns.

## Filled ladder section

```markdown
## Ladder - libfoo (Python HTTP client, 4.2k stars, docs ~18k views/month)

| Tier                                                                                            | Price  | Reward                                                         | Delivery cost/month at 10x        |
| ----------------------------------------------------------------------------------------------- | ------ | -------------------------------------------------------------- | --------------------------------- |
| Backer                                                                                          | $5     | name in BACKERS.md                                             | ~0 (scripted)                     |
| Supporter                                                                                       | $25    | name in BACKERS.md + thanks page                               | ~0                                |
| Team                                                                                            | $250   | small logo in README + docs footer                             | 10 min/quarter                    |
| Business                                                                                        | $1,000 | large logo README + docs sidebar, quarterly group office hours | 1 h/quarter                       |
| Infrastructure                                                                                  | $4,000 | above + 48h security triage + named upgrade support            | ~4 h/month, capped, written scope |
| Not for sale: roadmap priority, merged PRs, exclusivity.                                        |
| Converting tier: Team. Gratitude tiers sit below it; no partial-perk tier between $25 and $250. |
```
