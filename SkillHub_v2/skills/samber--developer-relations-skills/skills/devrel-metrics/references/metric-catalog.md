# Metric catalog

Candidate metrics per tier, plus the published spines they hang off. Pick from here; do not ship the list.

Tiers below run reach → business impact, which is the order value and collection effort both rise in - not the order to build in. Build order is efficiency, decided in SKILL.md § The tier ladder: `enablement > engagement > product impact > business impact > reach`.

## Contents

- [Named spines and their sources](#named-spines-and-their-sources)
- [Tier 1 - reach](#tier-1--reach)
- [Tier 2 - engagement](#tier-2--engagement)
- [Tier 3 - enablement](#tier-3--enablement)
- [Tier 4 - product impact](#tier-4--product-impact)
- [Tier 5 - business impact](#tier-5--business-impact)
- [Open-source variants](#open-source-variants)
- [Qualitative evidence that belongs in the sheet](#qualitative-evidence-that-belongs-in-the-sheet)

## Named spines and their sources

| Spine                               | Source                                                                                                | Shape                                                                                                                  | Choose when                                                   |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| AAARRRP                             | Phil Leggetter, 2016, adapted from Dave McClure's AARRR with a seventh element for developer products | awareness, acquisition, activation, retention, referral, revenue, product                                              | a charter already names which of the seven the business funds |
| Developer journey                   | Matthew Revell, 2016                                                                                  | initial awareness → deep awareness → evaluation and validation → commitment → standardization → community and advocacy | the question is where developers leak, not which goal to fund |
| Awareness / enablement / engagement | Mary Thengvall, 2021                                                                                  | three functions mapped to advocate, developer-experience and community-management roles                                | several people each need a number they own                    |
| Orbit levels                        | Orbit Model, published 2019, no longer actively developed                                             | explorer → participant → contributor → advocate, gravity = love × reach                                                | community depth specifically; not a program-wide spine        |
| CHAOSS Starter Project Health       | CHAOSS, `chaoss.community/kb/metrics-model-starter-project-health/`                                   | time to first response, change-request closure ratio, contributor absence factor, release frequency                    | the product is a repository                                   |

Revell's journey guide closes by deferring per-stage measurement to a future guide that was never published. That is a fair statement of the field: the stage vocabulary is settled, the per-stage numbers are not, and inventing them for a specific product is legitimate work - just label them as yours.

## Tier 1 - reach

| Metric                 | Definition                                                              | Source                                | Caveat                                                                                                                                                                      |
| ---------------------- | ----------------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content sessions       | sessions on posts, docs pages or landing pages published by the program | web analytics                         | attribution to a channel is directional at best, and a third-party script misses most of a developer audience - report step-to-step ratios inside one source, not absolutes |
| Video and stream views | views over a fixed window after publication, not lifetime               | platform analytics                    | definitions of a "view" differ per platform; never sum across platforms                                                                                                     |
| Talk audience          | in-room attendance plus recording views at 30 days                      | organiser numbers, platform analytics | organiser counts are usually registrations, not attendance                                                                                                                  |
| Newsletter reach       | delivered and opened, by issue                                          | mail platform                         | open rates are inflated by privacy proxies; use clicks or replies instead where possible                                                                                    |
| Mentions               | third-party mentions of the product in developer venues over a period   | listening tooling or manual search    | volume says nothing about sentiment; pair with a read of the actual threads                                                                                                 |

Never make one of these a program goal. They exist to explain a downstream movement, not to be moved.

## Tier 2 - engagement

| Metric                               | Definition                                                                                         | Source                              | Caveat                                                                |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------- |
| Questions asked by non-staff         | questions opened in community venues or the forge by people outside the team, per period           | forge API, community export         | needs a staff/bot flag to mean anything                               |
| Repository clones and unique cloners | per period, against a trailing baseline                                                            | repository traffic panel            | short retention windows; export monthly or lose the history           |
| Docs search terms with no result     | count and top terms per period                                                                     | docs search log                     | the highest-yield engagement metric for a docs team: it names the gap |
| Qualified conversations              | conversations with someone who has the problem, influences the decision, and agreed to a next step | conversation log with a fixed shape | define the bar before the event, or the count is not comparable       |
| Sample-repo forks and template uses  | per period                                                                                         | forge API, template telemetry       | forks include vanity forks; pair with clones                          |

## Tier 3 - enablement

The tier a DevRel program most directly owns. Prefer these as primaries when the driver is developer enablement or adoption.

| Metric                            | Definition                                                             | Source                                  | Caveat                                                                         |
| --------------------------------- | ---------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------ |
| First-success rate                | share of new accounts reaching the defined success event within N days | product analytics                       | the success event must be one specific, instrumented action, agreed in writing |
| Median time to first success      | signup (or docs entry) → success event                                 | product analytics                       | medians only; the mean is destroyed by long-tail sessions                      |
| Step-level drop-off               | share abandoning at each documented step                               | product analytics plus docs analytics   | needs the quickstart instrumented per step; often the first real analytics ask |
| Support load per 100 new accounts | tickets or issues opened per 100 new accounts in their first 30 days   | support system                          | falling load can also mean falling adoption; read alongside signups            |
| Docs task success                 | share of testers completing a fixed task set on a cold environment     | moderated or unmoderated test runs      | small-N by nature; report the run list, not a percentage                       |
| Cold-run defect count             | failures found running the documented path on a clean machine          | scheduled cold run or docs-as-tests job | zero defects usually means the run was not cold                                |

Self-serve activation figures in the 20-40% band circulate widely for developer products. Treat them as order-of-magnitude context, not a benchmark - the sourcing is practitioner claim, not study.

## Tier 4 - product impact

| Metric                                    | Definition                                                                               | Source                             | Caveat                                                           |
| ----------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------- |
| Cohort activation                         | activation rate of accounts whose first touch was a program surface, versus all accounts | product analytics plus a touch tag | needs the cohort defined before the period, not after            |
| Cohort retention at 30/60/90 days         | still active at each mark, by join cohort                                                | product analytics                  | one cohort per period; do not average cohorts of different sizes |
| Second-project rate                       | share of developers starting a second project or second integration                      | product analytics                  | the strongest single signal that first success was real          |
| Feature adoption after an enablement push | adoption of the targeted feature before versus after, against a control feature          | product analytics                  | pick the control feature in advance                              |
| Contributor conversion                    | users who become contributors within a period                                            | forge API                          | see the open-source variants below                               |

## Tier 5 - business impact

| Metric                                        | Definition                                                                                     | Source                              | Caveat                                                                    |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------- |
| Influenced pipeline                           | value of opportunities whose account had at least one recorded program touch before the stage  | CRM plus a touch record             | over-counts by construction; never present without the word "influenced"  |
| DevRel Qualified Leads routed                 | connections passed to another team with the receiving team named, per period                   | a maintained log                    | a count of relationships, not of revenue; review for patterns quarterly   |
| Support deflection                            | tickets avoided, estimated from community answers to questions that would otherwise be tickets | support plus community data         | an estimate with a stated method, always; label it as one                 |
| Expansion in accounts with community presence | net expansion in accounts with at least one active community member, versus those without      | CRM plus community identity mapping | selection bias runs both ways; state it                                   |
| Hires sourced                                 | candidates entering the hiring funnel from program surfaces                                    | applicant tracking                  | keep separate from product metrics; different consent and different owner |
| Ecosystem integrations shipped                | third-party integrations, plugins or SDKs released in the period                               | forge, registry, partner list       | a slow metric; annual reading, not quarterly                              |

## Open-source variants

When the product is a repository and there is no purchase, anchor on the CHAOSS starter set rather than inventing metrics:

- **Time to first response** - median elapsed time from an issue or change request opening to a first _human_ response, bots excluded. The two-business-day figure widely quoted as the CHAOSS target is not one: it appears only inside VMware's case study on the starter-model page, as that company's internal guideline. Cite it that way.
- **Change-request closure ratio** - closed (merged plus rejected) ÷ opened in the same window. CHAOSS states the expectation qualitatively: projects should keep up with incoming change requests and resolve them in a timely manner. A ratio holding near or above 1 is a reasonable self-set line, not a published standard.
- **Contributor absence factor** - smallest number of people producing 50% of contributions. CHAOSS states the direction only: lower means higher dependency on fewer contributors, and therefore higher risk.
- **Release frequency** - releases per period including point releases. CHAOSS keeps this one deliberately open, stating that "no two projects have the same needs", and notes that delayed security releases leave users without an easy upgrade path.

**Treat every cadence or ratio cutoff as yours to set.** Any cutoff in a repository health report is either one company's internal figure (name the company), a self-set baseline (say so), or folklore. Adopt CHAOSS's definitions verbatim so the numbers stay comparable, and derive the thresholds yourself.

CHAOSS states its own caveats:

- "automation and bot activity can influence the usefulness of several metrics in this model, in particular Time to First Response and Change Request Closure Ratio".
- The absence factor ignores knowledge specialisation.
- Release frequency is meaningless for docs-only repositories and may be counted off-forge.
- "it's important not just to look at the numbers, but also at the trends".
- It also refuses cross-project comparison outright: "we do not compare projects against each other, but instead, we expect teams to use their metrics to make improvements".

Downloads, dependents and unique cloners beat stars for adoption. An issue opened by a stranger who read the docs is worth more than a hundred stars.

When the artifact ships to a hub rather than to a package registry - a model or dataset directory, a connector or plugin marketplace - add two metrics and keep them apart:

- **Hub downloads or installs** - a dependency signal. It accrues slowly to whatever is wired into someone's scheduled pipeline, so it barely moves at launch and keeps moving for years afterwards.
- **Hub likes or favourites** - an attention signal. It spikes on release and decays, and it concentrates on different artifacts entirely.

Reporting one as if it were the other is the standard failure on these surfaces; the hubs' own published analyses say so. Neither is deduplicated by user unless the hub's paid analytics tier is bought, so both are request counts, not people. Definitions differ per hub and sometimes per surface _within_ a hub - write the definition next to the number, and never sum across hubs.

## Qualitative evidence that belongs in the sheet

Numbers alone lose the argument when the counts are small, which is most of the time in DevRel. Reserve two rows of the framework for evidence that is not a number:

- **Verbatim quotes** from developers, with source and date, on what the program changed for them.
- **Friction findings** from cold runs and support threads, with the fix shipped and the date.

Both are auditable and both answer "so what". A framework of pure counts under-reports exactly the work that developers value most.

Two rules keep qualitative rows from becoming anecdote:

- **Tag each finding with a confidence level** - high, medium or low - set by how many independent sources back it, and show the tag next to the finding.
- **Hold a minimum sample.** Below roughly five to ten independent data points for a given segment, present the finding as a hypothesis, not a conclusion. This is the qualitative twin of the small-N floor applied to counts.
