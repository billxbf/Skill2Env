# Worked Examples and Case Studies

Documented programs to pattern-match against, one full positive worked example, and the benchmark numbers with their reliability flagged.

## Canonical programs, decomposed by the four decision variables

| Program                                      | Sidedness                                                                 | Reward type                                                            | Trigger                                                 | Tier/cap                                                                                 | The lesson                                                                                                                                                                               |
| -------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dropbox                                      | Both, symmetric (500 MB each)                                             | In-kind product value (storage)                                        | Install + login + email verified - not bare signup      | Total-earned cap (16/32 GB) that doubles as an upsell moment                             | Product-denominated rewards at near-zero marginal cost; ~1/3 of signups were already word-of-mouth before launch - the program captured existing WOM                                     |
| PayPal                                       | Both, symmetric ($20 → $10 → $5 → ended)                                  | Cash                                                                   | Signup + linked card + first transaction                | Per-referrer annual cap (later)                                                          | Cash fits a money product; the designed _exit_ - stepping the reward down as organic growth took over - is the real lesson                                                               |
| Airbnb                                       | Both, asymmetric; several times more for referring a host than a guest    | Account credit (travel credit)                                         | Friend's first _completed_ stay                         | Credit cap                                                                               | Pay more for the scarce side of a marketplace; their A/B test found altruistic framing ("give your friend $25") beat selfish framing globally                                            |
| Robinhood                                    | Both                                                                      | Lottery-shaped: ~99% of "free stock" grants worth ~$5, tail up to $200 | Account approved + funded                               | $1,500/year cap                                                                          | A probability distribution lets the headline advertise the tail while expected cost stays ~$5                                                                                            |
| Morning Brew                                 | Referrer-only                                                             | Swag/status ladder                                                     | Verified subscription                                   | 3 → 5 → 10 → 25 → 50 → 100 → 1,000; first tier reachable "from the coworkers around you" | Threshold ladders suit high-volume/low-value referrals; ~$0.25 per acquired subscriber at the sticker tier                                                                               |
| Developer cloud hosts                        | Both, asymmetric (friend gets a large intro credit, referrer a small one) | Account credit                                                         | Friend spends a threshold **and** stays active ~90 days | Non-expiring referrer credit                                                             | Retention-gated triggers for usage-based products; note several strong PLG dev platforms run _no_ program - strong organic WOM can make one unnecessary                                  |
| Tesla (negative example)                     | Both                                                                      | Escalating prizes up to free vehicles                                  | Referred purchase                                       | **Uncapped ladder** - the failure                                                        | Killed repeatedly for "adding too much cost"; lavish rewards for a product with intense organic demand mostly subsidize purchases that would have happened anyway                        |
| B2B SaaS at scale (pattern, not one company) | Referrer-side commission                                                  | Revenue share or account credit                                        | Closed-won / invoiced revenue                           | Contract-value based                                                                     | Several well-known SaaS products migrated their customer-referral credit programs into affiliate/partner programs as ACV grew - the customer-referral model has a scaling ceiling in B2B |

## Worked example: $49/month self-serve B2B SaaS

Inputs: $49/month entry plan, 80% gross margin, ~14-month average lifetime (LTV ≈ $686), paid CAC $220, referrers are end users at small companies who usually control the card themselves (principal-agent risk low).

1. **Ceiling**: $686 × 0.80 × 25% allowed ≈ **$137 total per successful referral** - the boundary, not the target.
2. **Sidedness**: double-sided, tilted to the friend (the $49 commitment is the hard action). Test a friend-only arm against it.
3. **Type**: account credit both sides (subscription product, referrers rebuy monthly, credit costs margin only when redeemed).
4. **Size and framing**: friend gets 1 month free (framed "first month free" - on a sub-$100 price a whole free month reads bigger than "$49 off"); referrer gets $30 credit. Nominal total $79, real cost ≈ $63 per successful referral - well under the $137 ceiling, which is defined per successful referral. The CAC comparison is a different number: the pass threshold gates on cost per _incremental_ referred customer. About 50% of rewarded referrals would have converted anyway, so $63 ÷ 0.50 ≈ **$126 per incremental customer** against paid CAC $220 - a 1.7× advantage, not the 3.5× the raw $63 implies. Check it against blended CAC too, which sits below the paid figure and thins the margin further.
5. **Trigger**: referrer credit fires when the friend's _second_ paid invoice clears (survives the refund window and first-month churn); show it as pending from day one.
6. **Tiers**: none at launch - volume unproven. Revisit if >10% of referrers refer 3+.
7. **Caps**: 10 rewarded referrals per referrer per year; program budget reviewed quarterly against incremental CAC.
8. **Validation**: 3 arms (both-sides / friend-only / referrer-only) on 10% of the active base for 8 weeks; decision metric = new paying customers per 1,000 exposed accounts, checked against a no-program holdout.

## Benchmarks - with reliability flags

Peer-reviewed (durable):

- Referred customers: 16-25% higher LTV, ~18% lower churn (persistent), and 31-57% more onward referrals - the reason referral CAC may justifiably exceed naive parity with other channels.
- ~50% of rewarded referrals in academic data would have converted anyway (only the rest are incremental).

Vendor-published (directional only - undisclosed methodology, commercial incentive; never present these as facts):

- Share of customers who share: healthy programs 5-15%.
- Referred-visitor conversion: median 3-5% (e-commerce), top programs 8%+.
- Mature programs: 15-25% of new-customer acquisition.
- Minimum motivating reward: ≈ $20 or ~11% discount.
- The widely quoted "83% of satisfied customers are willing to refer, 29% do" traces to a single 2018 study no longer available online - cite with that caveat or not at all.

Reward amounts at named companies change frequently; verify against the live terms page before quoting one to the user.
