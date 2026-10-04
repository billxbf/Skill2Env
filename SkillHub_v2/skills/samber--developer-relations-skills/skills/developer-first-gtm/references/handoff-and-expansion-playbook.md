# Handoff and expansion playbook

Contents: account rollup; the three signal families; the threshold rule template; contact routing by role; the champion enablement pack; expansion vectors and triggers; enterprise blockers; the numbers that prove expansion is real.

## Account rollup

Qualification happens at account level. Individual usage is the input, an account is the unit. Sources, roughly in order of reliability:

| Source                                       | Strength                               | Weakness                                                        |
| -------------------------------------------- | -------------------------------------- | --------------------------------------------------------------- |
| Organization/workspace object in the product | Authoritative, matches how they use it | Only exists if the product models teams                         |
| License key, API key or install ID           | Ties usage together across users       | Says nothing about which company                                |
| Email domain                                 | Cheap, immediate                       | Free-mail addresses and contractors leak; subsidiaries fragment |
| Self-reported company at signup              | Free text a human can act on           | Frequently blank or joking                                      |
| Enrichment from IP/company data              | Fills gaps at scale                    | Guesses, and looks invasive if quoted back at the user          |

Combine at least two. If none is available, building rollup is the first line item of the plan - every rule below depends on it.

## The three signal families

**Depth - is the product doing real work?**

- Production environment flag.
- Sustained volume over weeks (not a one-day spike).
- Integration into CI/CD or a deploy pipeline.
- Data retained rather than sampled.
- Repeat sessions across several weeks.

**Spread - is more than one human involved?**

- Second and third active developer in the same account.
- Invites sent and accepted.
- A shared workspace or project.
- Several repositories or services instrumented.
- A config file committed to a shared repo.

**Boundary contact - did someone touch something only an organization needs?**

- Visited or clicked SSO/SAML, RBAC, audit-log or compliance pages.
- Hit a rate, seat or retention limit repeatedly.
- Requested a security questionnaire, SOC 2 report or DPA.
- Opened billing, invoicing or procurement pages.
- Asked about self-hosting or data residency.

Boundary contact is the rarest and strongest signal because it maps one-to-one onto the paid boundary the business model defined.

- Depth without spread usually means a solo power user.
- Spread without depth usually means an evaluation that has not committed.

**A published cross-check.** Zapier's four sales-assist qualification signals, reported in _What is good free-to-paid conversion_:

- multiple active users on one domain
- usage growing over time
- a use case indicating the customer would benefit from help
- a role matching the ICP

Three of the four are spread and depth; the fourth is firmographic. Notably, the same source reports that sales touchpoints improved not only conversion but post-purchase retention - the argument against treating assisted contact as a tax on the free surface.

**Two dimensions, not one score.** _The Transition_ scores sign-ups on two axes:

- **observable** factors - title, company and size, corporate versus personal email domain, organisation size
- **behavioural** factors - completed or abandoned sign-up, feature breadth, frequency, activation depth, several users on one domain

Routing follows from the pair:

- high observable with low behavioural is a conversion-assist opportunity
- high observable with high behavioural is an expansion opportunity
- low observable is tech touch only, whatever the behaviour

The same source's advice on where to start is worth taking literally: post new sign-ups into an internal channel and have a human read them for a few weeks before building any scoring system.

Reject the MQL construction while you are here: a lead that accumulates points for opening an email and visiting the pricing page tells you about marketing exposure, not about a developer's product usage. Tuning its weights is the wrong project.

## Threshold rule template

Write one sentence, fill the blanks from your own conversion data - the percentile at which accounts historically start paying - and review it quarterly:

> An account becomes qualified when it has **N or more active developers** and **M weeks of production usage**, or when **anyone in it makes boundary contact**. Qualified accounts are contacted by **<role>** within **<hours>** with **<technical offer>**. Accounts below the threshold are **not contacted by a human**; they receive product and documentation surfaces only.

Rules for choosing N and M:

- derive them from the accounts that already converted
- prefer the value that produces a queue the responder can actually clear
- never copy a threshold from another company's blog post, since cohort shapes differ too much for the number to transfer

