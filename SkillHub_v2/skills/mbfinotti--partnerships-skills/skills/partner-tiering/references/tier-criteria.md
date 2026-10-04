# Tier Qualification Criteria

What earns a tier, over what window, and how to keep it undisputable. Decide criteria before benefits - criteria fix the population each benefit bundle gets promised to.

## The criteria menu, ranked by ranking power per unit of effort

Rows run in efficiency order, best ratio first. Effort here is data availability and the audit or adjudication each criterion commits you to - never a budget.

- efficiency (best ratio first): `sourced revenue > certified headcount > managed revenue/GRR > competencies > influenced revenue > CSAT`
- value (ranking power that survives a dispute): `competencies > managed revenue/GRR > sourced revenue > CSAT > certified headcount > influenced revenue`
- effort (heaviest first): `competencies > CSAT > influenced revenue > managed revenue/GRR > certified headcount > sourced revenue`
- compliance cost (heaviest first): `CSAT > competencies > influenced revenue`; the other three run on records the program already keeps and carry none.

| Criterion                         | What it measures                                | Gameability                           | Effort to run                                                  | Notes                                                                                      |
| --------------------------------- | ----------------------------------------------- | ------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Sourced revenue                   | Deals the partner originated                    | Low when verified in the vendor's CRM | Near-zero - the CRM already holds it                           | Production points systems weight sourced above assisted and managed                        |
| Certified headcount               | Individuals holding current certifications      | Low - auditable                       | Near-zero once a certification registry exists                 | Expire stale certs: one vendor stops counting expired certifications immediately           |
| Managed revenue / retention (GRR) | Health of the partner's installed book          | Low                                   | About a week - retention has to be computed per partner book   | The strongest top-tier gate - one major program requires >=80% GRR for its top earned tier |
| Competencies / specializations    | Validated, audited delivery depth               | Low - vendor-audited                  | A standing job - someone audits delivery evidence every cycle  | The direction of travel: one vendor cut ~170 badges to 28 competencies in 2026             |
| Influenced / co-sold revenue      | Deals the partner touched but didn't originate  | Medium - attribution disputes         | A standing job - every contested touch is adjudicated          | Require a verifiable touch, not a claim                                                    |
| CSAT / customer outcomes          | Measured satisfaction of partner-delivered work | Medium - respondent selection         | A standing job - a survey program you run, not one you receive | Gate on vendor-run surveys, never partner-collected ones                                   |

Compliance cost, concretely:

- **CSAT**: surveys reach the partner's customers, so consent and data-handling review comes before the first send, and a survey you must stop running is a criterion you must stop demoting on.
- **Competencies**: audits need the partner's project evidence under NDA.
- **Influenced revenue**: attribution rules have to survive the appeals path with legal reading them.

Default: open every design with sourced revenue plus certified headcount - both come from records the program already holds, so they cost a query. Add the GRR gate at the top tier as soon as retention exists per partner book.

Deleted, not demoted: raw self-reported pipeline and joint-business-plan contribution. They are the documented gaming vector, and left on the menu at low priority they reappear as a criterion in the first draft. Vendor-accepted deal registrations survive - as a leading indicator inside sourced revenue, never as a criterion of their own.

This order starves competencies: the highest ranking power on the list and the heaviest to run, so efficiency never picks it. Promote it anyway when the top tier's job is delivery quality rather than volume, or when partners already dispute their placement - an audited competency is the one criterion a partner cannot argue with.

## Points models

- Blend criteria into a weighted points pathway (the Alexander Group's third mechanic) when any single metric misranks partners.
- Set per-category minimums, not just a total. Microsoft's Partner Capability Score requires 70/100 with points in every category, so skilling alone - worth 40 of the 100 - cannot carry a designation.
- Publish the point formula; partners optimize what they can compute. HubSpot's ladder (Gold 325 → Platinum 925 → Diamond 3,100 → Elite 9,000 points, earned per $100 MRR across sourced/assisted/managed motions) is the most concretely documented production example.
- Weight motions unequally: sourced revenue carries more points than assisted or managed in that same production system, because origination is the scarcer behavior.

## Measurement windows

- Default to a rolling trailing-12-month or trailing-4-quarter window - rolling windows are the recommended guard against "tier tourism", where one big quarter buys a year of status.
- Match window length to the sales cycle: enterprise-cycle partners need multi-year evidence windows; transactional partners can be judged on 12 months.
- State the recalculation moment explicitly. One program recalculates monthly on a fixed day; most review quarterly or annually. The window and the recalculation moment are separate decisions.

## Gameability - the dispute test

Criteria double as the program's defense when a partner contests a demotion. Maureen Little, VP of Technology Partnerships at Okta: "They have to be things you cannot dispute."

- Reject logo counts for the same reason self-reported pipeline is already off the menu: both are the vanity metric behind the documented pay-to-play failures.
- Derive thresholds from evidence, not aspiration. Cody Jones of Zapier: "Go work with your most successful partners. Figure out what they do... Create those as the requirements for ascending tiers."
- Run every candidate criterion through one question: can the partner move this number without creating real value? If yes, drop or verify it.

## Criteria for non-transacting partner types

Jay McBain's core critique: most partners entering ecosystems today - tech/ISV, referral, advisory - never resell, so a revenue ladder reads them as "bad partners". Two ways to fix that, and they are not equally cheap:

- efficiency: `fitted criteria on the existing ladder > a separate track per motion`
- value (contribution the structure can actually recognize): `separate track > fitted criteria`
- effort (heaviest first): `separate track > fitted criteria`. Fitted criteria are a threshold table for one partner type, roughly a week's work inside a structure that already exists. A separate track is a second structure with its own benefits, cadence, governance and comms - a quarter at least, and permanent afterwards.
- Default to fitted criteria. Move to a separate track when non-transacting partners pass roughly a quarter of the base, or when the benefits they want (co-marketing, directory placement, integration support) barely overlap with what the transacting ladder pays out - at that point one ladder is two programs sharing a table.
- **ISV / technology partners**: integration depth and maturity, count of joint customers, marketplace listing presence - the criteria one data-platform vendor uses for its product-partner track.
- **Referral / advisory partners**: accepted-introduction volume and influenced pipeline, both verified in the vendor's CRM, never self-reported.
- **Track split**: build / sell / service is the documented pattern; level partners within their track rather than against each other.
