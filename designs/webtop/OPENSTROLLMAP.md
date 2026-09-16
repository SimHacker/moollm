# OpenStrollMap

*The navigable mind-mirror of OpenStreetMap: a subjective frame over the world's best objective map,
with a firm rule about which facts go where.*

Related: [`ROOM-STROLLING.md`](ROOM-STROLLING.md) · [`EBIKE-PATH-GRAMMAR.md`](EBIKE-PATH-GRAMMAR.md) ·
[`KISSING-ROOMS.md`](KISSING-ROOMS.md) · [`SIGNED-ASSESSMENTS.md`](SIGNED-ASSESSMENTS.md) ·
[`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md)

## Why it has to be a separate layer

OpenStreetMap has a governing principle and it is the right one: **verifiability.** What goes in is what
another mapper could go and check on the ground. That rules out, deliberately and permanently, most of
what a stroll is made of — that this street is worth riding twice, that the light here is good at seven,
that you stopped for eleven minutes and it was the best eleven minutes of the ride.

So this is not a fork of OSM and not a campaign to loosen its standards. It is the
[frame over the cloth](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job), one layer up: OSM holds
what is true of the ground, OpenStrollMap holds what is true of a reader. The split is the same one that
runs through all of this, and OSM's community drew it first and enforces it better.

**Mind mirror** is the honest description of the upper layer, in Leary's sense —
[`SIGNED-ASSESSMENTS.md`](SIGNED-ASSESSMENTS.md) already argues that a rating is an
**assessment record**: author, target, dimension, value, date, evidence, signed and free to conflict,
never universal metadata bolted onto a shared node. That constraint was derived for a corpus and it turns
out to be exactly the constraint OSM's verifiability rule imposes from the other direction.

## The data model lines up term for term

The correspondence is not analogy. OSM's primitives are the ones this design has been reaching for:

| OSM | Here | Note |
|---|---|---|
| **node** | a place, and its [eroom](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job) | The intersection is the node; the eroom is the room that stands for it |
| **way** — an *ordered* list of nodes | a [warp thread](EBIKE-PATH-GRAMMAR.md#a-ride-is-a-warp-thread-and-the-city-is-what-crosses-it) | A street is already a sequence with an arc length. Nobody has to invent the major axis |
| **relation** — ordered members with roles, modifying nothing | a [skein](KISSING-ROOMS.md#the-skein-an-ordered-list-that-is-not-yet-a-set-of-links) | Membership without linkage, shareable on its own, exactly as designed. OSM's route relations are skeins of ways, and the national and regional cycle networks are skeins somebody already curated |
| **tags** — free `key=value`, conventions grown on a wiki | a [tagsonomy](../TAGSONOMY-COMPILER.md) | A planetary-scale folksonomy with no fixed schema that nonetheless converged. The prior art for the compiler is the whole of `addr:*` and `highway=*` |
| **changesets, version history, permanent IDs** | provenance | Who changed what, when, and why, per object, forever — the same argument [Git makes about Xanadu](../../indexes/XANADU.md), made about places |
| **notes** | a [moot](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job) at a place | An open question anchored to a location, which is what a moot is |

Two consequences fall out immediately. **Addresses come with their side of the street**, because
`addr:housenumber` carries the parity that already
[tells you which way to flick](EBIKE-PATH-GRAMMAR.md#what-the-weft-is-made-of-depends-on-where-you-are-on-the-block).
And **a skein does not need inventing as a storage format**, because a relation is one, which means a
stroll can be published as an ordinary OSM-shaped object even when its *contents* stay private.

## What the frame adds

Everything subjective, per-reader, and rebound whenever somebody picks up the phone:

- **Moors** — [reading cursors](READING-CURSORS.md) tied to places, with history, resumable.
- **Strolls** — skeins of places with the [ride grammar](EBIKE-PATH-GRAMMAR.md) attached: pauses, speeds,
  crossings, what you said out loud.
- **Blooms** — [proximity-weighted attention](ROOM-STROLLING.md#slices-inside-an-arc-need-not-be-equal-the-bloom),
  which is a fact about where you are, not about the street.
- **Assessments** — signed, owned, conflicting, compiled into an index rather than averaged into a score.
- **Gloom** — the parts you have not ridden. A property of a reader, not of a city, and the single most
  useful thing to render that OSM cannot hold.

## The two-way protocol

The layering earns its keep by making the round trip explicit, and by being strict about direction:

**Upstream, and welcome:** a bike path that exists and is not mapped, a shop that has closed, a bollard,
a surface that is cobbles and says asphalt. Verifiable, checkable by the next person, and a ride track is
good evidence for exactly this class of correction. A stroll app should make contributing this trivially
easy and should count it as the price of admission.

**Never upstream:** ratings, moods, dwell times, routes you liked, anything about a rider. Not because it
is worthless — it is the entire point of the upper layer — but because it is unverifiable by
construction, and pushing it down would corrupt the commons this whole design depends on. The
[three privacy gates](EBIKE-PATH-GRAMMAR.md#privacy-is-an-editing-problem) apply with full force, and the
middle one is [groom](ROOM-STROLLING.md#two-layers-and-every-word-gets-one-job).

## The name

**OpenStreetMap → OpenStrollMap**, one letter, the same trick as `scroll → stroll` and for the same
reason: keep everything that works and change what the strip is made of. The street is the objective
thing that is there for everyone. The stroll is what one person did along it, and it is nobody else's to
average.

---

↑ [webtop hub](README.md)
