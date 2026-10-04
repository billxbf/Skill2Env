# Variant Matrix Template

The variant matrix is the handoff artifact: one row per variant, complete enough that whoever launches the ads needs no follow-up questions. A matrix without version codes or tracking mapping is incomplete.

## ID scheme

Split the stable ID from the human name, so renaming never breaks tracking history.

- **ID**: `<angle>_<awareness>_<seq>_v<N>` - lowercase, underscores only, no spaces. Awareness codes: `ua` unaware, `pa` problem-aware, `sa` solution-aware, `pra` product-aware, `ma` most-aware. Example: `pain_pa_01_v1`.
- **Name**: a short human label, e.g. "Chasing invoices pain". Free to change; the ID never changes.
- **Version**: `v1` is the first shipped wording of an angle; `v2`, `v3` are wording iterations of that same angle after it wins - never new angles. A new angle gets a new ID at `v1`.
- Mirror the full ID into the ad name and the click-tracking field (e.g. the content parameter) exactly as written. Case differences and mixed separators split one variant's results into multiple reporting rows - lowercase everything, one separator, and have one person approve any new tracking value before launch.

## Columns

| Column          | What goes in it                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ID              | Stable ID per the scheme above                                                                                                                   |
| Name            | Human label                                                                                                                                      |
| Angle           | One of the taxonomy families, plus the argument in one sentence                                                                                  |
| Awareness stage | One of the five                                                                                                                                  |
| Formula         | PAS / BAB / AIDA / 4 Us headline / other - the structure applied                                                                                 |
| Headline        | The copy, within the user-confirmed limit                                                                                                        |
| Primary text    | The copy; mark where the fold/clip lands                                                                                                         |
| Description     | The copy, or "n/a" where the surface has none                                                                                                    |
| CTA             | The chosen label from the platform's fixed list, or freeform where allowed                                                                       |
| Hypothesis      | One line: "Because [evidence], we believe [this angle] will [outcome] for [audience]"                                                            |
| Evidence source | Where each proof point traces to - review link, case-study figure, call note; `none - proof-free` when the variant deliberately carries no claim |
| Surface(s)      | Which placement(s) this row is written for                                                                                                       |
| Gate            | 6/6 pass record, with date                                                                                                                       |
| Status          | draft / shipped / winner / retired                                                                                                               |

## Asset-pool sheet

On pool surfaces (the platform assembles combinations), replace the single headline/description cells with a bucketed asset list per variant-angle:

```
Angle: mechanism_sa_02_v1
  Headlines (bucket: mechanism)   1. ... 2. ... 3. ...
  Headlines (bucket: proof)       4. ... 5. ...
  Headlines (bucket: cta)         6. ...
  Descriptions                    1. ... 2. ...
```

Buckets keep the pool varied across themes and non-duplicative within them. Every asset still traces to the matrix row's evidence and passes the gate individually.

## Handoff block

Close the matrix with:

- The naming/tracking glossary used (separator, casing, awareness codes) - kept with the matrix, not in a separate document.
- The destination page each variant was matched against, with its headline as pasted by the user on the match date.
- Rejected angles and the reason, as the seed of the next round.
- A pointer to the test design owner: sizing, duration, and success criteria are decided in `mbfinotti/advertising-skills@ad-creative-test-plan`, not here.
