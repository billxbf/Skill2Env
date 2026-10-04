# Measurement and kill rules

Measure on four levels - reaction, learning, behavior, results (Kirkpatrick, 1954; popularized 1959 and 1994). The documented failure mode is that trainers stop at levels 1-2: satisfaction scores and quiz results, reported as impact. Design from level 4 backwards, the same order backward design imposes on the curriculum.

Phillips adds a level 5, ROI (benefit vs. cost). Kaufman argues ROI belongs at level 4 and level 5 should measure client/societal impact. Pick one convention, say which, and stop debating it.

Kirkpatrick Partners' own definitions are worth quoting verbatim when someone argues the levels mean something else - level 3 in particular is not "did they like it later":

- Reaction - "the degree to which the target audience finds an experience or initiative favorable, engaging, relevant, and supportive of the work needed to achieve the targeted outcomes."
- Learning - "the degree to which the target audience acquires the intended knowledge, skills, attitude, confidence, and commitment."
- Behavior - "the degree to which the target audience performs the critical behaviors in its environment **and is supported in and accountable for its performance**."
- Results - "the degree to which targeted organizational outcomes occur as a result of an experience or initiative and performance support."

The same source states it is "critical to start with Level 4: Results, and understanding the 'Why' and the purpose of the program". Design the measurement plan in that direction, and note what level 3's wording obliges you to build: a program that teaches a behaviour nobody at the learner's employer supports or rewards will not show a level-3 movement, and that is not a curriculum defect.

## The four levels in developer education terms

| Level    | What it answers               | Developer education signal                                                                                                                  |
| -------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Reaction | Did they find it relevant     | Course rating, completion rate, drop-off point per module                                                                                   |
| Learning | Did they acquire the skill    | Lab pass rate, exam pass rate, item-level failure clusters                                                                                  |
| Behavior | Do they apply it at work      | Post-course product usage: features adopted, API calls, projects created, support tickets avoided                                           |
| Results  | Did the business outcome move | Account expansion, time-to-competence for new hires at customers, partner-delivered implementation quality, hiring-market credential demand |

Levels 3-4 require joining learner identity to product usage. Decide that plumbing **before** launch - it cannot be reconstructed after the first cohort has already learned anonymously.

## Metric set per tier

Pick one primary metric per level per tier. More than one primary metric per level means none of them is primary.

| Tier                  | Reaction                                           | Learning                                                        | Behavior                                                        | Results                                                                                                  |
| --------------------- | -------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Curated learning path | Path completion rate                               | Self-reported confidence, or a single end-of-path check         | Feature adoption among path finishers vs. matched non-finishers | Time-to-first-production-use                                                                             |
| Curriculum with labs  | Per-module drop-off                                | Lab pass rate and failure clusters                              | Depth of product usage 30/90 days after completion              | Support ticket rate per active account, onboarding duration                                              |
| Badge                 | Issuance rate vs. starts                           | Graded-task pass rate                                           | Usage delta for badge holders' accounts                         | Named external consumption: buyers or partners citing the badge                                          |
| Certification         | Candidate satisfaction, exam experience complaints | Pass rate, per-domain score distribution, item exposure signals | Implementation quality of certified staff, escalation rate      | Certified-head counts in contracts, deal cycles unblocked, renewal rate of accounts with certified staff |

## Baselines and honest expectations

Everything in this section is reasoning to argue with, and every target below is one you set - completion rate, lab pass rate and any certified-heads-to-renewal ratio included. Say that out loud when reporting, or the first number you publish becomes the standard you are held to.

- Completion rates for free, ungated, self-paced developer content are low by nature. Treat completion as a diagnostic of module sequencing, not as an outcome.
- A pass rate near 100% means the assessment is not assessing. A pass rate collapsing near zero usually means the lab environment broke, not that learners got worse - check the environment before the curriculum.
- First-cohort numbers are a baseline, not a verdict. Set the target for cohort two, and say so when reporting cohort one.
- No major vendor certification program publishes a pass rate to benchmark against. AWS's own certification FAQ states it directly: "AWS Certification passing scores are set by using statistical analysis and are subject to change. AWS does not publish exam passing scores because exam questions and passing scores are updated to reflect changes in test forms as the content is updated." Microsoft, Cisco and CompTIA withhold the same figure without stating a reason. A first cohort's pass rate has no published number to sit next to - that is a limit on comparison, not evidence the assessment is wrong.

## Attribution limits - state them before anyone asks

- Education rarely holds a clean counterfactual. Learners who opt in are already more committed than those who do not, so raw before/after comparisons overstate the effect.
- Use matched comparison groups (similar accounts, similar tenure, no course) rather than the whole non-learner population.
- Never claim revenue caused by a course. Claim the observable link - "accounts with at least one certified engineer renewed at X% vs. Y% for matched accounts without" - and label it as correlation.
- Multi-touch attribution collapses when education sits mid-funnel behind docs and community. Report education's contribution as a named influence on a specific stage, not as sourced pipeline.
- Say which of the four levels you cannot measure this year, and why. An unmeasured level named in advance is credible; one discovered at review is not.

## Kill rules

Write the kill rule before launch, as a number and a date. A program without one survives on sunk cost.

Each kill rule needs:

- The metric.
- The threshold.
- The review date.
- The action if the threshold is missed.

Per tier:

- **Path or module**: fewer than N starts per month over two consecutive quarters → retire the path, keep the underlying artefacts.
- **Curriculum**: behavior metric shows no difference between completers and matched non-completers after two cohorts → stop authoring, keep what exists on maintenance only.
- **Badge**: no external consumer cites it within two quarters of launch → stop issuing, honor existing badges to their stated expiry.
- **Certification**: candidate volume below the number that funds one exam re-alignment cycle → announce sunset, run a final window, honor validity windows already promised.
- **Any tier**: the named owner leaves and is not replaced within one release cycle → freeze the program rather than let it drift out of date.

## Retirement mechanics

Retiring well is part of the program design, not an admission of failure.

1. Announce the end date before the last enrolment, never after.
2. Honor every credential already issued to its published validity window - revoking retroactively destroys trust in every future credential.
3. Keep content readable at a stable URL with a dated "no longer maintained" banner, or redirect to the replacement.
4. Move anything still true into docs, so the knowledge survives the program.
5. Record the reason for retirement next to the original charter, so the same program is not proposed again in eighteen months with the same evidence.
