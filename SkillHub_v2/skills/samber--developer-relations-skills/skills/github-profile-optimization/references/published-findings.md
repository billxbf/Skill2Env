# Published findings on profile work

What is known about whether profile work pays off, which figures are published and which are self-set, and which claims to refuse. Read this before quoting any figure to a user, and before promising a result.

## Contents

- Published claims and their sources
- Self-set baselines (not industry standards)
- Claims to refuse
- Audience divergence
- Practitioner voices
- Why no named framework appears

## Published claims and their sources

| Claim                                                                                                                                                                                                                 | Source                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Activity traces read as "more reliable and verifiable than a static list of individuals' skills", but only when cheap to verify; the strongest signals are activity history and work on high-status projects          | Marlow & Dabbish, CSCW 2013 (predates profile READMEs entirely)                                                                            |
| Platform activity is only a _partial_ proxy for expertise: high feature values correlate with expertise, but "the proxy fails in the case of developers with low feature values, who can be both experts and novices" | Montandon et al., MSR 2019, tested on 575 developers across three large projects                                                           |
| 81% of hiring managers use resumes as the first screening step; small companies weight portfolios more than large ones (80% vs 66%); C-level respondents valued public projects above years of experience             | HackerRank 2018 Developer Skills Report (39,000+ developers, 7,000+ employers); the only figure in this space with a disclosed methodology |
| ~6.0 million suspected fake stars across 18,617 repositories running star campaigns, detected over 20TB of public event data (July 2019 – December 2024)                                                              | He et al., "Six Million (Suspected) Fake Stars on GitHub", arXiv:2412.13459, ICSE '26                                                      |
| Star growth is driven by promotion, not quality; stars measure attention and reach                                                                                                                                    | Borges & Valente, _Journal of Systems and Software_, 2018                                                                                  |
| Profile READMEs launched July 2020, quietly; the practice grew out of hobbyist curation lists formed within days, not out of a professional discipline                                                                | Simon Willison's dated post (10 July 2020) and the curation repositories that followed it                                                  |
| Public-code filters exclude contractors under NDA, people who cannot publish for licensing or security reasons, and compound an existing time-privilege gap                                                           | Ashe Dryden, "The Ethics of Unpaid Labor and the OSS Community"                                                                            |
| "GitHub is all the public work you've ever done, unordered, unfiltered and unexplained. It tells no story and provides no context"                                                                                    | James Coglan, 2013                                                                                                                         |
| Measurement is the top unsolved problem in the field (67.3% naming it), and profile-level measurement is not even a tracked category                                                                                  | 10th Annual State of Developer Relations Report                                                                                            |

Two absences matter as much as the published claims:

- No peer-reviewed study measures whether profile changes affect callback rates, and the audit study that would settle it has never been run, so never promise a hiring outcome from profile work.
- No host offers profile-level analytics: repository traffic exists, is limited to 14 trailing days, and requires push access to that specific repository.

## Self-set baselines (not industry standards)

Present these as working defaults, revisable by the owner. Never present them as a published standard.

| Baseline               | Value                               | Why this number                                                                      |
| ---------------------- | ----------------------------------- | ------------------------------------------------------------------------------------ |
| Scored pass mark       | 13 of 16                            | Leaves room for one weak area without letting two through                            |
| Blocking checks        | 4, all must pass                    | Each one is a failure a visitor notices in the first screen                          |
| Cold-reader window     | 45 seconds                          | Approximates a scan, not a read                                                      |
| Cold-reader pass       | 4 of 4 (5 of 5 for an organization) | A profile that answers three of four still misroutes a quarter of visitors           |
| Decoration cap         | 3 visual elements                   | Each third-party image is a dependency that can freeze in the image proxy            |
| Pin count to fill      | All 6                               | The platform's own limit, and the fallback ordering is worse than any deliberate one |
| Positioning candidates | 3                                   | Enough to escape the first phrasing, few enough to decide in one pass                |

## Claims to refuse

- "60-80% of recruiters check GitHub." Vendor-blog figures citing unnamed "industry surveys" with no traceable methodology. Do not repeat them, even hedged.
- Any promise that a profile rewrite produces interviews, stars, contributors or signups. No study measures this effect in either direction.
- A view-counter badge as evidence anything worked: it increments on every image load through the anonymizing proxy, counting bots and repeat loads, and public scripts inflate it trivially.
- A dense contribution graph as evidence of skill. Backdating a commit is one environment variable, and public tools paint arbitrary shapes into the graph.
- Any specific achievement threshold as durable; achievements are a public preview and the tiers change without notice.

## Audience divergence

The same tactic is a plus for one reader and a cost for another, which is why the skill asks who the profile is for before it advises anything.

| Constituency          | Goal                   | Optimizes                                                     | Where advice conflicts                                                              |
| --------------------- | ---------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Maintainers           | Adoption, contributors | Repository READMEs, contribution guides, organization profile | Reject star-chasing; want real adoption evidence                                    |
| Companies             | Awareness, funnel      | Organization README, pins, verified badge                     | Have an investor-optics incentive to care about stars while knowing they are vanity |
| Job-seeking engineers | Get hired              | Personal README, pinned original work, activity               | Told to optimize a surface many reviewers never open                                |

The sharpest conflict: maintainer culture reads streak and trophy widgets as noise, while job-seeker advice promotes them. A profile that impresses an early-career peer group can cost credibility with a senior reviewer.

Staged guidance that follows from this:

- **Job seekers, stage 1**: treat the profile as a verification surface, not a discovery surface. Make the resume and a searchable professional profile strong first, then make sure the code host does not contradict them.
- **Job seekers, stage 2**: invest deeper only when the target is small, founder-led, or infrastructure/open-source heavy, where the portfolio genuinely carries weight. Then pin three to six original repositories, enable anonymized private-contribution counts, and skip decorative widgets.
- **Companies, stage 1**: assign ownership before content. The organization profile is a governed brand asset; only organization owners can set pins.
- **Companies, stage 2**: refuse the vanity trade. Never buy stars or tolerate farming; publish adoption evidence (named users, downloads, release cadence) instead. If investors ask for stars, contextualize them next to adoption data rather than optimizing them.
- **Maintainers**: put real adoption evidence in the profile prose, which is the counter-norm serious maintainers already endorse.

## Practitioner voices

- **swyx**, on profile-adjacent metrics he has been asked to track: "GitHub stars on my demos (yuck), traffic attributed to my Google Analytics UTM tag (yuck yuck)... ultimately not meaningful."
- **Braydon Coyer**, on decoration: developers "inject a bunch of 'cool' widgets and badges" when a profile "should highlight what makes you unique."
- **Dewan Ahmed**: developer relations "has the same attribution problem as marketing with none of the agreed proxies."
- A recruiter, on Blind: "I mostly use github to, uh, confirm/find your email." Another: "Interviewed over 150 people. Never looked at any GitHub."

Treat forum testimony as directional counter-evidence to the hype, not as survey data.

## Why no named framework appears

One marketing post coins an acronym framework for profile decisions. It has no evidence base, no adoption outside its own post, and no citations from other practitioners.

Profile optimization is not a headline conference topic in the field, and the discipline has no validated goal-to-decision model, so naming an invented framework would borrow authority the practice has not earned. Use the audience question and the scorecard instead.

Scope limit on everything above: the studies cited are English-language and US-centric. They do not cover hiring and developer-relations practice elsewhere; say so if a user's context is outside that scope.
