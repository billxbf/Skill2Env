# Compensation guidance

Contents: why no survey-grade dataset exists, the structural finding that changes how this benchmark works, and what to check for a live figure.

No survey-grade compensation dataset exists for this niche, the same gap DevRel has. Direct lookups (Levels.fyi, Glassdoor, Payscale, BuiltIn) either 404, return no usable content, or block scraping. Never present an undated number as verified.

## The key structural finding: platform comp rides the general ladder, unlike DevRel

This is the one finding worth stating explicitly and prominently, because it flips how this skill's compensation gate should read relative to `devrel-hiring`'s:

- Stripe's own posting for this exact function is titled **"Staff Software Engineer, API Platform"** - the leveling word is "Staff Software Engineer," the general engineering ladder rung, with "API Platform" as a qualifier/team name, not a separate ladder. This is a directly sourced, concrete data point that at least one major infra-first company places platform engineering on its general software-engineering levels rather than carving out a bespoke platform-specific pay scale.
- The API Product Manager literature converges on the same pattern from the PM side: career-progression sources describe API PM levels as "typically company-specific rather than standardized industry-wide, though it generally mirrors general product management career ladders with added emphasis on technical/developer-facing skills at every level."
- This contrasts with DevRel, where compensation has no reliable anchor to an existing ladder at small or mid companies, which is why DevRel pay is comparatively undersurveyed and unpredictable across company sizes.

**Practical implication for a hiring manager:** where `devrel-hiring` must anchor an offer to a dated crowdsourced figure and treat it as directional, this skill can instead anchor an offer to the company's own general software-engineering (or general product-management) comp bands at the equivalent level - the same way any other backend-engineering or PM specialization gets leveled and paid. State this as the actionable answer rather than hedging it away.

## What to check for a live figure

- The company's own published engineering or PM level ladder and comp bands, if public (GitLab publishes both, though the specific compensation figures for its Partner Integration Engineer family were not visible in the fetched handbook page - only the job-level structure was).
- Crowdsourced leveling sites (Levels.fyi) searched by the _general_ engineering or PM title plus team name (for example, "Staff Software Engineer" at the target company, filtered to a platform or API team) rather than by a bespoke "platform engineer" or "API product manager" title, since those bespoke titles return sparse or no data.
- Devtools-focused recruiters, the same channel devrel-hiring names for its own undersurveyed compensation gap.

Never quote an undated figure from memory; if the harness can browse, pull a current figure with its source, date, and level before using it in any deliverable, exactly as devrel-hiring instructs for its own compensation gate.
