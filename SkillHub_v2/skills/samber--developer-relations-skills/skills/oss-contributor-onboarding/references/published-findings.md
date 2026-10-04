# Published findings on contributor onboarding

Published figures on newcomer onboarding with their methodological caveats, plus the baselines this skill sets itself. Read this before quoting any figure to a maintainer.

## 1. Published figures

| Claim used in the skill                                                                                                                                 | Source                                                                                                                                                                  | Caveat                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Contributors reviewed within 48 hours return at a much higher rate; "it only takes one negative experience to make someone not want to come back"       | GitHub Open Source Guides, <https://opensource.guide/building-community/>                                                                                               | Practitioner guidance, no published dataset behind the 48-hour figure           |
| Newcomer barriers fall into five categories: social interaction, prior knowledge, finding a way to start, documentation, technical hurdles              | Steinmacher et al., _A systematic literature review on the barriers faced by newcomers to open source software projects_, Information and Software Technology 59 (2015) | Literature review over 20 primary studies, not a measurement of any one project |
| Newcomers choose issues labelled by the API domain required more often than by architecture area                                                        | Steinmacher et al., arXiv:2103.12653                                                                                                                                    | 74 participants, single study                                                   |
| `good first issue` means members committed to extra assistance; `help wanted` is the broader signal                                                     | <https://www.kubernetes.dev/docs/guide/first-contribution/>                                                                                                             | Project-specific convention, widely copied                                      |
| GitHub surfaces the `good first issue` label algorithmically and publishes no criteria for it                                                           | <https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/encouraging-helpful-contributions-to-your-project-with-labels>                | -                                                                               |
| "The hard part of getting into open source for the first time isn't the implementation of a feature, but figuring out how to actually contribute code." | Kent C. Dodds, _First Timers Only_, <https://kentcdodds.com/blog/first-timers-only>                                                                                     | Opinion piece that launched the `first-timers-only` label convention            |
| CNCF "encourage[s] projects to use DCO as it's easier to setup and use"                                                                                 | <https://github.com/cncf/foundation/issues/130>                                                                                                                         | Foundation policy, not a measured friction study                                |
| A CLA "creates friction for new contributors: someone who wants to fix a typo must first complete a signing workflow"                                   | <https://tenthirtyam.org/dispatches/2026/04/08/dco-vs-cla-managing-contribution-agreements-in-open-source/>                                                             | Practitioner post                                                               |

## 2. Self-set baselines

The following numbers are self-set defaults, not published standards. State them as such when a maintainer asks where they come from, and let a project override any of them with a reason.

- The scorecard's pass mark (all four blocking checks, plus 12 of 16 scored points).
- A standing stock of at least three valid unclaimed beginner issues.
- Sizing a first issue at roughly one evening of work, setup included.
- The 15-minute ceiling for a stranger locating the file to change during the task-path cold run.
- A quarterly re-audit cadence.
- The 90-day window used for "second-contribution rate".

Two thresholds used alongside them are published rather than self-set: the 48-hour review window comes from the Open Source Guides, and the CHAOSS metric definitions (time to first response, contributor absence factor, new contributors) come from the CHAOSS project.

## 3. Structured mentorship programs

A maintainer can host a newcomer cohort instead of building one. Program terms as each program publishes them:

| Program               | Stipend                                    | Duration                          | Eligibility                                       | Published outcome                                                                                                                   |
| --------------------- | ------------------------------------------ | --------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Google Summer of Code | $750–$6,600, purchasing-power adjusted     | 8–22 weeks (12 standard)          | 18+, any newcomer since 2022                      | 63.5% of 2,456 studied participants opened a PR to the same project after the program; 85.74% of GSoC PRs merged (arXiv:2412.13120) |
| Outreachy             | $7,000 flat                                | 3 months                          | People facing underrepresentation or bias in tech | 80% still contributing (2019 alum survey, 37% response rate)                                                                        |
| LFX Mentorship        | $1,000–$6,600, purchasing-power adjusted   | 12 weeks full-time / 24 part-time | Varies, often first-timers                        | 270+ graduates since 2019                                                                                                           |
| MLH Fellowship        | up to $5,000, need-based                   | 12 weeks                          | Students, graduates, non-traditional              | Not published; pods of 8–10 with a mentor                                                                                           |
| Season of Docs        | $5,000–$15,000 granted to the organization | 3–5 months                        | Organizations apply and hire the writer           | Per-project case studies                                                                                                            |

Sources: developers.google.com/open-source/gsoc, outreachy.org, docs.linuxfoundation.org/lfx/mentorship, developers.google.com/season-of-docs.

