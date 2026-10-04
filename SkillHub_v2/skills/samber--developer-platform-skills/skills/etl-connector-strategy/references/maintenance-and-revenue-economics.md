# Connector maintenance economics and the revenue-share reality

## Build-cost baselines

Vendor-published estimates from integration-tooling vendors (both sell integration products - treat as order-of-magnitude, never as quotes): a single moderately complex API integration at $10,000-$50,000 to build (Albato); $50,000-$150,000+ for a single advanced integration (Bindbee). Use the ratio these imply, not the figures, when sizing a specific build.

## The maintenance tax

- **Annual maintenance runs 15-30% of the original build cost, and can reach 50% in mature, high-change phases** (Bindbee: "annual maintenance runs 15–25% of the original build cost, and can reach 50% in mature phases"; their cited example puts ten in-house integrations' upkeep at roughly $150,000/year - keep the ratio, drop the figure outside that context).
- The tax compounds linearly with connector count: each connector is an independent recurring obligation sharing no fixed cost with the others. Practitioner framing: self-built connector maintenance is "manageable at three to five sources" but "punishing across more than ten" - the point where it becomes specialist work.
- **Four cost drivers** account for most of the spend:
  - Authentication changes.
  - Schema drift - fields renamed, retyped, or restructured without notice.
  - Rate-limit shifts.
  - Pricing/compliance overhead.

## The one peer-reviewed figure in this domain

Yasmin, Tian & Yang, "A First Look at the Deprecation of RESTful APIs: An Empirical Study" (ICSME 2020): across 1,068 specifications spanning 212 multi-version APIs, 251 versions introduced breaking changes - and **219 of those (87.3%) shipped with no deprecation information at all**; only 32 (12.7%) carried any prior signal. The same study found on average 46% of a REST API's operations are deprecation-related at some point in its lifecycle. Even a "generous" notice window in industry commentary is often only 30 days.

Two planning consequences:

1. Budget for upstream breakage arriving unannounced - monitoring, not changelog-watching, is the detection mechanism.
2. The vendor's _own_ API change discipline directly sets this cost for every connector and every customer pipeline built against it - which is why the extraction-readiness audit sequences before any build.

## Who absorbs the tax, per build path

- **Platform-managed listing**: the platform absorbs it. The managed platforms' own pitch is connectors that "require zero maintenance, and automatically adjust to source changes," and customer-side quotes credit exactly this (Strava's data scientist on being freed from maintaining connectors and handling API changes).
- **Vendor-SDK connector**: split - the platform hosts and runs the code and centralizes shared logic (a low-code layer ships cursor-handling fixes once for every connector built on it), but the vendor must validate data, notify the platform of upcoming source changes, and redeploy.
- **Custom outside-platform connector**: 100% with whoever built it. Meltano's own warning about the "benevolent community member" model is the documented failure shape.

## Revenue share: essentially does not exist

- **No ETL/ELT platform pays a source vendor for a connector.** Fivetran charges its customers on Monthly Active Rows; the customer pays, the source vendor is not paid, and no public program shares that revenue back. Stitch/Singer and Meltano run on free contributions - historically Singer contributors received swag, not money.
- **Airbyte is the only platform that ever proposed revenue share, and it did not ship as announced.** September 2021, tied to its license change: a floated "participative model" where connector maintainers "would have the option to get a revenue share" in exchange for owning SLAs and fixes - explicitly conditional language. Cite it as announced-but-never-delivered-as-described, never as an existing precedent.

  What shipped in April 2022 was a bounty-based Maintainer Program of flat one-time fees, a shape the current Contributor Program still keeps:
  - New sync mode: $150.
  - Missing streams: $150.
  - Full unit-test coverage: $150.
  - Critical bug: $100.
  - Minor bug: $50.
  - Docs: $10-$25.

- **Certification is not charged either**, on any platform: the cost of a badge is the vendor's engineering time, not a listing fee.

## What exists instead: co-marketing and partner programs

Real, but not connector pay:

- Fivetran's enhanced Partner Program (announced 2025) offers partner tiers, resell/co-sell motions, co-branded marketing and demand-gen tools, and a partner academy.
- Airbyte's partner program (launched 2024) targets technology-services providers with co-sell support.

Both are primarily consulting/reseller/SI and technology-alliance motions - **neither platform publicly offers a SaaS source vendor paid premium catalog placement or expedited engineering priority**. Treat that as "not publicly stated," not as proof private arrangements never happen.

## Payoff ranking for the internal pitch

By realistic, attributable value: **support-ticket deflection and customer retention (real, direct, immediate once the connector ships) > competitive-parity distribution (real but hard to attribute) > co-marketing/demand-gen via a partner tier (available, but requires an active partnership relationship, not just a listed connector) > revenue share (essentially does not exist - do not plan around it)**.

Lead the internal business case with support-cost and retention math. A case built on a hoped-for revenue line fails at its first finance review - and deserves to.
