# QwenCloud CLI Reference

This is the sole reference for CLI installation, authentication flow, command selection, arguments, pagination, output modes, and exit handling. Read the relevant domain reference separately to interpret returned data.

## Prerequisites and Safety

- Require Node.js >= 18 and the QwenCloud CLI. Check with `qwencloud version`; if absent, install with `npm install -g @qwencloud/qwencloud-cli`.
- The account commands in this skill require qwencloud-cli >= 1.3.0. On an older version, do not run them; ask the user to upgrade with `npm install -g @qwencloud/qwencloud-cli` and wait for confirmation before retrying.
- Run only commands and arguments documented here. Never assemble arbitrary shell strings.
- Use only URLs returned by CLI/API output; never construct or guess a URL.
- Before any account-data command, run `qwencloud auth status --format json`. Continue only when `authenticated` is true and the token is unexpired. The explicit update check is the only exception.

Validate every argument before invoking the CLI; never use the CLI itself as a validator:

- A calendar-month value must match `YYYY-MM`, with month `01..12`.
- A calendar-date value must match `YYYY-MM-DD` and be a real date. Request logs also accept valid RFC3339 timestamps.
- Require `from <= to`, positive integer page values, and the command-specific limits below.
- Require enum values to match the documented lowercase values exactly.

Reject an invalid value without starting a command. Affected CLI versions can silently replace or clamp invalid input, return a false empty result, or exhaust memory on an invalid month. After a successful query, compare returned period, pagination, filter, and granularity fields with the request whenever those fields are present. If they differ, do not present the response as the requested result.

## Output Modes

For normal work, pass `--format json`, parse the structured response, and present only the relevant human-readable result. Never dump raw JSON or parse table/card output programmatically.

Use `--format text` only when the user explicitly requests plaintext. Preserve the returned block exactly, including alignment, spacing, progress bars, and separators. Put any optional analysis after the block, separated with `---`.

Without an explicit format, TTY output is command-specific human-readable output such as a table or card, while piped output is JSON.

## Command Map

| Intent | Command |
|---|---|
| Authentication status/login/logout | `qwencloud auth status`, `qwencloud auth login`, `qwencloud auth logout` |
| Aggregate usage | `qwencloud usage summary` |
| Per-model PAYG usage | `qwencloud usage breakdown` |
| Free-tier quota | `qwencloud usage free-tier` |
| PAYG usage | `qwencloud usage payg` |
| Request history, failures, latency, or request ID | `qwencloud usage logs` |
| Billing cycles | `qwencloud billing summary` |
| Cost ranking or per-key consumption | `qwencloud billing breakdown` |
| PAYG spending limit and alert configuration | `qwencloud billing limit` |
| Token/Coding Plan status | `qwencloud subscription status` |
| Subscription order history | `qwencloud subscription orders` |
| Token Plan Team summary | `qwencloud subscription tokenplan status` |
| Token Plan Team seats | `qwencloud subscription tokenplan seats` |

## Authentication

Check status first:

```bash
qwencloud auth status --format json
```

If already authenticated and unexpired, continue without logging in again.

For a non-TTY or headless login, initialize once:

```bash
qwencloud auth login --init-only --format json
```

Parse the stdout JSON `events` array. For a `device_code` event, present and open the returned `verification_url` with the appropriate platform command:

```bash
open "$VERIFICATION_URL"          # macOS
xdg-open "$VERIFICATION_URL"      # Linux
start "" "$VERIFICATION_URL"      # Windows
```

Immediately start the completion phase; do not wait for the user to confirm authorization:

```bash
qwencloud auth login --complete --format json
```

Keep polling through this flow on `pending`. On `expired`, restart from initialization; on `error`, report the failure. Never run initialization again while the current device code is pending because that invalidates the open authorization page.

In an interactive TTY, use:

```bash
qwencloud auth login
```

Logout is destructive to the current session. Obtain explicit confirmation before running:

```bash
qwencloud auth logout
```

## Usage

Aggregate usage:

```bash
qwencloud usage summary --format json
qwencloud usage summary --period last-month --format json
qwencloud usage summary --from 2026-03-01 --to 2026-03-31 --format json
```

Accepted period presets are `today`, `yesterday`, `week`, `month`, `last-month`, `quarter`, and `year`; a validated `YYYY-MM` is also accepted.

Free Tier quota (complete model list):

```bash
qwencloud usage free-tier --format json
qwencloud usage free-tier --period month --format json
```

The JSON response contains the full `free_tier[]` list. No top-N or pagination arguments are needed. When the user asks for all free-tier quotas, present every returned model and its quota details, including expired, exhausted, and unknown entries unless the user requested a filter.

To let the user view the full list directly in a terminal, provide:

```bash
qwencloud usage free-tier --format text
```

If the answer abbreviates the list, state how many models are shown out of the total, mark the result `partial`, and include this command or the complete JSON command above. Preserve any user-requested period/date filters in the supplied command. Agents still use JSON for normal queries; the text command is a user-facing way to view all rows.

Focused PAYG query:

```bash
qwencloud usage payg --days 7 --format json
```

The summary and Free Tier queries accept a period or explicit dates. The PAYG query also accepts a positive days value. Use only one date form in a query.

Per-model PAYG breakdown requires a model:

