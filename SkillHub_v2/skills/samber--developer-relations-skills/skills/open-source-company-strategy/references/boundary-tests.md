# Drawing and defending the open/closed line

Contents: the five gates · the CAP quadrants · the asset scoring table · open-core boundary shapes · a worked brief · weak vs strong rows.

## Table of Contents

- [The five gates, in order](#the-five-gates-in-order)
- [The CAP quadrants - a second read on the same assets](#the-cap-quadrants-a-second-read-on-the-same-assets)
- [The asset scoring table](#the-asset-scoring-table)
- [Open-core boundary shapes](#open-core-boundary-shapes)
- [A worked brief (fragment)](#a-worked-brief-fragment)
- [What we sell](#what-we-sell)
- [Motive](#motive)
- [Open](#open)
- [Competitive case](#competitive-case)
- [Weak vs strong rows](#weak-vs-strong-rows)

## The five gates, in order

Apply them in this order. Gates 1, 3 and 5 are vetoes: failing any of them keeps the asset closed no matter how well it scores elsewhere.

### Gate 1 - Irreversibility (veto)

Every released version stays licensed forever. Re-licensing later needs every copyright holder's consent for future code and cannot touch past code, so the practical outcome of a reversal is a fork of the last open version plus a public trust cost.

Ask: if this can never be closed again, does the decision change? A "yes" is not a failure - it is the discovery that the honest verdict is **Not yet**, with a written condition that would change it.

### Gate 2 - Differentiating or context

Riehle's split: generic components move outward to shared maintenance, differentiating assets stay in-house. In his distributor example the code is open while the test suites, configuration databases and compatibility matrices - what customers actually pay for - stay closed. Moore's core-versus-context is the same cut in general-management vocabulary.

Ask: does the company win deals _because of_ this asset, or does it merely need the asset to exist? Losing this gate does not force a closed verdict; it usually means opening a smaller piece, or opening it later.

**Run this gate twice per asset - once on the differentiating layer, once on its enablers.** Linåker et al. argue enabling frameworks must be actively contributed even when the differentiating layer stays closed, because a competing open solution adopted outside the firm's control erodes the differentiating edge and forces a costly redesign (Sony's media frameworks vs. its camera effects, step 1). Treating "the asset" as the unit hides exactly this decision.

### Gate 3 - Value capture (veto)

Name the mechanism that still stops a competent competitor from taking the opened asset and reselling it: hosting and operations · proprietary data · network effects · trademark and brand · support and SLA · certification · a paid tier · integration with a closed system.

"The license" is not a mechanism. It cannot stop a competitor willing to comply, and it cannot substitute for a trademark - the name and logo are what stop a fork calling itself your product, and they need their own registration and usage policy.

Henry Chesbrough's Open Innovation (2003) names the same substitution at the level of the whole firm: Closed Innovation holds that "we should control our IP, so that our competitors don't profit from our ideas," while Open Innovation holds that "we should profit from others' use of our IP, and we should buy others' IP whenever it advances our own business model." The business model, not the IP boundary, is what captures value - this gate applies that same swap to one asset instead of the whole company. Chesbrough's argument is general R&D and IP management, written before open-core SaaS existed; it grounds the substitution, it does not evaluate any specific open-source business model.

### Gate 4 - Contribution viability

Would an outsider ever contribute? That needs a buildable repository, a visible issue tracker, a contribution path and code legible without internal context. Code failing this is _published_, not open source: it carries the publishing cost with none of the shared-maintenance return, so the maintenance motive cannot be claimed for it.

Separate the two things this gate covers, because companies reliably supply one and not the other. West and O'Mahony compared twelve corporate-initiated projects and found sponsored projects far readier to offer **transparency** - visibility into what is happening - than **accessibility** - the ability to participate.

A public repository with no route to commit rights, no roadmap input and no answered pull requests passes the transparency half and fails the gate. When a user reports "we open sourced it and nobody came", check accessibility first.

O'Mahony and Karp (2022) track that same gap over time rather than at one moment: across four governance phases of one platform, outside participation rose as access widened and fell again once governance direction turned ambiguous, and external participants only took on leadership roles once a structured, collectively-determined process replaced single-sponsor control. Passing gate 4 at launch is not a permanent result - an accessible project that drifts into ambiguous governance loses the contributors it opened for, which is why the operating model in step 8 needs a named owner, not just an open repository.

### Gate 5 - Ownership (veto)

A named maintainer, an agreed release rhythm and a stated issue-response commitment - or it does not ship. Dump-and-run publishing is the fastest way to turn a talent or trust motive into evidence against the company.

## The CAP quadrants - a second read on the same assets

The gates give a verdict. Linåker et al.'s Contribution Acceptance Process model, documented at Sony Mobile, gives each asset a _dominant objective_ instead, by placing it on two axes - business impact and control complexity:

| Quadrant              | Position                              | Dominant objective                   | Typical posture                                          |
| --------------------- | ------------------------------------- | ------------------------------------ | -------------------------------------------------------- |
| Strategic             | High impact, high control complexity  | Ecosystem control                    | Contribute selectively, hold governance influence        |
| Platform / leverage   | High impact, lower control complexity | Time-to-market                       | Contribute actively; the ecosystem carries the load      |
| Products / bottleneck | Lower impact, but damaging if absent  | Cost reduction or alliance formation | Open it and share the maintenance, even with competitors |
| Standard              | Low impact, low control complexity    | Cost reduction                       | Fully open, let the ecosystem own it                     |

This adds two things over a gate list:

- a **per-artifact success definition**, valid only if declared at decision time rather than reconstructed afterwards
- a re-evaluation rule: the authors note the model does not capture how fast an artifact drifts from differentiating to commodity, and recommend re-running the evaluation every product planning cycle

The same paper validates the quadrant classification at three further firms beyond Sony Mobile, anonymized for confidentiality: an agriculture-tech firm's grain-marketing platform (CTO interview), a mobile games studio (founder interview), and a large telecommunications firm's internal infrastructure project (cross-functional workshop). Each firm's feature set was mapped onto the same four quadrants with percentage breakdowns, so the classification's external applicability rests on four organizations, one named.

Sony's authority model is worth copying at scale: contributions classified trivial, medium or major; trivial needs only the relevant business manager, the rest go to a cross-functional board of engineers, business managers and legal. Frame agreements pre-authorize contribution to ecosystems already judged non-competitive, so routine cases never reach the board.

## The asset scoring table

Score every candidate asset on one row. Verdicts: **Open**, **Closed**, **Not yet** (with the condition).

| Asset | Motive served | G1 irreversible | G2 differentiating | G3 value capture | G4 contributable | G5 owner | Verdict |
| ----- | ------------- | --------------- | ------------------ | ---------------- | ---------------- | -------- | ------- |

Rules that keep the table honest:

- every candidate asset appears exactly once, since an asset left off is a decision made by omission
- G3 holds a mechanism, not a license name
- G5 holds a person's name and an hours-per-week number, not a team
- a **Not yet** row is complete only when it names the event that would flip it (a hire, a revenue threshold, a shipped paid tier, a spec stabilizing)

## Open-core boundary shapes

When the verdict is "core open, some features paid", the boundary needs a rule that survives roadmap churn. All three cost about the same to adopt, so durability per quarter of upkeep is the ranking axis - efficiency: `buyer-tiered > scale-tiered > feature-by-feature judgment`:

- **Buyer-tiered.** Tier features by _who buys them_: the individual contributor's features stay in the open tier, the manager, compliance and executive buyer's features go paid. GitLab publishes this model on its stewardship page, along with eleven commitments and a documented 2020 re-audit that moved eighteen features into the open tier. It is the most durable rule because "whose problem is this?" has a stable answer while "how valuable is this?" does not.
- **Scale-tiered.** The open tier serves a single team or a bounded deployment; multi-tenant, HA, or fleet-scale operation is paid. Durable, but it prices out exactly the large community deployments that generate contributors.
- **Feature-by-feature judgment.** Decided case by case at roadmap time. Least durable: it re-litigates the line every quarter and invites taking features back.

Whichever shape is chosen, publish where the line sits. Having a line is not the credibility failure; hiding it is.

## A worked brief (fragment)

No company publishes a gate-by-gate table, so this is constructed: a hosted observability product, B2B, self-serve entry tier plus enterprise contracts. The numbers are illustrative - use the structure, not the figures. GitLab, Confluent, Sony Mobile and Google each publish a real line; read one of those before writing your own.

```markdown
## What we sell

Hosted ingestion, storage and query of telemetry, plus the on-call workflow around it.
Customers pay for operations at scale and for retention guarantees, not for the code.

## Motive

Commoditize your complement. The complement is instrumentation: every hour a customer
spends wiring up telemetry is an hour they are not sending us data. Cheaper, more
ubiquitous instrumentation raises demand for storage and query, which is what we bill.
Evidence: 4 of our last 10 lost deals stalled at instrumentation effort, not at price.

## Open

| Asset | G1 | G2 | G3 | G4 | G5 | Verdict |
| Language SDKs (6) | permanent, fine | context | hosting + retention | yes, users patch their own language | A. Rivera, 10h/wk | Open |
| Wire format spec | permanent, fine | context | hosting + retention | yes, third parties implement it | A. Rivera, 2h/wk | Open |
| Query-plan optimizer | permanent, NOT fine | differentiating | nothing left | no | - | Closed |
| Terraform provider | permanent, fine | context | hosting | yes | J. Okafor, 4h/wk | Open |
| Anomaly-detection models | permanent, NOT fine | differentiating | data volume, weakly | no | - | Not yet - revisit if a competitor ships an open equivalent |

## Competitive case

A hyperscaler forks the SDKs and points them at their own backend. We keep: managed
ingestion at scale, 13-month retention, the on-call workflow, and the trademark. We lose
nothing we bill for. Verdict: acceptable.
```

## Weak vs strong rows

**Weak - value capture**

> We'll open the core and stay ahead through faster development.

Speed is not a mechanism; a well-funded competitor is faster. This row fails gate 3 and the verdict must be Closed or Not yet.

**Strong - value capture**

> We'll open the core. Value capture is operations: multi-region ingestion with a 13-month
> retention guarantee, plus the trademark. A competitor can run the code; they cannot run
> our fleet or call it by our name.

**Weak - ownership**

> The platform team will maintain it.

No name, no hours, no response commitment. Fails gate 5. **Strong:** "A. Rivera, 10h/week, monthly releases, first response to issues within 3 business days, backup maintainer J. Okafor. Reviewed at the next planning cycle."

**Weak - motive**

> Open source is how developer tools grow, and it will help with hiring and credibility.

Three motives, none tested, none measurable; it will be measured on stars. **Strong:** "Primary: commoditize the instrumentation complement. Secondary (not measured): talent. Success signal: paid ingestion volume, not SDK downloads."

**Weak - demand pull**

> Our largest customer asked for the connector to be open source, so we're opening it.

A request is not a requirement, and the row skips every other gate. Ask what happens on refusal; if the renewal is not conditional, this is a preference dressed as a mandate. Even when it _is_ conditional, the ownership and value-capture gates still apply - a repository opened to close a deal and then abandoned becomes the same customer's complaint six months later.

**Strong - demand pull**

> The renewal (€480k ARR) is conditional on the connector shipping under an OSI-approved licence
> before Q3. Two other customers in the same regulated segment will inherit the benefit, and one
> has agreed to co-maintain. Gate 3: we still hold the managed control plane and the trademark.
> Gate 5: M. Duarte, 6h/week, monthly releases. Declared objective: cost sharing - at least one
> external organisation landing connector fixes within 12 months.
