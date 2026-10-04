# Survey instruments for community sentiment

Sentiment is the pillar most often faked with automated text scoring. The published instruments are surveys, corroborated by behavioural traces - ask people, then check whether their behaviour agrees.

## Contents

- [Pulse survey](#pulse-survey-quarterly)
- [Annual survey](#annual-survey)
- [Maintainer burnout check](#maintainer-burnout-check)
- [Lapsed-member question](#lapsed-member-question)
- [Sampling and response rates](#sampling-and-response-rates)
- [Confidence labels on qualitative findings](#confidence-labels-on-qualitative-findings)
- [Privacy limits](#privacy-limits)
- [Sources](#sources)

## Pulse survey (quarterly)

Two items. Anything longer will not be answered at a quarterly cadence.

1. "How likely is it that you would recommend this community/project to other people?" - Likert scale from "Not at all likely" through "Neutral" to "Extremely likely".
2. "What is the most frustrating thing about participating here?" - free text, optional.

Scoring item 1: split respondents into detractors, passives and promoters, then report **promoters % minus detractors %**. The published CHAOSS page writes the subtraction the other way round, which flips the sign. State the direction on every chart so a positive number always means "more promoters than detractors".

Corroborate the score with implicit signals from the same period - responsiveness and contribution-acceptance rates. A score that disagrees with behaviour usually means the survey reached a different population than the one doing the work.

## Annual survey

Add the newcomer and belonging items once a year, filtered to people who joined in the last 12 months:

- "I feel welcome in the community." (Likert)
- "The community treats new members well." (Likert)
- "What did you need when you arrived that you could not find?" (free text)
- "What stopped you from participating more?" (free text)

Cross-read against behaviour: do first-time participants return within 90 days? Agreement between the survey and the funnel is what makes either credible.

## Maintainer burnout check

Ask the small group carrying the load, separately and privately. Likert items on:

- energy and emotional drainage,
- fatigue and time away,
- thoughts of stepping back or leaving,
- workload versus capacity,
- whether their contribution feels valued,
- whether they can raise a concern safely.

Trace signals to watch beside the survey: sustained high contribution ending abruptly, contribution concentrated in very few people, expressed exhaustion or cynicism in public threads.

Burnout is the finding that activity metrics hide best - a community can post record numbers in the quarter its two maintainers decide to quit.

## Lapsed-member question

Send a one-question note to members who were active and then went silent for 60+ days: "You stopped participating a while back - what changed?" The people who left hold the answer to why, and they are systematically missing from every other instrument.

Keep it opt-out-friendly and send it once. A follow-up campaign to people who already left reads as pressure.

## Sampling and response rates

- Volunteer-community response rates are low. Below roughly 30 responses, treat the result as qualitative evidence with dates attached, not as a percentage.
- Report the response rate next to the score, always. A 68 built from 9 answers is a conversation starter, not a number.
- Keep the population definition stable between waves (e.g. "members active in the last 90 days"), otherwise the trend measures your sampling, not sentiment.
- Never mix a pulse wave sent to everyone with one sent to power users. Segment instead.

## Confidence labels on qualitative findings

Borrowed from customer-research practice, because a sentiment finding travels further than the sample behind it. Label every qualitative finding before presenting it:

| Label  | When                                                                                    |
| ------ | --------------------------------------------------------------------------------------- |
| High   | five or more independent people said it, across more than one channel or wave           |
| Medium | three to four independent people, or one strong wave with agreeing behavioural evidence |
| Low    | one or two people, or a single free-text field with no behavioural corroboration        |

Below roughly five independent data points on a theme, call it a hypothesis and name the cheapest way to test it. A single loud thread is not a community sentiment, and presenting it as one is how a community team ends up rebuilding something nobody else minded.

An adjacent instrument worth knowing but not adopting blind: the Sean Ellis product-market-fit item ("How would you feel if you could no longer use this?", with a 40% "very disappointed" line popularised by Superhuman). It measures product fit, not community health, and no community-specific validation of the 40% figure exists. If you adapt the wording to a community, say that it is adapted and drop the benchmark.

## Privacy limits

Published metric guidance repeats the same caution: using and disseminating health metrics can create privacy violations, with data-protection law and platform terms named as the exposure. In practice:

- Report sentiment in aggregate only. Never attribute a score to a named member.
- Keep survey responses separable from identity, and say so in the invitation - anonymity is what makes the burnout and lapsed-member instruments work at all.
- Check the venue's terms before bulk-exporting message content for any kind of analysis.

## Sources

- CHAOSS, Project Recommendability - <https://chaoss.community/kb/metric-project-recommendability/>
- CHAOSS, Project Burnout - <https://chaoss.community/kb/metric-project-burnout/>
- CHAOSS, Newcomer Experience - <https://chaoss.community/kb/metric-newcomer-experience/>
