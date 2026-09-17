# Souvenirs — the universal objects, and the album that holds them

*Souvenir*, from French, "to remember" — from Latin *subvenire*, to come to mind. A souvenir's
entire job is to make something come back to you later. That is also the job of every object in
this document.

[SOUL-BRIDGES.md](SOUL-BRIDGES.md) covers who may cross a save-file border and what the
destination owes them. This document covers **what they can carry**, and the one class of thing
that crosses between *any* two games whatsoever.

## 1. The album is the floor, because it needs nothing from the game

Every other crossing needs format work. Characters need a save parser. Objects need an asset
pipeline. Zones need a tile map.

A photograph and a caption need a screen and a clock.

So the **album is guaranteed** — for a game with no album feature, a game that will never be
patched again, a 1996 DOS binary under emulation, a game whose format nobody has reversed. Every
game can be photographed. Which makes the album both the first thing to build and the last thing
you would ever lose:

| What the destination supports | What the album still does |
|---|---|
| A full bridge | Round-trips native album pages both ways; provenance carries save id, souls in frame, the exact DVR moment |
| A photo or replay mode | Imports its native captures, exports back into its format |
| **Nothing at all** | Capture, caption, narrate, publish. Provenance degrades to game plus timestamp — [degraded, not failed](../robust-first/) |

That bottom row is the whole guarantee. Nothing above it is required for a soul to come home
with something in its hands.

