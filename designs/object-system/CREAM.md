# The Cream Layer — cited YAML sources, rendered for humans

Every doc in this series cites live YAML files — GLANCEs, CARDs, CHARACTER sheets, lineage
references. YAML Jazz makes them readable, but a human skimming the series shouldn't have to
context-switch into eight files to follow the argument. This page renders each cited source as
prose, with a link to the live file (always authoritative — these digests are the cream, the
YAML is the milk).

Cited by: [SELF-AND-MOOLLM.md](SELF-AND-MOOLLM.md) ·
[LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md) ·
[YOUTRACKDB-VS-MOOLLM.md](YOUTRACKDB-VS-MOOLLM.md) ·
[LIVE-OBJECTS-EXAMPLES.md](LIVE-OBJECTS-EXAMPLES.md) · Index: [README.md](README.md)

---

## prototype — the Self philosophy as a skill

Source: [skills/prototype/GLANCE.yml](../../skills/prototype/GLANCE.yml) (deeper:
[CARD.yml](../../skills/prototype/CARD.yml) · [SKILL.md](../../skills/prototype/SKILL.md))

*"Objects clone from prototypes, not instances from classes."* Everything is concrete, nothing
is abstract; delegation, not inheritance; networks, not trees. The core distinction: class-based
means *instance of an abstract class*; prototype-based means *clone of a concrete object*.
Delegation worked example: `excalibur` inherits from `sword-prototype`, overrides `damage: 50`,
and delegates `type` up the chain to get `"weapon"`. Applies to any YAML: characters inherit
`skills/character`, rooms inherit `skills/room`, buffs inherit `skills/buff`. The anti-taxonomy
line quoted in [SELF-AND-MOOLLM](SELF-AND-MOOLLM.md#anti-taxonomy) is here: not
`Thing → Animal → Dog → Labrador` but `biscuit ←→ labrador-traits ←→ friendly-traits ←→ palm`.
Lineage credits Ungar & Smith (Self, 1987), Alan Kay, Brendan Eich.

## artifactory — the constructor that resolves "class AND instance"

Source: [skills/artifactory/GLANCE.yml](../../skills/artifactory/GLANCE.yml) (deeper:
[CARD.yml](../../skills/artifactory/CARD.yml) · [SKILL.md](../../skills/artifactory/SKILL.md))

*"The Engine of Creation. It builds, edits, and destroys — including itself."* The
general-purpose constructor: CREATE / EDIT / DESTROY / PERSIST / INSTANTIATE / COMMIT as one
composable operation set. Its `selfish_inheritance` section is the crispest statement of the
object model anywhere in the repo: prototype-based to the bone; INSTANTIATE = clone; skills are
traits objects; COMPOSE is multiple delegation; a prototype is a full object that's ALSO the
template — which resolves "class AND instance." Its cosmology section supplies the git story
used across this series: the filesystem is a snapshot of a universe-state, a commit freezes it,
the commit DAG is branching many-worlds time, and MERGE is the superpower physics lacks. Lineage:
von Neumann's universal constructor, Lem's Trurl & Klapaucius, PKD's Ubik and Autofac (the
anti-pattern), Drexler, Factorio, Spore, Papert.

## cauldron CARD — identity through location, and the patron

Source: [skills/cauldron/CARD.yml](../../skills/cauldron/CARD.yml) (deeper:
[META-PLAN.md](../../skills/cauldron/META-PLAN.md))

Two slots this series leans on. **`identity_through_location`**: "A cauldron instance's identity
is its directory. `docs/configuration/` IS the configuration-flags cauldron instance. Moving the
directory renames the instance. Copying it instantiates a sibling." — the Self identity model,
stated operationally. **`patron`**: The Weird Sisters (Macbeth), "practical, not parodic: the
cauldron produces dinner, not curses" — the canonical patron-as-prototype, a latent-space parent
that genuinely shapes behavior (Phase 1 really is chaotic-becoming-useful, and pretending
otherwise is why plans go bad).

## the-bartender CHARACTER — four traditions, one personality

Source:
[the-bartender/CHARACTER.yml](../../examples/adventure-4/characters/fictional/the-bartender/CHARACTER.yml)

