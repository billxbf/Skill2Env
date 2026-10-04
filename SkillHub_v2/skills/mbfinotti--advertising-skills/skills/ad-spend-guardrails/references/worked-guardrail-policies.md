# Worked Guardrail Policies

Three examples: a filled B2B SaaS policy, a filled B2C e-commerce policy, and a negative example annotated line by line. The numbers are illustrative - they exist to show the shape of a defensible derivation, not to be copied as targets.

## Table of Contents

- [Example 1 - B2B SaaS](#example-1-b2b-saas)
- [Example 2 - B2C e-commerce](#example-2-b2c-e-commerce)
- [Example 3 - negative example, annotated](#example-3-negative-example-annotated)

## Example 1 - B2B SaaS

Context: $18K ACV, 68% gross margin, median sales cycle 78 days, $2.1M cash, $180K monthly burn, venture-funded and scaling. Conversion feed reliable (server-side CRM import of SQL and closed-won), no incrementality testing yet.

```
SPEND GUARDRAIL POLICY - Northwind Analytics, effective 2026-09-01, review 2026-12-01

Inputs
  Contribution per closed-won deal  $12,240 (ACV $18,000 x 68% GM)      measured
  Lead-to-close rate                7.4% SQL -> closed-won, 4 quarters    measured
  Payback target                    14 months (board-agreed)             measured
  Runway                            11.7 months at current burn          measured
  Cash cap on paid media            $95,000 / month                      estimated

Derivation
  Allowable CAC (break-even)  = $12,240 contribution per deal
  Allowable CAC (target)      = monthly gross profit $1,020 x 14 months = $14,280
                                -> the payback target is LOOSER than break-even,
                                   so break-even binds. Target CAC set at $8,500,
                                   the level the FY plan needs to fund headcount.
  Break-even cost per SQL     = $12,240 x 7.4% = $906
  Target cost per SQL         = $8,500 x 7.4%  = $629

Layers
  Break-even floor   cost per SQL $906        -> stop, always
  Target floor       cost per SQL $629        -> investigate within one weekly review
  Hard floor         cost per SQL $820        -> automatic halt of the breaching channel
                                                 + escalation to VP Marketing

Guardrail set
  1. Cost per SQL (CRM-sourced, 6-week trailing window)
     counter-metric: SQL-to-closed-won rate - catches cheap SQLs that never close
  2. Blended CAC on new logos only (excludes expansion), monthly
     counter-metric: new-logo share of pipeline
  3. Paid media spend as share of runway, monthly
     counter-metric: none needed - it is itself the cash constraint

Kill rules
  Streak    cost per SQL above the hard floor for 3 consecutive weekly reads
  Rate      35% of a channel's quarterly budget consumed with cost per SQL above
            the hard floor
  Evidence  no kill before 6 weeks of data AND 30 SQLs on the channel; a channel
            below either bar is held flat, never killed
  Restart   restart at 50% of prior budget after a documented fix (creative, offer,
            targeting or tracking), approved by the Growth Lead, reviewed at 4 weeks

Governance
  Owner            CFO owns break-even inputs; VP Marketing owns target and hard floors
  Escalation       target breach -> Growth Lead, weekly review
                   hard breach   -> VP Marketing, 48h decision
                   break-even breach -> CFO, immediate halt, no discretion
  Override         VP Marketing may authorize up to 4 weeks above target floor with a
                   written reason logged in the marketing operating doc; anything above
                   break-even floor requires CFO co-sign; overrides are never standing
  Re-baseline      quarterly, plus on: pricing change, gross-margin change > 3pts,
                   sales-cycle change > 2 weeks, CRM attribution change

Exemptions
  Exploration budget 12% of monthly paid spend, exempt from the cost-per-SQL floors.
  Own rules: each test carries a hypothesis, a decision date, and a spend cap of
  3x target cost per SQL before a keep/cut call.

Assumptions
  7.4% lead-to-close holds at higher volume. If it degrades below 6%, every floor above
  is wrong and the policy must be re-derived, not adjusted.
```

## Example 2 - B2C e-commerce

Context: $74 AOV, 54% contribution margin after COGS and delivery, repeat purchase within 90 days, profitable and self-funded, no MMM, platform pixel plus server-side events.

```
SPEND GUARDRAIL POLICY - Fernbrook Goods, effective 2026-09-01, review 2026-12-01

Inputs
  AOV                        $74                                      measured
  Contribution margin (CM3)  54% after COGS and delivery, before ads  measured
  Contribution per order     $39.96                                   measured
  Cash cap on paid media     $140,000 / month                         measured
  Repeat rate, 90 days       31%                                      measured

Derivation
  Break-even ROAS       = 1 / 0.54 = 1.85x
  Break-even CAC        = $39.96 first-order contribution
  Target ROAS           = 2.40x, the level that funds the 18% net-profit plan
  Marginal vs blended   at 54% margin the marginal floor is 1.85x and the blended
                        floor is set at 2.40x. Scaling decisions read the marginal
                        number; the monthly report reads the blended one.

Layers
  Break-even floor   marginal MER 1.85x        -> stop, always
  Target floor       blended MER 2.40x         -> investigate at the weekly review
  Hard floor         blended MER 2.00x         -> automatic halt of new scale-ups,
                                                  spend held at prior week's level

Guardrail set
  1. Blended MER, weekly (total revenue / total marketing spend)
     counter-metric: new-customer share of orders - a MER met by retargeting existing
                     buyers is not the same business
  2. Contribution margin after ads, daily
     counter-metric: discount depth - margin held up by promo dependence is borrowed
  3. Marginal MER on the last 25% of spend, at every scale-up decision
     counter-metric: none - it is the scaling gate itself

Kill rules
  Streak    blended MER below hard floor for 5 consecutive days
  Rate      $12,000 spent in any 72h window with blended MER below the hard floor
  Evidence  no kill on a campaign below $1,000 spend or below 3 days live; both bars
            must clear
  Restart   restart at 60% of prior daily budget once the underlying cause is named
            and fixed; two clean weeks required before returning to full budget

Governance
  Owner        Founder owns the break-even inputs and the hard floor;
               Head of Growth owns the target floor
  Escalation   target breach -> Head of Growth, weekly
               hard breach   -> Founder, same day
  Override     Founder only, maximum 14 days, reason logged; seasonal peaks are
               pre-approved in writing before the season, never mid-flight
  Re-baseline  quarterly, plus on: COGS change, shipping-cost change, price change,
               or any change to the conversion-tracking setup

Exemptions
  Creative testing 15% of monthly spend, judged on a spend-based rule (no purchase by
  $500-1,000 spend -> cut) rather than on the MER floors.

Assumptions
  54% CM3 assumes current shipping rates and a return rate at or below 8%. Peak-season
  shipping surcharges push break-even ROAS above 2.0x - re-derive before November.
```

## Example 3 - negative example, annotated

What a policy looks like when each rule in the skill is broken. Read it as a checklist of what to reject.

```
AD SPEND RULES
- Target ROAS: 4x across all channels.
- If ROAS drops below 4x, pause the campaign.
- Test budget comes out of the same pot.
- Marketing team reviews performance in the Monday meeting.
```

| Line                                    | What is wrong                                                                                                                                                                                                                                          |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "Target ROAS: 4x"                       | No derivation. 4x is folklore with no traceable author - it is break-even at a 25% contribution margin, retroactively declared a target. This business's margin is never stated, so nobody can tell whether 4x is generous or ruinous                  |
| "across all channels"                   | One flat threshold across segments that behave differently. It starves prospecting, which always looks worse than retargeting, and flatters brand search, which harvests demand that was already coming                                                |
| "If ROAS drops below 4x"                | Which ROAS? Platform-reported, blended, contribution-margin? Undefined variant means the number is unauditable. It also collapses break-even, target and hard floor into one line, so a single bad day and a structural collapse get the same response |
| "pause the campaign"                    | Binary, immediate, with no evidence gate, no consecutive-period requirement and no minimum spend. This is a thrash generator: pause, restart, reset learning, repeat                                                                                   |
| (missing)                               | No restart condition. Once paused, nothing says what has to be true to turn it back on, so paused campaigns accumulate                                                                                                                                 |
| "Test budget comes out of the same pot" | Testing is held to the production efficiency bar, which quietly ends testing. Ring-fence it with its own rules                                                                                                                                         |
| "Marketing team reviews"                | No named owner, no approver, no separation of duties. The team spending the money also decides whether the ceiling was breached - which means the ceiling is a preference, not a control                                                               |
| (missing)                               | No counter-metric. The fastest way to hit a 4x ROAS floor is to shift budget into retargeting and branded search; nothing here would make that visible                                                                                                 |
| (missing)                               | No re-baselining date and no event triggers, so the number survives a pricing change, a margin change and a tracking change without anyone noticing it is now wrong                                                                                    |
