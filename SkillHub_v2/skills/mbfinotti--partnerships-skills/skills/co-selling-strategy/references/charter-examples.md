# Charter Examples

One worked charter and one annotated failure. Every number below is derived from a specific input in the situation described, not a default - re-derive each value from the user's own cycle length, ACV, partner mix, and comp structure rather than copying these.

## Worked example: mid-market B2B SaaS, reseller + SI mix

Situation: $40k ACV, 100-day average sales cycle, proven direct motion, two partner types (resellers, SIs), goal of growing partner-sourced pipeline.

```
CO-SELL OPERATING CHARTER - <company>, <date>
Scope            : Resellers + SIs, mid-market segment. Account classes: named-account list
                   (top 20) direct-only regardless of registration; all else shared-pursuit.
Process track    : Lightweight playbook-fill per reseller (90-min working session, fixed
                   5-section template); heavyweight JBP reserved for the one strategic SI.
Attribution      : Sourced vs influenced tracked separately; sourced test = "would the deal
                   exist without the partner?"; attribution locks 14 days after deal creation.
Registration     : Grants price protection + pre-sales engineering access + priority support.
                   Window 90 days (cycle is 100 days; 90 > 75% rule), one 30-day extension
                   on documented activity. Approval within 48h. Rejection grounds, published,
                   closed list: (1) duplicate registration, (2) account already in active
                   direct pipeline or an existing customer, (3) account on the named-account
                   list, (4) not qualified - no budget, timeline, or decision-maker access,
                   (5) no verifiable partner relationship with the account, (6) thin
                   submission with no evidence of value-add activity. Every rejection
                   carries its reason.
Credit & comp    : Comp-neutral via quota retirement - partner-attached revenue retires rep
                   quota dollar-for-dollar; partner margin absorbed at company level, never
                   passed to rep commission. Multi-party split decided at registration, not
                   at close. Signed off by Finance and CRO.
Decision rights  : Registration approver: partner operations lead (no quota impacted).
                   First-pass dedup/territory check: channel ops, automated. Attribution
                   co-owned by Partnerships + RevOps, reconciled monthly. Disputes:
                   RevOps adjudicates within 5 business days, registration timestamp as
                   tiebreaker. RoE document owner: VP Partnerships, CRO co-sign
                   (user-decided - no industry default exists).
Engagement rules : Direct AE pulled in when a registered deal passes discovery; SI engaged
                   on any deal with an implementation component. Named-account exceptions
                   listed above. Escalation: automated flag -> channel ops review ->
                   RevOps adjudication.
KPIs & review    : Sourced pipeline share and influenced revenue share (tracked separately),
                   attach rate, time-to-approval vs 48h SLA, dispute rate. Quarterly review;
                   flag any partner exceeding ~30% of channel revenue.
```

Why it passes the checklist:

- Every decision-rights cell names a role with no competing quota.
- The window clears the 75%-of-cycle rule.
- The rejection grounds are a published closed list, each one verifiable from the registration record.
- The two clocks are kept apart: 48h to approve a registration, 5 business days to adjudicate a contested one.
- Comp neutrality is funded and signed off.
- A rep can test any deal against the rules in one read.

## Negative example: the charter that causes the conflict it was meant to prevent

Each line below is a real, sourced failure pattern - annotations in brackets.

```
Scope            : "All partners, all segments."
                   [No account classes, no named-account exceptions - every deal is
                   potentially contested ground.]
Registration     : 30-day window on a 120-day sales cycle; approval "as fast as possible";
                   rejection reasons decided case by case.
                   [Window at 25% of cycle punishes partners for the vendor's own cycle
                   length; unpublished rejection grounds make every rejection look
                   political; slow ad-hoc approval is itself what drives land-grab and
                   duplicate registrations.]
Credit & comp    : Partner deals pay reps 50% of normal commission; the 3% marketplace fee
                   is deducted from rep commission on marketplace deals.
                   [The canonical adoption killer: a rep who loses credit when a partner
                   attaches will never say yes, and reps route around the marketplace.]
Decision rights  : "Registrations approved by the VP of Direct Sales. Credit splits
                   negotiated between the rep and the partner manager on each deal."
                   [Approver's own quota is affected by the decision - structural conflict
                   of interest. Per-deal negotiation with no lock or SLA is how reps end up
                   spending selling time arguing splits instead of selling.]
Engagement rules : Registrations visible in the partner portal.
                   [The portal the sales team never opens: direct AEs are blindsided,
                   neither informed nor consulted - the documented origin point of
                   channel conflict.]
Attribution      : "Partner influence recorded at close by the partnerships team."
                   [Claims made after the outcome is known are unprovable and political;
                   partnerships as sole owner makes the number look self-serving.]
```

The fix is not better dispute handling downstream - it is rewriting these lines upstream so most disputes never form.
