# Vendor key format, scoping, and ownership census

Cross-vendor reference tables backing steps 1, 3, and 6 of the workflow. Cite vendors as evidence of convergence, never as tools the reader must adopt.

## Prefix taxonomy across vendors

The prefix+random-body(+checksum) shape is near-universal among mature API platforms:

| Vendor    | Prefixes                                                                          | What the prefix encodes                                                              |
| --------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Stripe    | `sk_live_`, `sk_test_`, `pk_live_`, `pk_test_`, `rk_live_`, `rk_test_`, `sk_org_` | Key type (secret / publishable / restricted / org-level) × environment (live / test) |
| GitHub    | `ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_`                                            | Token class: personal, OAuth, user-to-server, server-to-server, refresh              |
| Slack     | `xoxb-`, `xoxp-`, `xapp-`                                                         | Bot vs user vs app-level token (hyphen-separated, not underscore)                    |
| Shopify   | `shpat_`, `shpca_`, `shpss_`                                                      | Admin token, custom-app, shared-secret classes                                       |
| OpenAI    | `sk-`, `sk-proj-`, `sk-svcacct-`                                                  | Account-wide vs project-scoped vs service-account                                    |
| Anthropic | `sk-ant-api...`, `sk-ant-admin...`                                                | API vs admin key class                                                               |

Stripe's `whsec_` is a webhook signing secret, not an API key - keep the two families visibly distinct in the taxonomy so neither is mishandled as the other.

Stripe authenticates via HTTP Basic Auth with the key as the username, HTTPS only - the key never needs a custom header scheme.

## GitHub's encoding, quantified

GitHub redesigned its tokens specifically for detectability - the old hex-only format was "indistinguishable from other encoded data like SHA hashes":

- 3-character prefix + `_` + 30-character Base62 random body + 6-character CRC32 checksum (Base62, leading-zero padded).
- Entropy: log2(62) × 30 ≈ 178.6 bits, up from ~160 bits in the prior 40-character hex format - more entropy in a similar length.
- The checksum lets a scanner structurally validate a candidate string before alerting or doing a database lookup, cutting false positives at the regex layer.
- Cost: roughly 10 characters of usable token length, per GitHub's own accounting. GitHub reused the identical design for npm tokens, citing the 128-to-178-bit entropy jump verbatim.
- Entropy floor from adjacent tooling: production-auth libraries warn below 32 characters / ~120 bits - treat that as the minimum, GitHub's ~178 bits as the benchmark.

## Secret Scanning Partner Program - the six-step registration

Register once the platform has real leaked-key incidents to justify the integration; the prefix+checksum format is the prerequisite either way.

1. Email `secret-scanning@github.com` and agree to GitHub's terms.
2. Supply a unique secret-type name plus a detection regex - GitHub explicitly recommends the prefix + high-entropy-body + checksum shape - and a test account.
3. Stand up a public HTTPS endpoint receiving webhook POSTs (JSON array of `token`/`type`/`url`/`source` matches).
4. Verify GitHub's request signatures using its ECDSA public keys (`ECDSA-NIST-P256V1-SHA256`, fetched from `https://api.github.com/meta/public_keys/secret_scanning`).
5. Revoke the reported secret and notify its owner - GitHub's guidance: treat any reported match as public and compromised, full stop.
6. Optionally return true/false-positive feedback (raw or SHA-256-hashed token only - GitHub accepts no other hash format for this channel).

Partner-pattern alerts run by default on all public repositories (owners cannot opt out) and go straight to the registered provider - near-real-time notice of a customer's leaked key, enabling auto-revocation before abuse. GitGuardian is the named commercial complement with broader surface coverage than GitHub's native scanning.

## Per-vendor scoping mechanics

| Vendor                   | Mechanism                                                                                                                                                                                                           | Notable constraints                                                                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GitHub fine-grained PATs | Scoped to exactly one resource owner (personal account or one org, never both), limited to selected repositories, granular per-permission grants (e.g. read-only issues, write pull requests), mandatory expiration | 64 permission types; 50 tokens per user; 366-day max expiry in org/enterprise contexts; org owners can require approval before issuance and can revoke members' PATs |
| SendGrid                 | Three-way split: Full Access / Custom Access (per-resource scopes) / Billing Access - one key holds billing or other permissions, never both                                                                        | Keys default to Full Access when scopes are omitted at creation - the named fail-open anti-pattern to design against; 69-character keys, 100 per account             |
| Slack                    | OAuth scopes attached per method (`chat:write`, `channels:history`) separately to bot (`xoxb-`) vs user (`xoxp-`) tokens                                                                                            | The same permission is granted differently depending on requesting token type                                                                                        |

GitHub recommends fine-grained PATs over classic tokens precisely because classic tokens carry broad scopes like `repo` and can live forever - the vendor's own argument for the promoted rung of the scoping ladder.

## Ownership models per vendor

| Tier            | Vendor examples                                                                                                                                                                                                                                                                    | Lifecycle behavior                                                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Individual      | GitHub PATs ("access GitHub resources on behalf of yourself"), OpenAI user keys ("tied to your user and work only while you retain access to the project")                                                                                                                         | Dies - or silently keeps working - on the owner's departure; full per-person accountability                                               |
| Organization    | Stripe `sk_org_` (requires `Stripe-Context` and `Stripe-Version` headers on every request; reaches across every account in the organization), GitHub org-approved PATs                                                                                                             | Bigger blast radius traded for cross-account convenience; adds a governance layer - approval before issuance, admin review and revocation |
| Service account | OpenAI service accounts ("a pseudo-user designed for system access", default read/write on the project, restrictable), Anthropic service-account keys (deliberately not workspace-scoped), Shopify custom-app `shpat_` tokens (owned by the app, not an employee login; no expiry) | Survives personnel changes by design - the credential's validity is decoupled from any human's employment status                          |

## Storage-model census

- Irretrievable (hash-only, shown once): Stripe, AWS, GitHub, OpenAI ("For security reasons, you won't be able to view it again"), Anthropic (returns only a `partial_key_hint`, e.g. `sk-ant-api03-R2D...igAA`), Linear, Resend; Shopify uses a "Reveal token once" flow. AWS IAM: "The secret access key can be retrieved only at the time you create it."
- Retrievable (encrypted, re-displayable): Twilio, Supabase, RapidAPI.
- Directional pattern: services handling sensitive or financial data lean irretrievable; lower-stakes services trade security for the convenience of retrieval.
