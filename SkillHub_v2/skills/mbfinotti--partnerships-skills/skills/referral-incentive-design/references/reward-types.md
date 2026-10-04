# Reward Type Selection

How to choose what each party receives. The menu is stable; the choice is driven by product economics and referrer identity, not creativity.

## The menu, ranked by efficiency

Efficiency here is value delivered per unit of _effort to run the reward_ - setup work, ongoing administration, fulfillment burden, coordination with finance or legal, and how hard the reward is to withdraw once published. It is not value per dollar paid out; what each type costs you is a separate axis, and the two disagree.

- **efficiency**: in-kind product value > account credit == free months/seats > discount > status/recognition > cash/gift card > swag > charity > sweepstakes
- **cost to you** (cheapest first): in-kind == status > account credit == free months/seats > discount > swag > sweepstakes > cash == charity
- **value to the recipient** (strongest first): cash > account credit == free months/seats > discount > in-kind > swag > sweepstakes > status > charity
- **effort to run** (lightest first): discount > status > account credit == free months/seats > in-kind > cash > charity > swag > sweepstakes
- **compliance cost** (lightest first, only the three exposed types): cash/gift card > charity > sweepstakes. The other six trigger no review beyond the terms page every reward needs - but every published reward is hard to withdraw, so treat any headline number as a one-way door.

Two ties, both real:

- **Account credit == free months/seats**: the same billing primitive under two labels, the same margin-on-redemption cost, the same wiring. They differ only in how the number is framed: present a percentage under a $100 price and an absolute amount above it, never in what they cost or take to run.
- **In-kind == status on cost**: both grant something whose marginal cost rounds to zero. They split on effort and on whether an in-group exists to make status mean anything.

| Reward type                                        | Real cost to you                                   | Effort to run                                                                                            | Fits best when                                                                     | Watch out for                                                                                                                                                                  |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| In-kind product value (more storage, seats, usage) | Near-zero when marginal cost is low                | A week: one provisioning hook, then near-zero                                                            | Freemium and infrastructure products where a unit of product is cheap to grant     | Only motivates people already invested in the product                                                                                                                          |
| Account / product credit                           | Below face value (only costs margin when redeemed) | An hour to a week - billing systems already have a credit primitive                                      | Subscription or repeat-purchase products; the referrer will buy again              | Worthless to a referrer who will not purchase again; unredeemed credit still needs accounting treatment                                                                        |
| Free months / seats                                | Deferred revenue cost                              | An hour to a week - same primitive as credit                                                             | Subscription products; symmetric "give a month, get a month" offers                | Free-month hunters churn after redemption                                                                                                                                      |
| Percentage or fixed discount                       | Margin give-up on the next purchase                | Near-zero - a coupon code your commerce stack already issues                                             | Retail/DTC with healthy margin; friend-side incentives                             | Attracts bargain hunters on the friend side if oversized                                                                                                                       |
| Status, recognition, early access                  | Near-zero                                          | Near-zero to grant, a standing job to keep the in-group real                                             | Communities, developer tools, prosumer products where referring is a public act    | Needs a real in-group to signal to; fabricated exclusivity backfires                                                                                                           |
| Cash / gift card                                   | Full nominal cost, real P&L outflow                | A quarter: payout rails, finance sign-off, then per-referrer tax reporting forever                       | Money-adjacent products (fintech, payments); one-time high-consideration purchases | Feels transactional; can crowd out the social motivation to recommend; triggers tax reporting thresholds in some jurisdictions                                                 |
| Physical swag (usually tiered)                     | Low unit cost + fulfillment overhead               | A standing job: inventory, addresses, shipping, customs, replacements                                    | Newsletters, community brands; milestone ladders                                   | Logistics; works as a ladder, rarely as a single flat reward                                                                                                                   |
| Charity donation                                   | Full cost, weaker conversion                       | A week to wire a donation vendor, then receipting every cycle                                            | Mission-driven brands, image-sensitive audiences                                   | Underperforms direct rewards on conversion in field tests - offer as a _choice_, never the only option; charitable-solicitation and cause-marketing rules vary by jurisdiction |
| Sweepstakes / lottery entry                        | Fixed prize pool                                   | A quarter, most of it legal: official rules, registration where required, rules you cannot amend mid-run | High-volume, low-value-per-referral programs                                       | Advertises a big number while expected payout stays small; some jurisdictions regulate lotteries                                                                               |

