# Governance, legal gates, and market context

## Governance detail

**Ownership by scale.** Sales leadership owns comp design early. Ownership shifts to RevOps/Sales Ops as the org scales, with HR/Total Rewards supplying market benchmark data for OTE levels (QuotaPath 2023 survey).

Alexander Group survey data on the split:

- ~40% of companies: sales management/sales ops runs the redesign.
- ~28% of companies: a cross-functional design task force.
- Roughly half: require top-leader (CEO/COO/president) sign-off.

The scaled flow, in order: RevOps-led design, finance validation, executive sign-off.

**Steering-committee model (WorldatWork).** Three teams across six phases (plan, design, implement, administer, assess, manage):

- **Steering committee** (sales, RevOps, HR, finance): confirms the pay-for-performance philosophy and resolves cross-functional conflicts before design starts.
- **Design team:** defines structure and measures.
- **Administration team:** operationalizes tracking and owns dispute/exception handling with defined escalation paths, never case-by-case improvisation.

**Cadence.** Annual review aligned to the fiscal year. Plans carry published start and end dates, never left open-ended (Cichelli). More frequent major changes create confusion and instability, and any mid-cycle change to pay opportunities is a governance exception requiring its own sign-off.

**Back-testing and communication load.** Test the new plan against actual historical per-rep performance before rollout - it catches unintended over/underpayment and builds committee trust. Roughly 60% of reps take 3-6 months to fully understand a new plan; over-invest in rep-facing plan documentation and explanation at launch.

**Deliberate evolution is legitimate.** The annual-stability rule is a floor, not a freeze. A documented counter-example, HubSpot's early sales organization under Mark Roberge, ran three successive AE plans as deliberate strategy shifts:

1. Pure upfront payment with a clawback (churn exploded).
2. Rates tiered by each rep's customer-retention quartile.
3. The same rate, with the payout itself staggered over the customer's first year contingent on retention.

The lesson: the comp plan is a primary lever for executing a strategy change. Evolve it deliberately at the fiscal boundary, not reflexively for stability's own sake.

## Legal gates - check with counsel, never resolve in-plan

This is general information for flagging risk, not legal advice. Every item below is a gate:

- Identify whether it applies to the org's jurisdictions and rep population.
- Flag it to counsel.
- Record counsel's answer in the plan file.

Statute details and thresholds change frequently - verify current status.

1. **Written signed commission agreements.** Several US states mandate a written agreement describing how commissions are computed and paid, signed by the employee (California Labor Code 2751; New York Labor Law 191 for commission salespersons). Missing paperwork forfeits the employer's presumption on any unwritten deduction or forfeiture term.
2. **Clawback enforceability - earned vs unearned.** Once a commission is _earned_, it is generally a wage and clawing it back is an unlawful deduction; advances and unearned commissions can be recovered only when the written plan clearly defines the earning event. Defensible clawbacks are narrowly scoped (churn or non-payment within a stated window) and never exercised under "sole discretion" language.
3. **Post-termination commissions - the procuring-cause doctrine.** When the plan is silent, a rep who set the sale in motion can be owed the commission even after leaving; an "at-will" designation alone does not displace this. Only explicit plan language conditioning post-termination commissions does.
4. **Damages multipliers.** Multiple states treat unpaid commissions as wages with statutory multipliers (double, treble) plus fees - the cost of a commission dispute is a multiple of the commission.
5. **Retroactive caps.** Capping payouts after deals closed, under a plan document that said "uncapped", has been litigated: _Comin and Briggs v. IBM_ (N.D. Cal., 3:19-cv-07261) settled for $4.75M in 2023 over California reps whose commissions were capped after large deals had already closed, and _Vinson v. IBM_ (M.D.N.C.) separately allowed a claim over commissions capped at 400% of quota after they were earned - cap language and any post-hoc payout adjustment are counsel items.
6. **Pay transparency.** A large and growing set of US states require the pay range in job postings; for sales roles the good-faith range should reflect full OTE, not base alone. Coverage thresholds vary by state and remote roles are generally in scope; the cited practical approach is complying with the strictest applicable state. Transparency also raises internal-equity scrutiny - existing reps see what new-hire postings imply.
7. **Overtime exemption for inside sales.** The outside-sales exemption doesn't cover phone/internet selling, and the retail-establishment commissioned exemption rarely applies to B2B SaaS - many SaaS inside-sales reps are non-exempt by default, a widely under-appreciated gap since commission-heavy pay does not itself imply exemption.
8. **Commission-expense accounting (ASC 606 / ASC 340-40).** Incremental costs to obtain a contract are capitalized and amortized over the expected benefit period _including anticipated renewals_ - a baseline audit/IPO-diligence expectation. Renewal commissions paid at a lower rate than initial-sale commissions is itself evidence the initial commission covered the whole relationship.
9. **UK/EU commercial agents.** Termination indemnity/compensation rules protect self-employed agents selling _goods_; they typically don't reach software/services - but confirm per arrangement.
10. **B2C-specific.** Draw recovery from final paychecks (negative balances at separation) is state-law- and contract-dependent, and a recurring dispute pattern in solar and auto.

