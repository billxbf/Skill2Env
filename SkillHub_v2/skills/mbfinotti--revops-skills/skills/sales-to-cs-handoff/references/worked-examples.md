# Worked Examples

Three artifacts: a filled handoff spec for a mixed-motion org, a filled packet for one deal, and a negative example with its cost. Company names and figures are illustrative.

## Example 1: Filled handoff spec (mid-market + self-serve SaaS)

```
HANDOFF SPEC - Northbeam Analytics, 2026-03-02, v1
Scope      : mid-market sales-led (~25 deals/mo) + self-serve (~400 conversions/mo).
             Non-goals: onboarding curriculum, 90-day success plans, health scoring.
Trigger    : Mid-market - opportunity set to Closed Won with signed contract attached.
             Gate blocks on: products+exclusions, ACV/term/renewal date, special terms,
             business objective, success metrics, timeline expectations, economic buyer,
             day-to-day contact, resonating use cases, concerns raised, commitments log,
             integrations list (if any). Self-serve - billing event `subscription.created`;
             gate blocks on plan, billing state, signup source, marketing consent.
Packet     : Mid-market - CRM fields above + 1-page brief + links to 2 key call recordings.
             Self-serve - the account record is the packet.
Artifact   : CRM record of the opportunity (fields) + attached brief. Event payload for
             self-serve. Chat and email are never the record.
Clocks     : Mid-market - internal ≤ 1 business day; kickoff held ≤ 5 business days after
             acceptance. Self-serve - assignment instant; first lifecycle email ≤ 1 hour.
Meetings   : Mid-market - async internal brief with CSM confirmation, then customer
             kickoff where the AE introduces the CSM live. Self-serve - none; activation
             flow targets "first dashboard shared" as the activation event.
Acceptance : Mid-market - receiving CSM accepts/rejects ≤ 1 business day, reason-coded;
             re-submission ≤ 1 business day; second reject escalates to both managers.
             Self-serve - automated record validation; failures queue to CS ops.
Escalation : SLA breach -> owning manager at 100% elapsed; kickoff at risk -> both
             managers at 50% elapsed unscheduled; BAD-FIT -> monthly alignment forum.
Automation : On trigger: assign CSM by segment rule (fallback: pool lead), notify, create
             kickoff task, enroll in "New Customer" sequence, remove contact from all
             sales sequences, set Customer Since date.
KPIs       : Gate completeness ≥95% | first-submission acceptance ≥90% | internal median
             ≤1 bd | kickoff median ≤5 bd (p90 reported) | TTFV to "first dashboard
             shared" trending down | 90-day churn tracked as outcome | reject codes monthly.
Governance : Process owner: RevOps lead. Acting: AEs (supply), CSMs (accept/receive),
             CS ops (self-serve validation). Review: weekly during 60-day pilot, then
             monthly. Change log: spec doc revision history.
```

## Example 2: Filled handoff packet (one mid-market deal)

```
HANDOFF PACKET - Harwell Logistics, closed-won 2026-03-10, AE: R. Okafor -> CSM: L. Deme
Commercial : Platform (Growth tier, 40 seats) + Routing module. EXCLUDED: forecasting
             module (demoed, not bought - customer may assume otherwise). $58k ACV,
             12 months, renewal 2027-03-10. Special: net-60 payment, 30-day opt-out
             clause at month 6. 12% discount for case-study participation commitment.
Objective  : Cut delivery-window misses from 9% to under 4% before their Q4 peak season.
Success    : Agreed metric: delivery-window miss rate in their weekly ops report.
             They consider it working when their own dashboard shows <6% by end of Q2.
Timeline   : Live before 2026-05-01 - hard expectation, tied to a board commitment.
Stakeholders: Economic buyer: COO T. Harwell (signed, will not attend onboarding).
             Champion/day-to-day: Ops Director M. Chen (enthusiastic). Skeptic: IT lead
             J. Prieto - concerned about API load, needs early technical win.
Context    : Resonated: exception-alerting demo on their own sample data. Evaluated
             CompetitorX (lost on implementation time) - they will re-engage at renewal.
             Concerns raised: data accuracy of carrier feeds; prior vendor failed here.
Commitments: (1) Dedicated onboarding call with IT lead in week 1. (2) Carrier-feed
             accuracy review at day 30. (3) Case study drafted only after Q2 metric hit.
Technical  : TMS integration via REST API (their side, IT lead owns); no SOW; SSO required
             before company-wide rollout.
Recordings : Discovery call 2026-01-22, technical deep-dive 2026-02-18 (links in CRM).
```

## Example 3: Negative example - the handoff that wasn't

The same deal, as it actually happens in orgs with no designed process:

The AE marks the deal closed-won on the 10th, posts "Harwell signed! 58k!" in chat, and moves to the next deal. The CRM holds the contract PDF and a notes field reading "good discovery, ops pain, IT guy difficult." No assignment fires.

The CS manager notices the win in the revenue dashboard four days later and assigns whichever CSM has capacity. The CSM books a kickoff for week three - the earliest slot - and prepares by reading the notes field.

At kickoff, the CSM asks Harwell to describe their goals. M. Chen repeats the entire discovery conversation, visibly annoyed. Nobody knows about the week-1 IT call commitment, so J. Prieto - the skeptic - gets no early technical win and goes cold.

The forecasting-module exclusion surfaces in week five as "wait, that's not included?" The 30-day carrier-feed review never happens because nobody knew it was promised; the accuracy concern resurfaces in month three as an escalation.

The customer exercises the month-6 opt-out. Sales blames onboarding; CS blames the deal.

What it cost, in the terms this skill measures:

- Internal handoff 4 days instead of 1.
- Kickoff at 15 business days instead of 5.
- Two recorded commitments dropped (both were in a call recording nobody linked).
- TTFV never reached.
- $58k churned at month 6, plus the case study that was part of the price.

Every failure maps to a missing spec line:

- Gate (exclusions, commitments).
- Assignment automation (4-day gap).
- Acceptance step (a reject for UND-PROM/INC-GOAL would have caught the notes field).
- The external clock (15 days unmeasured because it was untracked).
