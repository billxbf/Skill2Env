# Foundations and fiscal hosts

What each type requires, what it provides, and how to decide whether to join at all.

- [The join-or-not test](#the-join-or-not-test)
- [Host types](#host-types)
- [Entity types, if the project incorporates itself](#entity-types-if-the-project-incorporates-itself)
- [Two failure cases worth knowing before filing](#two-failure-cases-worth-knowing-before-filing)
- [What gets traded away](#what-gets-traded-away)
- [Graduation mechanics](#graduation-mechanics)
- [Governing the money once it exists](#governing-the-money-once-it-exists)
- [Readiness gaps to fix first](#readiness-gaps-to-fix-first)
- [Where counsel is required](#where-counsel-is-required)

## The join-or-not test

Check all three before recommending a direction:

1. **Money.** Does the project need to receive donations, hold funds, pay contractors or reimburse travel? A legal entity is unnecessary until money is involved; a fiscal host removes the need to incorporate.
2. **Neutrality.** Do adopters need proof no single vendor controls the project? Enterprise procurement and other open-source projects ask; individual users do not. Foundation membership is the cheapest credible proof, a vendor-held trademark the cheapest way to lose the claim.
3. **Autonomy budget.** How much control over process, brand and reporting is the project willing to give up?

If money and neutrality are both "no", stay independent and revisit on a trigger - the first sponsorship offer, the first adopter asking about control, or the first time a maintainer pays for infrastructure personally.

## Host types

| Host type                          | What it requires                                                                                                                                         | What it provides                                                                                   | Cost                                                                                                                             |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Lightweight fiscal host            | nothing beyond an open project and a public ledger                                                                                                       | donation handling, transparency, no governance imposed                                             | a percentage of donations                                                                                                        |
| Fiscal sponsor with legal services | a licence that is both OSI-approved and DFSG-free; written decision-making, which the sponsor formalizes rather than replaces; asset assignment optional | financial administration, licensing and legal consultation, infrastructure - but no direct funding | around 10% of processed revenue                                                                                                  |
| Incubator-style foundation         | a champion and mentors, IP clearance and a software grant, a trademark check, monthly then quarterly reporting, releases voted twice                     | a durable neutral home, a dispute venue, an established brand                                      | the project adopts the foundation's committees, vote rules and release process wholesale, and the foundation holds the trademark |
| Level-gated technical foundation   | documented governance and a code of conduct at entry, exercised governance at the next level, organizational diversity at the top                        | staged onboarding, marketing reach, a strong neutrality signal                                     | rising process obligations at each level, plus the trademark                                                                     |
| Ecosystem or language foundation   | varies; narrower scope                                                                                                                                   | community fit and existing relationships                                                           | usually lighter than the two above                                                                                               |

Two easily missed details:

- A fiscal sponsor holding assigned assets typically cannot later transfer them to an individual or a for-profit; that irreversibility is what an adopter reads.
- A level-gated foundation checks the community-health files during review (licence, readme, contributing, code of conduct, maintainers, governance, security policy), plus a public adopters list before a level change.

## Entity types, if the project incorporates itself

Most projects should join something rather than incorporate. When incorporation is genuinely on the table, the split below is the decision underneath the host choice.

| Structure                                  | Money treatment                                                                                   | Governance shape                                                       | Typical users                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ |
| US public charity                          | donations deductible; must serve a public, charitable or educational purpose; lobbying restricted | community mission, board-led                                           | language and tooling foundations with individual-donor bases |
| US trade association                       | dues generally deductible as a business expense, not as charity                                   | corporate members, dues tiers, board seats attached to the upper tiers | most multi-vendor infrastructure foundations                 |
| European registered association            | member dues; can obtain tax-privileged status                                                     | member-driven and democratic; assets held on behalf of members         | community forges and desktop projects                        |
| European foundation (Stiftung / stichting) | endowment or donations                                                                            | board-governed, no members, self-perpetuating                          | large single-product projects                                |
| Fiscal host                                | host holds the funds for many projects                                                            | project keeps its own governance under the host's rules                | anything that needs plumbing, not an entity                  |

Two things to weigh:

- A trade association serves its corporate members' common business interests: legitimate, but a different mission from a charity's, and adopters read the difference.
- The member-association form alone holds assets for the members, so they structurally cannot be sold to a for-profit - exactly the failure that has produced forks elsewhere.

## Two failure cases worth knowing before filing

- **Charity status is not a formality.** One project's US charitable-status application was denied after roughly four and a half years, on the reasoning that open-source software authorizes use by anyone for any purpose, including commercial ones. One examiner's opinion, not binding precedent - but the multi-year denial risk is why risk-averse projects route through an existing sponsor instead of filing.
- **A fiscal host can dissolve.** In 2024 a charitable fiscal host announced a staged dissolution affecting more than 600 collectives, giving roughly seven months to spend down or transfer funds. A similarly named host serving open-source projects was legally distinct and unaffected - telling the two apart mattered enormously to anyone whose money sat in one. Know which legal entity holds the funds, and write the exit plan while nothing is wrong.

## What gets traded away

Roughly in the order projects regret them:

- The trademark and brand, held or licensed by the host with commercial use subject to its policy.
- The release process, since a host with its own release votes adds days and a licensing review to every artefact.
- The decision rules, which some hosts impose and others freeze into an agreement that takes work to change.
- A reporting cadence that becomes an ongoing maintainer cost.
- Exit friction, since leaving is slow and assigned assets do not always come back.

The gain is symmetric: neutrality adopters believe, financial and legal infrastructure, a venue for disputes larger than the maintainer group, and continuity if the founding maintainers leave.

## Graduation mechanics

The gate is a community-maturity test, not a code-quality test: what is certified is that no single company can walk away and kill the project.

At a level-gated foundation, full due diligence happens when a sandbox project applies to incubate rather than when it enters:

- Documented production use by at least three independent adopters.
- A healthy committer body.
- A two-thirds supermajority of the technical oversight committee.
- At least three months from a committee member's sponsorship.

A failed vote can fall back a level. An incubator-style foundation instead runs a mentored provisional project, completes IP clearance before graduation, and decides on a self-assessment, a discussion thread and a board resolution - lighter and more discretionary.

Map to the target's published criteria early and fix the two slow gaps first - a single-employer maintainer pool and governance never exercised - because those take quarters, and adopting a complex structure shortly before applying is itself a recognized anti-pattern.

## Governing the money once it exists

Money arrives with governance questions the code never raised. Components that cover most of it:

- A written conflict-of-interest policy.
- A budget approved by the governing body rather than whoever holds the payment credentials.
- Spending-authorization thresholds.
- An explicit reserve target, so a deficit year reads as a planned drawdown.
- A transparency mechanism: a legally mandated annual filing beats any voluntary practice precisely because it is not voluntary, and a public real-time ledger gets a smaller project most of the same effect.

The recurring friction is paid maintainers. When some draw project funds and others do not, disputes follow over who authorizes spending and whether paid contributors gain disproportionate influence.

The best-tracked mitigation is funding a defined role for administrative and triage work rather than feature development, separating "paid to keep the lights on" from "paid to decide direction". A public ledger also exposes individual compensation to scrutiny; make that trade deliberately.

## Readiness gaps to fix first

Most rejections and delays come from the same causes, in fix order:

- Maintainers from only one organization.
- Governance documented but never exercised.
- Repository permissions contradicting documented roles.
- Unclear ownership of the name, domains or registry accounts.
- Missing community-health files or a stale maintainers list.
- No adopters willing to be named publicly where the host requires it.

The first two take quarters, the rest days.

## Where counsel is required

Say this plainly rather than answering it:

- Licence changes and relicensing.
- Contributor agreements and copyright assignment.
- Trademark registration and transfer.
- The sponsorship or membership agreement.
- Export control and sanctions.
- Anything touching employment status.

Prepare the decision - what the project wants, what the host requires, what it will trade - and let a lawyer paper it.
