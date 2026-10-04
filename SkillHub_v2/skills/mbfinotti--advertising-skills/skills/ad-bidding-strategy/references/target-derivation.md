# Target Derivation

This file covers:

- the two derivations every target needs, worked both ways
- the volume-threshold derivation
- the staleness/refresh discipline

Label every number you produce with its evidence tier: **documented**, **practitioner-convergent**, or **folklore**.

## Derivation 1 - from economics: the affordable ceiling

Core formulas (keep platform-attributed revenue, blended business revenue, and contribution margin distinct - never conflate):

```
break_even_CPA        = contribution per accepted conversion
break_even_ROAS       = 1 ÷ contribution_margin_rate
target_ROAS_with_profit_goal = 1 ÷ (contribution_margin_rate − desired_net_margin)
AOV form              : break_even_ROAS = AOV ÷ (AOV − variable costs per order)
                        variable costs = COGS + shipping + fees + returns allowance
```

Margin → break-even return:

| Margin | Break-even return |
| ------ | ----------------- |
| 50%    | 2.0x              |
| 40%    | 2.5x              |
| 33%    | 3.0x              |
| 25%    | 4.0x              |
| 10%    | 10.0x             |

The folk "aim for 4x" is exactly right for a 25%-margin business and wrong for everyone else.

B2C worked example: 45% contribution margin, desired 15% net margin → target return = 1 ÷ (0.45 − 0.15) = **3.33x**. Break-even alone would be 2.22x; the difference is the profit requirement.

B2B chain - walk the funnel backward from the deal:

```
break_even_CPL = average deal size (contribution) × lead-to-close rate
break_even_CPC = target CPL × landing-page conversion rate
```

B2B worked example: $10,000 contribution per closed deal, 5% of leads close → break-even cost per lead **$500**. Landing page converts 25% of clicks to leads, target CPL set at $400 (buffer below $500) → target cost per click ceiling **$100**. Chain longer funnels stage by stage (lead → MQL → SQL → closed-won), multiplying the stage rates.

The economics number is a **ceiling**, not the target. The live target sits below it by the margin buffer the business requires.

## Derivation 2 - from history: the achievable start

- Take trailing actual cost (or return) over a mature window: 30-60 days, **plus** the conversion lag - a window that hasn't outlived the lag under-counts conversions and overstates cost.
- Vendor guidance (documented): set the initial target from "the average from the last 30 days, adjusted for any conversion delays", and base a return target on "business goals as well as your historical performance as a reference".
- **Set the initial target at or near trailing actual.** Direction of caution differs by archetype: for a cost target, at or slightly _above_ actual; for a return target, at or slightly _below_ actual. Both directions are "looser than achieved" - the point is to start where the account already is.
- Never set the initial target at the aspirational number. A target meaningfully better than achieved performance makes the platform stop bidding rather than lose money for you - delivery collapses while the reported efficiency looks excellent. This is the most documented failure in target setting.

## Reconciling the two

```
economics ceiling  (what you can afford)      e.g. break-even CPA $500
live target        (start: trailing actual)   e.g. trailing CPA  $340
margin buffer      (the named gap)            $160, or 32%
```

- Record all three numbers in the policy. The buffer is what absorbs variance, modeled-value noise, and seasonality without breaching break-even.
- Tighten from trailing actual toward the goal in steps (see change discipline in the skill body), one evaluation window per step.
- **If the two are irreconcilable** - break-even sits below anything the account has ever achieved, at any spend level - no bid strategy fixes that. It is a unit-economics problem: offer, pricing, funnel conversion, or channel fit. Say so explicitly instead of proposing a tighter target that will simply choke delivery.

## The volume-threshold derivation

Teach this instead of any hardcoded conversion count - the derivation survives platform drift, the numbers do not:

```
required budget per period ≈ target cost × volume threshold ÷ period
```

Worked: a platform whose learning guidance is ~50 events per week, at a $40 target cost → 50 × $40 ÷ 7 ≈ **$285/day** to plausibly clear it. Inverted, it answers "what volume can my budget support": $100/day at a $40 target → ~17-18 conversions/week - enough for a cost-goal strategy to run, thin for diagnosing it, far from any documented return-goal minimum.

What a threshold miss actually means: not ineligibility, but variance - at low volume you cannot distinguish a bad target from bad luck inside any reasonable window. Three honest options, ranked by what each returns per unit of effort:

- efficiency (start here): **consolidation > upstream event > accept slower diagnosis**
- effort: **upstream event > consolidation > accept slower diagnosis**
  - The upstream event needs tracking work plus an import path for the downstream outcomes (about a week where that loop exists, a quarter where it has to be built).
  - Consolidation is one restructure plus one learning reset.
  - Accepting costs near-zero: one paragraph in the policy.
- value: **upstream event == consolidation > accept slower diagnosis**
- compliance cost: **upstream event > consolidation == accept slower diagnosis**
  - Importing downstream outcomes moves customer or deal records to a platform, so it needs consent, data-processing and residency review before anything ships, and the sharing is hard to walk back.
  - The other two move no data and need no sign-off.

Consolidation leads because it buys most of the signal for the least build and no review. The upstream event buys the same signal without giving up funnel depth, but only once the import path and its approvals exist. Accepting slower diagnosis is never worthless: it keeps the policy honest about what it can and cannot conclude, but it changes nothing about the variance.

Treat this as a default that shifts with context and with who executes it:

- an account already importing CRM outcomes has paid the upstream event's build _and_ its review, and should read it first
- an account whose structure is already consolidated has no consolidation left to spend
- a legal team that will not approve the export deletes the upstream event outright

## Sanity checks on the numbers feeding the derivation

- **Platform-attributed return is inflated** relative to business reality; cross-check any return target against MER (total revenue ÷ total marketing spend) or blended figures before trusting it (practitioner-convergent).
- Use **net accepted value** where refunds, cancellations, junk leads, or fraud are material - a return target derived from gross values is silently looser than it looks.
- **Marginal vs average**: derive scaling decisions from marginal cost/return (incremental spend ÷ incremental accepted outcomes), never the average. An account can hold a 4x average return while marginal return is below break-even (documented case: incremental return fell 2.5 → 1.2 while average held at 3.0 as spend scaled 10x).
- State which CAC/ROAS variant every input uses (paid vs blended vs fully-loaded; platform vs MER) - silently switching variants makes a target look achieved or breached with nothing changing.

## Staleness and refresh discipline

A target inherits the shelf life of its inputs, and none of them announce their own drift:

| Input                    | Rots when                                         | Refresh trigger                                                   |
| ------------------------ | ------------------------------------------------- | ----------------------------------------------------------------- |
| Contribution margin rate | COGS, pricing, discounting, shipping costs change | Re-derive on price/cost change, and at least quarterly            |
| Lead-to-close rate       | Sales process, ICP, lead mix shifts               | Re-derive quarterly from CRM actuals                              |
| Trailing actual          | Continuously - it is a moving window              | Recompute at every review-cadence checkpoint                      |
| Conversion lag           | Funnel or sales-cycle changes                     | Re-measure when the funnel changes; it sets the evaluation window |

Put an explicit **refresh date** on every target in the policy document. A policy whose target has an expired refresh date is provisional until re-derived - treat it the way you would a stale benchmark: directional, not authorization.
