# Worked Examples

Two filled specs (one B2C, one B2B) and one negative example. Thresholds tagged [illustrative] are defaults to replace with baselines derived from the program's own data; they are program-specific, never transferable.

## Example 1 - B2C meal-kit subscription (positive)

Context: $25/$25 double-sided credit, 30-day refund policy, payment instrument collected at first order, ~2,000 referrals/month.

```
REFERRAL GUARDRAIL SPEC - meal-kit refer-a-friend, 2026-08
Qualifying event : referrer credit fires when the referee's SECOND paid box is delivered
                   (paid + physically delivered = costly to fake; second box survives
                   one-box-and-refund farming). Referee discount stays on first box.
Caps             : 12 rewards/referrer/year, $300 lifetime [economic cap, kept under the
                   $600 US tax-reporting line - rises to $2,000 for tax year 2026];
                   program ceiling $60,000/month [budget decision]
Velocity         : flag >5 successful referrals/referrer/7 days [illustrative - replace
                   with p99 of legitimate referrers within 60 days]; cooldown, not ban,
                   on first breach
Hold policy      : 35 days = 30-day refund window + 5 processing; reward shown as
                   "pending - releases <date>" from day one
Eligibility      : referee is new if no prior order matches payment instrument OR
                   delivery address; referrer's own household excluded; referee ineligible
                   if referred by anyone in prior 12 months [copied from published
                   program precedent]; no stacking with other promos [published clause]
Verification     : email double opt-in + disposable-domain block for all; payment
                   instrument arrives with the qualifying event anyway; no phone gate
                   (friction unjustified at $25), no KYC
Monitoring       : payment-instrument reuse (tier 1, deterministic), similar-email check,
                   referred-vs-organic cohort dashboard (retention, refund rate, 90-day
                   revenue) by referrer decile; expected flag baseline 1-2.5% of devices
                   [vendor claim, other-market scope - sanity anchor only]
Enforcement      : (1) withhold with reason string, (2) 30-day link pause, (3) program
                   removal after 2 confirmed violations, (4) clawback only for confirmed
                   self-referral, never the referee's discount; appeal in every denial
                   message, human-reviewed, 14-day SLA
Terms status     : caps, eligibility, hold, and all 4 rungs added to published terms
                   BEFORE launch; existing earned rewards grandfathered
Calibration      : 5% holdout cell with velocity flag off and 20-reward cap; compare
                   90-day cohort value per 1,000 exposed referrers at day 90; loosen if the
                   strict cell trails the holdout on that basis, or if leakage saved is less
                   than friction cost incurred on the same exposure base
```

## Example 2 - B2B SaaS (positive)

Context: $500 company-account credit per referred workspace converting to a paid annual plan, ~15 referrals/month, sales-assisted.

```
REFERRAL GUARDRAIL SPEC - B2B workspace referrals, 2026-08
Qualifying event : credit fires when the referee's SECOND monthly invoice is paid
                   (survives the refund window and trial churn)
Caps             : 10 rewards/referring company/year; program ceiling $15,000/quarter
Velocity         : any referrer >2 conversions/month goes to review [illustrative]
Hold policy      : release after second paid invoice; no separate timer needed -
                   the qualifying event IS the hold
Eligibility      : domain-overlap check between referrer and referee (admin contacts,
                   billing entity, payment instrument) - the check that matters; work-email
                   requirement kept but treated as weak (a shell has a real domain);
                   referee rejected if already in pipeline or trial before the referral
                   timestamp (routing, not referring)
Verification     : billing-entity verification via the payment method already collected;
                   no individual identity checks
Review           : pre-payout human review of EVERY reward - ~$30 review cost vs $500
                   reward is ROI-positive in B2B (and would not be at B2C values)
Reward routing   : company-account credit by default; individual gift opt-in requires
                   named approval from the referrer's company (procurement/gift-policy
                   exposure precedes fraud exposure); regulated-sector referrals routed
                   to counsel before payout
Enforcement      : withhold-with-reason → program removal → clawback via credit reversal;
                   every rung in the published program terms; appeals to a named human
Terms status     : published on the program page; sales team briefed on the pipeline rule
Calibration      : with ~15/month, holdout cells lack power - instead audit 100% of
                   rewards quarterly against CRM outcomes and track referred-account
                   12-month retention vs sales-sourced accounts
```

Note what is identical to B2C - caps, budget ceiling, hold-covers-refund-risk, eligibility memory, published rungs - and what diverged: domain overlap, pipeline check, universal pre-payout review, company-credit routing.

## Example 3 - fitness app referral program (negative: what not to do)

Context: $10/$10 credit. Every line below is a real failure mode; do none of this.

- **Full ID-document verification for every referred signup**, justified internally by "referral fraud is 21% of ecommerce fraud". Defects: the statistic is circular vendor citation [unverified - do not use], and document upload alone drops 15-30% of legitimate signups [vendor claim] to protect a $10 credit. Fix: stop the ladder at email + disposable-domain checks; the payment instrument arrives at subscription anyway.
- **Silent removal of "suspicious" rewards.** No reason, no appeal. Defects: support tickets, churn of wrongly flagged users, and a deception/consumer-protection exposure in several regimes. Fix: reason string + appeal path, built first.
- **14-day hold against a 30-day refund window.** Theatre: the farmer refunds on day 20, reward already paid. Fix: hold = 30 + processing.
- **A cap added mid-program and applied to already-earned rewards.** Retroactive tightening - unenforceable against past referrals and the exact behavior regulators name. Fix: publish first, grandfather earned rewards.
- **Top referrer banned as a "ring" on IP clustering alone.** She runs a gym; members share the gym Wi-Fi. IP is the weakest signal and households/venues share IPs by construction; the enthusiastic advocate is the known false-positive mode of cluster detection.
  - Fix: corroborate with payment-instrument reuse, refund clustering, and her cohort's quality - which was excellent.
  - Result of the ban: the program's best advocate now posts about it.
- **No budget ceiling.** The month the program went viral on a coupon forum, spend was unbounded. Fix: program-level monthly ceiling converts incidents from unbounded to bounded.
