# The eBike Safari path grammar

*Don Hopkins · September 2026*

**Thesis:** a ride track is a [reading cursor](READING-CURSORS.md) whose substrate is a city. Same
type — a position with state and history that moves — and therefore the same affordances: resumption,
branching, inventory, notes, privacy. What is different is that the substrate is physical, which
means **the path itself is legible as gesture**, and the reader's body supplies signal that no
scroll position ever could.

The data pipeline exists: [`skills/urban-safari/`](../../skills/urban-safari/) already turns FIT
rides into map JSON with video keyframes as paths over the track. This is the layer above it — what
the path *means*.

**eBike Safari is a lot more than Foursquare on wheels.** Foursquare records that you were at a
place. This records how you arrived, how fast, which way you were facing, how long you stopped, what
you crossed, what you said out loud, and what you came back for.

---

## The ride track is a browser history with a body

A path is a sequence of positions with fine-grained GPS, timestamps, **object references, and
parameters at those locations** — which is precisely the structure of a browser history that never
throws away the interesting parts. The parallel is exact enough to steal from in both directions.

And a rider needs what a reader needs: accumulate the path, and along it, **what you did, what you
looked at, what you read, what you thought, what you agreed or disagreed with, and what you had
questions about.** Position without any of that is a GPX file, which is to a ride what a list of
visited URLs is to having read something.

## Gestures: the path is a command surface

The strongest thing the physical substrate gives you is that **movement has recognizable shape**, and
shape can be parsed.

| Gesture | Reading |
|---|---|
| Riding around a roundabout | a recognizable circuit — a deliberate mark, not noise |
| Riding it the wrong way | recognizable *and different*: a natural **undo** of the effect of riding around |
| **Pausing** | the most important one, and the richest |
| Going past, turning back, returning slowly | a request for detail about what you just passed |
| Crossing your own recent path | an event worth analyzing on its own |

**Pausing is the primary gesture** because duration and surroundings together are nearly enough to
infer intent. How long did you stop, and what is around you? A traffic light is not a canal bridge is
not sitting under a tree in a park eating lunch is not taking a Zoom call. Cross-reference the photo
library at that timestamp and location and the inference sharpens: maybe you were taking a photo,
reading a sign, or photographing a sign in Dutch in front of a building — which is a well-formed
request to translate it and tell you the building's history, issued by stopping and pointing a camera.

### Velocity sets the level of detail

At speed, resolving your surroundings address-by-address is wasted work: you will not be there long
enough for it to matter. Slow down, turn back, and go past again, and the same location deserves
fine-grained *"where am I and what is closest to me"* treatment. **Speed is the register dial** — the
same `SUPERBRIEF`/`BRIEF`/`VERBOSE` rung selector, driven by the body instead of a keystroke, and
requiring no interface at all.

Stopping is what unlocks lookup. *Oh, this is a bridge — you may be waiting for it to close, as you
have many times before. How long is the usual wait?* Now you are in **waiting-for-bridge context**,
which is a declared, named situation with a duration estimate and a history, and the only question
left is what the rider has said they want in it. A game? Email? Nothing? That is exactly the
situation an LLM is good at planning inside: rich, bounded, recurring, with stated preferences.

### The receipt: Selker's dwell time, and pie menus

This is not speculation about intent inference; the mechanism has been built twice.

**Ted Selker demonstrated a system that watched how long you pointed at items on a web page**, and
after you selected one, used the dwell times to guess which items you would be interested in next.
Attention leaks through hesitation, and hesitation is measurable without asking.

Don reimplemented the idea **in pie menus, measuring how long you linger in each slice** — so after
you pick your favorite color, the menu can guess your second favorite. A pie menu is a good place for
this because the slices are equidistant and the dwell is not confounded by travel distance, which is
the flaw in measuring hover on a linear list.

Lingering on a bike is the same signal at a different scale, and the same caution applies to both.

## Privacy is an editing problem

Timing and lingering are among the most private data a person emits, and among the most useful to
that same person. The resolution is not to collect less but to **make the sharing pass an explicit
edit**, filtered and abstracted before anything leaves.

