# Staged rollout with go/no-go thresholds

The three-stage plan below is based on named vendor practice - Cloudflare's internal portal is the closest real-world precedent (13 servers in April 2026 → 27 in Aug 2026, every one launched read-only first). The stage-gate numbers are not an industry standard; treat them as calibration defaults and re-baseline against your own first month of telemetry.

## Stage 1 - a credible, safe read-only server (order of weeks)

- Curate roughly 5-15 workflow-level tools designed top-down from real user jobs, never 1:1 from API endpoints (real-world median across 1,412 servers: 5 tools). Benchmark agent task-completion before and after pruning to this range.
- Read-only only. Implement OAuth 2.1 with PKCE (S256) and resource indicators from day one on the remote server - this is what passes enterprise security review, and it already puts the server well ahead of the community-server long tail on auth compliance.
- Instrument with OpenTelemetry from the first call: per-tool latency, error rate, call volume, client breakdown.
- Publish to the official MCP registry under a DNS-verified namespace; fan out to third-party directories.

**Gate to Stage 2**: sustained tool-call volume from real agent clients - explicitly not hackathon or demo spikes - and a tool-error rate under 2%.

## Stage 2 - write tools behind graduated safety (order of a quarter)

- Adopt a four-tier risk model (Read Only / Minimal Impact / Contained Write / Critical) enforced server-side so it cannot be bypassed by switching clients.
- Human-in-the-loop approval on every Contained Write tool.
- Critical-tier tools disabled by default.
- One risk level per tool.
- Scoped/restricted credentials.
- Agent and session attribution plus asynchronous audit logging on every write.
- Idempotency keys.
- Dry-run preflight wherever feasible.
- Rate or spend caps on financially consequential tools.

**Gate to expand write scope**: a clean audit trail, zero unattributed writes, and demonstrated approval-flow reliability in production.

## Stage 3 - differentiate and prove value (second quarter onward)

This is the move from "supports MCP" to "supports MCP well."

- **MCP Apps UI** for the single highest-value workflow - an approval screen, a filterable dashboard, a configuration wizard.
  - MCP Apps launched January 26, 2026 as the protocol's first official extension: a tool points at a UI resource that the client renders in a sandboxed iframe, communicating over audited messages.
  - It uses pre-declared templates rather than runtime-generated HTML, with optional user consent on UI-initiated tool calls.
  - Day-one launch partners: Amplitude, Asana, Box, Canva, Clay, Figma, Hex, monday.com, Salesforce, Slack.
  - Day-one client support: Claude, ChatGPT, Goose, VS Code. Real adoption, not a paper spec.
- **The gate before investing here**: validate that your target customers' security teams will permit iframe-rendered third-party UI inside their organization's AI assistant at all. Independent analysis flags this as the ecosystem's open adoption question - unresolved, not a settled yes. Ask two or three design partners before building.
- Institutionalize the tool-surface versioning discipline the spec doesn't mandate:
  - Schemas and prose descriptions treated as contract.
  - Golden-prompt behavioral CI.
  - A published deprecation window of at least 90 days with response-header signaling.
  - Schema version logged on every call.
- Measure and publish impact using the strongest first-party disclosure in the ecosystem as the model - the disclosure shape Atlassian published and the one to match:
  - Tool-call volume, write share, non-technical-user share, enterprise share.
  - Retention by cohort.
  - Accuracy and token-efficiency gains.

## The override that cuts across all stages

- **Accelerate**: if MCP appears as a hard requirement in actual buyer RFPs, move straight to Stage 2 or 3 regardless of where the timeline says you are - procurement pressure is the demand proof the staged plan exists to wait for.
- **Park**: if tool-call volume stays flat and no RFP demand materializes after two full quarters, treat the server as low-maintenance table-stakes positioning, keep Stage 1 maintained, and explicitly defer the production build-out until real demand is proven.