## Market shifts, 2023-2026 (dated - refresh before relying on)

- **Efficiency-era correction.** Post-2021: quotas rose, AE ramps lengthened (Bridge Group: 4.3 → 5.3 months), pay mix drifted slightly toward variable in mid-market/enterprise, and 4x-6x quota:OTE discipline returned. Treat any benchmark dated 2021-2022 as stale.
- **Usage-based pricing breaks booking-centric comp.** A majority of SaaS companies now run some usage-based pricing (Pavilion cites ~61%, 2025), so revenue materializes long after signing.

  Competing designs, with **no settled best practice**:
  - Territory profiles weighting bookings vs consumption by account maturity.
  - Consumption run-rate as the paid measure.
  - Hybrid base-plus-overage crediting.
  - Multi-year consumption-tied comp.

  Traditionalist warning: each risks turning comp into an annuity that stops tracking new selling effort. Present the camps, don't pick one as industry standard.

- **AI compression of the SDR role.** Prospecting automation is shifting SDR comp toward qualified-opportunity and sourced-pipeline quality gates over raw activity - and reshaping ICM tooling itself (AI plan optimization, anomaly detection).
- **Transparency pressure.** Posted OTE ranges compress the informational advantage that used to justify wide pay-mix variance between similar companies.

## ICM tooling - integration note

**What the tools automate:**

- Commission calculation.
- Crediting.
- Dispute/inquiry workflows.
- Rep-facing statements.
- ASC 340-40 amortization schedules.
- Plan modeling/back-testing.

**What no tool substitutes for:**

- Measure selection.
- Pay mix.
- The quota:OTE ratio.
- Accelerator break points.
- Crediting rules.
- The strategic steering of the plan - the judgment in SKILL.md.

Plan _management_ is the differentiator once design is done, tracked through standing health signals:

- Attainment distribution.
- Payout volatility.
- Exception volume.
- Dispute counts.
- Time-to-close on commissions.

Vendor landscape by buyer size (citation only; analyst placements and per-seat prices below are secondary-relayed and change - verify before quoting):

- **Lightweight/SMB tier:** QuotaPath, Visdum, Palette, Core Commissions.
- **Mid-market:** Everstage, CaptivateIQ, Performio.
- **Enterprise suites:** Xactly, Varicent, SAP SuccessFactors Incentive Management, Oracle, beqom, Forma.ai.
- **CRM-native:** Salesforce Spiff/Incentive Compensation Management.
- **Planning-led adjuncts:** Anaplan, Pigment, usually paired with a dedicated comp engine.

Enterprise pricing in this market is not publicly documented - never quote a number for it.