**Default rung**: in-kind product value when the product has a cheap unit to grant, account credit everywhere else. Move to cash only when the referrer will never buy again or the product is money-adjacent - the one case where the efficiency leader is worth nothing to the person receiving it.

**What this order starves**: swag and status. Both lose every round on ratio because fulfillment and community upkeep are standing jobs, yet they are the only rewards that keep a high-volume, low-value-per-referral ladder affordable at its top rungs - a 1,000-referral tier is swag, never cash. Promote them when the reward is a ladder rung rather than a flat payout, and there is a real in-group to signal to.

This order is a default, not a law: it shifts with the product and with who has to run it. Re-rank against what you already know about the user before you present the menu:

- A product whose marginal unit costs near zero pushes in-kind further ahead of everything else.
- A finance team that refuses cash payouts deletes cash from the menu rather than demoting it.
- An existing rewards or fulfillment platform collapses the effort gap between swag, gift cards and credit, and re-ranks all three.

## Decision criteria, in order

1. **Can the reward be denominated in the product's own value?** If a unit of product (storage, credits, seats, usage) has near-zero marginal cost, in-kind rewards deliver high perceived value at low real cost, and redemption deepens engagement instead of draining cash - which is why it leads the efficiency order above. Account credit costs you the margin on redeemed credit, not the face value, a point most programs never model.

2. **Will the referrer buy again?** For one-time, high-consideration purchases, a discount on a product the referrer will never rebuy is worthless to them - pay the referrer in cash-equivalents and give the friend the discount. For subscriptions and repeat purchases, credit rewards the referrer _and_ drives their next purchase.

3. **Does reward-product congruence apply?** Field and lab evidence (Hu & Zhang, _Frontiers in Psychology_ 2021) shows utilitarian rewards work better for utilitarian products, hedonic rewards for hedonic products. A B2B tool is utilitarian: prefer cash, credit, or capability over gifts and experiences.

4. **Is referring a public, identity-driven act?** Where recommendations are visible (developer communities, open-source ecosystems, professional networks), image motivation does real work, and monetary rewards can crowd it out (Ariely, Bracha & Meier, _American Economic Review_ 2009 - evidence transferred from prosocial-behavior settings, treat as strong inference rather than direct proof). Status tiers, early access, and public recognition can outperform cash here at near-zero cost.

5. **Is the product innovative or novel?** Customers are _less_ likely to recommend innovative products when publicly rewarded for it - the reward taints the recommendation (Dose et al., _Journal of the Academy of Marketing Science_ 2019). The documented fixes: do not disclose the referrer's reward to the recipient, increase the reward size, or reward both sides.

## The B2B principal-agent fork

In B2B the person who refers is usually an employee, but the buyer is their company. Rewarding the individual with cash or gift cards collides with corporate gift policies (many prohibit cash outright and treat gift cards as cash; common limits are $25-50 per gift with logging requirements) and can pull the program into per-referrer tax reporting.

The durable pattern is **two-track**:

- **Company track**: account-level value - credits, discounts, service upgrades - flowing to the customer's company. Policy-neutral, procurement-friendly.
- **Individual track (optional)**: a modest, capped, non-cash token the individual can choose (or donate), with an explicit opt-out for referrers whose employer forbids gifts.

Fire both tracks only on verified invoiced revenue, never on leads or trials.

## Negative example - what not to do

A $200/month B2B analytics tool offers referrers a $25 Amazon gift card at friend signup. Three compounding errors: the reward is cash-equivalent to an employee (gift-policy collision), it fires on signup rather than a paid conversion (pays for tire-kickers), and $25 against a plausible four-figure LTV is deep in the too-small zone where a token payment performs worse than a plain "thank you" would. Better: 1 month of account credit to the company per closed-won referral, plus an optional charity-or-swag choice for the individual.
