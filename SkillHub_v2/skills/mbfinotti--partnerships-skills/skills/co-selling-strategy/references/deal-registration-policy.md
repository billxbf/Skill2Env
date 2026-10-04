# Deal Registration Policy and Rules of Engagement

Citations name the publishing vendor or consultancy so single-source claims stay auditable. Treat vendor-content items as one practitioner's convention unless corroborated.

## The four decisions a registration policy must make

Converged core structure of a registration policy document (PartnerStandard deal-registration guide - consultant content):

1. **Protection-window duration** - how long a registration shields the partner, plus extension triggers.
2. **What registration grants** - customer protection plus a defined support bundle, never protection alone.
3. **Approval criteria and SLA** - response timeline and who decides.
4. **Dispute resolution** - tiebreaker rules and escalation path.

The same source's framing is worth repeating to users: "the form is not the point - the trust the form creates is."

## Protection windows

Reported ranges vary by context - present as a range, not a fixed rule (ZINFI, xAmplify):

| Context                                  | Typical window             |
| ---------------------------------------- | -------------------------- |
| SMB / general deals                      | 30-90 days                 |
| SaaS standard                            | 90-180 days                |
| Enterprise / complex                     | 90-180 days                |
| Named/strategic account-level protection | up to 12 months, renewable |

One vendor (xAmplify) proposes a tiered 90/180/365-day schema by segment - a single vendor's proposal, not observed universal practice.

- **Rule of thumb: set the window to at least 75% of average sales-cycle length.** This is the load-bearing sizing rule. A window shorter than the cycle punishes partners for the vendor's own cycle length.
- Published real-world example: Check Point runs a 90-day registration, extendable once by 30 days (120-day max), with reminder emails 30 days before expiry.

## What registration grants

Two grant types, ranked by value per unit of effort: `non-price bundle > additional discount`. On effort they invert - `additional discount > non-price bundle` - because a published discount is the harder commitment to reverse, not the harder one to write.

- **Non-price bundle**: pre-sales engineering access, co-marketing support, priority deal support. Costs internal hours per registered deal and is adjustable per partner without renegotiating anything.

  For partner types that don't earn on margin (SI/consultancy, ISV/tech, referral, marketplace), it is the entire value of registering: a margin-only grant gives them no reason to register at all. Best ratio, and the default grant for every partner type.

- **Additional discount**: commonly cited at **5-15%** beyond standard partner pricing for registered deals (rework.com). Recurring margin on every registered deal, published to the channel and effectively irreversible once granted. For resellers, VARs and distributors it outranks the bundle on value, since margin _is_ their economics - that is the one context where the ordering flips.

For SI, ISV, referral and marketplace partners, **delete the discount from the menu** rather than offering it at a lower rate: they do not earn on margin, so it buys no registration behaviour at any level.

## Approval: criteria, SLA, separation of powers

- Recommended default: **48-hour approval SLA** (PartnerStandard). The same source recommends three published rejection grounds. Prefer the fuller canonical list held by `mbfinotti/partnerships-skills@partner-channel-conflict` - a short list reads cleaner but pushes every unlisted case into approver discretion, which is the thing the published-grounds rule exists to remove.
- Documented approver convention (Oracle PRM docs; Fullcast):
  - The channel account/sales manager approves, typically on a 24-48h SLA.
  - **Channel operations** runs the first-pass review (duplicate and territory-conflict checks, often automated).
  - Administrators hold override authority to revert mistakes.
- **Separation of powers**: the approver must not be someone whose quota is affected by the decision. Direct sales leadership approving registrations that block direct reps' credit is a structural conflict of interest - approval authority belongs with partnerships/channel ops, separated from the competing P&L (PartnerStandard - consultant content, but the strongest governance principle in this literature).
- Initial approval rate and time-to-approval are not benchmarked across the industry: set targets from the program's own history rather than an external number. The one numeric SLA convention in circulation covers dispute adjudication (below).

## Rejection grounds actually used

Common published grounds (ZINFI):

- Duplicate registration: account already active in the CRM or assigned to a direct rep.
- Territorial conflict.
- Insufficient proof of value-add or genuine partner engagement - "just forwarding a name." One source reports ~12% of submissions denied on this ground.
- Speculative land-grab: the partner has no real relationship with the account. Ease of registration must be balanced against this abuse, since slow or manual approval itself causes land-grab and duplicate-claim behavior.

## Escalation ladder for contested deals

Consistent across sources (Forecastable, rework.com):

1. Automated duplicate/conflict detection by account name or domain.
2. Flag to channel/partner ops for manual review.
3. The documented, timestamped registration record serves as evidence of the first-mover claim.
4. Revenue-operations adjudication under a defined SLA - the one concrete number in the literature is a **5-business-day dispute-adjudication SLA** (Forecastable).
5. Attribution locks **14 days after deal creation** to prevent late, opportunistic credit claims.

Resolution options when two parties both claim an opportunity: award-to-one, co-registration with a defined split, or reject-both (rework.com). Deliberately not ranked - which one applies is settled by what the registration record shows about each claimant, not by effort or payoff, so an efficiency order here would be false precision. The tie-break rules that do decide it belong to `mbfinotti/partnerships-skills@partner-channel-conflict`.

## Rules-of-engagement document sections

Converged across ZINFI, Impartner, and Gradient Works - a genuine, widespread practice, not one vendor's invention:

1. Account/territory ownership rules: direct-only, partner-only, open/shared-pursuit with priority rules.
2. Lead/deal registration process - how a partner formally claims an opportunity.
3. Deal protection policy - criteria for a _valid_ registration: named contact, confirmed buying intent, active partner involvement, not a company-name drop.
4. Approval/rejection SLA and the conflict-resolution ladder.
5. Conflict escalation process - a predictable governance path, not ad hoc negotiation.
6. Lead distribution and brand-representation rules.
7. Review/update cadence.

Plus, per other sources: co-sell trigger conditions (when direct-team support gets pulled in) and named-account exceptions reserved for direct regardless of registration. A real published example exists: HubSpot's partner-program sales rules of engagement are public and worth reading as a reference artifact. Forrester also sells a "Mitigating Channel Conflict: Rules of Engagement" report - analyst-grade but paywalled.

Ownership of the rules-of-engagement document itself has a practitioner convention rather than a settled industry standard: partner or ecosystem leadership owns the framework, co-designed with sales, customer success, revenue operations, and legal - ownership meaning maintaining the model, monitoring adherence, and driving updates, not making decisions alone (per The Pedowitz Group). This lines up with the comp-plan linkage's CRO/sales-leadership co-sign-off, but is one consultancy's stated pattern, not a measured industry norm - the user still decides it explicitly for their own org rather than inheriting a default.
