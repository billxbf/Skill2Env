# Rate-limit header families - syntax, adoption, and Retry-After mechanics

The wire formats behind the header-family menu, with the cross-vendor evidence for why the legacy family is still the default.

## Legacy family: the `X-RateLimit-*` trio

```
HTTP/1.1 200 OK
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640000000
```

- `Limit`: ceiling for the current window.
- `Remaining`: calls left in it.
- `Reset`: when the window rolls over.

This is the de facto convention most real APIs ship today, but **reset semantics vary by vendor**: GitHub's `reset` is a UTC epoch timestamp, other vendors use seconds-until-reset. Document which one yours means, and never change it silently - that swap breaks client parsing invisibly instead of producing a visible error.

## IETF family: `RateLimit` and `RateLimit-Policy`

Source: `draft-ietf-httpapi-ratelimit-headers` (IETF httpapi WG; R. Polli, A. Martinez, D. Miller). Current version: **draft-11, dated 23 May 2026, expiring 24 November 2026** - Standards Track intent, still an Internet-Draft, not an RFC. The most recent HTTPDIR early directorate review (filed against draft-10) came back marked "not ready" - an ordinary part of IETF process, but it means field syntax can still change before RFC, reinforcing the caution against treating the field names as settled.

```
RateLimit-Policy: "default";q=100;w=60
RateLimit: "default";r=15;t=23
```

- `RateLimit-Policy` advertises the quota policy itself: `q` = quota units, `w` = window in seconds, optional `pk` = partition key. This is the field that lets a well-behaved client self-throttle before its first 429.
- `RateLimit` reports current state: `r` = remaining quota, `t` = time to reset.
- Multiple simultaneous policies are explicitly supported (an hourly and a daily quota advertised together); the draft also covers concurrency limits, not just request rates.
- Deliberately unspecified: no mandated algorithm, no mandated correlation with status codes, and **no guarantee implied** - the values "are informative and MAY be ignored"; a client seeing "5 remaining" is not promised those 5 calls.
- Syntax churn risk: versions ≤07 used a different `limit=…, remaining=…, reset=…` list syntax; draft-08+ moved to the quoted structured-field form. Track the httpapi WG rather than hard-coding today's field names as permanent.
- The draft's own text concedes that a naive fixed-window reset design "encourage[s] clients into cyclic burst-pause behaviour" - the reset-boundary stampede - which is why published retry guidance still needs jitter even with a standardized header.

**Current adoption reality:**

- Cloudflare adopted the draft in September 2025 - the one named Tier-1 example.
- GitHub still emits only the legacy `X-RateLimit-*` family.
- Stripe emits neither family.

A policy cannot assume clients parse the IETF fields, and a client cannot assume any API emits them.

## `Retry-After` mechanics

- Status code 429 Too Many Requests is defined by RFC 6585 (April 2012), which also **forbids caching a 429** - a caching proxy that ignores this makes the throttle appear to persist longer than intended.
- `Retry-After` has two valid forms per RFC 9110: delay-seconds (`Retry-After: 120`) or an HTTP-date (`Retry-After: Wed, 21 Oct 2026 07:28:00 GMT`). Delay-seconds dominates in APIs and gateways; HTTP-date appears mainly around planned maintenance.
- The pervasive client bug: `parseInt`-ing the header assuming delay-seconds - an HTTP-date parsed that way yields `NaN`, and an unclamped client falls into an instant retry storm. Prefer emitting delay-seconds; your docs should tell clients to detect both forms and clamp to ≥ 0.
- Precedence rule (IETF draft, verbatim): "If a response contains both the RateLimit and Retry-After fields, the Retry-After field MUST take precedence and the effective window MAY be ignored."

## Cross-vendor comparison

| Platform        | Header family                                                                    | Reset semantics                       | Throttle signal                                                    |
| --------------- | -------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------ |
| GitHub REST     | `x-ratelimit-limit/remaining/used/reset/resource` (+ `retry-after` on secondary) | UTC epoch seconds                     | 403 or 429; JSON message; primary → `x-ratelimit-remaining: 0`     |
| GitHub GraphQL  | same headers + `rateLimit{}` body object                                         | epoch seconds                         | primary over-limit → **HTTP 200** with error + `remaining: 0`      |
| Stripe          | `Stripe-Rate-Limited-Reason` only (no `X-RateLimit-*`, no IETF fields)           | n/a                                   | HTTP 429, `type: rate_limit_error` + `code`; SDKs retry internally |
| Shopify REST    | `X-Shopify-Shop-Api-Call-Limit: 40/40`; `Retry-After` on 429                     | n/a (bucket)                          | HTTP 429                                                           |
| Shopify GraphQL | `extensions.cost.throttleStatus` in body                                         | n/a (bucket)                          | **HTTP 200** with `THROTTLED` error code                           |
| SendGrid        | `X-RateLimit-Limit/Remaining/Reset`; `Retry-After` on 429                        | reset window                          | HTTP 429                                                           |
| Discord         | `X-RateLimit-*` + `Reset-After`/`Bucket`/`Scope`/`Global`; `Retry-After`         | epoch seconds + `Reset-After` seconds | HTTP 429, JSON `{message, retry_after}`                            |
| Twilio          | `Twilio-Concurrent-Requests` (concurrency-based)                                 | n/a                                   | HTTP 429, error `20429`                                            |

The load-bearing conclusion: header formats are genuinely incompatible across vendors - three separate legacy headers vs two structured IETF fields vs vendor-unique shapes vs body-only signaling. Whatever family you pick, your published docs are the only thing that makes it parseable on purpose rather than by reverse engineering.

## Implementation notes

- Stripe's exact headers vary by account and should be confirmed empirically: it emits `Stripe-Rate-Limited-Reason` and a `rate_limit_error` body but does not document a `Retry-After` header at all - its posture is "react to 429s, throttle client-side, SDKs retry internally".
- The IETF draft is a distinct standard from RFC 9457 Problem Details: rate-limit state vs generic error-body shape, different layers, not competing options.
- GitHub's secondary-limit point figures (900 points/min REST, 2,000/min GraphQL) are stated directly in GitHub's own rate-limits documentation - cite them as official. The per-endpoint point cost of some individual endpoints stays undisclosed by GitHub's own admission.
