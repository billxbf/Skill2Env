# Program Economics Envelope and Benchmarks

This file covers the _program-wide_ economic shape - whether gross margin can fund a channel at all, and what compensation bands exist per motion. Modeling one partner relationship belongs to `mbfinotti/partnerships-skills@partner-economics`.

## The envelope method

Partner margin is a purchase, not a gift. Derive it from four questions, in order:

1. **What operational task is the partner taking over?** Sales motion, delivery, support, local-language coverage, vertical expertise, implementation, ongoing success work.
2. **What would that task cost in-house?** The partner margin comes out of this saving - "if you're paying margin for work you would have done anyway, you're not buying anything from the partner."
3. **What is the partner's own cost structure?** The offer must leave the _partner_ a business: a 25% margin on a $20k deal is $5k, which must cover their acquisition and delivery costs. Model their side before setting your number.
4. **How does the resulting cost-of-sale compare to direct CAC?** A channel whose all-in cost exceeds the direct motion's is a strategy tax, not leverage.

Two envelope-level rules that belong in the architecture, not in later tuning:

- **Direct-rep compensation neutrality.** Reps must never earn less because a partner touched the deal. Misaligned comp is a root cause of channel conflict, not a symptom.
- **Track cost-to-serve per partner from day one.** Most programs track partner revenue but not the discounts, funds, headcount, and training behind it. A partner "generating" $2M can net half that after true costs. The program P&L is the number finance will eventually ask for.

Copying a competitor's margin table is a named structural mistake - their economics bought different work.

## Compensation bands by motion

These are per-motion bands to price a motion already chosen, not a ranking of motions - SKILL.md step 4 ranks the menu, and richer bands here do not mean a better motion.

Almost all bands below are vendor-blog or practitioner consensus - remarkably convergent, but not audited analyst data. Treat as starting points for first-principles math, never as answers. The two analyst-grade exceptions are marked.

| Motion                                | Band                                                     | Sourcing quality                                  |
| ------------------------------------- | -------------------------------------------------------- | ------------------------------------------------- |
| Referral commission                   | 10-20% of first-year value (some cite 5-20, mode ~10-15) | Vendor/practitioner consensus                     |
| Reseller margin                       | 20-40%                                                   | Vendor-blog consensus                             |
| Value-added reseller                  | 25-35%                                                   | Vendor-blog example                               |
| Managed service provider              | 20-40%, usually recurring                                | Vendor-blog consensus                             |
| Distributor                           | 8-15% (wider ranges cited)                               | Vendor-blog, wide variance                        |
| Hyperscaler cloud resale              | 2-10%                                                    | **Analyst-sourced (Canalys) - higher confidence** |
| Deal-registration extra discount      | +5-15% on top of base                                    | Vendor-blog consensus                             |
| Market-development funds              | 2-5% of channel revenue                                  | Vendor-blog                                       |
| Legacy on-premise enterprise discount | ~40% off list (≈20% cost coverage + 20% profit)          | Long-standing practitioner rule of thumb          |

Program-shape reference points, same caveats:

- Deal-registration protection windows commonly 90-180 days (account-scoped and time-bound, never territorial).
- ~1 partner manager per 25-50 partners as a staffing rule of thumb, with 10-20 _active_ resellers per manager the sustainable engagement range per one practitioner.
- Indirect share of B2B IT spend is large (analyst-sourced ~two-thirds and, notably, recently _declining_ as AI infrastructure spend bypasses the channel), so "everyone does channel" is true and still not an argument that this company should.

## The success horizon

Set at design time, because the most common structural killer is judging a channel on the 30-90 day cycle of direct sales:

- **Year 1: leading indicators only.** Partners recruited _and activated_, first deals registered, time-to-first-deal (a sub-90-day target per partner is one practitioner's benchmark), enablement completion. Expect little net revenue, since relationship maturity takes 2-3 years.
- **Year 2: meaningful partner-sourced pipeline** and the beginnings of a repeatable co-sell play.
- **Year 3: material revenue contribution.** The frequently cited band for maturing programs is 20-30% of revenue, with ~28% cited for mature ones - vendor-survey numbers, directionally useful, not guarantees.

Course-correction triggers worth writing into the spec:

- No partner-sourced pipeline building by end of year 1 → revisit partner fit and enablement, not headcount.
- Most recruited partners dormant → stop recruiting, fix activation.
- Executive sponsor not defending the program by year 2 → existential risk, address before requesting budget.

Widely recirculated deal-velocity claims ("deals close 46% faster / 53% more likely with a partner") come from a single vendor's survey of its own ecosystem. Attribute them if cited, but never present as established fact.
