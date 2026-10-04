# Worked Sequence Plans

Two complete artifacts in the deliverable format - one B2C ecommerce, one B2B SaaS. Adapt the reasoning, not the literal day numbers.

## Table of Contents

- [Example 1 - B2C ecommerce (skincare DTC brand)](#example-1---b2c-ecommerce-skincare-dtc-brand)
- [Example 2 - B2B SaaS (compliance-automation platform)](#example-2---b2b-saas-compliance-automation-platform)
- [Negative example - the welcome dump](#negative-example---the-welcome-dump)

## Example 1 - B2C ecommerce (skincare DTC brand)

Context from the interview:

- B2C, activated = first tracked sale within 30 days.
- 12% one-time commission, 60-day cookie, $50 payout threshold, net-30 hold.
- Intake is coupon-deal sites, social creators, and email-list owners.
- Links + codes auto-provisioned, postback live.
- Tax form gates payout.
- Automated sender, no AM capacity.
- ~150 approvals/month.

```
SEQUENCE PLAN - GlowKit Affiliates, 2026-08
Activation       : first tracked sale within 30 days of approval
Routing          : coupon-deal -> self-serve | social creator -> self-serve
                   email-list owner -> self-serve; 150/mo, no AM => no high-touch tier
Touches          :
  T1 Trigger : approval (within minutes)
     Channel : email  Sender : automated program address
     Action  : copy your link/code (both in the first two lines)
     Content : approval confirmed; commission, cookie, payout terms; disclosure
               attestation; what arrives next; under 300 words
     Asset   : pre-coded link + unique coupon code
  T2 Trigger : day 2
     Channel : email  Sender : automated
     Action  : grab the one asset for your archetype
     Content : coupon sites -> code page template; creators -> caption pack +
               disclosure line; list owners -> ready-cut email
     Asset   : asset hub, deep-linked per archetype
  T3 Trigger : first click (behavior; overrides calendar)
     Channel : email  Sender : automated
     Action  : place the code where that traffic came from
     Content : celebration + top-converting page for their traffic source
     Asset   : best-converting-pages one-sheet
  T4 Trigger : no click by day 10 (behavior)
     Channel : email  Sender : automated
     Action  : send one ready-cut email / publish one post (30-minute job)
     Content : lowest-effort promo, pre-written, link pre-coded
     Asset   : swipe copy
  T5 Trigger : day 21, only if not activated
     Channel : email  Sender : automated
     Action  : make one sale by day 30
     Content : activation bonus - extra $25 on the first sale before the window
               closes (deadline-bound; rate design per the commission skill)
     Asset   : reminder of code + link
  T6 Trigger : first sale (behavior)
     Channel : email  Sender : automated
     Action  : none - celebrate; state when commission approves (after the
               30-day return window) and pays (net-30)
Activation nudge : $25 first-sale bonus, expires day 30, carried by T5
Never-activated  : entry = no click and no sale by day 30; re-engagement at day
                   45 (one incentive + one asset); final notice at month 6 -
                   "account archived unless you reply"; then suppress, not delete
KPIs             : 30-day activation rate | median time-to-first-sale |
                   never-activated share at day 30 | open/click per touch
```

Why it holds:

- Every touch asks one action.
- The link leads touch 1.
- T3/T4 are behavior-driven, so stuck and gone get different messages.
- Payout terms and gating are stated on day 0, not at first commission.

## Example 2 - B2B SaaS (compliance-automation platform)

Context from the interview:

- B2B, activated = first qualified referral (demo booked and accepted) within 90 days.
- 25% recurring commission for 12 months, 90-day cookie, deal registration in place.
- Intake is consultants, agencies, and two tech partners.
- Named partner manager with call capacity.
- ~15 approvals/month.

```
SEQUENCE PLAN - CompliCo Partners, 2026-08
Activation       : first qualified referral (accepted demo) within 90 days
Routing          : consultant -> hybrid | agency -> high-touch
                   tech partner -> high-touch; 15/mo with named PM => calls viable
Touches          :
  T1 Trigger : approval (within minutes)
     Channel : email  Sender : named partner manager
     Action  : book your kickoff call (high-touch) / log in and register a
               deal (hybrid)
     Content : approval, terms + disclosure attestation, commission and
               clawback terms, tax/payout setup link (gates payout)
     Asset   : portal credentials + deal-registration link
  T2 Trigger : day 1
     Channel : in-portal + email  Sender : automated
     Action  : activate your sandbox account
     Content : sandbox/NFR access, integration docs for tech partners
     Asset   : sandbox credentials
  T3 Trigger : kickoff call booked (behavior) - else day 7 reminder
     Channel : call  Sender : partner manager
     Action  : agree the activation plan - first-deal date, next-step owners
     Content : terms recap, targets, product walkthrough, promo-calendar slot
     Asset   : sales deck + comparison/buyer-question material
  T4 Trigger : certification completed (behavior) - certification exists as a
               touch; its curriculum belongs to the enablement skill
     Channel : email  Sender : automated
     Action  : register your first deal
     Content : celebration + deal-registration walkthrough
  T5 Trigger : no deal registered by day 45 (behavior)
     Channel : email  Sender : partner manager
     Action  : reply with the one account you'd pitch first
     Content : personal check-in; offer co-pitch help; one concrete next step
  T6 Trigger : day 75, only if not activated
     Channel : email  Sender : partner manager
     Action  : register a qualified referral by day 90
     Content : time-boxed ramp incentive (economics per the commission skill)
  T7 Trigger : first qualified referral (behavior)
     Channel : email  Sender : partner manager
     Action  : none - celebrate; explain pending -> approved commission flow
               and the 12-month recurring window
Activation nudge : ramp incentive, expires day 90, carried by T6
Never-activated  : entry = no registered deal by day 90; one re-engagement at
                   day 120 (new use-case angle + offer to co-sell); final
                   notice at month 6; archive, keep door open
KPIs             : 90-day activation rate | median time-to-first-referral |
                   never-activated share at day 90 | call-booked rate | per-touch engagement
```

Why it holds:

- The window (90 days) matches B2B deal physics instead of importing the B2C 30-day cutoff.
- Sandbox and deal registration are provisioned day 0.
- Calendar touches only fire when behavior hasn't.
- The clawback-aware payout explanation arrives with the first success, when the partner actually cares.

## Negative example - the welcome dump

One email at approval containing: login, link, code, 14 banners, the full terms PDF, tax form, brand guidelines, a certification invite, and "let us know if you have questions" - then silence. No single action, the link below the fold, no follow-up branch, no deadline. This is the most common real-world shape and the one the plan above exists to replace.
