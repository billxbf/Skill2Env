# Coverage benchmarks by segment, and how much to trust them

Use these bands to bootstrap a target when the org's own conversion history is missing or unstable - then replace them with the org's own math after ~2 closed quarters. Every band below reduces to the same mechanic: `coverage ≈ 1 ÷ win rate`.

## Segment bands (directional - ranges vary slightly across sources)

| Segment                                 | Typical cycle | Typical win rate | Coverage band |
| --------------------------------------- | ------------- | ---------------- | ------------- |
| High-velocity SMB / assisted self-serve | ~30 days      | 40-60%           | 1.7x-2.5x     |
| Mid-market / sales-assisted             | 60-90 days    | 20-40%           | 2.5x-4x       |
| Enterprise field sales                  | 120-180 days  | 9-25%            | 4x-7x         |
| Strategic / mega-deals                  | 180+ days     | 10-15%           | 7x-10x        |

For a genuinely **new motion** (not just a new rep in an established one), neither win rate nor cycle length is known yet - run a more conservative 5-7x until conversion stabilizes, then invert the real number.

## Why motion - not just deal size - moves the band

- **Buying-committee size depresses win rate.** Published counts for a complex B2B decision range from ~5-7 (HBR, 2017) through 6-10 (Gartner) to 13 (Forrester, 2024) - sources define "complex deal" differently, so cite the range, never one number. Each added stakeholder is a veto point.
- **Cycle volatility.** SMB deals enter and exit fast; some practitioners argue that volatility warrants _more_ SMB coverage than its win rate implies, others less - the literature doesn't resolve it. Segment and use the org's own history instead of picking a side.
- **Threading requirements.** Enterprise deals need many engaged contacts, and under-threaded deals silently decay late - the quantified evidence is in the quality-evidence reference.

## Coverage targets drift as win rates drift

Bridge Group's AE research (the most methodologically transparent series in this space - consistent survey methodology since 2006, no product riding on the findings) recorded median win rate on qualified pipeline falling from 23% (2022) to 19% (2024). It states the implication directly: that four-point drop moves required coverage from 4.3x to 5.3x. Hence the standing trigger rule in the workflow: recompute a segment's target whenever its win rate moves ~2+ points, rather than waiting for the annual planning cycle.

## Source reliability, for citing any of the above

- **Most independent:** Bridge Group (transparent long-running survey) and Dixon & McKenna's _The JOLT Effect_ (2.5M recorded sales conversations, published methodology).
- **Rigorous but self-sourced:** Dave Kellogg - the deepest public methodology on target derivation, with worked examples drawn from his own enterprise-software career rather than a broad sample.
- **Vendor-published, directionally useful, not independently audited:** ORM Technologies, Clari, Gong, UserGems, SaaStr's stated rules of thumb. Read the data, discount the framing - each has a product whose value rises if you believe your pipeline needs their rigor.

## Contested claims - flag, don't resolve

- **The flat 3x rule** (SaaStr's much-cited default) is widely criticized as a relic of 1990s six-figure/~33%-win-rate/9-month-cycle enterprise selling; it remains the most common anchor in the wild. Use it only as a zero-data starting point, never as a defensible target.
- **1÷win-rate vs conversion-inversion:** most sources still teach the simple inversion; Kellogg's conversion-rate method is the rigorous upgrade. Both are legitimate at different data maturities.
- **Raw vs weighted as "the" number:** one camp frames coverage as a capacity question (compute it raw), the other as a forecast-honesty question (compute it weighted). Resolve it as different jobs - raw answers "enough at-bats?", weighted answers "what will this produce?" - and always report both.
