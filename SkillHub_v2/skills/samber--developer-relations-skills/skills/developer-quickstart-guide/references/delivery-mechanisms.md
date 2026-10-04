# Delivery mechanisms

A quickstart's content and its container are separate decisions. Pick the content first; then walk the ranked containers below from the top and stop at the first one that removes the friction actually breaking your budget.

## Contents

- Choosing a container
- Language and platform tabs
- Embedded browser sandboxes
- API try-it consoles
- Notebooks
- CLI scaffolding
- What every non-page container still owes you

## Choosing a container

Rows run best-ratio-first: friction removed per hour of building the container and holding it working.

| Container        | Friction it removes                                | Build and upkeep                                                                             | Reach for it when                                                          |
| ---------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Plain docs page  | None beyond the words                              | Near-zero - it breaks only when the commands do                                              | Default. Always, and especially when the reader's own machine is the point |
| CLI scaffold     | Install and project-setup steps, outright          | An hour to document; the generator is owned by product either way                            | "Start a new project" is the real onboarding path                          |
| Try-it console   | The client setup between reader and first response | Near-zero when an OpenAPI spec is already published; a standing job to keep the spec current | The success moment is a response from a hosted API                         |
| Language tabs    | Re-reading the path in the wrong language          | An hour to wire, then every tab is a quickstart you must cold-run each release               | Two or three genuine first-class languages, no more                        |
| Notebook         | Install, and the gap between narrative and a chart | A week: its own hosting, execution and rendering story                                       | The success moment is a chart, a table or a query result                   |
| Embedded sandbox | The whole toolchain install                        | A standing job: a third-party runtime becomes a dependency of your onboarding                | Toolchain install is the single biggest time sink in the budget            |

- value: embedded sandbox > CLI scaffold > notebook > try-it console > language tabs > plain page
- build and upkeep effort: embedded sandbox > notebook > language tabs > try-it console > CLI scaffold > plain page
- compliance cost: embedded sandbox > notebook > try-it console > language tabs == CLI scaffold == plain page
- efficiency: plain page > CLI scaffold > try-it console > language tabs > notebook > embedded sandbox

Compliance cost belongs on this menu because three containers execute the reader's code, and sometimes their credentials, on a third party's infrastructure. An enterprise reader's security review, and any data-residency commitment you have made, gate the sandbox and the hosted notebook runner before the reader ever loads them. Tabs, scaffolds and the page itself trigger no review and are reversible in a commit, which is why they tie.

The last three rows tie on compliance cost for the same reason and nothing else; they differ sharply on effort, so never read that tie as equivalence.

**Default: the plain page.** Move up exactly one rung when a measured cold run shows the friction that rung removes is what breaks the budget - not because the rung looks impressive in a launch.

That order starves the embedded sandbox: the container that removes the most friction loses every round on effort. Promote it anyway when the toolchain install alone exceeds the time budget, or when the reader cannot install anything on a locked-down machine.

Delete the sandbox and the notebook from the shortlist, rather than leaving them at the bottom, whenever the interview named no owner for the container or a security review the team will not clear. A container nobody maintains fails in front of the reader on their first visit.

This ranking is a default, not a law: it shifts with what the team already runs.

- An OpenAPI spec already published promotes the try-it console.
- A docs framework with a working tab group promotes tabs.
- An in-house sandbox the platform team already maintains for something else moves the sandbox from a standing job to near-free, and straight to the top.

No published selection framework was found for this decision; the ordering and the fit column follow from what each container structurally can and cannot do, and from what each one costs to keep alive. Say so if you present it as guidance.

## Language and platform tabs

A language switcher looks like branching but is not. It renders one path in parallel variants; the reader picks once, and nothing downstream forks on a variable.

- Implement it as tab components wrapping the blocks that diverge, at the exact point of divergence.
- Synchronize every tab group on the page through a shared group identifier, so choosing Python once switches all remaining blocks and persists across visits. Docs frameworks that support this (Docusaurus's `groupId` being the reference implementation) also keep groups with different identifiers independent.
- Real branching (for example, "if you're behind a proxy, do X, otherwise Y") is not a tab. That is a how-to guide's job.
- Every tab is its own quickstart sharing a layout. Cold-run each one. An unverified tab is worse than a missing one, because the reader trusts it identically.
- More than two or three tabs is a signal, not a feature: the page is trying to serve audiences that want different success moments. Consider separate pages.

## Embedded browser sandboxes

Useful when installing the toolchain is the single biggest time sink in the path.

- Browser-native runtimes (StackBlitz's WebContainers) boot a development environment inside the tab itself, client-side, with no server round-trip per action.
- Hosted sandbox VMs (CodeSandbox and its embeddable Sandpack component) suit examples that need a real backend process rather than pure client-side execution.
- Terminal-scenario platforms (Instruqt) sandbox a full CLI or infrastructure environment instead of a JS runtime, reaching the CLI, database and self-hosted infrastructure product classes a browser-native JS sandbox cannot.
- Shared tradeoff: the reader's environment is the vendor's, not theirs. A green run in a sandbox does not prove the page works on a real machine, so keep at least one real-machine pass in the cold-run protocol.
- Second tradeoff: the sandbox is now a dependency of your onboarding. Decide what the page does when it is down or blocked by the reader's network.

## API try-it consoles

- A console generated from an OpenAPI specification lets the reader call the live API from the docs page with no authoring cost beyond keeping the spec current.
- It shows exactly the operations in the spec, so it cannot demonstrate a multi-step flow or client-library ergonomics - retries, pagination helpers, typed responses. Those still need written steps.
- Use it beside the quickstart, not instead of it: the console proves the endpoint exists; the quickstart proves the reader can build with it.

## Notebooks

- A notebook interleaves narrative and executable cells in one linear document, which matches a quickstart's single happy path closely.
- Best fit when the success moment is a chart, a table or a query result rather than a terminal line.
- Cost: notebooks render poorly as static docs pages and need their own hosting and execution story. Zero-install hosted runners exist and are widely used for this, but treat the specific pairing as an implementation choice to verify, not a given.

## CLI scaffolding

A generator (`npm create <name>`, `cargo new`, and their equivalents) is a different delivery mechanism, not a shorter page. One command emits a project that already runs.

- It deletes the "install dependencies" and "create project structure" steps outright - the generator's prompts _are_ those steps - and it moves the success moment earlier.
- Copy-paste hazards mostly vanish: there is no command to mistype, only prompts to answer.
- Support both modes the way established generators do: a non-interactive flag for the experienced reader who wants zero friction, and a guided prompt path for the newcomer.
- It cannot replace the page. A skeleton is not the product's value; the reader still needs to be told what to do with the running scaffold to reach the real success moment.
- It only fits products where "start a new project" is the primary onboarding path. For a hosted API, an existing codebase, or a SaaS dashboard there is nothing to scaffold.

## What every non-page container still owes you

Whatever the container, the pass threshold does not change:

- Commands run verbatim.
- Output matches.
- No prerequisite appears mid-run.
- The budget holds.
- The reader never leaves to finish.

A sandbox that satisfies four of five has moved the friction, not removed it.
