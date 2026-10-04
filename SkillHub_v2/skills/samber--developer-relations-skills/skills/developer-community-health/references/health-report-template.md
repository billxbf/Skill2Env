# Community health report

## Contents

- [Template](#template)
- [Worked example](#worked-example)
- [Negative example](#negative-example)

## Template

```markdown
# Community health - {community name} - {period}

## Primary outcome

{The one thing this community exists to produce, in one sentence.}

## Metric sheet

| Metric | Pillar | Definition / formula | Source | Baseline | Threshold (origin) | Owner | Action if breached |
| ------ | ------ | -------------------- | ------ | -------- | ------------------ | ----- | ------------------ |

## Reading - {period}

| Metric | This period | Baseline | Direction | Note |
| ------ | ----------- | -------- | --------- | ---- |

## Findings

1. {Finding} - evidence: {numbers, dates, links}. Confidence: {high/medium/low, and why}.

## Actions

| Action | Owner | By when | Metric it should move |
| ------ | ----- | ------- | --------------------- |

## Watch list

{Metrics still baselining, known instrumentation gaps, events that distorted the period.}

## Next review

{Date, and what will be re-checked first.}
```

## Worked example

Illustrative numbers for an open-source project with a Discourse forum, at monthly cadence.

```markdown
# Community health - Acme Toolkit - August 2026

## Primary outcome

Peer support: users answer each other's usage questions, so the two maintainers spend their hours on code.

## Metric sheet

| Metric                                      | Pillar         | Definition / formula                                | Source                    | Baseline            | Threshold (origin)                                                     | Owner | Action if breached                                 |
| ------------------------------------------- | -------------- | --------------------------------------------------- | ------------------------- | ------------------- | ---------------------------------------------------------------------- | ----- | -------------------------------------------------- |
| Median time to first human response (forum) | Responsiveness | Question post → first non-bot reply                 | forum export              | 9h (Apr-Jun median) | > 24h for two months (folklore cutoff, unsourced - recalibrate in Nov) | Priya | Recruit 2 answerers in the APAC timezone           |
| Zero-reply question rate                    | Responsiveness | Question threads with no human reply within 7 days  | forum export              | 12%                 | > 20% (self-set, ~1.7x baseline)                                       | Priya | Weekly sweep of unanswered threads                 |
| Non-maintainer share of answers             | Activity       | Answers not written by the 2 maintainers            | forum export + staff flag | 46%                 | < 35% (self-set, ~0.75x baseline)                                      | Priya | Recognise top answerers; stop answering first      |
| Active participants                         | Activity       | Distinct non-bot people posting in the month        | forum export              | 74                  | < 50 (self-set, ~0.7x baseline)                                        | Priya | Diagnose before acting; check for event distortion |
| First-time posters returning within 90 days | Funnel         | Second post by a first-time poster, per join cohort | forum export              | 22%                 | < 15% (self-set, ~0.7x baseline)                                       | Sam   | Review first-answer time for newcomers             |
| Contributor absence factor                  | Concentration  | Smallest number of people producing 50% of commits  | git history               | 2                   | 1 (single point of failure)                                            | Sam   | Open the reviewer rung to the top 3 contributors   |
| Recommendability                            | Sentiment      | "Would you recommend this project?", NPS-style      | quarterly pulse           | +21 (n=38)          | drop > 15 points (self-set)                                            | Sam   | Interview 5 detractors                             |

## Reading - August 2026

| Metric                          | This period  | Baseline | Direction | Note                                              |
| ------------------------------- | ------------ | -------- | --------- | ------------------------------------------------- |
| Median time to first response   | 31h          | 9h       | worse     | Both maintainers were at a conference 8-15 Aug    |
| Zero-reply question rate        | 24%          | 12%      | worse     | Concentrated in the same two weeks                |
| Non-maintainer share of answers | 51%          | 46%      | better    | Two new regulars answered 14 threads between them |
| Active participants             | 96           | 74       | up        | Release 3.0 landed 6 Aug - burst, not trend       |
| First-time posters returning    | 19%          | 22%      | flat      | n=31 first-timers; within noise                   |
| Contributor absence factor      | 2            | 2        | flat      | -                                                 |
| Recommendability                | not surveyed | +21      | -         | Next pulse: September                             |

## Findings

1. Responsiveness degraded for exactly one two-week window while both maintainers were away - evidence: 31h median overall, 11h median outside 8-15 Aug. Confidence: high, the split is clean. This is a coverage gap, not a decline.
2. Two new regulars now answer without being asked - evidence: non-maintainer answer share up 5 points, 14 threads. Confidence: medium, one month of data.
3. The August participant spike is release-driven - evidence: 62% of new posts reference 3.0, spike starts the day after release. Confidence: high. Do not carry it into the trend line.

## Actions

| Action                                                                       | Owner | By when   | Metric it should move                   |
| ---------------------------------------------------------------------------- | ----- | --------- | --------------------------------------- |
| Ask the two new regulars to hold answer duty during maintainer absences      | Priya | 12 Sep    | Zero-reply rate, time to first response |
| Publish an "away" banner with expected response time before the next absence | Priya | Next trip | Newcomer experience                     |
| Open the reviewer rung and invite the top 3 contributors                     | Sam   | 30 Sep    | Contributor absence factor              |

## Watch list

Newcomer-experience survey items still unasked (first wave in September). Chat venue not instrumented - no export on the current plan, so chat activity stays anecdotal.

## Next review

28 September 2026 - re-check time to first response outside travel windows, and whether the two new regulars stayed.
```

What makes this report work:

- Every number is read against the community's own baseline.
- Each threshold carries its origin, so nobody mistakes a working convention for a standard.
- The burst is labeled instead of celebrated.
- The small-N cohort is called out as noise.
- Every finding ends in an owned action.

## Negative example

```markdown
# Community Health Dashboard - Q3

- Total members: 4,812 (+312 this quarter) ↑
- Messages sent: 18,204 (+9%) ↑
- Discord sentiment: 78% positive (auto-analysis)
- Engagement rate: 12%
- Top contributors: @dev_alice (412 msgs), @bob_builds (388 msgs), @carol_hacks (301 msgs)

Overall: community is healthy and growing. Recommend continued investment.
```

Why it fails:

- Total members and message counts only go up. Neither can detect a community going quiet where it matters.
- No baseline, no period comparison, no note that a launch or event happened in the quarter.
- "Engagement rate" is undefined - nobody can recompute it or tell what would move it.
- Automated sentiment on developer chat scores blunt bug reports as negative and jokes as positive. There is no survey behind the 78%.
- A public per-member message leaderboard rewards volume and creates privacy exposure.
- No responsiveness metric at all: 18,204 messages are compatible with every single question going unanswered.
- No owner, no threshold, no action - the report cannot be wrong, so it cannot be useful.
