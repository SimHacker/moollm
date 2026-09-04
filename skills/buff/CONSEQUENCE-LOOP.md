# Consequence loop — how buffs close the advertisement cycle

**A buff is a persistent effect over time.** That single property is what turns
a sequence of disconnected actions into a world with memory, because a buff is
the only term in the cycle that outlives the tick that created it.

Everything else in the chain is instantaneous. A dependency graph says what
exists. An advertisement is an offer, made and gone. A pie menu is a choice
presented and dismissed. An action runs and returns. Only the buff stays — and
because it stays *and advertises*, it feeds the consequence of one action back
in as the input to the next.

Two consequences of persistence are worth naming separately, because they get
confused:

- **Continuous application** — while it lives, the buff does ongoing work,
  converting ambient conditions into behavior every tick.
- **Succession** — when it dies, it can spawn the next one (`spawns_after`),
  which is why a hangover follows a party without anyone scheduling it.

## The loop, and why buffs are what closes it

```
tech tree  →  what exists at all           (permanent, progress-gated)
    ↓
object     →  advertises what it affords   (skills/advertisement/)
    ↓
pie menu   →  ads become slices, by score  (the auction, made visible)
    ↓
action     →  the chosen ad runs           (SimAntics; the verb)
    ↓
BUFF       →  the consequence persists     (this skill)
    ↓
    └──────→  the buff's OWN card advertises  ─────┐
                                                   │
              ...back into the auction  ←──────────┘
```

Without buffs the loop is open: act, take effect, be forgotten. The world has
no memory between ticks and no consequence can argue for itself.

With buffs it closes, because of the one line in
[GAME-PIECES.md](../../designs/GAME-PIECES.md) that does all the work: **a buff
is a full prototype, so it carries its own CARD with its own advertisements.**
A consequence is therefore automatically a new offer. POISONED does not merely
subtract from your stats — it bids *"seek antidote"* to its host and
*"administer antidote"* to bystanders. The debuff recruits a healer. That is
how a state change becomes a plot.

This is the same reason the pie menu never needs cleaning up. The menu is the
union of the cards of every live mixin, derived at lookup. A buff joins the
pool and the slices appear; the buff expires and they leave with it. Nothing was
stored, so nothing goes stale.

## Buffs are where the argument lives

[Procedural rhetoric](../../designs/indexes/PROCEDURAL-RHETORIC-INDEX.md) says a
simulation argues through its rules. The specific place a simulation keeps its
argument is **the buff table**, because a buff encodes four editorial decisions
at once:

1. **Which consequences persist at all** — what the world refuses to forget.
2. **How long** — `post-accident-shame` running 24 ticks instead of 2 is a
   claim about how much humiliation an accident deserves.
3. **Whose stats move** — and this is the sharp one. Model poverty as a debuff
   on the *person* (reduced focus, reduced productivity) and the simulation
   argues that poor people are less capable. Model it as a debuff on the *room*
   or the *neighborhood* (fewer affordances, worse advertisements available)
   and the same mechanism argues that environments produce outcomes. Identical
   machinery, opposite politics, and the only difference is which dimension you
   bound the coordinate to.
4. **What it then advertises** — a debuff that bids "seek help" builds a world
   with a social safety net in it. One that bids nothing builds a world where
   suffering is inert.

So the tuning table is the editorial, and this is exactly where **agitprop**
enters as a design capability rather than a slur: if buffs are authorable
prototypes, then authoring a buff is authoring an argument, and a buff library
is a palette of arguments. See
[bits/theme-inclusion-agitprop](../../../WillWrightShowForFood/bits/theme-inclusion-agitprop/theme-inclusion-agitprop.md)
in WWSFF for the show treatment.

The honest corollary: a buff table is a legible, reviewable, diffable artifact,
which makes the argument *auditable* in a way a neural policy never is. You can
read the politics of a MOOLLM world in `git diff`.

## Media: the ambient path into the loop

[MOODY.md](../../designs/MOODY.md) adds the other input. Media playing in a room
broadcasts **time-varying heat per semantic tag** (romantic, energetic,
intellectual) into that room's auction, the room's children inherit it, and
buffs **gate the constraint wires** — a BLISSED buff wires the room's joy
envelope into happiness at full gain; noise-cancelling headphones are a buff
that disables exactly one binding.

Two lines from that design belong here verbatim in spirit: *a time-windowed
broadcast ad is a buff with an expiration date*, and *heat is ambient context*.
Media does not act on characters. It changes the weather of the auction, and
buffs decide which characters are wired to feel it.

## Construction set: the player authors the consequences

The Sims' actual innovation was not the simulation, it was that
**advertisements let strangers extend it** — new objects dropped in, declared
what they afforded, and the auction picked them up with no code changes. The
community shipped millions.

Buffs are the same move one layer in. If a buff is a prototype with a card,
then the construction set does not stop at objects; players author
*consequences*. A modder who ships a buff has shipped a rule about what matters
and for how long — and because the buff advertises, the rest of the world
responds to it without knowing it exists.

