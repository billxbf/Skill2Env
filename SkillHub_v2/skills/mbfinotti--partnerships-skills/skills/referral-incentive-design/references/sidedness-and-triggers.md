# Sidedness and Payout Triggers

Who gets rewarded, how the split works, and when the payout fires.

## Sidedness: the evidence, honestly stated

The founding taxonomy is **Reward-Me / Reward-You / Reward-Both** (Ryu & Feick, "A Penny for Your Thoughts", _Journal of Marketing_ 2007) - the academic origin of the industry's "sidedness" vocabulary. Its contingency findings still drive the decision:

- Rewards raise referral likelihood most for **weak ties and weaker brands** (strong ties to a strong brand refer without payment).
- For weak ties / weaker brands, rewarding the **referrer** matters most; for strong ties / strong brands, directing at least part of the reward to the **recipient** works better.

Three later results sharpen this:

| Finding                                                                                                                                                                                                                                            | Evidence                                                                                   | Design implication                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| Recipient-only rewards matched double-sided rewards costing **twice as much**; referrers were about equally likely to share either way, and the friend - who has the harder job (actually signing up and paying) - responds to their own incentive | Gershon, Cryder & John, _Journal of Marketing Research_ 2020, field experiments            | Seriously test the friend-only arm; most programs over-invest in the referrer side           |
| Prosocial splits (equal, or generous-to-friend) beat selfish (referrer-takes-all) schemes                                                                                                                                                          | Jain et al., _Journal of Management Information Systems_ 2021, randomized field experiment | If double-sided, split evenly or tilt toward the friend                                      |
| Exception: referrer-side material rewards regain power when the referral **process is high-effort**                                                                                                                                                | Baylor Keller Center synthesis of 8 studies                                                | If sharing takes real work, pay the referrer for it - but first ask why sharing is that hard |

There is a genuine practitioner-vs-researcher tension worth surfacing to the user rather than hiding: prominent growth operators hold that the referrer's motivation is the primary lever, while the field-experimental evidence says the recipient's reward does more work. The honest recommendation is to run all three arms (referrer-only, friend-only, both) on a small share of the base - sidedness tests are cheap and this question is genuinely unsettled.

### The efficiency order

- **efficiency**: friend-only > double-sided > referrer-only

Effort is identical across the three arms - the same payout rail, the same terms page, one recipient or two - so the efficiency order collapses onto the value order in the table above, where recipient-only rewards matched double-sided programs costing twice as much.

**Default rung**: friend-only, headline written to the friend ("Give your friend X"), referrer payout kept out of that headline. Altruistic framing beat self-interested framing in a large marketplace's own global A/B test.

**Move to double-sided** when any of three conditions holds:

