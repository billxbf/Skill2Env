# Sales source snapshot

**Snapshot date: 2026-08-26**, with a 2026-09-08 pass adding exact URLs to existing entries and correcting three renames (INBOUND to UNBOUND, "GTM Summit" to GTM2026, the Sales Confidence domain), and a 2026-09-11 spot-check re-confirming the two highest-visibility conference entries (GTM2026: Sept 28-Oct 1 2026, NYC, live registration; UNBOUND: Sept 16-18 2026, Boston, sold out) still current. Scope: the information ecosystem of the sales profession, both B2B SaaS and B2C high-ticket. People are in [references/people-to-follow.md](./people-to-follow.md), books in [references/books.md](./books.md), and YouTube channels in [references/video-channels.md](./video-channels.md) - each split out of this file to keep it scannable.

Sections run in the attention-efficiency order set in SKILL.md - cheapest-per-outcome medium first, most expensive last. Section order and the stated ranking never disagree. Each medium opens with what an entry costs in attention and what it buys, plus the rows that deviate from their medium's price.

## Table of Contents

- [Status vocabulary](#status-vocabulary)
- [B2B SaaS ecosystem](#b2b-saas-ecosystem)
- [Sources that serve both B2B and B2C](#sources-that-serve-both-b2b-and-b2c)
- [B2C high-ticket ecosystem](#b2c-high-ticket-ecosystem)
- [Graveyard - dead, renamed, merged, migrated, or ruled out](#graveyard-dead-renamed-merged-migrated-or-ruled-out)
- [Signal vs noise](#signal-vs-noise)

## Status vocabulary

- `verified-active` - direct, dated evidence of recent activity at the snapshot date (noted per row).
- `unverified` - no direct evidence either way: blocked fetch, undated page, or reported active without dated proof. **Not** a death verdict.
- `likely-dead` - fetched and found nothing newer than ~12 months, or the domain 404s, parks, or fails DNS.

Structural caveat: YouTube (consent wall), Reddit (hard block), and LinkedIn/X (bot redirects) are unverifiable by plain fetch. An `unverified` on those mediums reflects tooling, not source health - treat a failed fetch there as unknown, never as dead.

Audience numbers appear only where publicly stated, with origin labeled. "not stated" means no published figure exists; never substitute an estimate.

Anything ruled out - dead, migrated, or unrecommendable without re-verification - lives in the Graveyard at the bottom and appears in no table above it. A ruled-out source parked at the foot of a live menu gets recommended anyway.

---

## B2B SaaS ecosystem

### Newsletters and written sources (B2B)

- **Costs:** minutes per issue, with a hard end.
- **Buys:** a phrase or a play liftable into tomorrow's email.
- **Deviations:** Winning by Design and the vendor blogs publish rolling long-form, closer to a podcast episode per piece. 30MPC and Leslie Venetz are the shortest reads here and the best fit for a sub-30-minute ceiling.

| Source                      | URL                       | Cadence    | Audience (stated)                                                                 | Best for                                                        | Status / evidence                                                                               |
| --------------------------- | ------------------------- | ---------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| The GTM Newsletter (GTMnow) | gtmnow.com                | Weekly     | "over 100,000 GTM professionals" (2023 announcement); site claims 60,000+ network | Full go-to-market view for VP/CRO/founder                       | `verified-active` - posts dated Aug 25, 14, 11 2026. **saleshacker.com now 301-redirects here** |
| Leslie Venetz               | leslievenetz.substack.com | ~2-3x/week | not stated                                                                        | Outbound and discovery messaging craft, B2B                     | `verified-active` - seven posts Aug 10-24 2026                                                  |
| 30MPC newsletter            | 30mpc.com                 | Weekly     | 60k+ subs (self-claimed)                                                          | Tactical plays in text form                                     | `verified-active` - site live                                                                   |
| Sales Gravy newsletter      | salesgravy.com            | Weekly     | 470,000 subs (self-claimed)                                                       | Prospecting fundamentals; **B2B and B2C both**                  | `verified-active` - fresh "Ask Jeb" blog series visible                                         |
| Winning by Design           | winningbydesign.com       | Rolling    | not stated                                                                        | RevOps/GTM leaders; SaaS revenue architecture                   | `verified-active` - webinar Aug 27 2026, Impact Summit Sep 2 2026                               |
| Outreach blog               | outreach.ai               | Rolling    | not stated                                                                        | Vendor content marketing on outbound; solid but self-interested | `verified-active` - posts through Aug 25 2026. **outreach.io redirected to outreach.ai**        |
| Salesloft blog              | salesloft.com             | Rolling    | not stated                                                                        | Vendor content marketing on sales engagement                    | `unverified` - dates JS-rendered, not fetchable                                                 |

### Benchmark and data sources (B2B)

- **Costs:** minutes, once a quarter or a year, which amortizes to near-zero weekly.
- **Buys:** a defensible number for a quota, comp, or board conversation.
- **Deviations:** RepVue's continuous index is a two-minute lookup and the cheapest row here. The full Bridge Group and Ebsta reports run closer to an hour if read properly rather than skimmed for the headline.

| Source                           | Publisher                            | Cadence                | Methodology / sample                                                                                     | Status / evidence                                                                                                                                                                                                                                                                |
| -------------------------------- | ------------------------------------ | ---------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SDR Metrics & Compensation       | The Bridge Group                     | Biennial               | 351 B2B companies (2025, 10th ed. since 2007)                                                            | `verified-active` - 2025 edition published                                                                                                                                                                                                                                       |
| AE Metrics & Compensation        | The Bridge Group                     | Periodic               | 170+ SaaS companies (2024 ed.)                                                                           | `verified-active` - 2026 AE report published                                                                                                                                                                                                                                     |
| Cloud Sales Index / Salary Guide | RepVue                               | Quarterly / continuous | Crowdsourced rep-reported; Q4 2025: 43.83% quota attainment from 272 companies, ~57k ratings             | `verified-active` - mid-2026 update                                                                                                                                                                                                                                              |
| GTM Benchmarks                   | Fullcast (formerly Ebsta + Pavilion) | Annual                 | 2025 ed. (as Ebsta x Pavilion): 655K opportunities, 2,000+ CROs. 2026 ed.: 316 companies, $75B+ pipeline | `verified-active`, brand changed - confirmed via search: Ebsta's founder Guy Rubin moved to Fullcast, and the 2026 edition ships as "Fullcast's 2026 State of GTM Benchmarks report," no longer under the Ebsta x Pavilion name. Update any citation expecting the old branding. |
| State of Sales                   | Salesforce                           | ~Annual                | 4,050 professionals, 22 countries (7th ed., data Aug-Sep 2025)                                           | `verified-active`                                                                                                                                                                                                                                                                |
| SaaS Benchmarks Report           | High Alpha (formerly OpenView)       | Annual                 | 800+ SaaS companies (2024 ed.)                                                                           | `verified-active` - continues after ownership transfer                                                                                                                                                                                                                           |
| State of Revenue AI              | Gong Labs                            | Annual                 | 7.1M opportunities, 3,613 companies (Dec 2025)                                                           | `verified-active`                                                                                                                                                                                                                                                                |

Methodology grading:

- **Bridge Group:** transparent, consistent, no conflicting product. A credible anchor.
- **RepVue:** largest rep-reported sample, self-selection bias applies. A credible anchor.
- **Ebsta x Pavilion, Gong Labs:** methodologically real but double as lead magnets. Read the data, discount the framing.
- **Salesforce:** a survey of opinion, directional only.

Never anchor on one source: they diverge by more than 15% on key metrics, so triangulate at least three before setting quota or comp.

Market-wide signal: quota attainment collapsed to ~43% and win rates to ~19% in 2025, from 55-65% and ~29% earlier in the decade.

Bridge Group caution:

- The research firm is **bridgegroupinc.com**.
- bridgegroup.com is an unrelated wealth-management company.

### Podcasts and shows (B2B)

- **Costs:** tens of minutes per episode.
- **Buys:** a full framework with the reasoning left intact, the thing a newsletter compresses out.
- **Deviations:** The Advanced Selling Podcast is short-format and the cheapest row here. Sell Better's near-daily live shows are the most expensive, at most of an hour on someone else's clock. 30MPC publishes multiple episodes a week, so a user on a 30-minute ceiling takes one episode, never the feed.

This whole medium is close to free for a user with a commute or a gym habit. Promote it accordingly.

| Source                                 | Who runs it                                  | Cadence                | Audience (stated)                                    | Best for                                                                        | Status / evidence                                                                                        |
| -------------------------------------- | -------------------------------------------- | ---------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 30 Minutes to President's Club (30MPC) | Nick Cegelski, Armand Farrokh                | Multiple episodes/week | 3.6M+ downloads, 60k+ newsletter subs (self-claimed) | Tactical cold-call and discovery scripts; AE, SDR, frontline manager            | `verified-active` - ep #593 dated Jul 28 2026; site live                                                 |
| Sell Better / The Daily Sales Show     | Will Aitken et al.                           | Near-daily live shows  | not stated                                           | SDR/AE tactical skill-building, free and live                                   | `verified-active` - show schedule visible through Sep 8 2026                                             |
| The GTM Podcast                        | Scott Barker / GTMfund                       | Weekly                 | tied to GTM newsletter base                          | VP/CRO, founder-led GTM                                                         | `verified-active` - GTMnow publishing Aug 2026                                                           |
| Make It Happen Mondays                 | John Barrows (JB Sales)                      | Weekly                 | ~10,000 weekly listeners (vendor listicle claim)     | AE fundamentals, SDR-to-AE transition; r/sales calls Barrows unusually non-guru | `verified-active` (org only) - JB Sales site live; no episode dates rendered, check the podcast feed     |
| Sales Gravy podcast                    | Jeb Blount                                   | ~2x/month              | 509 episodes total, active 2007-2026                 | Prospecting and fundamentals; **serves B2B and B2C both**                       | `verified-active` - confirmed via search, dated February 2026 episodes with named guests                 |
| Outbound Squad                         | Jason Bay                                    | Weekly (Tue)           | 360+ episode archive                                 | SDR and outbound AE frameworks                                                  | `verified-active` - site live; now sales-led rather than content-led                                     |
| Revenue Builders                       | Force Management (John McMahon, John Kaplan) | 2x/week (reported)     | 4.9/5 from 251 Apple reviews                         | Enterprise sales leaders, VP/CRO                                                | `verified-active` - confirmed via search, dated 2026 episodes with named guests (Cursor, Wiz, Snowflake) |
| The Sales Leadership Podcast           | Rob Jeppsen                                  | Weekly                 | 4.8/5 from 150 Apple reviews                         | Sales managers, CROs                                                            | `verified-active` - confirmed via search, dated 2026 episodes with named guests                          |
| Topline                                | Pavilion (Sam Jacobs et al.)                 | Weekly                 | not stated                                           | CRO, founder                                                                    | `verified-active` - listed on Pavilion's live site                                                       |
| The Advanced Selling Podcast           | Bill Caskey, Bryan Neale                     | ~3x/week               | 700+ episodes since 2006                             | Short-format fundamentals for micro-learners                                    | `verified-active` - confirmed via search, dated February 2026 episode with a named guest                 |
| Revenue Leadership Podcast             | Kyle Norton / Pavilion                       | Weekly                 | not stated                                           | VP Sales, CRO                                                                   | `verified-active` - listed on Pavilion's live site                                                       |
| Win Rate (Andy Paul)                   | Andy Paul                                    | unknown                | not stated                                           | Sales leaders                                                                   | `unverified` - andypaul.com SSL failure                                                                  |
| The Brutal Truth About Sales           | Brian Burns                                  | unknown                | not stated                                           | Enterprise AEs                                                                  | `unverified` - no reliable URL reached                                                                   |

Practitioner signal, credible tier (working reps recommend these unprompted on r/sales): 30MPC, John Barrows, Sales Gravy (fundamentals), Revenue Builders (leadership).

Most "best sales podcast" listicles are vendor SEO ranking the same 8-12 shows, usable for discovery, never as independent editorial.

### People to follow (B2B)

- **Costs:** minutes, but unbounded. A feed has no end, so it expands to fill whatever budget is left.
- **Buys:** a running read on how the market's language is shifting.

Cap it explicitly, at two or three names and a ten-minute skim, or it eats the budget the rest of this list needs.

LinkedIn is decisively the primary B2B platform, and X is secondary and declining. Full roster with confirmed LinkedIn URLs, grouped by specialty: [references/people-to-follow.md](./people-to-follow.md).

### Communities (B2B)

- **Costs:** tens of minutes a week, recurring, with no end state.
- **Buys:** an answer no publisher has written up, and the peers who answer the next one.
- **Deviations:** r/sales is skimmable on demand and the cheapest entry here. Pavilion's 707 events a year is a standing job rather than a subscription, and costs nothing extra to someone whose membership is already paid.

| Community              | Type / cost                                       | Audience (stated)                                                                                                                                                                                                                                                                                                                                                                | Best for                                                                                     | Status / evidence                                                                                              |
| ---------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Pavilion               | Paid membership, Slack, 707 in-person events/year | Use "5,000+ executives" - Pavilion's own live site as of the 2026-08-26 snapshot. Do not quote the "10,000+ paying members, 70+ countries" figure: it is 2021-era material still circulating on Pavilion's own properties, and the vendor's current and past claims contradict each other. Cite neither as a settled size; both are self-reported and no third party audits them | VP/CRO, RevOps leaders; the only B2B community here charging real money, and the most senior | `verified-active` - live site, Sep 2025 press, active podcasts                                                 |
| RevGenius              | Free Slack + platform                             | Self-claims 60k Slack / 100k members; third-party tracker lists ~17k - treat counts skeptically                                                                                                                                                                                                                                                                                  | SDR-to-CRO networking, sponsor-funded                                                        | `verified-active` - events dated Aug 27, Sep 15, Sep 17 2026                                                   |
| Bravado / The War Room | Free web community                                | 400k+ globally (self-claim)                                                                                                                                                                                                                                                                                                                                                      | Rank-and-file SDR/AE talk, comp threads                                                      | `unverified` - HTTP 429 rate-limited                                                                           |
| RevOps Co-op           | Free Slack                                        | 19,000+ members (2026, per CRO Club's ranking; figures across the community's own pages range 4,000-19,000+ depending on last update)                                                                                                                                                                                                                                            | RevOps practitioners. **Not** RevOps, Inc. (revops.io), a software firm absorbed by Maxio    | `verified-active` - confirmed via search, active with growing membership through 2026                          |
| Wizards of Ops         | Free Slack                                        | 4,000+ members (2026, up from ~2,500 in earlier snapshots)                                                                                                                                                                                                                                                                                                                       | RevOps/SalesOps                                                                              | `verified-active` - confirmed via search, listed in a roundup dated within the last two weeks as of the search |
| r/sales                | Free subreddit                                    | not stated                                                                                                                                                                                                                                                                                                                                                                       | Unfiltered practitioner consensus; skews AE/SDR; where guru claims go to die                 | `unverified` - Reddit blocks plain fetch (structural); practitioner signal strongly indicates active           |

### Conferences (B2B)

- **Costs:** days, plus travel.
- **Buys:** relationships and off-record numbers that exist in no published form.

Budget this as an annual block of days, never against a weekly minutes ceiling. Scored per week it always loses, which is exactly the starvation SKILL.md warns about.

**GTM2026** (attendgtm.com) - Pavilion's flagship, formerly branded "GTM Summit". Sept 28-Oct 1 2026, NYC, invite-only. `verified-active`. **SaaStr AI Annual** (saastrannual.com) - May 11-12 2027, San Mateo. `verified-active`. **UNBOUND** (unbound.hubspot.com) - HubSpot's rebrand of INBOUND; confirmed via 301 redirect from inbound.com. Sept 16-18 2026, Boston (sold out). `verified-active`. **Sales 3.0 Conference** (sales30conf.com) - Selling Power-run series; virtual AI Sales Summit Sept 2-4 2026, virtual Sales Training and Enablement Summit Dec 2-4 2026, plus historical in-person editions. `verified-active`. Each pairs a real practitioner draw with heavy vendor sponsorship.

### UK and Europe

Europe overwhelmingly consumes the US sources above. Genuinely distinct:

- **Sales Confidence** (salesconfidence.com - not `.co.uk`): UK SaaS sales community, James Ski. Confirmed via its own X account and a published contact address. `verified-active`.
- **Institute of Sales Professionals:** UK professional body, Ofqual-accredited qualifications, 100+ free member webinars/year. `unverified`.
- **SaaStock** (saastock.com): Dublin-anchored European SaaS conference, also running a US edition (SaaStock USA, April 15-16 2026, Austin). `verified-active`.

No European benchmark report matches the US ones' standing.

---

## Sources that serve both B2B and B2C

- **Sales Gravy / Jeb Blount** - prospecting fundamentals apply to both; see B2B tables for status.
- **Chris Voss / Black Swan Group** (blackswanltd.com) - negotiation, explicitly cross-applicable. `verified-active` - blog and podcast items visible, undated; irregular cadence.
- **Jeremy Miner / 7th Level** (7thlevelhq.com) - NEPQ methodology; self-styled "largest B2C sales training company in the world and 5th largest in B2B", the clearest single bridge between the ecosystems. Paid-course business model, but reads as a training operation rather than pure hype. `verified-active` (org site).
- **Grant Cardone / 10X** - cross-vertical motivational brand both worlds know; most serious B2B practitioners treat it as motivation, not tactics. Primarily course-selling and info-marketing layered on a real-estate business - not a neutral practitioner resource. `verified-active` - 10X Sales Manager Workshop Sep 10-11 2026; 10X Growth Con Apr 2-4 2026.

---

## B2C high-ticket ecosystem

A genuinely separate world: single-call closes, in-home/retail settings, commission-only comp. It runs on:

- YouTube (top-of-funnel).
- Facebook Groups (community).
- Paid coaching/conferences (monetization).

Almost nothing on Slack or Substack, and barely any benchmark reporting.

Many of its best-known names are primarily course-sellers and info-marketers rather than neutral practitioner resources. That is stated per row below, neutrally, because it affects whether the source is worth the user's time. Reddit (r/realtors, r/insurance, r/solar) is the skeptical counter-channel where practitioners critique the coaching-guru economy.

The efficiency order shifts here, for a supply reason rather than a value one. Trade-association data is the cheapest high-value entry, while the figures below trade almost entirely in video and events, so this ecosystem's ranking starts one rung lower than B2B's.

### Benchmark and data sources (B2C)

- **Costs:** minutes, once a quarter or a year.
- **Buys:** market-level ground truth that the creator economy around it does not publish.

No rep-level performance benchmarking (quota, ramp, win rate) exists as a published product in B2C - that absence is itself a finding. The credible data is trade-association market data, far more rigorous than anything the creator economy publishes:

| Source                                 | Vertical    | Cadence                  | Status / evidence                                                                                           |
| -------------------------------------- | ----------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| LIMRA                                  | Insurance   | Quarterly                | `verified-active` - FY2025 annuity data published (record $464.1B); covers ~89-92% of the US annuity market |
| NAR Profile of Home Buyers and Sellers | Real estate | Annual (44th year)       | `verified-active` - Nov 2025 edition; first-time buyers at record-low 21%                                   |
| NAR Member Profile                     | Real estate | Annual                   | `verified-active` - Aug 2025 edition (paid)                                                                 |
| Cox Automotive Car Buyer Journey       | Automotive  | Annual + quarterly index | `verified-active` - Jan 13 2026 edition                                                                     |

### Figures and brands (B2C)

- **Costs:** tens of minutes per video and days per event. This ecosystem's primary mediums are the two most expensive ones.
- **Buys:** vertical-specific tactics and, at the events, the peer network that carries most of a B2C rep's actual deal flow.
- **Deviations:** the podcasts (The D2D Podcast, Stay Paid) price like any podcast. The flagship conferences price like conferences and belong in an annual block.

| Figure / brand                     | Vertical                                       | Primary platform                           | Character                                                                                                                               | Status / evidence                                                                                                                                                                                                                                                                     |
| ---------------------------------- | ---------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sam Taggart / D2D Experts          | Door-to-door (solar, roofing, pest, alarms)    | YouTube, The D2D Podcast, paid training    | Training business with a real flagship event                                                                                            | `verified-active` - D2DCon (9th year) Jan 23-24 2026, Utah; "2,800 D2D professionals trained annually" (self-claim)                                                                                                                                                                   |
| Cody Askins / 8% Nation            | Insurance                                      | YouTube, Facebook, conference              | Conference-and-leads business; "500k+ agents reached" is a self-claim                                                                   | `verified-active` - 8% Nation conference Jul 7-10 2026, Dallas                                                                                                                                                                                                                        |
| Jeremy Miner / 7th Level           | Cross-vertical (NEPQ)                          | YouTube, "Sales Revolution" Facebook group | See dual-ecosystem section above                                                                                                        | `verified-active` (org site)                                                                                                                                                                                                                                                          |
| Adam Bensman / The Roof Strategist | Roofing, solar                                 | YouTube, podcast, paid RSRA community      | Practitioner-teacher with a paid community layer                                                                                        | `verified-active`, but rebranding mid-transition - confirmed active with dated 2026 episodes (Feb, May), but content from May 2026 onward appears to be shifting to "The STRONG Roofer" under TAMKO Building Products. Confirm the current name before recommending it going forward. |
| Tom Ferry                          | Real estate                                    | Coaching, conference, YouTube              | "Real estate's #1 coach" is a self-claim; large genuine event                                                                           | `verified-active` - Success Summit (23rd year) 2026, Anaheim                                                                                                                                                                                                                          |
| Ryan Serhant / SERHANT.            | Real estate (luxury)                           | YouTube, media, brokerage                  | The most practitioner-first B2C name checked - an operating brokerage with education as a secondary layer                               | `verified-active`                                                                                                                                                                                                                                                                     |
| Grant Cardone / 10X                | Cross-vertical, real estate                    | YouTube, conferences                       | See dual-ecosystem section above                                                                                                        | `verified-active`                                                                                                                                                                                                                                                                     |
| Stay Paid (ReminderMedia)          | Real estate                                    | Podcast                                    | Vendor-run agent-marketing podcast                                                                                                      | `unverified` - landing page confirms existence, no episode dates                                                                                                                                                                                                                      |
| Salesman.com (Will Barron)         | Was cross-vertical B2B; now service businesses | Web, formerly The Salesman Podcast         | **Repositioned**: salesman.org redirects to salesman.com, now a service-business mentorship funnel with no episode archive; B2C-leaning | `verified-active` (redirect only) - treat the podcast era as ended                                                                                                                                                                                                                    |

---

## Graveyard - dead, renamed, merged, migrated, or ruled out

The pattern to internalize: brands here migrate silently far more often than they shut down. Old URLs redirect or rot quietly. Everything below is excluded from every table above - do not reintroduce a row from here into a recommendation without a fresh browser-based verification.

| Source                                | What happened                                                                     | Current state                                                                                                                                               |
| ------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sales Hacker → GTMnow                 | Re-acquired by GTMfund from Outreach, rebranded (Aug 2023)                        | saleshacker.com 301s to gtmnow.com; active under the new name                                                                                               |
| Blissful Prospecting → Outbound Squad | Jason Bay moved brands; old domain left to rot (Cloudflare 526)                   | Old domain dead, no redirect; new brand active                                                                                                              |
| Revenue Collective → Pavilion         | Rebrand + $25M growth financing (2021)                                            | Active as Pavilion                                                                                                                                          |
| Outreach.io → Outreach.ai             | Company domain rebrand                                                            | Old domain redirects                                                                                                                                        |
| Chorus.ai                             | Acquired by ZoomInfo (~$575M, Jul 2021), folded in                                | No longer standalone                                                                                                                                        |
| CSO Insights                          | Absorbed via Miller Heiman → Korn Ferry (2016/2019)                               | Defunct as a brand; its Sales Performance Optimization study no longer published                                                                            |
| OpenView SaaS Benchmarks              | OpenView wound down (2024)                                                        | Report continues under High Alpha                                                                                                                           |
| LinkedIn State of Sales               | No edition after 2022                                                             | Apparently discontinued (inferred from absence, not announced)                                                                                              |
| Sales Enablement Society              | Rebranded Revenue Enablement Society (2023)                                       | Active under new name                                                                                                                                       |
| Josh Braun Substack                   | joshbraun.substack.com holds two posts, both Apr 2023                             | `likely-dead` as a newsletter; Braun himself is reported active elsewhere, probably LinkedIn (unverifiable by fetch) - recommend the person, never this URL |
| Kyle Coleman Substack                 | kylecoleman.substack.com archive shows "No posts"                                 | `likely-dead` as a newsletter; Coleman remains professionally active - same treatment as Braun                                                              |
| Modern Sales Pros                     | Invite-only forum, 35,000+ members (self-claim); last clearly dated activity 2024 | `likely-dead` - may continue privately, but not recommendable without a member's confirmation                                                               |

Reversed on re-verification with search access (2026-09) - move these three into the live recommendation table, not this ruled-out one:

- **Masters of MEDDICC (Andy Whyte)** - confirmed real and actively producing episodes under the MEDDICC brand's own media channel (meddicc.buzzsprout.com; distributed to Apple Podcasts, Spotify, iHeart). Recent named episodes with named guests (CROs at Microlise, StarTree, Sales Collective). `verified-active`.
- **Andy Elliott / The Elliott Group** - the correct domain is `elliott247.com`, not andyelliott.com or theandyelliott.com. The Elliott Group is active, Scottsdale AZ-based, with an active YouTube channel (@AndyElliottOfficial) and Instagram (@officialandyelliott). `verified-active`.
- **SDR Chronicles (Morgan J Ingram)** - the personal-domain dead end was the wrong lead; his current vehicle is a YouTube channel under the same "SDR Chronicles" name, plus a LinkedIn Live show ("Muffins with Morgan"), through his role as Director of Sales Execution and Evolution at JB Sales Training (JBarrows). `verified-active` under the corrected identifiers.

## Signal vs noise

**Genuinely practitioner-cited:**

- B2B: 30MPC, John Barrows, Bridge Group, RepVue, r/sales itself.
- B2C: D2DCon, 8% Nation, Tom Ferry's Success Summit, within their verticals.

**Noise dressed as signal:**

- The "best sales podcasts" listicle genre (vendor SEO).
- Vendor benchmark framing (real data, self-serving conclusions).
- The B2C funnel where free content exists to sell a conference ticket that sells a coaching program. The information can still be real, but the business model is the product.