```bash
qwencloud usage breakdown --model qwen3.6-plus --days 7 --format json
qwencloud usage breakdown --model qwen3.5-plus --period 2026-03 --format json
qwencloud usage breakdown --model qwen-plus --period 2026-03 --granularity month --format json
qwencloud usage breakdown --model qwen3.5-plus --from 2026-01-01 --to 2026-03-31 --granularity quarter --format json
```

Use one date form: a validated month/preset, positive `--days`, or real explicit dates. Breakdown granularity is `day`, `month`, or `quarter`.

Request logs:

```bash
qwencloud usage logs --period 7d --page 1 --page-size 50 --format json
qwencloud usage logs --period 24h --status 4xx --status 5xx --page 1 --page-size 50 --format json
qwencloud usage logs --model qwen-plus --page 1 --page-size 50 --format json
qwencloud usage logs --from 2026-08-18 --to 2026-08-31 --page 1 --page-size 50 --format json
qwencloud usage logs --request-id 9f2c…a1bd --page 1 --page-size 50 --format json
```

- An exact `--request-id` lookup does not require a time range. Query it directly without adding `--from`, `--to`, or `--period`, and do not ask the user for a date or history range. Add time filters only if the user explicitly requests them; do not automatically search additional time windows for a request ID.
- For time-based history queries or explicitly requested time filters, use only the safe presets `1h`, `24h`, `7d`, `today`, `yesterday`, and `week`. Do not use `month`, `quarter`, or `year` because the resolved range may exceed 14 days.
- An explicit history range must resolve to at most 14 days per query. Split a longer user-requested history range into consecutive, non-overlapping windows of at most 14 days. This does not make a time range required for request-ID lookup.
- `--model` is repeatable. `--status` is repeatable and must be `0`, `2xx`, `4xx`, or `5xx`.
- `--request-id` overrides model and status. Omitting time arguments does not establish unlimited retention or coverage; describe the actual returned scope rather than inventing one.
- `--page` must be a positive integer. Always pass `--page-size` in `1..50`, normally 50, even though help advertises 100.

For each query (or each window of an explicitly requested history range), start at page 1 and verify the response echoes the requested page and page size. Accumulate items and increment the page while `page × pageSize < totalCount`. Verify that both the collected-item count and unique-request-ID count equal `totalCount`; otherwise classify the result as `partial`.

Never initiate a log query with page size 51..100. If a prior or user-supplied query in that range returned empty, repeat the entire query from page 1 with page size 50 before interpreting it. For an empty request-ID lookup, say that the query returned no matching log and report its period if supplied; never make a global nonexistence claim. Apply the coverage limits in [usage.md](usage.md) before classifying a log result as empty.

## Billing

Billing-cycle summary:

```bash
qwencloud billing summary --format json
qwencloud billing summary --from 2026-07 --format json
qwencloud billing summary --from 2026-07 --to 2026-08 --format json
```

Each supplied `--from` or `--to` value must be a validated `YYYY-MM`. Supplying neither option or only one option is valid; require `from <= to` only when both are present. `--charge-type` is `all`, `subscription`, or `payg`. Do not pass a day value such as `2026-07-01`. Require the returned period to match the intended range after defaults are resolved.

Cost breakdown:

```bash
qwencloud billing breakdown --period month --group-by model --top 20 --format json
qwencloud billing breakdown --from 2026-08-01 --to 2026-08-31 --granularity month --group-by model --top 20 --format json
```

`--granularity` is `day` or `month`; `--group-by` is `model` or `api-key`; `--charge-type` is `all`, `subscription`, or `payg`. `--top` must be an integer in `1..20` and defaults to 10. If the user requests more than 20, use 20, explain the limit, and classify the result as `partial`. Before classifying any empty breakdown queried with an omitted or non-20 top value, repeat the same filters with `--top 20`.

Do not combine an explicit granularity with a period preset. Use a preset alone and let the client choose the compatible granularity, or use explicit dates with the desired granularity. Keep an explicit day-granularity range within 31 days and an explicit month-granularity range within 12 calendar months.

The spending-limit query is read-only:

```bash
qwencloud billing limit --format json
```

## Subscriptions

Aggregate or plan-focused status:

```bash
qwencloud subscription status --plan token --format json
qwencloud subscription status --format json
qwencloud subscription status --plan coding --format json
```

`--plan` must be `token` or `coding` when supplied.

Order history:

```bash
qwencloud subscription orders --page 1 --page-size 20 --format json
```

Dates must be real and ordered; `--type` must be `purchase`, `renew`, or `upgrade`; `--page` must be at least 1; `--page-size` must be in `1..100`. Verify the response pagination and fetch all required pages.

Team seat summary and instances:

```bash
qwencloud subscription tokenplan status --format json
qwencloud subscription tokenplan seats --page 1 --page-size 20 --format json
```

For seat instances, `--spec-type` must be `pro` or `standard`, `--page` must be at least 1, and `--page-size` must be in `1..100`. Verify returned page and filter fields, then fetch pages until `current × size >= total`. An unfinished traversal is `partial`.

## Exit Handling and Updates

Prefer the structured error payload over the numeric exit code because affected versions do not map every transport, authentication, and argument failure consistently. Known exit codes are: 0 success, 1 general/usage error, 2 authentication error, 3 network error, 4 configuration/argument error, and 130 interruption.

Only when the user explicitly asks about CLI updates or versions, run:

```bash
qwencloud version --check
```