That is the whole phrase, assembled: a **visual procedural rhetoric programming
language and construction set**. Visual because the pie menu is the auction made
visible and the tuning surface is the program text. Procedural rhetoric because
the buff table is the argument. Programming language because guards, lifetimes
and card merges compose. Construction set because the consequences are
authorable by someone who never reads the engine.

## Blender — commands, their parameters, and state over time

Blender is the richest shipped example of "a command that keeps its parameters
and its state after it runs," and it has several constructs doing different
parts of the job:

| Blender construct | What persists | Conflict policy | Buff analogue |
|---|---|---|---|
| **Modifier stack** | parameters, non-destructively; base data → evaluated data | explicit stack order | **EFFECTIVE-VALUES exactly**: base is truth, evaluated is reality |
| **Constraints** | a target, a space, and an `influence` weight 0–1 | stack order, weighted blend | MOODY's gated wires — influence *is* a continuous guard |
| **Operators** + Adjust Last Operation | the command's parameters, live and re-tweakable after execution | last one wins | the action with its tail still attached |
| **Modal operators** | interaction state while running (grab, knife, spin) | exclusive — one modal at a time | a buff mid-lifetime, with its own event loop |
| **Gizmos** (called Manipulators before 2.80) | the interactive handles bound to a tool's parameters | tool-owned | the pie menu's cousin: the auction made grabbable |
| **Tools** (`WorkSpaceTool`) | a gizmo plus a keymap plus retained operator properties | active tool wins | a persistent stance, not a one-shot verb |
| **NLA strips** | actions on tracks with blend mode and influence | track order + blend mode | layered timed buffs on channels |
| **Drivers** | an expression over other properties | recomputed on dependency change | a `while:` guard, continuously evaluated |
| **Geometry Nodes** | the whole parameterized procedure, as a graph | node wiring | the construction set for modifiers |
| **BGE logic bricks** (sensor → controller → actuator) | actuator state and duration | brick wiring | the visual-programming cousin, removed in 2.80 |

The two worth stealing outright:

**The modifier stack** is the cleanest shipped implementation of
base-versus-effective with a declared order — the same protocol as
[EFFECTIVE-VALUES.md](EFFECTIVE-VALUES.md), except Blender got the UI right:
each modifier is a collapsible panel showing its parameters, individually
toggleable for viewport and render separately. That is *disable-but-remain*
(the second rung of the GAME-PIECES ladder) with a checkbox, and it is why
artists trust it: the base mesh is always still there.

**Constraints with an `influence` slider** are the piece MOODY needs. Influence
is a continuous guard — not "does this apply" but "how much," with the value
itself drivable by an expression. A buff whose strength is a driven float rather
than a boolean is strictly more expressive than anything in this skill today.

The synthesis for the buff model: **a buff is a command that hasn't finished,
expressed as a modifier that hasn't expired** — Blender's operator half supplies
the parameters and the running state, its modifier half supplies the ordered
non-destructive evaluation, and neither half alone is a buff.

### Footnote: Garnet's Interactors are a different lineage

Worth not conflating. Garnet (Brad Myers, CMU) made *input behavior* a
first-class parameterized object — menu-interactor, move-grow-interactor — with
running states (start, running, abort, stop) instead of scattered callbacks, and
Amulet followed with `Am_Command` objects carrying parameters and undo. That is
Blender's modal-operator idea, prototype-based, fifteen years earlier.

⚠ Gap: [GARNET-AMULET-PROTOTYPE-SYSTEM.md](../../designs/GARNET-AMULET-PROTOTYPE-SYSTEM.md)
covers Garnet's prototypes, parallel trees, slots and constraints, and never
mentions Interactors. Don was at CMU with Myers; that section is missing.

## See also

- [SELF-KORZ.md](SELF-KORZ.md) — the three readings, and the lifetime axis
- [GAME-PIECES.md](../../designs/GAME-PIECES.md) — the canonical model, find-best-N, the scoring ladder
- [MOODY.md](../../designs/MOODY.md) — media as ambient heat; buffs gate the wires
- [TECH-TREE.md](../../designs/TECH-TREE.md) — the dependency graph of what exists at all: unlock as a permanent, progress-gated buff
- [skills/advertisement/](../advertisement/) — the auction the buffs bid into
- [designs/sims/sims-pie-menus.md](../../designs/sims/sims-pie-menus.md) · [sims-find-best-action.md](../../designs/sims/sims-find-best-action.md) · [sims-object-model.md](../../designs/sims/sims-object-model.md) · [sims-simantics-vm.md](../../designs/sims/sims-simantics-vm.md)
- [designs/indexes/PROCEDURAL-RHETORIC-INDEX.md](../../designs/indexes/PROCEDURAL-RHETORIC-INDEX.md) — Bogost, arguing agents
- [designs/GARNET-AMULET-PROTOTYPE-SYSTEM.md](../../designs/GARNET-AMULET-PROTOTYPE-SYSTEM.md) — the Interactors gap
- [buffopedia/](buffopedia/) — how eighteen other systems answered the same four questions
