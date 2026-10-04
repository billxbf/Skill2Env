# Indexability, versioning and retirement

Contents: robots directives · AI and assistant crawlers · sitemaps per generator · sitemap size limits · preview and staging leakage · rendering · canonical rules platforms don't enforce · translations and hreflang validation · mirrored domains · retiring a version · generated reference trees.

## Table of Contents

- [Robots directives](#robots-directives)
- [AI and assistant crawlers](#ai-and-assistant-crawlers)
- [Sitemaps](#sitemaps)
- [Preview and staging leakage](#preview-and-staging-leakage)
- [Rendering](#rendering)
- [Version canonical postures](#version-canonical-postures)
- [Translations and hreflang validation](#translations-and-hreflang-validation)
- [Mirrored domains](#mirrored-domains)
- [Retiring a version](#retiring-a-version)
- [Generated reference trees](#generated-reference-trees)

## Robots directives

Supported as a `<meta name="robots">` tag or an `X-Robots-Tag` response header (the header is the only option for non-HTML files such as PDF exports or an OpenAPI JSON):

| Directive                                              | Effect                                                  |
| ------------------------------------------------------ | ------------------------------------------------------- |
| `noindex`                                              | keep the URL out of results                             |
| `nofollow`                                             | don't follow this page's links                          |
| `nosnippet` / `max-snippet:[n]`                        | suppress or cap the text snippet                        |
| `data-nosnippet` (HTML attribute)                      | exclude one block from the snippet                      |
| `max-image-preview:[setting]`, `max-video-preview:[n]` | cap media previews                                      |
| `noimageindex`, `notranslate`, `indexifembedded`       | narrower controls                                       |
| `unavailable_after:[date]`                             | drop after a date - fits a version with a published EOL |

The rule that costs docs teams the most: a URL disallowed in `robots.txt` is never crawled, so its `noindex` and its canonical are never read. Blocking `/v1/` in `robots.txt` leaves those URLs indexable as bare URLs forever. Allow the crawl and serve `noindex`, or redirect.

Never block CSS or JS in `robots.txt` - the renderer needs them.

## AI and assistant crawlers

Audit these per agent and report the cost of each rule. A single blanket rule against "AI bots" is the mistake to catch. Three categories behave differently and are usually served by different named agents:

| Category               | What it controls                                                              | Cost of blocking a docs site                                                       |
| ---------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Search-style discovery | whether the docs can be surfaced and quoted in an assistant's answer          | the docs disappear from the answers the company most wants to appear in            |
| User-directed fetch    | whether an assistant may fetch a page a user explicitly pasted or asked about | a developer asking their assistant about your docs gets nothing back               |
| Model training         | whether the content may be used to train a model                              | no search-visibility cost; this is a licensing and policy decision, not an SEO one |

Rules to apply rather than a name list, because vendors rename agents and add new ones:

- Read every `User-agent` block in `robots.txt` and resolve which category each named agent belongs to against that vendor's own current crawler documentation. Never infer the category from the name.
- Some crawler controls are explicitly scoped to non-search uses and have no effect on ordinary search inclusion; check each one's documented scope before reporting it as a visibility problem.
- Check the CDN, WAF or bot-management layer as well as `robots.txt`. Some platforms block AI crawlers by default for new sites, which produces a policy nobody in the docs team chose and nobody can find in the repository.
- `robots.txt`-family signals are honour-system: a compliant crawler obeys them, a non-compliant one is only stopped at the edge. Don't present a robots rule as enforcement.
- Machine-readable surfaces (`llms.txt`, markdown endpoints, published specs) are a publishing decision, not a ranking one. Nothing about them is a ranking or citation factor, and they must not duplicate the sitemap's job. Route that work to samber/developer-relations-skills@coding-agent-docs-optimization.

## Sitemaps

Where the sitemap comes from, per generator:

| Generator                   | Sitemap source                                                     |
| --------------------------- | ------------------------------------------------------------------ |
| MkDocs / Material           | built into `mkdocs build`                                          |
| Docusaurus                  | `@docusaurus/plugin-sitemap` (on by default in the classic preset) |
| Sphinx / Read the Docs      | `sphinx-sitemap` extension                                         |
| VitePress                   | `sitemap` key in `.vitepress/config.*`                             |
| Astro Starlight             | `@astrojs/sitemap`                                                 |
| Next.js / Nextra            | a `sitemap` route handler, or `next-sitemap`                       |
| Hugo                        | built in                                                           |
| Mintlify / GitBook / ReadMe | generated by the platform                                          |

The three recurring defects:

1. Every version is listed instead of the canonical one, so the sitemap contradicts the canonical tags.
2. URLs use the platform subdomain rather than the custom domain.
3. `lastmod` is the build timestamp, so every page looks edited on every deploy. Google only trusts `lastmod` when it is consistently accurate - wire it to the source file's last commit date, or omit it.

Google retired the sitemap ping endpoint in 2023. Submit through Search Console and let the crawler pick up changes.

Size limits come from the sitemaps.org protocol, which a large reference tree does reach:

- one sitemap file: no more than 50,000 URLs, under 50MB uncompressed (52,428,800 bytes)
- a sitemap index: no more than 50,000 sitemaps, under the same byte ceiling

Gzip is allowed, but the uncompressed size is what counts. Above either limit, split into an index - several generators emit one flat file regardless of page count and will breach the cap without warning.

## Preview and staging leakage

Branch previews, PR previews and staging hosts are the most common source of accidentally indexed docs. Managed platforms usually send `X-Robots-Tag: noindex` on preview URLs by default. Self-hosted preview environments and per-branch docs builds usually do not.

Verify with the actual response, not the platform's reputation:

```bash
curl -sI https://docs-pr-482.preview.example.com/ | grep -i x-robots-tag
```

If nothing comes back, add the header at the CDN or the server, and add the host to `robots.txt` only as a second layer - never as the only one, since a blocked page can still be indexed URL-only.

## Rendering

Test with JavaScript disabled and confirm the body text, the canonical link and the internal links are already in the HTML:

```bash
curl -s https://docs.example.com/guides/webhooks | grep -c "rel=\"canonical\""
```

Client-rendered docs shells, lazily hydrated page bodies, tab panels holding the per-language sample, and API explorers that fetch a spec at runtime all risk arriving after the render pass. Two related traps: content behind a tab or accordion is indexed but rarely the reason a page ranks, and a search widget that owns navigation leaves whole sections with no crawlable `<a href>` path.

## Version canonical postures

The three postures, their effort and their ranking are in `SKILL.md` Step 3, where the choice is actually made. Mixing them produces the conflicting signals Google resolves on its own. What follows are the two rules no platform enforces for you, whichever posture you picked:

- A canonical must point at a page that genuinely says the same thing. If the page was removed or rewritten between versions, redirect it to the nearest real equivalent instead; Google ignores a canonical to unrelated content.
- Ship an in-page banner ("You are reading v1.4; the current release is 3.0") whatever the posture. It fixes the human half of the problem, which the canonical does not.

## Translations and hreflang validation

Each locale self-canonicalizes and carries a full `hreflang` set including `x-default`. Canonicalizing `/fr/` to `/en/` deletes the French docs from search. The one exception worth `noindex`ing is unreviewed machine translation: it competes with the English page and satisfies nobody.

Requirements stated in Google's own localized-versions documentation - report a breach as a defect, not a suggestion:

| Rule           | Google's wording, condensed                                                         |
| -------------- | ----------------------------------------------------------------------------------- |
| Self-reference | each language version lists itself as well as all the others                        |
| Return links   | if page X links to page Y, Y must link back to X, or the annotations may be ignored |
| `x-default`    | the reserved value used when no other language/region matches the user's setting    |
| Code format    | ISO 639-1 language, optionally followed by an ISO 3166-1 Alpha 2 region             |
| Delivery       | HTML tags, HTTP headers and sitemap entries are equivalent; pick the convenient one |

Practitioner checks that Google does not state, but that catch real breakage - present them as heuristics:

- Keep `hreflang` on canonical URLs only; a page canonicalized elsewhere has its annotations discarded.
- Match protocol and trailing-slash form exactly across the set; a mismatch is a different URL.
- Prefer sitemap delivery for a locale × version tree, on `<head>` weight alone - hundreds of tags per page is an operational problem, not a ranking one.
- Emit the set for canonical versions only. Annotating archived versions creates members that are themselves canonicalized away.

Invalid values seen most often:

- `eng` (ISO 639-2)
- `jp` for Japanese (`ja`)
- `en-uk` (the region code is `GB`)
- `EU` or `UN` as a region
- `es-LA` for Latin America
- a region with no language prefix

`zh` is valid but ambiguous - use the ISO 15924 script subtag (`zh-Hans`, `zh-Hant`), which may itself carry a region (`zh-Hans-US`).

Regenerate the whole mesh whenever a locale is added or removed. Adding `/ja/` without updating `/fr/`'s alternates leaves `/fr/` advertising an incomplete set, which is a return-link failure for the new locale.

## Mirrored domains

Docs often resolve on both a platform host (`project.readthedocs.io`, `org.github.io`, `project.pages.dev`) and a custom domain. Choose the custom domain, canonical the platform host at it, redirect where the platform allows, and make the sitemap agree.

The `docs.example.com` vs `example.com/docs` question is a weaker, separate decision - a subfolder inherits the main domain's authority, a subdomain is easier to host independently. Treat it as infrastructure. Migrating an established docs site costs more than the difference is worth.

## Retiring a version

1. Decide the redirect target per page, not per tree: current equivalent → nearest equivalent → the version index. A blanket redirect of every old URL to the docs home is treated as a soft 404 and loses the page's history.
2. `301` where an equivalent exists; `410` only for content that is genuinely gone with no successor.
3. Keep the redirects for at least one major release cycle - external tutorials, cached answers and issue threads keep sending traffic long after the version dies.
4. Update the sitemap in the same deploy, or the sitemap keeps advertising URLs that now redirect.

## Generated reference trees

Auto-generated API/CLI reference produces thousands of thin, near-identical pages that are also the highest-intent pages on the site. Don't blanket-`noindex` them. What works instead:

- One page per resource or command, not per field or flag.
- One shared prose page with a language switcher rather than one URL per SDK language, unless the prose actually differs per language.
- Stable `id` anchors per symbol so a long page can earn anchor-level results and be linked from the product.
- A written description on the highest-traffic entries only; the rest can fall back to a generated one.
