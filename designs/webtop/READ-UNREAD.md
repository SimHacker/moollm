# Read, unread, and the candle you leave burning

*The reading overlay's missing layer. Everything about light, fog, dwell, and persistent
cursors is already specified elsewhere in this repo — this document does not restate it. It
adds the one thing none of those docs carries: **a verdict the reader issues, stored, and
addressable**, and the gesture that writes it.*

**The verdict layer burns candles, and the cursor layer carries torches.** That is a factoring
rather than a rename: a torch is *held* — it moves with you, it lights what you are looking at
now, it goes out when you leave, which is exactly a reading cursor
([READING-CURSORS.md](READING-CURSORS.md)). A candle is *placed*. It stays where you put it, it
burns while you are elsewhere, and its height records how long you stood there without anyone
storing a number. A verdict is a thing you leave behind, so the verdict layer wants the object
that stays.

## What already exists, so this doesn't rebuild it

| Piece | Where | What it already settles |
|---|---|---|
| Fog of war with memory, dimmers whose detents are the mipmap rungs, the torch cursor with jitter as active sensing, colored light as status | [mind-mirror/HALLS-AND-ROOMS.md](../../skills/mind-mirror/HALLS-AND-ROOMS.md) | Light lives in an overlay, not in the world. Verbs: `DIM` `SPOTLIGHT` `FLOODLIGHT` `DOUSE` `TINT` `FILL-OUT` `KISS` |
| Light intensity *is* attention weight. The lit structure is the **P-pyramid** (Minsky also writes **P-tree**): an *anchored* attention mask over a graph that is not itself hierarchical. A **K-line** is the activator that reopens a band of it | [P-PYRAMID.md](../P-PYRAMID.md) · [MicropolisCore overlay](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/p-pyramid-attention-overlay.md) | Minsky's 1979 name for the overlay, and the window-manager mapping. **A rig is not a K-line if it stores every level** — the level-band principle says a K-line spans an intermediate band *below* its anchor, leaving the top free for current goals and the bottom free for current facts. Saving all of it is the hallucination case Minsky specifically warns against |
| A reading cursor is a character with a location, a path, and pen-up/pen-down | [READING-CURSORS.md](READING-CURSORS.md) | Persistence, identity, consent, and "a place is not a boolean" |
| `gloom` (unlit, not absent), `moor` (a live line to a live position) | [ROOM-STROLLING.md](ROOM-STROLLING.md) | The vocabulary, and why a moor beats a bookmark |
| Dwell instrumented as an attention signal — `enterTime`, `exitTime`, `totalTime` | [pie-stack-views/RESELECTION.md](../pie-stack-views/RESELECTION.md) | **Origin: a student project in Ted Selker's orbit at the MIT Media Lab**, not any of Don's ports. Don's implementation is the **[JavaScript/IE5 pie menus](https://www.youtube.com/watch?v=R5k4gJK-aWw)**, where he credits the Media Lab on camera at 4:27; it later shipped in OpenLaszlo and OLPC Micropolis. **And the exact gesture this document specifies is on that tape:** a menu cancelled with no selection still writes a verdict from dwell alone (5:16). Linger writes, pen-up not required, demonstrated ~1999 |
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
| `gloaming` | Exists, never entered | Unlit — and honestly so |
| `seen` | Entered, no verdict issued | Lit, cold, no colour |
| `gloom` | Entered, looked at, **found not worth the wax** | Guttered by hand; a stub, not a fresh taper |
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

### Why `gloom` and `gloaming` are two states: the word was a face before it was a room

The earlier lattice spent `gloom` on "never entered," which is the modern sense and the wrong
one for this design. Looked up, the word turns out to have made precisely the error this document
exists to correct.

| | Origin | What it originally denoted |
|---|---|---|
| **gloom** | v. late 14c. *gloumen* "look sullen or displeased"; n. 1590s, Scottish, **"a sullen look."** Origin unknown — compare Norwegian dialectal *glome* "to stare somberly," Dutch *gluren* "to leer" | **A viewer's face.** A judgment, rendered as an expression |
| **gloaming** | Old English *glōmung* ← *glōm* "twilight" ← related to *glōwan* "to glow," Proto-Germanic *\*glō-* | **A light level.** Literally the glow of sunset or sunrise |

