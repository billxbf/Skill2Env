# Standards-war framework (Shapiro & Varian)

Contents: [Source](#source) · [When it applies](#when-it-applies) · [Four battle types](#four-battle-types) · [Seven key assets](#seven-key-assets) · [Two tactics](#two-tactics) · [How wars end](#how-wars-end-and-why-to-price-a-truce-first) · [After winning](#after-winning) · [How to use it in a posture decision](#how-to-use-it-in-a-posture-decision) · [Worked classification](#worked-classification)

## Source

Carl Shapiro and Hal R. Varian, "The Art of Standards Wars", _California Management Review_, Vol. 41, No. 2, Winter 1999, pp. 8-32; adapted by the authors from _Information Rules: A Strategic Guide to the Network Economy_ (Harvard Business School Press, 1998). Every quotation below is from that article. Cite it by name - it is the canonical framework for this decision, and naming it saves you arguing the logic from first principles.

## When it applies

The framework governs "battles for market dominance between incompatible technologies" in markets with "strong _network effects_ that cause consumers to play high value on compatibility". Two consequences:

- No network effects, no standards war. A format nobody else has to agree with is a product decision, not a standards decision.
- Not every new technology triggers one. Sony and Philips "pooled together and openly licensed their CD patents"; they "were not in a battle with another new technology" because no rival incompatible technology was contesting the same adopters.

## Four battle types

Classify by which side offers backward compatibility with the technology already installed. "The critical distinguishing feature of the battle is the magnitude of the switching costs, or more generally the adoption costs, for each rival technology."

|                      | Rival compatible            | Rival incompatible          |
| -------------------- | --------------------------- | --------------------------- |
| **You compatible**   | Rival Evolutions            | Evolution versus Revolution |
| **You incompatible** | Revolution versus Evolution | Rival Revolutions           |

- **Evolution** strategy = "superior performance with minimal consumer switching or adoption costs".
- **Revolution** strategy = "such compelling performance that consumers are willing to incur significant switching or adoption costs".
- **Rival Evolutions**: DVD vs. Divx, the 56k modem battle, competing Unix flavours. Both sides read the old world; the fight is over features and allies.
- **Evolution versus Revolution**: includes "the important case of an upstart fighting against an established technology that is offering compatible upgrades".
- **Rival Revolutions**: Nintendo 64 vs. Sony PlayStation, AC vs. DC.

Read the table, not the prose: the article's text says "three distinct flavors" and then enumerates four cells.

## Seven key assets

"Your ability to successfully wage a standards war depends on your ownership of seven key assets":

1. control over an installed base of users
2. intellectual property rights
3. ability to innovate
4. first-mover advantages
5. manufacturing capabilities
6. strength in complements
7. brand name and reputation

Two qualifiers that do most of the work in practice:

- "No one asset is decisive." Atari's large installed base lost to Nintendo's superior technology; Sony and Philips controlled CDs but "could not move unilaterally into DVDs".
- "Don't forget that _customers_ as well as technology suppliers can control key assets, too. A big customer is automatically in 'control' of at least part of the installed base." A large adopter can therefore be recruited as a co-combatant, not just as a reference.

For a software or infrastructure vendor, assets 5 and 7 usually translate to operating cost per unit of scale and to whether developers already trust your specs.

## Two tactics

- **Preemption** - "build an early lead, so positive feedback works for you and against your rival." Its instruments are penetration pricing and, for zero-marginal-cost software, free or negative pricing. Three checks before giving it away:
  - do free users generate network externalities for paying ones
  - what is the installed base actually worth and when does the offsetting revenue arrive
  - are you falling for the "Winner's Curse"

  Note the constraint that bites open specs: "Penetration pricing may be difficult to implement if you are building a coalition around an 'open' standard", because no single supplier will fund the losses without a sponsor's control to recoup them.

- **Expectations management** - "The second key tactic in standards wars is the management of expectations." The legitimate form is "assembling allies and by making grand claims about your product's current or future popularity". The abusive form is vaporware, cited against Microsoft in the 1994 consent-decree ruling.

## How wars end, and why to price a truce first

"Standards wars can end in: a _truce_, as happened in 56k modems and color television where a common standard was ultimately adopted; a _duopoly_, as we see in video games today with Nintendo and Sony battling toe-to-toe: or a _fight to the death_, as with railroad gauges, AC versus DC electric power, and videotape players."

The truce argument, which is the sourced backing for proposing a merge instead of a feature race:

- "Before entering into a standards battle, would-be combatants are well-advised to consider a peaceful solution."
- "Unlike many other aspects of competition, where coordination among rivals would be branded as illegal collusion, declaring an early truce in a standards war can benefit consumers as well as vendors, and thus pass antitrust muster."
- "the more costly a battle is to both sides, the greater are the pressures to negotiate a truce; and one's strength in battle is an overriding consideration when meeting to conduct truce talks."

That last clause sets the sequencing: build the position first, then talk, because your assets are the currency at the table.

## After winning

- **Migration path**: "If you cannot improve your technology with time, while offering substantial compatibility with older versions, you will be overtaken sooner or later. Rigidity is death." The Minitel case is the article's illustration of harvesting an installed base by default rather than by decision.
- **Commoditize complements**: "Your goal should be to retain your franchise as the market leader, but have a vibrant and competitive market for complements to your product" - the same logic as the commoditization test in the main skill.
- **Preemption's hangover**: "Going early usually means making technical compromises, which gives that much more room for others to execute an incompatible Revolution strategy against you."

## How to use it in a posture decision

The framework describes the fight; the posture ladder decides whether to fight at all. Use it in two places only:

1. **The control test.** Score the seven assets honestly. A team holding none of them that still proposes Drive is choosing a war it cannot fund; the honest posture is Contribute.
2. **When a rival spec already exists.** Classify the battle first, because the type sets the tactic.
   - Rival Evolutions rewards allies and expectations management.
   - Rival Revolutions rewards preemption and raw performance.
   - Anything Evolution-versus-Revolution turns on whether your compatibility advantage outlasts their performance advantage.

Do not stretch it further. It is a 1999 framework about product markets with network effects; it says nothing about venue choice, IPR mode or conformance programmes, which the main skill covers through its own venue reference.

## Worked classification

A constructed scenario, not a documented case - it shows the classification mechanics, so do not cite it as precedent. A vendor publishes a new wire format for agent-to-tool calls. An incumbent framework ships its own format that also parses the older convention every existing integration uses; the vendor's does not.

- Rival is compatible with the installed technology, you are not → **Revolution versus Evolution**.
- Implication from the framework: you are asking adopters to pay switching costs the incumbent is not, so you need "such compelling performance" that they accept it. Absent that, the article's own reading is that the compatible side wins slowly by default.
- Asset check: you hold ability to innovate and brand among a niche; the incumbent holds installed base and complements. Four of seven against you.
- The conclusion the framework pushes toward is not "fight harder" - it is the truce: propose bridging both formats before either has enough adopters for a fight to the death to be worth funding.
