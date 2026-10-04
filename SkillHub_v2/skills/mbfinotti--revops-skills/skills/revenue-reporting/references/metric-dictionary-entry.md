# Metric dictionary entry - shape and worked example

## Entry shape

Every spine metric gets one entry with exactly these fields. The dictionary is versioned; a change to any field is a new version with a dated note, and the next report footnotes it.

- **Metric**: canonical name and any aliases in circulation.
- **Question it answers**: one sentence; if none, the metric leaves the spine.
- **Formula**: exact arithmetic, including the window.
- **Inclusions / exclusions**: every contested rule (reactivation, netting, base exclusions, windows), resolved in writing.
- **Source of truth**: which system's record wins at which stage, per the field-ownership rules in `mbfinotti/revops-skills@crm-data-governance`.
- **Owner**: the person accountable for the number being right (not the presenter).
- **Cadence and window**: how often computed, over what trailing period.
- **Version**: number, date, and one-line changelog per revision.

## Worked example

**Metric**: Net revenue retention (NRR). Aliases: net dollar retention, NDR.

**Question it answers**: does the existing customer base grow on its own, before any new business?

**Formula**: (starting recurring revenue of the cohort + expansion - contraction - churn) / starting recurring revenue of the same cohort, computed monthly and reported as the trailing-12-month figure.

**Inclusions / exclusions**: cohort is every customer active at the window start; customers acquired inside the window are excluded from both numerator and denominator. One-time fees, services, and variable overage excluded from the recurring base. Same-product seat changes net within the period; a customer dropping product A while adding product B books a contraction line and an expansion line separately. Reactivations within 90 days of churn count as this cohort's expansion; later returns count as new business (resolved 2026-01, do not re-litigate per period).

**Source of truth**: billing system for recurring amounts; CRM for account identity and segment; the ledger wins any dispute on recognized amounts.

**Owner**: RevOps analytics lead computes; finance certifies.

**Cadence and window**: monthly compute, trailing-12 reported; the monthly point-in-time series lives in the appendix only.

**Version**: 1.2 (2026-01) - reactivation rule added; 1.1 (2025-07) - overage excluded from base; 1.0 (2025-02) - initial.

## What a bad entry looks like

"NRR = net revenue retention, standard formula, from the dashboard." No cohort rule, no window, no exclusions, no owner - which means every producer computes it differently, and the first time two artifacts disagree the meeting becomes a definitions debate. The entry above exists precisely so that debate happens once, in writing, and never again in the room.
