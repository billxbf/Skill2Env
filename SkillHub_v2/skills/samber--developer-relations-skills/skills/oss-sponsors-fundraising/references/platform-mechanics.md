# Sponsorship platform mechanics

Fees, minimums and limits change. If you can browse the web, confirm any number before the user commits to it.

## Contents

- GitHub Sponsors: tiers
- GitHub Sponsors: goals
- GitHub Sponsors: fees, eligibility, accounts
- Invoiced sponsorships (corporate procurement)
- FUNDING.yml
- Fiscal hosting and Open Collective
- Dependency-share and obligation platforms
- Choosing a platform

## GitHub Sponsors: tiers

- Up to **10 published monthly tiers** and **10 published one-time tiers**. Publishing all twenty is possible and always a mistake - three to five live tiers is what people read.
- Maximum tier price **US$12,000/month**. Custom amounts may carry a recommended or minimum amount; the minimum applies to recurring and one-time alike.
- **A published tier's price cannot be edited.** Repricing means retiring the tier and publishing a replacement; existing sponsors remain on the retired tier until they change or cancel. Design the ladder for two years out.
- Each tier carries a reward description plus an optional welcome message explaining how to claim the reward - the welcome message is where delivery instructions belong, not the tier blurb.
- A tier can grant its sponsors access to a **private repository** (organization-owned, admin access required; only personal accounts can be invited). This is the native mechanism for sponsor-only content - anything more elaborate means building an app that checks sponsorship status through the API.

## GitHub Sponsors: goals

- Two goal types: a **number of monthly sponsors**, or a **monthly amount**. One goal at a time.
- An amount goal **publicly displays monthly sponsorship income**. Treat it as a permanent disclosure decision, not a UI toggle.
- A goal cannot be edited below what has already been achieved, and a retired goal cannot be reactivated - only replaced with a new one.

## GitHub Sponsors: fees, eligibility, accounts

- **Personal accounts: no fee** - 100% of the sponsorship reaches the developer.
- **Organization accounts: up to 6%** - 3% credit-card processing plus a 3% service fee. Invoiced billing removes the credit-card portion.
- Eligibility explicitly covers non-code work: bug reports, issue triage, code, documentation, leadership, business development, project management, mentorship and design. A documentation maintainer or triager qualifies.
- Region-gated, with a waitlist for unsupported regions. Confirm the maintainer's country is supported before building the program around this platform.

## Invoiced sponsorships (corporate procurement)

- **Minimum $5,000 per invoice**, payable within 30 days. Credit does not expire and is spent down over time.
- The 3% service fee applies; the credit-card fee does not.
- Switching an organization to invoiced billing **cancels its existing sponsorships**, which must then be re-established - expect a gap and warn the sponsor.
- The invoiced sponsor agreement runs **three years** before renewal.

Consequence for program design: a company that can only pay against a purchase order cannot send $50/month. Either size the ask to clear $5,000, or receive it through a fiscal host that issues invoices.

## FUNDING.yml

Location: `.github/FUNDING.yml` on the default branch. The sponsor button must also be enabled in repository settings (Settings → General → Features → Sponsorships).

```yaml
github: [maintainer-one, maintainer-two] # one org plus up to 4 developer usernames
open_collective: project-name
ko_fi: username
liberapay: username
patreon: username
polar: username
buy_me_a_coffee: username
thanks_dev: u/gh/username
tidelift: npm/package-name # platform-name/package-name
issuehunt: username
community_bridge: project-name # LFX Mentorship
custom: ["https://example.com/sponsor"] # up to 4 URLs
```

- One username per external platform. Quote any URL containing a colon.
- Where the package ecosystem supports funding metadata (for example the npm manifest's `funding` field), fill it too - funder tooling reads manifests as well as this file.

## Fiscal hosting and Open Collective

- A collective cannot hold money itself: a **fiscal host** holds the funds and pays approved expenses, letting a project transact without incorporating.
- Open Source Collective charges **10%** of funds received; hosts generally range **3-10%**.
- Money leaves as **expenses approved by core contributors**, recorded on a public ledger. Full transparency is a trust asset and a privacy constraint - every payment to the maintainer is visible.
- The alternative, receiving money personally, puts tax and legal liability on one individual and makes multi-maintainer splits awkward.

## Dependency-share and obligation platforms

- **thanks.dev** distributes a funder's budget across their dependency graph, direct and transitive, three levels deep, breadth-first; funders can reweight by language or GitHub org. Maintainers get paid without pitching anyone - the requirement is being findable and payable. The vendor's own FAQ and account/settings pages are JS-rendered and login-gated, so its mechanics are corroborated via search instead (Jamie Tanna's product-requirements analysis, a Hacker News thread where co-founder Armin Nehzat describes a 5% minimum tip that a funder can raise up to 100%, and Canonical's own account of an actual invoice quoting the same 5% commission). A single third-party comparison site claims a 0% platform fee with only Stripe processing costs passed through, but that claim traces to no statement from thanks.dev itself. Confirm the fee directly on the funder's own thanks.dev account or settings page - the live setting, not the marketing site - before quoting one.
- **Tidelift** pays recurring amounts for _obligations_ (security response, maintenance, metadata quality) rather than goodwill. Closer to a contract than a donation, and it survives the sponsor's enthusiasm fading.
- **Polar, Ko-fi, Liberapay, Buy Me a Coffee, Patreon, IssueHunt** cover one-off, content-driven or bounty-driven funding. Patreon is the historical route for content rewards; Ko-fi and Buy Me a Coffee suit low-friction one-time thanks.

## Choosing a platform

| Situation                                              | Use                                                                   |
| ------------------------------------------------------ | --------------------------------------------------------------------- |
| Solo maintainer, personal income, no entity            | GitHub Sponsors personal account (no fee)                             |
| Multi-maintainer project, shared budget, public ledger | Fiscal host (Open Collective or equivalent)                           |
| Company sponsor paying by purchase order               | Invoiced sponsorship (≥$5,000) or an invoice from the fiscal host     |
| Small library, no audience to pitch                    | FUNDING.yml plus package metadata; harvest dependency-share platforms |
| Selling named commitments, not goodwill                | Obligation platform, or a direct retainer contract                    |

Two platforms is the practical maximum: one for individuals, one that can issue invoices. More than that splits reporting and confuses the ask.
