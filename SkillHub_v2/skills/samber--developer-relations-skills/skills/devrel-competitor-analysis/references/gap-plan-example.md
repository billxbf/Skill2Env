# Worked example

Contents: [Peer set: wrong and right](#peer-set-wrong-and-right) · [Scenario](#scenario) · [Scorecard excerpt](#scorecard-excerpt) · [Per-surface read](#per-surface-read-excerpt) · [Time to first success](#time-to-first-success) · [Gap plan](#gap-plan) · [Weak row rewritten](#weak-row-rewritten) · [Reading a burst](#reading-a-burst) · [Method and limits](#method-and-limits)

Company names here are placeholders. Use real observed values in a real report - never carry these numbers over.

## Table of Contents

- [Peer set: wrong and right](#peer-set-wrong-and-right)
- [Scenario](#scenario)
- [Scorecard excerpt](#scorecard-excerpt)
- [Per-surface read (excerpt)](#per-surface-read-excerpt)
- [Time to first success](#time-to-first-success)
- [Gap plan](#gap-plan)
- [Weak row rewritten](#weak-row-rewritten)
- [Reading a burst](#reading-a-burst)
- [Method and limits](#method-and-limits)

## Peer set: wrong and right

The peer set decides everything downstream, and the tempting version is wrong often enough to be worth a worked pair.

**Wrong**

> Peer set: the four best-funded vendors in the observability category, ranked by last raise.

Three problems compound:

- Funding rank picks companies whose motion is sized for distribution the user does not have, so most findings arrive already unusable.
- Every peer sits in the same category, so the set inherits one shared blind spot and produces no copyable idea from outside it.
- Nobody asked what an evaluator would actually do instead of buying, which for a tracing tool is frequently "keep the open-source collector and grep the logs", a competitor with no funding at all.

**Right**

> Peer set: Northwind (category leader - sets the expectation an evaluator arrives with), Kestrel (closest direct substitute, same stage and price point), Fernpath (adjacent-category outlier - a database company whose contributor-onboarding practice is worth stealing), and the default alternative, which for our segment is self-hosting the open-source collector.
>
> Excluded: two rivals with no public developer surface to observe, and one acquired last year whose motion is frozen and will not predict anything.

Roles, not a ranking. The fourth entry comes from asking what a developer would use if the product vanished - a demand-side reading of the competitive set, which routinely surfaces documentation, a forum answer or a hand-rolled script rather than a funded vendor. The exclusions are written down because an unstated exclusion is where the blind spot hides.

## Scenario

An observability startup ("Ours") sells a self-serve tracing tool to backend engineers, with an enterprise tier a platform team signs off on. Peer set:

- **Northwind** - category leader, sets the expectation.
- **Kestrel** - closest direct substitute, same stage.
- **Fernpath** - adjacent-category outlier, a database company whose docs practice is worth stealing.

Excluded: two rivals with no public developer surface at all, and one acquired last year whose motion is frozen.

## Scorecard excerpt

Observed 2026-08-28. Sources footnoted per cell in the real report.

| Observation                             | Ours     | Northwind        | Kestrel      | Fernpath             |
| --------------------------------------- | -------- | ---------------- | ------------ | -------------------- |
| Quickstart exists                       | yes      | yes              | yes          | yes                  |
| Steps to first result                   | 11       | 4                | 7            | 3                    |
| Timed first success                     | 34 min   | 6 min            | 18 min       | 5 min                |
| Credit card before first result         | yes      | no               | no           | no                   |
| SDK languages                           | 3        | 8                | 4            | 6                    |
| Languages with their own quickstart     | 1 of 3   | 8 of 8           | 2 of 4       | 6 of 6               |
| Doc modes present per major feature     | ref only | all four         | ref + how-to | all four             |
| Migration guide per major version       | no       | yes              | no           | yes                  |
| Public changelog with feed              | no       | yes              | yes          | yes                  |
| Releases, last 12 months                | 9        | 26               | 14           | 31                   |
| Median time to first response on issues | 4 d      | 1 d              | 2 d          | <1 d                 |
| Merged PRs from outside the company     | 4%       | 11%              | 6%           | 34%                  |
| Blog posts/month, 12-mo median          | 1.5      | 6                | 2            | 4                    |
| Posts per named DevRel human            | 1.5      | 1.2              | 2.0          | 1.3                  |
| Evergreen share of posts                | 30%      | 55%              | 25%          | 70%                  |
| Primary community venue                 | none     | forum            | chat         | forum                |
| Median time to first reply              | n/a      | 3 h              | 9 h          | 2 h                  |
| Staff share of replies                  | n/a      | 40%              | 85%          | 25%                  |
| Conferences sponsored                   | 1        | 12               | 3            | 5                    |
| Own recurring event                     | no       | annual user conf | no           | monthly office hours |
| Security/compliance page for buyers     | yes      | yes              | no           | yes                  |
| DevRel humans named publicly            | 1        | 5                | 1            | 3                    |

Note the two rows that carry the analysis. _Posts per named DevRel human_ shows the content gap is capacity, not discipline - Ours out-produces the leader per person. _Merged PRs from outside the company_ shows Fernpath running a genuinely different motion, not just a bigger one.

## Per-surface read (excerpt)

**Documentation and DX.**

- Credit card: every peer reaches first success without one; Ours does not.
- Quickstart per language: all three peers publish one per SDK language; Ours publishes one and expects the other two languages to adapt it.
- Documentation modes: Northwind and Fernpath cover all four per feature; Ours ships reference only, so an evaluator who does not already know the product has nothing to read.

The structural difference: peers treat the docs set as a product surface with its own coverage rule; Ours treats it as reference generated from code.

**Open source.** Fernpath is the outlier that matters: a third of merged pull requests come from outside the company, against 4-11% for everyone else. That is a contributor-onboarding practice - labelled first issues, a documented development environment, sub-day first response - not a side effect of popularity.

## Time to first success

| Company   | Minutes | Blocking step                                                      |
| --------- | ------- | ------------------------------------------------------------------ |
| Ours      | 34      | credit card wall at step 4; sample app assumes a running collector |
| Northwind | 6       | none                                                               |
| Kestrel   | 18      | API key issued by email, ~7 min wait                               |
| Fernpath  | 5       | none                                                               |

The credit card wall is the single widest observed gap and the cheapest to remove.

## Gap plan

Sorted by impact per unit of cost, highest first - not by impact alone, and not cheapest first. The reference-only docs row outranks the changelog feed despite costing more, because the ratio, not the price, decides what gets done first.

| Gap                                      | Impact | Cost   | Verdict                                                                                                                    | Owner       | Date           |
| ---------------------------------------- | ------ | ------ | -------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------- |
| Credit card required before first result | high   | low    | close - free sandbox key, no card                                                                                          | DX lead     | 2026-09-30     |
| No quickstart for 2 of 3 SDKs            | high   | low    | close - port the primary quickstart                                                                                        | DX lead     | 2026-10-15     |
| Docs are reference-only                  | high   | medium | close - one how-to and one explanation per major feature                                                                   | Docs        | 2026-12-15     |
| No public changelog feed                 | medium | low    | close - publish with a feed                                                                                                | Docs        | 2026-10-01     |
| No migration guide practice              | medium | medium | close - start with the next major                                                                                          | Eng + Docs  | next major     |
| 4% outside contribution                  | medium | high   | counter - we are not an OSS-first product; lean on the managed onboarding path instead                                     | -           | -              |
| No community venue                       | medium | high   | ignore this quarter - under 800 active users, a dead channel reads worse than none; revisit at 2,000                       | DevRel lead | review 2027-01 |
| 1 conference sponsored vs 12             | low    | high   | ignore - Northwind buys reach we cannot outspend; speaking slots at 3 events instead                                       | DevRel lead | 2026-11        |
| 1.5 posts/month vs 6                     | low    | high   | counter - per-head output already exceeds theirs; the constraint is headcount, and it belongs in the budget case, not here | -           | -              |

The recorded ignores are the point. Without them, "no community venue" gets rediscovered as a fresh insight every quarter.

What this sort starves is the bottom three rows: outside contribution, a community venue and event presence are each real evidence to an evaluator and each cost a program rather than a task, so a ratio ranking demotes them every quarter. Name that in the report with the condition that promotes them - the venue at 2,000 monthly active users, outside contribution if the product ever goes OSS-first - or the ranking quietly becomes a permanent veto.

## Weak row rewritten

**Before**

> Northwind has 18,400 GitHub stars and 42,000 community members. We have 2,100 stars and no community. We are significantly behind on community.

Three problems:

- Stars and total members can only rise, so neither carries trend information.
- Nothing here is actionable - "be bigger" is not a task.
- The comparison ignores that Northwind is seven years older with a much larger installed base, so the gap describes company age, not program quality.

**After**

> Northwind's forum answers a public question in a median 3 hours with 40% of replies coming from members rather than staff - a peer community, not a support desk. Ours has no venue. At our current 800 monthly active users, opening one would likely produce a visibly empty room, which reads worse to an evaluator than no venue at all. Verdict: ignore this quarter, revisit at 2,000 monthly active users; meanwhile cut issue first-response time from 4 days to under 1, which is the same signal at our scale and costs a rota rather than a program.

The rewrite reports a rate rather than a total, names the structural difference (peer answers versus staff answers), states why the obvious move is wrong at this stage, and lands on something the team can start on Monday.

## Reading a burst

Cadence charts invite the wrong conclusion in both directions, so annotate before interpreting.

**Wrong**

> Northwind published 22 posts in March and 3 in July. Their content operation is inconsistent and under-resourced; we can win on reliability.

**Right**

> Northwind's March spike (22 posts) lines up with their user conference and a major-version launch; the rest of the year holds a steady 4-6 per month. That is a planned launch burst on top of a maintained baseline, not instability. The comparable read for us is the baseline, where we sit at 1.5. Kestrel's flat 2 per month with no burst at all is the more interesting finding: they have no launch moment to concentrate around.

A practitioner reading of exactly this pattern - one vendor's 65-post month treated as deliberate launch cadence while another vendor's flat months were the real problem - is the sourced version of this correction. The general failure is symmetrical: a burst mistaken for a trend, and a burst mistaken for incompetence.

## Method and limits

State plainly what the report rests on:

- The twelve-month window.
- The four sampled weeks for community volume.
- Time-to-first-success is one run by one person on one machine.
- Team size counts named humans and is an undercount.
- Community size for chat venues is a volume proxy rather than a member count.
- No number here came from behind a login.

Close with what would change the conclusions - Kestrel shipping a free tier, or Northwind's user conference being cancelled - so the reader knows which findings are load-bearing.
