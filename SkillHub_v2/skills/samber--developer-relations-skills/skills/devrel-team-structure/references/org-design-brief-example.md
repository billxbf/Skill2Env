# Worked org design brief

An illustrative brief for a fictional Series-B payments-API company with four people doing DevRel work. Use it for shape and level of detail, not as a template to fill with the same answers.

---

# DevRel org design brief - Northbank API, March

## Table of Contents

- [Situation](#situation)
- [Work inventory](#work-inventory)
- [Reporting line](#reporting-line)
- [Shape](#shape)
- [Coverage](#coverage)
- [Roles](#roles)
- [Interlocks](#interlocks)
- [Ladder and titles](#ladder-and-titles)
- [Budget](#budget)
- [Re-org triggers](#re-org-triggers)
- [Transition](#transition)
- [Weak versus strong, on the contested sections](#weak-versus-strong-on-the-contested-sections)

## Situation

The community manager resigned; her replacement req is being held while leadership argues whether DevRel should move from marketing to product. Funded driver: developer adoption - developers pick the API, and a finance lead signs. Sponsor: VP Marketing, who has held the budget for two years.

## Work inventory

| Surface                       | Owner today              | Manager         | Hours/week | If it stops                                     |
| ----------------------------- | ------------------------ | --------------- | ---------- | ----------------------------------------------- |
| API docs                      | 1 technical writer       | Eng manager     | 30         | Support volume rises within two weeks           |
| Quickstarts and samples       | Advocate A               | VP Marketing    | 8          | Trial activation drops, invisible for a quarter |
| Blog                          | Advocate A + 3 engineers | VP Marketing    | 10         | Organic traffic decays over months              |
| Discord (2,400 members)       | vacant since February    | -               | 12         | Already degrading: median first response 4 days |
| Conference talks              | Advocate B               | VP Marketing    | 12         | Nothing immediate                               |
| SDK maintenance (5 languages) | 2 platform engineers     | Eng manager     | 6          | Issues age, integrations break on API changes   |
| Changelog                     | Product manager          | Head of Product | 2          | Customers miss breaking changes                 |

Unowned since February: community. Informally absorbed: Advocate A is answering Discord between other work, which is why sample apps slipped two quarters.

## Reporting line

DevRel reports to marketing, because the funded driver is developer adoption and the VP Marketing owns it. This line starves the product feedback loop. The head of product covers it through a standing 30-minute roadmap slot every two weeks, owned by Advocate B. Reviewed in September, or immediately if the sponsor changes.

## Shape

Centralized, four people plus the docs interlock. Rejected embedding advocates in the two product squads: with four people, each squad would get half a person and the craft would have no owner. Revisit at eight people.

## Coverage

| Function                         | State                                                         |
| -------------------------------- | ------------------------------------------------------------- |
| Developer advocacy               | owned                                                         |
| Community management             | unowned - this brief's primary gap                            |
| Technical writing                | owned by engineering (1 writer), shared review with DevRel    |
| Developer marketing              | shared: DevRel writes, marketing distributes                  |
| Developer education              | deliberately refused this year - no certification, no academy |
| Developer experience engineering | owned by platform engineering, service interlock              |

## Roles

| Person                         | Surfaces owned             | Backup                   | Capacity assumption                       |
| ------------------------------ | -------------------------- | ------------------------ | ----------------------------------------- |
| Advocate A                     | quickstarts, samples, blog | Advocate B               | 70% of 4 days (1 day on support rotation) |
| Advocate B                     | talks, roadmap interlock   | Advocate A               | 70%                                       |
| Community manager (open req)   | Discord, champions pilot   | Advocate A until month 3 | 70%                                       |
| Technical writer (dotted line) | API docs                   | none - flagged risk      | not DevRel-controlled                     |

Bus-factor-one risks: API docs, and the changelog while it stays with one PM.

## Interlocks

- Product - collaboration during launch windows, X-as-a-service otherwise - feedback in, launch dates out - arbiter: head of product.
- Engineering - facilitation - technical review in, writing coaching out - arbiter: eng manager.
- Docs - X-as-a-service both ways - drafts and structure decisions - arbiter: eng manager.
- Support - X-as-a-service - recurring failure signals in, troubleshooting pages out - arbiter: support lead.
- Sales - X-as-a-service, capped at four hours per week - evaluation material out, objections in - arbiter: VP Marketing.

## Ladder and titles

Advocates sit on the marketing ladder, which levels on campaign ownership and does not describe their work. Action: adopt the engineering IC ladder's levels with DevRel-specific criteria, drafted by June. The "Head of DevRel" title on the open req maps to a manager-of-three scope - leave it at manager until the team clears six people.

## Budget

- Headcount budget: VP Marketing.
- Program budget (events, community tooling, swag): VP Marketing.
- Docs headcount: eng manager.

Confirmed unusual - most programs have these split across two owners.

## Re-org triggers

- Sponsor change at VP Marketing.
- A second team starts running developer events without an interlock.
- Docs stays at bus factor one for another quarter.
- Team reaches eight people.
- The sales interlock exceeds its four-hour cap for three consecutive weeks.

## Transition

- Week 1: publish this brief; Advocate A stops answering Discord ad hoc, and a triage rota covers it until the hire.
- Month 1: open the community req with the coverage map attached; start the roadmap slot.
- Quarter 1: draft the ladder criteria; re-check the docs backup risk.
- Unchanged: reporting line, docs ownership, refused education scope.

---

## Weak versus strong, on the contested sections

**Work inventory**

- Weak: "The team owns docs, content, community and events." A list of nouns re-assigns work nobody can trace back to a person.
- Strong: the table above - a named owner, their manager, real hours, and what breaks if the surface stops. It is the only section that survives contact with the people already doing the work.

**Reporting line**

- Weak: "DevRel will report to marketing, which is where it fits best given our go-to-market motion."
- Strong: the version above - driver, leader, starved pillar, named cover, review date. The weak one cannot be checked later, so nobody notices when the product loop dies.

**Shape**

- Weak: "We will move to a hub-and-spoke model with embedded advocates per squad."
- Strong: "Centralized at four people. Hub-and-spoke rejected: it needs a hub of two plus two spokes, which is six of our four heads. Revisit at eight."

**Coverage**

- Weak: "Community is a priority this year."
- Strong: "Community management: unowned since February. Median Discord first response is 4 days. Covered by a triage rota until the hire lands."

**Roles**

- Weak: "One advocate per two product lines is the industry ratio."
- Strong: "Two advocates cover six surfaces at 70% capacity - a planning baseline we chose, not a benchmark. Advocate-per-product-line ratios in circulation are single-company anecdotes; this headcount comes from the surface table above."

**Interlocks**

- Weak: "DevRel will partner closely with product, support and sales." Three permanent collaborations with no arbiter, which reads as availability rather than a boundary.
- Strong: the five lines above - one mode per team, what crosses, a named arbiter, and a cap in hours where the load is known to grow.

**Re-org triggers**

- Weak: "We will revisit the structure annually." A date nobody watches, and no way to tell early that the design has stopped fitting.
- Strong: observable conditions - sponsor change, a second team running events without an interlock, docs at bus factor one for another quarter. Each one is visible without a survey.
