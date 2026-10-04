# Worked examples

Four samples: a B2C verbatim-slot package, a B2B verbatim-slot package, a model-generated source rewrite, and an annotated negative example. Product names, evidence, and numbers in the first three are fictional samples showing the shape - never reuse their claims. The negative example's before/after pair is real (Demand Curve, growth newsletters #333-334, 2026).

**Situation description, weak vs strong** (Persona + Intent + Scope, see the main skill's verbatim workflow):

- Weak: "CRM sales software best tools comparison."
- Strong: "A founder evaluating CRM options for a small remote sales team struggling with pipeline visibility."

## 1. B2C verbatim-slot package (in-assistant sponsored card)

Fictional product: Loftly, a meal-planning app. Assumed pasted limits: title 50 chars max (~16-24 recommended), copy 100 max (~32-48 recommended), no CTA field, situation description up to 280 chars.

- **Placement + control axis**: in-assistant sponsored card, verbatim, advertiser-written path, owned by paid media.
- **Situation description** (Persona + Intent + Scope): "A busy parent deciding how to stop wasting weeknight time and food money, asking for realistic meal-planning help for a family that hates repeats." (147 chars)
  - Alternate for delivery diagnosis: "A parent comparing meal-planning apps after abandoning one that suggested recipes their kids refused." (101 chars)
- **Slot copy**:
  - Title: "Dinner solved by 4pm" (20 chars)
  - Copy: "Loftly plans the week from meals your kids already eat." (55 chars)
  - Ask folded in: none needed beyond the landing page - early-thread slot, soft ask implied.
- **Grounding table**:
  - "meals your kids already eat" → app builds plans from logged accepted meals (product doc, supplied).
  - "by 4pm" → framing of the daily plan notification, not a measured outcome; kept as feature framing, no stat claimed.
- **Compliance note**: platform label expected; not a regulated category; no legal review required.
- **Quotability gate**: 10/10 - self-contained, product named, one idea, claim first, specific situation, sourced, no time-bound claim, recommendation register, no superlative, inside limits.
- **Measurement plan**: no account baseline yet - first 30 days set it; attribution window 14 days; read delivery across the two situation descriptions before judging the copy line.

Why it passes: it names the reader's live situation (weeknight scramble, picky kids), reads like a colleague's tip, and survives being lifted out of the thread.

## 2. B2B verbatim-slot package

Fictional product: Ledgerline, an accounts-payable automation tool. The reader is an operations lead building a case for a CFO.

- **Situation description**: "An operations lead at a 50-200 person company evaluating AP automation because month-end close keeps slipping past day five." (124 chars)
- **Slot copy**:
  - Title: "Close in 3 days, not 8" (22 chars)
  - Copy: "Ledgerline cut close time 60% for 40 mid-size finance teams." (60 chars)
- **Grounding table**:
  - "60% / 40 teams" → 2026 customer cohort study, supplied by user.
  - "3 days, not 8" → median before/after from the same study.
  - Both dated; review date set for the study's anniversary.
- **Why the B2B shape differs**: the line hands the reader a quantified outcome they can repeat in a meeting. A B2C-style feel-good line ("AP without the pain") gives the internal case nothing to carry.
- **Quotability gate**: 10/10. Note check 9 especially: "cut close time 60% for 40 teams" is narrow and sourced - an assistant's own answer can sit beside it without contradicting it. "The fastest close in the industry" would fail.
- **Measurement plan**: conversion volume too low for copy-level significance - read delivery, click-through, and demo-request quality quarterly against the account's own trailing numbers.

## 3. Model-generated source rewrite (answer-engine / AI search placement)

The placement synthesises the ad text from the landing page and product feed; there is no string to write. The deliverable is the rewritten source passage.

**Before** (landing-page passage the model currently lifts):

> "Our revolutionary next-generation platform leverages cutting-edge AI to transform the way modern teams work. Trusted by industry leaders everywhere, it delivers unparalleled value across every workflow."

Problems:

- No product name.
- No claim a model can extract.
- Unsupported superlatives.
- Zero specifics.

The model either skips a passage like this or paraphrases a competitor's clearer page instead.

**After**:

> "Ledgerline automates invoice approval for mid-size finance teams. Teams using it close their books in a median 3 days instead of 8, based on a 2026 study of 40 customers. It connects to the ledger systems mid-size companies already run."

Why it works:

- Product named in sentence one.
- Claim first.
- One idea per sentence.
- A sourced, dated number.
- Each sentence quotable alone, at roughly 15-25 words.

Feed fields get the same pass: exact current price in the price field, natural problem-solving language in the description. On this path, the feed is the copy.

Order used:

- Landing-page passage first: the writer owns it, and it ships the same day.
- Feed fields second, once the feed owner is booked.
- Structured data: filed to the dev queue as a follow-up ticket.
- The review programme: named as a standing job outside this package's effort ceiling, listed rather than silently dropped.

## 4. Negative example, annotated (real pair - Demand Curve)

- **Search-style, fails in a conversation**: "Best CRM for Startups. Try Free."
- **Conversational, works**: "Still updating pipeline manually?"

What the failing line gets wrong inside a response slot:

1. **Register**: it interrupts. The reader is mid-deliberation with an assistant; a category-winner announcement reads as a banner that wandered into the thread.
2. **Unsupported superlative**: "Best" is exactly the claim the model's own answer beside it may qualify or contradict in the same turn (quotability check 9).
3. **No situation**: it addresses nobody. The working line names the reader's live problem and lets them self-select.
4. **Two moves in one slot**: a claim plus a CTA shout, neither developed - against the one-idea rule.
5. **Context dependence**: on a search results page, surrounding chrome (ratings, sitelinks, competitors) props it up. Alone in a slot, it carries nothing.

The fix is never a trim of the failing line - it is a rewrite from the situation up. Quotability gate result for the failing line: fails checks 1, 2 (pronoun-free but product-free), 3, 5, 8, and 9.
