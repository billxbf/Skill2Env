# Language-order cases and versioning decoupling

Documented company cases for step 2 (language order) and step 5 (versioning and cadence) of the workflow.

## Language order is audience-driven - the documented cases

No major API vendor publishes a ranking algorithm. Each maps its buyer's stack, then confirms with its own traffic and registry telemetry. The fintech-vs-AI/dev-tools contrast is the clearest documented pattern:

- **Twilio.** Its engineering blog states the rationale directly: "For a long time we've supported and maintained helper libraries and tooling in the most popular languages and environments used by developers." Documented growth path: from a few languages and 12 endpoints to "8 subdomains and over 200 endpoints in 7 languages: C#, Java, Python, PHP, Ruby, Node.js and Salesforce". Go was then added later as a deliberate, named, sequenced expansion: "We're now expanding that coverage by providing a Twilio Helper for Go". Twilio also runs the documented two-tier model (official + "Community Supported Libraries") and moved its official libraries to auto-generation from an in-house generator "inspired by boto3, raml-codegen and swagger."
- **Plaid (fintech).** Exactly 5 official libraries - Ruby, Node, Python, Java, Go - plus a documented long tail: the OpenAPI spec lets developers "auto-generate your own client libraries in over 40 different languages," with C#, PHP, and Rust explicitly named as third-party-generation-only.
- **Stripe (fintech).** Official server-side SDKs for Ruby, PHP, Java, Python, Node, .NET, and Go, plus a separate community-libraries page. The set is read as reflecting its merchant/web-developer base - Ruby and PHP trace to early web-commerce adoption, not to general popularity rankings.
- **OpenAI / Anthropic (AI/dev-tools).** Both lead with Python and TypeScript - the dominant AI-integration languages - then expand to Go, Java, Kotlin, Ruby. Both portfolios were generated via Stainless, covering "the five languages that cover the bulk of production AI integration work."

**Sequencing pattern across the cases:**

1. Ship the language the earliest customers already use.
2. Add the second-most-common next.
3. Achieve breadth via codegen or OpenAPI self-service rather than more official SDKs.

Twilio's one-language-at-a-time additions and Plaid's "5 official + 40 via OpenAPI" both illustrate the official-core-plus-generated-long-tail model.

## Audience-mapping practice and documented patterns

Vendors uniformly map their buyer's stack as the primary input to language ordering, not generic popularity rankings. No company cites Stack Overflow Developer Survey, TIOBE, or GitHub Octoverse by name as a formal decision input.

Telemetry-driven prioritization ("usage analytics decide the next language") is stated only as general practice by SDK tooling vendors - no company publishes its own telemetry-driven decision as policy. When you instrument client `User-Agent`/SDK-header telemetry, use the data to confirm the audience mapping rather than originate it.

The add-a-language threshold this skill recommends (a sustained double-digit share of API traffic, or repeated enterprise-deal requests naming the language) is self-set. Make it explicit in your policy as your own decision, not a published standard.

## Stripe's three decoupled versioning policies - the canonical worked example

Stripe states the split directly: "We use the semantic versioning standard for SDKs, and version APIs by release date." Three genuinely separate policies:

1. **SDK package version - SemVer per package** (e.g. `stripe-python` 6.0.0). A breaking change to the SDK's code surface (renamed method, changed constructor) is a different event from a breaking change to the API contract. Conflating the two forces an SDK major release every time the API changes even when no client code broke, and vice versa.
2. **API version - date-based with account pinning.**
   - Each account is pinned to the API version active at its first request. Every breaking change ships as a new dated version (e.g. `2024-09-30.acacia`) rather than mutating the pinned one.
   - Cadence: two named major releases per year that may break, plus monthly backward-compatible releases.
   - A per-request `Stripe-Version` header overrides the pin for a single call: how canary-testing a new version works before migrating an account's default.

   Owning this policy is `samber/developer-platform-skills@api-versioning-policy`'s job. This skill only records the boundary.

3. **Language-runtime support window** - which host-language versions the SDK runs on:
   - Go: "the 4 most recent Go versions".
   - Node: "all LTS versions of Node.js 18+".
   - Python: 3.9+, with a 1-year extended-support window after a Python version's own upstream end-of-life.

   AWS runs the same policy as an explicitly separate axis (e.g. its Go SDK supports the latest two GA Go versions plus a 6-month grace window).

**The artifact that keeps decoupling workable: a published mapping table from SDK major version to the API version(s) it supports.** Both Stripe and AWS maintain this in GitHub wikis/READMEs - copy the artifact, not just the principle. The inferred recommendation to write into policy: bump SDK majors only on SDK-surface breaks, maintain the mapping table, and never let an API version change force an SDK major (or the reverse).

## Release cadence norms - a predictability promise, not a productivity metric

- **Azure:** a fixed monthly release train across all supported languages (its Java client BOM moved to monthly cadence in September 2021) - with Azure's own explicit warning: "YOU SHOULD NOT publish new package releases just to keep to a regular cadence." The train exists for integrator predictability, not to manufacture releases.
- **AWS:** continuous GA releases as changes land - new services, API updates, bug and security fixes - no calendar cadence.
- **Google Cloud:** continuous, auto-generated releases via the GAPIC Generator - release when the generator has new input.

Pick one model and state it in the strategy document. The choice follows the build model (a generated portfolio releases naturally on-change, a handwritten one benefits from a train that batches work).
