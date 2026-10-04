# Company type, decision authority and the non-reversal commitment

Contents: the company-type table · GitLab's published mechanics · Google's published mechanics · what to commit never to close · the six reversal cases · a weak and a strong commitment.

## Company type changes the answer

The same gates produce different verdicts depending on who is asking. Ask which row applies before drawing a line.

| Dimension          | Venture-backed startup                                                                                                                                                          | Public / late-stage software company                                                                                                                      | Non-software company                                                                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dominant motive    | Distribution and adoption ahead of monetization - Open Core Ventures frames the open core as a distribution and R&D strategy, with proprietary features as the monetization arm | Defending an existing revenue line against a hyperscaler - HashiCorp's stated 2023 trigger was vendors commercializing without material contribution back | Cost sharing, talent, and requirements imposed from outside - Bloomberg's open source office sits inside the CTO Office and frames open source as infrastructure and culture |
| Boundary primitive | Buyer persona: individual-contributor features open, manager and executive features paid                                                                                        | Deployment mode: self-hosting stays permitted, a competing managed service does not - Confluent's restriction targets competing SaaS specifically         | Enabler versus differentiator inside the product - Sony contributed multimedia frameworks while withholding camera-effect features                                           |
| Who decides        | Founder or CEO, effectively unilaterally                                                                                                                                        | Cross-functional with executive sign-off; GitLab names the CEO as final decider on large pricing decisions                                                | Governance board spanning engineering, business and legal, with IPR review                                                                                                   |
| Reversal exposure  | Low near-term, extreme once adoption is large                                                                                                                                   | Highest: fork risk plus a shareholder-visible narrative                                                                                                   | Low on the product axis, real on the talent and customer-requirement axis                                                                                                    |
| Timescale trap     | Founder-speed decisions outrun the community's ability to absorb them                                                                                                           | Quarterly reporting pressure                                                                                                                              | A Linux Foundation practitioner notes companies measure in three-month spans while maintainers organize around neither quarters nor fiscal years                             |

## GitLab: the boundary published as promises

GitLab's stewardship page publishes eleven explicit promises rather than a principle. Among them:

- an open-sourced feature will never move to a paid tier
- features landing in both editions ship simultaneously with no fixed delay
- all tests for an open source feature are released too
- the open source codebase carries no artificial limits on repositories, users, size or performance
- every stage of the DevOps lifecycle has at least some open source feature

The criterion is a **persona test, not an asset test**: who cares most about a feature - if the likely buyer is an individual contributor it is open source, otherwise source-available. GitLab states there are no features useful only to managers or executives; every proprietary feature still has an individual contributor who wants it, just not enough to be the buyer. Sid Sijbrandij attributes the framework to a 2008 formulation by Adam Lampitt about segmenting by user base rather than feature, and says he has used it since 2015.

Two details make this a live process rather than a manifesto:

- GitLab publishes acceptance criteria for the _reverse_ case, a community contribution opening an existing paid feature
- in 2020 a named executive reviewed every feature in every tier and moved eighteen features across seven DevOps stages into open source, framed as correcting tier placement under the buyer-based model

Large tiering decisions route through a named matrix:

- the Senior Director of Pricing is responsible
- CPO and CRO agree
- CMO and CFO give input
- the **CEO decides**, the only publicly named final decider found for the open/closed question

## Google: strategy call separated from compliance review

Google's release documentation assigns the "is this okay to release" call to the **launch creator's manager**, not the open source programs office, on the stated ground that the office "frequently lacks the business context to make it." Larger launches escalate to a director or VP. The office runs licensing, patent and privacy review as parallel approvers on the same launch record, routed through a launch-management system, so the decision is auditable afterwards.

The published rejection criteria are unusually candid: does the release touch Google's "secret sauce" (ranking, filtering)? Does sharing help users, or only competitors?

Named examples of things not okay to release include a proprietary algorithm kept for business reasons and a project competing with other Google interests undesirably. The stated default is **approve unless there is a good reason not to**.

The pattern worth copying from both: the business-context call belongs to whoever owns the business case, the compliance call to a specialist reviewer, and neither substitutes for the other.

## What to commit never to close

A commitment is only worth writing if breaking it would be visibly embarrassing. Each costs the same to publish - a sentence - so strongest first is also the efficiency order:

1. Never move an already-open feature into a paid tier (GitLab's promise, and the one most likely to be tested).
2. Never add artificial limits - repository count, user count, data size, throughput - to the open edition.
3. Never re-license already-open components away from an OSI-approved license.
4. Ship the tests for open features alongside the features.
5. Announce any boundary change before it lands, with the reasoning and the effective version.

Pair each promise with the role that has standing to break it. A promise nobody is accountable for is a marketing line.

## The six reversal cases

Every case below narrowed or renamed something already given. The cost concentrated in the reversal event, priced in forks.

| Case                    | Reversal                                                                   | Documented response                                                                                                                                               | What it reveals                                                                                  |
| ----------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| HashiCorp, 2023         | MPL-2.0 to BUSL-1.1 across all products                                    | The OpenTF fork emerged within days and became OpenTofu under the Linux Foundation                                                                                | Fork speed is the real cost signal - days, not quarters                                          |
| Elastic, 2021 then 2024 | Apache-2.0 to SSPL/ELv2, then AGPL added back                              | Banon acknowledged the 2021 change knowingly caused a fork with a different trajectory, and said three years later that Amazon was "fully invested" in OpenSearch | The relicensing was reversible; the fork was not                                                 |
| Redis, 2024 then 2025   | BSD to RSALv2/SSPLv1, then AGPLv3 in Redis 8                               | AWS and Google backed Valkey before the AGPL return; the CEO stated the move achieved its goal but "hurt our relationship with the Redis community"               | A licensing win and a community loss, conceded in one sentence                                   |
| Red Hat, 2023           | RHEL sources restricted to CentOS Stream                                   | Oracle, SUSE and CIQ formed OpenELA; the company blog called part of the demand "disingenuous"                                                                    | Attacking the objector's motive escalates rather than resolves                                   |
| Docker, 2017            | `docker/docker` renamed `moby/moby` - no license change, no code withdrawn | Overwhelmingly negative; the announcing pull request sat at 7 upvotes against 110 downvotes                                                                       | The cleanest natural experiment: nothing was taken away and the backlash was still severe        |
| Chef, 2019              | Open core to fully Apache-2.0 - a third to half the codebase newly opened  | RedMonk noted the binary builds stayed proprietary, prompting public questions about the "100% open source" claim                                                 | Opening _more_ still draws credibility attacks if a proprietary edge exists and is not disclosed |

These cases expose two residual risks that no framework resolves:

- governance surprise as a cost independent of scope (Docker)
- supply-side withdrawal: opening an asset creates a dependency on people who can withdraw their own contribution

## Weak and strong commitments

**Weak**

> We're committed to open source and will always have a strong community edition.

Nothing here can be violated, so nothing here can be trusted. No promise, no scope, no owner.

**Strong**

> We will never move a feature that has shipped in the open edition into a paid tier. Adding
> new paid features above the line is in scope; moving existing ones down is not. Only the CEO
> can approve an exception, and any exception is announced before the release that contains it.
> Reviewed at each annual planning cycle; the current text is published at /stewardship.

**Decision rights, weak and strong.** "Engineering leadership will review open source proposals" has no split between business call and compliance review, no escalation path, no default posture - every proposal becomes a negotiation. The strong version: "The proposing team's director makes the release/no-release call and owns the business case. Legal and security review licensing, patents and secrets in parallel and can block on those grounds only. Anything touching the ranking pipeline escalates to the CTO. Default is approve."
