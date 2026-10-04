# Subject Line Pattern Library

Every statistic below is vendor-published marketing data from companies selling email tooling - email-coaching products, revenue-intelligence platforms, outbound agencies, and sales-engagement platforms. None is independently audited or peer-reviewed, and the percentages from different vendors do not reconcile with each other. Trust the direction, never the magnitude.

No named, cross-source framework exists for subject lines; what follows is the unbranded convergence across independent sources plus clearly labeled single-source claims. Company names in examples (Northwind, Acme) are fictional.

## Table of Contents

- [B2B cold outbound](#b2b-cold-outbound)
- [B2C lifecycle and promotional](#b2c-lifecycle-and-promotional)
- [Parked questions - ranked test queue](#parked-questions-ranked-test-queue)
- [Rules identical in B2B and B2C](#rules-identical-in-b2b-and-b2c)

## B2B cold outbound

Regime summary: short, plain, anchored to the recipient's world. The best-corroborated rule in the whole domain - stated independently by an email-coaching vendor, by two separate revenue-intelligence datasets (25-28M cold emails; 1M+ executive sales cycles), and by an outbound agency (5.5M emails) - is to keep it to roughly 1-4 words.

### Length

- Target 1-4 words, at most ~35 characters. Mobile clients truncate around 30-35 characters, so brevity is a hard constraint, not a style choice.
- Vendor figures for calibration: 2-word subjects ~60% more opens than 5-word (email-coaching vendor); 2-4 words ~46% open rate vs. 34% at 10 words (outbound agency, 5.5M emails); moving from 2 to 4 words reduced replies ~17.5% (same email-coaching vendor).

### Angle catalog - pick one per variant

Ranked by replies bought per research minute spent, highest ratio first - not by what is cheapest. Research cost is the only effort that counts here: minutes spent per prospect, and whether the angle is written once for a whole list or rewritten prospect by prospect.

- efficiency: `internal-style noun > specific pain question > executive-world anchor > competitor == company initiative > trigger event`
- value, replies when it lands: `trigger event > internal-style noun > executive-world anchor > competitor == company initiative > specific pain question`
- research effort: `trigger event > competitor == company initiative > executive-world anchor > internal-style noun == specific pain question`

Both ties are real:

- `internal-style noun == specific pain question` on effort: neither adds a per-prospect lookup - one comes from the body's own topic, the other from the persona pain known before opening the list.
- `competitor == company initiative` on both axes: they cost one pass over the same public account pages, survive the same sequence, and buy the same thing - proof the sender read the account - with no vendor measurement separating them.

Casing in the examples below is arbitrary. Capitalization is contested (see Parked questions), so treat casing as a test variable, not part of the pattern.

| Angle                         | Research cost                                                       | Mechanism                                                                                                                                          | Good example                                   | Bad example                            |
| ----------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------- |
| Internal-style plain noun     | near-zero; written once, reused across the whole list               | Reads like a colleague's note, not a vendor's pitch; internal-looking subjects roughly doubled opens in a revenue-intelligence study (85M+ emails) | "reply rates" · "trial delays" · "Q2 forecast" | "Boost your reply rates by 300%"       |
| Specific pain question        | near-zero; one pain per persona, reused across the whole segment    | A question naming their exact pain; generic questions fail (see Parked questions)                                                                  | "losing ramp time?"                            | "Quick question?" · "Have 15 minutes?" |
| Executive-world anchor        | an hour per segment; reused for every exec in it                    | Anchors to the exec's stated priorities, never the sender's product (revenue-intelligence executive dataset)                                       | "student dropout risk"                         | "Our platform for education leaders"   |
| Competitor / market reference | an hour per account; survives the whole sequence                    | Names a rival or market shift they track                                                                                                           | "Northwind migration"                          | "Beat your competitors today"          |
| Company initiative            | an hour per account; survives the whole sequence                    | Names a public initiative or project they own                                                                                                      | "Acme expansion plan"                          | "Partnership opportunity!"             |
| Trigger event                 | a standing job; sourced per prospect, goes stale fast, reused never | References something that just happened at their company                                                                                           | "your sdr hiring"                              | "Congrats on the news!!"               |

Default: draft the set from the top of the efficiency order downwards, and stop where the research budget runs out.

**What this order starves: the trigger event.** It has the highest ceiling of any angle here and loses every efficiency round, because a fresh trigger per prospect never amortises across a list.

Promote it anyway when:

- The list is short enough that a day of sourcing covers it.
- A trigger feed is already licensed and monitored.
- The campaign targets named accounts where one missed reply costs more than the sourcing does.

Re-rank against what you already know about the user, and name which fact moved which angle:

- A licensed intent or technographic feed makes the competitor angle near-zero - promote it alongside the internal-style noun.
- No trigger data and no budget to source it deletes the trigger-event angle from the candidate set. Delete it, say so, and draft one fewer variant; an angle parked at the bottom reappears later as work nobody scoped.
- The same deletion hits competitor and company initiative where account-by-account research is not possible.
- An executive-only list promotes the executive-world anchor above the specific pain question: the exec dataset backs the anchor, and the question form is contested.
- An SDR against a fixed daily send quota is spending sends, not research hours - the angle order stands, but the parked-question tests are what gets cut.

This order is a default, not a law. It shifts with list size, recipient seniority, and who executes it; a researcher with account-plan time and an SDR clearing a quota should not draft the same set.

### Anti-patterns with vendor-measured impact

Fix in the order listed. Avoiding any one of these costs the same near-zero effort - a word choice at drafting time, no research and no extra send - so measured harm alone orders the table, and reply damage outranks open damage because replies are what calls the winner in this regime. `empty subject == prospect's first name` on harm: both land on the same measured -12% replies, and nothing in the source set separates them further.

| Anti-pattern                              | Reported impact (vendor-published)                                                                          |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Fake "Re:" / "Fwd:" prefix                | Hard fail, no measurement needed: destroys trust and is the exact deceptive-subject case CAN-SPAM prohibits |
| Pitching the product in the subject       | -57% replies                                                                                                |
| Prospect's first name in the subject      | ~12% fewer replies (attributed to a sales-engagement platform's data) - signals mail-merge                  |
| Empty subject                             | +30% opens but -12% replies                                                                                 |
| Numbers and percentages                   | -46% opens                                                                                                  |
| Excessive punctuation ("!!!", "??")       | -36% opens                                                                                                  |
| Urgency words ("ASAP", "urgent")          | opens fall below 36%                                                                                        |
| Salesy verbs ("increase", "boost", "ROI") | -17.9% opens                                                                                                |

### Contested question: capitalization

- One email-coaching vendor teaches title case and claims skipping it costs roughly 30% of opens.
- Guidance derived from a revenue-intelligence dataset, and a popular paid cold-email training program, teach lowercase instead and claim the data supports that.

These are directly contradictory vendor claims with no independent arbiter. Do not enforce either.

Pick one casing for the current test and hold it constant across every variant; casing itself is ranked in Parked questions below.

### Contested question: questions in the subject

- An outbound agency reports question subjects performing well (~46% open).
- An email-coaching vendor reports questions cutting opens by ~56%.

Practitioner reconciliation: a specific pain question can work; a generic one ("Quick question?") reads as a mass template and fails. Default to statements when unsure.

### Executive recipients

- Executives process hundreds of emails a day and decide in under ~3 seconds (revenue-intelligence study, 1M+ exec cycles).
- Ultra-concise and understated wins; anything salesy is rejected on sight.
- On an executive list, the executive-world anchor moves up the efficiency order, ahead of the specific pain question: their initiative, their risk, their metric is the only framing that survives three seconds.

## B2C lifecycle and promotional

Regime summary: a genuinely different game. Clarity and stated benefit win; several things that measure as negatives in B2B cold (numbers, longer lines) are normal here.

### Length and preheader

- Subject: 40-60 characters ideal; keep to ~50 or less to survive mobile truncation.
- Preheader: ~90-140 characters. It must extend the subject - complete the thought or add intrigue - never repeat it. Subject plus preheader is the tested unit.

### Patterns that work

No value ordering here, deliberately: which pattern wins is decided by what the body contains, not by the pattern itself. A shipping confirmation cannot be a story tease, and a nurture essay cannot be a Direct - ranking these against each other across campaigns would be false precision. So one axis orders the rows, and it is stated rather than implied:

- production effort: `story tease > how-to > direct == number == question`
- Pick the cheapest pattern the body already supports. The three-way tie is genuine: direct, number and question are each one line written from content already sitting in the email, with no extra drafting pass.

| Pattern     | Production effort                                                                                                                 | Good example                               | Bad example                         |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------- |
| Direct      | near-zero; the event names itself                                                                                                 | "Your report is ready"                     | "We have something for you"         |
| Number      | near-zero; count what the body already lists                                                                                      | "3 ways to save on your renewal"           | "37 incredible unmissable deals!!!" |
| Question    | near-zero; name the pain the body answers                                                                                         | "Still struggling with meal planning?"     | "Want to know a secret?"            |
| How-to      | an hour, and only if the body genuinely teaches something                                                                         | "How to cut your grocery bill in one week" | "How to change your life"           |
| Story tease | an hour; needs a real story, and the only pattern that fails silently - intrigue that never pays off costs trust on the next send | "The pricing mistake I almost made"        | "You won't believe what happened!"  |

- Clear beats clever; specific beats vague. If a reader must decode the line, ship the clearer variant.
- Numbers are fine in this regime, unlike B2B cold.
- Emoji is polarizing: never a default, and ranked as a test candidate in Parked questions below.

## Parked questions - ranked test queue

Three questions in this file have no answer worth asserting:

- B2B casing.
- B2B question-versus-statement.
- B2C emoji.

Each is resolvable, and each is paid for in sends rather than hours - a two-arm test needs 200+ sends per variant, so roughly 400+ sends buys one answer - the test-design reference carries that floor and the multi-variant multiplier.

- expected gain: `angle test > casing > question form == emoji`
- send cost: `angle test == casing == question form == emoji` - each is one binary variable resolved by the same two-arm test at the same per-variant floor, so the send bill is identical and gain alone orders the queue
- efficiency: `angle test > casing > question form == emoji`

Run the angle test first, always. Angle carries the only large measured effects in this file - an internal-style noun roughly doubling opens, pitching in the subject costing -57% replies - while every parked question rests on a single unreconciled vendor claim.

| Parked question                   | What resolving it buys                                                                    | Why it ranks here                                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Casing (title case vs. lowercase) | A rule applying to every subject sent afterwards - a compounding asset, not a one-off win | The only parked question with no practitioner reconciliation at all, and the cleanest single variable: casing changes nothing else about the line |
| Question vs. statement            | A default for one angle, and a usable one already exists (specific works, generic fails)  | Hard to run cleanly - a question and a statement are usually different angles too, so the test confounds unless the angle is held identical       |
| B2C emoji                         | An audience-specific answer that does not transfer to another list                        | Same send bill, narrowest scope; the answer expires whenever the audience changes                                                                 |

`question form == emoji` on gain: both buy an answer scoped to one angle or one audience, where casing buys a rule over every future send.

Delete rather than queue: a list too small to power one two-arm test at the floor above has no test queue. Say that plainly and ship the defaults - hold casing constant, statements over questions, emoji off - instead of leaving a queue nobody can run.

## Rules identical in B2B and B2C

These apply unchanged to both regimes:

- One variable per test, with a written falsifiable hypothesis before any variant is drafted.
- Mobile truncation discipline - write for the smallest screen the audience uses.
- Never promise in the subject what the body does not deliver.
- Deceptive subject lines are illegal under CAN-SPAM in both regimes, not merely bad practice.
- Variants must differ by angle, never by synonym swap.
