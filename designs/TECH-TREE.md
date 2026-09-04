# Tech Tree — one mechanism for everything you unlock

> *"Research completes when the prerequisite code lands; the reward is the
> pointer to what's now buildable."*
> — [DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md](object-system/DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md)

## It is a graph, not a tree

The name is a misnomer and every game that ships one knows it. Nodes have
multiple prerequisites, branches rejoin, and the interesting structure is always
the diamond where two lines of work converge. It is a **directed acyclic
graph**. Civilization's is a DAG. Factorio's is a DAG. A cycle is a design
error, not a feature.

*Tech tree* survives as the name because it is a K-line — say it and everyone,
human or LLM, already knows about prerequisites, frontiers, gated content, dead
branches and respec, with nothing respelled. But the same artifact has at least
four other names depending on where you are standing, and they are all the same
object:

| Vantage | What they call it | What the edges mean |
|---|---|---|
| Game design | tech tree, skill tree | research unlocks content |
| Software delivery | dependency graph, runbook order | this PR must land before that one |
| Scrum | board columns, blockers, epics | this story blocks that story |
| A wall of post-its | the wall | string between cards |
| Conspiracy board | red string | *"it's all connected"* |

The conspiracy board is the funniest and the most accurate. Nodes plus string,
gated by what you have already figured out, with the frontier being wherever the
string runs out — which is exactly the reading protocol below.

## The claim

[GAME-PIECES.md](GAME-PIECES.md) establishes that a **buff is a mixin with an
expiration date or condition on its delegation edge**, that a buff is a full
prototype carrying **its own CARD with its own advertisements**, and that
attaching one merges its card into the host's advertisement pool — so the
host's menu is the union of the cards of every live, enabled mixin, derived
fresh, never stored.

A **technology tree is the same mechanism with a different guard.** Swap the
temporal condition for a predicate over progress and nothing else changes:

| | Host | Guard | Payload |
|---|---|---|---|
| Buff | one piece or character | `expires_at` / `expires_when` / `while` | card merge |
| Tech node | the player, the faction, the world | `requires:` — a predicate over completed nodes | card merge |

Both are a delegation edge with a condition, evaluated at lookup. The buff's
edge is trying to go away; the tech node's edge is trying to arrive. That is
the entire difference.

Which means one node type covers everything a tree can hand you:

- **Tech** — objects you can make, recipes, machines, factories
- **Spells** — a spellbook is an unlock graph; each spell is a prototype
- **Plug-in abilities** — a move-set, a verb, a pie-menu slice
- **Modifiers and buffs** — the unlockable is itself a gated mixin
- **Runbooks** — design documents and the code they authorize (see below)

You do not need a tech system, a spell system, an ability system, and a buff
system. You need `inherits:` with guards, and a directory naming what each
node hands over.

## Unlock is a card merge

The unlock is not a boolean sitting in a save file. It is the same event as
attaching a buff: a prototype's card joins an advertisement pool, and the pool
is scored by the same advertise → score → act auction the pieces already run.

```yaml
# tech/AUTOMATION-2.yml
node:
  id: automation-2
  requires: [automation-1, electronics-1]      # guard over the graph
  research_complete_when: "have(science-pack-2, 40)"
  unlocks:
    - objects/ASSEMBLING-MACHINE-2.yml         # a craftable, with its own card
    - buffs/FAST-INSERTER-SPEED.yml            # a modifier, permanent host = player
    - abilities/BLUEPRINT-PASTE.yml            # a verb, joins the pie menu
```

Everything under `unlocks:` is a path to a prototype. The reward for research
is **the pointer**, and the pointer is the same kind of thing at every tier —
which is why a spell, a machine, a permanent stat modifier, and a document can
all hang off the same node without a special case.

When the guard is satisfied, those cards start advertising. Nothing patches the
player; the unlocked prototypes stand next to the player and shout, and the
scoring engine hears everyone at once.

## What is state and what is derived

The discipline from GAME-PIECES is *never cached, evaluated fresh* — castling
rights as a stored flag is a bug factory, and the troll flag failed because
the world was supposed to clear it. Tech trees need that discipline applied
with one honest exception:

- **The completion ledger is state.** Which nodes are done is an append-only
  event log with provenance: who researched it, when, at what cost. That is
  history, not cache. Append-only, per the house rule.
- **The frontier is derived.** What is researchable *now* is computed by
  evaluating guards against the ledger. Never store it. A "next steps" list
  maintained by hand is the troll flag with better branding.
- **The advertisement pool is derived.** Unlocked cards are gathered at lookup
  time, the same as any live mixin's card.

Store what happened. Compute what is possible.

## The cauldron is the engine

[skills/cauldron](../skills/cauldron/) melts a cross-cutting plan into one
monolith (MELT, STIR), then ladles it into topical docs plus **playbooks** —
one per landable PR — for parallel low-cost executors (LADLE, SERVE). That
output is already a dependency graph: the template's Navigation block names
what each playbook is **Preceded by** and what it **Unlocks**, and LADLE's
tree shape puts a dep graph in `playbooks/README.md`.

