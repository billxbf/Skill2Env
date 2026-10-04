# Guardrail Mechanics

The control ladder, ordered by leverage per unit of friction. Vendor blogs present this order backwards - detection tooling first, program design last. Work top-down: each rung makes the next one cheaper.

- efficiency: `event > caps == hold > eligibility > verification > review`
- value: `event > eligibility > hold > verification > caps > review`
- effort: `review > event > verification > eligibility > caps == hold`
- compliance cost: `verification > eligibility > event == caps == hold > review`

Caps and hold tie because each is a payout-side number published in terms, shipped in one config change, gating no legitimate user, and each bounds a loss the other cannot - caps bound volume, hold bounds reversal. Event, caps and hold tie on compliance cost because none touches identity data or needs sign-off. Review sits lowest on that axis because a human in the loop reduces exposure rather than adding it.

Effort is composite: friction charged to legitimate users, build time, reversibility. Event design ranks high on it - rewiring the trigger is a quarter of product and billing work - yet still leads on efficiency, because that cost is one-time engineering while verification charges every legitimate signup forever. Caps and hold are near-zero on both build and friction; manual review is a standing job that never ends.

Default: caps, hold, and published eligibility first, always. Climb to event redesign the moment the qualifying event is bare signup or an unpaid action.

The order starves verification and review - high value against automated account farming and B2B shell entities, losing every efficiency round; promote them when per-item review cost sits below the reward value, or when an incident is confirmed automated rather than opportunistic. Treat this as a default, not a law: it shifts with context and with who executes it, so re-rank against the program's own answers before writing the spec.

Provenance tags:

- `[published terms]` - a program's own published rules.
- `[academic]` - peer-reviewed work.
- `[vendor claim]` - published by a party selling the remedy.
- `[verified]` - regulator/court filing or multiple independent reports.
- `[derive from own data]` - program-specific; compute the baseline from the program's own history rather than copying a number.

## Table of Contents

