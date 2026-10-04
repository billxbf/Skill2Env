# Idempotency key lifecycle - worked walkthrough

A complete pass through one key's life, from first claim to reaping, using the default-rung mechanism (DB unique constraint) and the patterns from the Postgres reference implementation (Brandur Leach, brandur.org/idempotency-keys). No vendor publishes their production internals, so treat this as an independent, Stripe-inspired reference design, not Stripe's disclosed code.

## Storage schema

Relational-flavored for concreteness; every column maps to a concept any store needs.

```sql
CREATE TABLE idempotency_keys (
  id              BIGSERIAL PRIMARY KEY,
  account_id      BIGINT NOT NULL,          -- per-caller scope, never global
  idempotency_key TEXT NOT NULL,            -- client-minted, e.g. up to 255 chars (Stripe's cap)
  request_fingerprint TEXT NOT NULL,        -- payload checksum for the mismatch guard
  locked_at       TIMESTAMPTZ,              -- non-NULL = in-flight; drives lock recovery
  recovery_point  TEXT NOT NULL DEFAULT 'started',  -- resumable position for multi-step requests
  response_status INT,                      -- stored outcome: both success AND failure
  response_body   JSONB,                    -- replayed verbatim on completed retry
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (account_id, idempotency_key)      -- the atomic claim: the DB picks one winner
);
```

## The atomic claim

Never `SELECT` then `INSERT` - under concurrent retries both callers see "absent" and both proceed (TOCTOU). Insert first and let the constraint arbitrate:

```sql
INSERT INTO idempotency_keys (account_id, idempotency_key, request_fingerprint, locked_at)
VALUES ($1, $2, $3, now())
ON CONFLICT (account_id, idempotency_key) DO NOTHING
RETURNING id;
```

- A returned row: this caller won the claim; proceed as a first attempt.
- No row: the key exists. Read it and branch on its state (next section).
- The claim insert and the business mutation commit in one transaction (or the first atomic phase's transaction) - the AWS hard requirement: token recorded and effect applied are all-or-nothing.

## Branching on an existing key - the three states

**State: complete** (`response_status` set) - first compare `request_fingerprint`.

- Fingerprint matches → replay `response_status` + `response_body` verbatim. No re-execution, even if the stored outcome is a 500 (Stripe v1 semantics: the retry gets exactly what the original got).
- Fingerprint differs → payload mismatch, a client bug. Reject:

```json
HTTP/1.1 409 Conflict
{ "code": "invalid_idempotent_request",
  "message": "This idempotency key was already used with a different request payload. Use a new key, or resend the original payload." }
```

(Resend's documented code name; fix advice belongs in the message - see `samber/developer-platform-skills@api-error-design` for message rules.)

**State: in-flight** (`locked_at` recent, no stored response) - the original is still running. Default handling, per the field convention:

```json
HTTP/1.1 409 Conflict
{ "code": "concurrent_idempotent_requests",
  "message": "A request with this idempotency key is currently in progress. Wait and retry." }
```

Never let the second caller through because the first "seems stuck" - the alternatives (block for the bounded result; 202 + status URL for long-running effects) also keep exactly one executor. The expired IETF draft made this deliberate: in-flight conflict and completed replay are different responses, not fallbacks.

**State: in-flight but lock expired** (`locked_at` older than the lock timeout) - the original crashed or was abandoned. This caller may take over the lock (an atomic conditional `UPDATE ... SET locked_at = now() WHERE locked_at < $threshold`) and resume from `recovery_point` - not from the beginning.

## Multi-step requests: recovery points around foreign state mutations

A request that calls an external, non-rollbackable system mid-flight (a card charge, an outbound email) cannot be one transaction. Decompose into atomic phases separated by each foreign call:

```
Phase 1 (txn): claim key, validate, create local order row     → recovery_point = 'order_created'
  -- foreign state mutation: charge the card --
Phase 2 (txn): record charge id                                 → recovery_point = 'charge_recorded'
  -- foreign state mutation: send confirmation email --
Phase 3 (txn): store final response                             → recovery_point = 'finished'
```

- Within each phase, everything commits or nothing does (ACID).
- Record intent _before_ each foreign call - a crash between the call and its response then leaves evidence to reconcile, instead of a silent duplicate on retry.
- A retry (or the completer) reads `recovery_point` and resumes at the right phase: `charge_recorded` means the card is charged - never charge again, continue to the email.

## Retention: two horizons, then reaping

- **Replay window (~24h)** - governs correctness: retries inside it replay; a reused key after it is treated as a brand-new request (every surveyed provider does this; none errors on post-TTL reuse). Set it from the longest retry chain - DLQ replays, dispute windows - not from storage cost. Tell integrators the operational consequence, as Resend does: "complete your retry logic well within 24 hours."
- **Reaper threshold (~72h)** - governs operations: records outlive the replay window so a bad Friday deploy's failed requests survive the weekend for a developer to push through on Monday.

## The two background jobs

- **Completer**: finds requests that look abandoned mid-flight (claim held, lock expired, client gave up) and pushes them to completion using only idempotency keys and recovery points - no per-endpoint knowledge.
- **Reaper**: deletes records past the reaper threshold, attempts cleanup on anything unfinishable, and logs what it couldn't finish for a human to chase.

Recovery is these active processes, not passive expiry - expiry alone leaves half-finished requests half-finished forever.

## Client-side pairing

The key only works if the client reuses it across retries of one intent. For critical calls, write the intent to a durable queue with a pending status _before_ the first attempt, so the retry state - key included - survives an application restart.

Derivation, in the recommended order:

- Event-derived (`order-confirm-${orderId}`) - deterministic by construction.
- Request-scoped (`reset-${userId}-${resetRequestId}`).
- A random UUID generated once and reused.

The anti-pattern that defeats everything: `Date.now()` or a fresh `crypto.randomUUID()` per attempt.
