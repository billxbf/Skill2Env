# Confounder Screen - The Differential Diagnosis Playbook

Run every section before any fatigue verdict. Each entry gives the telltale pattern that distinguishes the confounder from true fatigue, and the check that confirms it (screen FAILS, the confounder explains the decline) or clears it (screen PASSES, move on). A single confirmed confounder that accounts for the decline ends the fatigue inquiry: the verdict is `confounded` (or `saturating` for the audience case) and the fix targets the cause, not the creative.

True fatigue's signature, for contrast:

- Gradual, sustained across two-plus periods.
- Specific to individual creatives rather than the whole account.
- Visible in two or more signals at once.
- Conversion rate typically holding while costs rise.

Run all eleven regardless; this order only decides what to check first when the clock is short, ranked by decline explained per minute of checking:

- efficiency: change-history reads (§1 budget/bid, §2 learning-phase reset, §11 sibling mix, §10 landing page/offer) > window-composition recomputes (§5 seasonality, §7 attribution maturity, §9 noise) > breakdown pulls (§8 placement/device, §4 auction CPM against the account's other ad sets) > pool trending (§3 saturation)
- effort, lightest first: change-history reads (one log, minutes) > window recomputes (re-run the delta on matched windows) > breakdown pulls (one export per dimension) > pool trending (a reach series, and sometimes a live fresh-creative test)

The top group leads on both axes because it is where this file's own biggest false-positive generator sits - a learning-phase reset is answered by a date, not by analysis. Re-rank for the account: an account nobody has touched in six weeks makes the change-history group cheap but empty, which promotes the window recomputes to first.

## 1. Budget or bid change

More spend forces the platform into broader, cheaper-to-lose auctions and lower-intent pockets of the audience; efficiency degrades in a way that looks identical to fatigue - CTR down, CPA up - within days of the increase.

- Telltale: the decline starts at, or within the learning re-stabilisation window after, a budget/bid step - not gradually. The whole ad set moves together, not one creative.
- Check: pull the change history and overlay change dates on the metric series. Decline onset aligned to a budget/bid event → FAIL. If the budget rose, compare against the _pre-increase_ efficiency at the old spend level, not against the peak; some efficiency loss at higher spend is the normal cost of scale, not decay.

## 2. Learning-phase reset

Any significant edit - creative tweak, budget step beyond the platform's tolerance, audience or optimization-event change, bid-strategy change, a long pause - resets algorithmic learning, and delivery swings wildly for days afterwards. New launches do the same in their first days. This is the single biggest false-positive generator.

- Telltale: high day-to-day variance rather than a steady slide; onset exactly at an edit or launch; platform UI showing "learning" status.
- Check: interview answer plus change history for the last-edit date. Any significant edit inside the comparison window → FAIL; re-measure only on a clean window starting after delivery stabilises. Meta's guidance: allow at least 7 days after a significant edit before evaluating.

## 3. Audience overlap / audience saturation

The pool is depleting - through small audience size, overlapping ad sets bidding against each other, or simply having reached everyone - and no creative, however fresh, fixes a tapped-out pool. Fatigue and saturation need opposite remedies (new creative vs audience expansion), which is why this split gets its own verdict.

- Telltale: first-time impression ratio falling, reach flattening while impressions climb, frequency grinding upward account-wide, and - the key separator - conversion rate degrading along with engagement (fatigue usually leaves CVR stable while costs rise). Multiple creatives in the same audience decaying together points at the pool, not the assets.
- Check: trend first-time impression ratio (or new-user reach) and rolling reach. Where feasible, run the discriminating test from Meta's research: launch a fresh creative to the _same_ audience - recovery means it was fatigue; no recovery, but performance returning on a _fresh_ audience, means saturation → verdict `saturating`. Also check audience-overlap tooling for sibling ad sets competing for the same people.

## 4. Auction-side CPM inflation

Competitor entry, seasonal auction pressure (Q4, sales periods, elections) raises the price of every impression. Costs rise with the creative doing nothing wrong.

- Telltale: CPM up while CTR holds steady - the audience responds exactly as before; each response just costs more. Usually visible account-wide and industry-wide, not on one creative.
- Check: compare the creative's CPM trend against the account's other ad sets and, if available, category benchmarks for the same weeks. CPM up, CTR flat → FAIL (auction, not fatigue). CPM up _and_ CTR down remains consistent with fatigue - keep screening.

## 5. Seasonality and comparison-window composition

Weekends, holidays, paydays, and seasonal demand shifts change who is online and how they behave. A comparison window with different day-of-week or holiday composition than its baseline manufactures a decline from nothing.

- Telltale: the "decline" disappears when comparing like-for-like days (this Tuesday-to-Monday vs last Tuesday-to-Monday), or mirrors last year's seasonal curve.
- Check: recompute the delta on day-of-week-matched windows excluding holidays and promo days. Delta shrinks into the noise band → FAIL.

## 6. Tracking breakage, deduplication faults, consent-mode shifts

A pixel outage, a broken event, a server-side/browser dedup fault, or a consent-banner change under-reports conversions. Reported CPA rises while real performance is unchanged - measurement decayed, not the creative.

- Telltale: conversions drop suddenly (often to a step-function new level) while clicks and engagement hold; the drop coincides with a site release, tag change, or consent update; platform-reported conversions diverge from the order system.
- Check: reconcile platform-reported conversions against the source of truth (orders, CRM) for the window. The healthy state is a _stable ratio_ between the two, not equality; a ratio that lurches at the decline's onset → FAIL. Also check the platform's event diagnostics for match-quality or event-volume drops.

## 7. Attribution-window skew

Platforms attribute conversions to the click date and keep crediting for days afterwards, so the most recent days of any trailing window are always under-reported. Every trailing window therefore ends in an apparent decline - phantom decay by construction. Comparing metrics across different attribution windows (7-day-click vs 1-day-click) manufactures the same artefact.

- Telltale: the "decay" is concentrated in the last few days of the window and backfills upward when re-pulled a week later; or the baseline and comparison windows use different attribution settings.
- Check: compare only lag-mature windows (both windows old enough that the attribution window has fully closed), same attribution setting on both. Decline evaporates on mature windows → FAIL.

## 8. Placement or device mix shift

The same ad delivering into a different placement/device mix (more Audience Network, more right-column, more mobile) shows different blended CTR/CPM without any change in creative effectiveness - the mix moved, not the response within any cell.

- Telltale: blended metrics decline while per-placement metrics are stable; the placement/device breakdown shows share shifting toward structurally-lower-CTR inventory.
- Check: break the metric down by placement and device and compare within cells against the same cells in the baseline. Within-cell stability with shifted mix → FAIL.

## 9. Normal statistical noise on small numbers

Small daily denominators make rates jump around; a two-day dip on a few thousand impressions is a coin flip, not a trend.

- Telltale: the observed delta sits inside the baseline's sampling-noise band; the "trend" is one or two periods old; single-day granularity on a low-volume creative.
- Check: run the Confidence Gate's noise check (`p ± 2 × sqrt(p(1-p)/n)` on the baseline window). Delta inside the band, or fewer than two consecutive periods of movement → FAIL (as in: not evidence of anything). This is the confounder the gate exists to formalise.

## 10. Landing page or offer change downstream of the ad

A page redesign, price change, stock-out, expired promo, slower page, or broken form collapses conversion downstream of a perfectly healthy ad.

- Telltale: CTR and engagement healthy, CVR down - the exact inverse of the fatigue signature. Onset aligned to a site deploy or offer calendar. All traffic sources to that page degrade together, not just this creative.
- Check: overlay site/offer change dates; compare CVR for other traffic hitting the same page. Page-wide CVR drop → FAIL; the fix is the funnel, not the creative.

## 11. Sibling-mix shift inside the ad set

Adding or removing creatives changes how the platform splits delivery. A new sibling siphons spend and the best pockets of the audience; a removed sibling dumps its (possibly worse-fit) delivery onto the survivors. The measured creative's blended numbers move without its effectiveness changing. Cosmetic resizes count as siblings too - near-duplicates cannibalise each other's reach.

- Telltale: the decline's onset matches a sibling launch/pause in the same ad set; spend share moved at the same moment; the creative's within-segment response is stable where it still delivers.
- Check: change history for sibling adds/removals inside the window; trend each sibling's spend share. Mix event aligned with the decline → FAIL - re-baseline from the new mix's stabilisation date instead of refreshing the creative.
