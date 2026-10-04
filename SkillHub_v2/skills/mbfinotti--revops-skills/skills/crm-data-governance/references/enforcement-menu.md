# Enforcement Menu

Tool-agnostic mechanisms, ranked by value per unit of effort - not by how light they are. Value is data that is actually correct when a decision reads the field, never fields filled. Effort is admin build time, rep friction imposed, standing maintenance, and how hard the mechanism is to walk back.

- efficiency: `picklist > conditional-required > defaults > permissions > layout > hard-required`
- value: `conditional-required > picklist > permissions > defaults > layout > hard-required`
- effort: `hard-required > layout > permissions > conditional-required > picklist > defaults`
- compliance cost: `hard-required > permissions > picklist == defaults == layout == conditional-required`

- **Hard required leads the effort axis** despite near-zero build time: it is the mechanism reps route around, and the "n/a" habit outlives the rule that created it. Adding it costs an hour; removing it leaves a field full of junk nobody will re-collect.
- **Hard required also leads compliance cost**, through the same asymmetry: on a personal-data field, a mandatory gate compels collection the lawful basis may not cover, and the review that unwinds that is slower than the one that would have prevented it.
- **Per-role permissions rank second on compliance cost, in the opposite direction**: they are what a data-protection or financial-controls review asks to see, so building them buys sign-off instead of spending it.
- **The remaining four tie at the floor** (`==`) because none touches personal data or needs an approval.

1. **Restricted picklist over free text** - value: every read of the field stays interpretable and groupable, on every report and automation, forever. Effort: an hour of admin config, negative rep friction (picking beats typing), reversible by deactivating a value. Restricted is the default; open values need a stated reason. Retire values by deactivating, never deleting, so historical records keep their meaning. Prefer one shared, centrally-governed value set over per-field local lists when several fields need the same vocabulary.
2. **Conditional required-at-stage validation** - the workhorse. Value: the highest on the menu - presence guaranteed at the moment the value has meaning (the canonical case: loss reason required only when a deal moves to closed-lost). Effort: an hour of declarative build, friction charged only at the gate, and removable without residue because reps met it at one transition rather than every save.
3. **Default values** - value: correct wherever the common case genuinely dominates; below that it manufactures confident wrong values that read as filled. Effort: near-zero. A correct default beats an empty required field - but never use one to make a required field look satisfied.
4. **Per-role field edit permissions** - value: protects the authoritative writer's value from the second writer, which is the correctness property the whole system-of-record map depends on. Effort: an hour to set, then a standing job as roles, teams and integration users change. Structural constraint to know: a schema-required field typically cannot be independently permission-gated - required-ness and per-role securability conflict at the platform level.
5. **Layout scoping** - value: prevents wrong-hands edits and screen noise, but never makes a value correct. Effort: an hour each, multiplied by every layout, record type and stage the field appears on, and a standing job as those multiply. A field nobody should touch shouldn't be visible.
6. **Hard required** - value: guarantees non-blank and nothing more; the documented outcome is fill rate up, accuracy down. Effort: the menu's worst, per the effort axis above. Reserve it for fields where a record without the value is genuinely meaningless.

## Choosing the rung

Default: restricted picklists on every governed picklist field, plus defaults where the common case dominates, in the first pass. Climb to conditional required-at-stage for any field a decision reads at a known transition - forecast category at commit, loss reason at closed-lost, decision-maker at proposal.

What this order starves: per-role permissions and hard required. Both lose every efficiency round to config that costs an hour, yet both carry value the cheap rungs cannot buy:

- Permissions are the only mechanism that stops a second writer from overwriting the authoritative one. Promote permissions the moment a governed field has two writers and the system-of-record designation is being ignored in practice - the rule is only as real as the permission behind it.
- Hard required is the only mechanism that guarantees the record cannot exist without the value. Promote it only for a field whose absence makes the record undecidable.

A governance program that only ever picks the cheap rung ends up with a dictionary full of fields nobody trusts.

Delete, don't demote. A sales org that has already worked around required fields deletes hard required from the menu for rep-entered fields entirely; name it as deleted in the spec, because a rung parked at the bottom reappears as scope at the next escalation. A platform without declarative conditional validation deletes conditional required-at-stage - never substitute custom code for it.

Re-rank against what the Interview already established before applying the order:

- A CRM with strong native declarative validation collapses conditional required-at-stage to near-zero build and moves it above picklists.
- An admin who owns permission sets already moves permissions up two rungs.
- A team with no CRM admin at all drops everything except picklists and defaults.

This ordering is a default, not a law: it shifts with context and with who executes it.

## When required backfires

Practitioner debate is consistent on the failure mode: hard-required fields on busy users produce "n/a", punctuation, and plausible-looking junk that passes the gate - or workflow adoption collapses entirely. The rule: **reps are not the enforcement mechanism of last resort.** Their incentives push toward selling, not stewardship, and B2B teams "should never assume that someone within your sales team is going to help you in adding data" (Mazzalai).

If a required gate yields junk, the field needs an automated source (integration write, enrichment, default) or it shouldn't be required. "You can't delegate your way to a clean CRM. But you can build the automation." (RevOps Co-op)

## Optional integration note (vendor-specific)

Only when the user names their platform:

- **Salesforce**: restricted picklists and global value sets, validation rules (`ISPICKVAL` + `ISBLANK` for required-at-stage), field-level security, page layouts/record types, flow-set defaults.
- **HubSpot**: property validation, conditional property logic, stage-required properties on pipelines.

Map each menu item to the platform's native feature rather than building custom code.
