# Readiness gates and critical-mass thresholds

Contents: gate checklist with evidence tests → verdict rules → day-30 leading indicators → published anchors → day-90 pass thresholds with their basis → measurement notes → sources.

## Table of Contents

- [Gate 1 - Demand](#gate-1-demand)
- [Gate 2 - Owner](#gate-2-owner)
- [Gate 3 - Purpose](#gate-3-purpose)
- [Gate 4 - Venue vacuum](#gate-4-venue-vacuum)
- [Gate 5 - Seed supply](#gate-5-seed-supply)
- [Verdict rules](#verdict-rules)
- [Day-30 leading indicators](#day-30-leading-indicators)
- [Published anchors](#published-anchors)
- [Day-90 pass thresholds](#day-90-pass-thresholds)
- [Measurement notes](#measurement-notes)
- [Sources](#sources)

## Gate 1 - Demand

The community makes peer conversation possible; it does not create the appetite for it. Accept as evidence:

- Repeat questions arriving privately (support inbox, DMs, maintainer email) that another user could have answered.
- Users answering each other unprompted in issues, threads, replies or a third-party space.
- A problem domain deep enough to sustain conversation. A product fully learnable from a quickstart generates no recurring discussion.
- A shared identity beyond the product - who members are or want to be. Rooms organized purely around a vendor's feature list run out of things to say.

Reject as evidence: competitor communities existing, a leadership request, a launch checklist item, "our users are technical so they'll want a Discord".

## Gate 2 - Owner

- One named person, not a team-in-principle, with weekly hours protected for the first 90 days _and_ a sustained figure for after them. The launch quarter is the cheap part; the standing presence is what the venue class is chosen against.
- The first phase is deliberately unscalable: answer every post, welcome every member by name, host the ritual. Budget hours for that, not for "monitoring".
- Record whether that person can be present most days or only in batches - it deletes venue classes outright rather than adjusting them.
- No named owner, or hours that depend on a future hire, fails the gate. Delay is cheaper than a public failure.

## Gate 3 - Purpose

Name the outcome with CMX's SPACES vocabulary, then state it as a measurable claim:

| Letter | Outcome                  | What the community is for                                                                             |
| ------ | ------------------------ | ----------------------------------------------------------------------------------------------------- |
| S      | Support                  | members answer each other, cutting support cost and raising satisfaction                              |
| P      | Product                  | members' ideas and feedback drive product decisions                                                   |
| A      | Acquisition and advocacy | a network of ambassadors drives awareness and growth                                                  |
| C      | Content and contribution | members contribute content that becomes part of the product or its assets                             |
| E      | Engagement               | people gather around a common interest related to the product; internally, employees/partners/vendors |
| S      | Success                  | adoption and customer lifetime value rise through best-practice sharing and upskilling                |

CMX's own rule for a new community: "If you're starting out, just focus on one objective from the SPACES Model. Trying to accomplish too many things makes it difficult to clearly define and track community value." Source: <https://cmxhub.com/the-spaces-model/>.

Examples of the measurable claim:

- "cut repeat setup tickets by a third within two quarters"
- "get 10 usable roadmap signals per month"
- "convert 5 power users into contributors this year"

Secondary outcomes are fine, unranked outcomes are not: the primary outcome decides the community model, the venue and the thresholds.

## Gate 4 - Venue vacuum

Search for where the audience already gathers, then ask, for each, whether the outcome could be reached by showing up there instead:

- Ecosystem chats
- Subreddits
- Q&A sites
- Language communities
- An existing user group

Owning a space buys control, archive and member data; joining one costs no seeding and no moderation staffing. Fail this gate when an existing space already serves the outcome - the recommendation is to participate, not to launch.

FeverBee frames the same test as an ecosystem-maturity question: map whether an ecosystem already serves the need before building a new community on top of it. Source: Richard Millington, "Your Ecosystem's Maturity Should Guide Your Big Community Decisions," FeverBee, <https://www.feverbee.com/ecosystemmaturityindex/>; "We Need A New Playbook For Building Brand Communities," FeverBee, 2 September 2024, <https://www.feverbee.com/newplaybook/>. CNCF enforces a narrower, operational version of the same rule: Kubernetes project Slack channels exist "to organize an existing community, not seed new ones." Source: "Slack Guidelines," kubernetes.dev, <https://www.kubernetes.dev/docs/comms/slack/>.

## Gate 5 - Seed supply

- At least 20 people the team can invite **by name** this month, ideally 20-50.
- Coverage matters more than count: one reliable answerer per topic area, two or more time zones for a global audience.
- Founding members should already behave like contributors or advocates. A cohort of passive newcomers produces silence.

## Verdict rules

| Gates passed              | Verdict                                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 5                         | Launch. Proceed to venue choice and seeding.                                                                                      |
| 4 with written mitigation | Launch on a delayed date, gated on the mitigation landing - not on the calendar.                                                  |
| ≤ 3                       | Do not launch. Recommend the alternative that returns the most per standing hour, plus the evidence to collect for a re-decision. |

The alternatives and their ranking live in the skill body - one ordering, by evidence bought per hour of standing presence, not by cost. Do not re-derive a second order here.

## Day-30 leading indicators

Too early for ratios, so watch behavior instead:

- Any post authored by someone outside the founding cohort.
- Any question answered by a member rather than the team.
- The ritual running on schedule, at least twice, with attendance above the organizer.
- Median first-response time under a few hours during working hours.

Zero member-authored answers at day 30 predicts a failed day-90 gate; act then, not later.

## Published anchors

Three published findings anchor this area. Frame the target with them before quoting any percentage.

| Finding                                                                                                                                                                                 | Source                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| ~90% of members never post, 9% contribute occasionally, 1% produce most contributions (90-9-1). Lurking is the baseline, not a defect; a _change_ in the ratio is the news.             | Jakob Nielsen, NN/g, 8 October 2006, <https://www.nngroup.com/articles/participation-inequality/> |
| Contributors who received a review within 48 hours returned and contributed again at a much higher rate; "it only takes one negative experience to make someone not want to come back". | Mozilla study cited in GitHub Open Source Guides, <https://opensource.guide/building-community/>  |
| Recurring activity, not cumulative membership, marks a group alive: inactive after >90 days without an event; active requires a quarterly event with more than 10 _attendees_.          | CNCF community group rules, <https://github.com/cncf/communitygroups>                             |

Read every measurement against a trailing baseline rather than the launch month. CHAOSS's burstiness metric exists because releases, conferences and media coverage produce spikes that decay; comparing a quiet month against a launch spike is the most common false trend in community reporting. <https://chaoss.community/kb/metric-burstiness/>

## Day-90 pass thresholds

The metric _definitions_ below are sound and reusable. The cutoff values are adapted from practitioner baseline practices. Present them as a starting hypothesis to recalibrate against the community's own trailing data as soon as one exists, not as an unchangeable standard.

| Signal                                | Pass  | Warning | Failing | Where the numbers come from                                                                                                      |
| ------------------------------------- | ----- | ------- | ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Questions answered within 24h         | > 90% | 75-90%  | < 75%   | `community-building` ("unanswered questions" <10%/10-25%/>25%), consistent with `community-marketing`'s ">24 hours" warning sign |
| Share of posts written by non-staff   | > 50% | 30-50%  | < 30%   | inverse of `community-building`'s moderator-message share (<30%/30-50%/>50%); the >50% pass is set here                          |
| New members posting within 7 days     | > 40% | 20-40%  | < 20%   | `community-building`, adopted as published                                                                                       |
| Monthly active / total members        | > 20% | 10-20%  | < 10%   | `community-building`; `community-marketing` states the same 20% DAU/MAU bar                                                      |
| Threads with ≥ 1 reply                | > 80% | 60-80%  | < 60%   | metric named by `community-marketing`, thresholds set here                                                                       |
| Engagement share of the top 5 members | < 50% | 50-80%  | > 80%   | the >80% failing band is `community-marketing`'s warning sign; the <50% pass is set here                                         |

Reading the results:

- Two or more failing signals → re-run the shape and seeding steps on the specific failure, or trigger the fold-back. More promotion into a silent room lowers every ratio.
- High answer rate with a low non-staff share means the team is doing the community's job; the room is a support channel wearing a community's name.
- High activity concentrated in the top 5 members is fragile: those five leaving takes the community with them.
- Adjust thresholds for a deliberately small, high-value B2B room - a 40-member customer community can pass on absolute counts (every question answered, five distinct members posting weekly) while missing percentage bars. State the adjustment and its reasoning in the brief.

## Measurement notes

- Prefer the venue's native analytics; where they are thin, sample manually for one week per month rather than building instrumentation the owner cannot maintain.
- Count staff by role, not by badge: a paid contractor answering support is staff.
- Track joins and leaves separately; net member count hides churn.
- Report the count of active members alongside every ratio. With a ~90% lurker baseline, a percentage moves as fast when members leave as when activity grows.

## Sources

- GitHub Open Source Guides, "Building community" and "Finding users" - public-place-to-talk principle, 48-hour responsiveness evidence (Mozilla study), one-negative-experience warning. <https://opensource.guide/building-community/>, <https://opensource.guide/finding-users/>
- Jakob Nielsen, "Participation Inequality" (NN/g, 2006) for the 90-9-1 baseline. <https://www.nngroup.com/articles/participation-inequality/>
- CMX, "The SPACES Model" for the outcome vocabulary and the one-objective rule. <https://cmxhub.com/the-spaces-model/>
- CHAOSS burstiness metric for the spike-versus-trend caveat. <https://chaoss.community/kb/metric-burstiness/>
- CNCF community group rules for the activity floor. <https://github.com/cncf/communitygroups>
- Orbit Model for member-level vocabulary. <https://orbit-model.joshed.io/>
- FeverBee, "Your Ecosystem's Maturity Should Guide Your Big Community Decisions" and "We Need A New Playbook For Building Brand Communities" for the venue-vacuum test. <https://www.feverbee.com/ecosystemmaturityindex/>, <https://www.feverbee.com/newplaybook/>
- CNCF, "Slack Guidelines" for the operational venue-vacuum rule governing Kubernetes project Slack channels. <https://www.kubernetes.dev/docs/comms/slack/>
