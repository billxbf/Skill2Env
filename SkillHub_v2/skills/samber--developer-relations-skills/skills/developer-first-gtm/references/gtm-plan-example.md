# Worked example: a developer-first GTM memo

Contents: a full memo that passes; the same product's failing memo, annotated; weak-versus-strong lines section by section.

The company below is fictional and the numbers are invented - no company publishes a motion memo with real figures. Use it for the _shape_ of each section and for the positive-versus-negative contrast, never as a benchmark. Published figures that _can_ be quoted live in `sourced-benchmarks.md`.

**Context.** Sprocketd is a hosted feature-flag and configuration service. Open-source SDKs, hosted control plane. Roughly 6,000 free accounts, 40 paying, mostly single-team. Two founders, one engineer doing part-time customer work, no sales hire.

---

# Developer-first GTM - Sprocketd

## Table of Contents

- [Constraints](#constraints)
- [Friction gates](#friction-gates)
- [Rejected motions](#rejected-motions)
- [Primary motion](#primary-motion)
- [Entry design](#entry-design)
- [Handoff rule](#handoff-rule)
- [Expansion path](#expansion-path)
- [Leading indicators](#leading-indicators)
- [Refused](#refused)
- [Revisit triggers](#revisit-triggers)
- [The same product's failing memo](#the-same-products-failing-memo)
- [Weak versus strong, section by section](#weak-versus-strong-section-by-section)

## Constraints

Business model is consumption plus an organization tier; the paid boundary is environments, flag-evaluation volume and the governance features (audit log, approvals, SSO). Product friction is low: the SDK works against a hosted sandbox with a key issued instantly, no infrastructure. Response capacity is one engineer for roughly five hours a week - any rule producing more than a handful of conversations a week is fiction.

## Friction gates

- **Entry - pass.** Cold run on a clean machine: docs to first flag evaluated in 6 minutes, four steps, one of them (create account) deferrable behind a sandbox key. Removing it is scheduled.
- **Value - partial.** A single developer sees a flag flip in their own app, which is real value. Approvals, audit and environment separation only matter once a second team exists. Bottom-up is therefore the entry, not the whole motion.
- **Spread - pass, weakly.** The SDK config lands in a shared repo and flag names appear in pull requests, so a second developer usually sees it. But nothing forces an invite; 71% of accounts still have exactly one active developer after 60 days.

## Rejected motions

- **Top-down with developer proof** (rejected): no existing budget line for feature management at our target accounts; the spend today is inside platform-team salaries.
- **Ecosystem-mediated** (premature, not rejected): cloud-marketplace listing is attractive for procurement drawdown, but we have no partner enablement capacity this year. Revisit when a second person can own it.

## Primary motion

Bottom-up self-serve, with developer-influenced sales as the secondary once account rollup ships. Money path: developer adopts in the sandbox → team adopts in staging → production deployment and a second environment cross the volume boundary → card for the team plan, or a conversation for the organization tier.

Prerequisite that must hold: individual developers can pay the team plan without approval. Verified on 14 of the 40 current paying accounts.

## Entry design

First-value moment: **a flag the developer created flips behaviour in their own running application.** Steps to it: 4 today, 3 after the sandbox-key change. Always open, never gated: full documentation, pricing page with real numbers, all limits, the SDK source, and the error/troubleshooting pages.

## Handoff rule

Account rollup from workspace object plus email domain, shipping this quarter.

> An account becomes qualified when it has **3 or more active developers** and **4 weeks of production evaluations**, or when **anyone in it opens the SSO, audit-log or security-questionnaire page**. Qualified accounts are contacted by **the founding engineer** within **48 hours** with **an environment-and-limits review offer**. Accounts below the threshold are **not contacted by a human**.

Thresholds derived from our own data: paying accounts had a median of 3.5 active developers and 5 weeks of production usage before their first payment. Expect roughly 6 qualified accounts a month, which fits the five-hour budget.

Routing: developer gets the limits review; champion gets the enablement pack (internal case, re-runnable rollout benchmark, migration path from the home-grown flags they usually have, risk answers, cost comparison against building it); security gets the questionnaire pack unprompted.

## Expansion path

- Single-team accounts → _more developers, same team_: product-owned, triggered by a second developer appearing; the fix is an invite prompt at the moment a flag is shared, which does not exist yet.
- Multi-team accounts → _more teams, same company_: founder-owned, triggered by a new workspace on a known domain; requires the platform team to standardize, so the pack must survive an architecture review.
- All accounts → _more workload_: product-owned, triggered by first production deploy and by repeated limit hits.

Multi-threading rule: no account above the qualification threshold has fewer than two engaged contacts, one of them manager-level.

## Leading indicators

| Indicator                                      | Today                            | Target                   | By        |
| ---------------------------------------------- | -------------------------------- | ------------------------ | --------- |
| Accounts reaching first value in first session | 38%                              | 55%                      | end of Q3 |
| Accounts with 2+ active developers at day 60   | 29%                              | 45%                      | end of Q4 |
| Qualified accounts contacted within 48h        | not measured                     | 90%                      | end of Q3 |
| Cohort account free-to-paid at 90 days         | 0.7%                             | 1.5%                     | end of Q4 |
| Net revenue retention                          | not measurable yet (n too small) | report from Q1 next year | -         |

## Refused

No outbound to accounts below the threshold. No gated documentation, pricing or limits. No enterprise-only tier without a self-serve team plan underneath it. No paid tier for basic authentication hardening.

## Revisit triggers

A cloud provider ships a competing managed feature-flag service; qualified-account volume exceeds 15 a month (needs a dedicated responder); day-60 multi-developer share stays below 35% two quarters running (the spread mechanic is the problem, not the funnel); first partner offers co-selling.

---

## The same product's failing memo

This version reads well in a board deck and cannot be executed. Every line below is a real pattern, not a strawman; the annotation says what breaks.

> ## Motion
>
> Sprocketd runs a **PLG motion** with an enterprise sales layer for larger accounts. We will also pursue cloud marketplace and partner channels opportunistically.

Three motions declared as one, no rejection stated, so every one of them gets re-proposed next quarter. "Opportunistically" is how a motion with no owner is written down.

> ## Conversion
>
> Our free-to-paid conversion is 0.7% against an industry benchmark of 3-5%, so conversion is our top priority for the year.

The benchmark is real but it is the wrong row: developer-focused companies convert at a 5% median, half of everyone else, and the 3-5% band assumes account-level cohort measurement over six months. This memo compares a lifetime user-level ratio against a cohort account-level band and concludes the funnel is broken. The number that matters - 71% of accounts still have one developer at day 60 - is a spread problem, and it is not in the memo at all.

> ## Qualification
>
> Sales reaches out to high-intent users. We score leads on pricing-page visits, docs visits, email opens and signup recency, and route anything above 60 points.

Users, not accounts: forty sign-ups from one bank become forty leads and forty emails. The signals are marketing exposure rather than product usage, which is the MQL construction wearing a PQL label. No owner, no response window, and no statement of who is deliberately never contacted - so in practice everyone is.

> ## Expansion
>
> Land and expand. Once we have a foothold we grow the account through quarterly business reviews and upsell conversations at renewal.

No vector, so nobody can tell whether this account grows by seats, teams, workload or surface - and those need different owners. Triggers are calendar-driven, which means the conversation happens when the contract says so rather than when the account does something.

> ## Hiring
>
> We will hire two AEs in Q1 to capture the enterprise demand we know is there.

Never tested against the 4x fully-loaded-cost bar, and the current account base is majority single-developer. The reps arrive, find nothing to work, and start emailing sign-ups - which damages the free surface the whole motion depends on.

> ## Metrics
>
> Signups, MAU, ARR, and NPS.

All four are lagging or unactionable. None of them moves before revenue, so nothing here can tell the team the motion is failing while there is still time to change it.

---

## Weak versus strong, section by section

**Motion choice**

- Weak: "We'll run a PLG motion with a sales-assisted layer for enterprise."
- Strong: names the money path, the prerequisite verified against real accounts, and what was rejected and why.

**Entry design**

- Weak: "Improve onboarding and reduce time to value."
- Strong: names the first-value event, counts the mandatory steps, and states what stays ungated forever.

**Handoff rule**

- Weak: "Sales follows up with high-intent users."
- Strong: one sentence with numbers derived from own data, an owner, a response window, a technical offer, and an explicit do-not-contact line.

**Expansion**

- Weak: "Land and expand into the enterprise."
- Strong: a vector per account segment, a trigger that fires on an observed event, an owner, and a multi-threading rule.

**Indicators**

- Weak: "Track signups, MAU and revenue."
- Strong: a small set that moves before revenue, each with a current value, a target and a date - plus an honest "not measurable yet" where the sample is too small.
