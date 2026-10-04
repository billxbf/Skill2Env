# Worked example: budget pacing report

A full example of the report shape described in the SKILL.md "Output shape" section - header, metrics table comparing the flat and weighted curves, status, suppression, diagnosis, recommendation, and owner.

```
BUDGET PACING REPORT - <campaign>, <date>
period : calendar month 2026-09-01 → 2026-09-30 | day 12 of 30, 18 remaining
budget : $30,000 (hard commitment) | buy: auction | model: B2B lead gen

metric                        flat curve      weighted curve (business-day index)
expected to date              $12,000         $11,050
spend to date                 $9,600          $9,600
pacing ratio                  0.80            0.87
projected period spend        $24,000         $24,000
budget utilization            32%             32%
remaining budget              $20,400         $20,400
required daily spend          $1,133          $1,133
trailing 7-day avg daily      $780            $780
adjust spend by               +$353/day       +$353/day

status     : UNDER-PACING - weighted 0.87, below the 0.90 on-pace floor
             (band is practitioner convention, recalibrated quarterly on this account)
suppression: none - gate passed (12-day denominator, no edits in 7 days, figures restated)
diagnosis  : impression share lost to rank elevated; lost to budget near zero
             → bid competitiveness is the constraint, not budget
recommend  : raise the bid target ~10% on the two under-delivering campaigns;
             do NOT raise the budget - it is not the binding constraint
owner      : <name> | next check: tomorrow's daily pacing review
```
