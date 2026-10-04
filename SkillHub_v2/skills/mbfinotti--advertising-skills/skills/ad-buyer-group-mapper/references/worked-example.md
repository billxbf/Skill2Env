# Worked Examples

Filled-in outputs in the shape defined by SKILL.md's Output shape section, plus starter per-role patterns. All angles below are illustrations of the method, not benchmarks - verify every pattern against the user's own closed-won data, call notes, and reviews before use.

## Starter per-role patterns (defaults to verify)

Practitioner-claimed defaults, not controlled evidence. Use them to seed the map when the user's own evidence is thin, and mark every row built from them as `hypothesis`.

Read the `Proof / offer type` column against the offer-type ranking in SKILL.md § Per-role output: this table says which offer fits a role, that ranking says which one to build first when you cannot build them all.

| Role                | Measured on                                                | Personal risk                                                   | Proof / offer type that fits                                            |
| ------------------- | ---------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Champion            | The pain metric the offer fixes                            | Sponsored a failed project; spent political capital for nothing | Comparison guides, business-case builders they can circulate internally |
| End user            | Daily throughput / quality of their own work               | Forced onto a tool that makes their job worse                   | Demo, free trial, hands-on content - no sales gate                      |
| Economic buyer      | Budget efficiency, ROI of the line item                    | Approved spend that produced no return; CFO scrutiny            | ROI calculators, benchmark reports, customer proof with numbers         |
| Technical evaluator | System reliability, integration cost                       | Owning the integration when it breaks                           | Technical docs, architecture pages, security whitepapers                |
| Gatekeeper-blocker  | Risk avoided: breaches, compliance findings, bad contracts | Being the one who signed off before an incident                 | Compliance certifications, audit reports, security documentation        |

## Example 1 - B2B, per-role map justified

**Input:** compliance-automation SaaS, $85K ACV, selling to mid-market fintech (200-1,000 employees), ~350 named target accounts, closed-won notes from 22 deals available, professional network + broad social, $18K/month.

**Committee summary.**

- Committee size: closed-won notes show a median of 4 distinct roles per deal (range 3-6), consistent with the TrustRadius mid-market band, well under the "6 to 10" complex-purchase figure.
- Purchase type: mostly net-new category.
- Precision verdict: 350 named accounts and $85K ACV clear both thresholds (<500 accounts, approaching $100K ACV); per-role creative is defensible.
- Trade-off declared: this map takes the precision side, since the 95-5 objection applies less when reach is already bounded at 350 accounts.

**Role map.**

| Role                                      | Evidence                                                                                 | Measured on                                  | Personal risk                                               | Likely objection                                                                       | Messaging angle                                                                                                                    | Proof/offer                                                                                                                                 | Targeting proxy                                                                                                               | Proxy size vs. floor                                                                                                                                                            |
| ----------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Champion (Head of Compliance)             | Evidenced - present in 22/22 won deals                                                   | Findings closed per audit cycle              | Sponsoring a tool that fails the next audit                 | "We already handle this in spreadsheets"                                               | "Your next audit prep in days, not quarters - without adding headcount" (verbatim from 3 call notes: "audit prep eats my quarter") | Audit-readiness checklist, ungated                                                                                                          | Account list + function: Legal & Compliance, seniority: Director+                                                             | ~2,100 - below practical floor; acceptable only because account-list ABM campaigns run on engagement objectives, flagged for mbfinotti/advertising-skills@ad-audience-targeting |
| Economic buyer (CFO / VP Finance)         | Evidenced - 18/22 won deals show finance sign-off                                        | Cost of compliance program vs. fine exposure | Approving a five-figure line that duplicates existing spend | "What does this replace?"                                                              | "One line item that retires three tools and caps fine exposure"                                                                    | ROI model comparing tool consolidation + penalty avoidance                                                                                  | Account list + function: Finance, seniority: VP+                                                                              | ~1,400 - same flag as above                                                                                                                                                     |
| Technical evaluator (Head of Engineering) | Hypothesis - appears in 9/22 notes; disproof: cut if absent from next 10 wins            | Integration and maintenance load             | Owning a brittle integration                                | "Another vendor API to babysit"                                                        | "Read-only connectors, no schema changes, sandboxed in an afternoon"                                                               | Architecture doc + sandbox access                                                                                                           | Account list + functions: Engineering AND Information Technology (cross-functional role straddles both), seniority: Director+ | ~3,800                                                                                                                                                                          |
| Gatekeeper (Security review)              | Evidenced - validation-stage security review in 14/22 notes, reopened requirements twice | Vendor risk accepted on their signature      | "New vendor, new attack surface"                            | "The vendor assessment is pre-filled - SOC 2 Type II, pen-test report, DPA on request" | Security documentation pack, ungated                                                                                               | Same account list + function: Information Technology, seniority: Manager+, reached from supplier-selection stage onward - before validation | ~2,900                                                                                                                        |

