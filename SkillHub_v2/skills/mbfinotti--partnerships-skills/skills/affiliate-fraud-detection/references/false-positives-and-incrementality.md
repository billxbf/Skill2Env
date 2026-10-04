# False Positives and Incrementality

The most expensive detection failure is not missed fraud - it is terminating a legitimate partner. This file separates the two.

## Legitimate-but-often-non-incremental partner taxonomy

Coupon, cashback, loyalty, browser-extension, retargeting, and brand-search partners are legitimate businesses that sit near the checkout moment and win last-click credit. That looks like poaching in a last-click report, but is contractually permitted unless the terms say otherwise. Low incrementality is a repricing problem, not fraud - the fix is a lower commission tier, and repricing belongs to `mbfinotti/partnerships-skills@affiliate-commission-structure`.

Reserve fraud enforcement for cases with technical evidence:

- Cookie-drop reproduction.
- Referrer obfuscation.
- Stand-down violations.
- Shared device/IP across accounts.
- Stolen-card chargebacks.

## The evidence is genuinely contested - test, don't assume

- Against coupon partners: an agency framework holder states incrementality testing "consistently shows [last-click] overstates affiliate contribution by 30 to 40%" (agency claim, commercial incentive).
- For coupon partners: a comScore/Google study found 94% of transactions driven by coupon-affiliate paid-search ads were incremental - only 6% of purchasers were already on the retailer's site before clicking.

Both cannot be generalized; run the program's own test before repricing or restricting anyone.

## Incrementality test design

Four methods answer the same question. Listed in efficiency order, not rigor order:

- value (most first): `user-level holdout > geo test > practical pause > attribution proxies`
- effort (most first): `user-level holdout > geo test > practical pause > attribution proxies`
- compliance cost (most first): `practical pause > geo test > user-level holdout > attribution proxies`
- efficiency (best first): `practical pause > attribution proxies > geo test > user-level holdout`

- **Practical pause test**: pause commissions for one partner type in one market for 4-6 weeks; if overall conversion and revenue do not move, those partners were capturing demand, not creating it. An hour to switch off, then waiting. Most exposed of the four contractually: it visibly singles out a partner type, so check notice obligations in the terms before flipping anything.
- **Attribution proxies**: compare last-click vs multi-touch, test alternate attribution windows, separate new-customer share. An hour on data already collected, and cheap enough to run first - but correlational, so it only decides whether a real test is worth running. Never reprice a partner on a proxy alone.
- **Geo test**: suppress the partner type in matched regions for 4-6 weeks; validate in a pre-test period that treatment and control regions track within 3-5% before trusting the readout. A week to match regions and validate the pre-period. Same contractual act as the pause, drawn by geography instead of partner type.
- **User-level holdout**: withhold exposure from a random control group; compare conversion. Cleanest causal read, and randomization means no partner is visibly singled out. Costs a quarter: randomization in the tracking layer, engineering time, and enough scale to detect the effect.

Start with the pause test. Move up to a geo test when the market is too small or too seasonal for a single-market readout to separate the partner's effect from noise.

That order starves the user-level holdout - best evidence, worst ratio, beaten every round. Promote it when the repricing decision is large enough that the partner will contest it, or when the partner type is big enough that a pause readout's noise band swallows the effect being measured. If the terms forbid suppressing a partner without notice the program cannot give, delete the pause and geo rungs from the plan and say so rather than leaving them for later: run proxies and put the contract change on the roadmap.

| Test outcome                    | Action                                                                                                   |
| ------------------------------- | -------------------------------------------------------------------------------------------------------- |
| No revenue movement when paused | Reprice to a lower tier, keep the partner - checkout-moment conversion assistance retains nuanced value. |
| Revenue drops                   | The partner is incremental: leave the rate alone and recalibrate whatever rule flagged them.             |

## Structural false-positive environments

Some legitimate situations mechanically resemble fraud. Baseline against known-good behavior instead of lowering the global threshold:

- Launch or promo windows: coordinated legitimate spikes look like bot bursts - annotate campaign calendars into the anomaly rules.
- Concentration: a handful of partners driving most sales is the normal affiliate power law - audit it, never auto-enforce on it.
- Corporate networks and VPNs on B2B traffic: a data-center or VPN flag on one lead is weak; the same fingerprint across many "unrelated" leads is strong.
- New partners with thin history: 2-SD outlier math is unstable on small samples - hold them to first-week watchpoints and longer payout terms, not outlier rules.
- Bulk B2B referral events (webinars, conference scans): many leads, same timestamp window, same IP block - legitimately.

## Process controls that keep false positives cheap

Four controls, in efficiency order - build downward, and stop wherever the effort ceiling lands:

- value (most first): `appeals process > per-rule trip-risk naming > partner classification > false-positive KPI`
- effort (most first): `appeals process > false-positive KPI > partner classification > per-rule trip-risk naming`
- efficiency (best first): `per-rule trip-risk naming > partner classification > false-positive KPI > appeals process`

- **Per-rule trip-risk naming**: every rule row names the legitimate behavior that could trip it and the discriminating check. Near-zero - one more column in a table already being written - and it kills the most common false positive at design time, before anyone is flagged.
- **Partner classification**: segment by role (content, creator, review, coupon, cashback, loyalty, comparison, paid-media, B2B referral) and never measure or pay all roles identically. An hour, and every rule built afterwards inherits it; it only pays off through those rules, which is why it ranks below naming.
- **False-positive KPI**: track false-positive rate from sampled review as a first-class metric paired with catch rate - a rule set optimizing catch alone is incomplete by construction. A standing job of manual sampling each cycle, and it measures the problem rather than preventing it.
- **Appeals process**: a fixed window, reviewed by someone other than the analyst who raised the flag. A week to publish plus a standing job to staff, and it is the only control that recovers a false positive after enforcement has already landed.

That order starves appeals, which is the one control the wrongly-terminated partner actually needs. Promote it above everything else in a licensed or regulated vertical, where it is a supervisory expectation rather than a nicety, and in any program that has already terminated a partner it later had to readmit.
