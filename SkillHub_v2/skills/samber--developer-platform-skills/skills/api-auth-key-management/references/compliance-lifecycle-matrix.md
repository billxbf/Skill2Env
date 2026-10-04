# Compliance lifecycle matrix

Framework-by-framework detail behind step 7 of the workflow: what each regime actually requires of a key lifecycle, and the product features that pressure produces.

## When each regime applies

| Trigger                            | Regime pulled in        | Nature of the obligation                                                                                                 |
| ---------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Handling payment / cardholder data | PCI-DSS 4.0/4.0.1       | Legal/contractual - prescriptive requirements, mandatory since April 1, 2025 for the 8.6.x set                           |
| Selling to enterprise customers    | SOC 2 (usually Type II) | Commercial - the buyer's procurement/security review demands the report even when the seller's own risk profile wouldn't |

Ask about both in the interview; either one flips lifecycle governance from good practice to required.

## SOC 2: policy plus operating evidence

SOC 2 prescribes no tool and no cadence. Under the Trust Services Criteria - CC7.2 and Confidentiality C1.2 - it expects a **documented policy covering the full secret lifecycle**: provisioning, rotation, revocation, destruction. What the auditor checks is evidence the policy operates, not that it exists:

- Key-management logs: every key-related action recorded with who, what, when.
- Periodic access reviews and change-management approval records for privileged key actions.
- Demonstrable, regular rotation - actually performed, not just scheduled.
- Role definitions and ACLs governing who may create, rotate, or revoke keys.

**Type II is the trap to design for**: controls must operate consistently across a 3-12-month observation window. A policy adopted the week before the audit satisfies Type I (point-in-time) and fails Type II by construction - which is why automated, continuous evidence generation matters more than any individual control.

## PCI-DSS 4.0/4.0.1: prescriptive, but not a fixed interval

The common assumption that PCI mandates "rotate every 90 days" is wrong - correct it explicitly. Requirement 8.6.3 (wording consistent across eight independent named QSA/compliance sources - Raidiam, BDO, SecurityMetrics, VISTA InfoSec, StudySection, Microsoft Learn, Schellman, PCI Guru - all converging on the same substance, zero variance, and the same March 31, 2025 mandatory date). PCI SSC blocks automated access to its own standard document, so the quote below is triangulated across the independently-published sources named above rather than read first-hand from PCI SSC's own text; a reader who needs the literal PCI SSC sentence for a contractual or audit citation should download the PDF directly from PCI SSC's own document library, which requires no account:

> "Passwords/passphrases for any application and system accounts are protected against misuse as follows: Passwords/passphrases are changed periodically (at the frequency defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1) and upon suspicion or confirmation of compromise. Passwords/passphrases are constructed with sufficient complexity appropriate for how frequently the entity changes the passwords/passphrases."

Read as three obligations:

1. **The organization justifies its own cadence** via a documented targeted risk analysis (Requirement 12.3.1) - there is no fixed-interval rule to point at, and an auditor will ask for the analysis document itself.
2. **Compromise-triggered rotation is unconditional** - immediately on suspicion or confirmation, regardless of the analyzed cadence.
3. **Complexity must match cadence** - slower rotation demands stronger keys (the 120-bit entropy floor from step 1 satisfies this trivially).

These 8.6.x requirements became mandatory on April 1, 2025 (best-practice-only during the 4.0 transition before that). Separately, PCI requires all API/payment transactions logged in a **tamper-resistant** manner, retained a **minimum of 12 months**, with the most recent 3 months immediately accessible - not archived to cold storage.

## From audit expectation to product feature

State this as a design rule, not a compliance footnote: each auditor expectation maps to a feature mature platforms ship, and building the feature is what generates the evidence.

| Auditor expectation                        | Product feature it forces                                                                                                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Stale credentials cannot persist silently  | Mandatory expiration (GitHub fine-grained PATs must expire; org policies can cap maximum lifetime)                                                                             |
| Regular rotation demonstrably happened     | Expiry warnings and forced-rotation reminders - evidence generated without relying on human memory                                                                             |
| Every key operation reconstructable        | Audit log of create (who/when/why), use (when/where/which endpoints), rotate (grace window, initiator), revoke (when/why); retained 90 days to 12+ months depending on regime  |
| Offboarding and access reviews enforceable | Service accounts and org-owned keys - decoupling credentials from individuals is itself an access-review control, not only a UX choice                                         |
| Least privilege as the default posture     | Restrictive-by-default scoping - simultaneously the security best practice and the literal evidence SOC 2 access-control criteria and PCI least-privilege requirements ask for |

## Documentation obligation either way

Whichever authentication mechanism the boundary decision lands on (static key or OAuth), document the rationale - auditors ask why the mechanism was chosen, and "it was already there" is a finding.
