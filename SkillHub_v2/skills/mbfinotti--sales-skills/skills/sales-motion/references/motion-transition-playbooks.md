# Motion transition playbooks

The three transitions a motion decision usually triggers - exiting founder-led sales, layering sales onto self-serve, and shifting toward enterprise or channel - each with its gates, sequence and named failure modes.

## Exiting founder-led sales

Every motion starts here; the PLG-vs-sales-led question is not live until the founder has sold. The staged progression (Pete Kazanjy):

1. Validate the problem.
2. Build the MVP.
3. Founder personally sells to 20-30 customers.
4. Hire 2 "pioneer" sellers and generalize the motion from what the founder learned.

**The exit signal is repeatability, not revenue** (Euclid Ventures): "a repeatable ability to identify, acquire, and onboard additional customers", never an ARR figure. Quantified gates practitioners use:

- A minimum viable sales motion: 30-50 qualified prospects run through the process, 10-20 converting.
- The standard-deal test: 3-5 deals won at standard origin, price and scope.
- Stability of 3 of 4 core metrics (win rate, cycle length, ACV, conversion) for 90 days.
- The practitioner phrasing: "by deal 5 you should recognize the same objection from deal 1 and have a written save; by deal 10 your discovery call shouldn't have any new questions."

Counter-signal: early wins that are idiosyncratic - the buyer knew the founder, an unusual use case - are not repeatability regardless of ARR.

**Readiness checklist before any sales hire** (composite: Raaz Herzberg, Jason Lemkin, Pete Kazanjy):

- 10-20+ _unaffiliated_ customers closed personally.
- More than 20% of the founder's time booked with customers.
- A specific, repeatable pattern in how deals closed.

Any "no" means hiring is premature - the failure mode is premature delegation, which breaks the founder's market-feedback loop before it has taught anything transferable.

**Hire executors, not a leader.** The most common mistake is hiring a sales _leader_ rather than sales _executors_ who can refine a motion that doesn't exist yet.

- **Do:** hire the hungry senior AE archetype - entrepreneurial background, breaks new ground, works deals personally, feeds insight back to the roadmap.
- **Avoid:** a playbook-execution seller hired too early.

Recruiting mechanics live in mbfinotti/sales-skills@sales-hiring.

