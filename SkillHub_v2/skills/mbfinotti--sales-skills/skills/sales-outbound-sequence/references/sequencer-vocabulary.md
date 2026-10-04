# Sequencer Vocabulary Mapping

Optional integration note - the only place vendor names appear in this skill. The plan itself is written in the generic terms of the left column; translate when loading it into a specific tool.

| Generic term in the plan | Concept                              | Verified vendor terms                                                                                                                                                  |
| ------------------------ | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sequence / cadence       | The whole multi-touch program        | HubSpot "sequence"; lemlist "campaign"                                                                                                                                 |
| Step / touch             | One scheduled action                 | HubSpot "step" (automated email, manual email task, call task, general task, social task); lemlist "step"                                                              |
| Wait / delay             | Gap between steps                    | HubSpot: delays set in business days, up to 90                                                                                                                         |
| Exit / unenroll          | Removal on reply, meeting, opt-out   | HubSpot "unenroll" - with an option to unenroll the contact alone or all contacts at the company (the account-level pause this skill's multi-threading rule relies on) |
| Suppression              | Never-enroll lists                   | Generally a settings-level exclusion list; name varies by tool                                                                                                         |
| Skip / snooze            | Pausing one step or one prospect     | lemlist per-lead step skip                                                                                                                                             |
| Sender rotation          | Later steps from a different mailbox | lemlist supports same-thread sender rotation                                                                                                                           |

Only the HubSpot and lemlist terms above were verified against vendor documentation while researching this skill. Other sequencers - Outreach, Salesloft, Apollo, Salesforce Sales Engagement, Reply.io, Smartlead, Instantly, and B2C flow builders like Klaviyo or Customer.io - implement the same concepts under their own names (e.g. "cadence", "flow", "journey"). Check the tool's own documentation rather than assuming the mapping.

Two practical checks before loading any plan into a tool:

- Confirm whether delays count calendar days or business days (a "day 3" touch can land on a Sunday otherwise).
- Confirm the tool's exit triggers cover all five immediate exits - many auto-exit on reply but not on a reply from a colleague at the same account.
