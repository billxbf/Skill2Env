# Synthetic test pack and rollout sequence

## The test pack

A fixed set of synthetic records, pushed through every ingestion path, with the expected owner written down before the run. The pack is an artifact that lives beside the routing matrix and is re-run on every assignment-affecting change.

One row per case:

| Case | Scenario                            | Input record                                        | Ingestion path | Expected owner                                     | Expected SLA          |
| ---- | ----------------------------------- | --------------------------------------------------- | -------------- | -------------------------------------------------- | --------------------- |
| P-01 | Named account, clean match          | Company on named list, all fields populated         | Web form       | Named-account owner                                | 4 business hours      |
| P-02 | Existing account, no opportunity    | Email domain matches an owned account               | Web form       | Account owner                                      | 4 business hours      |
| P-03 | Open opportunity on matched account | Domain matches, account has open opp                | API            | Opportunity owner                                  | 2 business hours      |
| P-04 | New enterprise company, in coverage | 2,000 employees, covered country                    | Web form       | Enterprise pool, capacity-based pick               | 4 business hours      |
| P-05 | Product-qualified signal            | Usage threshold crossed on a free workspace         | Product event  | Product-led sales pool                             | 24 hours from trigger |
| O-01 | Two tiers both match                | Named account that is also enterprise-sized         | Web form       | Named-account owner (higher tier wins)             | 4 business hours      |
| O-02 | Ownership vs rotation               | Existing account owner is at their open-lead cap    | Web form       | Account owner regardless of cap                    | 4 business hours      |
| B-01 | Blank routing field                 | Country empty, everything else populated            | Web form       | Triage queue, not a rotation                       | Same business day     |
| B-02 | Enrichment times out                | Segment field unresolved at decision time           | API            | Explicit missing-field branch, then triage         | Same business day     |
| B-03 | Duplicate of an existing lead       | Same email as an open lead                          | List import    | Existing lead owner, no second assignment          | unchanged             |
| H-01 | Subsidiary hierarchy conflict       | Subsidiary matched, parent owned by another rep     | Web form       | Conflict queue with dwell timer                    | 1 business day        |
| H-02 | Partner deal registration active    | Registered account arrives inbound direct           | Web form       | Channel manager review                             | 24 hours              |
| C-01 | Assigned rep out of office          | Eligible pool, next rep flagged OOO                 | Web form       | Next available rep in pool                         | unchanged             |
| C-02 | After-hours arrival                 | Arrives 02:00 in the contact's timezone             | Web form       | After-hours queue plus auto-acknowledgment         | Next open hours       |
| C-03 | Rep with no availability configured | Eligible pool, one rep never set availability       | Web form       | Not the silent fallback; explicit pool rules apply | unchanged             |
| X-01 | No rule matches                     | Country and company size both blank, unknown domain | Manual entry   | Triage queue, named owner                          | Same business day     |
| X-02 | Assignment write fails              | Valid decision, owner-field write rejected          | API            | Retry queue, decision logged separately from write | Paged to Ops          |

Run the same pack through each path the CRM can receive a lead on:

- web form
- API
- list import
- CRM sync
- chat or scheduling tool
- manual entry

An identical record must produce an identical owner on every path. A path that disagrees with the others is the single most common silent-drop cause, and it is invisible from a dashboard because both paths report a populated owner field.

Record the run:

- case
- path
- expected owner
- actual owner
- pass or fail

Keep the results alongside the change log entry.

## Rollout sequence

1. **Sandbox.** Load the pack plus edge-case records:
   - duplicates
   - incomplete fields
   - unusual attribute combinations

   Ideally replay real historical leads from the last full week. If a rule change cannot be tested against last week's inbound, it is not ready to ship.

2. **Canary, or shadow mode - a ranked choice, not an either/or.**
   - efficiency: canary > shadow mode
   - value: shadow mode > canary
   - effort: shadow mode (a week, plus a parallel compute path the CRM may not support) > canary (an hour, a scoping filter over one segment)

   Run the canary by default. Enable the new logic for one controlled segment (one region, one source, or one pool) and reconcile daily: count submissions at the source against records in the CRM, and confirm the difference is zero. Any unexplained loss triggers rollback rather than investigation-in-production.

   Shadow mode computes the intended owner on live volume without writing it, then diffs intended against current behaviour record by record. It sees every disagreement instead of only the ones one segment happens to exercise - some will be the intended fix, some new defects, and only a record-level diff separates them. That extra coverage is what the week buys.

   Shadow mode wins, despite the effort, on exactly two conditions:

   - the change moves ownership across every segment at once, so no canary can contain it
   - a wrong owner is unrecoverable rather than merely embarrassing: partner deal registration, contractual territory, a regulated-region carve-out

   Otherwise the canary's faster feedback beats the shadow's completeness.

3. **Full rollout.** Expand once the canary window shows no leads queue-owned past the acceptance SLA and no per-source volume anomalies.

**Approval and versioning:**

- propose the change as a ticket
- require a second approver for anything that changes who owns a lead
- record it in a change log with the date, the tiers touched, and the test-pack result

Sales leadership owns communicating a territory or fairness change to the reps it affects, because those changes touch quota attainment directly.

## Rollback plan

Keep the ability to restore the previous rule set as a single action, and know before shipping which state it restores to. Never edit assignment-affecting logic directly in production - a rule edited in production on a Friday is an incident waiting for Monday.

Rollback triggers, decided in advance:

- unexplained per-source volume loss
- any lead unassigned with no reason code
- catch-all volume rising above its normal band
- distribution skew outside the team's agreed variance

## Post-change monitoring

- Error alerts routed to a named owner, not a shared inbox nobody reads.
- Volume monitoring per source with alert-on-silence. Zero leads from a source on a Tuesday is a failure wearing a green checkmark; nothing in a standard CRM alerts on absence.
- Separate fields for the routing decision and the CRM write result. A correct decision followed by a failed write otherwise looks identical to a rule that never matched, which turns a one-minute query into an investigation.
- A weekly one-page report: speed-to-lead by stage, acceptance gap, never-touched count, catch-all volume and dwell, distribution per rep.
- A weekly catch-all review that converts recurring exception types into new rules, so the exception set shrinks instead of accumulating.