**Validate the transition month by month** (Kazanjy's ramp gates):

1. **Month 1:** onboarding. Red flag: can't absorb material.
2. **Month 2:** 10-20 first meetings, 50%+ converting to second meetings. No first meetings at all is fatal, act immediately.
3. **Month 3:** a subset reaches proposal. Meetings without progression is a coaching issue, not a hiring issue.
4. **Month 4:** meaningful closed revenue.

Named early-stage tactics worth citing instead of inventing examples:

- **Collison Install** (Stripe): close early enterprise deals by personally handling the technical implementation, removing integration risk.
- **$1 Invoice Test** (Jeff Weinstein): charge a token $1 to cross the psychological barrier of asking for money.

Treat the young motion as **source code** (Kazanjy): run small cohorts, observe what breaks, version the scripts and objection handling deliberately.

## Layering sales onto self-serve (PLG → product-led sales → enterprise)

**The dominant pattern is layering, not replacement.** Pocus's customer-base survey found 98% of PLG companies either have a sales team or plan to hire one.

The open question is _when_, never _if_ (Pete Kazanjy). Self-serve users at $19-29/month are lead generation, not the business; real enterprise revenue lives at $50K-$250K contracts. Dropbox added sales almost too late, Slack barely in time.

**Only two economically justified reasons to add sales to self-serve** (Lenny's Newsletter, "The Transition"):

1. **Penetration/expansion** - unify disparate pods of self-serve users inside one organization into a single contract (Slack/Zoom account managers). Fits multi-player products.
2. **Conversion assist** - raise conversion of high-value signups that stalled before activation. Fits when deal value justifies human intervention.

**The 4x economic test** ("will the juice be worth the squeeze"): a salesperson should deliver roughly 4x their fully loaded cost in incremental revenue. Treat ~4x as the go/no-go floor. Model it as a chain:

```
rep meeting capacity/month → monthly opportunity budget
rep cost ÷ opportunities = cost per opportunity
opportunities × win rate = wins
wins × deal value = revenue
revenue ÷ rep cost = ROI (target ~4x)
```

Kyle Poyar's caution: efficient-looking sales-assisted deals can mask a team that is a net drain. Validate that assisted conversions are _incremental_ (would not have converted anyway), not just profitable-looking in aggregate.

**Route accounts to humans on product signals, not titles alone.** Zapier's four product-qualification signals:

- Multi-player use: multiple active users on one domain.
- Usage growth over time.
- Use-case fit for assistance.
- Role fit against ICP.

Zapier found that sales touchpoints improved retention as well as upmarket conversion. The two-axis routing matrix crosses observable factors (title, company size, domain) with behavioral factors (activation depth, frequency, multi-user):

- High-observable + low-behavioral: conversion-assist outreach.
- High-observable + high-behavioral: expansion play.
- Low-observable: tech-touch only, no human.

**Bessemer's timing and sequence** for the PLG-to-enterprise layer, keyed to roughly the $25M ARR mark ("many of our highest-performing PLG portfolio companies… scale to $100 million of ARR and beyond by successfully introducing an enterprise sales engine as they passed the $25 million ARR mark"). Six tactics, deliberately in this order - build PQL scoring and pricing flexibility _before_ hiring the first enterprise sales leader:

1. Let end-users drive top-of-funnel enterprise pipeline.
2. Mine PQLs to guide direct sales.
3. Use clear heuristics to triage and scale accounts.
4. Introduce pricing/packaging flexibility.
5. Ensure the architecture supports expand-and-extend.
6. Establish cohesive hiring and comp.

Reference companies: Auth0, HashiCorp, Imply, PagerDuty, Twilio. Counter-signal both ways: operationalizing upmarket too early "can be disastrous if not executed well"; waiting too long carries its own opportunity cost.

**Re-comp before re-org** (Kyle Poyar). Keeping sales-led comp while flipping toward PLG is what makes AEs gate or sabotage the self-serve motion. The concrete fix, done _before_ the org chart changes:

- Pull AEs off sub-$25K deals.
- Shrink base 15-25%.
- Expand variable.
- Pay 1.5x-2x accelerators on expansion ARR from PQL-crossed accounts.

Plan mechanics belong to mbfinotti/sales-skills@sales-comp-design - what lives here is the sequencing rule.

**Keep the self-serve path open.** Best-in-class free-to-paid conversion is 2.5x higher when a seamless in-product upgrade/billing path exists (OpenView-era finding); its absence forces inefficient sales-assisted closes even on small accounts. The PLG + sales flywheel (Shaun Clowes): PLG feeds sales qualified leads and usage data; sales feeds back leads that aren't ready - running both is a resilience play, "very hard to knock over".

## Shifting toward enterprise

What changes structurally when the motion moves upmarket - product, narrative and buyer psychology, not just headcount:

- **Dual-track product gate** (Aparna Chennapragada) - every feature must now satisfy the end-user experience _and_ organizational governance (security, admin controls, compliance). SSO / SOC 2 / audit-logging-class features are a prerequisite for the motion, not a follow-on.
- **Narrative shift** (Geoffrey Moore) - before the chasm the pitch sells "we believe what you believe"; after it, "we need what you have" - a concrete, repeatable solution to a recognized problem. Founder vision-selling does not scale into a repeatable enterprise motion without this register change.
- **FOMO vs FOMU** (Matt Dixon) - enterprise buyers are moved by fear of messing up, not missing out; dialing up FOMO backfires in most reported cases. Counter-tactic, "pings and echoes": state a concern other buyers face at this stage and read whether the buyer confirms or refutes it.
- **Mission-First Value Chain** (Palantir-derived) - access → demonstrated value → contracts → growth, in that order; pushing sales methodology before value is established reads to the buyer like a bad first date.
- **Comp is a signal, not a fix** - a maturing land-and-expand motion outgrows the 50/50 new-logo-only plan (Sahil Mansuri: it rewards mercenary behavior at the expense of retention). Flag it, then hand design to mbfinotti/sales-skills@sales-comp-design.

## Channel / partner-led

- **Margins** (Bessemer GTM guide):
  - VARs typically take 20-30% (higher in high-tax markets like India/Brazil), given **in perpetuity** for SaaS so the partner protects renewal.
  - Pure resellers take 5-10% (transaction processing only), cited elsewhere at 20-40% when bundled with more.
  - Referral partners take a one-time 15-30% of first-year contract value.
- **Sourced vs influenced are two metrics, never one.** Sourced = partner originated the deal (pipeline generation); influenced = partner accelerated a deal originated elsewhere. ACV drives the split: sub-$10K SMB/PLG deals run 55-75% marketing-sourced (partners mostly influence); $200K+ enterprise deals run only 15-28% sourced (partners mostly accelerate).
- **Channel CAC discipline**: channel CAC should run 20-40% below direct CAC to pay for its own margin give-up (Pacific Crest survey: up to 50% lower than field sales in the best cases). Scaling gate: partner CAC 20-40% below direct _and_ a 3:1 revenue-to-cost ratio - a positive-margin pilot alone is not enough.
- **Swim lanes before scale.** Jay Simons (Atlassian): "the direct sales motion can begin to cannibalize the opportunity for the channel partner." Agree explicit account/segment/vertical swim lanes before scaling either motion, never adjudicate deal-by-deal after conflicts start.

## Transition failure modes (all directions)

1. Running a high-touch motion under a low ACV - burns cash on deals that can never repay CAC.
2. No in-product billing path - the self-serve funnel stalls at upgrade and forces sales-assisted closes on small accounts (the 2.5x finding above).
3. Channel cannibalization - direct sales competing with partners for the same deal; fixed by swim lanes, not by escalation.
4. Premature delegation - sales hired before the founder's motion is repeatable.
5. Comp changed after the org chart - the re-comp-before-re-org rule inverted.
