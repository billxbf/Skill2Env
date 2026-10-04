# Output report - worked example

A full worked pre-launch tracking verification report, showing a NO-GO decision blocked on a deduplication defect.

```
PRE-LAUNCH TRACKING VERIFICATION - <campaign>, <date>
platform(s): <...> | funnel: B2B | B2C | both | server-side: yes/no
launch: <date> | budget at risk: <amount>

check                          result       impact     fix effort        evidence
1 settings & designation       pass         -          -                 1 primary action = purchase; count-once n/a
2 tag debug                    pass         -          -                 tag fired once, on confirmation only
3 test conversion              pass         -          -                 order #QA-1042, click ID present end to end
4 payload inspection           pass         -          -                 value 4.90, currency EUR, event ID = order ID
5 platform UI + status         pass         -          -                 event visible; status: recording
6 deduplication                fail         critical   a week (dev)      server event ID differs; 2 conversions counted
7 test-data exclusion          pass         -          -                 filter ACTIVE; QA order refunded, conv. retracted
8 soak                         unknown      -          -                 starts after fix
9 sign-off                     -            -          -                 blocked by check 6

dedup rate : 0% (target ≥ ~90%)
gaps       : platform vs analytics n/a | analytics vs backend n/a | server vs browser n/a

DECISION: NO-GO
fix order  : shared event ID (only blocker at or above the default rung)
blockers   : shared event ID missing server-side (fix owner: dev team)
deferred   : click-identifier chain across the checkout domain - risk-accepted by <name>,
             hard launch date, revisit post-launch
deleted    : consent path - no consent-regulated traffic in scope (not applicable)
re-verify  : full sequence from step 3 after fix ships, then GO decision
approver   : <name>    date: <date>
```
