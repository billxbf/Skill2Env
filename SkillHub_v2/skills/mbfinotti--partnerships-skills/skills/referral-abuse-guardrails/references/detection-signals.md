# Detection Signals

Honest strength ratings, with direction of travel. Weight durable signals over degrading ones; run the two-tier shape (cheap deterministic checks auto-applied, expensive corroborative review before any enforcement) as a mental model borrowed from ad-measurement standards - never as a compliance claim.

Provenance tags:

- `[academic]` - peer-reviewed work.
- `[vendor claim]` - published by a party selling the remedy.
- `[vendor docs]` - a platform's published product documentation.
- `[regulator]` - a regulator's published position.
- `[verified]` - multiple independent reports.
- `[derive from own data]` - program-specific; compute the baseline from the program's own history rather than copying a number.

## Signal catalogue

Rank the signals before instrumenting any of them:

- efficiency: `payment-reuse == cohort-quality > velocity > email-similarity > graph > fingerprint`
- value: `cohort-quality > graph > payment-reuse > velocity > email-similarity > fingerprint`
- effort: `graph > fingerprint > cohort-quality > payment-reuse == velocity == email-similarity`
- compliance cost: `fingerprint > graph > cohort-quality == email-similarity > payment-reuse == velocity`

- Payment-reuse and cohort-quality tie on efficiency because both already sit in billing data the program keeps anyway, neither degrades when a browser or device changes, and each catches precisely what the other cannot: payment reuse settles the one-person case deterministically, cohort quality is the only thing that sees a ring of real people. Neither substitutes for the other.
- Payment-reuse, velocity and email-similarity tie on effort: each is a single query over data already stored, shipped in an afternoon, reversible by deleting the query.
- Cohort-quality and email-similarity tie on compliance cost: both profile customers across accounts without collecting anything new.

Cookie linkage and IP/subnet clustering are excluded from these lines rather than ranked last. Their value is already at the floor, so ordering them would be false precision - they stay in the table below only because vendors still sell them and a defender needs the reason to refuse.

This order starves graph/network signals: the only thing that sees rings, and last but one on efficiency because a cluster model plus its corroboration workflow is a standing job with real profiling exposure. Promote it when a ring is already confirmed, or when per-referral reward value makes one cluster incident material on its own.

Re-rank on what exists: a program with a trust-and-safety function already running graph analysis pays no marginal effort, which moves it straight to the top. The ordering is a default, not a law - it shifts with context and with who executes it.

| Signal                                                            | Strength                                                            | Direction            | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Payment-instrument reuse                                          | Strongest deterministic signal available to a non-regulated program | Stable               | Scarce, costly to rotate, and already held if the program charges money. Check it first.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Downstream cohort quality                                         | Strongest overall; the one signal nobody can game                   | Stable               | See below - it detects rings and farming that every identity check misses.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Timing/velocity bursts                                            | Moderate                                                            | Stable               | Cheap tier-1 flag; thresholds must come from the program's own data, never a copied number [derive from own data].                                                                                                                                                                                                                                                                                                                                                                                     |
| Email similarity / plus-addressing                                | Moderate vs low-effort abuse                                        | Stable               | Cheap; useless against rings. False-positive class: family members on a shared domain with similar names [vendor docs].                                                                                                                                                                                                                                                                                                                                                                                |
| Graph/network signals                                             | High for rings - the only signal that sees them                     | Improving (academic) | Group-detection systems find fraud clusters that per-account checks miss [academic, production-deployed]. Known false-positive mode: legitimate high-volume actors - the enthusiastic advocate looks structurally identical to a small ring [academic]. Never enforce on graph shape alone; require corroboration (reward-splitting behavior, refund clustering, cohort collapse).                                                                                                                     |
| Device/browser fingerprint reuse                                  | High but overstated                                                 | Degrading            | A device-intelligence vendor itself states fingerprinting utility has "significantly degraded" over the last decade [vendor claim]; one browser deliberately reduces entropy; browser tampering measured at 4.4% of desktop identifications and ~1 in 5 events involving a VPN, from a 23.4B-event denominator [vendor claim]. Legal overlay: the UK regulator holds that deploying fingerprinting requires fair choices and possibly consent even outside advertising [regulator] - route to counsel. |
| Cookie-based self-referral linkage _(unranked - do not build on)_ | Low and falling                                                     | Degrading            | Third-party cookies are blocked by default in two major browsers; the third's deprecation was reversed (2024) but its replacement attribution APIs were retired (2025) [verified]. Durable answer: server-side attribution off billing webhooks, not browser state.                                                                                                                                                                                                                                    |
| IP / subnet clustering _(unranked - do not build on)_             | Weakest classic signal                                              | Degraded             | A referral platform explicitly recommends against enabling its own same-IP check (offices and buildings share static IPs) [vendor docs]; carrier-grade NAT pools mobile users; households share an IP by construction - and household referrals are often exactly what the program wants to allow. Use only combined with user-agent or as ring corroboration.                                                                                                                                         |

## Downstream cohort quality - the operational test

Academic baseline: a ~10,000-customer, ~3-year bank study found referred customers retain better and are worth at least 16% more than comparable non-referred customers [academic, peer-reviewed]. A related summary puts the profitability gap at 25% over 33 months - the two figures measure different quantities, so never present them as competing estimates of the same thing. Old and single-industry: treat as directional.

The test to build into every spec: **if the referred cohort does not beat organic on retention, refund rate, and 90-day revenue, the program is buying signups, not acquiring customers.** Volume metrics can make fake referrals look like a working growth loop; cohort quality cannot be gamed, because gaming it requires the referred accounts to become genuinely valuable customers - at which point the program won.

Dashboard: referred vs organic, by referrer decile, on retention / refund rate / 90-day revenue. A single referrer whose cohort collapses is a cheaper ring detector than any graph model.

## Calibration baseline

Expected multi-accounting background rate: 1-2.5% of devices access 3 or more accounts, many over 50 [vendor claim, explicitly scoped to one region's food-delivery market]. Use as an expected-flag-rate anchor to sanity-check rule output - a flag rate of 20% means the rules are wrong, not the users - never as a target.

## What not to rely on

- Any vendor-published detection-accuracy percentage without a stated denominator.
- The "$443B false declines" figure - unverifiable precision; cite the mechanism (a wrongly withheld reward costs reward + support + churned LTV) instead.
- A referral-specific false-positive benchmark: none is published anywhere. Anyone quoting one is extrapolating from payments data. Calibrate with the holdout cell in the Pass Threshold instead.