- The product is new or innovative: a visible referrer reward taints the recommendation, and rewarding both sides is one of the documented fixes.
- The brand is weak and the ties are weak (Ryu & Feick: the referrer's reward does the work there).
- You are running the three-arm test and want both-sides as the control.

**Move to referrer-only** only when the referral process is genuinely high-effort - a personal introduction, a demo the referrer sits in on. First ask why sharing is that hard; fixing the friction usually beats paying for it.

This ordering is a default, not a law. It rests on consumer-side field experiments, so downgrade your confidence for B2B. Re-rank it against anything you already know about this user's base - a brand nobody has heard of, or a referral flow that takes real work, moves the order before the evidence does.

## Asymmetric splits

Symmetric "Give $X, Get $X" is the default because it is easy to say and feels fair. The three tilts below are not competing options to rank: each fires on a different fact about the product, and at most one is true at a time. Break symmetry deliberately when the two sides have different jobs:

- **Tilt toward the friend** when the conversion barrier is high (expensive product, long commitment) - their reward subsidizes the hard action.
- **Tilt toward the referrer** when advocacy itself is costly (a personal introduction, a high-effort process), or when the referrer will never buy again (give them cash-equivalent, give the friend the discount).
- **Pay more for the scarcer side of a marketplace**: reward supply-side referrals (a new host, a new seller) several times more than demand-side ones.

## Disclosure

Whether the friend can see the referrer's reward changes behavior. Both options cost the same to implement and the evidence points both ways, so ranking them would be false precision - decide per context instead. Disclosing the referrer's reward can _increase_ referring by removing the hidden-agenda awkwardness (Wharton/Goethe reward-communication research), but for innovative products a _visible_ referrer reward taints the recommendation (Dose et al., _Journal of the Academy of Marketing Science_ 2019). Default: keep the referrer's payout out of the friend's headline; make the friend's benefit the visible message.

## Payout triggers

The trigger fires at the point where a referred signup becomes a real customer. Ranked by efficiency - protection bought per unit of engineering, instrumentation and cross-team coordination:

- **efficiency**: first purchase > qualified activation > closed-won/first invoice > retention threshold > staged payout
- **value** (protection against paying for a non-customer, strongest first): retention threshold > closed-won/first invoice > qualified activation > staged payout > first purchase
- **effort** (lightest first): first purchase > qualified activation == closed-won/first invoice > retention threshold > staged payout

The tie is real: qualified activation and closed-won each wire one new definition onto an event the business already emits - an activation event, or a CRM stage plus finance confirmation - with no holding state and no partial payouts either way.

**Bare signup is deleted from this menu, not ranked last.** It pays for tire-kickers, invites gaming, and no economics rescue it; a program firing on signup is a program to diagnose, not a design to choose.

| Trigger                                                               | Effort to run                                                                | Typical use                 | Trade-off                                                            |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------- |
| First purchase / funded account                                       | Near-zero - the billing event already fires                                  | B2C, fintech                | Standard; still exposed to refunds                                   |
| Qualified activation (installed + verified + first meaningful action) | A week - define and instrument the activation event                          | Freemium, PLG               | Filters tire-kickers at the cost of some legitimate payouts          |
| Closed-won / first paid invoice                                       | A week - a CRM stage plus finance confirmation, across two teams             | B2B sales-led               | The B2B norm; fire on verified invoiced revenue, not leads or trials |
| Retention threshold (spend ≥ $X **and** active N days)                | A quarter - usage instrumentation, a holding state, a pending-reward display | Infrastructure, usage-based | Cleanest signal; delays gratification - show the pending reward      |
| Staged payout (small at qualified lead, larger at conversion)         | A quarter to build, then a standing reconciliation job                       | B2B long sales cycles       | Keeps referrers engaged through a months-long cycle                  |

**Default rung**: first purchase / funded account. Move up to qualified activation when free signups are cheap to fake or the first purchase is trivially small.

**What this order starves**: the retention threshold - highest value, high effort, so it loses every round on ratio. Promote it whenever refund and churn exposure is large: usage-based billing, a generous refund window, or a first month that a meaningful share of customers cancel inside.

The ordering shifts with the business and with who builds it:

- A sales-led B2B company has no self-serve purchase event at all, which promotes closed-won to the top.
- A months-long cycle in which referrers go quiet promotes the staged payout.
- A team with no analytics engineer cannot reach the retention threshold at any price, which deletes it rather than demoting it.

Two design notes:

- **A visible pending reward is itself a motivator.** "You'll receive $50 when Alex completes their first month" keeps the referrer engaged and costs nothing until the condition clears.
- **Delay is also the margin guard.** Immediate rewards maximize participation and satisfaction; conditioned/delayed rewards protect against refunds and churn. Match the holding period to the product's refund window - that decision belongs to incentive design even though enforcement against deliberate abuse does not (that is a separate fraud-prevention concern).

## Caps

Every structure needs explicit caps before launch, because they are painful to introduce later:

- **Per-referrer annual cap**: bounds P&L exposure.
- **Total-earned cap**, where rewards accumulate: a storage or credit ceiling can double as an upsell moment, since the power referrer who hits the cap is a warm expansion lead.
- **Program budget ceiling**: reviewed against incremental CAC rather than attributed revenue.
