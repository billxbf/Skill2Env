# Funder scans, eligibility rules and where the money lands

What a corporate funder's tooling reads before a human ever sees the project, the published eligibility rules of employee-nominated funds, and the continuity risk attached to whichever entity receives the money. Figures are verified against the sources named inline.

## Contents

- What the scanners read
- Payability signals
- Employee-nominated fund eligibility
- Disqualifiers a funder applies
- Where the money lands, and how it can disappear
- Self-audit pass

## What the scanners read

Funder-side tooling resolves a dependency tree and enriches every node with health data, then a human ranks the shortlist. Three signals do most of the ranking:

- **Dependency relation.** Resolution APIs (deps.dev and equivalents) mark each node `SELF`, `DIRECT` or `INDIRECT`, across npm, PyPI, Cargo, Go, RubyGems, Maven and NuGet. Direct dependencies get read; transitive ones mostly get the automatic $4-$10 breadth sponsorship.
- **OSSF Scorecard, _Maintained_ check (0-10).** The usable liveness proxy: 7-10 reads as actively maintained, 4-6 partial, 0-3 likely dormant. A project that has gone quiet for a quarter looks dormant to a scan even when the maintainer is simply busy - a small, regular commit and release cadence is what keeps the score honest.
- **OpenSSF Criticality Score (0-1).** Weighted from project age, update recency, contributor count, organisation diversity, commit frequency, release cadence, issue-closure and comment activity, and dependents count. Published as public datasets and explicitly built to direct support and security resources.

None of these can be gamed usefully, and trying is a bad trade. Treat them as a mirror: a low _Maintained_ score before an outreach campaign predicts the objection the buyer will raise.

## Payability signals

- `.github/FUNDING.yml` on the default branch, with an **org-level fallback**: `{owner}/.github` → `FUNDING.yml` applies to every repository of that owner that lacks its own. A stale org-level file silently overrides nothing but covers everything else - check both.
- Registry metadata: npm's `funding` field (string, object with `url`, or array). Funder tooling reads manifests as well as the repository.
- Every link gets **fetched and verified live** by the funder before it enters their list. A 404 removes the project from the list entirely.
- **No funding mechanism, no target.** This is a hard filter in every documented program, not a scoring input.

## Employee-nominated fund eligibility

The FOSS-fund pattern (Indeed's FOSS Contributor Fund, also run at Microsoft, Spotify and Sourcegraph) allocates a fixed budget to one project per cycle - **$10,000/month** at Indeed. Only employees who contributed to open source during that cycle may nominate or vote.

Indeed's published eligibility rules, all four required:

1. The project is in use by the company.
2. It carries an OSI-approved license.
3. It has a mechanism to receive funds.
4. It is not employee-owned (their conflict-of-interest rule).

Two consequences for a maintainer:

- The nominator is an employee who already uses the project, so the engineer filing your issues is the person who puts you on the ballot - worth knowing when you decide how to treat that engineer's bug report.
- The vote drifts toward famous projects, which programs try to correct by surfacing underserved ones; a small library wins on a nominator's story, not on its star count.

A project that can only accept a support contract or a subscription is excluded from these funds outright - a fixed one-time budget needs a recipient it can pay once.

## Disqualifiers a funder applies

- Corporate-maintained projects: the money is a rounding error to the vendor and buys nothing.
- Support-contract-only or subscription-only recipients, when the budget is one-time.
- Employee-owned projects, wherever a conflict-of-interest rule exists.
- License or governance mismatch with the funder's own policy.
- Recent maintainer conduct incidents or a dependency-hijack history - the sponsor's brand attaches to the sponsee.

## Where the money lands, and how it can disappear

| Route                            | Fit                                                                                            | Live risk                                                                          |
| -------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Personal account on the platform | solo maintainer, no entity, no fee on personal accounts                                        | tax and legal liability sit on one individual; multi-maintainer splits get awkward |
| Own legal entity                 | invoicing companies directly, several maintainers                                              | setup and accounting cost; charity status is not a given (see below)               |
| Fiscal host                      | receiving money without incorporating; typically 3-10% of funds, 10% at Open Source Collective | the host itself can fail                                                           |

Two documented cautions:

- **A fiscal host can dissolve and take your money's home with it.** The Open Collective Foundation (a US 501(c)(3) host charging 5%) announced dissolution on 28 February 2024, effective 31 December 2024, giving its 600+ collectives until 30 September 2024 to spend down or transfer funds.
- **The separately named Open Source Collective** - a distinct 501(c)(6) hosting only OSS projects - was unaffected. Confirm which entity actually holds your funds, and write the exit-and-transfer plan before you need it.
- **Charity status is not a formality.** Yorba applied for US 501(c)(3) status in December 2009 and was denied on 22 May 2014 - roughly four and a half years - the IRS reasoning that its open-source licenses authorise use "for any purpose, including nonexempt purposes such as commercial". Risk-averse projects route through an already-recognised fiscal host instead of filing from scratch.

When money is shared between maintainers, separate the roles the money pays for. The Django Software Foundation funds a Fellowship for triage and administrative work rather than feature development, which keeps "paid to keep the lights on" apart from "paid to decide direction".

That split is the documented friction point when some maintainers are paid from project funds and others are not. A public ledger (Open Collective and similar) adds real-time accountability and exposes each maintainer's compensation to the community; that trade is a decision, not a default.

## Self-audit pass

Baseline checklist - this skill's synthesis of the signals above, not a published rubric. Run it before any corporate outreach and once a quarter afterwards:

1. Funding link present in `.github/FUNDING.yml`, verified live today, and consistent with the org-level fallback.
2. Package-manifest funding metadata filled in every ecosystem the project publishes to.
3. Scorecard _Maintained_ score checked; if it reads dormant, fix the cadence before pitching.
4. A named legal route to receive money - entity, contractor arrangement or fiscal host - with the tax form ready.
5. An invoice can be issued this week, with bank details, for an amount above the platform's invoiced floor.
6. License OSI-approved and stated in the repository, so an employee nomination cannot fail on rule 2.
7. If several maintainers share the money: spending authority written down, and roles the money pays for named.
