# The Webtop

**One entry point.** A classic WIMP publishing shell — tabs, windows, pie menus, rooms, semantic
zoom — over corpora that already exist, with an LLM filling in the levels nobody wrote.

`https://github.com/SimHacker/moollm/tree/main/designs/webtop`

This is the hub. Everything below either lives here or is linked from here.

---

## Two ideas

### The semantic pyramid

Gwern, on where Xanadu's interface went wrong:

> transclusion ... should have been 'vertical' with popups, and 'zooming in' and 'zooming out' at
> different levels of abstraction (**link-icon → title → abstract → section** etc.)

That ladder is the whole system. Ours goes one rung further down than his: past the link icon to a
**single emoji or SVG glyph**, small enough to be a pie menu slice, a graph node, or a symbol on a
map. And one rung further up: a room, a show, a city.

The reason nobody built this before is that the author had to write every rung. Gwern's own
footnote, the one that started this:

> I think one of the reasons outliner approaches have not caught on for hypertext in general is that
> while useful, they wind up foisting too much work on the author... However, **LLMs open up many
> new design opportunities for automatically summarizing/expanding to build a full hierarchy while
> the human author writes just what is necessary**, which I think can resurrect many old 'tools for
> thought' ideas and finally make them usable.

You write the rung you care about. The machine generates the rest, on demand, in context.

**It has been built once already.** A HyperTIES article was required to have a **title, a synonym
list, a description, and a body** — the ladder as a mandatory schema, in 1988, with an addressing
layer in front of it. The rung the web dropped is the description; the rung nobody has rebuilt at
all is synonyms, which is what let you link by writing the phrase instead of pasting a URL.
See [`hyperties/ARTICLE-SCHEMA.md`](hyperties/ARTICLE-SCHEMA.md) — it is the node contract this
whole design inherits.

### The card

Every strand of this work independently converged on the same object: a small typed record with a
title, a description, links, arbitrary properties, and optional attached media, which can evolve
over time and be rendered at any size.

| Where | What it's called |
|---|---|
| HyperTIES, 1988 | an article with a hand-written **definition** shown before you follow the link |
| StoryMaker, 2009 | *"A scene is the universal card of StoryMaker — the atom of a story"* |
| Urban Safari, 2011 | geolocated scene cards, navigated adventure-style while riding |
| eBike Safari | cards played at a place, linking both ways — in time and in meaning |
| ShowMaker | show objects as graph nodes; *"a show is a graph walk over StoryMaker content"* |
| MOOLLM | `CARD.yml` — the room interface, and the guest skills card |
| Borretti's wish | *"record templates... having typed fields... links to other records, or lists of links"* |
| The webtop | a **view record** — someone's saved traversal, addressable and citable |

It is one object. The pyramid is what you get when you can render that object at every scale, and
the shell is what you get when you can arrange, route, and share them.

---

## Who this is for

Not most people. Gwern's Zettelkasten test — *are you writing a book? do you publish a dozen papers
a year?* — is the correct filter, and both he and Don are on the far side of it, by decades of
demonstrated willingness to pay the cost by hand.

Design for the long-tail writer with a corpus that has to outlive their memory. If the LLM widens
the audience, good; that is a consequence, not the goal.

