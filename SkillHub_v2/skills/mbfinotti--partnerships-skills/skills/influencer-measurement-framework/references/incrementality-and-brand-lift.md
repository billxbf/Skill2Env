# Incrementality testing and brand lift - when they belong in the plan

Incrementality is the only measurement class that answers "did this creator activity _cause_ anything," and most creator campaigns cannot power it. The plan's job is to decide honestly which side of that line the campaign falls on.

## Geo-lift / synthetic control [verified methods]

- Method: withhold (or concentrate) the creator activity in test regions; compare outcomes against a weighted synthetic control built from untreated regions. Privacy-durable - needs no user-level identifiers.
- Open tooling exists: Meta's open-source **GeoLift** package (R; augmented synthetic control) and Google's **CausalImpact** (Bayesian structural time series). Both are free and harness-independent - if you can run R or Python, either works; otherwise hand the design to whoever owns analytics.
- Alternatives when platforms offer them: conversion-lift holdouts and ghost-ad designs - precise, but they require platform ad spend and inherit the self-measurement conflict below.

## The MDE power check - run it before promising a test

1. Compute the Minimum Detectable Effect (MDE) for the available budget, conversion volume, and window (GeoLift ships power-analysis functions; CausalImpact requires a manual pre-period fit).
2. Practitioner target [practice]: a 5-10% MDE over a 4-8 week window.
3. Decision rule: if the computed MDE exceeds the lift you would actually act on (e.g., the test can only detect a 25% lift but a 10% lift would already justify the spend), **do not run the test** - write "directional only" into the plan.
4. Why this is non-negotiable: an underpowered test returns "no significant lift" for a channel that genuinely works, and someone cuts a working channel on the strength of a test that could never have seen the effect.

**Program-size reality [practice]:** single-creator and micro-influencer budgets almost never generate enough conversions to power a test. Incrementality is realistic for always-on programs or creator spend aggregated at portfolio level - never per-creator. B2B conversion volumes rarely power it at all.

## Brand lift studies

- Design: randomized exposed-vs-control groups assigned pre-campaign, surveyed natively on recall, awareness, message association, favorability, consideration, intent.
- Entry costs are statistical-power thresholds, not price lists [vendor/platform - directional]: platform-run studies start around low five figures and run to six figures depending on platform; independent panels cost more but see across platforms. Minimums change - verify current thresholds with the provider (if you can browse the web, check; otherwise mark the figure "unverified, ask provider").
- Duration: typically 1-4 weeks of in-flight surveying; short flights return "inconclusive".
- **The self-measurement conflict [practice - widely voiced]:** platform-run lift studies are the platform "marking their own homework". Note the conflict in the plan; corroborate with an independent panel when budget allows - while remembering the panels selling that argument are also commercially interested.
- Cheap proxy when no study is powered or funded: pre/post movement in trailing branded-search volume and direct traffic against the pre-launch baseline. Correlational, honest about it, and free - which is why the baseline capture step is mandatory for awareness campaigns.

## Decision thresholds that change the plan [practice]

- MDE comes back above ~15-25%: drop incrementality; rely on triangulation + survey; plan says "directional only".
- Code-leakage rate (redemptions with zero matching link clicks) exceeds a few percent: switch to single-use codes.
- Survey self-report for the creator channel exceeds 20-30% while click-based attribution gives it under 5%: the model is wrong, not the survey - reweight toward the survey signal and note it in the readout.
- B2B with under ~20% of closed-won deals naming a trackable channel: promote HDYHAU to primary; branded-search volume becomes the corroborating KPI.
