# Classifying documentation pages

## The compass

Two questions decide any page. Answer them about the page's _dominant_ content, not its title.

| If the content…   | …and serves the user's…      | …then it belongs to… |
| ----------------- | ---------------------------- | -------------------- |
| informs action    | acquisition of skill (study) | tutorial             |
| informs action    | application of skill (work)  | how-to guide         |
| informs cognition | application of skill (work)  | reference            |
| informs cognition | acquisition of skill (study) | explanation          |

Tie-breaker for reference versus explanation: would someone open this _while working_, or after stepping away from the work? Reference is consulted mid-task and is usually "boring and unmemorable"; explanation is read away from the keyboard.

Tie-breaker for tutorial versus how-to: does the page promise learning, or a finished task?

- A tutorial takes a beginner down one managed path in a contrived setting and guarantees success.
- A how-to assumes competence, forks on real-world variables, and hands responsibility to the reader.

## Acceptance criteria per mode

- **Tutorial**
  - One linear path, no branching, no alternatives.
  - Every command produces stated visible output.
  - No configuration menus.
  - No "why" digressions longer than a sentence.
  - Ends at a working artefact the reader built.
- **How-to guide**
  - Titled with the goal ("Rotate an API key", not "API keys").
  - Assumes prerequisites instead of teaching them.
  - Branches where reality branches.
  - May state its limits.
  - Does not explain the machinery it drives.
- **Reference**
  - Mirrors the shape of the product (one section per command/endpoint/setting/class).
  - Consistent field order.
  - Complete over readable.
  - Examples are illustrative one-liners, never walkthroughs.
  - No persuasion, no tutorials embedded.
- **Explanation**
  - Titled around a topic or question ("Why the scheduler retries", "Architecture overview").
  - Admits alternatives and trade-offs.
  - Safe to skip for someone mid-task.
  - Contains no required steps a reader must execute.

## Mixing symptoms and their fix

| Symptom in the page                                                 | What it really is                 | Default fix                                                                |
| ------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------- |
| Numbered steps followed by a full option table                      | how-to plus reference             | Move the table to reference, link to it                                    |
| Steps interrupted by three paragraphs of rationale                  | tutorial plus explanation         | Pull the rationale into an explanation page, leave one sentence and a link |
| "If you use Postgres, do X instead" inside a beginners' walkthrough | how-to wearing a tutorial's title | Split: keep one supported path in the tutorial, move variants to how-tos   |
| A how-to that starts at "install the CLI"                           | tutorial or quickstart            | Replace the setup block with a prerequisites line linking the quickstart   |
| API page with long narrative before the signature                   | reference plus explanation        | Cut the narrative to one sentence, link the concept page                   |
| "Concepts" page that ends with a setup procedure                    | explanation plus how-to           | Extract the procedure into its own how-to                                  |
| One page holding install, tour, API table and FAQ                   | all four                          | Split by mode first, worry about naming second                             |

Small crossings are normal and healthy; the mixing threshold is in SKILL.md Step 3.

## Worked examples

**Good classification.** Page `deploy-to-kubernetes.md`: title states a goal, assumes a running cluster, branches on ingress controller, no product tour, links to the Helm values table instead of restating it. Informs action, serves work → **how-to guide**, correctly placed under "Guides". No finding.

**Misplaced page.** Page `concepts/authentication.md`: a token-lifecycle diagram (explanation), eight numbered steps to rotate a key (how-to), then a table of every scope (reference). Three modes, three audiences, one URL. Finding: split into `concepts/authentication.md` (keep the lifecycle), `guides/rotate-an-api-key.md`, `reference/scopes.md`; nav gets the two new pages, the concept page keeps links to both.

**Negative example - over-classification.** Reporting "this reference page contains one explanatory sentence" as a finding. That sentence is doing its job. Reserve findings for pages where a reader arrives with one need and meets another.

## When the site already runs another taxonomy

- **DITA** (OASIS XML standard): base topic types are `concept` ("What is…?"), `task` ("How do I…?") and `reference` (specifications, commands, parameters, error codes). DITA 1.2 added `general-task` to ease migration of legacy content; 1.3 added `troubleshooting` and `glossentry`. Three Diátaxis quadrants map onto DITA types, but a Diátaxis tutorial has, in Tom Johnson's reading, "a different rhetorical shape tailored for education rather than solving problems". DITA has no direct equivalent, so a DITA site with no learning path is a real gap, not a mapping artefact.
- **Every Page is Page One** (Mark Baker): every topic must stand alone because any page can be the reader's first. Its seven characteristics:
  - Self-contained.
  - Specific and limited purpose.
  - Conform to a type.
  - Establish their context.
  - Assume a qualified reader.
  - Stay on one level.
  - Link richly.

  Baker explicitly rejects generic typing: "The type of an EPPO topic is not something generic like concept, task, or reference, but more specific and related to the specific subject matter." A maintainer who has read Baker and dropped generic types has a defensible position; audit their pages on self-containment and context-setting instead.

- **Microsoft Learn content types**: conceptual, how-to, tutorial, reference, quickstart, declared in front matter via `ms.topic`. Audit the declaration against the content - a mismatch is a machine-checkable finding.
- **The Good Docs Project templates** follow the Diátaxis types directly, so they combine with this audit rather than competing with it.
- **Single-type conventions slot inside a taxonomy, they do not replace one.** An ADR directory (`docs/adr/`, sequential numbering, immutable once accepted, superseded ADRs pointing forward) or a Standard Readme file is already correctly typed. Do not flag it for not fitting the four-quadrant split.

Two sourced cautions apply before recommending a taxonomy change:

- Practitioners converge on structure mattering more than which framework supplies it: a Markdown system with consistent templates plus a named framework reaches DITA's structural benefits "without the XML complexity".
- Taxonomy invention has a documented cost. Paligo records a team that "spent months debating a single new DITA topic type for 'troubleshooting' content… It was finally dropped entirely, and the team resorted to basic topic types with writing guidelines, achieving the same results without the XML complexity."

Sources: OASIS DITA 1.0/1.3 specifications; everypageispageone.com; idratherbewriting.com; learn.microsoft.com; thegooddocsproject.dev; Paligo; docsbydesign.com.

## Hard cases

- **Release notes / changelog**: reference (consulted at work, describes the machinery's history). Migration guides that walk through upgrading are how-to guides.
- **FAQ**: usually a symptom, not a mode - each entry belongs to a real mode. Keep the FAQ as an index if search is weak, and file the answers properly.
- **Glossary**: reference.
- **Troubleshooting / error pages**: how-to when they prescribe a fix, reference when they enumerate error codes. Split when both.
- **Auto-generated API docs**: reference by construction; audit their completeness and entry points, not their prose.
- **Tutorial series**: acceptable as long as each part keeps a single path and the series has one entry point.
- **Landing / index pages**: not a mode - judge them on whether they route to all four.
