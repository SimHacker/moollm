# Views as Testimony

*Don Hopkins · August 2026*

**Thesis:** A saved view is an opinion about what matters, recorded as data. That makes views queryable, comparable, remixable — and a medium for argument.

Part of the **pie-stack-views** design cluster ([README](README.md)). Critique origin: [DYE-A-TRIBE](../DYE-A-TRIBE.md). The underlying data model is [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md).

---

## A layer above the knowledge graph

Sparse view trees are a layer *above* the knowledge graph, not part of it — saveable, exchangeable, editable, diffable documents in their own right, and since they are themselves data, they can view each other, and themselves. A view tree does not show everything; it shows what one person, one viewpoint, one LLM, or one application thinks is important — a curated path through a structure too large to show.

## Pivoting, blending, remixing

Because the views are data above the graph, the relationship inverts on demand: at any object you can ask *what other views are there on this?* — answered with immediate visual feedback, a constellation of tiny thumbnail graphs — and pivot to one, blend it into the current view, or remix two views into a third with a general-purpose view-graph editor.

## Scale is testimony

How far a view opens a node — its header level, its zoom — tells the reader it mattered enough to spend scarce space on, and because that judgment is recorded as data, it is queryable. *What other views show this object at more than 120% scale?* is a question about who considered it important, asked as a media query over the view layer. Views are not silos; they are perspectives you can stand in, compare, and compose — and interrogate.

## A medium for argument

Two people who disagree about what matters can debate by demonstration — zooming and unzooming, opening and closing, dramatically — then just as dramatically animate between their saved views, watching one emphasis dissolve into the other. The interpolation itself is inspectable: stop partway, stake the intermediate state, label it as a new example or a new position, and come back later to interpolate against *it*. The rhetorical moves that in conversation are only gestures — *look closer*, *step back*, *compare these two* — become recorded, replayable, sharable operations on a shared structure.

The arc completes socially: a view starts as one person's judgment, becomes queryable testimony (*who considered this important?*), and ends dialogic — the disagreement itself representable, animatable, and diffable. The doorway topology of overlapping views ([Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md)) supplies the mechanism for the best case: discovering that the thing you cared about was already an object of interest from a perspective you never knew existed.

## The Korz connection

Much of this is inspired by **Korz** (Ungar and Ossher, Onward! 2014), which made *subjectivity* a language primitive: method dispatch is symmetric across any number of contextual dimensions rather than owned by a single receiver, so what an object does — and how it presents itself — depends on the context asking. A view tree is that idea worn as an interface. Standing in a view adds a dimension to every lookup: the same node answers with a different scale, a different summary, different children unfolded in different directions, depending on the perspective in force. Pivoting between views is changing a dispatch coordinate; blending two views is dispatching in both at once.

The lineage is fitting: Ungar is already in this story through Self and Morphic (the ARK line in [Dye-a-Tribe](../DYE-A-TRIBE.md)), and Korz is where that line arrived at the same conclusion the view layer does — perspective is not decoration on the data; it is a coordinate of it.

## Tours: the geolocated case

The same model describes **StoryMaker** and **Urban Safari / eBike Safari**: a navigable, geolocated story-and-travel graph, where a tour is a saved view tree — one guide's judgment of what matters, laid as a path over a city too large to show — and the rider can leave the path at any moment and pick up another. The knowledge graph is a real city; pivoting between views is switching guides mid-ride; and the viewer-freedom clause is literal, because you are on a bicycle and can steer wherever you want.

The open-as-selector rule ([Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md)) has a concrete reading here: at any location the question is *what scenes are at this location?*, and opening the place means choosing among them. Scenes themselves have multiple incoming and outgoing links to other scenes, so an author can thread them however the story wants — single-threaded, branching, looping, or deliberately disconnected — and a rider (or a second author) can open many views on the same scenes, of different kinds or several of the same kind, without disturbing anyone else's threading.

## Peripheral views: the precedent

