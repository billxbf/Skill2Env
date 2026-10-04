# Override mechanisms and change-notice benchmarks

Named precedent for the two change-facing steps: how real platforms grant limits above the published tiers, and how much notice a limit change gets versus a version deprecation.

## Seven named override mechanisms

The pattern across all of them:

- Self-serve tiers publish exact numbers; the top tier publishes a process.
- Overrides are keyed to the authenticated principal (API key, org, app installation), never a person.
- Every platform reserves the right to lower limits again for stability, regardless of any override granted.

| Platform  | Mechanism                             | Notable detail                                                                                                                                                                                    |
| --------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stripe    | Support ticket                        | Large increases require **≥ 6 weeks' lead time** - the citable planning floor                                                                                                                     |
| Anthropic | Spend-based auto-promotion, Tiers 1→4 | Custom tier beyond Tier 4 arranged with the account team, never self-serve                                                                                                                        |
| GitHub    | Enterprise plan gating                | 15,000 req/hr tied to Enterprise Cloud org membership or org-owned app status; OSS projects occasionally get case-by-case manual whitelisting                                                     |
| Zoom      | Plan gating                           | Higher limits for Business/Enterprise/Education/Partner accounts - not purchasable standalone                                                                                                     |
| Auth0     | **Time-boxed self-serve burst**       | A paid add-on raises the Authentication API limit to a multiplier of the default, but only for up to 48 hours per month - the rare self-serve exception                                           |
| Zyte      | Ticket with structured lead time      | Temporary increases via support ticket ≥ 24h ahead, specifying API key, desired RPM, target sites, dates; permanent increases via sales or account manager - the most process-documented template |
| OpenAI    | Explicit activation                   | Enterprise plan does **not** auto-grant higher limits - they must be configured with OpenAI even after purchase                                                                                   |

Two design details worth copying:

- An override can hold one dimension non-negotiable: GitHub Enterprise Server admins can exempt users from rate limits entirely via `ghe-config`, but the exemption explicitly cannot bypass the separate GraphQL point quota.
- A higher-priced plan does not automatically imply higher limits (OpenAI) - state explicitly in your docs whether yours does.

## Limit change ≠ version deprecation

The industry treats these as two different regimes; keep their numbers separate when citing.

**Rate-limit changes are non-breaking.** IBM's public API policy, verbatim: "The rate limits can be adjusted on API endpoints during the lifetime of the API and does not require a version update. The clients that receive the HTTP status code 429… must make adjustments." Shopify and Stripe both explicitly reserve the right to temporarily reduce limits for platform stability with little or no notice. Consequence: a published rate limit cannot be treated as a contract or SLA - consistent with the IETF draft's insistence that its header values are hints, not guarantees.

**Version deprecation gets formal, long windows** (via `Deprecation`/`Sunset` headers, changelog, targeted email - machinery owned by `samber/developer-platform-skills@api-versioning-policy`). Named benchmarks for the _version_ window, for contrast only:

| Company            | Version-deprecation notice                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| Atlassian          | 6 months (standard)                                                                                      |
| IBM                | 12 months                                                                                                |
| Microsoft Graph    | commonly 24 months                                                                                       |
| Salesforce         | ≥ 3-year support per version; retirement waves with 1-year notice; retired versions return HTTP 410 Gone |
| Canvas/Instructure | ≥ 30 days for material policy changes                                                                    |

Practitioner consensus for graduated change rollouts generally:

- ~30 days for minor endpoint changes.
- 60–90 days for major deprecations.
- 6–12 months for full version sunsets.

Run these as a multi-email cadence: announce, remind, warn, throttle, remove. These are the _deprecation_ numbers; a rate-limit change sits below all of them, which is exactly why it needs its own written notice policy - nothing else forces communication.

## Rate-limit-specific change practice

- Version the _policy document_ alongside the API; publish burst, sustained, and the algorithm in use.
- Announce reductions with lead time proportional to blast radius. Stripe's ≥ 6-week guidance for large _increases_ is a reasonable floor to apply symmetrically to _decreases_.
- Introduce or tighten limits on live traffic via GitHub's admin rollout sequence, communicating with affected callers before each tightening:
  1. **Observe** - log real traffic, no enforcement.
  2. **Baseline** - enforce at a high initial ceiling.
  3. **Refine** - tighten from observed data.
- Expose limits in-band via headers so well-behaved clients adapt automatically rather than needing to read a changelog.
- **Never silently change reset semantics** (e.g. epoch-seconds → seconds-remaining): that change breaks client parsing invisibly instead of producing a visible error - it deserves a major announcement on its own.
- Zuplo's line for the policy's tone: "provide ample notice and explain the reasons for the changes to maintain transparency and trust."