Full argument: [`hyperties/README.md`](hyperties/README.md#who-this-is-for-and-why-that-is-not-a-hedge)

---

## Read the objections first

[**`OBJECTIONS.md`**](OBJECTIONS.md) — Borretti's "Unbundling Tools for Thought", which gwern
endorses, and which argues that everything here is an advanced form of procrastination. Including
the engine-versus-game joke, which is aimed squarely at us. What we concede, and what we answer.

---

## The parts

| Directory | What it holds |
|---|---|
| [`gwern/`](gwern/) | The publishing engine: popups-as-windows, annotation, archives. Plus [`NENEX.md`](gwern/NENEX.md) — his edit-log neural wiki proposal, the engine that needs our shell |
| [`hyperties/`](hyperties/) | Shneiderman's lab, and the parts that already worked together in 1988: mandatory definition previews, embedded menus, click-background-reveals-all, pie-menu routing, scriptable applets. Includes the [distilled HN archive](hyperties/HN-ARCHIVE.md) and [who did what](hyperties/TEAM.md) |
| [`nelson/`](nelson/) | Visible connection: why a link should be a bridge and not *"a diving board into the darkness"*. Transclusion as infrastructure, self-revealing interfaces, intertwingularity |
| [`winer/`](winer/) | Outline as syntax for code *and* data; the object DB that is the outline; view state in the document. Plus [`HN-POSTS.md`](winer/HN-POSTS.md) — 71 of Don's HN comments, deduped |
| [`temkin/`](temkin/) | Declare and Mesa: constraints that stay true, and a zoomable canvas shared with an agent |
| [`pie-stack-views/VIEW-STATE-ANCESTORS.md`](../pie-stack-views/VIEW-STATE-ANCESTORS.md) | What you focused on, expanded, and zoomed into is authored content — shareable, citable, answerable |
| [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) | How the corpus becomes navigable without a model in the loop: LLM proposes the warm things at build time, the build **crystallizes** a static index, and you **melt** it back up to restructure. Four shipped receipts — MDL Zork interning aliases to one object, HyperTIES compiling storyboards to FORTH, CAM-6's Forth-to-lookup-tables, Scott Adams' interpreter-plus-database — plus the ground-up version, where the seeds are GPS-located spoken impressions |
| [`SUMMARY-GENRES.md`](SUMMARY-GENRES.md) | The pyramid's second axis: same rung, different register. The terms of art (topos, snowclone, shibboleth, facet, focalization), and why a sardonic bingo card is a contact sheet of textual glyphs with an objective scoring function — hit rate near one half |
| [`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md) | What this brings to gwern's world: **playability, explorability, inventory, multi-userness, reading cursors** — all of it under gwern's own stated principle, *"give the reader agency."* An article does not get a room, it *is* one — a directory exporting the document interface and the ROOM interface at once, with behavioral objects and characters in it, hosted in GitHub repos. Includes the inventory-is-transclusion finding (`TAKE REF` weighs nothing, `TAKE OBJECT` is heavy) and the static-versus-social tier split |
| [`AUTO-FAQ.md`](AUTO-FAQ.md) | Residents answer in context and the answers **persist as artifacts** others retrieve without re-deriving — the tagsonomy compiler applied to dialogue. The key move: an answered question records what got activated to produce it, which **is a K-line** (Minsky, AI Memo 516), so the artifact is a re-activatable path and the text is one rendering of it. An answer record is also a Drescher schema — activation as context, question as action, answer as result — with reinforce/spawn/prune following for free. Named for PKD's *Autofac*, and the pun is the warning: a factory that cannot be switched off fills the repo with answers nobody asked for |
| [`TREE-NAVIGATION.md`](TREE-NAVIGATION.md) | **Tab order flattens a tree into a line, and that is the original error** — then in/out navigation gets bolted on per widget with no grammar, so users can only learn exceptions. Defines the structural command set first (siblings, depth, extremes, history, expand/collapse) and makes `TAB` a *derived projection* of the tree walk. The invariant: every structural operation reachable by keyboard, pie menu, **and** drag, all invoking the same named command — which is a lint, not a taste. Receipts from ThinkTank (keyboard-driven) and MORE (1986, drag-and-drop *without spoiling the keyboard interface*). Type-ahead turns out to be the link-resolution protocol with a different entry point |
| [`DISPENSERS-AND-SOUVENIRS.md`](DISPENSERS-AND-SOUVENIRS.md) | Every document is a **dispenser** — vending machine, brochure stand, single-item crank — and what you carry out is a stamped **souvenir** with a backlink, so an inventory becomes an itinerary. Souvenirs are tickets, and a ticket is a UI to a service, which text adventures shipped in 1977 as the mail-in matchbook. Parameterized dispensers take *your photo* and turn the crank via the ECG construction, then the whole thing deploys onto real ride tracks: Pokémon without the brand name, and a souvenir turns out to be a semantic seed with a face on it |
| [`READING-CURSORS.md`](READING-CURSORS.md) | **A reading cursor is a character**, because `CHARACTER.yml` already owns `location:` and a location in a corpus of rooms is a position in a document. Cursor / read head / character are the same object — a position in a substrate, with state, that moves — so a reading position gains identity, inventory, a path, a rung, and an owner. The receipt: gwern.net's `demo-mode` already keeps a durable per-reader model in LocalStorage and spends it on whether to animate a toolbar; dark mode persists and your place in the argument does not. The generalization: **the bookmark is to reading position what the clipboard is to selection** — invisible, dead, no identity, no history — Nelson's complaint one layer over. Seek time is the reader's re-entry cost, so semantic zoom and reading cursors attack the same context cost from opposite sides of the screen. A versioned corpus lets a stale cursor report what moved under it, which no bookmark can |
| [`EBIKE-PATH-GRAMMAR.md`](EBIKE-PATH-GRAMMAR.md) | The same cursor with a **city** as its substrate, which makes the path legible as **gesture**: a roundabout is a mark and riding it backwards is an **undo**; pausing is the primary gesture, and duration plus surroundings plus the photo library at that timestamp is nearly enough to infer intent. **Velocity is the register dial** — address-by-address detail is wasted at speed and earned when you stop. Receipts: Selker's dwell-time next-item prediction, reimplemented as pie-menu slice lingering. Pauses are the natural cleavage points, so segmentation is free and DWIM moves fall out; **every self-crossing is an event**. Resumption is start/continue/branch — git on wheels. Privacy is an editing pass with three gates, not one |
| [`OBJECTIONS.md`](OBJECTIONS.md) | The strongest case against all of it |

Sibling pack, kept at its original URL because it has been shared publicly:
[`../webtop-gwern-inheritance/`](../webtop-gwern-inheritance/) — the founding study, including
[GWERN-WHAT-TO-INHERIT.md](../webtop-gwern-inheritance/GWERN-WHAT-TO-INHERIT.md),
[MOOLLM-WEBTOP-VISION.md](../webtop-gwern-inheritance/MOOLLM-WEBTOP-VISION.md),
[K-PYRAMID-ATTENTION-MAPS.md](../webtop-gwern-inheritance/K-PYRAMID-ATTENTION-MAPS.md),
[MEMORY-PALACE-PIE-MENUS.md](../webtop-gwern-inheritance/MEMORY-PALACE-PIE-MENUS.md),
[REVERSE-OVER-ENGINEERING.md](../webtop-gwern-inheritance/REVERSE-OVER-ENGINEERING.md).

---

## The lineages

Each of these solved part of it, in production, and none of them ever met each other.

| Whose | What it contributed | Where it lands |
|---|---|---|
| **Engelbart** | Viewspecs — view configuration as a first-class control you can set and hand to someone; outlines embedded in maps | The view record |
| **Bush** | Associative trails: *"he builds a trail of his interest through the maze of materials"* — the trail is the contribution | Views as citations |
| **Nelson** | Transclusion, links both ways — quoting by reference so the quote stays connected | Transclusion instead of copying |
| **Shneiderman / HyperTIES** | Definition previews, embedded menus, background-click reveals all targets, easy authoring | [`hyperties/`](hyperties/) |
| **Winer** | Outline as code-and-data syntax; object DB as outline; `expansionState` in the document head | [`winer/`](winer/) |
| **Gwern / Said Achmiz** | Popups that are real windows; annotation and local archives; the semantic zoom ladder; Nenex | [`gwern/`](gwern/) |
| **Temkin** | Declarative constraints that re-satisfy; a zoomable spatial canvas shared with an agent | [`temkin/`](temkin/) |
| **NeWS / HyperLook** | The window as a scriptable object; flip any stack into edit mode; pie menus everywhere | The shell itself |

---

## The app lineage: one substrate, many tenants

**StoryMaker → Bar Karma → Urban Safari → eBike Safari → ShowMaker.** Same card, same graph, each
tenant adding a layer rather than a fork.

Until now **no single document narrated all five in order** — the chain existed in three overlapping
partial documents. This section is the missing spine; the per-project detail stays where it lives.

The pre-history runs back into Don's own NeWS work: **HyperLook → DreamScape → MediaGraph → iLoci →
StoryMaker**. And the participation model escalates by artifact — **stories → episodes → worlds**:
Bar Karma viewers submitted scenes, Urban Safari explorers submitted places, Repo Show guests submit
code, docs, simulations, and room descriptions.

**StoryMaker's nine layers**, from the 2011 SFC architecture slides — the schema every later tenant
inherits: Reality → Places → Assets → Scenes → Links → Storylines → Ratings → Comments → Metadata.
Ratings and comments attach to *everything*, which is why the view record is not a new idea here so
much as the missing tenth layer.

**Five navigation views over one graph** — Map, Road, Pie, Album, Branching Story
([`family-album-as-storymaker.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/family-album-as-storymaker.md)).
That is the webtop's multi-view thesis, already specified for this data, years before it had a shell
to run in.

