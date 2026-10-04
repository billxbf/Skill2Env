# Ecosystem readiness gates and complementor economics

Two instruments. The gates decide whether to open anything at all; the worksheet decides whether anyone will build once you do. Report every gate as pass, fail or unknown - an unknown carries a resolver and a date, and never counts as a pass.

**Where the numbers come from.** Every count and cut-off on this page is a default this skill sets so the gate can be argued about, not an industry benchmark. Replace any of them with your own historical data when you have it, and record that you did.

The gates take their concepts from named work:

- Yegge on externalizable interfaces (G2).
- Spolsky on commoditizing complements (G4).
- Eisenmann/Parker/Van Alstyne on envelopment (G6).
- Adner on complement readiness (G7).

## Contents

- The seven gates
- Complementor economics worksheet
- Scoring the worksheet
- Value-share principle

## The seven gates

### G1 - Counted demand

**Pass**: at least five specific complements requested by named customers in the last two quarters, with at least two requested by more than one customer.

**Evidence, best first**:

1. Unsupported glue customers already built.
2. Requests you refused.
3. Deals slowed or lost for a missing complement.
4. Feature requests.
5. Sales anecdotes.

**Fail means**: no market for complements exists yet. Stay at rung 1–2 and re-run in two quarters.

### G2 - Externalizable interfaces

**Pass**: the capability complementors need is already reachable through an interface you would be willing to publish unchanged, and your own features use it.
**Fail means**: the platform work is an architecture project, not a partnership project. Cost it as such before promising dates.

### G3 - Identified builders

**Pass**: you can name at least three real organizations or teams - not personas - with a reason of their own to build, and you have spoken to two of them.
**Fail means**: supply is hypothetical. Test it with interviews before designing surfaces.

### G4 - Commoditized complement, not commoditized core

**Pass**: abundance of the complement raises demand for what you sell.
**Fail means**: the ecosystem would turn your product into the cheap layer. Refuse it explicitly and record the reasoning.

### G5 - Staffing

**Pass**: the standing obligations of the chosen rung have named owners and committed capacity for the next four quarters - not a launch project team.
**Fail means**: pick the rung below.

### G6 - Envelopment exposure

**Pass**: you can name the larger platform most able to bundle your category and state what makes your ecosystem non-generic to it - proprietary data, workflow ownership, a regulated surface, an install base it cannot reach.
**Fail means**: the complements you attract may be building for your successor. Not automatically disqualifying; it caps how much you should invest.

### G7 - Complement readiness

**Pass**: every external dependency the bet needs - standards, adjacent vendors' APIs, customer-side prerequisites - either exists today or has a dated, credible arrival.
**Fail means**: the launch date is a guess. Sequence around the slowest dependency.

## Complementor economics worksheet

Fill one column per builder archetype you are counting on. Numbers may be rough; ranges are fine, blanks are not.

| Line                                                         | Independent software vendor | Agency / integrator | Customer's internal team |
| ------------------------------------------------------------ | --------------------------- | ------------------- | ------------------------ |
| Reachable customers wanting this complement                  |                             |                     |                          |
| Expected attach rate                                         |                             |                     |                          |
| Their revenue per customer (licence, hours, or avoided cost) |                             |                     |                          |
| Annual return to them                                        |                             |                     |                          |
| Build cost (person-weeks)                                    |                             |                     |                          |
| Annual maintenance cost, including migrations you force      |                             |                     |                          |
| Their best alternative                                       |                             |                     |                          |
| Net return versus alternative                                |                             |                     |                          |
| What they need from you that you are not offering yet        |                             |                     |                          |

## Scoring the worksheet

- At least one archetype must show a clearly positive net return against its alternative. If none does, the ecosystem has no supply and no messaging fixes that.
- If the only positive column is the customer's internal team, you have an extension-point case (rung 4), not an app-ecosystem case (rung 5).
- If the positive return depends on you sending customers to them, that traffic is part of the offer - write it into the obligations, not into the pitch.
- Recompute after any change to the take-rate, the migration schedule or the category crowding rules; all three move the result.

## Value-share principle

Set this before any rate exists. These four are principles this skill asserts, not measured results - argue with them explicitly rather than treating them as settled:

1. The surplus left with the complementor must make building on you the rational choice against their alternative.
2. Keep the take-rate at zero until liquidity is real - a tax on a market that does not exist yet only deters the supply you are trying to recruit.
3. Crowding a category is a value transfer from complementors to you; do it deliberately, and say so.
4. When you eventually charge, charge for something that grew because of you - distribution, billing, trust - not for the right to exist on your surface.

Rates, billing mechanics and listing economics are downstream execution, not part of this decision.