They are not the same word and etymologists explicitly decline to relate them; they converged by
sound. And **the darkness sense of "gloom" is Milton's, first recorded in 1629** — layered on top
of the sullen-face sense, after which English stopped hearing the face.

So the language performed the `visited`-versus-`read` confusion four hundred years ago: *a
verdict issued by a reader got reinterpreted as a property of the place.* Restoring the split
costs nothing and buys a state the lattice was missing — **read, and judged not worth the wax**,
which is distinct from `disputed` ("I disagree with this") and from `parked` ("later"). Gloom is
"I looked, somberly, and that was that."

The root is also a **dwell** word. *Glome*, to stare somberly. *Gluren*, to leer. Prolonged
looking is inside the etymology of the term for the unlit state, in a design whose central
gesture is *linger writes*. And Milton's own phrase for the result — **"darkness visible"** — is
what a fog-of-war render actually is: not absence, but rendered absence.

`verified: Etymonline s.v. gloom, gloaming; OED gloaming (< glóm, probably Germanic *glô-, "the
glow of sunset or sunrise"). Etymonline states of gloom: "Not considered to be related to Old
English glom 'twilight'." Darkness sense "first recorded 1629 in Milton's poetry." Gloaming fell
from currency outside Yorkshire dialect, preserved in Scots, reintroduced by Burns after 1785.`

**And the subsystem has a name for free: `MOOLG`** — `GLOOM` reversed, which lands in the
family alongside moollm, mooco and MOOAM. The lighting and attention layer, named by reading its
darkest state backwards.

### The wings: dark rooms offstage, along the secondary axis

