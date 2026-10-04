# Storage and lookup schema

Implementation detail behind step 2 of the workflow: the table shape, the lookup flow, and the full hashing rationale.

## The schema (irretrievable default rung)

```sql
CREATE TABLE api_keys (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id UUID NOT NULL,            -- user, org, or service account (see step 6)
  key_prefix VARCHAR(16) NOT NULL,   -- plaintext, indexed: the O(1) lookup handle
  key_hash CHAR(64) NOT NULL,        -- SHA-256 of the full key; never the plaintext
  name VARCHAR(255),                 -- human label, e.g. "CI pipeline - staging"
  scopes TEXT[] NOT NULL,            -- restrictive by default, never empty-means-all
  created_at TIMESTAMPTZ DEFAULT NOW(),
  last_used_at TIMESTAMPTZ,          -- written async, fire-and-forget
  expires_at TIMESTAMPTZ             -- also carries the rotation grace window
);
CREATE INDEX idx_api_keys_prefix ON api_keys(key_prefix);
```

- `key_prefix` here means the key's leading characters (type/environment prefix plus the first few body characters), stored plaintext - enough to narrow lookup to a handful of rows, too little to reconstruct the secret.
- `expires_at` is doing double duty by design: normal expiry, and the grace-period end when a rotation marks the old key `expiring` instead of deleting it.
- Never `scopes` defaulting to full access when omitted - that is SendGrid's named fail-open anti-pattern.

## Lookup flow on every request

1. Parse and structurally validate the presented key: known prefix, correct length, checksum passes. Reject malformed input with no database round-trip.
2. Query by plaintext `key_prefix` (indexed) to get the small candidate set.
3. Compute SHA-256 of the presented key; compare against each candidate's `key_hash` in constant time - a naive string `==` leaks timing information.
4. Check `expires_at` and revocation status; enforce scopes (authorization, after authentication).
5. On success, enqueue the `last_used_at` update asynchronously - never block the request on telemetry.

## Why SHA-256, and the debate history

Fast SHA-256 is the prevailing choice for machine-generated keys, but it was a genuine practitioner debate - present it as prevailing-with-rationale, not as always-obvious:

- The case for fast hashing: bcrypt/Argon2 (and OWASP's password-storage guidance recommending them) exist to defend low-entropy, human-chosen secrets against brute force. A generated key at 120-178 bits of entropy is not brute-forceable at any per-hash cost: an RTX 4090 computes ~21.2 billion SHA-256 hashes/second (hashcat v6.2.6, mode 1400) - devastating against an 8-character password, irrelevant against 2^178 combinations. A slow hash therefore adds CPU on every authenticated request without a corresponding security gain. Vendor guidance (Zuplo's apikeys.guide): "For irretrievable keys, hash with SHA-256: fast, deterministic, FIPS 180-4 standardized. bcrypt and Argon2 are a performance anti-pattern for high-entropy secrets; reserve them for passwords."
- The minority position, still live: slow-hash everything as defense-in-depth in case a key is ever generated with insufficient entropy, or for uniform treatment of all stored secrets. Some production systems layer SHA-256 lookup with a bcrypt verification pass; many hash directly with bcrypt.
- Two mechanics tilt toward SHA-256 regardless:
  - Salted slow hashes cannot be looked up (`WHERE hash = ?` never matches across salts - hence the prefix-lookup column).
  - bcrypt truncates input at 72 bytes, so long keys must be pre-hashed with SHA-256 anyway, undercutting "just bcrypt everything" as a uniform policy.
- The entropy precondition is what makes fast hashing safe: enforce the 120-bit floor at generation (step 1) or the whole rationale collapses.

## Retrievable rung storage

When the interview lands on retrievable (low-stakes data, lost-key support load dominates):

- Encrypt with AES-256-GCM. Hold the key-encryption-key in a KMS, never in application config.
- Store a SHA-256 hash alongside the ciphertext so request-path validation never needs a decrypt round-trip - decryption happens only on an explicit dashboard "reveal" action, which is itself an audit-logged event (step 7).
