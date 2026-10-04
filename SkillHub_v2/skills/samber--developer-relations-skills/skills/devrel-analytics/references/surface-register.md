# Surface register

One row per surface in the tracking plan. Fill owner, data source, retention, bias and collection recipe before writing a single event.

## Contents

- [The register table](#the-register-table)
- [Docs, blog and marketing site](#docs-blog-and-marketing-site)
- [Repositories](#repositories)
- [Package registries](#package-registries)
- [Artifact and connector hubs](#artifact-and-connector-hubs)
- [Community venues](#community-venues)
- [Off-web surfaces](#off-web-surfaces)
- [Product and CLI](#product-and-cli)
- [The account roll-up (B2B) versus the individual motion (B2C-shaped)](#the-account-roll-up-b2b-versus-the-individual-motion-b2c-shaped)

## The register table

| Surface                         | Source that exists                                                                           | Retention                                                                                                                               | Baked-in bias                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Docs / blog / marketing site    | client event collection, server or CDN logs, search-console-class data                       | your tool's setting; search console data commonly 16 months                                                                             | client collection under-counts developers heavily                                    |
| Repository                      | forge traffic endpoints (views, clones, referrers, popular paths), git history, issue/PR API | **14 days** on traffic endpoints, and only for repos you hold write access to                                                           | clones include CI and mirrors; stars only ever go up                                 |
| Package registry                | registry download API                                                                        | npm: 18 months, 365 days for bulk queries, 7 days per version; PyPI: 180 days of time series, longer only via its public data warehouse | see the two definitions below                                                        |
| Artifact / connector hub        | hub API fields (downloads, likes, installs), or a paid publisher-analytics export            | full history on the paid export of one major hub; the public API returns current totals, not series                                     | every hub defines "download" differently, and the default counts deduplicate nothing |
| Community venue                 | venue analytics panel or export API                                                          | free plans cap message history                                                                                                          | bots, staff accounts and duplicate identities inflate every count                    |
| Talks, podcasts, print, hallway | nothing automatic                                                                            | n/a                                                                                                                                     | invisible unless you plant a vanity URL, a short link or a self-reported field       |
| Product / CLI / SDK             | your own event stream, API request logs                                                      | yours                                                                                                                                   | the only surface that proves behaviour changed; usually owned by another team        |

Sources for the retention figures: the forge's REST metrics/traffic documentation, and each registry's own stats documentation. Re-check them when the plan is revised - they change without notice.

## Docs, blog and marketing site

Collect: page view with a `section` property (`docs`, `reference`, `blog`, `marketing`), `docs_search_performed` with `zero_results`, `sample_copied`, quickstart step events, outbound clicks to the repository and to signup.

Do not collect: scroll depth on reference pages, time-on-page as a quality signal. Reference pages are scanned, not read; both metrics report the opposite of what they seem to.

Search-console-class data is the only source that sees the real queries reaching a docs site. Segment it by path prefix - a sitewide average hides that reference pages earn impressions and no clicks while guides earn the reverse.

ReadMe's own Developer Dashboard product binds this to the API side directly: a per-language Metrics SDK sits as request/response middleware on the API server, forwarding request/response details (with optional redaction of private fields) to build a per-developer API log, while the same system exposes per-page doc view counts, the top search terms typed into docs search, and a per-page "was this helpful" score. ReadMe frames "Time to First Call" as the north-star metric this instrumentation optimizes toward - the API-side equivalent of the time-to-first-success events this register already recommends for a quickstart.

## Repositories

Collect daily via the traffic endpoints and append to your own store: unique visitors, unique cloners, top referrers, top paths. Add from the issue/PR API: first-time contributor count, time to first response, open-to-close ratio, external pull requests merged.

Traps:

- The 14-day window means a monthly export loses half the data. Schedule daily.
- Clones are not people; CI clones on every build.
- Stars are monotonic and gameable. Convert to stars-per-period if you report them at all, and never as a headline.
- Referrers into a repository are mostly stripped, exactly like web referrers.

Sample and template repositories have no instrumentation pattern of their own; no dedicated named framework exists for sample-app telemetry (forks, clones, template-repo usage). Read the same traffic endpoints, stars-per-period and clone counts as any other repository row - forks are the one signal specific to a template repo, and inherit the same CI/mirror-inflation trap as clones.

## Package registries

A registry's counting policy is a published property of that platform, not a vendor feature, so the two dominant ones are named here - an unnamed retention figure cannot be acted on. Read whichever registry the product actually ships on; the pattern generalises, the numbers do not.

- **npm** counts "the number of HTTP 200 responses we served that were tarball files". Build servers, mirrors and analysis bots are all counted deliberately; npm's own guidance is that below roughly 50 downloads/day the signal is mostly automation. It is a request count, not a person count.
- **PyPI** excludes known mirrors by default and exposes with-mirrors and without-mirrors as separate series.

So an npm figure and a PyPI figure for the same product measure different things and must never be summed as "users". Report the trend of one registry against its own baseline. If the product ships on several, keep one series per registry, each with its definition written next to it.

## Artifact and connector hubs

A hub where the product ships as a model, dataset, connector, plugin or app is a fourth counting regime, not a variant of the package-registry one. Two rules decide everything you can say from it.

**The same hub can count two of its own surfaces incompatibly.** On Hugging Face, a model download is every HTTP `GET` or `HEAD` against a per-library query file - `config.json` by default - so a CI job that touches the file on every build counts every time, and self-contained formats such as GGUF double-count a whole-repository clone. A dataset download on the same hub is the opposite: every file one IP fetches from one repository inside a 5-minute window collapses to a single download. Model and dataset counts from that hub are therefore not summable and not comparable, and neither is comparable to a package registry.

**Unique downloaders are a paid feature, not a default.** The hub's own organisation dashboard states its figures are "not deduplicated by user"; request-level logs carrying a hashed user or IP, country and user agent exist only as an add-on to the top enterprise tier. Until that is bought, no "how many people" question is answerable from the surface - only "how many requests".

Collect: per-artifact downloads, likes, and the hub's own trending or usability score where one exists; per-connector installs. Snapshot daily into your own store and report deltas - the public API returns current totals, not history, so a series you did not save is gone.

Traps:

- **Likes are not stars, and not downloads either.** On the ML hubs they are a recency signal that concentrates on new releases, while downloads concentrate on old dependencies. The hub's own published analysis calls treating either as a proxy for the other "the most common mistake we see in coverage of the Hub". Keep them as two series and label what each one means.
- **Trending scores are opaque.** They are exposed as an API sort key with no published formula and no stability guarantee. Usable as a snapshot observation, never as a tracked metric.
- **Polling is rate-limited per plan.** Limits are enforced over 5-minute fixed windows and differ by tier - an anonymous caller gets a fraction of what an authenticated one does. Always send a token; a collection job that silently starts 429-ing produces a flat line that reads as lost adoption.
- **Installs on a connector hub are not usage.** Hosts publish install counts and almost never publish uninstalls or active-workspace counts, so the number is monotonic by construction. Pair it with a first-party signal from the connector itself if you need to claim adoption.

## Community venues

Collect: monthly active members, messages by channel, questions asked versus questions answered, median time to first human response, share of answers written by non-staff, new-member retention at 7 and 30 days.

Four things break these numbers before you even read them:

- **Bots.** A welcome bot answering in four seconds makes time-to-first-response look excellent while no human ever replied. Keep an explicit bot list and filter at query time.
- **Identity.** The same person is a forge handle, a chat handle, a commit email and a forum account. Without a merge step, "unique contributors" is inflated and every concentration measure is wrong.
- **Retention caps.** A metric defined today may be uncomputable for last quarter. Snapshot monthly into your own store from day one.
- **Staff flag.** "Share of answers written by non-staff" and "moderator share of messages" separate a community from a support queue, and both need the flag.

## Off-web surfaces

There is no passive collection here. Plant one of these before the appearance, never after:

- A short, speakable vanity path per talk or episode - the only clean per-appearance click signal.
- A QR code per event resolving to a tagged URL.
- One self-reported source field at signup, short, with a stable answer list so quarters stay comparable.

Read these as a floor on the surface's contribution, never a total, and pair them with a branded-search or direct-traffic read over the 7-14 days after publication against the preceding baseline.

## Product and CLI

The product event stream is where enablement and behaviour-change claims are actually settled: activation, time to first success, second-project rate, cohort retention. Getting a devrel event into it usually means a negotiation with whoever owns it - budget for that, and settle on one shared `user_id` rather than a parallel devrel-only identity.

Stripe's own engineering blog describes a structural way to make that negotiation unnecessary: a canonical log line, one structured line per request per service, emitted asynchronously to the data warehouse, whose schema also powers the charts on Stripe's customer-facing Developer Dashboard. The observability pipeline and the enablement surface are the same pipeline there, not two a team has to keep in sync.

CLI and SDK telemetry is a separate decision with a real trust cost in developer audiences. If you propose it:

- Make it opt-out at minimum, with a visible first-run notice.
- Document exactly what is sent.
- Ship a documented environment variable to disable it.
- Never send code, paths, or arguments.

Next.js's own CLI telemetry documents that floor concretely: command invoked, framework version, OS, plugins, build duration/size, explicitly excluding anything that could carry secrets (env vars, paths, file contents, logs), disabled with one documented command. A stricter shape sits above the floor: Go's own toolchain telemetry (`golang.org/x/telemetry`) is opt-in, scoped to tools the Go team itself maintains, and only uploads counters approved through a public proposal process, with every result published back openly. That model trades reach for trust and costs real governance overhead - a proposal process and a review body - worth adopting only where that overhead already exists, not a bar every CLI needs to clear.

A telemetry surprise costs more community trust than the data is worth.

## The account roll-up (B2B) versus the individual motion (B2C-shaped)

- **Individual self-serve adoption**: the spine stops at `user_id`. Funnel views run person by person, and the success event is a product action.
- **Company buying**: every event must also carry `account_id`, resolved from the signup domain or the product's own org object. The buying decision, the renewal and the churn all live on the account, so a person-level-only plan cannot answer any question the funder asks.
- **Both at once** (the common devtool case): instrument person-level everywhere, roll up to account only where an org object genuinely exists, and never present an account-level rate computed from a partially resolved population without saying what share resolved.

An account-level touch record is also what an influenced-pipeline rule depends on. If the CRM cannot carry "this account had a devrel touch before this stage", that rule cannot be honestly reported - decide that here, before promising it.
