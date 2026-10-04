# Adoption and ROI evidence - ranked by strength, with a do-not-cite list

Use this file when building the business case in workflow step 1 or the impact disclosure in step 7. Every figure below is attributed to whoever published it; the last section lists figures that circulate widely and must not appear in any deliverable.

## Tier 1 - first-party published data (the strongest evidence that exists)

**Atlassian (July 2026, "What 5M+ daily MCP tool calls taught us")** - the only major vendor publishing hard first-party impact data, and the disclosure model to match:

- Over 5 million tool calls every working day, climbing month over month; 1M+ monthly users.
- Nearly a third of calls are writes - "agents creating structured data… a different pattern than any integration we've ever seen."
- 44% of MCP users aren't on software teams; over 50% of monthly active users are enterprise (up from ~40% in the earlier GA post - real growth between two disclosures).
- Grounded agents "deliver 44% more accurate answers using 48% fewer tokens"; "retention is up in every single cohort."

**Sentry** - publishes scale (its server grew 30M → 60M requests/month in roughly two months; 5,000+ organizations; 10-15 tools total) and monetizes MCP observability as an adjacent commercial product, but does not publish adoption-to-revenue attribution. Its stated design stance is deliberately cannibalistic: the server lets users do everything without visiting the web interface - optimizing user outcomes over engagement.

**Cloudflare** - internal-adoption commitment (13 → 27 internal servers in four months, all read-only first) but no external revenue figure.

**Stripe and Linear publish no MCP-specific adoption or revenue metrics at all.** Both are private companies; any online claim attributing revenue specifically to their MCP servers is unverifiable. Public commentary routinely conflates their agent-platform statistics with MCP-server usage - do not repeat that conflation.

## Tier 2 - citable analyst and survey baselines

- Forrester, "Predictions 2026: AI Agents, Changing Business Models, And Workplace Culture Impact Enterprise Software" (forrester.com blog, Nov 5, 2025): "Thirty percent of enterprise app vendors will launch their own MCP servers… Tech leaders need to interrogate their business app vendors on their approach to MCP."
- Stacklok's State of MCP survey (n=300 senior technical leaders, Dec 2025): ~41% of software organizations in limited-to-broad MCP production. **This is the citable adoption baseline** - use it instead of the inflated figures in the do-not-cite list.
- Enterprise pilots stall before production: only 11-14% of enterprise agentic pilots reach production (The Agentics Co., drawing on Stacklok), blocked on identity, audit, and access-control gaps - the exact scope of the write-safety and auth steps.
- Gartner (paywalled report): by 2026, 75% of API gateway vendors and 50% of iPaaS vendors will have MCP features; 40% of enterprise applications will include AI agents by end of 2026.
- RFP pressure is a qualitative signal only - MCP is described as "the new checkbox on RFPs." State it in those terms and never attach a percentage to it.

## Tier 3 - directional single-source analyses (cite with the label, never as industry fact)

- Bloomberry (1,412 real-world servers): median 5 tools per server, ~52% read / 25% write. Roughly half of the companies shipping a server have no public REST API, and 86% have no workflow-automation integration. For those vendors, MCP is a bet on a brand-new acquisition channel, not an extension of an existing surface.
- "Over 20,000 MCP servers in the wild; less than 5% make a single dollar" (individual DEV Community analysis) - the monetization counterweight; directional only.
- Production build-and-maintenance cost order of magnitude: a simple hand-built API-integration server at 150-250 hours; production-grade maintenance as a standing annual engineering commitment (Institute of AI PM estimate - vendor/analyst figure, not audited).

## The do-not-cite list

These circulate widely and are debunked or unverifiable. Citing any of them discredits the whole business case:

- **"78% of enterprises use MCP in production"** - explicitly flagged and debunked by an independent tracker. Use Stacklok's 41% instead.
- **"28% of Fortune 500 companies run production MCP deployments"** - debunked alongside the 78% figure.
- **A "Perplexity partial pullback from MCP"** - rests on a single unverified second-hand report; omit entirely rather than repeat.
- **"73% of outages originate at the transport/protocol layer"** - single vendor analysis, not independently corroborated; directional at best, never a statistic.
- Registry entry counts and package-download figures presented as usage - downloads measure install interest, exclude private mirrors, and cannot be read as execution counts (the 177,000-tool academic study states this limitation itself). Only in-server telemetry measures usage.

## The verdict to carry into any recommendation

For most B2B SaaS vendors in 2026, an MCP server is competitive/defensive positioning rapidly becoming procurement table stakes - "the competitive advantage has shifted from 'supports MCP' to 'supports MCP well.'" Proven direct-revenue ROI is demonstrated by a handful of leaders, with Atlassian's data the strongest single dataset. The clear exception: a vendor with no prior public API, for whom MCP can open a genuinely new acquisition channel.
