# Example Cadences and Output Package

Filled examples to copy in shape, never in content - the real plan must come out of the Interview and the decision rule. Day numbers are working days.

## Example A - B2B mid-market, cold outbound, long pattern

Decision-rule record: mid-market segment, ~150 accounts/rep, light-plus personalization, 3 staffed channels, mid ACV → 9 touches / 18 working days / 3 channels.

| #   | Day | Channel    | Type      | Purpose                                                  | Exit check before sending                   |
| --- | --- | ---------- | --------- | -------------------------------------------------------- | ------------------------------------------- |
| 1   | 1   | Social     | Manual    | Connection request, blank                                | Suppression list, active-sequence dedupe    |
| 2   | 1   | Email      | Automated | Problem email - the personalization budget is spent here | Reply/opt-out/bounce                        |
| 3   | 3   | Email      | Automated | In-thread bump, 1-2 lines                                | Reply/opt-out/bounce                        |
| 4   | 5   | Phone + VM | Manual    | Call; voicemail points back to the email                 | Replied or connected → exit to conversation |
| 5   | 8   | Email      | Automated | New angle + proof point                                  | Reply/opt-out/bounce                        |
| 6   | 10  | Phone + VM | Manual    | Second call; second and final voicemail                  | Connected → conversation                    |
| 7   | 12  | Social     | Manual    | Short DM, no pitch, references the email                 | Reply anywhere → exit                       |
| 8   | 15  | Email      | Automated | Third angle or a concrete offer                          | Reply/opt-out/bounce                        |
| 9   | 18  | Email      | Automated | Breakup with explicit yes/no ask                         | Then suppress; recycle window opens day 60  |

Multi-threading: second contact at the account enters the same table offset by 3 days; a reply from either pauses the other pending rep review. Personalization from touch 2 is reused in touches 4, 6, and 7.

## Example B - SMB high-velocity, short sprint

Decision-rule record: SMB, 600-prospect scored list, templated personalization, email only → 4 emails / 12 working days.

| #   | Day | Channel | Type      | Purpose                                                 |
| --- | --- | ------- | --------- | ------------------------------------------------------- |
| 1   | 1   | Email   | Automated | Problem email, segment-level personalization            |
| 2   | 4   | Email   | Automated | In-thread bump                                          |
| 3   | 8   | Email   | Automated | New angle + proof                                       |
| 4   | 12  | Email   | Automated | Final note - states it is the last, no breakup ceremony |

Same exit checks as Example A before every send. Cohort enters in daily batches of 120, not one launch. Recycle at day 90, trigger-gated.

## Example C - B2C cart abandonment (trigger-anchored)

Consent recorded at signup for email; SMS included only for express double opt-in subscribers.

| #   | Time after abandonment | Channel | Purpose                              | Conditions                                                   |
| --- | ---------------------- | ------- | ------------------------------------ | ------------------------------------------------------------ |
| 1   | +2-4 h                 | Email   | Reminder, cart contents, no discount | Not purchased; not in another flow                           |
| 2   | +24 h                  | Email   | Incentive if margin allows           | Not purchased                                                |
| 3   | +26 h                  | SMS     | One-line nudge                       | Express opt-in only; inside quiet hours; the flow's only SMS |
| 4   | +48 h                  | Email   | Final reminder, then flow ends       | Not purchased                                                |

Exits: purchase, opt-out - immediate, identical to B2B reply exits. Cross-flow frequency cap applies; suppressed from batch promotions while in-flow.

## Negative example - the pile-up

| Day | Touches                                            |
| --- | -------------------------------------------------- |
| 1   | Email + call + voicemail + DM + connection request |
| 2   | Email + call + SMS                                 |
| 3   | Email + DM                                         |

Why it fails: three channels a day with no labeled cluster:

- Reads as harassment.
- Spends the whole channel budget before any reply data arrives.
- Triggers opt-outs and complaints that damage the domain for every other sequence.
- Leaves nothing for week 2.

One intentional cluster day maximum; spread the rest.

## Output package sample

Deliver every plan in this shape, in order:

1. **Cadence table** - as in the examples: touch, day, channel, type, purpose, exit check.
2. **Decision-rule record** - the factor scores and the pattern they picked.
3. **Multi-threading plan** (B2B) - contacts per account, stagger, account-level pause rule.
4. **Exit, suppression, and recycle block** - immediate exits, pre-enrollment suppression checklist, cooldown length, re-entry trigger and cap, breakup-or-stop choice with one line of rationale.
5. **Capacity check** - the arithmetic from the capacity reference, showing the plan fits.
6. **Pre-committed metrics** - thresholds, ceilings, review date (template in the capacity reference).
7. **Copy handoffs** - the list of touches needing copy, each routed to its sibling skill.
