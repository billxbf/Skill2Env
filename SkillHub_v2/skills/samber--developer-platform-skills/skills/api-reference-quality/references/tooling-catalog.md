# Tooling catalog per rollout stage

Tools are named as instances of their category. Recommend the category first, then whichever instance fits the team's stack. Every tool below is spec-driven - a machine-readable spec (OpenAPI/AsyncAPI/GraphQL SDL) is the prerequisite for all of them.

## Stage 1 - source-of-truth generation platforms

Render the reference from the spec so a page can never be edited independently of the contract.

- **Redocly, Stoplight, SwaggerHub, ReadMe, Bump.sh, Mintlify** - hosted docs platforms consuming the spec. Mintlify ties docs to Git with bi-directional sync so a spec change and its rendered-reference change land in the same PR review.
- **Zuplo** - the strongest "one spec, every surface" instance found: a single OpenAPI document drives gateway routing, request validation, interactive docs, the developer portal, and API-key scoping simultaneously.
- Open-source renderers: **Swagger UI** (original, basic try-it), **Redoc** (three-panel layout; try-it gated to the commercial tier), **Stoplight Elements** (React components).

## Stage 2 - spec linters (completeness gate)

Lint on every commit touching the spec, pre-commit and in CI, before any other check - a spec failing its own lint cannot produce a trustworthy reference regardless of renderer.

- **Spectral** (Stoplight, open-source) - given/then JSONPath rules with severities; `spectral lint --fail-severity` gates CI; built-in `oas` ruleset flags missing descriptions.
- **Redocly CLI**
  - Built-in rules including `operation-description`, `operation-operationId`, `operation-operationId-unique`, `no-invalid-media-type-examples`.
  - CI-friendly output formats.
  - `.redocly.lint-ignore.yaml` as a legacy escape hatch.
- **Vacuum** (open-source, Go) - Spectral-ruleset-compatible and much faster; adds example-based rules checking that schemas/parameters/operations actually carry examples - the exact gap OASQuali measured as most common.
- **RateMyOpenAPI** (Zuplo) - grades a spec 0-100 across categories including documentation and completeness; 80/100 is its default passing bar. Cite the per-spec scoring mechanism only; the bar is a tool default, not an industry average.

Rule set to enforce at minimum:

- Per-operation description and operationId.
- Documented responses including a 4xx.
- Examples on parameters and schemas.

Start at warn severity, flip to fail-on-warn once clean.

## Stage 3 - contract testing (accuracy gate)

The spec is only a source of truth as long as it contains truth. A spec with no contract-test coverage is unverified prose with better formatting.

- **Schemathesis** (Python, property-based, open-source) - generates test cases straight from the OpenAPI/GraphQL schema; asserts the server never 500s on generated input and every response matches the documented schema. Used by Netflix, SAP, Red Hat, IBM, JetBrains. Practitioners report a first run on a production schema typically surfaces 5-15 issues - the tool for catching undocumented behavior.
- **Portman** (Apideck, open-source) - converts the spec into a Postman collection with injected contract tests (status, content-type, schema compliance), variation tests, and chained-CRUD tests; runs via Newman in CI.
- **Dredd** (open-source) - validates live responses against the documented description. Carry Phil Sturgeon's caveat when recommending it: Dredd "is testing your documentation is accurate using the API, it is not for testing your API" - he now recommends OpenAPI-3.x contract assertions folded into the existing test suite instead of a separate Dredd pass.
- **Prism** (Stoplight, open-source) - turns any spec into a mock server plus validation proxy; consumer-side contract testing before the real API exists.
- **oasdiff / ApiNotes** - spec-to-spec breaking-change diffing in CI. (Optic, the prior standard recommendation for this job, was archived January 2026 - do not recommend it.)

Gate merges on lint + contract-test pass, never on the docs site merely rebuilding - a site rebuilds cleanly from a spec that lies.

## Stage 4 - per-language snippet parity and try-it

The mechanism is the OpenAPI `x-codeSamples` extension: a per-operation array of language-tagged samples the docs platform renders in the reference panel, replacing generic HTTP snippets that don't correspond to real SDK usage.

Two ways to keep parity in sync:

- **SDK-generator overlays**
  - **Speakeasy** - generates idiomatic SDKs across ~10 languages and pushes `x-codeSamples` overlays for all operations. Production users include Vercel, Cloudflare, Mistral.
  - **APIMatic**, **Fern** (publishes to npm/PyPI/Maven Central/NuGet/RubyGems; acquired by Postman), **Stainless** - peer options.
  - **OpenAPI Generator** - the free option (50+ targets), with the known caveat that its output is "technically correct but rarely production ready".
- **Hand-maintained, CI-tested snippet repository** - the Twilio model: one repo, one testing harness, a fake API server validating every snippet before merge. Higher editorial effort, full idiomatic control.

Platform notes:

- ReadMe defaults to HTTP-based snippets and needs a Stainless/APIMatic integration for SDK-based ones.
- Mintlify renders multi-language examples from the spec and integrates with Speakeasy.

Try-it: embed a console with pre-filled test credentials (the Stripe model) or ship a ready-to-run collection. Effect-size numbers for either are vendor-produced - see the measured-evidence file before citing any multiplier.

## Stage 5 - institutionalization

No tool - process:

- Same-PR spec/docs changes enforced in review.
- Documentation expectations in the engineering ladder.
- Quarterly re-audit against support-ticket and docs-search analytics.