Cheapest crossing in the whole design, cheaper even than
[a letter to the editor](SOUL-BRIDGES.md#3-the-role-gate-entering-a-game-that-has-no-individuals):
one picture, one caption, one timestamp.

## 2. A souvenir is an object; its type is an interpretation of it

One rule holds the model together:

> **Every souvenir is an object — named properties and nothing more. Its type is an
> interpretation of those properties, not a separate way of storing them.**

Types are **self-describing** — the object says what it is — and they **multiply inherit** from
skills and capabilities rather than sitting in a single-parent class tree. A thing can be a
photograph *and* a place record *and* a receipt at once, borrowing behavior from each. Prototype
delegation, the same as everything else in MOOLLM.

The payoff is what happens on the receiving end when the type is unknown, which will be most of
the time. A world that has never heard of a type can still read the properties, keep every one it
does not understand, and pass the whole thing on intact — [accept liberally, emit
conservatively](../postel/). An unrecognized souvenir still has a title, a picture, and a date,
so it degrades to something a human can look at rather than to an error.

**Never drop unknown fields.** A bridge that discards what it cannot parse is a bridge that
skims the traveler on the way through.

## 3. The album is a polymorphic array

The album is an **ordered sequence of typed objects**, and it does not care which types. Scenes,
cards, blog posts, clips, letters, receipts, maps, portraits — sequence is the only structure it
imposes, and sequence is what turns a pile of souvenirs into a story.

Prior art, all of it the same shape: HyperCard's stack of cards, a blog's feed of posts, a
scrapbook, a commonplace book, a photo album with captions in the margin.

## 4. The Dublin Core floor

Standard metadata is a solved problem and we do not get to re-solve it. **If a field has a Dublin
Core equivalent, use the Dublin Core name.** New fields only where a souvenir genuinely has a
property the world outside games does not.

The fifteen elements of the Dublin Core Metadata Element Set (DCMI, from a 1995 workshop in
Dublin, Ohio), and what each one carries here:

| Dublin Core | Here |
|---|---|
| `title` | The caption's headline — what this souvenir is called |
| `description` | The caption body, the narration, the story |
| `creator` | Who made it: a player, a character, an assistant draft a human then edited |
| `contributor` | Everyone else with a hand in it |
| `publisher` | Who published it, if it left the album |
| `date` | When — real time, and see `coverage` for in-world time |
| `type` | **The interpretation of the object.** Scene, card, post, clip, letter, receipt |
| `format` | Media format of the payload |
| `identifier` | Stable id, so a souvenir can be cited and re-found after it travels |
| `source` | The game, save, or capture it came out of |
| `language` | For captions, and for games that speak their own (Simlish is a language) |
| `relation` | **Pointers to the people, items, and places in the scene** — the connective tissue |
| `coverage` | **Both geographies at once**: real-world GPS *and* in-game location, plus in-world time |
| `rights` | Provenance and permissions — who may republish this, and who appears in it |
| `subject` | What it is about, for search and for shelving |

Two of those do more work here than they do in a library.

**`coverage` carries two geographies.** A souvenir photographed in a game has an in-game location
(a lot, a tile, a room, a coordinate in a world that may not exist anymore) and often a
real-world one too (where the player was sitting, where a stream was broadcast from, where a
photograph was originally taken before somebody scanned it into a game). Neither substitutes for
the other, and collapsing them loses the more interesting half. Keep both.

**`relation` is what makes a souvenir more than a picture.** Pointers to the souls in frame, the
objects on the table, the place it happened, the album it belongs to, the save it cites, the
moment in the recording. This is the field that lets a photograph reunite with the character it
depicts after both have crossed into a game that has never heard of either.

Beyond Dublin Core, the additions worth standardizing are the ones about being *in a simulation*:
in-game coordinates, save identifier, the recorded moment cited, and the ids of souls present.

## 5. Types worth standardizing early

Every one of them is the same object with a different interpretation: **title, media, description,
metadata.**

| Type | What it is |
|---|---|
| `scene` | A moment: still or clip, captioned, with who and where and when |
| `card` | An album page — the unit of sequence |
| `post` | A blog entry: longer prose, published, dated, commentable |
| `clip` | Video or audio with narration; a run of these in order is machinima |
| `letter` | Correspondence — the cheapest way a voice enters a world that has no body for it |
| `receipt` | A manifest of what crossed a border, and at what exchange rate |
| `place` | A location record, in either geography or both |
| `portrait` | A depiction of a soul, citable by that soul afterwards |

More specific kinds are expected and cost nothing, because an unknown type still reads as a
titled object with a picture in it.

## 6. Why souvenirs survive customs when other things don't

[Value is world-relative and gets marked to the local market](PORTABLE-NPCS.md#6-customs-the-trolls-luggage),
and for most things the rate can be zero: a skill learned in one world may convert to nothing at
all in the next.

Souvenirs are the exception, and structurally so. A photograph with a caption and a date does not
need the destination to model photography, or skills, or economies, or anything else — it needs
somewhere to put a picture. So the thing a traveler brings home is the thing most likely to
arrive intact, which is why the enrichment a round trip promises is mostly made of souvenirs:
memories, pictures, letters, and the album they live in.

## Where this is implemented

| Layer | Home |
|---|---|
| Album schema, card model, capture and narration, per-game album bridging | [`soul-angel/SOUL-ALBUM.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/SOUL-ALBUM.yml) |
| The recording an album cites moments in | [`soul-angel/DVR.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/DVR.yml) |
| Albums as authoring tools rather than archives | [`family-album-as-storymaker.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/family-album-as-storymaker.md) |
| Imagined-forward album pages, marked as dreams | [`the-imagine-loop.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-imagine-loop.md) |
| Objects and albums as in-game artifacts | [`the-computer-as-portal.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-computer-as-portal.md) |
| Shops, pipeline, GUID registry, rights — the marketplace these are traded in | [Soul City catalog](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) |

A per-game album bridge translates vocabulary and format in both directions and **leaves the
game's own name for the feature alone.** The Sims has a Family Album; that is what it is called
there. We uplift; we do not annex.

## See also

- [README.md](README.md) — the front door, and why the tools live on this side of the bridge
- [SOUL-BRIDGES.md](SOUL-BRIDGES.md) — who crosses, and what the destination owes them
- [PORTABLE-NPCS.md](PORTABLE-NPCS.md) — advertisements, treaties, customs
- [GLOSSARY.md](GLOSSARY.md) — souvenir, Dublin Core, customs, and the rest
