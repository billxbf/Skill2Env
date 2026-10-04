# Signing scheme reference

Worked detail behind SKILL.md step 3. Spec: Standard Webhooks (`standard-webhooks.com`, spec at `github.com/standard-webhooks/standard-webhooks`) - community-driven and vendor-neutral, with self-reported adoption by OpenAI, Anthropic, Google Gemini, Kong, Svix, Supabase, Twilio, PagerDuty, and others. Treat that list as directional (claimed, not audited), but it is the closest thing this domain has to a standard.

## Standard Webhooks construction

Three headers on every delivery:

```
webhook-id: msg_2KWPBgLlAfxdpx2AI54pPJ85f4W
webhook-timestamp: 1706100000
webhook-signature: v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=
```

Signature computation:

```
signed_content = "{webhook-id}.{webhook-timestamp}.{raw_body}"   # literal dots
signature      = base64( HMAC-SHA256( secret, signed_content ) )
header value   = "v1," + signature
```

Verification on the receiving side recomputes the HMAC from the raw body and, separately, rejects deliveries whose `webhook-timestamp` is older than a tolerance window - the spec recommends 300 seconds. Without the timestamp check, a captured legitimate request replays indefinitely: the signature proves authenticity, not freshness.

## Secret formats

- Symmetric HMAC secret: 24-64 random bytes, base64-encoded, prefixed `whsec_`; signature id `v1`.
- Asymmetric ed25519: private key prefixed `whsk_`, public key prefixed `whpk_`; signature id `v1a`.

The prefix makes a leaked key immediately identifiable as a webhook secret by scanning tools - a pattern worth copying even without adopting the full spec. Offer asymmetric signing when you don't control both ends: the consumer verifies with a non-secret public key instead of holding your shared secret. A single provider can support both modes simultaneously.

## Zero-downtime rotation

`webhook-signature` carries multiple space-delimited `<version>,<signature>` pairs; the receiver verifies against any of them. Rotation flow:

1. Issue the new secret; sign every delivery with both old and new.
2. Subscriber deploys the new secret and confirms verification passes.
3. Revoke the old secret only after confirming delivery success under the new one.

There is no cutover moment where a request fails to verify. Because the scheme is uniform, verification can also live once at an API-gateway layer instead of per-integration in application code.

## How the major non-adopters sign (contrast table)

| Provider | Header                                 | Content signed                                              | Encoding | Replay protection                                               | Rotation                                            |
| -------- | -------------------------------------- | ----------------------------------------------------------- | -------- | --------------------------------------------------------------- | --------------------------------------------------- |
| Stripe   | `Stripe-Signature` (`t=<ts>,v1=<sig>`) | `"{timestamp}.{raw_body}"`                                  | hex      | Yes (timestamp)                                                 | Roll secret, up to 24h dual-validity                |
| GitHub   | `X-Hub-Signature-256` (`sha256=<sig>`) | raw body only                                               | hex      | **None** - consumers track the `X-GitHub-Delivery` GUID instead | None - manual reconfigure with a gap                |
| Shopify  | `X-Shopify-Hmac-SHA256`                | raw body only                                               | base64   | **None**                                                        | Client-secret change with up to ~1h propagation lag |
| Convoy   | `X-Convoy-Signature`                   | "simple" (body) or "advanced" (Stripe-style with timestamp) | hex      | Opt-in via mode                                                 | Rolling secrets with explicit expiry                |

The pattern to learn from the weak rows: a body-only signature has no replay protection and usually no overlap rotation. GitHub's and Shopify's schemes predate the convergence - don't copy them for a new platform.

## Consumer pitfalls your signing docs must cover

These dominate real integration failures; document them explicitly rather than assuming they're obvious:

1. **Verify every request, no exceptions** - a handler that "only" posts to chat still triggers arbitrary side effects on a spoofed event.
2. **Verify against the raw body** - a framework's JSON body-parser re-serializes the body before the check runs and breaks the HMAC (e.g. Express needs `express.raw({ type: 'application/json' })` on the webhook route specifically).
3. **Exempt the webhook route from session-auth middleware** - the route authenticates by signature; uniform auth middleware 401s it before the handler runs.
