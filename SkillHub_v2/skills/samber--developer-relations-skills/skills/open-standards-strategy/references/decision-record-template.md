# Decision record template and worked examples

Contents: [Template](#template) · [Worked example 1: driving a spec](#worked-example-1-driving-a-spec-that-collapses-an-nm-problem) · [Worked example 2: rival spec](#worked-example-2-answering-a-rival-spec) · [Negative example](#negative-example-what-a-bad-record-looks-like) · [Public precedents](#public-precedents-worth-citing)

## Template

```markdown
# Standards decision: <specification name>

Date: <YYYY-MM-DD> · Owner: <person> · Review: <date>

## Landscape

- Specs covering this job, their venue, stage, IPR mode.
- Implementations, split into vendor-controlled and independent.
- Our counted demand: deals, tickets, RFPs naming this standard.
- Conformance suite and certification mark: exists / does not exist.

## Decision

Posture: <ignore | consume | conform | extend | contribute | co-found | drive>
Because: <2-4 sentences, including the layer being commoditized and the product whose demand rises>

## Alternatives rejected

- <posture>: rejected because <test it failed: demand, commoditization, control, cost>
- <posture>: rejected because <...>

## Venue and IPR (only if contribute or above)

Venue: <...> · IPR mode: <RF / non-assert / RAND> · Trademark holder: <...>
Charter-time commitments we cannot revise later: <...>

## Conformance plan

Test suite owner · who may run it · fee · certified spec version and expiry · public registry location.

## Staffing

Named person, hours per month, committed horizon.

## KPIs and thresholds

| Metric | Threshold | Sourced or baseline | By when |
| ------ | --------- | ------------------- | ------- |

## Kill rule

If <metric> is below <threshold> on <date>, we <de-escalate to posture X / donate / withdraw>,
and our obligation to existing implementers is <notice period, bridge or successor, migration path>.
```

Tag every threshold in the third column. "Sourced" needs a name a reader can check (RFC 6410, a venue's own process document, a published study); anything else is "baseline" and is expected to be argued with.

## Worked example 1: driving a spec that collapses an N×M problem

**Situation.** A vendor of observability tooling integrates with 9 agent frameworks; each customer wants their own 3. Each framework pairing costs weeks and breaks on every upgrade.

**Landscape.** No spec covers the job. Two competitors ship proprietary adapters. Counted demand: 14 deals in 12 months named at least one missing integration.

**Tests.**

- Demand: passed, named accounts.
- Commoditization: the standardized layer is the wire format between framework and collector - a layer the company does not sell; it sells the analysis on top.
- Control: 40% share of the collector market and the only cross-framework tooling.
- Cost: two engineers for four quarters is fundable.

**Decision.** Drive, with a Git-based community specification, royalty-free, reference implementation under a permissive licence, conformance suite shipped with v1.

**Why this shape.** The pattern that made the Language Server Protocol work applies: integration effort "must be repeated for each development tool, as each provides different APIs", and a common protocol turns M×N into M+N. Language-neutral primitives, not framework-specific constructs, are what make the spec adoptable by parties who dislike each other.

**KPIs.**

- Two independent interoperating implementations - _sourced_, from RFC 6410 §2.2's bar for Internet Standard status.
- Within 12 months of v1, at least one from a party that is not a customer, and 6 of the 9 frameworks covered - _baseline_, chosen from this market's annual framework release cadence, not from any published norm.
- Conformance suite passed by every implementation claiming support - _baseline_.

**Kill rule.** Fewer than two independent implementations at month 12 → stop investing in the spec, keep the adapters as product features, and publish a note saying so rather than letting the spec rot in public. Anyone who already implemented v1 gets 6 months' notice and a maintained adapter, because withdrawal is our decision and theirs is the sunk cost.

**Exit.** If adoption crosses the threshold, donate the spec to a neutral host to remove the "one vendor controls this" objection, before a competitor stands up a rival neutral spec.

## Worked example 2: answering a rival spec

**Situation.** Your spec has 6 implementations; a competitor's has 5. Both cover the same job. Adoption of both is stalling, and buyers say they are waiting for the market to settle.

**Analysis.** This is the fragmentation case, not a feature race. The OpenTelemetry precedent is direct: the merged project's own framing was that "the biggest problem with either project has been the fact that there were two of them", and "the main benefit to the ecosystem is the consolidation itself – not some specific and shiny new feature". Shapiro and Varian reach the same conclusion from the economics: "declaring an early truce in a standards war can benefit consumers as well as vendors, and thus pass antitrust muster", and pressure to negotiate rises with the cost of the fight to both sides.

**Decision.** Propose a merge rather than a feature push, on the terms that made that precedent work:

- bridges preserving backward compatibility with both predecessors
- a dated end to parallel development
- positioning of the merged spec as the next major version of both rather than a third option
- a governance body seated with both sides from day one

**What this costs.** Roadmap control and the sunk narrative of "we won". What it buys is the only thing that matters at this point: unblocked adoption for the merged spec.

## Negative example: what a bad record looks like

```markdown
# Standards decision: OpenFoo

Posture: contribute. We believe in open standards and want to be good ecosystem citizens.
We will join the working group and send an engineer to meetings.
Success: increased visibility in the community.
```

Four defects, each fatal on its own:

1. **No named change.** Attendance without a target revision buys travel expense, not influence - text and sustained presence are what move consensus venues.
2. **No commoditization test.** Nobody checked whether the spec covers the layer the company sells. Standardising your own differentiator hands competitors interchangeability with you.
3. **Unmeasurable success.** "Visibility" cannot fail, so the programme can never be stopped.
4. **No IPR or staffing reality.** Charter-time patent commitments and multi-year attendance were never priced.

## Public precedents worth citing

- **RFC 6410 §2.2** - the IETF's maturity bar: "There are at least two independent interoperating implementations with widespread deployment and successful operational experience." The one implementation-count threshold in this skill that is genuinely sourced.
- **Shapiro & Varian, "The Art of Standards Wars"** (_California Management Review_ 41:2, Winter 1999) - the four battle types, the seven key assets and the truce argument.
- **Language Server Protocol** - the M×N framing: one server reusable across tools, tools supporting languages "with minimal effort"; language-neutral primitives (document URIs, text positions) kept the protocol simple enough to adopt.
- **OpenTelemetry** - consolidation of OpenTracing and OpenCensus; bridges for backward compatibility, predecessors moved to read-only mode within the year, merged project framed as the next major version of both.
- **PDF** - de facto first via free readers, formalised afterwards as ISO 19005-1:2005 and ISO 32000-1:2008; the standard number followed adoption, it did not create it.
- **Khronos Adopters Program** - conformance separated from membership ("A company does not have to be a member of Khronos in order to become an Adopter"), tiered fees (OpenGL 3.2–4.5 at $25,000 for members, $30,000 for non-members; WebGL free), and passing grants both logo rights and a licence to members' essential patents.
- **Embrace, extend, extinguish** - the _United States v. Microsoft_ record, including the 1998 Gates memo that "allowing Office documents to be rendered very well by other people's browsers is one of the most destructive things we could do to the company"; cite it when arguing for a conformance mark rather than as a tactic to copy.
