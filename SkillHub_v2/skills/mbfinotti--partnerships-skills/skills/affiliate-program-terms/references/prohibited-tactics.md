# Prohibited Tactics & Enforcement Ladder

The operating principle, from practitioner Geno Prussakov (AM Navigator; author of _Affiliate Program Management: An Hour a Day_): "any practices that you do not explicitly prohibit are, implicitly, permitted" (https://www.amnavigator.com/blog/2019/03/27/affiliate-program-agreement-terms-conditions/). Enumerate every ban; a catch-all like "no unethical marketing" prohibits nothing.

This section is the most litigated and most operationally enforced part of the agreement - cookie stuffing has been prosecuted as federal wire fraud, and major networks terminated a top browser extension in 2026 for attribution manipulation. Drafting it precisely is what makes enforcement possible; detecting violations is a separate operational job (see the fraud-detection skill in SKILL.md's Reference).

## The ban list

The list is not a menu. Under the enumerate-or-permit principle, every tactic left off is permitted - draft all of them, minus only the ones physically impossible for the program (no marketplace clause where nothing is sold on marketplaces). Three entries are program positions rather than bans: brand-keyword bidding, coupon/deal sites, and browser extensions. Those three are ranked in SKILL.md's Interview, where the user picks them; this file drafts whichever was picked.

- **Trademark / brand-keyword bidding.** Four standard policy positions cover most programs, in the Interview's ranked order: strict prohibition, trademark-only prohibition with modifier allowance, tiered allowance by partner, keyword whitelist.

  Whichever position is chosen, the ban itself covers:
  - Exact-match marks, misspellings, permutations, trademark-plus-modifier and trademark-plus-coupon terms.
  - The brand as a required negative keyword.
  - Trademark use in ad copy and direct-linking of paid-search traffic.

  Established wording pattern: "strictly prohibited from bidding on [Brand] trademarked terms using Broad, Phrase, or Exact match types... all possible permutations, combinations, misspellings, and character substitutions." For TM+ terms, a published industry approach is to state publicly that TM+ bidding is not allowed, then whitelist one or two trusted affiliates.

  Contested: the ban is contractual only - search engines will not enforce it, and keyword bidding is generally lawful; only trademark use in ad copy is independently actionable. `[LEGAL REVIEW]`

- **Typosquatting.** Registering misspelled brand domains to capture type-in traffic - both trademark infringement/cybersquatting and a cookie-stuffing vector.
- **Cookie stuffing and forced clicks.** Setting tracking cookies without a genuine click (0x0 iframes, popunders, redirects). Criminal exposure exists: US DOJ prosecuted cookie-stuffing schemes as wire-fraud conspiracies.
- **Adware and browser-extension injection.** Software injecting affiliate cookies during normal browsing.
- **Extension "stand-down" violations.** Require any permitted browser extension to stand down - not fire - when another affiliate is earlier in the clickstream. The Performance Marketing Association's proposed Toolbar and Software Industry Standard requires disclosure, a related user action, and a direct transparent user benefit before an extension may attach an affiliate link, code, or cookie.
- **Unauthorized discount codes.** Publishing codes not issued to that affiliate, or expired/internal codes.
- **Spam and unsolicited email.** Some programs also ban affiliate links in email entirely, and in offline/printed material.
- **Misleading claims and fake reviews.** Fabricated results, fake or AI-generated reviews, undisclosed insider reviews - in the US these now carry direct civil-penalty exposure under the FTC Reviews Rule (16 CFR Part 465, effective October 2024), which unlike the Endorsement Guides is penalty-bearing without any prior Notice of Penalty Offenses.
- **Brand impersonation.** No presenting as "[Brand] Official", "[Brand] Support", or "[Brand] Sales" in handles, ads, or domains.
- **Self-referral and incentivized traffic.** Bar commissions on the affiliate's own purchases and, commonly, friends/family; bar undisclosed incentives that manufacture referrals; bar claiming commission twice on the same traffic through multiple programs.
- **Unauthorized marketplace listings.** Ecommerce programs: no listing the merchant's products on third-party marketplaces.
- **AI-generated spam content.** A newer clause - mass low-quality AI content around affiliate links; industry guides now carry dedicated AI-usage and content-integrity sections.

## Drafting the three program positions

The Interview settles which position; these are the words each one needs.

- **Brand bidding.** Wording depends on the position chosen:
  - Strict prohibition: one clause covering permutations, misspellings and character substitutions, plus a negative-keyword obligation and a ban on the mark in ad copy.
  - Modifier allowance: enumerate the permitted modifier set as explicitly as the banned one, or the allowance swallows the ban.
  - Tiering or whitelist: name the tiers or the cleared keyword list in an incorporated policy document rather than in the master terms, so a promotion or removal does not run the amendment cycle - and state the grounds for refusing a partner, which P2B requires and which inconsistent enforcement otherwise destroys.
- **Coupon/deal sites.** The restricted position - the one leading the Interview's ordering - needs four sentences:
  - Only codes issued to that affiliate may be published.
  - Expired and internal codes void the commission.
  - Trademark-plus-coupon terms fall under the brand-bidding clause.
  - Last-click on a code-page visit earns or does not earn (say which).

  A full ban is one sentence; permitting fully is silence, which is the same thing under the enumerate-or-permit principle.

- **Browser extensions.** A ban is one sentence naming injection, cookie-dropping and click-forcing software. Permission needs the stand-down obligation above, plus a stated evidentiary basis - whose clickstream data settles a stand-down dispute - and the disclosure and genuine-user-benefit conditions as warranties the affiliate makes on each release.

## The enforcement ladder

The rungs below are a sequence, not a menu, and are deliberately left unranked: you do not pick two of five, and the escalation order is what makes for-cause termination and recovery defensible afterwards. Ranking them by payoff per unit of effort would sit against that sequence and buy nothing.

Draft a graduated, explicit ladder so every response short of termination has contractual footing:

1. Written warning with cure period.
2. Voiding of commissions generated through the violating tactic.
3. Account suspension pending investigation.
4. Termination for cause (immediate, no notice-period benefit).
5. Recovery of already-paid commissions attributable to the violation, plus reserved damages rights.

- Deem any prohibited-tactics violation a material breach - this is what unlocks for-cause termination and recovery.
- State which rungs may be skipped for severe violations (fraud, cookie stuffing) - jumping straight to termination must be contractually reserved, not improvised.
- Deleted rung, not a demoted one: permanent commission-rate cuts. A contested practitioner point makes the case - a rate cut neither stops nor removes the violator, so it buys the appearance of a response and leaves the tactic running. Do not carry it at the bottom of the ladder where it reappears as the easy option.
- Pair the ladder with the automatic brand-licence revocation and pending-commission clauses so enforcement has a clean exit path; workflow step 6 drafts both immediately after this section.