The concrete requirements:

- **Elide by geography.** Ride segments near home, work, or any location the rider does not want
  revealed must be removable, and removable *by rule* rather than by remembering each time. Strava's
  privacy-zone handling is the prior art to study, including its known failure modes — a zone that
  hides the endpoint but leaves every approach vector visible does not hide the endpoint.
- **Rides start where you say they start.** Explicitly beginning a ride somewhere other than your
  door is the low-tech version of the same control, and it works.
- **Three gates, not one:** whether it is recorded at all, what is kept after curation, and what is
  published. Systems reliably implement the first and third and omit the middle.

The corresponding argument for reading traces is in
[READING-CURSORS.md](READING-CURSORS.md#honest-costs); it is the same requirement, and the ride
version is worse because the trace is of a physical body in a real city.

## Voice is the annotation channel

Riding occupies the hands and eyes, which rules out every note-taking interface that has ever
shipped. Recording video and audio of the ride solves it, provided the audio is **parsed rather than
merely archived** — spoken utterances become edit decisions, annotations, tags, keywords, questions
to answer later, todo notes to return when there is time, take-a-photo commands, try-this-restaurant
markers, see-this-show reminders.

This is the same slurp-into-your-outline mechanism as
[reading notes](READING-CURSORS.md#outlines-with-their-own-insertion-cursors-the-student-model), with
speech as the input method and the city as the document. The insertion cursor is still an insertion
cursor; you just cannot see it while you are riding.

## Resumption: git on wheels

At a location — or before you get there — the choice is the same three every time:

| Move | What it is |
|---|---|
| **Start a new ride** | a new branch from nothing |
| **Resume the existing ride from its end** | continue on the tip |
| **Branch out from an existing ride** | fork at a point that is not the tip |

That is repositories, branches, forking, and merging, on wheels. And the same three moves work with
no bicycle involved: planning a ride, riding transit, or telling the story of a ride from a thousand
miles away. The path object does not care whether a body traversed it yet.

### Pauses are the natural cleavage points

A path needs to be cut into segments, and **pauses are where the joints already are** — which makes
segmentation automatic rather than a chore. Once segmented, a set of DWIM navigation moves falls out,
and these are the ones worth having by default:

- *"Resume on the next outgoing path from the time of the incoming path"* — the common case, stated
  as one command.
- **Enumerate incoming and outgoing paths by time** at any location, and pair them by adjacent
  timestamps or by opposite directions. Most of what a rider means by "where did I go from here" is
  answered by that pairing.
- **Recognize crossings.** Paths cross other paths at intersections; a path crosses *itself* when you
  ride around a block, or go down and come back up.

**Every self-crossing is an interesting event.** It invites analysis of the path and the locale, and
it can legitimately be parsed as a command, a selection, a focus, or a request for more information —
because a person who has just returned to a point they were recently at has almost always done so on
purpose.

## A ride is a warp thread, and the city is what crosses it

[ROOM-STROLLING.md](ROOM-STROLLING.md) works out the mobile navigation model on a room graph: a
**major axis** whose neighbours stay glued on screen (`mood`), a **minor axis** of off-screen
destinations reached by leaving (`loom`), and a weaving vocabulary for the substrate underneath. A ride
is the same model with a better-behaved major axis, because **a ride supplies its own coordinate
system**: elapsed time, or arc length along the track. Monotonic, unbroken, and authored by the act of
riding it.

So the ride is a **warp thread**. Scrubbing forward and back through it is `mood` — continuous, with
what came before and after still on screen. Everything the city offers is **weft**: it crosses the
thread rather than running along it, and it is not visible ahead of itself.

And this is where the metaphor stops being a metaphor. **A season of rides over one city is a woven
cloth.** Each ride is a thread; the intersections are the picks where threads cross; the fabric is what
accumulates. Nobody wove it on purpose, which is exactly what makes the crossings worth something —
they are the places where a reader can leave one thread for another without being told they may.

### What the weft is made of depends on where you are on the block

A street has two kinds of position on it, and they offer different weft. This is not a refinement of the
model, it is the model: **`loom` means something different mid-block than it does at a corner.**

**On a block, the weft is the two sides of the street.** Left and right, and that is the whole fan:
addresses, shopfronts, doorbells, a bench, a canal. Exactly two directions, each keeping a
[full 90° quadrant](ROOM-STROLLING.md#the-gesture-is-one-pie-and-the-asymmetry-is-in-the-geometry) — the
most forgiving case there is, where any sideways flick lands and aim is irrelevant. And the numbering
system already tells you which way to flick, because **house numbers are odd on one side and even on the
other**: the address *is* the direction. Nobody designed that as an interface and it works as one.

Drawn as a map rather than as a fan, that is
[a spiked block](../pie-stack-views/GROOVES-AND-SPIKES.md#the-spiked-block-why-a-tab-must-be-movable-to-any-side):
the addresses pushed onto a spike in order with the odd numbers' tabs moved to the far side, which is both
sides of the street at one registration point and is also, with every window shut, a
[rack](KISSING-ROOMS.md#the-rack-is-a-spike-with-its-windows-shut).

The addresses do not fan out angularly, they arrive in sequence — they are ordered along the thread,
not around the circle. At any instant the fan holds the nearest one on each side, and how many others
resolve is [set by speed](#velocity-sets-the-level-of-detail). Riding a block fast is one door per side;
stopping is the whole doorbell panel.

### The bloom rides with you

The addresses on a side do not deserve equal slices, because you are not equally near them. Weight each
one by proximity and the side arc becomes a
[fisheye](ROOM-STROLLING.md#slices-inside-an-arc-need-not-be-equal-the-bloom): the shopfront you are
passing takes the widest slice, its neighbours less, the far end of the block a sliver. Since
[angular width buys rungs](ROOM-STROLLING.md#slices-inside-an-arc-need-not-be-equal-the-bloom), that is
not just an easier target but a more legible one — the place beside you can afford its name and a line
about what it is, while the one at the corner gets a glyph.

**And the bulge travels.** It is a wave moving along the fan at exactly your speed, because the thing
driving it is your position, which is the property that keeps it honest: the macOS Dock bulges under the
*pointer*, so its targets grow because you reached for them, and the growth moves them as you arrive. A
bloom driven by the road grows things because you rode up to them. You always knew it was coming, and
your thumb had nothing to do with it.

**Which side blooms is set by which way you are facing.** Turn toward the shopfronts and that side blooms
while the other [moolbs](ROOM-STROLLING.md#moolb-giving-a-sides-space-away), handing its angle back so the
side you are looking at can have the sweep. Turning is the whole gesture, there is nothing to press, and
[yaw was the focus input the fisheye needed](ROOM-STROLLING.md#three-rotations-and-only-one-of-them-is-portrait-versus-landscape).
Three cautions, all of them physical:

- **Detent the sides, with hysteresis.** A bike wobbles and a hand shakes; the side must not flip because
  you swerved around a parked car. Friction at the crossover, as everywhere else in this cluster
  ([FRICTION-FIELDS](../pie-stack-views/FRICTION-FIELDS.md)).
- **A mounted phone reports the bike's heading; a held one reports yours.** Different signals, both
  useful, and the system should know which it has — turning your head toward a shop while the bike points
  down the street is exactly the interesting case, and a handlebar mount cannot see it.
- **Magnetometers lie near tram wires, steel bridges and parked cars**, which is to say all over
  Amsterdam. Heading wants fusing with the track's own bearing, and disagreement between them is itself a
  signal worth reading.

### Stopping rolls down the pyramid until it is an interface

Speed already picks the rung. Coming to rest in front of an address should not stop at *more detail* — it
should keep going, continuously, in one motion: the slice widens, the name gains a description, the
description gains hours and a rating, and then it crosses the last rung and **the address is a room you
are standing in**. Look at the menu. Order the pizza. Book the room upstairs. Progressive disclosure with
no dialog anywhere in it, driven by nothing but where you stopped, which way you turned, and how long you
stayed.

That last rung is where the [eroom](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job) earns its
name: the intersection is in the city, the eroom is in the corpus, and lingering in front of a door is how
you get from one to the other. It is also the cleanest reading of the pause we already have — **a pause is
a moor**, and mooring in front of a shop is a request to enter it.

The way back out is the reversal: [mooz](ROOM-STROLLING.md#room-strolling-mood-loom-zoom) out of the room,
and the bloom relaxes as you roll away.

**At an intersection the weft is roads, and taking one rotates your coordinate system 90°.** That is
the difference that matters, and it is why turning feels like a larger act than stepping into a shop:

| Where | Weft is | What taking it costs |
|---|---|---|
| **Mid-block** | Addresses and POIs on the two sides | Nothing. You enter, look, come back out facing the same way; the thread holds your place. A door is a leaf, and **doors do not rotate you** |
| **At an intersection** | The crossing roads | The frame. The new street becomes `mood`, the old street becomes weft, and its addresses become things you now cross rather than things you pass. **Roads rotate you** |
| **Anywhere, in time** | Your own other passes through this point | Nothing in space, all of it in time. Same place, different when — which is what makes [every self-crossing an event](#pauses-are-the-natural-cleavage-points) |

The rotation is not a metaphor for a rotation. It is
[`rotate_world`](ROOM-STROLLING.md#rotation-the-cloth-does-not-turn-the-loom-re-mounts-it) — the full
90° relabel, `north`→`east`→`south`→`west` — with the trigger moved from the phone's accelerometer to the
rider's handlebars. Turning a corner and turning the phone do the same thing to the frame, which is a
correspondence worth having on purpose: one policy, two ways to invoke it. Every navigation app already
knows this distinction and expresses it in its verbs. It says **turn** for a road and **arrive** for an
address.

A crossroads is, in the older sense, a **rood** — the cross itself, and the quarter it makes. Wayside
crosses stood at crossings for the ordinary reason that a crossing is where a traveller has a decision
and needs a mark. That is the same job an edge stub does. A four-way is the rood exactly, four cardinals
and nothing else, which the CA people call a
[von Neumann neighborhood](ROOM-STROLLING.md#the-gesture-is-one-pie-and-the-asymmetry-is-in-the-geometry);
Amsterdam's oblique canal crossings, where five or six ways meet at whatever angle the water chose, are
the **hood** — Moore, diagonals included, and the same eight seats were always in the pie.

### Traffic circles are pie menus, and not by analogy

Every property of a pie menu is physically present in a roundabout, which is why they are easy for
locals and confusing exactly where pie menus would be:

| Roundabout | Pie menu |
|---|---|
| Enter, then exit by heading | Angle selects the item |
| Exits are unevenly spaced around the circle | Slice widths follow the destinations, not a grid |
| Go around again because you were not sure | **Reselection** — nothing commits until you leave ([RESELECTION](../pie-stack-views/RESELECTION.md)) |
| A local takes the exit without slowing or looking | **Click-through** — the expert never sees the menu |
| Exit where you came in | Cancel. A 360° stroke back to the origin, which is what a U-turn is |
| Inner lane for later exits, outer lane for the first | **Radius pre-commits an angular range** ([RADIAL-DIMENSIONS](../pie-stack-views/RADIAL-DIMENSIONS.md)) |
| Mini-roundabout with one real exit | A single-item pie: any stroke lands it, aim is irrelevant |

The lane convention is the interesting one, because it is a radial dimension that millions of people
already have in their bodies: **how far in you ride encodes how far around you intend to go.** Nothing
in a screen pie menu currently exploits that as directly, and a roundabout is the field test.

Riding a roundabout the wrong way stays what the gesture table above already says it is — an undo — and
now has a reason: circulating against the grain unwinds the pick instead of laying it.

### Two frames over one cloth, and the query that falls out

A point in a city belongs to at least two threads, and which one is `mood` is a choice about mounting,
not about the city:

- **With the grain of a ride** — follow one afternoon in order. This is the frame every GPX viewer has.
- **With the grain of a street** — follow one street across every ride that ever crossed it. *Every
  time I have crossed Prinsengracht, in order, at this spot.* Cross-grain reading, and no ride app
  offers it, because the ride is assumed to be the only thread.

Both are strolls over the same web with the loom mounted differently. The second is the one that turns
years of tracks into a place rather than a pile of afternoons.

### The rest of the vocabulary was already here

- **A pause is a moor.** Tying up: the [primary gesture](#gestures-the-path-is-a-command-surface) already
  is the pause, and what you moored to is inferable from duration, surroundings, and the photo library
  at that timestamp.
- **The track is a spool.** GPS points wound on a thread, materialized around wherever the scrub head
  currently is, kept warm just off screen in both directions.
- **Velocity is `zoom`.** [Already argued above](#velocity-sets-the-level-of-detail): speed picks the
  rung, so the register dial needs no interface.
- **A stoop is where you dwell without entering.** Amsterdam supplies the word and the thing: the steps
  in front of a door are public, sittable, and not inside. That is peek-on-drag with a physical
  referent — the pause at an address that has not committed to the address.
- **Distance along a thread is measured in smoots.** Not a joke: the Harvard Bridge is painted in units
  of one undergraduate, and the result is a path whose every position has an address in a unit that only
  means anything on that path. A ride's arc length is the same kind of coordinate.
- **`oops` is undo**, which is what riding the roundabout backwards already meant above.
- **An eroom is the room standing for the place.** `Moore` reversed, and the distinction is needed the
  moment a ride is scrubbed from a couch: the intersection is in the city, the eroom is in the corpus,
  and only one of them has a commit history.
- **`groom` is the missing middle gate.** [Three gates, not one](#privacy-is-an-editing-problem) —
  record, groom, publish — and the one systems omit is the one that had no name.
- **`gloom` is the city you have not ridden.** Streets that exist, unlit, past the ends of the spool.
  Filling it in is the actual game, and a map that renders it as blank rather than as dark is lying about
  what it knows.
- **`doom` on wheels is turn-by-turn.** A blue line issuing imperatives, which gets you there without
  ever teaching you the city, and leaves nothing addressable behind. The whole point of recording rides
  as threads is that the trip survives as something you can navigate rather than something you obeyed.

## The same thing in four media

eBike Safari, gwern.net, Don's own corpus, and a Scott Adams-style life's-work-as-playable-adventure
are **instances of one design** with different parameters. They share the ideas, the problems, and
most of the solutions; they diverge on media type, audience, structure, and time scale.

| | Substrate | Grain | Time scale |
|---|---|---|---|
| eBike Safari | a city | GPS fix, second | a ride, a season, years of rides |
| gwern.net | an essay corpus | paragraph, anchor | a session, a resumption, a decade of revisions |
| A life's-work adventure | a biography | episode, artifact | a life |

What transfers unchanged: the cursor, the path as history, inventory, notes at a register,
resumption and branching, privacy as an editing pass, and the two-tier static/social split. What is
specific to each: the gesture vocabulary, the segmentation rule, and what counts as a place.

---

## Related

- [READING-CURSORS.md](READING-CURSORS.md) — the same object with a document as its substrate
- [ROOM-STROLLING.md](ROOM-STROLLING.md) — the navigation model this section instantiates: `mood`/`loom`/`zoom`, warp and weft, and the pie geometry a roundabout turns out to implement
- [`skills/urban-safari/`](../../skills/urban-safari/) — the shipping pipeline: FIT rides, map JSON, video-to-GPS sync
- [DISPENSERS-AND-SOUVENIRS.md](DISPENSERS-AND-SOUVENIRS.md) — souvenirs placed on real-world maps, parameterized by your own photos
- [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) — the affordances, and the static-versus-social tiers
- [../TAGSONOMY-COMPILER.md](../TAGSONOMY-COMPILER.md) — the ground-up half: GPS-located spoken impressions as semantic seeds
- [../pie-stack-views/TEMPORAL-SEMANTIC-ZOOM.md](../pie-stack-views/TEMPORAL-SEMANTIC-ZOOM.md) — zoom applied to time

↑ [webtop hub](README.md)