- **StoryMaker** — the card-based story filesystem. The scene card is the atom; it starts as written
  description, gets shot, and takes get uploaded into the card.
  [`storymaker-stories-and-scenes.yml`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/storymaker-stories-and-scenes.yml)
- **Bar Karma** — StoryMaker as a broadcast writers' room, on air.
- **Urban Safari** — the cards get GPS. Geolocated scene cards navigated adventure-style while
  riding; performed live with StoryMaker.
  [`LEGACY-URBAN-SAFARI.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/LEGACY-URBAN-SAFARI.md)
  — preserved in amber, deliberately not extended.
- **eBike Safari** — rebuilt from scratch on OSM. Cards link both ways, in time and in meaning; the
  bike is the controller; many games share one map and one data plane.
  [`apps/ebike-safari/design/`](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/ebike-safari/design)
- **ShowMaker** — *"specializes StoryMaker — same substrate, show layer added"*; a show is a graph
  walk over StoryMaker content.
  [`showmaker-network.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/showmaker-network.md)

The webtop is the shell all five of them wanted and none of them had: a way to open a card at any
size, route it into a window, zoom the graph, and hand someone your path through it.

Canonical sources, in reading order for anyone extending this:
[FRAMING-PITCH-AND-LINEAGE.md](https://github.com/SimHacker/DonHopkins/blob/main/projects/willwrightshowforfood/strategy/reviews/chatgpt-research-review/framing/FRAMING-PITCH-AND-LINEAGE.md)
for the participation escalation ·
[StoryMaker `architectural-overview.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/storymaker/architectural-overview.md)
for the canonical data model ·
[`amsterdam-gps-lineage.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/sources/amsterdam-gps-lineage.md)
for the 2026 continuation ·
[`shneiderman-2011-correspondence.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/storymaker/shneiderman-2011-correspondence.md)
for primary-source proof of the stack at peak deployment.

---

## Reading order

1. [`OBJECTIONS.md`](OBJECTIONS.md) — why this might all be a waste of time
2. This file — the two ideas
3. [`pie-stack-views/VIEW-STATE-ANCESTORS.md`](../pie-stack-views/VIEW-STATE-ANCESTORS.md) — the new mechanism
4. [`hyperties/`](hyperties/) — the parts that already worked together
5. [`gwern/NENEX.md`](gwern/NENEX.md) — the engine half
6. [`winer/`](winer/) and [`temkin/`](temkin/) — structure and constraints
7. [`../webtop-gwern-inheritance/`](../webtop-gwern-inheritance/) — the founding study in full

---

## Status

Design, not implementation. No code in this directory. The parts are being specified so they can be
built as one system rather than assembled from seven half-systems that never met — which is the
entire complaint that produced it.

Named for **Ground Up Software**, which is what you call a company when the prescription is
"rewrite it from the ground up" and you have been doing that since before the prescription.

↑ [designs](../README.md)
