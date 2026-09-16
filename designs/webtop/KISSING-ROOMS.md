# Kissing rooms and the skein

*Direct-manipulation linking, and a name for the ordered list of scenes that has been waiting for one
across four implementations.*

Lineage: DreamScape (1995, Kaleida ScriptX) → [iLoci](../iloci.md) (2009) → MediaGraph (2010) →
Bar Karma / StoryMaker / Urban Safari. Rooms connect **by bumping them together**, and kissing them
again disconnects them. Built three times, never named properly.

Related: [`ROOM-STROLLING.md`](ROOM-STROLLING.md) · [`OPENSTROLLMAP.md`](OPENSTROLLMAP.md) ·
[`../pie-stack-views/GROOVES-AND-SPIKES.md`](../pie-stack-views/GROOVES-AND-SPIKES.md) ·
[`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md)

## The kiss, and why it beats `@dig`

A MUD builds its world with `@dig north to hall` — a command with a verb, a direction name, a
destination name, and an implied inverse you have to remember to make. Four things to get right, none
of them visible, and the undo is another command.

A kiss is: **push two rooms together until they touch.** The link appears. Push them together again and
it goes. No syntax, no names, no separate inverse, and undo is the same gesture — which makes it
quintessential direct manipulation in Shneiderman's sense: the object of the verb is the thing under
your finger, and the result is visible in the place you did it.

Two properties are worth stating because everything below depends on them:

- **The kiss is its own inverse**, so undo/redo is free and needs no command history to be legible.
- **The direction is not typed, it is derived.** Rooms touching left-to-right make an `east`/`west`
  pair; stacked, a `north`/`south` pair. Nobody names a direction, so nobody can name a wrong one.

## The skein: an ordered list that is not yet a set of links

StoryMaker and Urban Safari both need the same object — **a one-dimensional ordered list of scenes,
assembled on what is physically a Scrabble letter rack**, shareable on its own, whose members are very
often *not* connected to each other. The sequence is a claim about order. It is not yet a claim about
adjacency in the world.

Call it a **skein**.

- In textiles a skein is yarn wound in order and **not yet woven**: sequence without cloth, which is
  exactly membership without links.
- In criticism a *narrative skein* is a story strand, so it already means this to writers, which is who
  StoryMaker is for.
- A skein of geese is an ordered line of things travelling together, which is what a playlist is.
- And it takes its place in a pipeline the [cloth vocabulary](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job)
  already implies: **wool → skein → warp → web.** Raw material, ordered material, mounted and linked
  under tension, finished cloth. Those are the four states a corpus is ever in.

**The rack is the UI, the skein is the object.** If the rack wants a woven name, the tool that holds
warp threads in order and spacing while a loom is being dressed is a **raddle** — a peg rack, which is
precisely a Scrabble rack for threads. `rack` is the word to ship and `raddle` is there for whoever
wants the ornament.

**A skein is first-class and shareable, and sharing it changes nothing else.** It has an identity, it
can be published, forked, and handed over, and doing so does not touch the rooms it names. This is the
same object [OpenStreetMap calls a relation](OPENSTROLLMAP.md#the-data-model-lines-up-term-for-term):
an ordered collection of members that does not modify its members.

### Warping: turning implied order into authored links

The verb for mounting threads on a loom in order, under tension, ready to be woven, is **warping**. So:

| Command | What it does | Notes |
|---|---|---|
| **kiss** | Toggle the link between two touching rooms | The primitive. Everything else is spelled out of it |
| **warp the skein** (*link all*) | Link every consecutive pair | **Creates, never breaks.** Existing links elsewhere survive |
| **unwarp** (*unlink all*) | Break every consecutive link in the skein | Leaves non-consecutive links alone |
| **kiss/unkiss the pair** | One consecutive join | The two-item case, for hand work |

**There is no per-pair group toggle, on purpose.** Toggling each consecutive pair independently is a
command nobody wants: it turns a half-linked skein into its photographic negative, which is never the
intent. What is wanted is the group-level predicate: **if everything is already linked, break it all;
otherwise link it all.** One gesture, one meaning, and the meaning is legible from the current state.

### Smooshing is the group kiss

Select several rooms and **narrow their container** — the rooms press together, all the touching pairs
kiss at once, and on release the container animates back to the size that neatly contains them. A group
kiss, performed by squeezing.

The animation is doing real work. Squeezing shows the *cause* (they are touching, so they link) rather
than announcing the effect, and the release settling to a snug fit says *the operation is over and this
is the new shape*. It is the same physical story as the single kiss, scaled up, so nothing new has to be
learned to use it.

## One editor, in one dimension or two

The rack is not a second editor with a second interaction model. **The rack is a
[groove](../pie-stack-views/GROOVES-AND-SPIKES.md)** — a one-dimensional manifold you can dock things
to, which that design already unifies with layout and constraint — and the rooms are docked to it. Free
2-D map editing is the same kissing editor with the constraint removed. Nothing about the gesture
changes, so nothing about the gesture has to be taught twice.

That is also why **reordering preserves links**: a link is between two room identities, never between
two positions, so a permutation of the rack cannot break one. What a permutation changes is which
members are *adjacent*, and a rack must never let membership and linkage look like the same fact.

## Touching is the notation, and the gap is the measurement

**A link between neighbours draws nothing.** Two rooms that are touching are linked, and the touch says
so — which kills the clutter problem at the root, because the local links are the overwhelming majority
and a map that drew all of them would be a hairball of short high-frequency scribbles obscuring the rooms
they connect.

That frees **the gap** to carry something else: **how closely related two neighbours are**, on a coarse
ordinal scale. Coarse on purpose. Four rungs can be read at a glance without a legend; ten cannot, and a
rack has nowhere to put a legend anyway.

| Sett | Reads as |
|---|---|
| **flush** | Bound. Same argument, same scene, same block |
| **tight** | Closely related |
| **loose** | Related, weakly |
| **open** | Adjacent in this list and nothing more |

The spacing parameter has a real name in the trade: a weave's **sett** is how closely its warp threads
are spaced, coarse or fine, which is exactly this. (And a *sett* is also the cobblestone Amsterdam is
paved with, which nobody planned.) In the map view the sett spaces rooms; in the fan the same idea is
[the bloom](ROOM-STROLLING.md#slices-inside-an-arc-need-not-be-equal-the-bloom) sizing slices. One
notion, two projections.

**Size is ordinal within a category; the category is carried by the edge.** Gaps apply to linked and
unlinked pairs alike, so size alone would be ambiguous — a thin seam between linked rooms would look like
a small gap between unlinked ones. The categorical cue is structural rather than metric: **linked
neighbours share one edge, drawn once. Unlinked neighbours each keep their own edge.** One line between
them means a door; two lines with air between means no door, however little air there is.

**Relatedness is one declared dimension at a time, never a blend.** Semantic, temporal, and graph
distance are three different questions, and a spacing that silently mixes them cannot be read. So the
rack declares which dimension it is spacing by, and that dimension is an ordinary
[assessment](SIGNED-ASSESSMENTS.md) — author, target, dimension, value — not a magic number baked into
the layout.

Which makes switching dimensions a feature rather than a setting. **Re-setting the rack under a new
dimension is a comparison instrument**: the same members, re-spaced, animated, so what clusters under
*temporal* and what clusters under *semantic* is visible as motion. You are not reading two charts and
holding them in your head; you are watching one rack breathe.

## Doors and halls: what a line is allowed to mean

If touching means linked, then a drawn line is free to mean something more specific, and there is an
obvious job waiting for it:

| | Rendered as | What it is | Cost to traverse |
|---|---|---|---|
| **Docked link** | Shared edge, no line | A **door**. One threshold between two rooms | None. You step through |
| **Undocked link** | A line | A **hall**. A corridor between rooms that are not neighbours | A turn. You walk down it |

**A hall is a place, which is why the line is not decoration — it is the floor plan.** The line's length
is how far you walk. Halls can hold things, have their own doors, and grow into corpora of their own; a
long undocked link is a corridor with rooms off it waiting to be written.

Two consequences, and the second one is the reason to prefer this over drawing every link:

- **Halls need no new interaction.** Walking a hall is a mood stroll down a degenerate thread with two
  ends and nothing on the sides — which is `A = 180°`, both sides
  [moolbed](ROOM-STROLLING.md#moolb-giving-a-sides-space-away) to nothing. A corridor is a warp-faced
  region, so the geometry already had it.
- **Non-local links cost a turn, and that is correct.** Wiring everything to everything stops being free:
  a door is immediate, a hall is a walk, so a map that arranges related things *next to each other* is
  genuinely faster to move through than one held together by long-distance ties. The hairball is
  discouraged by mechanics rather than by style guidance, which is
  [procedural rhetoric](../revolutionary-chess/README.md) pointed at authors instead of players.

## Smart link dragging: what happens to a link when a room moves

Move a room from the right of its neighbour to below it and the link should migrate from the `east`/`west`
pair to the `north`/`south` pair by itself. That is the DWIM everybody wants and it is easy in the empty
case; the interesting part is the conflict.

**Links are position-derived by default and pinnable by exception.** A link stores the pair of rooms; the
sides it uses are recomputed from relative position on every move, unless an author has pinned it, in
which case it keeps its sides and draws as a crossing tie. Derived-unless-pinned is the same move
GROOVES-AND-SPIKES makes with inferred constraints being **promoted** to declared ones: infer freely,
and let anything worth keeping be nailed down deliberately.

**A side is a spike, not a slot.** GROOVES-AND-SPIKES's spike is the ordered 1-D case, and that is what
a room's edge is: an ordered rail of anchors, so a side can carry several links at once, in an order that
means something. That order is the same order the pie already uses —
[angular order is margin order](ROOM-STROLLING.md#the-gesture-is-one-pie-and-the-asymmetry-is-in-the-geometry)
— so a room's east edge, its east stubs, and its east slices are three renderings of one ordered list.

When a migrating link wants an occupied side, the policy is configurable, and all four are reasonable in
different worlds:

| Policy | Behaviour | For |
|---|---|---|
| `stack` | The side is a spike; the arriving link takes an anchor in it, ordered by position | Cities, hubs, anything with real fan-out |
| `spill` | Nearest free anchor instead: the corner first, then the next side round | Grid worlds where one link per side is the whole point |
| `pin` | Refuse to migrate; draw the link crossing | Authored maps where the sides carry meaning |
| `ask` | Stop and offer the choice, on this link, once | Editing somebody else's map |

## The rack is a spike with its windows shut

The spike is not only the primitive that solves multiple links per side. Run it the other way and it
renders a **block**: push a street's addresses onto a spike in order, then move the odd numbers' tabs to
the opposite side, and you have both sides of the road at one registration point, tabs in address order,
windows hanging off left and right and overlapping as they crowd.

PSIBER's tabs defaulted to the left of an object-view window and were draggable to any edge, which looks
like a preference until something needs to mean something by it. **Tab side is carrying which side of the
road, and only a fully general edge assignment can carry it** — tabs pinned to the top, as in every
browser, have nowhere to put the datum. The
[full argument and its consequences](../pie-stack-views/GROOVES-AND-SPIKES.md#the-spiked-block-why-a-tab-must-be-movable-to-any-side)
belong with the spike, but one of them is about this document:

> **A spike with all its windows shut is a rack.** A tab is the collapsed rung — glyph, or glyph and
> title — and an open window is a lower one, so opening and closing windows while the tabs stay put is
> [zoom and mooz](ROOM-STROLLING.md#room-strolling-mood-loom-zoom), continuous. The rack and the block are
> one object at two rungs.

Which means a skein on a rack, a block of addresses, and an operand stack from 1989 are the same object
under three loads, and the sett is what the spacing does when nothing is open.

## Diagonals, and what belongs on a corner

The four corners are the tertiary direction, after major and minor, and there are three good uses that
do not compete with each other:

- **Corner buildings.** A room at a crossroads has neighbours at 45°, and pretending otherwise distorts
  the map. This is the [hood](ROOM-STROLLING.md#the-gesture-is-one-pie-and-the-asymmetry-is-in-the-geometry)
  — the Moore neighborhood — which always had eight seats.
- **Reaching past an intersection**, where the thing you want is across and along, and the diagonal is
  the honest single move.
- **Authored-ubiquitous items**: a map's own utility submenus, always present, deliberately out of the
  way of navigation.

That last one needs a boundary, because it looks like the inner hoop's job and is not:

> **The hoop is for verbs that apply to every object in the world; a corner is for items an author
> chose to put everywhere.** `understand` is on
> [the hoop](../revolutionary-chess/AGENCY.md#understand-is-always-on-the-menu) because it is true of
> anything that exists. *This map's* tool palette is on a corner because somebody decided it should
> follow you around. Universal versus merely omnipresent, and they must not share a ring, or the
> authored items start looking like laws.

## What stays configurable, and what does not

The point of configuration here is not flexibility for its own sake. It is that a story rack, a city
map, and a memory palace genuinely want different conflict rules, and the gesture vocabulary is
identical across all three. So: **the policies are configurable, the primitives are not.** A kiss always
means toggle, squeezing always means group kiss, the corners always mean 45°, and adjacency never
silently implies a link. Everything above that line can be set per map.

---

## Related

- [`../iloci.md`](../iloci.md) — the 2009 implementation and its DreamScape ancestor
- [`ROOM-STROLLING.md`](ROOM-STROLLING.md) — navigating what this builds: the pie, the arcs, the lexicon
- [`OPENSTROLLMAP.md`](OPENSTROLLMAP.md) — the same skein as an OSM relation, over real ground
- [`../pie-stack-views/GROOVES-AND-SPIKES.md`](../pie-stack-views/GROOVES-AND-SPIKES.md) — grooves, spikes, and inference promoted to declaration
- [`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md) — why a document is a room in the first place

↑ [webtop hub](README.md)
