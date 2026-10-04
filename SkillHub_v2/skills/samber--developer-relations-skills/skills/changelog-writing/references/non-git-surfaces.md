# Non-git surfaces

Four surfaces where the git-hosted templates do not apply, because each imposes caps, review, or machine consumers the repository does not. Read the section for the surface you are writing.

## Contents

- [Mobile app stores](#mobile-app-stores)
- [Enterprise and on-prem](#enterprise-and-on-prem)
- [Hosted APIs and cloud services](#hosted-apis-and-cloud-services)
- [Browser extensions](#browser-extensions)
- [Localization](#localization)

## Mobile app stores

| Constraint                       | Apple App Store              | Google Play                                        | Microsoft Store (MSI/EXE)       |
| -------------------------------- | ---------------------------- | -------------------------------------------------- | ------------------------------- |
| Field                            | "What's New in This Version" | "What's new in this release"                       | Release notes                   |
| Character limit                  | 4,000                        | 500 per language                                   | 1,500                           |
| Required                         | Yes, after the first version | No                                                 | Leave blank on first submission |
| Localization unit                | Per storefront               | Per Play Console locale, in language-tagged blocks | Not documented                  |
| Markdown / links                 | None; no clickable links     | None; URLs auto-linkified                          | Not documented                  |
| Version history visible to users | Yes                          | No, latest only                                    | Not documented                  |

The Google Play and Microsoft Store figures are verified against first-party documentation. Apple's 4,000-character limit is reported by third-party comparisons, not verified against Apple's own pages - flag it as such if a user relies on it.

Three rules follow from the table:

1. **The store text is a review criterion, not just copy.** Apple's guideline 2.3.12 requires apps to clearly describe new features and product changes; generic wording is acceptable only for pure bug-fix, security or performance updates. A vague "What's New" on a feature release is a rejection vector - this has no equivalent on any git surface.
2. **Write the 500-character version first, then expand.** Compressing 4,000 characters down to 500 degrades text far more than expanding 500 up to 4,000 - an inference from the caps, echoed by one secondary source, not a platform rule. Enforce the count mechanically; Play Console warns on overflow and API uploads fail outright, naming the offending language.
3. **Front-load the first sentence.** Roughly the first 170 characters render before the "more" fold (reported, not verified against Apple's documentation), so the single highest-impact change belongs there as a complete sentence.

Store notes are **locked at submission** - they ship with the binary and cannot be edited without a new version, which is why teams schedule the writing against the submission deadline rather than the merge date. Apple's Promotional Text (170 characters, editable without a new submission - reported, not verified against Apple's documentation) is the escape hatch for anything time-sensitive.

Use three coarse sections at most - New, Improved, Fixed, omitting empty ones. This follows the practice of existing store-notes tooling, not a platform requirement; the rationale is that a store reader will not parse six specification categories.

Evidence on whether any of this moves the needle: an analysis of 69,851 releases and 67.7M reviews across 2,232 top free Google Play apps found longer release notes and more frequent updates both correlate with higher average ratings (Yang, Hassan, Zou and Hassan, _Empirical Software Engineering_ 27:55, 2022). It is correlational and confounded by release frequency and app maturity - do not present it as a causal argument for writing more.

## Enterprise and on-prem

The reader may be many versions behind and may be reading the document as an input to a change-approval process rather than out of curiosity. That inverts the usual priorities:

- High value: stable identifiers, symptom phrasing, affected-version ranges, required-action statements.
- Negative value: narrative voice.

- **The unit of communication is often the advisory, not the entry.** Red Hat ships changes as individually numbered errata - security (RHSA), bug fix (RHBA), enhancement (RHEA) - drawn from one yearly numbering pool, with QE and management sign-off recorded as fields on the advisory itself.
- **Release notes become a structured, versioned document**, with chapters for new features, deprecated features, known issues, and asynchronous errata updates listing every subsequent patch release by advisory ID.
- **Entries carry upgrade preconditions.** "With advisory X, an in-place upgrade from 8.8 to 9.2 with FIPS mode enabled becomes possible" is a normal enterprise sentence; the identifier is part of the claim.
- **Advisories are machine-consumable.** Red Hat publishes CSAF JSON per advisory, ingested by vulnerability databases - the entry doubles as a security data feed.
- **Write fixes for diagnosis.** Microsoft's enterprise channel notes are long lists of "we fixed an issue that caused X" precisely so an administrator can match a symptom to a support ticket.
- **Lifecycle changes are themselves release-note events.** A change of support window or release cadence - HashiCorp's move to a twice-yearly enterprise cadence, for instance - is a category of note that fast-moving SaaS has no slot for.

## Hosted APIs and cloud services

Two architectures, both pushing the changelog toward being a machine artefact.

- **Version-derived.** Stripe generates its API changelog from version-change definitions, so it updates as services deploy. The precondition is versioning designed as a first-class concern - pinned per account, transmitted by request header - not a writing process. Where a project has that, argue for generation rather than authoring.
- **Feed-and-dataset.** Google Cloud publishes per-product release-notes pages with RSS feeds, a console-wide filterable view, and a public BigQuery dataset of release notes queryable with SQL. Practitioners build alerting pipelines on the dataset specifically because the feed HTML is painful to parse.

For a hosted API the changelog has machine consumers - monitoring pipelines, compliance reviews, coding agents - as well as human ones. **Stability of shape (dates, product names, categories) matters more than prose quality.**

A machine-readable channel is a deliverable, not a nice-to-have. No vendor has yet published a changelog designed primarily for agent consumption; if that shifts, the optimisation target moves from prose to schema.

## Browser extensions

The thinnest-documented surface, and mostly defined by an absence.

- **Chrome Web Store has no dedicated what's-new field.** Listing metadata covers title, description, screenshots, category and privacy policy.
- **Firefox AMO does have one**, per version, exposed in its API - with the quirk that the release-notes default locale is pinned to `en-US` regardless of the add-on's own default locale. Release pipelines can submit generated notes to it, alongside a separate notes-for-reviewers field: notes for Mozilla reviewers and notes for users are distinct artefacts.

Keep the canonical changelog outside the store - repository releases, or an in-extension "what's new" page opened on update - and treat any store field as a pointer. Users who disable auto-update do go looking for what changed before updating, and have filed issues when they could not find it.

## Localization

Platform mechanics bind this problem more than editorial theory does.

- Play is **per-language and hard-capped** at 500 characters, with a copy-from-previous-release action that carries translations forward - a time-saver and a staleness risk in equal measure.
- Apple serves localized notes by device language when a translation exists.
- English typically needs roughly **twice the characters of Korean or Japanese** for the same meaning, so English breaks the Play cap first even when every CJK version passes. Budget the reverse direction too: some target languages expand 30-40% over English (reported, unverified). The two figures point opposite ways because the direction depends on the target language; the discipline - budget for expansion in whichever direction applies - is the same.
- On overflow (reported practitioner guidance):
  1. Drop the lowest-impact items first.
  2. Group by feature.
  3. Cap each line at 3-4 items.
  4. Enforce the count in CI rather than by eye.
- Write for translation from the start - no idioms, no cultural references, no wordplay. Maintain a termbase, and give translators one internal owner to ask for context.
- Register is not universal. Formal address is the safe default in several markets (German _Sie_, French _vous_, Spanish _usted_, Russian _вы_, Dutch _u_, Italian _Lei_). Adapt idiom to a local equivalent; never translate it literally.

No first-party account of how any named company reviews _translated_ changelogs was found - who signs off on a locale, whether a locale reviewer can block a release. Treat governance claims in this area as unverified.
