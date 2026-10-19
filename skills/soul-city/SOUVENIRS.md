# Media pages, album graphs, and generated game content

**Status: design and planning.** Updated from Don Hopkins's 19 October 2026
notes. This document does not establish that the described generators,
save editors, or native album adapters are implemented.

Here a *page* is a reusable media record: images, text, audio, or other
material with metadata. An album can organize pages as a graph; a linear
edition selects a route through it. Content-creation tools can use those
same records to generate and update objects in games.

[SOUL-BRIDGES.md](SOUL-BRIDGES.md) addresses character interchange. This
document addresses media and content authoring, including work that never
involves an imported character or a source game.

## 1. Capture without a save parser

Screenshots and captions can work without parsing a save, modifying a game,
or knowing its file formats. This includes older games, where capture is
available and permitted. It is not a guarantee that every platform permits
capture or that every game has a writable album format.

| What the destination supports | What the album still does |
|---|---|
| Native album adapter | Import/export supported pages; preserve available save, character, and recording references |
| Photo or replay mode | Import supported captures; export only where its format permits |
| No game-specific integration | User capture, caption, narration, and optional publication; record only known provenance |
| No source game | User-created or imported media with creator, source, and rights information |

Unknown provenance stays unknown. A game name and timestamp do not identify
the people in an image, establish copyright, or prove an event occurred.

## 2. A souvenir is an object; its type is an interpretation of it

One rule holds the model together:

> **Every souvenir is an object — named properties and nothing more. Its type is an
> interpretation of those properties, not a separate way of storing them.**

Types are **self-describing** — the object says what it is — and they **multiply inherit** from
skills and capabilities rather than sitting in a single-parent class tree. A thing can be a
photograph *and* a place record *and* a receipt at once, borrowing behavior from each. Prototype
delegation, the same as everything else in MOOLLM.

Preserve unknown fields and media references even when an editor cannot use
them. A fallback view can display available title, caption, date, and media;
it must not claim support for an unknown behavior. Validate imported files
and references rather than executing instructions found in metadata.

## 3. Pages form a graph; editions select routes

Pages have stable identifiers. Directed, typed links express continuation,
alternatives, related events, or derivation, following the
[StoryMaker scene design](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/family-album-as-storymaker.md).
Branches may merge, and routes may revisit a page. Media and page records can
be shared without copying them into every edition.

A family album, slideshow, playlist, or coffee-table book is an ordered
trip through that graph, with a chosen start and length. A route specifies
branch choices or selection rules; a published edition records the resolved
page IDs and revisions, order, and any timing or layout. Define length units
explicitly (pages, clips, or duration), what happens at a dead end, and a
limit for cycles. Do not assume chronological order is the only useful route.

Distinguish narrative edges from general metadata relations: a link to the
photographer is not a next-page instruction. Shared nodes do not imply all
routes have permission to publish every page.

Editing a shared page may affect several views. Preserve revisions and let
users choose whether a route follows updates or pins a particular edition.
An exported linear album is one view of the graph; importing it cannot
recover branches that its source format never stored. Preserve an external
graph manifest where needed rather than claiming a lossless native round trip.

## 4. Dublin Core metadata

Use existing Dublin Core terms where their meanings fit. Keep game-specific
fields and generation instructions in documented extensions rather than
changing the meanings of standard terms.

