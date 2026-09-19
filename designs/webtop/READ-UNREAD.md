# Read, unread, and the torch you leave behind

*The reading overlay's missing layer. Everything about light, fog, dwell, and persistent
cursors is already specified elsewhere in this repo — this document does not restate it. It
adds the one thing none of those docs carries: **a verdict the reader issues, stored, and
addressable**, and the gesture that writes it.*

## What already exists, so this doesn't rebuild it

| Piece | Where | What it already settles |
|---|---|---|
| Fog of war with memory, dimmers whose detents are the mipmap rungs, the torch cursor with jitter as active sensing, colored light as status | [mind-mirror/HALLS-AND-ROOMS.md](../../skills/mind-mirror/HALLS-AND-ROOMS.md) | Light lives in an overlay, not in the world. Verbs: `DIM` `SPOTLIGHT` `FLOODLIGHT` `DOUSE` `TINT` `FILL-OUT` `KISS` |
| Light intensity *is* attention weight; a saved lighting rig is a K-line | [P-PYRAMID.md](../P-PYRAMID.md) · [MicropolisCore overlay](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/p-pyramid-attention-overlay.md) | Minsky's 1979 name for the overlay, and the window-manager mapping |
| A reading cursor is a character with a location, a path, and pen-up/pen-down | [READING-CURSORS.md](READING-CURSORS.md) | Persistence, identity, consent, and "a place is not a boolean" |
| `gloom` (unlit, not absent), `moor` (a live line to a live position) | [ROOM-STROLLING.md](ROOM-STROLLING.md) | The vocabulary, and why a moor beats a bookmark |
| Dwell instrumented as an attention signal — `enterTime`, `exitTime`, `totalTime` | [pie-stack-views/RESELECTION.md](../pie-stack-views/RESELECTION.md) | Shipped in OpenLaszlo and OLPC Micropolis; the gesture already exists |
| Reversible progressive disclosure driven by radial distance | [pie-stack-views/PUMPING-UP-PIE-MENUS.md](../pie-stack-views/PUMPING-UP-PIE-MENUS.md) | Fog pushed aside by appetite, folded back on the way in |
| `BRIEF` as adaptive detail computed from visit history | [adventure/SKILL.md](../../skills/adventure/SKILL.md) | 1977 shipped the idea that a revisit gets a *different* description, not a shorter one |
| A saved view is an opinion, recorded as data | [pie-stack-views/VIEWS-AS-TESTIMONY.md](../pie-stack-views/VIEWS-AS-TESTIMONY.md) | Why reader state is publishable rather than private telemetry |

**The gap:** every one of those stores *where attention went*. None stores **what the reader
concluded**, and none offers a gesture for saying so. Dwell is spent on inferring interest
and then discarded. `visited` is a flag the system sets. Nothing in the corpus can answer
*have I dealt with this*, which is the question that actually governs whether you can come
back to a thread a second time.

## Read is not visited, and it is not one bit

`visited` is a fact about the machine's history. **Read is a verdict, issued by a reader,
about a thing.** The distinction matters because the states are not ordered on one axis:

| Verdict | Means | Light |
|---|---|---|
| `gloom` | Exists, never entered | Unlit — and honestly so |
| `seen` | Entered, no verdict issued | Lit, cold, no colour |
| `read` | Dealt with; do not show me again unless it changes | Steady warm |
| `understood` | I could explain this to someone | Steady, saturated |
| `unread-again` | I read it, and it changed under me | **Relit** — the important one |
| `priority: 1..3` | Must read; ranked | Pulse rate carries the rank |
| `parked` | Read enough for now, deliberately shelved | Dimmed *by hand*, which is different from dim by neglect |
| `disputed` | Read and I disagree | `TINT` red — a verdict, not an error |
| `open-question` | Read and it opened something | `TINT` purple, per the existing colour convention |

`READING-CURSORS.md` already makes the argument this table implements: browser history
colours a link purple whether you skimmed it or extracted three quotes from it, and those
are not the same event. This is that complaint given a storage format.

## The gesture: linger writes, the menu overrides

**Pointing at something and lingering marks it read.** That is the whole default, and it is
free because the instrumentation shipped decades ago — `RESELECTION.md` accumulates per-item
dwell totals, and the pie menu's dwell-to-open timing is the same clock. Today that number
is spent on predicting the next item and then thrown away. Spend it on the verdict instead.

Three properties make the default safe rather than creepy:

1. **It is a control, not a property.** Pen-up/pen-down from `READING-CURSORS.md` is the
   privacy gate: a cursor with the pen up reads without recording. The turtle already
   solved this.
2. **It is reversible in one action**, which is the test
   [view-state-is-the-users](../../skills/design-sense/lenses/view-state-is-the-users.md)
   demands: zero or one action back to where you were, or the state isn't yours.
3. **The threshold is per-cursor**, because a cursor carries its own model. A skimming
   cursor should need longer to claim it read something than a studying one.

And the menu is the one you already have. The adventure editing verbs *are* the read-state
verbs, which is the evidence this layer belongs in the same vocabulary rather than a new one:

| Don's gesture | Existing verb | New? |
|---|---|---|
| mark as read | linger (default) | the default is new; the dwell isn't |
| mark as unread | — | **new: `RELIGHT`** |
| mark needs-reading, priority 1/2/3 | `TINT` + pulse | ranking is new |
| shrink and keep | `DIM` to a lower rung | existing |
| shrink and hide | `DOUSE` | existing |
| expand and keep | `DIM` up, pinned | existing |
| expand | `SPOTLIGHT` | existing |
| summarize and fork to a new room, bidirectional | `FILL-OUT` + `KISS` | **new: `FORK`**, which is `FILL-OUT` into a fresh room plus a `KISS` back |