Before writing any threshold, check that a human belongs in the loop at all. _The Transition_ offers the arithmetic: a salesperson should return about **4x their fully loaded cost** in incremental revenue. If the qualified-account volume times realistic deal size cannot clear that, the honest answer is a better product surface, not a rule.

One statistic to keep out of this section: the widely repeated "contact within 5 minutes and you are 21x more likely to qualify". It comes from inbound form-fill research in sales-led funnels, usually cited to a vendor blog rather than the underlying study, and importing it into a developer motion argues for contacting on sign-up - the single behaviour this audience punishes hardest.

## Contact routing by role

| Role                                     | First contact should be                                                                                                              | Never send them                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| Active developer                         | Help with the thing they are actually doing: a limits/quota conversation, an architecture review, a migration hand, a bug they filed | "15 minutes to learn about your needs"                 |
| Technical champion                       | The enablement pack below, framed as material for _their_ internal case                                                              | A pitch deck they cannot re-use internally             |
| Approver (security, architecture, legal) | The risk answers unprompted: license, data handling, SLA, security posture, exit plan                                                | Feature marketing                                      |
| Economic buyer                           | Cost comparison against status quo and the do-nothing option, ideally introduced by the champion                                     | A cold email that bypasses the champion and burns them |

## The champion enablement pack

The highest-leverage artifact in company adoption, because the champion argues in rooms you are not in. Contents:

1. A one-page internal case: problem, what changed after adoption, numbers taken from _their own_ usage.
2. A benchmark or proof they can re-run and defend as their own work.
3. A reference architecture and a migration path from what they run today.
4. Pre-answered risk questions: license terms, data handling and residency, SLA and support tiers, security posture and certifications, exit and data-export plan.
5. A cost comparison including the do-nothing option and the build-it-ourselves option.
6. Named references or public case studies in a comparable environment.

Instrument it. A pack that is sent and never opened is evidence that the person you think is a champion is not one yet.

## Expansion vectors and triggers

| Vector                     | What grows                        | Trigger to wire                                                                                | Natural owner                            |
| -------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------- |
| More developers, same team | Seats or active users             | Second/third developer joins; invite sent; a shared artifact opened by a new person            | Product (spread mechanics)               |
| More teams, same company   | Accounts or workspaces            | New workspace/domain appears; internal referral; platform-team enquiry                         | Sales or partnerships, with the champion |
| More workload per user     | Consumption                       | First production deploy; new environment or region; limit hit repeatedly; seasonal volume step | Product plus account owner               |
| More product surface       | Second product or governance tier | Org-level need appears (SSO, audit, policy); a second use case gets instrumented               | Account owner                            |

Additional account-level triggers worth wiring regardless of vector:

- a reorg or acquisition
- a renewal approaching with usage above or below plan
- a champion changing employer, which is simultaneously a risk in the old account and a warm entry in the new one

## Enterprise blockers

- **No standardization decision.** Team-by-team adoption plateaus until a platform or architecture group makes the tool a default. In large accounts, expansion strategy is mostly about reaching that decision - which means the champion pack has to survive an architecture review, not a hallway chat.
- **Procurement re-entry.** The second, bigger purchase triggers the security review, legal pass, vendor onboarding and sometimes an RFP that the first credit-card purchase skipped. Prepare the paperwork before the expansion conversation, not during it.
- **Champion single point of failure.** Multi-thread: a second technical advocate plus one manager-level contact, both of whom have seen value with their own eyes.
- **Pricing that punishes growth.** If the next unit of adoption produces an unpredictable bill, developers cap their own usage silently and the account flattens for reasons that never reach a report.

## The numbers that prove expansion is real

- **Net revenue retention** - a cohort's MRR today divided by that same cohort's MRR twelve months ago, including expansion, contraction and churn. Above 100% it means the installed base grows without new logos, the only honest headline for a land-and-expand claim. Read the band for the motion you actually run: published 12-month figures put a bottom-up product's "good" at around 100% and "great" at around 120%, against 110% and 130% for enterprise SaaS.
- Share of accounts with more than one active team.
- Time from first paid to first expansion.
- Share of revenue from expansion versus new logos.
- Count of multi-threaded accounts (two or more engaged contacts).
- **Counter-metric:** expansion produced by price increases or usage the customer did not choose is not expansion, it is deferred churn. Track active seats, not provisioned seats, for the same reason.
