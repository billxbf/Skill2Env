# Sponsorship policy, nomination process and measurement

The artefacts a sponsorship program publishes, and the numbers it reports on afterwards.

## Contents

- Public policy skeleton
- Nomination and voting process
- Outreach note to a maintainer (good and bad)
- Measurement table with a filled example
- Annual report shape
- Renewal and exit

## Public policy skeleton

Publish this on the company's open-source page before the first payment. Maintainers read it before accepting; employees read it before nominating. It is what stops the program being read as favouritism.

```markdown
# Open-source funding policy - <company>

## Why we fund

One paragraph: the mandate, in plain language.

## What we fund

Eligibility: in use by us / OSI-approved license / able to receive funds /
not maintained by our own staff. Anything else we exclude, and why.

## How much and how often

Budget shape, cadence, and whether a sponsorship is recurring or one-off.

## How a project is chosen

Who decides, on what inputs, how often, and how to ask us to consider a project.

## What sponsorship does not buy

No roadmap position. No merged pull requests. No priority outcomes.
No obligation to advertise us, thank us, or answer us faster than anyone else.

## Conflicts of interest

How we handle projects maintained by employees, by investors, or by customers.

## Disclosure

Our employees disclose the relationship when they advocate publicly for a
project we fund.

## Contact

A named human, not a form.
```

The line that does the most work is "what sponsorship does not buy". Maintainers publish the same boundary from their side; a funder who publishes it first is trusted faster.

## Nomination and voting process

For the employee-nominated model, write the rules down before the first cycle:

1. **Who nominates** - everyone, with no prerequisite. Restricting nominations to employees with linked accounts measurably suppresses participation.
2. **Who votes** - employees who contributed to open source during the cycle. Earning the vote by contributing is what turns the fund into a contribution program.
3. **Eligibility check** - run the four filters (in use, OSI license, can receive funds, not employee-maintained) before the ballot, not after.
4. **Cadence and amount** - a fixed amount per cycle, paid promptly. A fund that pays late loses its internal credibility first.
5. **Counterweight to fame** - seed each ballot with underserved candidates from the dependency graph, because open voting drifts toward projects that already have money.
6. **Reuse the ballot** - publish the nomination list internally as a menu for employees who want somewhere to start contributing.

## Outreach note to a maintainer

Most sponsorships need no outreach - you pick a tier and pay. Write to the maintainer when the amount is custom, invoiced, or tied to a placement.

**Good:**

> Hi <name> - we run <product> and <project> sits in our auth path; our SBOM shows it in every build we ship. We would like to sponsor at $1,000/month for the next 12 months, invoiced annually so it clears our procurement.
>
> To be explicit about what we are not asking for: no roadmap input, no priority on our issues, no obligation to mention us. If your top tier includes a logo on the docs site we would take it; if it doesn't, the sponsorship stands anyway.
>
> What do you need from us to invoice - an entity name, a PO, a tax form? Happy to work through your process.

**Bad:**

> Hi! We're excited to explore a strategic partnership around <project>. We'd want quarterly roadmap syncs, priority handling for our issues, and a joint blog post announcing the collaboration. Could you send over a deck of sponsorship packages?

The second note asks a volunteer for account management, implies influence over the roadmap, and treats a maintainer like a vendor with a sales team. It is also how a sponsorship becomes a story about a company trying to buy a project.

## Measurement table with a filled example

The figures below are invented to show the table's shape. No public benchmark exists for what a corporate sponsorship program should expect on any of these rows, so copy the columns and the discipline - never the numbers. Fill the baseline column from the company's own measurement before the first payment; that is the only number in the table with any authority.

| Mandate      | Metric                                                   | Baseline (year 0) | Target (year 1) | Actual                                   |
| ------------ | -------------------------------------------------------- | ----------------- | --------------- | ---------------------------------------- |
| Supply chain | Fundable direct dependencies covered                     | 4%                | 80%             | 86%                                      |
| Supply chain | Dependencies with a dormant maintenance score            | 31                | < 20            | 24                                       |
| Supply chain | Median response on issues we filed upstream              | 19 days           | < 10 days       | 11 days                                  |
| Reach        | Placements live and verified                             | 0                 | 8/8             | 7/8 (one docs redesign dropped the logo) |
| Reach        | Referral sessions from placement URLs                    | 0                 | any measurable  | 2,140                                    |
| Reach        | Unaided mentions of the program in developer communities | 0                 | > 5             | 12                                       |
| Internal     | Employees contributing during a voting cycle             | 6                 | 25              | 31                                       |
| Policy       | Breaches raised by a sponsee                             | -                 | 0               | 0                                        |

Two disciplines make this table honest:

- Capture the baseline **before** the first payment.
- Put a named owner on every row.

What it deliberately omits is any attempt to attribute revenue: nobody clicks a README logo and buys, and a last-click model built on this channel collapses at its first audit.

## Annual report shape

Short, public, and specific. The industry pledge publishes the minimum a report must disclose, short enough that there is no excuse for skipping it:

- The year.
- The number of full-time-equivalent developers on staff.
- The total paid.
- The amount per recipient.

Its own worked example reads like "14 developers on our team", "$30,000", "$10,000 to foo". Publishing it again each year is what distinguishes a program from an announcement.

The fuller template below adds what maintainers actually read on top of that minimum:

```markdown
# Where our open-source money went in <year>

Total: $X across N destinations.
Breadth: $A across M dependencies (median $B each).
Depth: table of project, amount, why it matters to us.
Nominated fund: projects chosen per cycle, and who voted.
What we got wrong this year: one honest paragraph.
Next year: budget direction and how to reach us.
```

The "what we got wrong" paragraph is what separates a report from a press release, and it costs nothing.

## Renewal and exit

- Put every sponsorship's renewal decision **before** the budget close date, not after; a lapse caused by internal timing reads to the maintainer as a withdrawal.
- Tell a maintainer before a sponsorship ends, with a reason and a date. A silent cancellation is remembered far longer than the money was.
- End a sponsorship for stated reasons only:
  - The dependency is gone.
  - The project is dormant.
  - The mandate changed.
  - A policy breach.

  Never for a disagreement over a technical decision - that is exactly the influence the policy promised not to buy.

- Re-run discovery annually. Dependency graphs move, maintainers hand over projects, and funding destinations go stale; last year's verified list is this year's unverified list.