The viewer is never captive to the curation: full freedom remains to open, close, rescale, and annotate, attaching side-commentary and tools beside any node. That last move has direct precedent in PSIBER's **peripheral views** ([*The Shape of PSIBER Space*, 1989, §2](https://donhopkins.com/home/catalog/psiber/data.html)): associated views and editors attached *beside* an object rather than contained in it — editor buttons, computed views, related objects — living in the view tree, visually distinct from the data they operate on. The full treatment, including why PostScript's homoiconicity was the enabling condition and what the webtop does not inherit for free, is [Peripheral Views](PERIPHERAL-VIEWS.md).

The separation does the same work the pie menu's figure-ground separation does one level down ([Reselection](RESELECTION.md)): commentary must read as commentary, not as part of the thing commented on.

## Visible clipboards and conveyor belts

A peripheral view need not be *about* its subject at all. Attach one as an embedded WYSIWYG clipboard: a staging area that holds material in plain sight while you work. This is the opposite of the design that enrages Ted Nelson — he coined *cut and paste* for the visible rearrangement of writing, and the desktop GUI took his terms and attached them to a hidden, single-slot buffer with no history, no identity, and no way to see what it holds (*Geeks Bearing Gifts*, 2008; *Computers for Cynics*). A clipboard done as a peripheral view is just another node in the overlay: visible, inspectable, scaled and placed by the same view parameters as everything else, holding as many items as you drop into it, each a live reference into the world graph rather than a dead copy.

### And addressable

The property that finishes the repair of Nelson's complaint: **expose views in the namespace, as children of their owners, by path.** A hidden buffer has no name, so nothing can refer to it; a view with a path can be linked, transcluded, cited, diffed, and handed to someone else. `designs/webtop/README.md/views/pyramid-argument` is a sentence you can put in a document. What the desktop clipboard lacks is not only visibility — it is *addressability*, and the two failures compound: you cannot see it and you could not point at it if you could.

Since views are children in the same namespace as everything else, they inherit the whole resolution protocol for free: scope-walking name resolution, synonyms, and the every-binding-in-scope-order answer to ambiguity ([`webtop/hyperties/LINK-RESOLUTION.md`](../webtop/hyperties/LINK-RESOLUTION.md)). Drilling into a fragment is the same mechanism one level down, so a view can be attached to a *section* rather than a document, and several views of the same target coexist as siblings under it.

### And therefore editable

Visibility and addressability are not two features, they are two thirds of one. **Things on the
system clipboard are dead.** You cannot edit what is on your clipboard, and the reason is not that
editing a buffer is hard — it is that the buffer is invisible, so there is nowhere to put the cursor.
Invisibility is not a missing convenience on top of an otherwise fine design; it is the thing that
forecloses every other operation. No history, no identity, no editing, no inspection, all downstream
of one decision.

Which makes the obligation strict: **if you bother to make the clipboard visible, and bother to allow
many of them arranged in whatever directory structure you like, then everything on them must be
editable.** A visible clipboard whose contents are still frozen would be worse than the hidden one,
because it would display its uselessness. Held to it here, this is cheap — a clipping is a file in a
tree, and files are editable by construction. You get it by not building a special case.

This is precisely what [Alan Kay means by things that hang on because they only kind of
work](../../skills/design-sense/masters/randall-smith.md): the single-slot clipboard works *just*
well enough for the copy-one-thing-paste-it-once case that nobody's daily workflow breaks, so the
pressure to fix it never accumulates, and forty years later it is still one slot. Nelson's fury is
proportionate — he coined the terms for the visible rearrangement of writing, and the survivor is a
hidden buffer that only kind of works.

### GitHub is the clipboard bus

The implementation is embarrassingly small: **add files to a `clipboard/` directory in git.** No big deal, and that is the point — an existing thing pressed into service as the implementation of an idealistic concept, while remaining perfectly good at everything else it does. Git supplies exactly the four things the desktop clipboard threw away: **history** (every cut is a commit), **identity** (every item is a path), **multiplicity** (as many items as you drop in), and **shareability** (push, fork, pull request). Nelson's objection was never that copying needed to be harder; it was that the rearrangement of writing should be visible and accountable. A commit log is an accountable rearrangement.

