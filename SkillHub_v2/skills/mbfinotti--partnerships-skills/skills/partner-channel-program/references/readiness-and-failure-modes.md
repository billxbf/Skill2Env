# Readiness Gate and Failure Modes

## The full readiness gate

Ask these before any design work. The gate exists because the single best-documented failure cause is launching a partner program to compensate for a direct motion that is not yet repeatable - "partners do not solve a broken direct motion; they amplify a working one."

1. Can you clearly explain your ideal customer?
2. Have you proven direct sales closure capability - not one heroic founder deal, a repeatable motion?
3. Is your go-to-market consistent and repeatable enough for a third party to copy? (Sales, onboarding, support processes a partner could actually replicate.)
4. Does your ACV support human-heavy partner work? Very low ACV funds referral-only at most; reseller and systems-integrator motions need materially more, because the partner's own cost of sale has to clear before yours does.
5. Are you expecting partners to solve a growth problem? **A "yes" here is a disqualifier by itself.**
6. Is there organic momentum - partners already servicing your customers, inbound requests to resell or integrate? No external interest at all suggests there may not be enough value for both parties yet.
7. Is there internal support: a named executive sponsor who will defend the program in cross-functional meetings, and access to sales, product, and success resources? A practitioner heuristic holds that the single most predictive failure indicator is whether the revenue chief actively defends the partner program.
8. Can gross margin fund partner margin and still leave the vendor a business?
9. Opportunity cost: what else could the company invest in right now instead?

No fixed quantitative launch checklist exists: readiness varies with market, product, and go-to-market maturity, so the call is a judgment made against the questions above. What is fixed: any disqualifier above means "not yet." Say so, name what must change, suggest the lighter motion that still fits (often referral-only or plain integration partnerships without a formal program), and stop.

## Failure catalog for existing programs

Structural causes first; tooling is rarely the reason a program dies - "the software is rarely the reason a partner program ends; the program is." This catalog is grouped by mechanism and its row order carries no priority: when several failures apply at once, fix them in the order ranked in SKILL.md's Diagnosing an Existing Program section.

| Failure mode                   | Mechanism                                                                                                                                                                | Fix                                                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Paper partnerships             | Agreement signed without either side knowing how they benefit each other; dies 60-90 days into onboarding                                                                | Validate a partner value proposition per partner before signing; no validation, no signature                  |
| Recruitment over activation    | Signed-partner count tracked instead of active-after-90-days; the vanity metric masks a dead program                                                                     | Stop recruiting; make activation the core metric; mutual action plan per partner                              |
| Cosmetic tiers                 | Badges with no economic differentiation at the boundary; partners notice fast                                                                                            | Rebuild criteria + benefit delta as a pair, or drop to a single tier honestly                                 |
| Unclaimed program funds        | Roughly half of allocated market-development funds go unredeemed (weakly sourced but widely repeated): claims friction, activities that don't match how partners operate | Design funds and deal registration together under one owner; funded leads get automatic registration approval |
| Reversed enablement sequencing | Shipping dozens of decks and a 200-page reference on day one                                                                                                             | Minimal launch kit: pitch deck, demo script, pricing sheet, 1-2 battle cards, one case study                  |
| House-account conflict         | Vendor keeps reserved accounts and competes on registered deals; partners stop registering and the program dies from inside                                              | Honor registration without carve-outs; write the conflict policy before the first selling partner             |
| Overloaded partner managers    | Portfolios beyond the sustainable ~10-20 active resellers per manager; engagement collapses into triage                                                                  | Cap portfolios in the architecture; fund headcount before recruiting past the cap                             |
| Annual-operating-plan trap     | A 50-page plan written in Q4, ignored after Q1                                                                                                                           | One-page quarterly mutual action plan with named owners on both sides                                         |
| Advisory-board theater         | A standing forum with no undecided topics on the agenda; false consultation without obligation to act                                                                    | Convene only with genuinely open questions; publish what will and won't be acted on                           |
| Misaligned ownership           | Channel under the sales chief inherits quarterly KPI horizons; a function that matures over 2-3 years gets killed at its first budget review                             | Reset the reporting line or explicitly contract a multi-year horizon with leadership                          |
| Penalized direct reps          | Reps compensated less on partner-involved deals block those deals                                                                                                        | Compensation neutrality on partner deals - an architecture decision, set before launch                        |

Widely cited failure-rate statistics ("70% of partnerships fail within two years") are anecdotal or secondhand. Do not present them as established fact. The "roughly 80 of every 100 recruited partners go inactive" figure is one practitioner's estimate: credible, not rigorous.

## Negative example - what not to do

A $4k-ACV SaaS vendor with flat direct sales launches a reseller program: four metal tiers, a 30% margin table copied from a competitor, a partner portal, and a recruitment target of 100 signings in year one.

Every architecture decision here is a documented failure:

- Partnerships deployed to fix a broken motion.
- An ACV that cannot fund a reseller's own cost of sale.
- Margin copied instead of derived from work the partner takes over.
- Tiers before any validated partner value proposition.
- Recruitment volume as the success metric.
- A program judged, and killed, at month 9 on direct-sales timelines.

The correct output for this user is the gate's "not yet": fix the direct motion, consider referral-only in the interim, and revisit when ACV and repeatability support more.
