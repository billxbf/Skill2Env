# Worked Examples

Every figure below is invented to illustrate the computations. Never quote them as benchmarks or defaults - the user's own backtest replaces all of them.

## Worked lift computation

Book: 520 active B2B accounts; 46 churned in the trailing 12 months; base rate 8.8% per 12-month window.

Candidate: "weekly active users down >= 40% vs the account's own trailing-90-day median, sustained 3 consecutive weeks."

- Fired on 61 accounts during the period. Of those, 19 churned within the following 90 days: 19/61 = 31.1%.
- Lift = 31.1 / 8.8 = **3.5x** base rate. Passes a 2x floor.
- Coverage = 19 of 46 churns fired it = **41%**.
- Median days from first fire to churn across those 19 = **74 days** lead time.
- False-alarm note: 42 of 61 firing accounts retained - at ~5 flags/month this fits a CSM team that can absorb 8/week.
- Verdict: **ship**.

## Worked WoE/IV computation

Candidate variable: days since last admin login, binned. Same book: 46 churned, 474 retained - right at the ~50-churn boundary where WoE/IV becomes admissible at all, so every number below is directional.

| Bin        | Churned (share) | Retained (share) | WoE = ln(c/r)           | (c - r) x WoE          |
| ---------- | --------------- | ---------------- | ----------------------- | ---------------------- |
| 0-13 days  | 8 (17.4%)       | 322 (67.9%)      | ln(0.174/0.679) = -1.36 | (-0.505)(-1.36) = 0.69 |
| 14-29 days | 14 (30.4%)      | 108 (22.8%)      | ln(0.304/0.228) = 0.29  | (0.076)(0.29) = 0.02   |
| 30+ days   | 24 (52.2%)      | 44 (9.3%)        | ln(0.522/0.093) = 1.73  | (0.429)(1.73) = 0.74   |

IV = 0.69 + 0.02 + 0.74 = **1.45** - far above the 0.3-0.5 "strong" band, which is itself the finding: at 30+ days of admin silence this is drifting from leading indicator toward tripwire. Re-bin tighter (0-6 / 7-13 / 14-29 / 30+) and check the lead time before shipping; the 14-29 bin alone is the honest early-warning zone.

## B2B register (abbreviated)

```
CHURN SIGNAL REGISTER - illustrative B2B book, v1
Base rate : 8.8% per 12 months; churned sample = 46 (24 months)
Method    : backtest + lift + WoE/IV (46 churns - boundary call, read as directional)
             regression/Cox deleted: nobody to refit the model after ship
Rows      : ordered by value per unit of instrumentation effort

signal      : active/provisioned seats < 40% for 60d
  category  : seats | lift 2.6x | lead 95d | coverage 28% | effort near-zero | verdict SHIP

signal      : ticket spike (>=3x own median) then zero tickets for 30d
  category  : support | lift 2.9x | lead 52d | coverage 26% | effort an hour | verdict SHIP

signal      : recorded champion departs (job-change event)
  category  : relationship | lift 4.1x | lead 48d | coverage 33% | effort a standing job | verdict SHIP
  confidence: small n (15 departures observed) - directional

signal      : WAU decline >=40% vs own 90d median, 3 consecutive weeks
  category  : usage | lift 3.5x | lead 74d | coverage 41% | effort near-zero | verdict SHIP
  confidence: event stream already existed, so the highest-value signal was also cheap -
              on a book without one this drops below the cheap categories

signal      : failed payment
  category  : billing | lift 6.0x | lead 9d | coverage 15% | effort near-zero | verdict CONFIRMATORY
  confidence: exempt from lead-time bar; escalation trigger only

signal      : NPS drop >=3 pts between waves
  category  : survey | lift 1.6x | lead 80d | coverage 17% | effort near-zero | verdict WATCH
  confidence: response bias - 61% of churned accounts never answered the wave

Register-level : shipped set fired on 76% of past churns at >=30d - clears 70% floor
Handoff        : -> mbfinotti/revops-skills@customer-health-score
```

## B2C register (compact)

```
CHURN SIGNAL REGISTER - illustrative B2C subscription app, v1
Base rate : 5.1% per month; churned sample = 1,240 (12 months)

session recency > 14d (vs subscriber's own weekly habit) : usage
  lift 3.2x | lead 21d | coverage 58% | effort near-zero | SHIP  (B2C lead times compress
  - 30d floor relaxed to 14d for this book, documented as a deliberate deviation)
card approaching expiry with no update                    : billing
  lift 2.8x | lead 30d | coverage 22% | effort near-zero | WATCH (billing climbs on a
  consumer book - pre-emptive here - but 22% misses the coverage floor)
core-feature breadth drops to 1 of 4 within a month       : adoption
  lift 2.4x | lead 26d | coverage 31% | effort a week | SHIP
cancellation-page visit                                   : behavior
  lift 9x   | lead 2d  | coverage 44% | effort near-zero | CONFIRMATORY

Champion and committee categories deleted, not ranked: no B2B equivalent on this book.
```

## A plausible-looking bad signal, decomposed

Proposed: "marketing-email open rate declining -> churn risk." Rejected on four grounds:

1. **No honest baseline** - inbox privacy features inflate or mask opens per mail client, so the metric moves for reasons unrelated to the customer; the "decline" is not attributable to disengagement.
2. **Coverage masquerading as lift** - the analyst computed "70% of churned accounts had declining opens" without checking retained accounts; retained accounts showed 62%, so lift was ~1.1x.
3. **Vendor artefact exposure** - send volume changed mid-period, moving the denominator.
4. **Fails actionability** - even were it real, the team's intervention (an email) is the very channel being ignored.

The fix is not a better threshold - it is replacing the signal with customer-initiated activity from a source the vendor does not pollute.
