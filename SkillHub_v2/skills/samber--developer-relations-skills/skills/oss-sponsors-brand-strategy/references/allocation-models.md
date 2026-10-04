# Allocation models, budgets and payment mechanics

Everything attributed to a program below was published by that program, and those publications drift - re-check before quoting a figure to a user, since platform terms and pledge totals change. The worked budget split is this skill's own default, not a published figure.

## Contents

- The four allocation models
- A worked budget split
- A weak portfolio and its diagnosis
- Payment mechanics and minimums

## The four allocation models

Listed in the efficiency order the skill ranks them in: value returned per unit of internal effort.

### 1. Breadth - dependency-share

Spread the budget automatically across the dependency graph, direct and transitive.

Reference program: one observability vendor distributed $500,000 to maintainers using $4-$10/month sponsorships across its dependency graph, reaching "95% or greater coverage" of its fundable dependencies, with roughly 90% of the budget allocated through a dependency-share platform. Its own summary of the long tail: "For many of our dependencies, we are likely their first and sole sponsor."

Read that 95% as a frontier, not a norm - the same write-up calls the company "the first company to approach 100% coverage of all of our fundable dependencies". A first-year program that lands anywhere near it has done something unusual.

- Discovery cost: near zero - the graph is the target list.
- Buys: coverage, goodwill, an honest answer to "do you fund what you use".
- Fails at: visibility. $10/month rarely appears on any public surface.
- Watch for: money landing on vendor-maintained or dormant packages, unnoticed for a year.

### 2. Depth - judgement-based strategic sponsorship

A short list of projects the company is visibly load-bearing on, funded at amounts a maintainer can plan around.

The same program's published depth allocations, per project per year:

- $15,000 to a session-replay library.
- $10,000 and $6,000 to two language foundations.
- $1,750 to a web framework.

That spread is the useful part; depth does not mean uniform.

- Discovery cost: a human decision per project, plus an annual renewal conversation.
- Buys: placement on real surfaces, a named relationship, and continuity of a dependency you cannot replace quickly.
- Fails at: coverage of the long tail.
- Watch for: a list assembled from internal advocacy rather than dependency reality.

### 3. Foundation or consortium membership

Dues to an organization that redistributes to projects and infrastructure.

The one public per-head benchmark comes from an industry pledge asking members for **more than $2,000 per full-time-equivalent developer per year**, paid to maintainers and foundations. It reports **$7,270,139** raised in total, with $3M+ in the trailing year. Members include mid-size software vendors, not only large enterprises.

- Buys: governance access, standing in an ecosystem, a listing.
- Fails at: individual maintainer relationships - nobody at a project knows your name.

### 4. Employee-nominated fund (the FOSS Contributor Fund)

A fixed amount per cycle, nominated and voted on internally. This is the one model with a named, published method behind it - _Investing in Open Source: The FOSS Contributor Fund_, by Duane O'Brien and Mandy Grover (O'Reilly Media, November 2021). Several large employers run a variant; the documented reference implementation:

- **$10,000 per month** to one selected project.
- **Anyone may nominate.** Only employees who made an open-source contribution during that voting cycle may vote - the franchise is earned by contributing, which makes the fund an internal contribution incentive as much as a donation.
- Project eligibility, all four required: in use by the company; OSI-approved license; has a mechanism to receive funds; not maintained by an employee.
- Reported lessons:
  - Open nominations to everyone rather than only employees with linked profiles.
  - Exclude projects that can only accept a support contract or subscription when the budget pays one-off.
  - The vote drifts toward famous projects, so deliberately surface underserved ones.
  - The nomination list doubles as an onboarding menu for employees who want to start contributing.

- Buys: internal engagement and a selection story that survives "why them and not us".
- Fails at: targeting precision.

## What a pledge-style commitment actually obliges

Worth reading even for a company that never joins, because it is the closest thing to a published standard for reporting this spend.

1. **Pay** more than $2,000 per FTE developer per year, direct to maintainers or foundations of the company's choice.
2. **Publish** a post reporting the year, the developer count, the total paid, and the amount per recipient. The published example format is deliberately plain: "14 developers on our team", "$30,000", "$10,000 to foo".
3. **Promote** it - a link to the post, a company description under 600 characters, branding assets.
4. **Renew** by publishing a new post each year.

