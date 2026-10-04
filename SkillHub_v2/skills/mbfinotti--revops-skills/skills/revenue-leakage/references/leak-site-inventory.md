# Leak Site Inventory

Probe every site below when mapping the funnel; skipping one is how a report misses the biggest leak. For each site: the mechanism, the detection signal, and the evidence to pull.

Markers:

- **[B2B]** - assumes a rep-owned pipeline.
- **[self-serve]** - assumes a product/billing funnel.
- unmarked - occurs in both.

This is a coverage checklist, not a menu to rank - the sites do not compete for the same slot, and ranking them by likely yield before the reconciliation has run would be guessing which one leaks in this funnel. Ranking happens once, downstream, on the sized register at workflow step 6. Skip a site only when the funnel structurally has no such step, and record that it was skipped for that reason.

## Entry and capture

- **Records never created.** Inbound paths that reach no system: a demo request answered from a personal inbox, a partner referral passed verbally, a chat conversation never logged. Detection: enumerate every inbound path with the user, then check each one produces a record with a timestamp. Evidence: compare source-system volume (form submissions, chat sessions, referral emails) against records created in the same window.
- **Records created but ownerless at birth.** No fallback owner in the assignment logic, so unmatched records land in a queue nobody watches. Detection: count records with no owner or a queue owner N days after creation - derive N from the funnel's own median time-to-assignment. Evidence: owner history showing assignment never happened.

## Assignment and first response

- **Unworked leads.** [B2B] Assigned but never contacted. Detection: records with an owner and zero outbound activity inside the expected window. Evidence: activity history per record; segment by owner to separate a capacity problem from an individual one - attribute to the process (no SLA, no escalation) unless owner history proves otherwise.
- **Misassignment.** [B2B] Routed to the wrong territory, segment, or a departed owner; the record sits because nobody believes it is theirs. Detection: residuals concentrated on a few owners or on records reassigned more than once. Fix design belongs to the lead-routing skill; here it is only a leak site.
- **First-response latency.** Response so slow the record is dead on contact. Measure the funnel's own response-time-vs-conversion curve and locate the decay point in that data; do not import the circulating 5-minute/21x/100x multipliers (unsourced - see SKILL.md Ground Rules).

## Qualification handoff

- **Passed but never accepted.** [B2B] The qualifying team marks a record ready; the receiving team never accepts or rejects it. Detection: reconcile passed vs accepted-or-rejected counts per period; the residual is the leak. Evidence: handoff timestamps on both sides. A missing shared definition of "accepted" shows up as high rejection plus high residual together.
- **Handoff living in chat or email.** The pass happens as a message, not a record transition - no timestamp, no reconciliation possible. Classify as a data-capture gap and instrument before measuring.

## Mid-funnel

- **Silent stalls.** Records open far past the step's expected dwell time with no recorded reason. Stale-deal data is the input signal; the leakage question is whether the record exited economically (dead but never closed) - not whether the field hygiene is good.
- **Silent close-date or renewal-date pushes.** Dates moved repeatedly with no reason code. Detection: date-change history per record; repeated pushes without activity mark a probable dead record inflating open-in-window counts.
- **No-decision losses recorded as nothing.** Deals that ended with no decision and were never closed out. These sit permanently in "open", corrupting the reconciliation. Evidence: open records whose last buyer-side activity is older than the funnel's full cycle length.

## Late stage - paper process

- **Verbal yes to signature.** [B2B] Procurement, legal review, security review, signature routing - the leak MEDDPICC names "Paper Process". Detection: reconcile verbal-commit or proposal-stage exits against signed contracts; pull time-in-contracting per record. Often untracked because contracting happens in a signature tool or email thread that never writes back to the record - then it is a capture gap first.

## Quote-to-cash

- **Quote-to-order-to-billing mismatches.** Discounts beyond policy, negotiated terms never reflected in the invoice, usage never metered or billed, invoices drafted but never finalized. Detection: three-way match on a sample - quote terms vs order vs invoiced amount. Evidence: billing-system records against closed-won records.

## Post-sale

- **Renewal misses.** Renewals that lapse because no one owned the motion, or auto-renew terms that existed on paper but were never triggered in the billing system. Detection: reconcile contracts due for renewal in the period against renewed/churned/still-pending outcomes; the residual is the leak.
- **Expansion never asked for.** Accounts consistently over plan limits or adding seats with no expansion motion triggered. Detection: usage-over-entitlement events with no follow-up record.
- **Involuntary churn.** [self-serve, also B2B] Subscriptions ending on payment failure with no retry schedule or recovery sequence wired to the failure event. Detection: reconcile payment-failure events against recovered / retried / cancelled outcomes; a failure event whose subscription silently ends with no recovery attempt is a pure leak. Scale anchor: 20-40% of total subscription churn is involuntary (Baremetrics, citing Paddle research); 2-5% for B2B SaaS (Baremetrics platform data).

## Self-serve funnel steps

- **Trial and checkout drops.** [self-serve] Step-level drop-off inside signup, activation, and checkout. The conservation test applies unchanged: events in vs events out per step. A step with no event instrumentation is a capture gap, not a zero.

## Untracked-step probe (run at every boundary)

For each adjacent pair of systems or owners, ask:

1. What happens between these two, exactly, and who does it?
2. Does that step write a timestamped record anywhere?
3. If the person doing it went on leave tomorrow, would records queue up invisibly?

Any "a human does it by hand in an inbox/spreadsheet/chat" answer marks a suspected leak site with no measurable drop-off until instrumented.