`FORK` is the one worth building first, because it is the only verb on the list that
*creates* rather than annotates, and because the bidirectional link is what keeps a forked
thought from becoming an orphan — the failure mode of every note-taking app that offers
"extract to new note."

## Unread is a diff, not a flag

The state that makes a thread readable twice is not *unread*; it is **changed since your
verdict**. New comments arrive at particular places in a graph, and the thing a reader needs
is not a notification count but a **relit room** in a map they already know.

The mechanism is already available: `READING-CURSORS.md` notes that a versioned corpus lets
a stale cursor report what moved under it, which no bookmark can do. So:

```yaml
verdict:
  by: don                      # whose verdict — light has an author
  target: quora/agi-answer#haig-shahinian
  state: read
  at: 2026-09-16T11:04:00Z
  corpus_version: 4f1c2ab      # what it looked like when I said so
```

A verdict is stale when `corpus_version` no longer matches. Stale plus `read` equals
`unread-again`, and the renderer relights exactly that room and nothing else. You return to
a map where the four places that changed are glowing and the two hundred you dealt with stay
warm and quiet.

This is the Quora failure inverted. Quora drops you a thousand miles from where you were
with no record that you had ever been anywhere. The same corpus with verdicts on it opens
with your own lighting rig intact and four rooms newly lit.

## Torches are objects, which is what makes them yours

A torch is not a pixel, a colour, or a CSS class. It is **an object in the room, with a
file, an author, and a diff** — which is what makes the whole layer addressable, shareable,
and arguable instead of being per-browser telemetry.

```yaml
torch:
  color: purple                # per the existing convention: an open question
  author: don                  # human-authored
  reason: "Haig's closure argument — does autopoiesis answer this?"
  lit: 2026-09-19
  lifetime: 90d                # decays; see below
  flicker: 0.2                 # unsettled — it wavers
```

Four consequences fall out of "torch is an object" and each one closes a hole in an existing
doc:

**Light carries provenance.** Don said the overlay should be both human-authored *and*
simulation- or model-expressed. If a torch has an `author`, then a model's guess about what
deserves attention and a person's deliberate mark are **distinguishable at a glance**, which
is the difference between a prosthetic and a slot machine. An unsigned light is a
recommendation engine.

**Lights can be published.** A lighting rig with authors is testimony
([VIEWS-AS-TESTIMONY.md](../pie-stack-views/VIEWS-AS-TESTIMONY.md)), so "here is how I read
this thread" becomes a shareable artifact — and two readers' rigs can be diffed, which is a
better argument than either of them restating their position.

**Torches decay, and that is a feature.** A light that never dims lies about your current
understanding: you read that carefully in 2019 and you could not explain it today. Lifetimes
make the overlay report the truth rather than the flattering version, which is the same
discipline
[reasoning-is-not-science](../../skills/design-sense/lenses/reasoning-is-not-science.md)
asks for — the grade recorded where you can't quietly lose it, including against yourself.
Decay is opt-in per verdict; `understood` should decay faster than `read`, because it claims
more.

**A convention makes a breadcrumb readable.** Minecraft's torch practice is not "place light
where interesting" — it is *torches on the right wall going in*, so the asymmetry tells you
which way is out. That is the whole reason the habit works in a branching cave, and it is
the lesson for the overlay: a mark that encodes direction beats a mark that encodes
intensity. `moor` already knows where you cast off from; the torch should show it.

## The coloring book is the progression, not the metaphor

Don's arrival sequence — dark and monochrome, then lit, then coloured, then animated — is a
render of the verdict lattice, and the point is that **the colours are the reader's
expression rather than a completion percentage**:

```text
gloom  →  seen  →  read  →  understood  →  annotated  →  forked
dark      cold     warm     saturated     tinted        connected
```

Paint-by-numbers would mean the system chooses the colours and you fill them in. A colouring
book means the palette and the placement are yours, which is why `TINT` takes a `reason`.
The physical instance already exists and is already documented: the De Pijp ride where the
bike is the crayon and a completed district fills in
([ebike ride gestures](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/sources/ride-gestures-2026-09.md)),
whose inverse is OpenStrollMap's `gloom` — the streets you have not ridden, a property of a
reader and not of a city
([OPENSTROLLMAP.md](OPENSTROLLMAP.md)).

## What to build first

1. **The verdict record** — the YAML above, in `CURSOR-STORAGE.md`'s format, with
   `corpus_version` so staleness is computable. Nothing renders yet; the data model is the
   whole first step, and it is small.
2. **Linger writes `read`**, pen-up respected. The dwell accumulator exists; wire its output
   to a verdict instead of to a prediction. (The Svelte `PieMenu` port still has dwell
   timing unrestored — that is the blocking dependency, noted in the pie-stack-views README.)
3. **`RELIGHT` on stale-plus-read**, rendered as a relit room on a map you already know.
   This is the feature that makes a thread readable twice and it is the one Quora's
   absence of it produced a whole recap shelf to work around.
4. `FORK`, with the back-link. Then ranking, then decay.

**See also:** [READING-CURSORS.md](READING-CURSORS.md) — the reader this state belongs to ·
[../../skills/mind-mirror/HALLS-AND-ROOMS.md](../../skills/mind-mirror/HALLS-AND-ROOMS.md)
— the lights it modulates ·
[../../skills/design-sense/lenses/view-state-is-the-users.md](../../skills/design-sense/lenses/view-state-is-the-users.md)
— the lens that says losing this is a data-loss bug ·
[PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) — the unvisited exit as the honest statement that
there is more

↑ [webtop hub](README.md)