Four payment categories do **not** count toward it:

- Company-controlled projects.
- Software benefiting the paying company exclusively.
- Maintainers the company already employs.
- Any arrangement returning substantial, non-incidental benefits beyond minimal acknowledgment.

The last one is where a "strategic sponsorship" quietly becomes a services contract; that is a distinction finance and legal will make eventually, so make it first.

## A worked budget split

Illustrative, not published - the percentages below are this skill's defaults and exist to be argued with. A 120-developer company, reach as primary mandate and supply chain as secondary, using the $2,000/developer floor. For context on what the top of the market pays, the one company that disclosed its actual spend reported **$3,700 per developer** - nearly double the floor.

| Line                                | Share | Amount/year | Rationale                                                                                   |
| ----------------------------------- | ----- | ----------- | ------------------------------------------------------------------------------------------- |
| Breadth across the dependency graph | 25%   | $60,000     | Automatic coverage; requires no annual decision                                             |
| Depth on 8 projects the buyers use  | 50%   | $120,000    | Placement on surfaces with measurable traffic; averages $15,000 each, spread $5,000-$30,000 |
| Employee-nominated fund             | 10%   | $24,000     | $2,000/month, one project per cycle                                                         |
| Reserve                             | 15%   | $36,000     | Incident response, a maintainer in trouble, a dependency that becomes load-bearing mid-year |

Adjust the split, never the discipline: every line names who decides it and what would end it.

## A weak portfolio and its diagnosis

> $250,000 announced in a blog post: $200,000 to a foundation membership at the top tier, $50,000 split between two projects the CTO likes. No dependency analysis. No renewal date. Placement not checked. Two of the three recipients were already funded by their corporate parent.

What is wrong with it, in order of cost:

1. **No mandate.** Nothing in the portfolio can be judged next year, because nobody said what it was for.
2. **No exposure link.** The company's actual dependency graph never entered the decision, so the supply-chain claim in the blog post is unsupported.
3. **Money to the already-funded.** The largest recipients had corporate backing; the marginal effect of the money is near zero.
4. **One-off shape.** No renewal date means it reads as a stunt to the audience it targeted.
5. **Unverified placement.** The reach claim was never checked against a surface or a traffic number.

## Payment mechanics and minimums

Platform names appear here because the numbers are platform-specific; the skill's own instructions stay generic so they survive a maintainer using something else.

- **Invoiced corporate billing** on GitHub Sponsors, the platform most maintainers publish on:
  - **$5,000 minimum per invoice**, payable within **30 days**.
  - **3% service fee** (the ~3% card-processing fee does not apply).
  - Credit spent down over time **without expiry**.
  - Under an agreement that runs **3 years** before renewal.
- **Switching an organization to invoiced billing cancels its current sponsorships**, and sponsored projects receive a cancellation email. Sequence the switch before the first sponsorship; a bulk re-sponsor tool exists but the maintainer still sees the cancellation.
- **Organization sponsorships** on that platform carry up to a 6% total fee when paid by card (3% processing + 3% service). Personal-account sponsorships pass through with no fee.
- **Fiscal hosts** (the route for projects that are not incorporated - Open Collective and similar):
  - Take a percentage of funds received, commonly 3-10%, with the Open Source Collective host at 10%.
  - Pay out against expenses on a **public ledger**, so every payment is visible.
- **Dependency-share platforms** (thanks.dev and similar) distribute one budget across a funder's direct and transitive dependencies (three levels deep, breadth-first, reweightable by language or org), which is how the breadth motion is executed without any outreach. thanks.dev's own funder page still blocks automated fetching, but its mechanics are corroborated via search; its fee has reportedly moved from a voluntary tip (5% per Canonical's 2023 account) toward 0% platform fee plus Stripe processing (more recent sources) - confirm the current fee before quoting one. Tidelift is the contract-shaped variant: it pays maintainers for named obligations rather than goodwill.
- **Below the invoiced minimum**, a company pays by card or through a fiscal host. A finance department that only issues purchase orders cannot send $50/month at all - decide this before designing the breadth line.
- Tax treatment differs by whether the payment books as marketing, engineering spend or charitable giving, and by jurisdiction. Present the options; route the decision to the company's finance and legal teams.
