# Worked example: bottom-up TAM/SAM/SOM for sales planning

A B2B SaaS sizing worked end to end, the sanity checks that validate it, a compact B2C variant, and the negative example to refuse. The B2B segment counts, ACVs, and filter percentages follow a published prior-art example; the capacity-ceiling cross-check at the end is illustrative arithmetic added to show the planning step, and is labeled as such.

## B2B: from segment counts to a shippable SOM

**TAM - bottom-up, per segment:**

| Segment          | Qualifying companies | ACV     | Segment TAM         |
| ---------------- | -------------------- | ------- | ------------------- |
| Small accounts   | 85,000               | $3,600  | $306.0M             |
| Mid-market       | 18,000               | $9,600  | $172.8M             |
| Enterprise       | 2,500                | $24,000 | $60.0M              |
| **Regional TAM** |                      |         | **$538.8M ≈ $539M** |

**Top-down triangulation:** the same market sized from a published industry figure landed within ~1% of the bottom-up build - unusually strong convergence. The more typical "good" range is ~10% variance on TAM and under a few percent on SAM. Treat anything under ~30% as confidence-building and anything past ~50% as a market-definition problem to reopen, not a number to discard.

**SAM - sequential filters, each with stated reasoning:**

- Product-readiness filter: 45% of TAM (the product serves these segments' requirements today, not after the roadmap ships).
- Addressable-switching filter: 70% (accounts contractually or structurally reachable - not locked into multi-year incumbent contracts, in served geographies and channels).
- SAM = $539M × 0.45 × 0.70 ≈ **$169M**.

These are the same filters the ICP and territory design must use. A SAM filtered differently for planning and for messaging produces two numbers that cannot both be true.

**SOM - capture-rate view:**

- Year 3, at a 2.5% capture rate: **$4.2M**.
- Year 5, at a 5% capture rate: **$8.5M**.
- New entrants rarely exceed 5% share within five years; a capture rate above that band needs an argument, not an aspiration.

**SOM - capacity ceiling (illustrative arithmetic, labeled):** suppose the team fields 10 quota-carrying reps closing ~40 deals per rep per year at a $9,600 closed-won ACV: `10 × 40 × $9,600 = $3.84M`. That sits *below* the $4.2M Year-3 capture-rate figure, so **$3.84M is the number that ships**.

The market would tolerate $4.2M; the team cannot physically produce it this period, and shipping the higher number manufactures a miss. (These capacity inputs are invented to demonstrate the step: substitute the org's real rep count, closed-rate, and closed-won ACV.)

Had the ceiling landed _above_ the capture-rate figure, the capture-rate figure ships instead - SOM is always the lower of the two bounds.

## Sanity checks on top of the math

Run all four before shipping:

1. **Implied customer count.** ~$4.2M at a ~$4,700 blended ACV implies ~900 customers - does that roughly match the independently estimated addressable customer count for the target segments? A SOM implying more customers than the segment contains is broken.
2. **Implied revenue per customer.** Divide SOM by the implied customer count; the result must fall inside the segment ACV range, not outside it.
3. **Share vs incumbents.** The target market-share percentage must sit below the established leaders' share - a new entrant projecting more share than the incumbent holds is a red flag.
4. **Public comparable.** Does a public company's actual reported revenue in the same category corroborate that a market of this size exists at all? Segment revenue from public filings is the single best free validation of a bottom-up number.

## B2C: the population-based variant (illustrative arithmetic, labeled)

The formula shape changes; the discipline does not: `TAM = addressable population × purchase rate × average annual spend`.

Example, invented round numbers: a metro area of 4,000,000 adults, of whom a 30% demographic filter matches the target profile (1,200,000), with an estimated 10% annual purchase rate and $180 average annual spend: `1,200,000 × 0.10 × $180 = $21.6M` TAM for that metro.

SAM narrows by the channels and locations actually operated. SOM is bounded by the capture-rate band and, since no rep closes these sales, by the org's own historical acquisition rates rather than the rep-capacity formula. Note the structural difference: this build yields rates and segments, never a named-target list.

## Negative example - what this skill refuses to produce

> "The category is worth $10B. If we capture just 1%, that's $100M."

This is the inflated-TAM slide, and it fails on contact: the 1% has no derivation, so it collapses the moment anyone asks "why not 0.1%?" It is common enough on pitch decks that sophisticated audiences recognize and discount it on sight - a precise percentage attached to that pattern circulates widely online but does not trace to a locatable study, so state the pattern, never the number.

The bottom-up build is structurally immune: it contains no free market-share parameter to inflate, only counts and prices that the operating plan already has to defend. When a user asks for this slide, build the triangulated version and present the smaller, defensible number - a well-reasoned smaller market beats a huge one that cannot be justified.