The working example of multiple latent-space inheritance. The file opens with **ontological
inheritance** — `inherits: [skills/fictional, QUARK-DS9, JAMES-BAR-KARMA]` — and a `k-lines:`
list adding `GUINAN-TNG` and `SAM-CHEERS` ("every bartender is a little bit Sam Malone"). The
inheritance is *load-bearing*: the personality text says exactly what each parent contributes
("From QUARK: knows every angle, information has a price, neutral ground for all factions. From
JAMES: has been here longer than anyone remembers, helps souls at crossroads"). And the
character is theme-polymorphic — the same object re-resolves as Grim (classic adventure), Z-4RT
(space cantina), or Nyx (cyberpunk) while the invariant slots (knows everyone's secrets, always
here) persist. JAMES-BAR-KARMA is itself a double K-line: Bar Karma was the Will Wright + Don
Hopkins Current TV show.

## schema-mechanism — Drescher as a skill, grounded

Source: [skills/schema-mechanism/GLANCE.yml](../../skills/schema-mechanism/GLANCE.yml) (deeper:
[CARD.yml](../../skills/schema-mechanism/CARD.yml) ·
[SKILL.md](../../skills/schema-mechanism/SKILL.md))

*"Context → Action → Result."* Drescher's computational theory of causal learning as a MOOLLM
skill. Methods map his thesis vocabulary directly: MARGINAL_ATTRIBUTION (track correlations with
success/failure), SPIN_OFF (child schema with refined context), SYNTHESIZE_ITEM (invent a
hidden-state hypothesis), PLAN_DIJKSTRA (shortest schema path to goal). State: items with
ON/OFF/UNKNOWN, discovered schemas, extended context/result statistics. The
`moollm_extensions` block is the grounding argument in three lines — `symbol_grounding: "Items
mean something"`, `causal_reasoning: "Why patterns hold"`, `natural_explanation: "Communicate
discoveries"`. Lineage line: `Piaget → Minsky → Drescher → MOOLLM`. Credits include Henry
Minsky's `pyleela.brain`.

## drescher-lineage — the Piaget-to-Leela chain, with sources

Source:
[skills/leela-ai/reference/drescher-lineage.yml](../../skills/leela-ai/reference/drescher-lineage.yml)
(context: [skills/leela-ai/](../../skills/leela-ai/))

The reference document behind the
[Drescher section](SELF-AND-MOOLLM.md#the-drescher-lineage--schemas-and-the-grounding-that-finally-arrived).
Piaget: when an action applies, what result it has. Drescher at MIT under Minsky and Papert:
*Made-Up Minds* (1991) and *Genetic AI: Translating Piaget into Lisp* (1986); robot hand and
eye; schemas as Context → Action → Result with tracked reliability
(P(result | context, action) vs P(result | context, ¬action)); spinoffs when context
differentiates; synthetic items; chaining as planning. Henry Minsky's exposure as an MIT
student, reimplementation in the 1990s, and the Leela AI founding (Henry Minsky, Cyrus Shaoul,
Milan Minsky — *Leela*, Sanskrit for divine play). Leela's implementation: symbolic schema core
in Python/GPU, neurosymbolic loop (ConvNet perception → LeelaCore symbolic reasoning →
corrections and self-supervised samples), applied to manufacturing video intelligence.

## henry-minsky-blocksworld — the microworld data, worked

Source:
[skills/schema-factory/examples/henry-minsky-blocksworld.yml](../../skills/schema-factory/examples/henry-minsky-blocksworld.yml)
(context: [skills/schema-factory/](../../skills/schema-factory/))

Credits Henry Minsky (pyleela) and Drescher directly. Structured data from the blocks/hand/eye
microworld: sensorimotor items (`hand1-grasping`, `block1-visible`, `eye-at-home`, tactile and
visual-field cells) and schemas with evidence — e.g. `hand1-reach-block1`: action
`hand1_forward`, context `[block1-visible, hand1-at-home]`, result `[hand1-near-block1]`,
reliability 0.76 from 38 successes / 12 failures, with the honest note "reach is probabilistic:
proximity sensors are noisy." This is what the schema-factory lints, ingests, and composes —
the deterministic half of the hybrid, before LLM synthesis.

## soul-angel — the Soul City app object (external, MicropolisCore)

Sources:
[GLANCE.yml](https://github.com/SimHacker/MicropolisCore/blob/main/apps/soul-angel/GLANCE.yml) ·
[SOUL-ALBUM.yml](https://github.com/SimHacker/MicropolisCore/blob/main/apps/soul-angel/SOUL-ALBUM.yml) ·
[README.md](https://github.com/SimHacker/MicropolisCore/blob/main/apps/soul-angel/README.md)

The app directory cited in [LIVE-OBJECTS-EXAMPLES](LIVE-OBJECTS-EXAMPLES.md) — itself a
filesystem object with a GLANCE (read order: README → ARCHITECTURE → SOUL-ALBUM → DVR →
SOUL-BRIDGE-SDK). Three tiers: universal DVR/album/narration for any game; per-game Soul Bridges
(TypeScript plugins reading and writing saves, characters, native albums — The Sims 1 first);
Soul City Broadcast Network. The naming discipline is Postel at the vocabulary boundary: *Soul
Album* is the generic cross-game schema, *Family Album* is what Sims fans call the in-game
feature, and each bridge maps native vocabulary onto the uplifted schema — "we never co-opt a
game's own names."

---

*Rule of the pyramid: these digests are GLANCE-level. When a detail matters, open the YAML — it
is the source of truth, and its comments carry meaning these summaries compress away.*
