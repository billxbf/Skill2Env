# Reported specs - vendor snapshot, refreshed September 2026

Optional note. This is the only file in this skill that names vendors and products. Every line is tagged with its sourcing tier.

**Re-verify every figure against the vendor's own advertiser help before use.** This space moves weekly. The original August 2026 snapshot was refreshed 2026-09-11: Perplexity's paused intake turned into a full advertising shutdown, Amazon's free Rufus-prompt beta went paid (and Rufus itself was rebranded), Google delayed the AI Max/DSA automigration by five months, and OpenAI's ChatGPT ads roughly quadrupled their country coverage and crossed a $1B run rate. Treat every date and status below as provisional again in another few weeks.

Tiers:

- **vendor-documented**: the vendor's own help/announcement.
- **practitioner-reported**: a named practitioner or agency, first-hand.
- **press-reported**: trade press, second-hand.
- **single-vendor benchmark**: the vendor selling the result.
- **rumour**.

## Verbatim surfaces (advertiser-authored string renders as written)

- **OpenAI ChatGPT ads** (vendor-documented) - the only surface with published copy field specs. Launched 2026-02-09 for logged-in US Free/Go tiers; paid tiers (Plus/Pro/Enterprise) stay ad-free. Expanded fast: 40+ countries by August 2026, then a further rollout to 31 European countries plus India/MENA from 2026-08-31, reaching a $1B annualized revenue run rate the same week (under 200 days after launch). A 2026-09-04 update made product feeds mandatory for shopping results and added Custom Audiences (mixed identifier types, 5M+ members, incremental add/remove/replace) and an Ads Manager Plugin. Re-check country coverage and feed requirements before citing either as fixed.
  - Fields: Advertiser name, Favicon, Title, Copy, Landing page, Image. No separate CTA field.
  - Limits: Title 16-24 characters recommended, 50 max. Copy 32-48 recommended, 100 max. Image square, 1200x1200 max; no published image minimum, aspect-ratio string, or format list (third-party numbers conflict, not official).
  - Three authoring paths: advertiser-written `chat_card`; "Suggested ad drafts" prefill from site metadata (generates no new copy); `product_ad_template` filled from a Google-compatible feed at serve time (`is_ads_eligible` flag required).
  - Practical targets: ~16-char title, ~32-char copy (practitioner-reported, Pacvue via a July 2026 OpenAI/Kepler webinar).
  - Targeting via Context Hints: plain-language situation description, up to 280 characters (practitioner-reported, Demand Curve).
- **Snap AI Sponsored Snaps** (vendor-documented) - launched 2026-04-28 in the chat tab, gray "Ad" label. Replies come from the advertiser's own chatbot; the opening message carries a welcome card, suggested prompts, and a legal disclosure.
  - **My AI Sponsored Links** are contextual, powered by Microsoft's Ads for Chat. The brand receives only query, over/under-18 age range, country/language, OS, and IP.

## Model-generated surfaces (model synthesises from your assets)

- **Google Ads in AI Overviews** (vendor-documented) - existing Search/Shopping/PMax/App assets become eligible above, below, or within the overview; **no new copy fields exist**. Query and overview content both considered at serve time. No ads at all in sensitive verticals: adult, alcohol, gambling, finance, healthcare, politics.
- **Google AI Mode formats** (vendor-documented, in test):
  - Formats: Conversational Discovery ads, Highlighted Answers, AI-powered Shopping ads.
  - Powered by AI Max/Performance Max; copy model-generated from feeds and assets.
  - Practitioner read (Jyll Saskin Gales): "zero control over your ad creative, and zero reporting on what ads showed where."
  - AI Max exited beta on 2026-04-15 (adding an AI Brief setup field and guaranteed text disclaimers for regulated industries), but the automatic Dynamic Search Ads migration Google originally set for September 2026 was delayed to February 2027 (announced 2026-06-11, citing advertiser feedback and Q4-planning disruption); only campaigns using Automatically Created Assets and campaign-level broad match still auto-upgrade on the original September 2026 date. Google also reopened DSA campaign creation from mid-June 2026 through January 2027. Re-check the migration date before citing - it has already moved once.
