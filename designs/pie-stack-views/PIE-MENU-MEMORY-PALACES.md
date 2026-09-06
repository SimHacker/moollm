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

Navigation honors the same contract as selection. Stroke within a room in a link's direction and the view glides along that link — but the glide is not a cutscene. The user can grab the background at any moment, **brake**, pan, or throw it with momentum, taking over from the animation without a mode switch — the Mario cannon made aimable and interruptible. Automatic transit when unattended, manual the instant it is touched. (Mario supplies the *cannon* — aim and power as a navigation primitive, which is
[direction-selects and distance-quantifies](RADIAL-DIMENSIONS.md) again, so `launch(direction, power)` needs no new input model. It does not supply the interruptibility; SM64 commits you to the arc. That part is Don's.)

Which gives the sharp form of the objection to canned transitions: **an animation that ignores input during its run is a mode.** It has a duration in which the user's normal vocabulary does not work, which is the definition, and the fact that it is short and pretty does not exempt it. The alternative is not a faster animation but a different ontology — the glide is not a scripted interpolation but **a physics state you are allowed to push on**, so incoming input adds to velocity rather than being queued or dropped. That is the same [literalism-versus-magic line](GROOVES-AND-SPIKES.md#cartoon-physics-and-arks-honest-lesson) ARK drew: physics is grabbable, scripts are not.

**The precondition, which is easy to miss.** You can only brake mid-flight if the place you stop in is a legitimate place. Interruptible transit therefore requires the space *between* nodes to be real — continuously navigable, renderable, and addressable — which is why it worked in MediaGraph's spatial graph and cannot be retrofitted onto navigation between discrete pages. A system whose only valid states are its nodes has no choice but to make transitions modal. This is the same requirement as semantic zoom needing intermediate scales to be meaningful, arriving in the navigation layer.

### The graph is a liminal space

Don's name for it, and it is better than the framing above, which was merely defensive — *the
in-between must be valid enough to stop in*. Liminality (van Gennep's *limen*, threshold; Turner's
betwixt-and-between) says the opposite and stronger thing: **in a rite of passage the threshold phase
is not the cost of reaching the far side, it is the part that does the work.** Transit is not overhead
to be tolerated. It is where the change happens.

Which licenses the strong reading of Don's phrase. Not *the edges are liminal and the nodes are
structural*, but liminal throughout — and then **a node is just a point where someone stopped often
enough to name it.** Nodes are bookmarks, not an ontological category; the graph's structure is a
record of where attention has settled, exactly as a desire path is a record of where feet went. The
[eBike Safari](../webtop/EBIKE-PATH-GRAMMAR.md) case is this literally, since lingering is what
promotes a GPS coordinate into a place.

It also explains why canned transitions feel not merely slow but *insulting*. **A cutscene abolishes
the liminal phase** — it takes the threshold, makes it opaque, and performs the transformation on you
offscreen. You are carried through the one stretch you might have learned something in. Turner's later
distinction sharpens it into a directive: **liminal** passage is obligatory and scheduled by someone
else, **liminoid** passage is voluntary and playful. Interruptible navigation is liminoid. Make the
threshold liminoid, never liminal.

And one non-obvious payoff for the multi-user layer. Turner's other claim about liminal phases is
**communitas**: status distinctions are suspended, so strangers in the threshold meet as equals. Nodes
in this system have owners, types and permissions; the space between them does not. So **cursors that
meet in transit meet outside the structure** — pilgrims on the road rather than congregants in the
church — which is a real property to design for rather than a metaphor to admire, and the natural home
for the unstructured encounter a [playable corpus](../webtop/PLAYABLE-CORPUS.md) needs.

The engineering requirement survives the reframe unchanged, and is now better motivated:
**liminal space must be addressable.** Without coordinates in the between, you cannot stop there,
cannot link to it, and cannot come back — and an unaddressable threshold collapses into a cutscene no
matter how it is animated.

#### The address is a blend, plus a DC offset

Don's representation, offered with a wink and correct anyway:

```
addr = lerp(src, dst, t) + offset
```

Not absolute coordinates — an **interpolation between two named nodes, plus a bias off the line.**
The wink is that this is not an analogy to view interpolation, it is
[the same operation already written down](VIEWS-AS-TESTIMONY.md) for views: *stop partway, stake the
intermediate state, label it, and later interpolate against it.* A saved view is a blend of named
views; a liminal address is a blend of named nodes. **One primitive, used in two layers.**

Four properties fall out, and the first is the reason to prefer it:

- **It is semantic, so it survives relayout.** Absolute coordinates rot the moment the graph is
  rearranged — they come to denote empty space, or the wrong thing. *Sixty percent of the way from A
  to B* still denotes the same **relation** after every node has moved, which is the anchor-stability
  argument from the [transclusion](../webtop/nelson/HN-XANADU-2026.md) thread arriving in the
  navigation layer.
- **"DC" is the right word, and it buys graceful degradation.** The lerp is the structured, meaningful
  component; the offset is constant bias carrying no structural information. So a client that does not
  understand offsets can drop them and still place you *on* the A→B path — nearly right rather than
  nowhere. `t` is required, `offset` is optional, which is
  [Postel](../../skills/postel/GLANCE.yml) applied to coordinates.
- **It formalizes "a node is just a bookmark."** A node is `t = 0` with zero offset. Nodes and
  in-between positions become the same type with no special case, which is exactly what the liminal
  claim demanded but could not previously cash. And promotion composes: stake a liminal address, name
  it, and subsequent addresses blend against *it*.
- **`t` outside `[0,1]` is meaningful**, which is convenient rather than a defect — overshoot past the
  destination is precisely the state the [ballistic cannon](#kinetic-navigation-the-aimable-interruptible-cannon)
  produces, and it needs no separate representation.

The honest cost is that **the same point has many addresses.** Near a junction, three edges give three
legitimate blends. They are not interchangeable: `lerp(A,B,0.5)` and `lerp(C,D,0.2)` may denote one
pixel while saying different things about what you were *doing*, so the address records route and
intent, not merely location — provenance in the coordinate, which is a feature. But it means addresses
cannot be compared for identity by comparing tuples. Two different questions need two different
operations: canonicalize to ask *same place*, do not canonicalize to ask *same journey*.

*Discipline, since this is a strong borrowing: keep it only where it predicts something. It predicts
that transit deserves state and an address, that transitions must be optional rather than scheduled,
and that encounters in the between are status-free. Three commitments that can be checked. Anything
past that is decoration.*

That closes the loop on Shneiderman's clauses simultaneously: the command structure is continuously represented as a place; navigating and editing are physical actions on the same representation; and even the automatic motion is reversible, because the user can seize it mid-flight. Reversibility extended to interrupting the system's own animations is the strongest form of the reselection argument — the commit is **soft**, so [reselection](RESELECTION.md) continues into the ballistic phase instead of ending at release.

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
