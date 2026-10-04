# Metric catalog

Definitions, formulas, data sources and published guidance for the four pillars. Pick at most 8 metrics total, at least one per pillar.

Definitions here are quoted from published metric pages. The _readings_ attached to them are marked as published or as this catalog's own interpretation, because the published model states almost no numeric guidance of its own.

## Contents

- [What is actually published](#what-is-actually-published)
- [Activity](#activity)
- [Responsiveness](#responsiveness)
- [Contributor funnel](#contributor-funnel)
- [Concentration and risk](#concentration-and-risk)
- [Sentiment](#sentiment)
- [The starter set](#the-starter-set)
- [Unsourced practitioner thresholds](#unsourced-practitioner-thresholds)
- [Sources](#sources)

## What is actually published

Quote these verbatim. Everything else in this file is definition plus interpretation.

- "it's important not just to look at the numbers, but also at the trends"
- "we do not compare projects against each other, but instead, we expect teams to use their metrics to make improvements"
- "every project is a little different, so it's important to interpret the metrics in light of a project's needs"
- "automation and bot activity can influence the usefulness of several metrics in this model, in particular Time to First Response and Change Request Closure Ratio. These metrics are only applicable when these activities are primarily driven by humans, not automated responses."
- "Make sure to exclude responses from bots or other automated systems when measuring genuine community engagement." (Time to First Response page)
- "Release frequency is highly variable because software projects belong to different industries and fields, and no two projects have the same needs."
- "A lower Contributor Absence Factor indicates higher dependency on fewer contributors, posing a risk if these individuals leave."
- The only numeric guideline anywhere in the model is a case-study line from VMware: "Our internal guideline for projects is that every PR should receive a response from a human within two business days." One company's internal rule - cite it that way.

Not published, though often repeated as if it were: a target for the change request closure ratio (the page only says projects should "keep up with PRs and resolve them in a timely manner"), and any release-gap threshold.

## Activity

| Metric                          | Definition                                                                                                                                                                                | Formula                                                | Source of data                         |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------- |
| Active participants             | Distinct humans who posted, commented, committed or reviewed in the period                                                                                                                | count distinct non-bot identities after identity merge | venue analytics, forge API             |
| Non-staff share of activity     | Share of messages/answers not written by employees or maintainers                                                                                                                         | non-staff activity ÷ total activity                    | same, plus a staff account flag        |
| Channel/venue concentration     | Where the conversation actually lives                                                                                                                                                     | activity per channel, ranked                           | venue analytics                        |
| Collaboration platform activity | "The count of activities across digital collaboration platforms (e.g., GitHub, GitLab, Slack, email) used by a project", carrying timestamp, sender, bot flag, threaded/non-threaded type | count per platform per period                          | exports or a community-analytics stack |
| Burstiness                      | "How are short timeframes of intense activity, followed by a corresponding return to a typical pattern of activity, observed in a project?"                                               | deviation from the trailing baseline; volatility bands | any activity series                    |

Reading notes: raw message volume is not health - its documented use is finding the lowest-barrier channel and mapping where conversation lives. Named burst causes: releases, conferences, hackathons, critical bugs, media coverage, mentorship programs. Label the burst in the report so nobody reads it as growth.

## Responsiveness

| Metric                       | Definition                                                                                                                                              | Formula                                          | Source of data                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | -------------------------------- |
| Time to first response       | "The amount of time between when an activity was opened (e.g. Issue or Change Request) and when it received the first response from a human"            | median elapsed time, bots excluded               | forge API; venue export for chat |
| Unanswered rate              | Share of questions/threads that got zero human replies                                                                                                  | zero-reply threads ÷ total question threads      | forge API, venue export          |
| Change request closure ratio | "The ratio between the total number of open change requests during a time period versus the total number of change requests closed in that same period" | closed (merged + rejected) ÷ opened, same window | forge API                        |

Reading notes: the only attributable response-time figure is VMware's internal two-business-day guideline, quoted in the CHAOSS starter model - a reference point from one company, not a standard. Both metrics are meaningless with bots included.

A closure ratio persistently below 1 means the backlog outruns the team - that reading is this catalog's, not published guidance.

## Contributor funnel

| Metric                                | Definition                                                          | Formula                                             | Source of data                       |
| ------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------ |
| First-time participants               | People whose first activity falls in the period                     | count of identities with no prior activity          | forge API, git history, venue export |
| Second-contribution rate              | Share of first-time contributors who come back within 90 days       | returning ÷ first-time, per join cohort             | same                                 |
| Cohort retention                      | Share of a join cohort still active at day 30 / 90                  | active-at-N ÷ cohort size                           | same                                 |
| One-and-done rate                     | Share of all-time contributors with exactly one merged contribution | single-contribution contributors ÷ all contributors | git history                          |
| First-PR merge rate and time-to-merge | External contributors only, tracked separately from maintainers     | median per period                                   | forge API                            |

Reading notes: a high one-and-done rate is normal in open source. It is a finding only when it moves after a change you made. Maintainers' own PRs are always faster and will mask the number that matters if mixed in.

Cohort width is a decision, not a default. Monthly join cohorts are the usual starting point.

Weekly or daily cohorts in a community that gains a few dozen people a month produce single-digit groups whose retention curves are pure noise. Widen the window until each cohort has enough people to read, state the window next to the number, and keep it stable between reports - changing the window changes the trend.

## Concentration and risk

| Metric                     | Definition                                                                                                                        | Formula                                                                                                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Contributor absence factor | "The smallest number of people that make 50% of contributions"                                                                    | rank contributors by contribution count, count how many are needed to cross half the total                                                                              |
| Elephant factor            | "The minimum number of companies whose employees contribute a specified percentage of the total commits in a software repository" | same procedure grouped by employer; worked example: commit counts 1000/433/343/332/202/90/42/33 → 50% threshold is 1,237.5, reached by the top two companies → factor 2 |

Reading notes: higher is safer for both. An absence factor of 5 means the project survives several departures, while a factor of 1 is a single point of failure.

A low elephant factor means one or two employers effectively control the project. Neither accounts for knowledge distribution - two people with disjoint expertise are not interchangeable.

## Sentiment

| Metric              | Definition                                                                          | Collection                                                                                                                                                                |
| ------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recommendability    | "How likely is it that you would recommend this community/project to other people?" | Likert item, scored NPS-style (promoters minus detractors)                                                                                                                |
| Newcomer experience | "How well does an open source community attend to welcoming newcomers?"             | Likert items ("I feel welcome in the community", "The community treats new members well") plus open-ended obstacle questions; corroborated by whether first-timers return |
| Maintainer burnout  | Chronic-stress state: energy depletion, cynicism, reduced efficacy                  | Likert items on energy, workload, feeling heard, psychological safety; trace signals: sustained contribution then abrupt stop, contribution concentrated in a few people  |

The question bank, cadence, sampling rules and privacy limits live in the survey-instruments reference linked from SKILL.md.

## The starter set

When the user has no framework at all and the community is code-centric, start from the four-metric published minimum and add one sentiment item. Instrument them in this order - decisions bought per hour of collection, matching the pillar ranking in SKILL.md:

- efficiency: time to first response > change request closure ratio > contributor absence factor > release frequency > recommendability
- effort: time to first response == change request closure ratio == release frequency (one forge query each, near-zero) > contributor absence factor (needs an identity mapping first) > recommendability (a survey to field, half a year between readings)

The three-way effort tie is real: all three are single queries against the same API, and no ordering between them survives contact with a different forge. Recommendability sits last on efficiency and stays worth adding, because it is the only item on the list that can contradict the other four.

1. Time to first response (responsiveness)
2. Change request closure ratio (responsiveness/throughput)
3. Contributor absence factor (concentration)
4. Release frequency - count of releases including point releases. No published gap threshold exists ("highly variable... no two projects have the same needs"). What the source does flag is that delayed security releases leave users with no easy upgrade path. Meaningless for docs-only repositories.
5. Recommendability, asked twice a year (sentiment)

For a chat/forum community with no code, swap 2 and 4 for active participants and non-staff share of activity.

## Unsourced practitioner thresholds

These circulate widely in community-management material with no published evidence behind them. Use as starting hypotheses. Replace with the community's own trailing median after three periods, and label them as unsourced whenever you quote them.

| Metric                            | Commonly quoted "healthy" | Commonly quoted "act now" |
| --------------------------------- | ------------------------- | ------------------------- |
| Support response time             | under 24h                 | over 72h                  |
| Unanswered questions              | under 10%                 | over 25%                  |
| New-member 7-day retention        | over 40%                  | under 20%                 |
| Monthly active ratio              | over 20%                  | under 10%                 |
| Moderator/staff share of messages | under 30%                 | over 50%                  |

Commonly cited warning signs from the same material, which do hold up as qualitative flags:

- Most posts come from the company team.
- Questions sit unanswered past a day.
- The same five people account for most engagement.
- New members stop after their introduction.

## Sources

- CHAOSS, Starter Project Health metrics model - <https://chaoss.community/kb/metrics-model-starter-project-health/>
- CHAOSS, Time to First Response - <https://chaoss.community/kb/metric-time-to-first-response/>
- CHAOSS, Contributor Absence Factor - <https://chaoss.community/kb/metric-contributor-absence-factor/>
- CHAOSS, Release Frequency - <https://chaoss.community/kb/metric-release-frequency/>
- CHAOSS, Elephant Factor - <https://chaoss.community/kb/metric-elephant-factor/>
- CHAOSS, Burstiness - <https://chaoss.community/kb/metric-burstiness/>
- CHAOSS, Collaboration Platform Activity - <https://chaoss.community/kb/metric-collaboration-platform-activity/>
- CHAOSS, Newcomer Experience - <https://chaoss.community/kb/metric-newcomer-experience/>
- Jakob Nielsen, "Participation Inequality: The 90-9-1 Rule" (2006) - <https://www.nngroup.com/articles/participation-inequality/>