- **Amazon Sponsored Products / Sponsored Brands Prompts** (formerly "Rufus" prompts; vendor-documented, now generally available) - launched in free open beta 2025-11-11, moved to paid general availability in the US 2026-03-25: clicks now bill under the campaign's standard CPC, ending the free-access window. Separately, the Rufus assistant itself was folded into a rebranded "Alexa for Shopping" experience on 2026-05-13.
  - **Auto-opts-in** advertisers running Sponsored Products auto/broad campaigns.
  - Copy auto-generated from product data, reviews, Brand posts, and campaign keywords.
  - Prompts are pre-determined; no self-serve targeting.
  - A separate, still-free placement type (ads inside AI-conversation replies, no bidding, no dedicated reporting line) continues to run alongside the now-paid prompts; industry analysts expect this to convert to paid with its own reporting line by late 2026 - re-check before citing "free."
  - Bundled into the "Other" placement line, so its ROAS cannot be isolated.
- **Perplexity Sponsored Related Questions** (vendor-documented, discontinued) - advertiser picked the sponsored questions and trigger keywords, got locked answers and term blocking, but never wrote the answer: "not written or edited by the brands sponsoring the questions." CPM-priced while it ran. Advertiser intake paused October 2025; **Perplexity abandoned advertising entirely in February 2026** and moved to a subscription/enterprise-only model - there is no self-serve platform, waitlist, or active ad product as of this check (2026-09-11). An executive left the door open to a future return but named no date; treat this surface as discontinued, not paused, until Perplexity relaunches something.
- **Microsoft Copilot Showroom Ads / Dynamic Filters** (vendor-documented pilots) - **copy field limits are unpublished**; confirm them in-product before drafting to a length rather than guessing at a spec. Microsoft's own claim (press-reported): Copilot search ads "perform 25% better than traditional search ads" on relevance/conversational metrics.
- **AI-native networks** (Koah, Kontext, Nexad) - generate copy from live session context. All CTR/CPA claims (2% average CTR, 122% lift; 3-5% CTR, 2-4x CPA) are single-vendor benchmarks, unverified.

## Economics and measurement figures in circulation

- Bid guidance (practitioner-reported, Demand Curve):
  - $3-5 CPC, with $3 "routinely fail[ing] to clear delivery thresholds."
  - CPMs $25-60.
  - 30-day test floor $1,500-3,000.
- "Roughly 60% of conversions from ChatGPT ads happen outside the immediate click window" → extend attribution to 7-14 days minimum (practitioner-reported, Demand Curve).
- Dark traffic: 70.6% of AI-adjacent visits arriving as "Direct" is a single-vendor figure; Conductor's 3.3B-session benchmark puts AI referral traffic at 1.08% of visits. Cite the pair, never one alone.
- Referral conversion figures (7.1%; 15.9% vs 10.5% vs 1.76%) come from different studies on different populations - quote the spread with sources.

## Treat as rumour or projection

- Any Meta in-answer ad product (rumour). Brave Leo, You.com, Arc advertiser docs (undocumented).
- Every circulating OpenAI ad-revenue figure (press-reported, unaudited). Amazon's ">$10B annual incremental sales" for Rufus (forward-looking projection, not revenue).

## Regulatory position (documented, stable)

No regulator has written an AI-answer-ad-specific rule; existing regimes bind unchanged.

- **US FTC**: "clear and conspicuous" native-ad disclosure ("Ad"/"Sponsored" acceptable; "Partner Content"/"Promoted" disfavoured).
- **UK ASA/CAP**: the Code is media-neutral - "AI does not create new categories of advertising." The CMA can fine up to 10% of global turnover under the DMCCA.
- **EU**: DSA Art. 26 requires real-time per-ad transparency; AI Act Art. 50 transparency has applied since 2 August 2026.

"The AI did it" is not a defence: the advertiser stays accountable for model-generated distortion, and no vendor label discharges these duties.
