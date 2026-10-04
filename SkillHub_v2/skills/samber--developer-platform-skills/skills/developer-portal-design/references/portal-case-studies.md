# Portal and TTFC case studies

Every figure below carries a sourcing label. Agency- and vendor-reported numbers are directional evidence that the portal is the lever, never numbers a client should expect to reproduce. The consistent theme across all of them: **the underlying API did not change in any of these cases - only the portal and documentation did** - yet TTFC, adoption, satisfaction, and support load all moved materially.

## Portal/documentation rebuilds (agency-reported - WriteChoice client retrospectives, not independently audited)

| Case                         | What changed                                                                                                                                                 | Reported outcome                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| PagBank                      | Portal restructured around the developer's actual journey (sign up → authenticate → first call → handle errors → production), tested multi-language examples | Integration time 20 days → 7 days; CSAT 29% → 89%; support tickets −50%                            |
| Tonder                       | Docs overhauled with a zero-to-first-transaction path, consistent terminology, self-serve sandbox                                                            | Integration time 2 months → 10 days; adoption doubled; support costs −80%                          |
| Yuno (payment orchestration) | Docs migrated between hosted platforms, getting-started flow restructured                                                                                    | TTFC of 15-20 minutes; adoption +50%; docs quality cited by enterprise customers during evaluation |
| Nayax                        | Fragmented docs consolidated into one unified portal                                                                                                         | Reported 2x more integrations per year; support costs −80%                                         |
| CarePortals                  | Portal rebuild                                                                                                                                               | Reported 20+ developer hours saved per week                                                        |

## Ready-to-run collections (vendor-reported - Postman, measured on its own platform)

Shipping an importable, forkable collection of working example calls accelerated first calls **1.7x on average, with outliers as high as 56x** against a ~17-minute baseline. Keep the ratio, not the exact minutes - the baseline is specific to the APIs measured.

## Personalized onboarding (vendor's own product - Twilio)

Twilio's redesigned onboarding uses a short intake survey (role, code preference, use case) to tailor the experience, auto-selects relevant configuration, and lets users test with or without code and see live results instantly. It also verifies a phone number at signup - not just email - so trial users can act immediately instead of stalling on a later verification step. Twilio's public onboarding promise is a concrete outcome with a time ("send your first SMS in minutes"), not a vague "get started" - copy the pattern of promising a specific outcome.

## AI docs assistant at scale (vendor showcase - kapa.ai, traffic figure corroborated by Docker's own engineering blog)

Docker deployed a RAG "Ask AI" assistant across docs serving ~13 million monthly views. The vendor reports the rollout took weeks versus an estimated 6-12 months of internal development.

Deflection outcomes from the same vendor's announcements:

- One customer reported a 20% monthly support-ticket reduction.
- Another reported a 28% cut in response times.

All deflection figures are vendor-reported.

## TTFC benchmark anchors (published, but context-bound - use as anchors, not pass/fail bars)

- No universal TTFC standard exists. Nordic APIs explicitly cautions that TTFC varies by API complexity, price, audience familiarity, and competitive pressure.
- Ably's portal-scoring rubric awards top marks when time to hello world is under 30 minutes.
- Twilio publicly targets developers up and running in 5 minutes or less.
- Practitioner guidance (WriteChoice): under 15 minutes for a simple REST API with token auth. Under an hour for a complex payment-orchestration API with OAuth and webhooks. Also: "Auth is where most developers stall first... If a developer can't authenticate in under five minutes, everything downstream stops."
- Survey figures place the early-stage quit rate between 50% and 70% when friction appears (secondary citation via Young Copy - treat as directional).
- Postman's State of the API research (13,500+ respondents in 2020): lack of documentation is the #1 reported obstacle to consuming APIs "by an extremely wide margin" (54.3%). It stayed the top blocker (52%) in the 2023 edition.

## Common friction points (synthesized from Nordic APIs, WriteChoice, DigitalAPI, Young Copy)

- Mandatory signup before any exploration.
- Email/phone verification delays.
- API-key provisioning delays or manual approval.
- Unclear base URLs.
- Sandbox-vs-production confusion.
- Missing or broken quickstarts.
- Code examples referencing deprecated endpoints or auth.
- Sandboxes gated behind a sales call.
- SDK installation friction.
- Auth and CORS setup snags.
