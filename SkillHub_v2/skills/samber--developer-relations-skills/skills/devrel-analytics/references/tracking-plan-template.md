# Tracking plan template

Copy the structure, fill it with the user's real surfaces and events, and keep the version block current. The plan is a contract between whoever defines the metric and whoever implements it - everything ambiguous in it becomes a defect three months later.

## Contents

- [Template](#template)
- [Worked example: a devtool docs and repository plan](#worked-example-a-devtool-docs-and-repository-plan)
- [Event naming: good vs bad](#event-naming-good-vs-bad)
- [Two rows compared](#two-rows-compared)
- [Two tagging vocabularies compared](#two-tagging-vocabularies-compared)

## Template

```markdown
# <Product> DevRel tracking plan

Version: 1.0 · Owner: <name> · Last verified: <date> · Review trigger: <redesign, new surface, quarterly>

## Decisions this plan serves

| #   | Decision | Question that settles it | Funnel view |
| --- | -------- | ------------------------ | ----------- |

## Surface register

| Surface | Owner | Data source | Retention | Known bias | Snapshot schedule |
| ------- | ----- | ----------- | --------- | ---------- | ----------------- |

## Build order

| Rank | What gets built | Effort (order of magnitude) | What it buys | Deleted / deferred, and why |
| ---- | --------------- | --------------------------- | ------------ | --------------------------- |

## Identity spine

- anonymous_id: <where set, which domains carry it>
- user_id: <when assigned, which event stitches it>
- account_id: <resolution rule, or "not applicable - individual motion">
- Unresolvable surfaces: <list, and the substitute signal for each>

## Events

| Event | Surface | Trigger | Properties | Decision # | Verified |
| ----- | ------- | ------- | ---------- | ---------- | -------- |

## Property registry

| Property | Type | Allowed values | Notes |
| -------- | ---- | -------------- | ----- |

## Link tagging vocabulary

| Parameter | Allowed values / pattern |
| --------- | ------------------------ |

## Funnel views

| View | Entry event | Steps | Success event | Segment |
| ---- | ----------- | ----- | ------------- | ------- |

## Baselines captured

| Metric | Value | Date | Source |
| ------ | ----- | ---- | ------ |

## Quality gate

| Check | Threshold | Current | Status |
| ----- | --------- | ------- | ------ |

## Known gaps

| Gap | Impact on which number | Owner | Decision |
| --- | ---------------------- | ----- | -------- |
```

## Worked example: a devtool docs and repository plan

Decision list (abridged):

| #   | Decision                           | Question                                            | Funnel view        |
| --- | ---------------------------------- | --------------------------------------------------- | ------------------ |
| 1   | Rewrite the quickstart or leave it | Where do first-time readers stop?                   | Quickstart funnel  |
| 2   | Keep or drop the weekly blog       | Do blog readers ever reach a first successful call? | Blog-to-activation |
| 3   | Renew the conference sponsorship   | Did the event produce anything past a badge scan?   | Event-tagged entry |

Events (abridged):

| Event                       | Surface | Trigger                           | Properties                                      | Decision # |
| --------------------------- | ------- | --------------------------------- | ----------------------------------------------- | ---------- |
| `docs_page_viewed`          | docs    | page render                       | `section`, `path`, `version`, `language`        | 1, 2       |
| `quickstart_step_completed` | docs    | step checkpoint reached           | `step_number`, `step_name`, `language`          | 1          |
| `sample_copied`             | docs    | copy control used on a code block | `path`, `block_id`, `language`                  | 1          |
| `docs_search_performed`     | docs    | search submitted                  | `query_length`, `results_count`, `zero_results` | 1          |
| `signup_completed`          | app     | account created                   | `self_reported_source`, `anonymous_id`          | 1, 2, 3    |
| `first_api_call_succeeded`  | product | first 2xx from a new account      | `endpoint`, `sdk_version`, `hours_since_signup` | 1, 2, 3    |

Quickstart funnel view: entry `docs_page_viewed {path: /quickstart}` → `quickstart_step_completed {step_number: 1..n}` → `signup_completed` → `first_api_call_succeeded`, segmented by `language` and by inbound source.

Known gap worth writing down explicitly: docs page views are collected client-side and a majority of this audience blocks that collection, so the funnel's absolute entry count is a floor. Step-to-step ratios inside the funnel are unaffected as long as the blocking is not correlated with the step - record that assumption, and sanity-check it once against server logs.

## Event naming: good vs bad

```
// ✓ Good - object then action, context lives in properties
quickstart_step_completed {step_number: 3, step_name: "install", language: "python"}
sample_copied {page, block_id, language}
docs_search_performed {query_length, results_count, zero_results}
first_api_call_succeeded {endpoint, sdk_version}

// ✗ Bad - context baked into the name, or no properties at all
reference_page_viewed
python_quickstart_step_3_done
button_clicked  // no properties
```

The first two bad names push context into the name, so every future query has to enumerate names. The third pushes everything into one bucket you can never split.

## Two rows compared

Good row:

| Event                       | Surface | Trigger                                                | Properties                                                 | Decision # |
| --------------------------- | ------- | ------------------------------------------------------ | ---------------------------------------------------------- | ---------- |
| `quickstart_step_completed` | docs    | reader reaches the checkpoint that proves the step ran | `step_number` (int), `step_name` (enum), `language` (enum) | 1          |

Bad row, and why:

| Event                          | Surface | Trigger                      | Properties          | Decision # |
| ------------------------------ | ------- | ---------------------------- | ------------------- | ---------- |
| `python_quickstart_step3_done` | docs    | scrolled past the code block | `label` (free text) | -          |

- The name hard-codes language and step, so every future query must enumerate event names and a fifth step means a fifth event.
- "Scrolled past" measures the page, not the reader. A step event has to fire on evidence the step worked, otherwise the funnel measures scrolling.
- A free-text property is un-queryable within a quarter.
- No decision number: nothing changes when this number moves, so the row should not exist.

## Two tagging vocabularies compared

Good - closed lists, one casing, a pattern the author can follow without asking:

| Parameter | Allowed values / pattern                                                                                                      |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| source    | `x`, `linkedin`, `hn`, `reddit`, `newsletter`, `conf`, `podcast`, `partner` (closed list; additions need a plan version bump) |
| medium    | `social`, `email`, `referral`, `talk`, `sponsorship` (closed list)                                                            |
| campaign  | `<yyyy-mm>-<artifact-slug>`, lowercase, hyphen-separated                                                                      |

Bad, and why every line of it breaks a report:

| Parameter | Allowed values / pattern                                                                                                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| source    | anything descriptive (`Twitter`, `twitter`, `X`, `x.com` all appear within a month, and no report can merge them afterwards) |
| medium    | `social media`, `Email Newsletter` (spaces and mixed case survive some tools and get mangled by others)                      |
| campaign  | `launch` (reused for three launches in eighteen months, so the series is meaningless)                                        |

Two more mistakes belong here rather than in the vocabulary:

- Tagging internal docs links, which restarts the session and overwrites the real source with your own.
- Leaving the published-link register unwritten, which makes every historical tag unreadable once its author forgets what it meant.
