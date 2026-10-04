# Asset Kit and Day-0 Provisioning

The pre-condition checklist: what must exist before the first touch sends. Vendor names appear only as sourced evidence, never as required tools.

## Day-0 provisioning checklist (both B2B and B2C)

Verify each item fires automatically at approval, or has a named owner with a same-day SLA:

- [ ] Portal/dashboard credentials issued.
- [ ] Tracking link generated (deep links + sub-ID/pass-through parameter conventions documented).
- [ ] Unique coupon/promo code issued, where the program uses codes.
- [ ] Asset library access granted (one persistent hub beats attachments).
- [ ] Terms acceptance + disclosure attestation captured (drafting the terms is the terms skill's job; capturing acceptance here is this skill's).
- [ ] Tax form and payout method collected, gating payout eligibility (below).
- [ ] Archetype + tier tag applied, so the routing fires the right sequence.

Speed matters: with auto-approval and auto-provisioning, an affiliate can be ready to promote in under an hour; manual provisioning is documented at 1-3 business days per affiliate - dead time inside the highest-intent window.

## Tracking readiness

If the activation event cannot be recorded, the sequence measures nothing:

- Server-side (postback) conversion tracking live, carrying a click ID and an order/transaction ID for deduplication. Cookie-only attribution undercounts: browser tracking prevention (per WebKit's published ITP documentation) caps JavaScript-set landing-page cookies at 24 hours under link decoration and clears script-writeable storage after 7 days without interaction.
- Trace the full path once, manually: click → recorded conversion → pending commission → refund/reversal state. If any hop is dark, reported activation understates reality and the KPI block is fiction.
- Coupon-code attribution tested where codes exist - a code redeemed without a click must still credit the affiliate.
- B2B: conversion events defined deep-funnel (trial, qualified opportunity, closed-won) and associated to the partner in the CRM; long multi-session cycles make cookie attribution least reliable exactly where deals are largest.

## Asset kit contents

**B2C ecommerce kit** - built for placement volume:

- Pre-coded tracking links and the unique coupon code.
- Banner set, product images, logo pack with usage rules.
- Swipe copy: 1-2 ready-cut emails, short social captions.
- Product one-sheet: positioning, top sellers, seasonal angles.
- Product feed access (loyalty/cashback and sub-network archetypes), with feed freshness and deep-link format documented.
- Disclosure requirement stated plainly next to the assets, not only in the terms.

**B2B SaaS kit** - built for depth per partner; one published program comparison (Rewardful) notes a standard kit of "logos, an approved tagline, three hero images, and a talking points document" is not enough for B2B, which needs:

- Everything above, plus:
- Sandbox, demo, or NFR (not-for-resale) account access - provisioned day 0, not on request.
- Use-case angles, competitor-comparison material, buyer-question material - fuel for long-form reviews and comparison posts.
- Sales deck and demo script for agency/consultant archetypes.
- Deal-registration link and its conflict rules.
- Pointer to the certification module when one exists (the curriculum itself belongs to the enablement skill).

## Sequencing asset creation

When interview question 5 reveals missing assets, don't delay launch for the full kit. Build in this order:

- efficiency: `link/code provisioning > attestation and tax collection > one leading asset per present archetype > banners, feeds, decks`
- effort: `banners, feeds, decks > leading asset per archetype > attestation and tax collection == link/code provisioning`
- compliance cost: `attestation and tax collection > everything else in the kit`

1. **Blocks touch 1** - working link/code provisioning, terms + disclosure attestation flow, tax/payout collection. Without these the sequence cannot start at all, which is why they lead on efficiency despite costing about a week each when the platform doesn't provide them (an hour when it auto-provisions). That identical shape - a week to wire by hand, an hour when the platform ships it - is what makes provisioning and attestation tie on effort; only the compliance axis separates them.
2. **Blocks touch 2** - the one leading asset per archetype actually present in the intake (swipe email, code page, caption pack, sandbox), a day or so each. Skip archetypes with zero approved affiliates - that is a deletion from the list, not a low-priority row.
3. **Everything else** - banners, feeds, decks, certification pointers, a week or more each and never finished - ships when ready, announced by a later touch or the asset hub. A late banner set costs little; a late link costs the whole window.

The compliance axis separates rung 1 from the rest of the kit, and it is why attestation and tax collection cannot be deferred into rung 2 even though a banner set costs more hours. The disclosure obligation and the tax-form requirement each need a sign-off you cannot apply retroactively: once a commission has been earned against an unattested placement or an uncollected tax form, the fix is a negotiation with the affiliate rather than a build task. Banners, swipe copy and decks carry no such exposure and stay fully reversible.

## Payout and tax gating

Collect payment and tax setup at onboarding, as a gate on payout eligibility - not after the first commission is earned:

- Tax form (per the affiliate's jurisdiction) and payout method captured inside the onboarding flow; payout threshold and hold period stated in touch 1.
- Chasing tax forms after paying is a documented recurring operational mistake in practitioner material; the reverse order costs nothing at onboarding and blocks nothing but payout.
- Precedent that unclaimed setups expire: one large program's published implementation voids commissions if the payment account isn't completed within 120 days of the first commission (ClickFunnels, via its payout provider) - tell affiliates the rule upfront rather than surprising them.
- Match commission state to risk: create commissions as pending, approve after the refund/clawback window closes. B2C risk ends with the return window; B2B recurring commissions carry reversal risk on every invoice, so holds run longer.
- Regulatory and tax specifics change - verify current forms and thresholds against the program's platform documentation and counsel; do not hardcode form names into the sequence copy.

## Compliance placement

Surface the disclosure obligation and restricted-terms policy (e.g. brand bidding) inside touch 1, alongside terms acceptance. No regulator or network prescribes a specific touch number or day for this, so the exact placement is a design choice, not an industry rule - but the FTC's 2023 Endorsement Guides update do require the brand running the affiliate program to train affiliates on disclosure requirements and provide compliant disclosure language before they publish any content, which puts a real compliance floor under placing it no later than touch 1, at approval.
