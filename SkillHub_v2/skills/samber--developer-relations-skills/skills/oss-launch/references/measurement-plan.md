# Launch measurement

## Baseline capture (evening before)

Every launch number is a delta; repository traffic panels keep only a short rolling window. An uncaptured baseline is unrecoverable. Snapshot and store outside the platform:

- Stars, forks, watchers.
- Unique visitors and unique cloners for the last available period.
- Registry downloads for the last full week (and the week before, to know the trend).
- Documentation sessions, and sessions on the quickstart page specifically.
- Open issues, external contributors, dependent projects.
- Current referrer list.

## Windows

### Day 1: Attention

| Metric                               | Read it as                                               |
| ------------------------------------ | -------------------------------------------------------- |
| Anchor thread rank and comment count | Whether the community engaged or scrolled past           |
| Stars per hour vs baseline           | The velocity discovery surfaces sample                   |
| Unique cloners                       | Readers who moved from reading to trying                 |
| Referrer mix                         | Which channel actually delivered, versus which felt loud |
| Demo/playground sessions             | Whether the demo carried the pitch                       |

Expect a large "direct" bucket: aggregators, chat clients and privacy-preserving browsers strip referrers. Tag links where the channel allows it and treat the rest as directional.

### Day 7: Trial

| Metric                                     | Read it as                                                           |
| ------------------------------------------ | -------------------------------------------------------------------- |
| Registry downloads vs pre-launch week      | Real installs, the first honest adoption number                      |
| Cloners still above baseline               | Interest that outlived the thread                                    |
| Quickstart page sessions and scroll depth  | Whether trial converts to first success                              |
| Issues and questions from outside the team | People who got far enough to hit a wall - the strongest early signal |
| Secondary pickups                          | Newsletters, reposts and translations that extend the window         |

### Day 30: Adoption

| Metric                                        | Read it as                                            |
| --------------------------------------------- | ----------------------------------------------------- |
| Retained download run-rate vs pre-launch week | The only number that separates adoption from applause |
| Repeat visitors and returning cloners         | Ongoing use rather than one-time curiosity            |
| First external pull request                   | The contributor funnel opening                        |
| Dependents / reverse dependencies             | Other projects betting on yours                       |
| Posts, talks or projects built on top         | Organic distribution starting                         |

Set targets as multiples of the project's own baseline, not as absolute numbers copied from someone else's launch. Comparing against peers is only meaningful within the same language, category and project age.

## Scale calibration instead of benchmarks

Launch-day stars per hour, front-page point thresholds and typical day-1 download lift circulate as if they were benchmarks; they trace back to single anecdotes and launch-consultancy claims. Product Hunt's vote thresholds are the clearest example: specific "500–1,200 quality-weighted upvotes for Product of the Day" figures are repeated everywhere and confirmed nowhere, while the platform itself says only that ranking runs on points and that "there's no secret formula".

Tell the user the number is unverifiable rather than quietly substituting a plausible one. A target invented to look rigorous produces a launch judged against fiction.

What _is_ documented, and useful as scale calibration rather than as a target:

- A launch can move real infrastructure load by an order of magnitude overnight. Supabase's own founding story is an early user posting it to an aggregator, the post staying on the front page for days, and "the number of databases we were hosting increased ten-fold." See the burnout note below, because this is the same event.
- Fork risk is measurable and large when a licensing decision goes wrong: the OpenTF manifesto drew endorsements from over 140 companies and 700+ individuals within weeks, and the resulting fork sits at roughly 35,800 stars.

## Over-performance is a failure mode too

The diagnosis table above assumes the launch under-performed. Plan for the inverse: a launch that outruns the team's capacity lands on a structurally fragile base. Tidelift's maintainer surveys put burnout at 46% of professional open-source maintainers, rising to 58% for maintainers of widely-used projects, with almost 60% having quit or considered quitting a project. Most projects are maintained by one or two people.

Decide the escalation trigger before launch day, while nobody is under load: at what issue volume do you switch to templates and `good first issue` routing, lock noisy threads, or freeze contributions temporarily. Recent precedent that this is not hypothetical - curl closed its long-running bug bounty in January 2026 after its confirmed-vulnerability rate fell from above 15% to below 5% under a flood of low-quality submissions, the maintainer describing it as "an attempt to reduce the noise".

## Diagnosing a flat launch

Localize the failure by funnel stage before changing anything:

| Symptom                              | Likely cause                                                | Fix                                                                         |
| ------------------------------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| Few impressions, few clicks          | Title and one-liner failed                                  | Rewrite the positioning; a relaunch with the same framing fails identically |
| Clicks fine, stars/clones low        | The README lost the ten-second read                         | Restructure the top of the README, add the demo                             |
| Clones fine, downloads/retention low | Install or first-run friction                               | Re-run the cold-run protocol; fix, then release                             |
| Everything fine, no discussion       | The project is understood and unremarkable to that audience | Wrong channel or differentiation is genuinely thin - decide which honestly  |
| Spike then zero on every metric      | Novelty-only interest                                       | Nothing to fix in the launch; the next release cycle is the real test       |

Only "wrong channel" justifies relaunching elsewhere. The rest justify fixing the artifact first, because a relaunch spends the novelty budget a second time.

## What not to report

- Stars as adoption. They are bookmarks; correlation with usage is weak.
- Launch-window traffic presented as a sustained baseline.
- Impressions or "reach" from platforms that count a scroll-past as a view.
- Any number bought, traded or solicited - beyond the ethics, platforms detect it, and an audit later costs far more than the flat week it papered over.