**The counter-case.** Hacktoberfest rewarded pull-request volume with a T-shirt and produced a 2020 spam wave severe enough that DigitalOcean made participation opt-in per repository, shortened the grace period, banned repeat spammers and dropped the T-shirt entirely in 2023 (<https://developerrelations.com/case-studies/overcoming-hacktoberfest-spam/>). An extrinsic reward with no quality gate buys volume, and volume is not what a thin review queue needs.

## 4. Whether programs work at all

The two most-cited studies disagree, and neither used a matched control group:

- The GSoC PR study (arXiv:2412.13120) found 63.5% post-program continuation.
- Labuschagne & Holmes, _Do Onboarding Programs Work? A Multi-Level Empirical Analysis of the Effect on Mozilla Contributor Activity_ (MSR 2015, DOI 10.1109/MSR.2015.49), found the opposite direction: "developers whose initial contribution is on a GFB [good-first-bug] or mentored bug are less likely to become long-term contributors", concluding "these programs alone do not automatically improve the odds."
- Silva et al. (arXiv:1910.05798, 141 students / 53 mentors) add the motivational reading: "students enter GSoC for an enriching experience, not necessarily to become frequent contributors."

Treat "an onboarding program improves retention" as unproven in the general case. Prefer a process metric the project can measure on its own funnel (time to first response, second-contribution rate) over importing another project's self-reported outcome. Say this out loud to a maintainer who wants to buy a program instead of fixing the path.

## 5. Bias in first-PR acceptance

Terrell et al., _Gender differences and bias in open source: pull request acceptance of women versus men_ (PeerJ Computer Science 3:e111, 2017, DOI 10.7717/peerj-cs.111), analysed 3,064,667 pull requests and linked 35.3% of users to a gender.

- Overall, women's PRs merged at a higher rate than men's: 78.7% vs 74.6%.
- Restricted to **outside contributors with an identifiable gender**, women dropped to 58% vs men's 61%, while contributors whose profiles were gender-neutral had the highest rate of all (70% women, 65% men).
- Authors' conclusion: "although women on GitHub may be more competent overall, bias against them exists nonetheless."
- Caveat: gender was inferred from name and Google+ profile linkage, only 35.3% of users were linkable, and the study predates many platform changes. The direction is robust; the exact percentages are not.

Related: Steinmacher et al. (arXiv:2301.10912) used GenderMag to find cognitive-style barriers in GitHub's own interface and measured improved task performance and self-efficacy after redesign, mainly for people with cognitive styles more common among women. Information-foraging cost - having to hunt for the process - is not distributed evenly across newcomers.

Reach-focused initiatives are measured differently again: Django Girls reports 1,137 workshops in 593 cities reaching 24,500+ women by 2024, with 71.2% of surveyed alums continuing to learn to code and 44.7% starting work in tech - self-reported, subset response (<https://www.djangoproject.com/foundation/reports/2024/>).

## 6. Cloud development environments

Devcontainer-based cloud workspaces (Codespaces, Gitpod, DevPod, Coder) are the strongest available fix for "setup takes a week", but every published time saving is vendor-reported: prebuilds cutting startup "from 3-5 minutes to 10-30 seconds", onboarding "from one to two weeks down to near-instant". Treat those numbers as marketing figures, not measurements.

Three constraints to raise before recommending one:

- **Who pays for compute.** Free personal allotments are small, and storage bills even while a workspace is stopped. Without an org-billed plan or a sponsor, the free tier caps how much a newcomer can experiment.
- **Portability before hosting.** `.devcontainer/` is shared across VS Code Dev Containers, Codespaces and DevPod; the vendor is not. Adopt the config first, the host second. Gitpod dropping its self-hosted option in 2024 is the cautionary case for hard-coding a vendor's terms into contributor docs.
- **Drift.** A cloud environment maintainers never use bit-rots. Make the devcontainer the canonical environment for everyone, and keep local setup a first-class path for contributors with poor connectivity to the vendor's regions.

## 7. Onboarding events and sprints

- PyCon US runs up to four days of post-conference sprints, free with registration, preceded by a ~3-hour "Introduction to Sprinting" workshop covering git, virtual environments and pull requests.
- pyOpenSci's sprint handbook (<https://www.pyopensci.org/handbook/community/events/sprints.html>) prescribes the operational spine:
  - pre-tag `sprintable` issues before the event
  - track output on a per-event board
  - count issues closed and PRs merged
  - follow up with attendees afterwards
- Kubernetes ran the most resourced program in the field - a ~5-hour New Contributor Workshop with a dedicated contributor-playground repository - and then stopped: "running the session during the summit never led to any people who weren't already contributing to the project becoming dedicated contributors" (<https://kubernetes.io/blog/2023/11/03/k8s-contributor-summit-behind-the-scenes/>). It was replaced in September 2024 by a monthly online New Contributor Orientation, overview-only.