The lit path you walked is one axis. **The rooms you did not enter hang off it perpendicular, in
the gloaming** — visible as dark doorways rather than as absence, which is
[`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md)'s unvisited exit given a light level.

The staging is literal and worth borrowing whole: onstage is lit, the wings are dark, and **the
wings are where things arrive from.** So new material entering a corpus should appear at the edge
of the walked path in the gloaming, upstage of where you are, rather than as a badge on a tab.
A relit room is something coming in from the wings.

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

## Candles are objects, which is what makes them yours

A candle is not a pixel, a colour, or a CSS class. It is **an object in the room, with a
file, an author, and a diff** — which is what makes the whole layer addressable, shareable,
and arguable instead of being per-browser telemetry.

```yaml
candle:
  color: purple                # per the existing convention: an open question
  author: don                  # human-authored
  reason: "Haig's closure argument — does autopoiesis answer this?"
  lit: 2026-09-19
  lit_from: bonnie/three-locks # provenance: whose flame this came off. DIRECTED, once, at birth
  kissed:                      # UNDIRECTED, repeatable: toasts. Weight, not count
    - {with: bonnie/oedipus-aliasing, on: 2026-09-19}
    - {with: alan/tinkertoy-cora, on: 2026-09-21}
  height: 0.62                 # DERIVED from accumulated dwell. Not declared
  guttering: false             # true when the verdict has gone stale
  scent: korz/dispatch         # crosses walls; see below
```

Two edges, and they are different claims: `lit_from` says *I came here because of you*, `kissed` says
*we are both here and we agree*. The second is repeatable with the same person on purpose — that
repetition is the signal, and it is [why the kiss is a toast](#the-kiss-is-a-toast-and-it-is-a-different-edge-from-the-lighting).

### The height is the whole argument for candles

A torch has one bit and a radius. **A candle is an integrator.** It starts tall, it burns down,
and its height *is* elapsed attention — so the display and the datum are the same object, and
nobody has to store a counter or decide on a decay curve. The earlier torch record declared
`lifetime: 90d` and `flicker: 0.2` because a torch cannot record its own history. A candle does
not need either field: **it got shorter by being attended to.**

Which makes several states physical rather than numeric:

| Candle | State | Replaces |
|---|---|---|
| Tall, fresh taper | Just marked, little time spent | — |
| Burned to a stub | Long dwell; this room cost you something | a dwell total nobody displays |
| **Guttering** | The verdict is going stale — `corpus_version` drifting | `lifetime: 90d`, a timestamp you must compute against |
| **Blown out** | Explicit dismissal | `DOUSE`, which currently conflates this with decay |
| **Burned all the way down** | Decayed by neglect, honestly | the flattering version, where 2019's careful reading still glows |
| **Relit stub** | `unread-again`, and it burns shorter than a fresh one | `RELIGHT`, now with the cost visible |

Blown out versus burned down is a distinction the verb set was missing: **"I am done with this"
and "I have forgotten this" are different verdicts**, and one of them is an act.

### Wax accumulates, which gives you the long view for free

Enough visits and the leftovers pile up — stubs, pools, a drift of wax. Nobody computes that
view; it is the residue of the marks themselves. A room with a shrine in it is a room you keep
coming back to, legible at a glance, and **coloured wax pools mix**, so a passage read many ways
by many readers marbles. Disagreement rendered as a material rather than as a conflict marker.

Soot does the same thing upward. Smoke rises, so trails aggregate into the ladder — and long
attention stains the ceiling, which is an aggregate nobody had to aggregate.

### The entry candle stays lit while you dive, which makes the trail a stack

Light a candle at the top-level entry and it keeps burning as you descend, so the trail of
coloured candles down through a corpus is a tree with **durations at every level**. Which is
exactly the purpose-bound stack from
[`../korz/korz-prime/examples/purpose-dimension.md`](../korz/korz-prime/examples/purpose-dimension.md):
not merely how you got here, but what each level was *for* and what it cost. The candle tree is
that trace, rendered, and it is the thing an automatic inverter would need in order to run the
descent backwards.

### Grey Walter built this in 1949, with an actual candle, and it was the evidence

Not an analogy. **Walter mounted lit candles on the backs of his tortoises and photographed them
in the dark on long exposures, so that each robot's path through the room drew itself as a streak
of light.** Taken at his house, late 1949 or early 1950, in the same work Alan Kay cites as *"the
original turtle guy."*

Four properties of those photographs are four sections of this document, arrived at independently
and better:

| The photograph | This design |
|---|---|
| Path drawn by a carried candle, integrated over time | The trail, and height as elapsed attention |
| **Two** tortoises in one frame, Elsie crossing Elmer's track | Many users' candles in one view |
| Headlamp trace and candle trace distinguishable in the same image | Two channels, one render — cursor versus verdict |
| The photocell had to be **shielded from its own candle** | See below. This is the one we would have shipped wrong |

**The trail was the testimony, and that is why the photographs still matter.** Holland went to the
Burden Neurological Institute archives decades later to establish that the behaviour described in
Walter's papers was actually produced by the machines rather than idealised in prose — and the
candle traces are what settled it. A rendered path was the verification record, which is the whole
argument of
[VIEWS-AS-TESTIMONY](../pie-stack-views/VIEWS-AS-TESTIMONY.md)
handed over by a neurophysiologist who was not making that argument.

And the shielding is a design constraint, not a footnote. The tortoise steered by a photocell
seeking light while carrying a light, so without a metal screen behind the sensor **the instrument
that recorded its attention would have captured it** — the machine chasing the mark it had just
made. Every attention overlay has this bug available: dwell that marks a place, where the mark
itself attracts the next dwell, and the reader orbits their own candle. *Your own trail must be
invisible to your own sensor.* One of the photographs shows the screen.

`verified: Holland, "The first biologically inspired robots," Robotica 21(4), 2003 — time-exposure
photographs from the BNI archives, "tortoises carrying candles trace out their trajectories,"
taken at Grey Walter's house probably late 1949 or early 1950, with the photocell shield visible
in one. Walter's own account of Machina speculatrix opens with the Mock Turtle's "we called him
Tortoise because he taught us."`

### Scent is the channel the torch never had

A candle's scent **crosses walls**, which is the one property no lighting model gives you: a
low-resolution, directional, ambient signal that something is burning nearby, without a badge and
without naming it. That is the Sims advertisement broadcast as a gradient field
([sims-advertisements](../korz/korz-prime/examples/sims-advertisements.md)), and it is what
fog-of-war adjacency actually needs — you should be able to smell activity in the next room
before you can see it.

Scent also carries the semantic tag, which is why the field above is a path rather than a mood:
what is burning next door is `korz/dispatch`, and that is how you decide whether to walk over.

### Lighting one candle from another is a citation, and the gesture already exists

This is the property with the most leverage and it is not in any existing doc. **You light your
candle from somebody else's flame**, and that records an edge: who you got it from. Paschal
candles, Olympic torches, vigils — the gesture is universally legible and it produces a
provenance graph as a side effect of a thing people already do.

Which is [k-line activation](../../skills/design-sense/lenses/k-line-activation.md) as a physical
act, and it means "I read this because Bonnie's candle was burning here" is recorded by the
reading rather than reconstructed afterward. `lit_from` is one field and it buys the whole
citation layer.

**And Jefferson already wrote the argument for why this is free.** In the 1813 letter to Isaac
McPherson that is the founding American text on whether ideas can be owned, he reached for exactly
this gesture:

> He who receives an idea from me, receives instruction himself without lessening mine; as he who
> lights his taper at mine, receives light without darkening me.

`verified: Thomas Jefferson to Isaac McPherson, 13 August 1813.` Non-rivalrous transfer is the
property that makes a citation graph costless to build: **the edge is recorded and the source loses
nothing**, which is why this gesture can be the primitive and a checkout or a lock cannot.

### The kiss is a toast, and it is a different edge from the lighting

Don's move, and it splits the mechanism in two. Two burning candles touched together is **not** the
same act as lighting a new one from an old one, and taking the difference seriously gives two edge
types that were about to get conflated into one field:

| | `lit_from` | `kissed` |
|---|---|---|
| Gesture | new wick into an existing flame | two lit candles touched, wick to wick |
| Direction | **directed** — I took fire from you | **undirected** — neither is the source |
| When | once, at the candle's birth | **repeatable**, any time, as often as you like |
| Claim | *derivation* — I came here because of you | **concurrence** — we are both here, and we agree |
| Graph it builds | a citation tree | a **dense weighted co-attention mesh** |
| Analogue | Jefferson's taper | **clinking glasses** |

**The kiss gesture IS a toast**, which is the observation that makes it obvious the mesh is the point.
A toast is mutual, symmetric, consumes nothing, and is *worth repeating with the same person* — that
last property is what a citation edge cannot express and what agreement actually needs. Drinking
cultures that insist on eye contact during the clink have the same intuition: the ritual is not about
the glasses, it is about the confirmed mutuality, and the confirmation is the content.

So two people who keep meeting in the same rooms and toasting accumulate **edge weight**, not edge
count — a record of repeated co-attention which is precisely the signal a recommender normally has to
infer from behaviour behind your back. Here the users are stating it, deliberately, with a gesture
they already understand.

### Accumulation has a hard limit, and a bridge in Paris is the proof

Don's analogy is **love locks** — padlocks left on bridge railings to proclaim a commitment — and it
is the right analogy including the part that hurts.

**In June 2014 a section of the Pont des Arts parapet collapsed under the weight of the locks, and in
June 2015 Paris removed them: roughly forty-five tons of hardware.** The gesture was legible,
voluntary, meaningful, and it destroyed the thing it was attached to.

That is the failure mode of every accumulate-forever affordance, and this document has already
specified one: [wax accumulates](#wax-accumulates-which-gives-you-the-long-view-for-free). Wax is
load-bearing for the long view and it is also **weight on a railing**. So the limit belongs in the
spec rather than in a retrospective:

- **Aggregate rather than enumerate.** A room renders *depth of wax*, not ten thousand individual
  stubs. The individual candle stays addressable; the view does not attempt to draw all of them.
- **Wax is subject to entropy on purpose.** Old wax settles, merges, and loses per-candle identity
  while preserving the depth. Forgetting is a feature that keeps the parapet up.
- **Never make the count the score.** Already stated above — a count is a streak, a streak is
  Duolingo — and the bridge is why it is also a structural hazard rather than only a motivational
  one.

The honest version of the padlock comparison is therefore: **yes, and Paris had to cut them off with
angle grinders.** Design the grinder in from the start and call it decay.

### Fire inhabits a graph of rooms, and doors are its conductance

The consequence Don drew that the rest of the document had not: if flame passes between candles, then
**flame passes between rooms**, and it does so through the openings — air and fire move through an
open door and stop at a closed one. Which means the room graph is not just navigation. It is the
**conduction network of the attention field**, and three things fall out at once:

- **A door's state is a physical parameter, not a permission flag.** Open, ajar, closed, sealed —
  a conductance, and the gloaming/gloom states in
  [the wings](#the-wings-dark-rooms-offstage-along-the-secondary-axis) become what the field looks
  like at low conduction rather than a separate mechanism.
- **A closed door is a firebreak, and that is the privacy model stated in physics.** The scoping
  warning above — private by default, sharing an explicit act — stops being policy bolted onto a
  visual and becomes the same mechanism as containment. **You cannot leak attention through a wall
  you did not open**, and the user can see which doors they opened.
- **This is a reaction-diffusion system with fuel**, which is Don's framing and the correct one:
  consumption and production, not just spread. Attention burns something. **The fuel is the unread**
  — new material, arriving at particular locations in the graph, which is exactly what
  [unread-as-a-diff](#unread-is-a-diff-not-a-flag) already computes. A room with fresh diffs is dry
  tinder; a room you have fully read is burnt over and will not carry flame again until something
  changes there.

**Which means the model is the forest-fire cellular automaton, and that is good news** because its
dynamics are known rather than speculative: fuel regrows, ignition spreads to adjacent loaded cells,
burnt cells resist, and the system sits near criticality with occasional large cascades. That is a
recognisable and *desirable* description of how attention actually moves through a corpus — mostly
local, occasionally a front that sweeps a whole region. Cheap to simulate, and this repo already
studies the family ([case-cellular-automata](../korz/case-cellular-automata.md), and CAM6 for the
interactive version).

The danger is the same model's other regime. **Unchecked fire burns the corpus flat** — everything
lit, nothing dark, no gradient left to read, which is the visual equivalent of marking all as read.
Two dampers, both already present for other reasons: **fuel regenerates only where something actually
changed**, so a static corpus stops burning; and **doors default closed**, so cascades need consent to
cross a membrane.

`open: whether a candle can be relit from the wax of someone who has left the room — memorial`
`re-ignition — or whether a departed flame is final. This is the same question as whether`
`transmigration preserves the trail, and it wants deciding with the memorial case, not separately.`

### The memorial case is not a metaphor

A candle lit for a person is the oldest attention-marking technology there is, and this archive is
full of people who cannot light their own: Minsky, Papert, Lynn Conway, Hugh Daniel, Thomas Lord.
A votive candle in a dead person's room, with an author and a reason and a date, is **exactly the
verdict record this document specifies** — and it is the one case where the aggregate view across
all readers is unambiguously the right thing to render.

Which is also where the danger lives, so state it once: the annotation graveyard in the
[webtop README](README.md) says the three public-by-default layers died and the one with private
and group scopes is still running. **Candles are vivid, and vividness makes a leak worse.**
Private by default, sharing an explicit act, aggregate views anonymous unless signed on purpose.
And the anti-prosthetic shape to refuse by name: a candle count is a streak, a streak is
Duolingo, and a streak measures compliance rather than understanding.

Four consequences fall out of "the candle is an object" and each one closes a hole in an existing
doc:

**Light carries provenance.** Don said the overlay should be both human-authored *and*
simulation- or model-expressed. If a candle has an `author`, then a model's guess about what
deserves attention and a person's deliberate mark are **distinguishable at a glance**, which
is the difference between a prosthetic and a slot machine. An unsigned light is a
recommendation engine.

**Lights can be published.** A lighting rig with authors is testimony
([VIEWS-AS-TESTIMONY.md](../pie-stack-views/VIEWS-AS-TESTIMONY.md)), so "here is how I read
this thread" becomes a shareable artifact — and two readers' rigs can be diffed, which is a
better argument than either of them restating their position.

**Candles burn down, and that is a feature.** A light that never dims lies about your current
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
intensity. `moor` already knows where you cast off from; the candle should show it — and a
candle carries the convention better than a torch does, because wax drips *down* and a lopsided
pool records which way you were facing when you stood there.

## The coloring book is the progression, not the metaphor

Don's arrival sequence — dark and monochrome, then lit, then coloured, then animated — is a
render of the verdict lattice, and the point is that **the colours are the reader's
expression rather than a completion percentage**:

```text
gloaming  →  seen  →  read  →  understood  →  annotated  →  forked
twilight     cold     warm     saturated     tinted        connected
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
