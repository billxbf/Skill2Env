# Page signals: titles, descriptions, headings, links, structured data

Contents: title templates · worked title examples · descriptions and snippet controls · headings and anchors · internal linking · structured data status · cannibalization.

## Title templates

On a docs site the title is generated, so fix the template once and every page inherits it. Find it in the generator config:

| Generator  | Title config                          |
| ---------- | ------------------------------------- |
| MkDocs     | `site_name` plus a theme title format |
| Docusaurus | `titleDelimiter`/`title`              |
| VitePress  | `titleTemplate`                       |
| Starlight  | `title`                               |
| Sphinx     | `html_title`                          |
| Mintlify   | `name` field in `docs.json`           |

Target shape: `{specific task or symbol} | {product} {section}` - the searched term first, the brand last, nothing between them.

| Weak                                          | Strong                                 | Why                                                               |
| --------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------- |
| `Documentation - Guides - Webhooks - Sending` | `Send a webhook \| Acme Docs`          | breadcrumb-as-title puts the query term fourth                    |
| `Acme Docs` (every page)                      | one title per page                     | duplicate titles collapse in results                              |
| `createClient - API`                          | `createClient() \| Acme SDK Reference` | the query is the exact symbol, parentheses included               |
| `Webhooks (v2.3.1)`                           | `Send a webhook \| Acme Docs`          | patch version in the title dates the snippet and burns characters |
| `Everything you need to know about webhooks`  | `Send a webhook \| Acme Docs`          | blog voice on a task page                                         |

Include the version only when versions are separately indexable.

### Length and rewriting: what the rule actually is

Google states there is no limit on how long a `<title>` element can be - the title link is truncated in search results as needed, typically to fit the device width. So 50-60 characters is a linting proxy for "does the important part survive truncation", never a pass/fail gate.

Rewriting is the separate problem, and the one that matters on docs sites. Google may build its own title link from:

- the visible page title
- heading elements
- `og:title`
- prominent styled text
- other page text
- anchor text in links pointing at the page
- `WebSite` structured data

Its stated trigger is having "detected an issue on the page", such as a boilerplate or breadcrumb-shaped title. The remedy is to make the template's shape informative. Trimming characters changes nothing.

The negative example this replaces, because it is the most tempting wrong fix:

| Wrong fix                                                      | What actually happened                                                                                          | Right fix                                                                   |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| a script shortening 400 titles to 60 characters                | Google was rewriting the title link because every title read `Docs - Guides - …` - not because titles were long | change the generator's title template so the page's own subject comes first |
| adding the product name to every `h1` to "reinforce the brand" | the `h1` stopped describing the page, giving the rewriter one more unhelpful source                             | leave the brand in the title template and keep the `h1` about the task      |

## Descriptions and snippets

A meta description is not a ranking factor and Google rewrites most of them, but a written one still wins wherever the page opens with boilerplate - which on a generated reference page it always does.

Write descriptions for the pages that matter (quickstart, top how-tos, top reference entries) and let the rest fall back. One sentence, states the task and the outcome:

| Weak                                                                                    | Strong                                                                                              |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| "This page contains documentation for the webhooks functionality of the Acme platform." | "Register a webhook endpoint, verify the signature, and retry failed deliveries with the Acme API." |

Snippet controls worth knowing: `max-snippet:[n]` caps the length, and the `data-nosnippet` attribute keeps a specific block - a deprecation banner, a legal notice, a breadcrumb rendered into the body - out of the snippet.

The strongest snippet lever is not a tag: make the first screen answer the query. A "Acme is a platform that…" preamble on every page produces identical, useless snippets sitewide.

## Headings and anchors

- One descriptive primary heading per page, matching the page's job, not the site's name. A second valid `h1` is not by itself a defect - the question is whether the primary heading is descriptive and the hierarchy unambiguous, so don't spend a fix-list row on it while the page's real problem is a generated title.
- Heading levels descend without skipping; generated reference pages often emit `h1` → `h4`.
- Every heading gets a stable `id`, kept stable across builds - anchor-level results and product deep-links both depend on it. Renaming an anchor silently breaks every link and cached answer pointing at it.
- On long reference pages, the symbol is the heading. `## createClient(options)` beats `## Creating a client`.

## Internal linking

Docs sites fail on internal linking in a shape general SEO advice misses: navigation links exist everywhere, contextual links almost nowhere. The nav gives every page the same undifferentiated link, so it can't signal which page matters.

Work in this order:

1. **Orphans** - pages with no inbound link from any other page. The crawl script reports these. Every one is either linked from somewhere or deleted.
2. **Dead ends** - pages with no onward link. A reference entry that never links to the how-to that uses it ends the session.
3. **Contextual links from high-traffic pages** - the quickstart, the top three how-tos and the index pages are the ones with authority to pass. Link from them, in prose, with descriptive anchor text.
4. **Cross-mode links** - tutorial → reference for the symbols it used, reference → how-to for the task it serves, troubleshooting → the guide where the failure happens.
5. **Breadcrumbs** - real ones, matching the URL path, with `BreadcrumbList` markup.

Anchor text: `retry failed webhook deliveries`, never `here`, `this page`, or `read more`. Generated "Next/Previous" pagination links are not contextual links and don't substitute for them.

## Structured data: what still pays on a docs site

| Type                                   | Status                                                                          | Verdict                               |
| -------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------- |
| `HowTo`                                | rich result removed by Google in August 2023, documentation deleted             | don't build                           |
| `FAQPage`                              | narrowed to government/health in 2023, stopped appearing entirely on 7 May 2026 | don't build                           |
| `BreadcrumbList`                       | still rendered                                                                  | worth it - docs have a real hierarchy |
| `SoftwareApplication` / `Organization` | product-level                                                                   | once, on the product pages            |
| `TechArticle` / `Article`              | no docs-specific rich result                                                    | harmless, low value                   |

Correct titles plus breadcrumbs beat a schema campaign on a docs site. A general SEO checklist that tells you to add HowTo or FAQPage markup is out of date.

## Cannibalization inside your own estate

A blog tutorial and a docs how-to targeting the same task split impressions and neither wins. Check with a site query per target task, then decide which surface owns it:

```
site:example.com "send a webhook"
```

Defensible default: the docs own task and reference queries, the blog owns narrative, benchmark and opinion queries. Make the loser link to the winner rather than deleting it - a blog post that opens with "the current reference is in the docs" keeps its backlinks and stops competing.
