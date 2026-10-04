# Authentication and Setup Preconditions

Everything in this file comes from the mailbox providers' and standards bodies' own documentation unless labeled otherwise. Requirements evolve; if you can browse the web, re-check the provider sender-guideline pages before asserting a date or threshold as current.

## Provider requirements (2024-2026 enforcement wave)

| Requirement                      | Gmail (Feb 1, 2024)                                                                                          | Yahoo (Feb 2024)                           | Microsoft consumer - outlook.com/hotmail/live (May 5, 2025)                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Bulk threshold                   | 5,000/day to personal Gmail, counted per primary domain (subdomains included); status permanent once reached | "significant volume" - no published number | 5,000/day per domain                                                                                            |
| All senders                      | SPF **or** DKIM; valid forward + reverse DNS (PTR); TLS; RFC 5322 format                                     | SPF/DKIM; valid DNS; RFC 5321/5322         | N/A                                                                                                             |
| Bulk senders                     | SPF **and** DKIM; DMARC at least `p=none`; DMARC alignment                                                   | Same                                       | SPF, DKIM, DMARC (≥ `p=none`, aligned) must all pass                                                            |
| One-click unsubscribe (RFC 8058) | Required for marketing/subscribed messages                                                                   | Required; honor within 2 days              | Recommended, not mandated                                                                                       |
| Spam-rate ceiling                | <0.10% target; never ≥0.30%                                                                                  | "keep below 0.3%"                          | none published                                                                                                  |
| Non-compliance                   | 4.7.x temp / 5.7.x permanent codes; mitigation loss                                                          | junk/bounce                                | outright rejection: `550 5.7.515 Access denied, sending domain does not meet the required authentication level` |

Do not claim one universal deadline: Gmail/Yahoo enforced from February 2024, Microsoft from May 5, 2025. Microsoft 365 business tenants are outside the consumer mandate's stated scope (inferred from Microsoft's own scoping language, not verbatim).

## Alignment

DMARC alignment = the From: header's organizational domain matches the SPF domain **or** the DKIM signing domain - one suffices at all three providers. Misalignment is the classic silent failure: SPF and DKIM each "pass" for some other domain (a sequencer's or ESP's), DMARC still fails. Gmail's alignment failure code is 4.7.32.

## Enforcement codes worth recognizing

- Gmail temporary: 4.7.23 (PTR), 4.7.27 (SPF), 4.7.29 (TLS), 4.7.30 (DKIM), 4.7.31 (missing DMARC), 4.7.32 (alignment). Permanent: 5.7.25 / 5.7.27 / 5.7.30.
- Microsoft: `550 5.7.515` - permanent rejection for unauthenticated bulk domains.
- `550 5.4.5 Daily sending quota exceeded` - a Google Workspace **account cap** breach, not a reputation signal. See "Hard caps" below.

## One-click unsubscribe specifics (bulk/marketing mail)

- Both headers required: `List-Unsubscribe:` with an HTTPS URL, plus `List-Unsubscribe-Post: List-Unsubscribe=One-Click`.
- A `mailto:` link alone does **not** satisfy the requirement; Gmail does not check the body for a link if the header is missing.
- Also include a clearly visible unsubscribe link in the body; honor requests within 48 hours (Gmail recommendation; Yahoo says 2 days).
- Applies to marketing/subscribed mail; transactional messages are exempt. Genuine 1:1 cold B2B below bulk thresholds is not covered by RFC 8058 - the plain-text opt-out question for that case is contested (see content reference).

## DMARC rollout and DKIM keys

- Ladder: `p=none` (monitor via `rua=` aggregate reports) → `p=quarantine` (optionally staged with `pct=`) → `p=reject`. Never jump straight to reject on a domain with unknown mail flows.
- DKIM keys: 1024-bit minimum, 2048-bit recommended (Gmail guidance).

## Verifying records

If you can run shell commands or DNS lookups:

```
dig TXT <sending-domain> +short              # SPF (exactly one record)
dig TXT <selector>._domainkey.<domain> +short # DKIM (selector from your sender/ESP)
dig TXT _dmarc.<sending-domain> +short        # DMARC
```

No output = record missing. Otherwise, ask the user to paste these lookups or a recent DMARC aggregate-report summary.

Known DNS gotchas (practitioner-documented):

- One SPF record per domain, ever. A second SPF TXT record invalidates both - merge `include:` mechanisms into a single record.
- Some DNS hosts split long DKIM values into multiple quoted strings; a stray space between the quoted parts silently breaks verification.
- SPF enforces a DNS-lookup cap; stacking sequencer + ESP + CRM `include:` mechanisms can exceed it and fail silently - flatten or prune the record.

## Domain and mailbox architecture - mechanics

The choice between architectures is ranked in SKILL.md ("Domain architecture - ranking the legitimate options"); this file carries only the mechanics that ranking assumes.

- Every sending domain must honestly identify the real sender - visible brand, real names, working reply path. A domain chosen to disguise the sender or dodge a limit crosses the ethics boundary; refuse.
- Gmail counts bulk-sender volume across the primary domain including subdomains - subdomain splitting does not reset the 5,000/day clock.
- A subdomain inherits the organizational domain's DMARC policy by default and pushes reputation back toward it; a separately registered domain shares neither, which is why its blast radius is contained and its warming starts from zero.
- B2B and B2C alike need the full authentication stack on every sending domain.

## Hard caps vs reputation thresholds - never conflate

| Number                                                         | What it is                                                                       | Consequence                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 2,000 msgs/day (paid Google Workspace account; 500 trial/free) | Outbound **account** hard limit, rolling 24h window (not midnight reset)         | `550 5.4.5`, ~24h lockout                                      |
| 5,000 msgs/day to one provider                                 | Inbound **bulk-sender classification** threshold (Gmail, Microsoft)              | Stricter authentication + unsubscribe + spam-rate requirements |
| 30-50 emails/mailbox/day                                       | Vendor folk norm, no provider basis; vendor ranges span 10-65 (~3x disagreement) | None from providers; a reputation-protection convention only   |

The 30-50 figure is not a provider limit and must never be presented as one. Treat it as a starting hypothesis to adjust against the sender's own postmaster data.