Items are references, not copies, which is the `TAKE REF` distinction already built in [`skills/inventory/`](../../skills/inventory/) — a pointer weighs nothing, a deep copy is heavy, and `DROP AS BOX` is the deliberate act of letting a reference become a thing with its own identity. So the clipboard holds live references into the world graph by default and dead copies only when you ask.

And the declaration that makes a plain directory *be* a clipboard is a selfish inheritance line rather than a subsystem:

```yaml
# clipboard/CARD.yml
inherits: [../../skills/inventory/CARD.yml]   # it IS an inventory; it just lives here
element_type: clipping
members: files                                 # each file is an item
order: big_endian_date                         # newest last, chronological for free
```

The pretending is load-bearing and openly declared. A directory asserts what it is, delegation supplies the behavior, and nobody had to write a clipboard. This is the same move as an article asserting `ROOM.yml` and thereby being a place ([`PLAYABLE-CORPUS.md`](../webtop/PLAYABLE-CORPUS.md)) — declaration plus delegation instead of implementation.

Push further and the clipboard becomes a conveyor. Factorio's vocabulary is exact: belts, inserter arms, mines, and factories are visible machinery whose contents you watch pass through — you debug the economy by looking at it. A peripheral view can work the same way. Attached beside a node, it shows objects *passing through* the system: the output of a query, the stream of matches from a search, values propagating through constraints. Not necessarily the subject of the view — possibly things derived from the subject, possibly things from anywhere. The view is a window onto flow.

That turns the view layer into a dataflow spreadsheet: formulas, constraints, a dependency graph — but tree structured, because the overlay is a tree of paths over the graph ([Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md)), so every automated cell has a place, a scale, and a parent to inherit view parameters from. The machinery is laid out in the same space as the data it processes, which is where a spreadsheet's power always came from: formulas living in the same grid as their results.

The commands hiding in menus unfold the same way. *Save as PDF* stops being a fire-and-forget verb and becomes a **PDF factory**: a machine placed in the view layer, with configurable generation parameters, templates, and saved configurations that project the viewed object into PDF — and because it is a peripheral view, you watch it work and inspect what comes out. The output need not terminate there: individual pages flow down a belt into a combining factory that assembles them into documents and injects material from other sources along the way — front matter from one node, a generated index from another, live figures from a third. Stephen Wolfram runs his books through exactly this kind of automated build pipeline, continuous integration for a manuscript; the Factorio angle makes the pipeline a *place* — machines you arrange, belts you route, intermediate products you can watch pass by and pull off the line for inspection.

The full loop: discover nodes in the world graph, interpret them with views, and animate them with pluggable automation. The graph is the territory; views are testimony about it; conveyors are testimony that works.

---

## Related

- [DYE-A-TRIBE](../DYE-A-TRIBE.md) — the critique this cluster grew out of
- [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — the data model underneath
- [View State Ancestors](VIEW-STATE-ANCESTORS.md) — the lineage and the `view:` record format
- [Peripheral Views](PERIPHERAL-VIEWS.md) — PSIBER in depth, and homoiconicity
- [The Tower](THE-TOWER.md) — the geolocated case as architecture; cards as contributions to a place
- [Temporal Semantic Zoom](TEMPORAL-SEMANTIC-ZOOM.md) — testimony on a timeline: tags as votes about what mattered
- [Pie Menu Memory Palaces](PIE-MENU-MEMORY-PALACES.md) — palaces and tours as saved views
- [*The Shape of PSIBER Space*, 1989](https://donhopkins.com/home/catalog/psiber/data.html) — peripheral views
- Ungar & Ossher, "Korz: Simple, Symmetric, Subjective, Context-Oriented Programming," Onward! 2014 — subjectivity as a dispatch dimension
- Ted Nelson, *Geeks Bearing Gifts*, 2008 — the hidden-clipboard critique
- [FACTORIO-MOOLLM-DESIGN](../FACTORIO-MOOLLM-DESIGN.md) — visible machinery as a design vocabulary
