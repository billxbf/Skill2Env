# SLAs, the Acceptance Gate, and KPIs

Every handoff between teams needs an SLA, a tracking mechanism, and someone accountable for follow-through - the widely repeated RevOps rule applies to sales-to-CS exactly as it does to marketing-to-sales. This file defines the two clocks, the acceptance mechanics, and the measurement layer.

## The two clocks

| Clock            | Starts                       | Stops                                                                       | Default target                                                                           |
| ---------------- | ---------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Internal handoff | Closed-won recorded in CRM   | Packet submitted, receiver assigned, receiver notified                      | 1 business day (same day for automated segments)                                         |
| External kickoff | Receiver accepts the handoff | Kickoff meeting _held_ (not scheduled) - or first automated touch delivered | Segment SLA: ≤ 10 business days high-touch, ≤ 5 mid-market, ≤ 2 SMB, ≤ 1 hour self-serve |

Rules:

- Measure in business hours/days from CRM timestamps, never from recollection. Report median **and** 90th percentile - the p90 tail is where customers ghost.
- The external clock stops at _held_, because a scheduled-then-slipped kickoff is indistinguishable from no kickoff to the customer. Track kickoff no-shows and reschedules separately.
- The internal clock does not start until the deal is genuinely closed-won per the stage's entry criteria - a gate on a mislabeled deal measures nothing.
- Defaults above are this skill's starting conventions; calibrate against the org's own baseline within the first quarter.

## The acceptance gate

The step that turns the handoff from a notification into a contract between teams.

1. **Submit**: rep completes the packet; the gate auto-checks must-block fields and required attachments. Incomplete submissions bounce immediately without starting the receiver's clock.
2. **Review**: the receiver (CSM, pool lead, or automated validator) reviews within a defined window - default 1 business day.
3. **Accept or reject**: acceptance transfers ownership and starts the external clock. Rejection carries a reason code and bounces to the rep with a re-submission clock (default 1 business day). A reject is a quality signal, never a fault ruling - no penalty for rejecting, or the gate becomes theater.
4. **Re-submission**: second submission reviewed against the cited reason only. A second reject on the same deal escalates automatically.

Starting reason codes (extend from observed rejects, retire unused ones quarterly):

| Code     | Meaning                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------- |
| INC-COM  | Commercial/contract fields incomplete or contradict the contract                                                |
| INC-GOAL | Business objective or success definition missing or generic boilerplate                                         |
| INC-STK  | Economic buyer or day-to-day contact missing                                                                    |
| INC-TECH | Known technical/delivery requirement undocumented                                                               |
| UND-PROM | Commitment made to the customer not recorded in the packet                                                      |
| BAD-FIT  | Customer appears outside the qualified-customer definition - routes to the alignment forum, not back to the rep |
| JUNK     | Fields filled with throwaway non-answers just to pass the gate                                                  |

## Escalation

| Situation                | Escalates to             | When                                          |
| ------------------------ | ------------------------ | --------------------------------------------- |
| Internal clock breached  | Rep's manager            | At 100% of SLA elapsed                        |
| Review window breached   | CS/pool manager          | At 100% of SLA elapsed                        |
| External clock at risk   | Both managers            | At 50% elapsed with no kickoff scheduled      |
| Second reject, same deal | Both managers jointly    | Immediately                                   |
| BAD-FIT code used        | Sales/CS alignment forum | Next session, with the deal as an agenda item |

## KPIs

| KPI                         | Definition                                                                    | Starting target         | Caveat                                                                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gate completeness           | % of closed-won deals passing the gate complete on first submission           | ≥ 95%                   | Measures presence, not quality - pair with the sampling audit                                                                                                                              |
| First-submission acceptance | % of handoffs accepted without a reject                                       | ≥ 90%                   | Near-100% alongside quality complaints means the gate checks the wrong fields                                                                                                              |
| Internal handoff time       | Closed-won → submitted+assigned, median and p90                               | Median ≤ 1 business day |                                                                                                                                                                                            |
| Kickoff time                | Acceptance → kickoff held, median and p90, per segment                        | Within segment SLA      | Stops at held, not scheduled                                                                                                                                                               |
| Time to First Value (TTFV)  | Close → customer gets real value or clearly sees the value potential (Murphy) | Measured; trending down | A goal, not a stopwatch: "a customer should NOT be considered 'onboard' simply after a certain amount of time has passed" - define the value event, don't let elapsed time stand in for it |
| Early-life churn            | Churn/non-renewal within first 90 days                                        | Tracked as outcome      | Downstream measure of handoff quality; never target-managed weekly, and shared ownership with onboarding                                                                                   |
| Reject-code distribution    | Rejects by reason code per month                                              | Reviewed monthly        | A recurring code is the packet definition asking to be changed                                                                                                                             |

Targets are this skill's conventions, set where a lower bar would not survive real deal flow - not published industry benchmarks. Iterate the gate, packet, and clocks until all hold on a rolling month.

## Instrumentation and cadence

- Timestamps: closed-won, packet submitted, receiver assigned, accepted/rejected (+code), kickoff scheduled, kickoff held, value event reached. All as CRM fields or workflow logs - if a timestamp can't be captured, the KPI on it is fiction.
- Automation at trigger: assign receiver, notify, create kickoff task, enroll in the segment's sequence, remove the contact from all sales sequences (the classic miss - the customer keeps getting prospecting emails after buying).
- Cadence:
  - Weekly during pilot: review every reject and every SLA breach individually.
  - Monthly in steady state: KPI dashboard, reject-code distribution, packet-quality sample of 5-10 deals.
  - Quarterly: re-fit reason codes, re-check must-block field list against what kickoffs actually used, recalibrate targets against the new baseline.
