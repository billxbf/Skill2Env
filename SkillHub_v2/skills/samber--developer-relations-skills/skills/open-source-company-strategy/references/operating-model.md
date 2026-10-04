# The operating model behind a company open source decision

Contents: the function set · inbound policy · outbound policy · upstream-first · where to participate · cost lines · scaling by company stage.

The line drawn in the strategy is only real if someone runs it. This file covers the company-side machinery. Project-side operation - decision rights, maintainer ladders, succession - belongs to `samber/developer-relations-skills@oss-governance`.

## The function set

The TODO Group describes an Open Source Program Office as "a designated place where open source is supported, nurtured, shared, explained, and grown inside a company", with six functions:

- communicate the strategy internally and externally
- oversee its execution across business units
- facilitate consumption of open source inside products
- ensure release quality for published code
- engage communities and manage contributions
- maintain license compliance review

Their staffing picture at scale:

- an executive-level program manager
- legal representation (a dedicated attorney for larger organizations)
- a review board spanning engineering, product and legal
- developer advocates
- tooling administrators
- compliance

Assign the **functions** regardless of company size; headcount is what scales. A twenty-person company runs all six as one engineer at 20% plus outside counsel on retainer. What it cannot do is leave them unassigned - the observed failure is not a missing office, it is a release nobody reviewed and a repository nobody answers.

**Do not let this office make the strategy call.** Keep step 7's split at any size: whoever owns the business case decides, a specialist reviews compliance, and neither covers for the other.

## Inbound policy - code the company consumes

- A license allowlist and denylist, with the escalation path for anything on neither.
- A third-party audit procedure at dependency-introduction time, not at audit time.
- An approval workflow proportionate to risk: automatic for allowlisted licenses, reviewed for the rest.

State the TODO Group's warning to executives: rigid policies get circumvented, and circumvention is where the security exposure appears. A policy engineers satisfy in minutes beats a stricter one they route around.

## Outbound policy - code the company publishes

- A contribution policy covering what employees may contribute on company time and equipment, and to which projects.
- A release checklist for new repositories: license file, notices, secrets scan, dependency licenses, trademark check, security contact, maintainer named.
- The CLA-versus-DCO decision - hand it to `samber/developer-relations-skills@oss-license-strategy`, but record that the choice exists, since dual licensing later is impossible without collecting the rights up front.

## Upstream-first

TODO Group's phrasing: "Submit patches upstream first, and consume in your own products downstream." Skipping it silently invalidates the maintenance motive that justified the strategy (step 8). Make it a stated engineering default with a documented exception path - a fix needed before upstream can review it ships downstream _and_ opens the upstream pull request in the same week.

## Where to participate

The TODO Group's engagement triage: assess which projects are strategically critical - critical business infrastructure, development and deployment tooling, customer-facing software - and engage deeply with the most important ones rather than contributing to everything the company consumes.

Rank the depth ladder by return per engineer-hour, not by price - efficiency: `contribute fixes upstream > report issues > maintain a component > hold a governance seat > fund a membership`, against effort: `maintain a component > hold a governance seat > fund a membership > contribute fixes > report issues`. Upstreamed fixes lead because they delete maintenance the company would otherwise re-pay at every upgrade; plain consumption buys nothing, so it is not a rung. The order starves maintaining a component - highest value on anything the company genuinely depends on, and a standing job - so promote it when the dependency is critical business infrastructure and nobody upstream maintains it. Pick a rung per project and write it down; undeclared ambition to reach the top rung on ten projects is how open source budgets get spent with nothing to show.

## Cost lines to budget

- Maintainer time - the dominant cost and the one usually left out. Count review, releases, issue and pull-request response, security-report handling.
- Legal review at release, plus inbound audit tooling.
- Training on licenses, governance and conflict resolution.
- Foundation memberships. The TODO Group's published band is $5,000–$250,000+ per year, undated in their guide and moving - an order of magnitude; check the target foundation's current schedule before it enters a budget.
- Community presence: conferences, sponsorships, travel.
- Security response: a contact address, a disclosure policy, someone on the hook.

State the annual total in the brief. A strategy whose cost was never added up gets cut mid-year, producing exactly the abandoned repositories it was supposed to avoid.

## Scaling by company stage

- **Pre-product-market-fit.** One person, part time; two artifacts only - a release checklist and a license allowlist. Open SDKs and specs, defer the rest.
- **Growth.** A named part-time owner with legal on call, published inbound and outbound policies, an upstream-first default, one funded maintainer per open repository.
- **Enterprise.** The full function set, a review board, compliance tooling, foundation memberships, a public position on the open-core line.

## Measuring the program

Measure against the motive first - per-motive signals live in the motives reference. Program-health signals underneath it:

- repositories with a named owner and a release in the last quarter
- median first response on issues from outside the company
- external contributor organizations
- upstream patches landed versus private patches carried
- time-to-approval on the inbound workflow

Red Hat's open source office adopted **CHAOSS** as its definition of community health - a ready-made metric vocabulary, but it measures health, not strategic return. Pair that with the TODO Group caution the skill's measurement section states, pick the two or three signals your motive implies, and ignore the rest even when a dashboard offers them.

The one documented company-level success criterion found for an individual project: Spotify spins successful open source projects into separate business units launching commercial products, with the open source office identifying candidates (Linux Foundation/TODO, "Business Value of the OSPO"). One company's model, not a benchmark.
