# Write-tool safety patterns: the six-pattern taxonomy

Each pattern below is proven by at least one named vendor implementation. They stack - a production write surface typically runs three or more at once. The organizing principle across all six: enforcement belongs server-side, because an end user cannot bypass a server-side control by switching MCP clients or disabling a local hook.

## (a) Scoped / restricted credentials

Issue the agent a credential scoped to only the operations it needs, enforced server-side - never the account's full-power key. Stripe's Restricted API Keys are the reference case: a read-only key cannot create refunds even if the model tries. GitHub's equivalent is fine-grained tokens plus toolset selection, so a consumer enables only the tool groups it needs.

- Pair with test-mode-first defaults where the product has a sandbox: new agent integrations start against test data.
- Friction: near zero once issued. This is the pattern to ship first.

## (b) Read-only vs write separation / lockdown mode

A server-level switch that strips every write tool from the surface, taking precedence over any other configuration. GitHub ships this as an environment flag and a request header.

- **Verify it, don't just configure it**: a documented GitHub bug (issue #2156) found the read-only flag failed to omit write tools in some configurations. Test that write tools are actually absent under lockdown before relying on it.
- GitHub also sanitizes tool-description content against prompt injection by default - description text is an attack surface (tool poisoning), and a lockdown mode doesn't cover it.

## (c) Human-in-the-loop confirmation

The spec-level primitive is elicitation: the server requests structured mid-call user input and the client renders a confirmation form before a destructive action executes. Named implementations span a sophistication range:

- Cloudflare's decision tree:
  - Durable approval waits for multi-step workflows that can pause hours or days.
  - A needs-approval predicate for chat tools.
  - Elicitation for servers proper.
  - Their stated rule: only require confirmation for actions with meaningful consequences (payments, emails, data changes) - approval fatigue on trivial calls trains users to click through.
- Block's Goose runs three permission levels across three modes; its smart mode combines an LLM permission classifier with the read-only annotation to auto-approve low-risk calls and flag the rest - a real case of annotations driving an authorization decision rather than staying advisory.
- Notion lets admins toggle each tool individually and choose per-tool whether it confirms or runs automatically. Azure requires elicitation consent for any tool handling secrets.
- Keep immutable audit logs regardless of approval outcome.

## (d) Risk-tiered server-side policy gates with attribution and audit

The most sophisticated pattern found, and the taxonomy's starved option. Cloudflare's WriteGuard (announced Aug 5, 2026) was built after "the Case of the Endlessly Closing Tickets" - an unattended background agent closed thousands of tickets. A shared policy layer sits in front of every MCP server and classifies each call into four tiers:

| Tier            | Action                                               |
| --------------- | ---------------------------------------------------- |
| Read Only       | pass through                                         |
| Minimal Impact  | pass through                                         |
| Contained Write | enrich with agent attribution + scrubbed audit event |
| Critical        | block before the handler runs                        |

Design choices worth copying:

- The human stays the principal - the agent operates under the employee's own permissions with added agent/session context, and there are no separate agent accounts.
- Audit logging is asynchronous, so it adds no request latency.
- A merge tool that triggers deployments is Critical-tier and disabled outright.

Cloudflare's internal portal grew from 13 servers (April 2026) to 27 (Aug 2026), every one launched read-only first.

Apply Block's rule when tiering: one risk level per tool. A tool spanning two tiers is two tools.

## (e) Dry-run / preflight modes

A `dry_run: true` parameter on destructive tools that returns planned-effect fields (what would be deleted, updated, archived) without mutating anything. A community Notion server implements this; the pattern is still rare - recommend it, and flag it as uncommon rather than standard.

**The negative example to design against**: a community Shopify server ships no dry-run at all - every create-product, delete-product, order-cancel, and refund call is live - and an open PR flagged that its order tools could send real customer emails and SMS with no confirmation step. The rule that follows: when dry-run isn't feasible, keep every destructive tool behind an approval gate; never ship a live-only destructive tool with no safety net.

## (f) Idempotency, rate limits, and spend caps

The least standardized layer. Idempotency keys and per-credential rate limits exist at the API level (Stripe's model); agent-specific spend caps are not yet a standardized MCP pattern.

- Add idempotency keys on every write.
- Add rate or spend caps on any financially consequential tool.

**Name the gap honestly**: undo/rollback is largely absent industry-wide. The ecosystem substitutes audit trails and attribution - pattern (d) - for true reversibility. Do not imply a mature rollback answer exists; design writes to be attributable and auditable because they will not be reversible.

## Rendering approvals as UI

MCP Apps is the protocol's official server-rendered UI extension, a stage-3 investment. It can render pattern (c)'s confirmation step as an in-conversation form or review dashboard instead of a bare text prompt. The direct product tie-in for write-heavy servers is the document-review use case, where the model sees approve/flag decisions in real time.
