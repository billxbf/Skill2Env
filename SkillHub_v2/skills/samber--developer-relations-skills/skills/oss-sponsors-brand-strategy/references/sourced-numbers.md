# Where every number in this skill comes from

Read this before quoting any figure to a user, and before defending a threshold in a budget review. Each row says whether the number was **published** by someone who ran a program, or **set by this skill** as a starting default. A default is a place to begin an argument, never an industry standard - presenting one as a benchmark is how a portfolio review gets discredited.

Published figures drift: platform terms change, pledge totals grow, programs re-publish. Re-check before quoting one.

## Contents

- Published figures
- Defaults set by this skill
- How to talk about each kind

## Published figures

| Figure                                    | Value                                                                                                                                    | Where it comes from                                                                                                                                             |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Per-developer funding floor               | more than **$2,000 per full-time-equivalent developer per year**                                                                         | The industry pledge's membership terms                                                                                                                          |
| Per-developer actual, one program         | **$3,700 per developer**, its own words: "quite reasonable compensation for the value we receive"                                        | An observability vendor's write-up of its $500,000 program                                                                                                      |
| Best published dependency coverage        | **"95% or greater coverage of our fundable dependencies"**, claiming to be "the first company to approach 100%"                          | Same write-up                                                                                                                                                   |
| Breadth sponsorship size                  | **$4-$10 per month** per dependency                                                                                                      | Same write-up                                                                                                                                                   |
| Depth allocations, same program           | **$15,000** to a session-replay library, **$10,000** and **$6,000** to two language foundations, **$1,750** to a web framework, per year | Same write-up                                                                                                                                                   |
| Share of that budget routed automatically | roughly **90%**, through a dependency-share platform                                                                                     | Same write-up                                                                                                                                                   |
| Employee-nominated fund size              | **$10,000 per month** to one project per cycle                                                                                           | The reference implementation of the FOSS-fund pattern, documented in _Investing in Open Source: The FOSS Contributor Fund_ (O'Brien and Grover, O'Reilly, 2021) |
| Fund eligibility rules                    | in use by the company; OSI-approved license; able to receive funds; not maintained by an employee                                        | Same                                                                                                                                                            |
| Invoiced corporate billing                | **$5,000 minimum per invoice**, **30 days** to pay, **3%** service fee, **3-year** agreement term                                        | The dominant sponsorship platform's own billing documentation                                                                                                   |
| Card-paid organization sponsorships       | up to **6%** total (3% processing + 3% service); personal accounts pass through at **0%**                                                | Same                                                                                                                                                            |
| Fiscal-host cut                           | commonly **3-10%** of funds received; the largest open-source host charges **10%**                                                       | Fiscal-host published fee schedules                                                                                                                             |
| Maintainer placement pricing              | tiers priced against **published monthly view counts** of 60k, 20k and 6k on specific surfaces                                           | A widely sponsored individual maintainer's public tier ladder                                                                                                   |
| Health-score reading                      | Scorecard **Maintained** check, 0-10                                                                                                     | The open scorecard project's definition                                                                                                                         |
| Criticality scale                         | **0 to 1**, from ten weighted signals including contributor count, organizational diversity and dependents count                         | The open criticality-score project                                                                                                                              |

## Payments a pledge-style program refuses to count

Published alongside the per-developer floor, worth applying even if the company never joins anything. Money does not count as open-source funding when it goes to:

- A **company-controlled project**.
- Software that **benefits the paying company exclusively**.
- A **maintainer the company already employs**.
- An arrangement returning **substantial, non-incidental benefits beyond minimal acknowledgment**.

The last one is the trap. A sponsorship negotiated for deliverables is a services contract; call it that, book it that way, and stop describing it as funding open source.

## Defaults set by this skill

These are starting points, not published figures. Say so when a user asks where they came from, and change any of them the moment the user has a better reason.

| Default                           | Value                                                                               | Why this starting point                                                                                      |
| --------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Opportunistic reserve             | **10-20%** of the budget                                                            | Enough to fund one unplanned emergency at depth-tier size without reopening the budget                       |
| Split for a reach-primary program | 25% breadth / 50% depth / 10% nominated fund / 15% reserve                          | Puts the majority on the surfaces the primary mandate is judged on, keeps breadth alive                      |
| Coverage pass threshold           | **80%** of fundable direct dependencies, when supply chain is the primary mandate   | Deliberately below the 95% frontier above: reaching that took a dedicated program and a platform integration |
| Scoring axes and weights          | exposure, fragility, audience fit, relationship value, weighted ×3/×2/×1 by mandate | A weighting that makes the primary mandate decide ties; the axes come from what funders say they buy         |
| Depth portfolio size              | roughly a dozen sponsorships a team can renew thoughtfully                          | An annual review that degenerates into rubber-stamping is worse than a shorter list                          |
| Dormancy cut                      | Maintained score **0-3** disqualifies without a revival agreement                   | The scorecard project's own reading of that band as likely unmaintained                                      |
| Review cadence                    | first check at **12 months**, annually after                                        | Matches the budget cycle that decides renewal                                                                |

## How to talk about each kind

- Published figure: name what it is evidence of. "One company that published its program paid $3,700 per developer"  -  not "companies pay $3,700 per developer".
- Default: name it as a starting point and invite the argument. "Start at 80% coverage; the only published program above that built a platform integration to get there."
- Anything you cannot place in either table: leave it out. An unsourced round number in a budget deck is the first thing a finance reviewer tests.
