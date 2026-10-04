# Partner Types, Tiers, and Rate Migration

## Incrementality-driven rate differentiation

A single flat rate treats every click as equally valuable, but incrementality data says otherwise (New Engen incrementality analyses, cited across 2026 industry coverage - vendor research, practitioner consensus):

- Content/creator partners: ~78-82% incremental - they create demand.
- Coupon/cashback/loyalty partners: often 66-71% NON-incremental - they capture last-click credit on demand others created, and cashback sites rebate 30-70% of the commission to the shopper.
- One audit found 81% of a DTC brand's affiliate revenue was non-incremental bottom-funnel, with ~20% linked to suspected fraud.

Four controls stop the overpayment. Rank them by cost removed per unit of friction, not by ease:

- efficiency: new-customer gate > rate cap > shorter attribution window > exclusive codes
- value: new-customer gate > exclusive codes > rate cap > shorter window - the gate removes payment on repeat buyers outright, and codes are the only control that produces evidence rather than just savings
- effort: exclusive codes > new-customer gate > rate cap == shorter attribution window - the last two tie because each is one rate-card field on the same screen, and codes take an hour per partner to issue and then a standing job to reconcile redemptions against the platform
- compliance cost: rate cap > new-customer gate == shorter window > exclusive codes - only the cap is a decrease on published terms, so it triggers the network rules and notice periods below, while the others narrow eligibility going forward

1. **Gate bottom-funnel partners to new customers only.** Biggest single removal. Requires a new-customer flag in tracking - without one this control is deleted from the menu until the flag ships, and the rate cap moves to first.
2. **Cap coupon/cashback/loyalty rates below content/creator rates.** One rate row per partner type. On a live card, give notice.
3. **Tighten their attribution window** (24 hours-7 days) versus content partners' standard window.
4. **Use exclusive codes per partner to measure lift directly.** Slowest and most administrative, but it is what turns the other three from assumptions into decisions - run it alongside them, not instead.

Separate control, different partner type: pay agencies/consultants and resellers on the recurring/rev-share end - they influence retention, not just the click.

**The 30-day holdout test**: pause your top 3 coupon partners for 30 days.

- If overall conversion volume holds flat while affiliate-attributed volume drops, they were harvesting existing demand: keep their rates capped.
- If total volume drops, they were incremental after all: restore and document.

Run this before and after any rate rebalancing, identically for B2B and B2C.

## Concentration: plan for the power law

Prussakov's "5/80 rule": 5% of affiliates drive 80% of the work. Telemetry agrees: the top 10% of revenue-generating affiliates produce 58.5% of referred revenue in the median program (FirstPromoter, 2026, 31M-referral dataset), and roughly 10% of affiliates generate a program's total revenue (Rewardful, 2026). Design the rate card for the head, not the long tail - custom rates for top partners matter more than the public headline.

Top-partner instruments, ranked by what they buy per unit of setup and negotiation:

- efficiency: milestone bonus > longer cookie window > private offer > invite-only tier > hybrid placement fee
- value: hybrid placement fee > private offer > invite-only tier > milestone bonus > longer cookie window - the fee is the only instrument that lands a publisher refusing pure performance, which is why it survives its effort
- effort: hybrid placement fee > invite-only tier > private offer == milestone bonus == longer cookie window - the last three tie because each is one field on that partner's record, while the tier needs eligibility rules administered every cycle, the fee needs a negotiation and off-platform invoicing
- compliance cost: hybrid placement fee > private offer > invite-only tier > milestone bonus == longer cookie window - a placement fee is a signed contract with a fixed term, and a private offer is close to irreversible in practice, since withdrawing one costs the relationship it bought

1. **Milestone bonus tied to new-customer revenue** (not gross) - pays only on the outcome, so it cannot exceed the ceiling by surprise.
2. **A longer cookie window as a negotiated perk** - one field, no extra commission rate. Watch that it does not quietly increase last-click capture on demand the partner did not create.
3. **A private offer above the public card** - one rate row, but treat it as permanent for that partner.
4. **An invite-only tier above the public ladder** - buys status, which travels further than money with a handful of partners, at the price of standing eligibility administration.
5. **Hybrid flat-placement-fee + lower percentage** - reserve it for the publisher who will not work on performance at all. Delete it from the menu when no such publisher is in the conversation.

Derive every custom rate from that partner's incremental value. Review the rate card quarterly to stop commission creep.

## Tier design mechanics

Whether to tier at all comes first: `flat > marginal tiers > retroactive tiers` on efficiency. No historical performance data deletes both tiered options - there is nowhere to place a breakpoint - so launch flat and revisit.

**Marginal vs retroactive.** Marginal pays the higher rate only on volume above the threshold. Retroactive pays it back to dollar one for the whole period.

- efficiency: marginal > retroactive
- value (motivation per partner): retroactive > marginal - the cliff is exactly what makes it pull harder
- cost: retroactive > marginal, and unforecastable rather than merely higher, since a partner crossing a breakpoint repriced their whole period
- compliance cost: retroactive > marginal - a tier a partner has earned cannot be taken back, so never cap retroactively - clawing one back destroys trust faster than any rate cut

The cliff also invites junk volume: a partner at 49 of 50 conversions has a strong incentive to push one low-quality sign-up over the line. Marginal is the default for that reason, not just the cheaper one.

**Measurement window** - `quarterly > rolling > monthly` on efficiency:

- quarterly smooths variance and needs one reset cadence to administer - the safest default
- rolling stays fairest in evergreen programs, but recomputes every partner's position continuously - a standing job wherever the platform cannot express it natively
- monthly creates the most urgency and the most breakpoint-gaming, and pays the administration cost twelve times a year instead of four

- Set breakpoints from historical performance: first tier reachable by ~70-80% of active partners, and top tier reserved for the top 10-20%.
- Threshold metric: prefer new-customer revenue over revenue, and revenue over referral count - each step further from new-customer revenue rewards more harvested volume, and all three cost the same to configure.
- When restructuring tiers: grandfather high performers for at least one cycle, and give 60 days notice.
- Documented SaaS tier examples:
  - Homesage.ai: 25%/30%/40% (Starter/Growth/Elite)
  - Pipedrive: 20% rising to 33% top tier
  - beehiiv: Launch/Bronze/Silver/Gold ladder

Tier mechanics are identical for B2B and B2C: only the threshold metric differs (customers or MRR vs orders or GMV).

## Rate migration guardrails

Sequence for changing a live rate card (in addition to the SKILL.md migration workflow):

1. Derive the target structure before announcing anything.
2. Lead with what stays the same. Announce top-partners-first with direct conversations, then broadcast.
3. Grandfather existing affiliates at the old rate, especially high performers for at least one cycle.
4. Provide a named contact and a one-page summary of the change.

Network guardrails are contractual, not courtesy. Awin's published rule on commission decreases, verbatim: "Maximum 20% reduction each time. Can only be done once every 30 days. Partners must be notified at least 7 days prior to the change."

Other documented norms:

- A 4-8 week migration with tiered partner communication and conversion de-duplication during parallel running (impact.com guidance).
- 4 weeks publisher notice before zeroing commission on an old network (DMi Partners).
- TikTok Shop locks a creator's rate for 30 days after they start promoting, regardless of seller decreases.

Fraud note (scope boundary): tier cliffs, retroactive tiers, and high flat CPAs each create incentives for junk volume, self-referrals, and cookie stuffing. Flag the incentive in the spec. The detection ruleset itself belongs to `mbfinotti/partnerships-skills@affiliate-fraud-detection`.
