# Pie Menu Memory Palaces

*Don Hopkins · August 2026*

**Thesis:** The one direct manipulation property a menu lacks — being the object of interest — can be recovered by promoting the menu itself to a place: a memory palace you build, edit, and travel by direct manipulation. This has shipped three times.

Part of the **pie-stack-views** design cluster ([README](README.md)). Critique origin: [DYE-A-TRIBE](../DYE-A-TRIBE.md).

---

## The missing property

A menu is command selection through an intermediary; the object of interest is elsewhere. That is the one clause of Shneiderman's direct manipulation definition a menu does not inherit (the full accounting is in [Reselection](RESELECTION.md)). The recovery is not to abandon menus but to promote the menu structure itself to an object of interest.

## Rooms, links, and kissing

Treat the menu structure as a **memory palace** — an adventure map of rooms linked by direction — and make the map directly manipulable: rooms laid out spatially, links created by kissing rooms together edge to edge, so that building the command structure and arranging it are the same act. The method of loci is the oldest user interface on record; a directional menu graph is its computable form, and editing it should feel like arranging furniture, not writing configuration.

This is a solved problem, shipped repeatedly:

- **DreamScape**, in Kaleida's ScriptX
- **MediaGraph**, built in Unity at Stupid Fun Club
- **iLoci**, on the iPhone — the name is the method of loci, on purpose

## What DreamScape actually was

The room graph was the shell; the substance was the objects in it. DreamScape's basic functionality
was **plug-together animated articulated media objects** — graphics plus audio — that you moved
between your **inventory** and the **room**, snapping them into each other. The canonical example:
a record you could snap into a record player and play, and then drag the needle to scratch to a
different part of the record.

Read that example closely, because it contains three of this cluster's arguments at once. The record
and the player are separate objects with a physical fit, so composition is a gesture rather than a
configuration dialog. The needle is a *directly manipulable playhead*, which is reselection applied
to media time — you browse a position by dragging before committing to it, exactly the contract in
[Reselection](RESELECTION.md) and the timeline version in
[Temporal Semantic Zoom](TEMPORAL-SEMANTIC-ZOOM.md). And scratching is what happens when you let the
user seize an animation mid-flight, which is the aimable, interruptible cannon above, one medium over.

The design lineage is explicit: after seeing Randy Smith's **Alternate Reality Kit** (Xerox PARC,
1986 — physics as interface, every object a concrete thing you grab and rewire while it runs), the
point of ARK landed, and DreamScape combined it with the **adventure / Zork / MUD / LambdaMOO / Sims**
line. ARK supplied *literalism first* — power that follows the world's rules teaches, power that
breaks them must be spent like currency — and the adventure line supplied rooms, inventory, and
objects that afford. A record player is literalism: it behaves like a record player, so nothing has
to be explained. See [randall-smith](../../skills/design-sense/masters/randall-smith.md) for the ARK
reading and the Self connection.

The third DreamScape demo, which never made it into the recorded WWDC session, turned the browser's
own URL and return stack into an editable tree — that one is in
[View State Ancestors](VIEW-STATE-ANCESTORS.md), because it is the direct ancestor of a saved view.

## Kinetic navigation: the aimable, interruptible cannon

Navigation honors the same contract as selection. Stroke within a room in a link's direction and the view glides along that link — but the glide is not a cutscene. The user can grab the background at any moment, pan, or throw it with momentum, taking over from the animation without a mode switch — the Mario cannon made aimable and interruptible. Automatic transit when unattended, manual the instant it is touched.

That closes the loop on Shneiderman's clauses simultaneously: the command structure is continuously represented as a place; navigating and editing are physical actions on the same representation; and even the automatic motion is reversible, because the user can seize it mid-flight. Reversibility extended to interrupting the system's own animations is the strongest form of the reselection argument.

## A pump instead of a glide

The same traversal can be expressed radially: a single stroke out and back within a slice is a natural *be there* gesture — arrive at the item, and a fresh circle of options rises around you. The memory palace and the pumped-up pie menu are one navigation model in two projections — three, counting the reversible pivot into Dasher's continuous-zoom steering. The radial projection and the Dasher pivot are developed in [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md).

## The data model

What a palace remembers — which rooms are open, at what scale, showing which detail — is a sparse view overlay over the underlying graph, and everything about saving, sharing, and composing palaces follows from that model. See [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) and [Views as Testimony](VIEWS-AS-TESTIMONY.md); the geolocated version, where the palace is a real city and the tour is the saved view, is discussed there via StoryMaker and Urban Safari / eBike Safari.

---

## Related

- [DYE-A-TRIBE](../DYE-A-TRIBE.md) — the critique this cluster grew out of
- [Reselection](RESELECTION.md) — the property analysis this article completes
- [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md) — the radial projection
- [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — what the palace remembers
- [Pie menus: CHI '88 and beyond](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/pie-menus-chi-88-and-beyond.md)