**Sequencing notes.**

- Champion and end users (merged into champion here, same people in this segment per call notes): problem identification.
- Economic buyer: business-case content engagement.
- Security pack: delivered during supplier selection, not validation, because two deals stalled when security arrived late.
- Economic-buyer and gatekeeper angles weight risk reduction over urgency: 15/22 lost-deal notes cite "decided to wait", matching the indecision pattern.

**Handoffs.** Audience construction, floors resolution, and budget: mbfinotti/advertising-skills@ad-audience-targeting. Copy per angle: mbfinotti/advertising-skills@ad-copy-variants.

## Example 2 - multi-decider household purchase

**Input:** residential solar installation, $22K average ticket, metro region, no platform decided, review mining of 180 installer reviews available.

**Committee summary.**

- Household type: two-decider (typically both partners), occasional third voice (adult child or contractor friend advising).
- Purchase characteristics: high-consideration, personal money, no formal review stages.
- Precision verdict: household-graph isolation is imprecise; run role-differentiated creative on one shared household audience instead of trying to target each member.

**Role map.**

| Role                             | Evidence                                                                                                        | Measured on (cares about)                        | Personal risk                                       | Likely objection                                                | Messaging angle                                                                                                               | Proof/offer                                                                                                                 | Targeting proxy                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Initiator-researcher (partner A) | Evidenced - 130/180 reviews name one partner as the researcher                                                  | Monthly bill reduction, doing the homework right | Championing a purchase the household regrets        | "Payback math never works out"                                  | "See your actual payback year from your last three bills" (verbatim review language: "the calculator matched our real bills") | Bill-based savings calculator, ungated                                                                                      | Geo + homeowner signals + category in-market behavior; retargeting pool from calculator use |
| Co-decider (partner B)           | Evidenced - reviews repeatedly cite "my wife/husband was worried about..."                                      | Not being locked into a bad contract             | "20-year contract with a company that might vanish" | "Rated installers, transferable warranty, no lien on the house" | Warranty terms one-pager, third-party review scores                                                                           | Same household audience - connected-TV and shared-device placements carry the risk-reduction creative to the second decider |
| User (whole household)           | Hypothesis - reviews rarely mention post-install experience; disproof: cut if next review pass confirms silence | Nothing changes day-to-day                       | (none - merged into co-decider's risk frame)        | -                                                               | -                                                                                                                             | -                                                                                                                           |

The user row is cut at the structural pass: no evidence, and its concerns are absorbed by the co-decider. Final map: two roles, two creative variants, one shared audience.

## Negative example - what not to ship

**Input:** $6K ACV email-deliverability tool, SMB buyers, no closed-won analysis, professional network, $3K/month.

**The bad map:** eight roles (CEO, CMO, VP Marketing, Marketing Ops, IT, Procurement, Legal, "Influencers") copied from a committee framework, each with its own campaign at ~$375/month, titles targeted exactly ("Director of Email Marketing"), each audience 800-3,000 people.

Why it fails every gate:

- No evidence: all eight roles are title-based inference - the weakest source - asserted, not hypothesized, with no disproof tests. TrustRadius's SMB band (2-3 people) and the ACV both predict a two-role committee.
- "Influencers" is not a role: it maps to no attribute and no angle.
- Every audience is below the ~5,000 significance floor and the 20,000-50,000 practical floor; $375/month cannot fund a learning phase anywhere.
- Exact-title targeting misses every variant of "Director of Email Marketing" the platform doesn't recognize.
- Procurement and legal do not exist as stages in a $6K self-serve purchase - they were imported from an enterprise framework, not from evidence.
- The precision thresholds point the other way: neither <500 named accounts nor >$100K ACV - one strong message to a broad marketing-function audience wins on economics.

**The fix:** two roles: champion-user in marketing, and economic buyer only as a proof point in the creative, not a separate audience. One consolidated campaign, function + seniority targeting, and a disproof test on the economic buyer ("add a finance-facing variant only if call notes show finance blocking deals").