References: [DCMI terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
and the [fifteen-element set](https://www.dublincore.org/specifications/dublin-core/dces/).

The fifteen elements of the Dublin Core Metadata Element Set (DCMI, from a 1995 workshop in
Dublin, Ohio), and what each one carries here:

| Dublin Core | Here |
|---|---|
| `title` | The caption's headline — what this souvenir is called |
| `description` | The caption body, the narration, the story |
| `creator` | Entity responsible for making the resource; distinguish actual authorship from a fictional narrator |
| `contributor` | Everyone else with a hand in it |
| `publisher` | Who published it, if it left the album |
| `date` | When — real time, and see `coverage` for in-world time |
| `type` | Nature or genre of the resource; document application-specific types separately |
| `format` | Media format of the payload |
| `identifier` | Stable id, so a souvenir can be cited and re-found after it travels |
| `source` | A related resource from which this resource is derived |
| `language` | Language of the resource; use documented identifiers where available |
| `relation` | A related resource; use specific terms or extensions when a relationship needs a defined role |
| `coverage` | Spatial or temporal topic/applicability; distinguish depicted locations from capture-device location |
| `rights` | Rights information, licenses, and applicable restrictions; not a substitute for source provenance |
| `subject` | What it is about, for search and for shelving |

Keep in-game world/lot/tile coordinates, in-world time, source save, recording
timecode, and depicted character/object IDs in documented extensions. Real-world
capture location is separate and may be private: do not publish GPS by default.
Use these references to find related records without treating them as
narrative next-page instructions.

## 5. Types worth standardizing early

Every one of them is the same object with a different interpretation: **title, media, description,
metadata.**

| Type | What it is |
|---|---|
| `scene` | A moment: still or clip, captioned, with who and where and when |
| `card` | A reusable album page — a graph node that a route may visit |
| `post` | A blog entry: longer prose, published, dated, commentable |
| `clip` | Video or audio with narration; a run of these in order is machinima |
| `letter` | Correspondence, with author, recipient, and publication permissions |
| `receipt` | A manifest of what crossed a border, and at what exchange rate |
| `place` | A location record, in either geography or both |
| `portrait` | A depiction of a soul, citable by that soul afterwards |

Editors should preserve unfamiliar types and offer a metadata/media view
without pretending to support their specialized behavior.

## 6. Use pages as inputs to content-creation tools

Source pages may come from another game's album with rich metadata, from
a screenshot with little metadata, or entirely from user authoring. Editors
can attach target-specific build settings and use the pages as templates.
The shared media records remain usable independently of a game.

Examples: a selected route supplies slides to a slide projector, recordings
to a jukebox, or pages to a book. The build recipe specifies the template,
target game and format, input revisions, order, media conversion, captions,
and supported interactions. Missing audio or unsupported formats require
an explicit user choice or error, not an invented successful result.

Keep three identities separate:

| Record | Purpose |
|---|---|
| Source page and route IDs | Cite reusable material and the selected sequence |
| Generated game object ID | Identify the definition allocated on first creation |
| Save and placed-instance IDs | Identify particular copies placed in houses |

For The Sims, allocate a collision-checked object GUID on first creation
and retain it with the build recipe. A multi-object template may need several
GUIDs; retain their mapping. Adding records or replacing slides should update
the existing definition, not mint unrelated GUIDs each time. A deliberate
fork creates a new object identity. Record builds, revisions, and outputs so
retries do not allocate duplicate objects.

Placement is a separate operation. Let users choose houses and place one
or several instances, or request automated placement with a preview.
Updating an installed definition does not necessarily rewrite state in
instances already saved in houses. Track both, validate each target save,
back it up, and report any unsupported migration or partial failure.
Do not overwrite a running game's saves without a supported workflow.

See the [object-shop plan](https://github.com/SimHacker/WillWrightShowForFood/blob/main/catalogs/soul-city/object-shops.md),
[GUID registry design](https://github.com/SimHacker/WillWrightShowForFood/blob/main/catalogs/soul-city/guid-registry.md),
and [Sims resource tooling](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io).
These are references to designs and available tooling, not evidence that
the complete media-to-object workflow is operational.

## 7. Planning checks

- Resolve a bounded route through branches, merges, and cycles; reproduce a
  pinned edition after the graph changes.
- Preserve unknown metadata and source IDs through edits; disclose losses
  at native-format boundaries.
- Build from authored media with no source game as well as imported albums.
- Rebuild a jukebox with another recording while retaining its GUID; test
  intentional forks and multi-GUID templates separately.
- Place multiple instances and account for each save update; preserve the
  original on validation failure and make retries safe.
- Check source licenses, attribution, privacy, and output rights before
  publishing. Capture alone does not grant redistribution permission.

## Related specifications and implementation references

| Layer | Home |
|---|---|
| Album schema, card model, capture and narration, per-game album bridging | [`soul-angel/SOUL-ALBUM.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/SOUL-ALBUM.yml) |
| The recording an album cites moments in | [`soul-angel/DVR.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/DVR.yml) |
| Albums as authoring tools rather than archives | [`family-album-as-storymaker.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/family-album-as-storymaker.md) |
| Imagined-forward album pages, marked as dreams | [`the-imagine-loop.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-imagine-loop.md) |
| Objects and albums as in-game artifacts | [`the-computer-as-portal.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-computer-as-portal.md) |
| Shops, pipeline, GUID registry, rights — the marketplace these are traded in | [Soul City catalog](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) |

A per-game album adapter uses the game's own feature names. The Sims has a
Family Album. Each adapter must document supported versions, tested
read/write behavior, and information its target format cannot preserve.

## See also

- [README.md](README.md) — the front door, and why the tools live on this side of the bridge
- [SOUL-BRIDGES.md](SOUL-BRIDGES.md) — who crosses, and what the destination owes them
- [PORTABLE-NPCS.md](PORTABLE-NPCS.md) — advertisements, treaties, customs
- [GLOSSARY.md](GLOSSARY.md) — souvenir, Dublin Core, customs, and the rest
