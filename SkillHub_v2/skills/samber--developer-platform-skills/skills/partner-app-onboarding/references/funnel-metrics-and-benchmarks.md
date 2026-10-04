# Funnel metrics and benchmarks for partner onboarding

These figures mix official documentation with third-party estimates that disagree with each other, and review timelines vary with queue volume - treat exact numbers as directional and re-verify against current official pages before citing them in a deliverable.

## The metric landscape: what has a name and what doesn't

- **Time-to-First-Call (TTFC) / Time-to-First-Hello-World (TTFHW)** - signup → first successful API call. The established DevRel first-touch metric:
  - Postman's then-Head of Developer Relations called it "the most important metric you'll need for a public API"
  - a developer-analytics vendor defines TTFHW as the time to reach "the minimal level of value from your API"

  Best-in-class benchmarks cited are seconds-to-minutes - two leading API companies under ~90 seconds (aspirational ceilings).

- **Time to first deal** - partner-agreement signature → first registered opportunity. The partner-ecosystem analog, aimed at revenue rather than apps. Forrester's named Partner Onboarding Framework (align, acclimate, activate, authorize - 2018 report) warns that a partner not actively selling within 90 days "most likely never will". Another partner-management vendor's framework similarly targets "first-deal acceleration".
- **Time-to-first-submitted-app** - signup → first app submitted for review. It sits in an unnamed gap between TTFC (technical first touch) and time-to-first-deal (commercial activation). A team adopting it is coining a metric, not citing one - label it self-defined in any report.

## The four-checkpoint funnel

Marketplaces keep their partner-funnel conversion numbers internal, so instrument your own:

1. signup → sandbox/credentials provisioned
2. provisioned → first API call (this is TTFC)
3. first API call → first app submitted
4. submission → approval

## Drop-off evidence

- The available drop-off figures come from **general developer-tool research, not marketplace-partner data**: one synthesis of developer-tool funnels reports 80-95% of visitors dropping off after clicking "Get Started," with 68% citing "too much setup time," and developers making a first API call within 10 minutes being 3-4x likelier to convert to paid.
- The second documented friction point is the **review gate**: a ~50% first-time security-review fail rate at the application-gated platform (its own estimate as relayed by third parties, at $999 per resubmission), and 2-3 rejection cycles before approval reported in another platform's developer community.
- **Post-launch eligibility walls** drive late attrition: a marketplace review requiring ≥5 active installs before it starts (threshold lowered from 10 in August 2025), and a certification requiring ≥6 months listed plus ≥60 active installs. Both hit partners after they believe onboarding is complete - disclose them upfront.

## Review-stage durations (the one well-documented funnel component)

The review gate dominates any realistic time-to-first-submitted-app-to-live once build time is added. First-submission figures across the five platforms studied:

| Platform archetype                     | Review duration                                                              | Fee                      |
| -------------------------------------- | ---------------------------------------------------------------------------- | ------------------------ |
| Fastest self-service commerce platform | 5-10 business days, often longer in practice                                 | none                     |
| CRM app marketplace                    | initial check ≤10 business days, whole process ≤60 days                      | $0                       |
| Enterprise collaboration marketplace   | 10-15 business days to approval; 5-10 just to start                          | none                     |
| Messaging-platform marketplace         | ~10 business days preliminary + up to ~10 weeks functional                   | none                     |
| Application-gated enterprise platform  | ~1-2 weeks verification + 3-4 weeks testing; 6-9 weeks end-to-end with queue | $999/attempt (paid apps) |

Range: roughly 1-2 weeks at the light end to ~2.5 months at the heavy end. The named platform behind each row, with its entry gate, provisioning and support shape, is in the platform-archetypes reference file linked from `SKILL.md`.

## Working thresholds

Self-set rather than industry pass-standards; treat as starting points to recalibrate against your own baselines:

- **TTFC above ~10 minutes** → fix onboarding friction (provisioning, credentials, quickstart) before investing anywhere else; the general-DevRel evidence puts the largest leak here.
- **First-review fail rate above ~30-40%** → build a pre-submission validator (an automated checker partners run before submitting) before considering heavier education mandates.
- **Time-to-first-submitted-app far exceeding review duration** → the bottleneck is docs and enablement, not the review team; spend there.
- Baseline every checkpoint against your own first quarter and track quarter-over-quarter conversion - measure the trend, not an absolute pass bar.
