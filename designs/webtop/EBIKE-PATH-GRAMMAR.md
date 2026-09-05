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
- [`skills/urban-safari/`](../../skills/urban-safari/) — the shipping pipeline: FIT rides, map JSON, video-to-GPS sync
- [DISPENSERS-AND-SOUVENIRS.md](DISPENSERS-AND-SOUVENIRS.md) — souvenirs placed on real-world maps, parameterized by your own photos
- [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) — the affordances, and the static-versus-social tiers
- [../TAGSONOMY-COMPILER.md](../TAGSONOMY-COMPILER.md) — the ground-up half: GPS-located spoken impressions as semantic seeds
- [../pie-stack-views/TEMPORAL-SEMANTIC-ZOOM.md](../pie-stack-views/TEMPORAL-SEMANTIC-ZOOM.md) — zoom applied to time

↑ [webtop hub](README.md)