- [1. Qualifying-event design (highest leverage, near-zero friction)](#1-qualifying-event-design-highest-leverage-near-zero-friction)
- [2. Caps, budget ceilings, velocity, cooldowns](#2-caps-budget-ceilings-velocity-cooldowns)
- [3. Hold and validation windows](#3-hold-and-validation-windows)
- [4. Eligibility rules with memory](#4-eligibility-rules-with-memory)
- [5. Verification gates - the friction ladder](#5-verification-gates---the-friction-ladder)
- [6. Manual review (last, and scoped)](#6-manual-review-last-and-scoped)
- [B2B specifics](#b2b-specifics)

## 1. Qualifying-event design (highest leverage, near-zero friction)

Move the reward trigger as late as the business model tolerates, onto an event that is costly to fake and hard to reverse.

Published examples [published terms]:

- Dropbox: referee must accept the invite, install the desktop app, sign in from it, and verify email - four steps, none of them identity checks; the desktop install is expensive to fake at scale.
- Expedia: referee must create an account, book, and _complete the travel_ - close to unfalsifiable.
- Gemini (regulated): sign-up, ID verification, and $100 traded within 30 days; unverified accounts explicitly ineligible.

Design rule: if the current event is bare signup or an unpaid action, recommend moving it to a paid, delivered, or usage-verified milestone before writing any other rule. Requiring a payment instrument by the qualifying event also delivers the strongest detection signal for free.

## 2. Caps, budget ceilings, velocity, cooldowns

Published cap values [published terms]:

| Program              | Cap type                | Value                  |
| -------------------- | ----------------------- | ---------------------- |
| Dropbox              | Lifetime referral count | 32                     |
| Expedia              | Annual reward count     | 10 per year            |
| Robinhood Crypto     | Per-promotion count     | 5                      |
| Crypto.com App       | Lifetime value          | $10,000                |
| Constellation Energy | Annual value            | $575 per calendar year |
| HealthExpress (UK)   | Annual value            | £3,000 per customer    |

Two honest notes on caps:

- The $575 annual value is a tax-operations decision disguised as a fraud control: US referral rewards are generally taxable service income with issuer reporting at $600+, a threshold rising to $2,000 for tax year 2026 [verified from published tax guidance]. US programs anchored just under $600 should revisit.
- The usual real reason for caps is economic (an uncapped program cannibalizes paid upgrades), not anti-fraud. Say so; it changes where the cap sits.

Budget ceiling: a program-level maximum reward count or currency value per month/year across all campaigns [vendor capability, published docs]. Always set one - it converts a worst-case incident from unbounded to bounded.

Velocity and cooldowns: no referral-specific public numeric threshold exists, and this is domain fact rather than a research gap - fraud-tooling vendors publish starting-point conventions for the adjacent problem of batch account-registration fraud instead (SEON: flag over 3 registrations per device ID within 60 minutes; over 5 accounts per IP subnet within 24 hours). Treat these as a labeled adjacent-domain starting point for a program with no history yet, never as a referral-specific sourced fact - derive the real threshold from the legitimate-referrer distribution (e.g. flag beyond p95-p99 of weekly referral claims) [derive from own data] as soon as any history exists.

Pair every cap with a per-window velocity limit: a lifetime cap without one can be exhausted in a weekend. Add a cooldown after a flagged burst rather than a ban - it preserves the false-positive case.

## 3. Hold and validation windows

Set the hold to the actual refund/chargeback window plus processing time, never a round number. A 30-day hold on a product with a 60-day return policy is theatre.

Published anchors: a 30-day post-grant hold [published terms, brokerage], 2-4 weeks processing after enrollment [published terms, energy]. A vendor rule of thumb matches the return-policy window (7-30 days retail) timed to when 70-80% of returns have occurred [vendor claim] - use the full window when margins allow.

Show rewards in a visible pending state during the hold; a silent gap reads as denial.

## 4. Eligibility rules with memory

- New-customer definition beyond email match: no prior order on the payment instrument, delivery address, or account cluster - email alone is trivially rotated.
- Self and household exclusion, stated in terms. One published program excludes the referrer's own household and any referee who received a link from _anyone_ in the prior 12 months [published terms] - that cross-referrer cooldown kills ring re-farming of the same referee without touching genuine one-off referrals; copy it.
- Once-per-lifetime and long-cooldown rules are the discipline transferred from card issuers (once per product lifetime; once per 48 months; application-count windows) [published terms]. These transfer cleanly to any program because they are memory, not friction.

## 5. Verification gates - the friction ladder

Climb only as far as the reward value justifies. Rank the rungs before picking one:

- efficiency: `email opt-in == disposable-domain > payment instrument > phone/SMS > KYC`
- value: `KYC > payment instrument > phone/SMS > email opt-in == disposable-domain`
- effort: `KYC > payment instrument > phone/SMS > email opt-in == disposable-domain`
- compliance cost: `KYC > phone/SMS > payment instrument > email opt-in == disposable-domain`

- Email opt-in and disposable-domain blocking tie on every axis: both are a one-time config on the signup flow, both stop bots and neither touches a motivated abuser, and each blocks the half of automated farming the other misses.
- KYC leads on value and loses on efficiency by the widest margin on this page: severe friction, document retention and liveness data to hold, and a decision you cannot reverse once collected.
- Phone/SMS outranks payment instrument on compliance cost because a number carries messaging-consent rules; the $9M settlement in the abuse-patterns reference came from a share flow, not from fraud.

Re-rank on what the program already has:

- Where payment is collected before the qualifying event, the payment-instrument rung's effort collapses to zero and it takes the top spot outright - the strongest available gate, already paid for.
- Where the program is regulated, identity verification is already law-required, so its rung costs nothing at the margin.

The starved rungs are phone/SMS and KYC. Promote phone/SMS on confirmed automated account creation at a volume the cheap rungs demonstrably fail to stop; promote KYC only under a regulatory requirement, never as a fraud control.

Delete a ruled-out rung from the spec rather than listing it as rejected. A non-regulated program deletes the KYC row outright and records the deletion as one clause on the Verification line ("KYC deleted - non-regulated program"); a rung parked at the bottom of a table reappears as scope the first time an incident makes someone nervous.

| Gate                         | Abuse resistance                      | Friction                        | Use it?                                         |
| ---------------------------- | ------------------------------------- | ------------------------------- | ----------------------------------------------- |
| Email double opt-in          | Low vs motivated abuser, high vs bots | Near zero                       | Always                                          |
| Disposable-domain blocking   | Low-moderate                          | Near zero, rare false positives | Always                                          |
| Payment instrument on file   | High - scarce, costly to rotate       | Moderate; kills tyre-kickers    | Yes when payment is already in the flow         |
| Phone/SMS verification       | Moderate                              | Small, plus per-message cost    | Usually                                         |
| Full KYC document + liveness | Very high                             | Severe                          | Delete the rung unless the program is regulated |

The KYC verdict is evidence-based, not taste: 63% of surveyed European consumers abandoned a financial-services sign-up over cumbersome identity verification [vendor claim citing a named third-party survey]. Abandonment ranges ~25% to 60%+ by brand familiarity, with document upload the single biggest drop at 15-30% [vendor claim].

A regulated firm eats that cost because law requires it; imposing it to protect a $10 credit trades a large certain loss for a small uncertain one. What does transfer from regulated programs: eligibility memory, payment-instrument-as-identity, staged payout, and clawback tied to account-open duration (3-6 month clauses in published card terms) [published terms].

## 6. Manual review (last, and scoped)

A queue whose per-item review cost exceeds the reward value is a net loss no matter how accurate. B2C: exception path only, for flags above a value threshold. B2B: pre-payout human review of every reward is the ROI-positive default [vendor claim, consistent with the loss shape - few, large rewards].

Escalation-style triage (auto-approve / hold-for-review / reject with reason) beats binary blocking.

## B2B specifics

These stay the same across contexts: caps, budget ceilings, hold-equals-refund-window, eligibility memory, published enforcement. B2B diverges on three abuse controls plus one routing default.

- efficiency: `domain overlap > pipeline check > pre-payout review`
- effort: `pre-payout review > domain overlap == pipeline check`

Domain overlap and the pipeline check tie on effort - each is a single join against data the CRM and billing system already hold, built once and run automatically - while review is a standing per-deal human cost. Company-account credit sits off the efficiency axis entirely: it is a compliance control, not an abuse control, and it lowers exposure rather than buying detection, so ship it regardless of rank.

B2B diverges on:

- **Domain overlap is the check that matters.** Compare referrer and referee domains, billing entities, and admin contacts. A work-email requirement alone stops disposable-address farming but not the two highest-value B2B abuses: the shell company with a real domain, and the cross-company employee split.
- **Pipeline check.** Reject referrals of accounts already in the sales pipeline or trial before the referral timestamp - that is routing, not referring.
- **Company-account credit by default.** Paying an individual employee to influence a purchase is a procurement/gift-policy problem before it is a fraud problem, and in regulated sectors (healthcare, real-estate settlement) referral payments can be unlawful [verified as to the statutes existing; application is a question for counsel]. Offer individual rewards only as an opt-in the referrer's employer can veto.
- **Pre-payout review** of every reward, as above.
