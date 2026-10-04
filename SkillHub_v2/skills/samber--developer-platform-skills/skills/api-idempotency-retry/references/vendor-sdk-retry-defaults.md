# Vendor SDK retry and idempotency defaults - cross-vendor comparison

How five platforms actually default and document this behavior, to calibrate your own SDK defaults and docs against. What converges is safe to copy; what diverges is exactly the part no standard settles - decide it explicitly for your own API.

## The comparison table

| Vendor                        | Default retry mode                                             | Max attempts      | Backoff / idempotency behavior                                                                                                                               |
| ----------------------------- | -------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS SDK v2 / CLI v2           | `standard`                                                     | 3 (incl. initial) | Exponential + jitter, gated by a token-bucket retry quota (14 tokens per transient-error retry, 5 per throttling retry, since the 2026 rebalance)            |
| AWS SDK `adaptive` mode       | opt-in                                                         | 3, same jitter    | Adds a client-side rate limiter reacting to throttling; not recommended for multi-tenant apps unless tenants get isolated clients                            |
| Stripe SDKs                   | client sets or omits the idempotency key; no fixed attempt cap | n/a               | v1: retry with the same key replays the previously saved response verbatim; v2: attempts to complete without side effects and may return an updated response |
| Google Cloud client libraries | per-service, varies                                            | varies            | Distinguishes _unconditionally_ idempotent operations (GET, list) from _conditionally_ idempotent ones needing preconditions/ETags before retry is safe      |
| Twilio                        | 24-hour idempotency window on config/orchestrator operations   | n/a               | Outbound webhook deliveries retried with exponential backoff up to 48 hours                                                                                  |
| Resend                        | idempotency opt-in per request                                 | n/a               | 24-hour key retention; two named `409` codes split payload-conflict from concurrent-in-flight                                                                |

## What to copy - the convergent core

- Retries on by default, bounded (AWS's 3 total attempts is the concrete anchor), with exponential backoff + jitter - since the 2023 update, most AWS SDKs ship this in standard/adaptive modes.
- A ~24-hour key retention window (Stripe, Resend, Twilio independently) - provided your retry chains actually fit inside it.
- Client-minted keys, V4 UUID recommended, generous length cap (Stripe: up to 255 characters).
- Payload-mismatch on a reused key rejected, never silently replayed.

## What to flag, not generalize

- **Stripe v1 vs v2 is a real behavioral fork - name the generation.**
  - v1: pure replay - same key returns the identical stored response, _including a stored 500_.
  - v2: supervised retry - may complete the operation without duplicating side effects, returning a response that differs from the original attempt.
  - "Stripe's idempotency model" without a version is an ambiguous claim.
- **Google Cloud has no single cross-product idempotency-key spec analogous to Stripe's.**
  - Cloud Storage uses object preconditions.
  - Individual APIs document their own retry guidance.
  - AIP-155 defines request IDs for the broader surface.
  - Scope any "Google does X" claim to the specific API.
- **Verified vs inferred:** none of Stripe, AWS, or Resend publish the isolation level or lock implementation behind their production key stores. Only the independent Postgres reference implementation (Brandur Leach's, Stripe-inspired) is concrete there - treat claims about "how Stripe's database enforces this" as inference from that reference design, never as disclosed internals.

## What this means for the SDK you ship

- The defaults decide behavior for the majority of callers who never read past installation - treat them as API contract, reviewed like one.
- Auto-generate an idempotency key for retry-unsafe operations when the SDK controls the request (Stripe's SDKs do) - the caller gets safe retries without knowing the mechanism exists.
- Expose the knobs (attempts, max delay, per-request key override) but make the zero-config path the safe one.
- Document the defaults in the SDK README with the same precision as the raw-HTTP contract: mode, attempt count, backoff shape, which operations get automatic keys.
