# Worked examples

Both examples are this skill's own constructions (**inference**) applying the verified role definitions and the evidence rubric. Rewrite specifics for the actual deal - never reuse verbatim.

## Example 1 - a defensible B2B map

Inputs given: mid-market deal (~$80K ACV) for a workflow-automation product at Meridian Freight (450 employees), evaluation stage. Contact list with titles, three call transcripts, six weeks of email activity, CRM contact roles half-filled.

```
STAKEHOLDER MAP - Meridian Freight, $80K mid-market, Evaluation, v2

| Name | Title | Role | Evidence | Conf. | Gap unproven | Next action |
|------|-------|------|----------|-------|--------------|-------------|
| Dana R. | Dir. Ops | Champion | T1: forwarded our one-pager to the COO
  unprompted (email thread); shared the internal vendor shortlist (call 2) | High
  | Whether she'll present the case in the exec meeting we won't attend
  | Ask her to co-build + present the business case at the Nov ops review |
| Marcus T. | COO | Economic buyer (hypothesis) | T3: Dana says "Marcus decides
  anything over $50K"; T4: title fits | Medium | Never met; claim uncorroborated
  by behaviour | Dana to arrange 20-min intro; forwardable email drafted |
| Priya S. | IT Manager | Technical blocker | T2: joined call 3, asked only
  integration + SSO questions | Medium | Whether she holds veto or advises
  | Send the architecture + SSO pack this week (near-zero); hold the POC
  unless she names an objection the docs can't answer |
| Leo M. | Procurement | Approver (not yet engaged) | T4: function exists at
  this size | Low | Everything | Ask Dana who ran paper on the last purchase |
| (unidentified) | Security reviewer | Silent detractor hypothesis | Product
  touches customer data -> assume a reviewer exists | Low | Identity | Ask
  Priya: "who signs off on data handling for new tools?" |
| Jen K. | Ops analyst | User/cheerleader | T2: replies within minutes,
  attends everything | Low-Med | None load-bearing | Keep warm; not a thread |

CHAMPION TEST LOG
Asks made      : rung 1 shortlist share (done, wk 2); rung 2 one-pager forward
                 (done, wk 2); rung 3 COO intro (committed, pending)
Follow-through : forwarded one-pager same day - T1
Next ask       : rung 4 - co-build + present the business case at the Nov ops
                 review; deadline before that review
Why this rung  : rungs 1-2 passed and rung 3 is committed, the decision moves in
                 an exec meeting we won't attend, and a competitor is shortlisted
                 - the promoting condition for rung 4, which the efficiency order
                 would otherwise never reach
Verdict        : champion - but re-test at proposal stage

ECONOMIC BUYER : Marcus T. - Medium only; intro pending. If Dana defers the
intro a second time -> reading 2 (fear of exposure) suspected; countermove:
hand her a one-page EB-ready case she presents herself.

COVERAGE : 4 engaged (Dana, Priya, Jen, +CFO office cc'd) vs ~4-7 benchmark.
Real relationships: 2 (Dana, Priya). Not single-threaded, but thin above
the line. Expansion target: Marcus (power), Leo (paper).

CHAMPION RISK : redundancy - Priya, if converted from blocker; exec sponsor -
none (gap); detection - manual only (gap).

REFRESH TRIGGER: Marcus meeting happens, or proposal goes out - whichever first.
```

Why this map passes the gate:

- Every row cites its evidence and tier.
- The only High confidence rests on Tier-1 behaviour.
- The EB is named but honestly held at Medium with the proving action attached.
- A blocker hypothesis exists for someone never seen on a call.
- Single-threading is assessed on relationships, not names.
- The next ask names its rung and the condition that promoted it rather than jumping the ladder.
- Both champion-risk gaps are stated instead of papered over.

## Example 2 - the naive counter-example (do not produce this)

Same inputs. Annotations mark each failure.

```
STAKEHOLDER MAP - Meridian Freight

- Marcus T., COO - DECISION MAKER (high confidence)      <- title only (Tier 4):
  can never exceed Low; no behaviour, no claim, never met
- Dana R., Dir. Ops - CHAMPION (high confidence)         <- right person, wrong
  basis: "she's super responsive and loves the product" is Tier 2 warmth;
  no capital-costing ask has been logged, so High is unearned
- Jen K., Ops analyst - KEY INFLUENCER                   <- responsiveness
  mistaken for power; she answers fast because it costs her nothing
- Priya S., IT Manager - SUPPORTER (she attended a call) <- attendance read as
  support; her questions were all integration risk - blocker signal ignored
- No blockers identified. Everyone we've met is positive. <- maps only who is
  on calls; no hypothesis for security, procurement, or finance; the silent
  detractor is unmapped by construction
- Next step: send proposal.                              <- no per-person next
  actions, no EB verification, no coverage count, no champion risk, no
  refresh trigger - a snapshot pretending to be a map
```

The tell that distinguishes the two: Example 1 states what it does _not_ know and what will prove it; Example 2 converts optimism and titles into confidence. On identical inputs, the naive map forecasts a clean close; the defensible map predicts exactly where this deal can die (unverified EB, unmapped security review, no exec sponsor).