Making the graph explicit turns the plan into a tech tree, and the cauldron
into its engine, because cauldron playbooks already ship **the guard
evaluators**. Every step ends with an inline `**Verify:**` block, and the PR
ends with end-of-PR verification commands. Those commands are exactly the
predicate a `requires:` edge needs:

```yaml
# PB-04 frontmatter
requires:
  - { node: PB-02, verify: "rg -q 'class FlagRegistry' src/flags/registry.py" }
  - { node: PB-03, verify: "pytest tests/flags/test_resolution.py -q" }
unlocks:
  - { doc: 07-rollout.md,     why: "rollout strategy only makes sense once resolution lands" }
  - { node: PB-07,            why: "per-tenant overrides need the registry" }
  - { feature: "flags in the admin UI" }
research_complete_when: "pytest tests/flags/ -q && rg -q 'FLAG_SCHEMA_VERSION = 3' src/flags/schema.py"
```

The frontier becomes executable. An arriving executor does not read a status
document that someone forgot to update; it runs the guards and is told what is
buildable. A landed PR unlocks its dependents mechanically. This is the SCRY
principle applied to the plan's own shape: **tool reports, LLM decides** —
verification commands are sensors, the frontier is the reading.

And it gates *reading depth by progress*, which is the point DUBLIN-CORE
makes: the semantic pyramid gates by relevance, the tech tree gates by
progress. Every gamer, human or LLM, already knows how to read one.

## Why the gaming term earns its keep

This is the [no-ai-humansplaining](../skills/no-ai-humansplaining/) argument
in practice: "technology tree" is a K-line into a vast prepaid region of
latent space. Say *tech tree* and the model already knows about prerequisites,
frontiers, gated content, research costs, dead-end branches, respec, and the
difference between a tree and a directed acyclic graph — none of which needs
respelling. Invent `PlanNodeDependencyDescriptor` and you have bought a cache
miss that never fills.

The same argument runs through the whole vocabulary here: buff, room,
advertisement, spell, unlock. Dual-audience keywords — a schema for the
engine, a genre for the LLM.

## Precedents worth naming

**Civilization** (1991) put the tree on screen and made the graph itself the
interface. **Factorio** made every node's payload a *recipe* — research hands
you a thing you can build, which is exactly card-merge semantics with no
narrative wrapper. **Metroidvania** design inverts the frame: the ability is
the key, so unlocking a double jump retroactively re-scores the entire map,
and every locked door was an advertisement waiting for a bidder. **Skill and
talent trees** (Diablo, WoW) unlock modifiers rather than objects — the
purest case of "the tree unlocks buffs." **The Sims 4** gates moodlet-bearing
traits and aspiration rewards behind milestones: buffs behind a progress
guard, shipped.

The one that matters most for MOOLLM is **Drescher's schema mechanism**
(already load-bearing in
[FACTORIO-MOOLLM-DESIGN.md](FACTORIO-MOOLLM-DESIGN.md)): schemas compose into
higher-level schemas as reliability accumulates. That is a tech tree that
**learns its own edges** instead of receiving them from a designer — the
authored lattice and the discovered lattice, same shape. Play-Learn-Lift is
the tree walking itself: PLAY explores the frontier, LEARN notices which
compositions hold, LIFT crystallizes them into a node other work can depend
on.

## Anti-patterns

- **Fake gating.** Hiding documents an executor needs is not a tech tree, it
  is a locked filing cabinet. The tree gates *depth and order of attention*,
  not access. Everything stays readable; the tree says what is *ripe*.
- **Hand-maintained frontiers.** A `NEXT-STEPS.md` nobody re-derives goes
  stale the first day. Guards or nothing.
- **Nodes with no payload.** A node that unlocks only other nodes is a
  bookkeeping artifact. Every node should hand over a prototype, a document,
  or a capability — something with a card.
- **Research as chore.** If completing a node does not visibly widen the
  advertisement pool, the tree is a progress bar wearing a costume.

## See also

- [GAME-PIECES.md](GAME-PIECES.md) — buffs as mixins with expiration dates,
  the three-layer lifecycle ladder, cards merging into the host's ad pool,
  find-best-N and the dispatch spectrum
- [MOODY.md](MOODY.md) — heat drives parameters, **buffs gate the wires**: a
  buff that enables or disables exactly one constraint binding
- [skills/buff/](../skills/buff/) — the runtime skill: APPLY, TICK, CLEANSE,
  tags, categories, and the EFFECTIVE-VALUES base-vs-effective tick protocol
- [skills/cauldron/](../skills/cauldron/) — MELT/STIR/LADLE/SERVE, and
  [protocols/TREE.yml](../skills/cauldron/protocols/TREE.yml) for the graph
  and frontier protocol
- [DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md](object-system/DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md)
  — where unlockable runbooks were first proposed, and the dual-audience
  keyword argument
- [FACTORIO-MOOLLM-DESIGN.md](FACTORIO-MOOLLM-DESIGN.md) — factory as
  cognitive model, Drescher schemas, the learning curve
- [skills/play-learn-lift/](../skills/play-learn-lift/) — how a node earns
  the right to be depended on
