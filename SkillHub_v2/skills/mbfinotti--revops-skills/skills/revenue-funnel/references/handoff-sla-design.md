# Handoff and SLA Design Mechanics

The model-level design of the funnel's three cross-functional handoffs. Execution of any single handoff belongs to the sibling skills named in SKILL.md's Reference section.

## The Paper-Mapping Exercise

Put both sides of a handoff in one room and map the funnel on paper - the complete journey from first marketing touch to expansion - marking every handoff point with who is responsible, the criteria, and where it breaks in practice. Practitioners report the biggest alignment gaps surface in the first 30 minutes, which makes this the mandatory cheap first step before any SLA infrastructure is designed. A widely repeated framing of what it catches: misaligned handoffs run "like a relay race where both runners are sprinting in opposite directions."

## Bilateral SLA Structure

A one-sided SLA is not an SLA. Structure every handoff agreement with obligations both ways:

- Marketing commits to what it delivers (volume, criteria, data completeness); sales commits to what it does with it (acceptance window, follow-up, disposition with reason codes).
- Document the consequence, not just the commitment: if sales misses the follow-up window, marketing is not accountable for that lead's conversion; if marketing sends leads below agreed criteria, sales carries no follow-up obligation on them.
- Set initial targets close to current baseline. An aggressive target nobody can meet destroys the SLA's credibility immediately.
- Operationalize triggers as behavior-based criteria, not a single point-score threshold.

**Representative timer structure** (adapt to the user's cycle, never copy blind): sales accepts or rejects each qualified lead within 8 working hours or it auto-reverts to marketing for nurture/redistribution; it advances to sales-qualified within 4 days or reverts again. CRM activity is the elapsed-time counter; unaccepted leads escalate to the sales manager, reroute, or return to marketing.

## Governance Cadence and Versioning

- RevOps watches live response times, data completeness on handed-off records, and rejection reason codes as the early-warning layer.
- Both teams review accepted/rejected/recycled volumes and disputed dispositions monthly.
- Leadership - the funnel council - re-ratifies definitions and targets quarterly. Council membership, decision rights, and the change-control process live in the governance charter artifact.
- The SLA itself is versioned, with old versions kept for audit. Enforcement, not definition, is the usual failure point: an SLA nobody reviews is just a document, so compliance metrics sit on a standing joint agenda, not in a drawer.

**RevOps scope discipline as the owner of this machinery:** own revenue-workflow definitions, definition governance, systems configuration and change control, commercial analytics, and operational enablement. Never own segmentation, ICP definition, offer bets, or pricing posture - those belong to commercial leaders. Owning the definitions and instrumentation while a commercial leader owns the strategy those definitions measure is what keeps accountability from corrupting.

## The Sales-to-CS Handoff as a Data Contract

At the model level this handoff is a data contract, not a meeting. Required payload:

- Buying-group roles
- Identified pain and its metrics
- Compelling event
- Success criteria
- Implementation scope
- Renewal risk factors

The account executive documents renewal risk during the sale so the CSM inherits a risk profile, not just a revenue number.

Enforce with an assignment gate: CS ownership confirms only after the handoff document is completed and reviewed, with RevOps tracking document completeness to spot recurring gaps. The CS-to-sales return path (renewal/expansion) mirrors it: defined expansion signals, a named owner for the expansion opportunity, and an agreed point where CS hands a qualified expansion back into the pipeline.

## Directional Evidence, Not Promises

Formal marketing-sales alignment SLAs correlate with stronger reported program ROI (65% of companies with them report strong ROI in HubSpot State of Inbound data), and analyst-cited research on aligned revenue operations reports roughly 19% faster growth and 15% higher profitability. Quote these as directional support for investing in the handoff layer - never as an outcome to promise a specific company.
