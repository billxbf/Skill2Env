# Cadence Patterns and the Length Decision

How to size and shape a cadence. Every number below is vendor-published or practitioner-reported unless labeled platform policy - treat magnitudes as calibration, not truth.

## Table of Contents

- [The length disagreement, stated honestly](#the-length-disagreement-stated-honestly)
- [Decision rule](#decision-rule)
- [Channel roles, ranked by replies per rep-minute](#channel-roles-ranked-by-replies-per-rep-minute)
- [Spacing](#spacing)
- [Motion-specific shapes](#motion-specific-shapes)
- [B2C lifecycle shapes](#b2c-lifecycle-shapes)
- [Breakup or just stop](#breakup-or-just-stop)

## The length disagreement, stated honestly

**Long camp** - sales-training practitioners and sales-engagement vendors:

- A prominent practitioner playbook teaches 10-14 touches over ~30 days (elsewhere 12-15 touches over 14-28 days), organized as weekly clusters of roughly 2 calls + 2 emails + 1 social touch, phasing social out mid-sequence and calls out late. It blends one email vendor's large dataset with the practitioners' own client work.
- A sales-engagement vendor's benchmark page recommends 8-12 touches over 17-21 days, with a channel mix of email 40-50%, phone 20-30%, social 15-25%, video 5-10% (vendor-published; it cites analyst research for "3+ channels, 15+ touches" at the enterprise end).
- The oldest named framework here, Cold Calling 2.0 (from the book _Predictable Revenue_), runs 5 emails on days 1 / 3 / 7 / 14 / 30 - breakup at day 14, trigger-gated re-engagement at day 30 - and reports the day-14 breakup often drawing the highest per-touch response.

**Short camp** - email-quality vendors and outbound agencies:

- A well-known email-coaching practitioner caps cadences at 5 emails - 3-4 if multi-channel - calls the industry's 15-25-touch defaults a symptom of low relevance, and cites a 4-email / 12-day cadence hitting a 10%+ meeting rate. His exit rule: no ceremonial breakup, just stop, and return when there is a new reason.
- An outbound agency's 2026 study of its own sends puts the sweet spot at 3-5 steps, finds step 3 books more meetings than steps 1 and 2 combined, and finds steps 2-5 produce the majority of email pipeline (vendor-published).
- Aggregated cold-email statistics report response dropping ~55% and spam complaints tripling past the fourth follow-up (vendor-published aggregation).

**Where the camps converge** (rare enough to trust more than any single number):

- Replies accumulate well past touch 1 - independently reported as ~70% of replies after email 1, and as steps 2-6 carrying ~59% of replies. Never judge a sequence on its first touch.
- Multi-channel touches raise email replies rather than winning on their own channel.
- Exit immediately on reply, everywhere.

## Decision rule

**short > mid > long** on replies bought per rep-hour and per point of domain risk - that is the starting order, and the table below is what overrides it. Score each factor from the Interview. Three or more marks in a column picks that pattern; a tie defaults short.

| Factor                     | Push long (9-15 touches, 3-4 weeks, 3 channels) | Push short (3-5 emails, 1-2 weeks) |
| -------------------------- | ----------------------------------------------- | ---------------------------------- |
| Segment                    | Enterprise ABM                                  | SMB high-velocity                  |
| List per rep               | Small, named accounts                           | Large, scored list                 |
| Personalization depth      | Deep per-account research                       | Templated or light                 |
| Channels genuinely staffed | 3+ (reps actually make the calls)               | Email only                         |
| Deal size                  | High ACV, long cycle                            | Low ACV, fast cycle                |

Mid-market or mixed signals: 6-9 touches over 2-3 weeks on 2 channels.

Ties default short because the downside is asymmetric: an over-long cadence on a low-relevance list multiplies complaints (vendor-published: complaints triple past follow-up 4) and damages the sending domain. A too-short one merely under-touches, and can be extended at the next recycle with data in hand.

What that default starves is the long multi-channel pattern on high-ACV named accounts, where the touches the short rule cuts are the ones that reach a buyer who ignores email entirely. Three factors promote it anyway:

- A list small enough that a rep knows each account.
- Channels genuinely staffed rather than nominally available.
- A deal size that pays for a quarter of persistence.

B2C: the trigger decides length, not this rubric - see the B2C shapes below.

## Channel roles, ranked by replies per rep-minute

Buy channels in this order, and stop where the capacity math stops you:

**in-thread bump > blank connection request > extra email angle > call + voicemail > social DM > video message**

The bump leads because it is the only touch that costs near-zero on every axis and still out-replies the email it follows. The axes disagree, so read them apart:

- value (replies added per prospect): call + voicemail > extra email angle > in-thread bump > blank connection request == social DM > video message
- effort (rep minutes per touch, heaviest first): video message > call + voicemail > social DM > blank connection request == in-thread bump == extra email angle
- deliverability risk (least reversible first): extra email angle > in-thread bump > call + voicemail == social DM == blank connection request == video message
- compliance cost (review the touch triggers before launch): call + voicemail > social DM == blank connection request > email touches > video message

- The three near-zero-effort touches tie because each is one templated step the sequencer fires unattended; the connection request joins them only because personalising it is deleted below, not because a click equals writing.
- The four non-email channels tie at zero deliverability risk because none of them touch the sending domain - their own irreversibility lands on the compliance line instead.

| Touch                    | What it buys                                                                                                                                                                                         | Rep minutes                                                                          | Least-reversible cost                                                                   |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| In-thread bump           | One practitioner source reports the bump out-replying the first email                                                                                                                                | Near-zero - templated, two lines                                                     | Adds send volume against the domain                                                     |
| Blank connection request | Opens the social channel; a practitioner claim and a separate vendor's large dataset agree blank requests connect as well as or better than personalised ones, with identical downstream reply rates | Near-zero                                                                            | Platform automation limits; a banned account is rebuilt, not restored                   |
| Extra email angle        | The channel that carries the ask - every other channel exists to get this one answered                                                                                                               | An hour, once, for the whole cohort                                                  | Complaints accrue against the sending domain, the one asset a cadence cannot un-burn    |
| Call + voicemail         | Multiplies email reply rates; voicemails almost never produce a callback, so the script points back at the email. Cap at two per prospect                                                            | A standing job - a daily call block, and it is the number the capacity math consumes | Do-not-call screening and jurisdictional call-time rules; a violation is not reversible |
| Social DM                | Modest lift once connected; at most two, no pitch, phase out mid-sequence                                                                                                                            | Minutes per prospect, manual                                                         | Platform ToS review; same account exposure as above                                     |
| Video message            | No independent evidence recovered - one vendor benchmark allots it 5-10% of the mix                                                                                                                  | Heaviest per touch, and it never templates                                           | Near-zero beyond a hosting/tracking privacy notice                                      |

Default rung: email sequence plus the in-thread bump plus the blank connection request. Promotion conditions:

- Call + voicemail: when callers are genuinely staffed, the list is small enough that a daily block covers it, and ACV justifies the block.
- Social DM: only after the connection is accepted.
- Video: only on a named-account list an SDR can hold in their head.

What this order starves: the human-voice channels. Call + voicemail sits top on value and top on effort, so a ratio ranking demotes it every round - and a collection that only ever computes efficiency ends up all-email against buyers who never answer email. Promote it anyway when the domain is the binding constraint rather than rep time: a new or warm-up-limited domain cannot buy more email touches at any price, which makes the call block the only remaining channel.

Deleted, not demoted:

- Personalised connection-request notes: the data says they buy nothing over blank ones, so the minutes are pure waste.
- SMS or messaging to any prospect without express opt-in: no consent basis, so it is not an option to rank.

Say which you dropped and why when presenting the plan.

Re-rank against what you already know about this user before presenting it:

- Domain state: a warmed domain with headroom promotes email touches; a new one promotes the call block.
- Team composition: a founder doing their own outbound has no daily call block, which pushes every manual channel down; an SDR team has one standing already, which pulls calls up.
- List size: a list of thirty named accounts inverts the whole order - per-account effort is affordable there and volume is not the constraint.

Two open questions the ranking does not settle:

- One theme at a time, or a new angle per email? Genuinely contested - one vendor hosts both philosophies and reports the multi-angle style outperforming in some campaigns. Treat it as a test candidate; default to a new angle per email since more sources lean that way.
- Phone connect rates conflict across vendors (roughly 5% pickup and declining, versus an agency reporting ~18.6% connection). Measure your own; commit no threshold borrowed from either.

Reuse the first touch's personalization across later touches and channels instead of re-researching each step - do the research once (route the angle choice itself to `mbfinotti/sales-skills@sales-outreach-personalization`, which ranks personalization tiers by minutes against replies booked).

## Spacing

- Front-load, then widen: 1-3 working-day gaps between early touches, stretching to 4-7 days toward the tail. Identical principle for B2B and B2C win-back.
- Trigger-anchored B2C flows are the exception and compress to hours (below).
- One intentional multi-channel cluster day is a legitimate named practitioner move (email + call + voicemail + social on day 1). Label it in the plan; never let clustering happen by accident.
- Send in recipient-local business windows and skip the recipient geography's holidays - identical for B2B and B2C. B2C adds legally loaded quiet hours for SMS and calls: confirm the jurisdiction's rules rather than assuming a window; messaging vendors treat quiet-hours violations as a litigation risk, not just etiquette.

## Motion-specific shapes

- **Cold outbound**: full pattern from the decision rule above.
- **Inbound-lead follow-up**: speed beats touch count.
  - First touch within the same working hour - the widely cited minutes-matter research is real but paywalled and not independently re-verified here; treat the direction as credible, the multipliers as folklore.
  - Then a short 3-4 touch sprint. Do not run a full cold pattern on someone who asked to hear from you.
  - Identical urgency logic for B2C signups and demo requests.
- **Event follow-up**: 3-4 touches over 7-10 days, first within 48 hours while memory is fresh. This shape is a convention across comparable playbooks, not measured data - say so.
- **Closed-lost / dormant re-engagement**: trigger-gated, not scheduled. Define stale (90-180 days without engagement, practitioner range), watch for job change, funding, or tech-stack change, then run a short 2-3 touch sequence that leads with the trigger. Only a small fraction of a stale list develops a fresh trigger in a given quarter - re-engage those, not the whole list.

## B2C lifecycle shapes

- **Cart / browse abandonment** (vendor-published structure): touch 1 a few hours after abandonment, touch 2 at +24-48h (incentive only here, not on touch 1 - discounting touch 1 trains abandonment), then stop. Add an SMS only with express opt-in, only inside quiet hours, and at most one SMS in the flow.
- **Win-back**: 2-3 touches starting 60-90 days after last purchase, then a sunset/re-permission message ("stay or go") and removal on silence.
- **Cross-flow rules**:
  - One flow at a time per person.
  - A global frequency cap across all marketing sends (vendor guidance clusters around a handful per week).
  - Suppress active-flow customers from batch campaigns.
  - Exits on purchase, reply, or opt-out are immediate, identical to B2B.
- Welcome and onboarding series are lifecycle marketing, out of this skill's scope beyond the spacing principle above.

## Breakup or just stop

**breakup touch > quiet stop** - on a long B2B cadence, and only there. Both cost one templated send or less, so the ranking is decided almost entirely on the value side.

- value (replies bought at the tail): breakup > quiet stop.
  - A practitioner playbook reports breakup emails raising reply rates sharply when framed as an explicit yes/no ("give them a reason to say no").
  - A CRM vendor reports 10-15% response on breakups.
  - The Cold Calling 2.0 framework places it as the highest-responding touch.
  - All vendor-published or practitioner-reported.
  - A quiet stop buys no reply now and keeps nothing but the option to return.
- effort: breakup > quiet stop. One extra templated send against zero; both round to near-zero.
- reversibility (what it spends): breakup > quiet stop. A sent breakup is a promise, so it spends the account's re-entry option until a genuine new trigger appears. The quiet stop spends nothing and can re-approach inside the cooldown.

Default: a breakup earns its slot at the end of a long B2B cadence; a short sprint just ends, and its last email may simply say so. What that order starves is the small named-account list, where the option to re-approach next quarter is worth more than one reply this month - on a list you cannot afford to burn, take the quiet stop even on a long cadence.

Not a menu for B2C: the sunset/re-permission message is a consent obligation, not a tactical choice, so there is nothing to rank against it. Send it, and remove on silence.

A sent breakup is a promise: suppress until a genuine new trigger.
