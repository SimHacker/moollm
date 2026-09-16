# Tours, rounds, and playlists

*A route through interesting places is a skein couched over a map. The hard part is not the routing, it
is the objective function — and the objective is dramaturgical, not metric.*

Related: [`KISSING-ROOMS.md`](KISSING-ROOMS.md) · [`EBIKE-PATH-GRAMMAR.md`](EBIKE-PATH-GRAMMAR.md) ·
[`OPENSTROLLMAP.md`](OPENSTROLLMAP.md) · [`ROOM-STROLLING.md`](ROOM-STROLLING.md) ·
[`skills/urban-safari/`](../../skills/urban-safari/)

Urban Safari did this. eBike Safari and ShowMaker do it with map points of interest and with YouTube
playlists, short-form and long.

## Embroidery is the third layer

The [cloth vocabulary](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job) has been running on two
layers: the **web**, woven, authored, versioned; and the reader's **frame**, subjective and rebound every
time somebody picks up a phone. A tour is neither. It is authored and shareable like the cloth, but it is
laid *over* finished cloth and **changes nothing underneath** — which is embroidery, exactly, and
embroidery has a precise vocabulary for the distinctions a tour needs.

| Stitch | What it is | The job here |
|---|---|---|
| **couching** | A thread laid along the surface and tacked down at intervals | The default. A route drawn continuously over the map, anchored at each stop, altering no street |
| **running stitch** | In and out: visible on top, hidden underneath, alternating | A tour that shows its stops and *hides its connections* — you took the metro between them and the route is not the point |
| **backstitch** | Each stitch reaches back to the last, no gaps | Every leg traced. What a ride track is |
| **basting** | Provisional stitches that hold things in place and come out later | A draft order. The skein before anybody [warps it](KISSING-ROOMS.md#warping-turning-implied-order-into-authored-links) |
| **appliqué** | A separate patch sewn onto the ground fabric | Foreign media landed on the map: a video, a photo, a souvenir |

Three more are in [the pool](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job) rather than spent:
**darning** (weaving across a hole — filling a missing connection), **sampler** (a piece worked to show
one of each stitch — a best-of tour), and **crewel**, which has no job and a great name.

**Why the layer distinction is not bookkeeping:** an overlay that alters nothing is precisely what
[OpenStrollMap's upstream rule](OPENSTROLLMAP.md#the-two-way-protocol) demands. A tour is somebody's
opinion about order and worth. It gets published, forked and argued with, and the map it is stitched over
never notices.

## A tour, and a round

A tour is a [skein](KISSING-ROOMS.md#the-skein-an-ordered-list-that-is-not-yet-a-set-of-links) with a
route couched under it. **A round is the closed case** — a postman's round, a milk round: an ordered
circuit, walked again tomorrow. A musical round loops too, which is the same shape in another medium, and
a closed tour is a `loop`, which the lexicon already has.

Open tours end at a destination. Rounds return, which makes them repeatable, comparable across days, and
the natural unit for *this is my Tuesday*.

## The travelling salesman is the wrong objective

Shortest-path-through-all-points is the classic framing and it produces bad tours. A guide is not trying
to minimize distance; it is trying to be worth doing. Optimizing for length yields the efficient
enumeration of a list, which is what a delivery van wants and no visitor does.

The real problem is a **routing problem with time windows**, and the constraints are all mundane:

- **Opening hours.** A stop is only a stop while it is open, and half of an itinerary's difficulty is
  arriving in the right order to catch things.
- **Legal, rideable ways.** One-way streets, cycle paths, bridges, stairs — a real graph search over
  [OSM's cycling network](OPENSTROLLMAP.md#the-data-model-lines-up-term-for-term), not straight lines.
- **Effort and weather.** Elevation, wind direction, and the fact that a headwind on the way home is a
  different ride from a headwind at the start.
- **Daylight**, which is a hard window in Amsterdam in December.
- **Bridge openings**, which are already a named, recurring, duration-estimated
  [context](EBIKE-PATH-GRAMMAR.md#velocity-sets-the-level-of-detail) in this design.
- **A time budget**, because the tour is two hours whether or not the optimum is three.

Nearest-neighbour plus 2-opt over that graph produces good tours, and the solver is not where the design
effort belongs. **The objective function is.**

### The objective is dramaturgical

Order is a claim — that is the whole reason a skein is its own object — so **a tour's order is a story
decision**, and this lineage has been here before: StoryMaker and Bar Karma were about assembling scenes
into a sequence that works, with the rack as the instrument.

What a good tour wants, and each of these is measurable enough to score:

| Property | Proxy |
|---|---|
| **An opener that establishes** | Start somewhere legible and characteristic, not the nearest thing to the door |
| **Variety** | Penalize runs of the same place type. Three churches in a row is a worse tour than three interesting things in a row |
| **An effort curve** | Climbs early, flat late. Distance-weighted by elevation and by hour |
| **Rest after dwell** | A long stop earns a short next leg. Duration and distance trade against each other |
| **Something that lands** | Reserve one stop as an ending rather than letting the route decide which is last |
| **Affinity** | Reader-specific weight from [signed assessments](SIGNED-ASSESSMENTS.md), not from a global popularity score |

So the score is a weighted sum of rideability, budget fit, variety, pacing, and affinity — with **the
weights in the reader's frame and the candidate set in the corpus.** Two people asking for the same
two-hour tour of the same neighbourhood should get different tours, and neither should be the shortest
one.

## A playlist is the same object with durations instead of distances

Both are one-dimensional, ordered, budgeted, and edited on the same
[rack](KISSING-ROOMS.md#the-rack-is-a-spike-with-its-windows-shut). Swap arc length for running time and
every argument above survives: variety, pacing, an opener, an ending, a rest after a long one. The
[sett](KISSING-ROOMS.md#touching-is-the-notation-and-the-gap-is-the-measurement) can space items by
duration, so a playlist's shape is visible before it is played.

**Short-form and long-form are two rungs of one place, not two items.** This is the useful claim for
ShowMaker: a short *is* the glyph-or-trailer rung of the thing whose body is the long-form video. So a
mixed playlist is a multi-rung skein, and the pyramid already knows what to do —
[mooz out](ROOM-STROLLING.md#room-strolling-mood-loom-zoom) and the run plays as shorts, zoom in on any
one and the full version arrives. Nobody has to maintain two playlists, and the shorts stop being a
separate content strategy and become a level of detail.

## The guide part needs no new machinery

A tour guide is three things this design already has:

1. **A couched route** — the skein, drawn over the map, anchored at its stops.
2. **A [moor](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job) at each stop** — a tied-up reading
   cursor, resumable, so a tour can be abandoned and picked up next week.
3. **Narration at the bottom rung** — which is
   [what stopping already does](EBIKE-PATH-GRAMMAR.md#stopping-rolls-down-the-pyramid-until-it-is-an-interface):
   dwell rolls continuously down the pyramid until the place is a room you are standing in, and the guide's
   voice is simply what that room says when you arrive.

And it works with no bicycle involved, because [the path object does not care whether a body traversed
it](EBIKE-PATH-GRAMMAR.md#resumption-git-on-wheels): the same tour is a plan before, a ride during, and a
story afterwards.

## Open questions

- **What happens to a tour when the map moves?** A stop closes, a bridge shuts for a year. A skein of
  fixed IDs is stable and goes stale; a skein of queries stays fresh and stops being reproducible. Both
  are wanted, so a tour probably has to declare which of its members are pinned and which are slots.
- **Who owns the weights?** The objective is per-reader, but a *published* tour is somebody's authored
  artifact and re-scoring it for a new reader is no longer their tour. There is a real difference between
  taking a tour and generating one, and the interface should not blur it.
- **Does a short count against the budget?** If a short is a rung rather than an item, a playlist's
  running time depends on which rung is playing, so the budget is not a property of the skein at all.

---

↑ [webtop hub](README.md)
