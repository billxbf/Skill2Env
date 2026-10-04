# Guardrail and Counter-Metric Design

The mechanism behind the "one paired counter-metric per owned metric" ground rule.

## The two laws a guardrail defends against

- **Goodhart's Law** (Charles Goodhart, 1975; generalized by Marilyn Strathern): "When a measure becomes a target, it ceases to be a good measure."
- **Campbell's Law** (Donald Campbell, 1979): the more a quantitative indicator is used for decision-making, the more subject it becomes to corruption pressures.

Manheim and Garrabrant (2018) decompose Goodhart failures into four modes, useful vocabulary for diagnosing _which way_ a metric is being gamed, not just that it is:

- regressive
- extremal
- causal
- adversarial

## Grove's paired indicators - the durable defense

Andy Grove, _High Output Management_ (1983), two decades before "Goodhart's Law" became common vocabulary: indicators direct attention toward what they monitor, so guard against overreacting "by pairing indicators, so that together both effect and counter-effect are measured." His quantity/output measures each get a quality-side pair:

- inventory levels with incidence of shortages
- vouchers processed with errors found
- square feet cleaned with a quality rating

The design rule this implies: a guardrail is not "a second metric to also watch" - it is specifically the quality-side pair to a quantity-side owned metric, measuring the dimension the owned number cannot see. Amplitude's North Star convention applies the same idea structurally: 2-3 guardrail metrics ride alongside the 3-5 input metrics at the same layer, never bolted onto the top metric as an afterthought.

## Standard GTM pairs

Inferred from Grove's mechanism, consistent with sourced guidance ("pair every efficiency metric with a quality or outcome metric" - WFM Labs); adapt to the user's tree rather than copying:

| Owned metric (quantity)        | Guardrail (quality)                          | Gaming it blocks                       |
| ------------------------------ | -------------------------------------------- | -------------------------------------- |
| SQL volume                     | SQL-to-opportunity conversion                | SDRs flooding the funnel with junk     |
| MQL volume                     | Down-funnel win rate / lead quality          | Marketing optimizing raw counts        |
| Pipeline coverage              | Win rate (specifically - not a generic pair) | Stage inflation, phantom opportunities |
| Sales velocity / deals closed  | Discount depth / net price realization       | Buying deals with margin               |
| Expansion revenue              | Churn rate or NPS                            | Upsells that damage retention          |
| Activity counts (calls, demos) | Meeting-to-opportunity rate                  | Activity theater                       |
| Health-score coverage          | Prediction accuracy vs. actual churn         | Vanity scoring                         |

## The documented failure this design prevents

A sales VP tied bonuses to holding 4x pipeline coverage; opportunity count doubled in three weeks, and win rate later dropped by nearly half - the pipeline had filled with noise, not opportunities. The diagnostic: coverage rising while win rate falls is almost always inflation, not improvement. This is Campbell's Law observed directly in a GTM setting, and the reason coverage's guardrail must be win rate itself.

## The escalation rule to write into the framework

If an owned metric rises while its paired counter-metric falls for **two consecutive review cycles**, treat it as gaming, not improvement: escalate to the branch's owner and the review tier above, and never pay out or celebrate the movement until the pair is explained. A guardrail register whose rule never fires is either a very honest org or an unwatched register - check which.

## Placement rules

- Guardrails attach where the gaming pressure is: at owned input metrics, one pair each. The top metric needs no guardrail of its own if every input beneath it is paired.
- A guardrail has a watcher, not a target. Setting a target on the guardrail turns it into a second owned metric and recreates the original problem one level over.
- When a guardrail fires repeatedly on the same branch, the fix is usually structural (re-cut ownership, change the comp trigger), not a stern reminder.
