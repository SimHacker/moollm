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

## Start here — four routes in

The hub is large on purpose and nobody should read it in file order. Pick the route that matches why
you arrived.

### If you are Gwern

Your own footnote is the thesis of this hub, so the interesting question is whether the rest holds
up. **What is here that you do not already have** is narrow and worth naming, so you can leave early
if it is not enough:

- **Primary sources on HyperTIES nobody has published** — the 1988 article schema, the build
  scripts, who wrote which implementation, and the parts that worked *together* rather than as a
  list of features. Don was on the team.
- **A shipped system with your architecture and one difference.** HyperLook was a statically
  publishable corpus with a dynamically composed chrome layer — and the chrome could be flipped into
  edit mode *while running*, by the reader, using the same tool that built it. SimCity shipped on it
  in 1992 as a sealed runtime. Plus Alan Kay's verdict on why the browser should have been HyperCard.
- **A build-time answer to the author-burden problem** you raised, with four shipped precedents
  rather than a proposal.
- **Two concrete disagreements**, not compliments: the pyramid needs a rung *below* the link icon,
  and your site already keeps durable per-reader state and spends it on toolbar animation.

Everything else is context you can skip.

1. [`OBJECTIONS.md`](OBJECTIONS.md) — Borretti's "Unbundling Tools for Thought", which you endorsed,
   turned on this work. What it concedes before it answers.
2. [`hyperties/ARTICLE-SCHEMA.md`](hyperties/ARTICLE-SCHEMA.md) — **the ladder shipped as a mandatory
   schema in 1988**: title, synonyms, description, body, with a build script proving the definition
   was a separate compilation unit. The receipt for "link-icon → title → abstract → section."
3. [`HYPERLOOK.md`](HYPERLOOK.md) — **your architecture, shipped in 1992, editable from inside**:
   HyperCard's model rebuilt on NeWS by Arthur van Hoff, productized with Don, with SimCity running
   in a sealed runtime while the authoring environment stayed fully live. The stripped runtime *is*
   the crystallize/melt split; property sheets were themselves stacks; a plugin was a document you
   opened. Includes Alan Kay on Apple blowing it "by not making the design framework the basis of a
   web browser," and the honest tension you have chosen the other side of.
4. [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) — how a corpus stays navigable **with no
   model in the loop at read time**. The LLM runs at build; the artifact is static. Written knowing
   what your site is and is not willing to become.
5. [`GLYPH-BENCHMARK.md`](GLYPH-BENCHMARK.md) — the bottom rung as a proposed eval, and an argument
   that the pelican has no referent while a thousand documents do.
6. [`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md) — *"give the reader agency"* taken literally: an
   article does not get a room, it **is** one.
7. [`READING-CURSORS.md`](READING-CURSORS.md) — the uncomfortable receipt: gwern.net already keeps a
   durable per-reader model in LocalStorage and spends it on whether to animate a toolbar. Dark mode
   persists; your place in the argument does not.
8. [`gwern/NENEX.md`](gwern/NENEX.md) — your edit-log neural wiki, read as the engine that this shell
   was specified around.

### If you are Said Achmiz

Everything above is written to the author of the corpus. This route is written to the person whose
code we read. **What is here that you do not already have**, so you can leave early if it is not
enough:

- **Two disagreements with the current design**, not compliments — one of them expensive.
- **Unpublished HyperTIES primary sources**: the mandatory 1988 article schema, the build scripts, the
  MockLisp authoring tool, and who wrote which implementation on which platform. Don was on the team.
- **A navigation invariant stated as a lint**, which your accesskeys and the gwern.net chord table are
  among the few shipped systems that would pass.

The credit line this pack carries, and why: *inspired by the publishing and hypertext system developed
by Gwern Branwen and Said Achmiz at gwern.net* — following gwern's own "tech co-creator" rather than
"frontend by," and deliberately not guessing which of you thought of what.

1. [`../webtop-gwern-inheritance/GWERN-WHAT-TO-INHERIT.md`](../webtop-gwern-inheritance/GWERN-WHAT-TO-INHERIT.md)
   — **the pin test.** Pinning sets a flag on the same window object; no rewrap, no reparent. That is
   the TNT OPEN LOOK pin-up menu architecture, arrived at independently decades earlier, and the
   opposite of the olwm/ICCCM rewrap dance X11 forced on a separate-process window manager with no
   shared class hierarchy. Convergent design, or the only sane choice in a DOM?
2. **The two disagreements.** Pinned popups die on page navigation — if pinning is promotion,
   promotion should outlive the document, on a persistent serialized desk
   ([`READING-CURSORS.md`](READING-CURSORS.md)). And desktop popups versus mobile popovers are two
   windowing engines where one adaptive window class would do. If you tried either and rejected it,
   **why** is the artifact we want.
3. [`TREE-NAVIGATION.md`](TREE-NAVIGATION.md) — the lint: every structural operation reachable by
   keyboard, pie menu, **and** drag, all three dispatching one named command. Not three code paths
   that happen to agree. Most likely document here to contain an error you can spot on sight.
4. [`hyperties/ARTICLE-SCHEMA.md`](hyperties/ARTICLE-SCHEMA.md) — embedded menus and link previews in
   1988, with a build step that pre-resolved them and a schema that made every article self-naming.
   The ancestor of the popup, with receipts.
5. [`hyperties/FOCUS-FLOW.md`](hyperties/FOCUS-FLOW.md) — HyperTIES could reveal every link at once;
   this fuses that with animated chevrons between tab stops to render the whole focus graph. Honest
   cost: it exposes bad tab order mercilessly. We think that is a lint worth having.
6. [`OBJECTIONS.md`](OBJECTIONS.md) — the strongest case against all of it, written down so you can
   attack the design instead of first reconstructing our awareness of its weaknesses.

Skippable for you: the corpus-as-place material, unless it interests you on its own.

### If you are David Temkin

Start by auditing what we say about you — there are known gaps flagged in the doc, and one claim was
already corrected once.

1. [`temkin/README.md`](temkin/README.md) — Declare, Mesa, DOMIsland, SimFaux, and
   [what we know we are missing](temkin/README.md#open-and-known-gaps-in-our-own-record).
2. **The two ideas** below — the pyramid and the card. Mesa is
   [the pyramid rendered as space](temkin/README.md#mesa-is-the-semantic-pyramid-rendered-as-space);
   the card is what Declare would call a record type.
3. [`../pie-stack-views/VIEW-STATE-ANCESTORS.md`](../pie-stack-views/VIEW-STATE-ANCESTORS.md) — view
   state as authored content. The Declare question underneath it: if the view is a constraint
   satisfaction over the document, saving the view saves the constraints.
4. [`TREE-NAVIGATION.md`](TREE-NAVIGATION.md) — the closest thing here to a Declare invariant: every
   structural operation reachable by keyboard, pie menu, **and** drag, all dispatching one named
   command. Stated as a lint rather than a taste, because that is the only version that survives.
5. [`AUTO-FAQ.md`](AUTO-FAQ.md) — the agent half of Mesa's shared canvas, generalized: residents
   answer in context and the answers persist as retrievable artifacts.
6. [`CURSOR-STORAGE.md`](CURSOR-STORAGE.md) — the systems layer, git as substrate. **Read the first
   half**; past the Postgres bridge it becomes deep infrastructure that nothing else depends on.
7. [`OBJECTIONS.md`](OBJECTIONS.md) — the strongest case that all of it is procrastination.

### If you have twenty minutes

[`OBJECTIONS.md`](OBJECTIONS.md), the two ideas below, then
[`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md). That is the argument, the case against it, and the
payoff.

---

## How the ideas relate

Twelve pieces, and the dependency order is the actual argument — each one exists because the one
above it is unusable without it.

```
        THE CARD  ──────── a typed node: title, synonyms, description, body, media
            │              (hyperties/ARTICLE-SCHEMA.md — shipped 1988)
            ▼
      THE PYRAMID  ─────── render that node at every scale: glyph → title → abstract → section → room
            │              (SUMMARY-GENRES.md · GLYPH-BENCHMARK.md)
            ▼
   TAGSONOMY COMPILER  ─── the LLM writes the missing rungs at BUILD time, so reading needs no model
            │              (../TAGSONOMY-COMPILER.md)
            ▼
    TREE NAVIGATION  ───── one command set for the resulting structure; TAB is a derived projection
            │              (TREE-NAVIGATION.md · ../pie-stack-views/)
            ▼
    PLAYABLE CORPUS  ───── a navigable node set with agency is a room; the article IS the room
            │              (PLAYABLE-CORPUS.md)
            ├──────────────► DISPENSERS      taking something out of a room; inventory = itinerary
            ├──────────────► AUTO-FAQ        characters in the room make it answerable
            ▼
    READING CURSORS  ───── a room needs a reader who persists: position + identity + inventory + path
            │              (READING-CURSORS.md)
            ├──────────────► EBIKE PATH      same cursor, city as substrate; the path becomes gesture
            ▼
    CURSOR STORAGE  ────── where that reader lives: orphan branch per cursor, git as the object store
            │              (CURSOR-STORAGE.md)
            ▼
    GITMAPPING / MOOFS  ── at scale: mount objects by name, index them, page in on read
                           (../MOOFS-NAMESPACE.md)

    OBJECTIONS  ────────── runs alongside all of it and is meant to win where it can
```

Read across instead of down and the same pieces group into four claims:

| Claim | Pieces | Rests on |
|---|---|---|
| **A node can be shown at any size** | card, pyramid, summary genres, glyph benchmark | authors already wrote descriptions in 1988; LLMs write the rungs nobody wrote |
| **A corpus can be navigable without an AI in the loop** | tagsonomy compiler, tree navigation, view state | compile the warm structure at build time; keep it static and inspectable |
| **A reader can have agency in it** | playable corpus, dispensers, auto-FAQ, reading cursors | a position in a substrate with state, history, and inventory is a character |
| **It can persist and be shared without a server** | cursor storage, gitmapping, GitHub as slow server | git is the object store, GitHub is the social layer |

The two seams where this could fail are marked in the docs rather than hidden: **the compiler's
synonym collisions** fail silently by resolving to a plausible wrong node, and **a reading cursor is
a worse privacy surface than inventory** because it records where you got bored rather than what you
liked.

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
| [`kay/`](kay/) | **He already reviewed this lineage, and the criticism is worth more than the praise.** Seven OLPC threads from 2007 extracted in [`kay/OLPC-2007.md`](kay/OLPC-2007.md), where three of this hub's theses turn out to pre-exist it: *"close to natural language but clearly not natural language"* as the criterion for a readable substrate, with HyperTalk's failure being that it looked **too** like English — a trap whose failure mode inverts once a model is reading the files; **science as map-making not bible-making, "with annotations for errors and kinds of measurements"**, which is the signed assessment with its evidence dimension; and **gray boxes that pop open**, where opacity is graduated and *"what is the center and what is the side will shift as the learning progresses"* — semantic zoom applied to mechanism. Plus the warning aimed at us: environments *"form tribal bonds that are rather religious in nature."* The browser should have been "not an 'app' but an Operating System" safely running encapsulated real objects; settling for a simple text format sent web media "in entirely the wrong direction," and circa the early 90s the whole thing "had the look and feel of an **atavistic hack**." **Symmetry** is his word for the property this hub keeps groping for — the reader can "turn around and 'author' in the same high-level terms." Then the two criticisms of Don's own work: that his group "missed the significance for personal computing of the design of Hypertalk," and that SimCity hid its simulation in a black box players cannot change — the first proved by **PdB**, the second answered by Micropolis. Plus **views as "watchers" that do not affect what they view**, the unsolved **automatic inverter** problem for dimensions a view discards, and the brief: *a second pass at the end-user programming problem has never been done* |
| [`nelson/`](nelson/) | Visible connection: why a link should be a bridge and not *"a diving board into the darkness"*. Transclusion as infrastructure, self-revealing interfaces, intertwingularity |
| [`winer/`](winer/) | Outline as syntax for code *and* data; the object DB that is the outline; view state in the document. Plus [`HN-POSTS.md`](winer/HN-POSTS.md) — 71 of Don's HN comments, deduped |
| [`temkin/`](temkin/) | Declare and Mesa: constraints that stay true, and a zoomable canvas shared with an agent |
| [`pie-stack-views/VIEW-STATE-ANCESTORS.md`](../pie-stack-views/VIEW-STATE-ANCESTORS.md) | What you focused on, expanded, and zoomed into is authored content — shareable, citable, answerable |
| [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) | How the corpus becomes navigable without a model in the loop: LLM proposes the warm things at build time, the build **crystallizes** a static index, and you **melt** it back up to restructure. Four shipped receipts — MDL Zork interning aliases to one object, HyperTIES compiling storyboards to FORTH, CAM-6's Forth-to-lookup-tables, Scott Adams' interpreter-plus-database — plus the ground-up version, where the seeds are GPS-located spoken impressions |
| [`GLYPH-BENCHMARK.md`](GLYPH-BENCHMARK.md) | The pyramid's bottom rung, proposed as an LLM eval better than the pelican on a bicycle. The pelican earns its place — cheap, memorable, hard to game — but it has **no referent**, so scoring is vibes. A thousand real documents do have one: the glyph is right if a reader who knows the document recognizes it and a reader who does not can pick it out of a contact sheet. Objective scoring function, and the whole semantic pyramid comes along so humans can judge from the top |
| [`SUMMARY-GENRES.md`](SUMMARY-GENRES.md) | The pyramid's second axis: same rung, different register. The terms of art (topos, snowclone, shibboleth, facet, focalization), and why a sardonic bingo card is a contact sheet of textual glyphs with an objective scoring function — hit rate near one half |
| [`HYPERLOOK.md`](HYPERLOOK.md) | **The shipped ancestor of this entire hub.** HyperCard's model rebuilt on NeWS as GoodNeWS by **Arthur van Hoff** at the Turing Institute in 1989, renamed HyperNeWS, productized as HyperLook with Don in 1992 — and you could **flip a running SimCity into edit mode**, open the transportation-fund slider's property sheet, and read the script that sent `SetTransportationFund` to the stack. Five things it had that this cluster keeps re-deriving: a **stripped non-editable runtime** for shipping products, which is crystallize/melt billed for in 1992; **property sheets that were themselves stacks**, so one tool went all the way down; delegation **Object → Card → Background → Stack → network client**, addressed by path of names; **warehouses**, where a plugin was a document you opened and its pages became your *New Object* menu; and PostScript as programming, graphics and data at once. Plus **PdB**, van Hoff's C-to-PostScript compiler — the dual path again. Carries Alan Kay's verdict that HyperCard "deserved to be successful" and that **Apple blew it by not making the design framework the basis of a web browser** |
| [`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md) | What this brings to gwern's world: **playability, explorability, inventory, multi-userness, reading cursors** — all of it under gwern's own stated principle, *"give the reader agency."* An article does not get a room, it *is* one — a directory exporting the document interface and the ROOM interface at once, with behavioral objects and characters in it, hosted in GitHub repos. Includes the inventory-is-transclusion finding (`TAKE REF` weighs nothing, `TAKE OBJECT` is heavy) and the static-versus-social tier split |
| [`AUTO-FAQ.md`](AUTO-FAQ.md) | Residents answer in context and the answers **persist as artifacts** others retrieve without re-deriving — the tagsonomy compiler applied to dialogue. The key move: an answered question records what got activated to produce it, which **is a K-line** (Minsky, AI Memo 516), so the artifact is a re-activatable path and the text is one rendering of it. An answer record is also a Drescher schema — activation as context, question as action, answer as result — with reinforce/spawn/prune following for free. Named for PKD's *Autofac*, and the pun is the warning: a factory that cannot be switched off fills the repo with answers nobody asked for |
| [`TREE-NAVIGATION.md`](TREE-NAVIGATION.md) | **Tab order flattens a tree into a line, and that is the original error** — then in/out navigation gets bolted on per widget with no grammar, so users can only learn exceptions. Defines the structural command set first (siblings, depth, extremes, history, expand/collapse) and makes `TAB` a *derived projection* of the tree walk. The invariant: every structural operation reachable by keyboard, pie menu, **and** drag, all invoking the same named command — which is a lint, not a taste. Receipts from ThinkTank (keyboard-driven) and MORE (1986, drag-and-drop *without spoiling the keyboard interface*). Type-ahead turns out to be the link-resolution protocol with a different entry point |
| [`DISPENSERS-AND-SOUVENIRS.md`](DISPENSERS-AND-SOUVENIRS.md) | Every document is a **dispenser** — vending machine, brochure stand, single-item crank — and what you carry out is a stamped **souvenir** with a backlink, so an inventory becomes an itinerary. Souvenirs are tickets, and a ticket is a UI to a service, which text adventures shipped in 1977 as the mail-in matchbook. Parameterized dispensers take *your photo* and turn the crank via the ECG construction, then the whole thing deploys onto real ride tracks: Pokémon without the brand name, and a souvenir turns out to be a semantic seed with a face on it |
| [`READING-CURSORS.md`](READING-CURSORS.md) | **A reading cursor is a character**, because `CHARACTER.yml` already owns `location:` and a location in a corpus of rooms is a position in a document. Cursor / read head / character are the same object — a position in a substrate, with state, that moves — so a reading position gains identity, inventory, a path, a rung, and an owner. The receipt: gwern.net's `demo-mode` already keeps a durable per-reader model in LocalStorage and spends it on whether to animate a toolbar; dark mode persists and your place in the argument does not. The generalization: **the bookmark is to reading position what the clipboard is to selection** — invisible, dead, no identity, no history — Nelson's complaint one layer over. Seek time is the reader's re-entry cost, so semantic zoom and reading cursors attack the same context cost from opposite sides of the screen. A versioned corpus lets a stale cursor report what moved under it, which no bookmark can |
| [`CURSOR-STORAGE.md`](CURSOR-STORAGE.md) | Where the rubber meets the road: a cursor is an **orphan branch**, `git switch --orphan` — a tangent universe with no parent commit, a typed addressable object with its own filesystem, where the name carries class and id (`cursor_<id>`, `character_<id>`). Already in production: Leela's alerting system stores each alert's evidence in an `Issue_<id>` branch. Three things git gives away — **the commit history is the path**, and therefore the return stack, better than Emacs's because it records what changed while you were there; **`git worktree` is the body plan**, so the worm with head in doc A and butt in doc B is two checkouts; and **forking is handing someone your character**. Custom ref namespaces (`refs/cursors/*`, Gerrit-style) are cleaner but GitHub cannot render them, and GitHub *is* the social layer, so branches win. Publishing must be a squash, because history is the part people forget to curate |
| [`EBIKE-PATH-GRAMMAR.md`](EBIKE-PATH-GRAMMAR.md) | The same cursor with a **city** as its substrate, which makes the path legible as **gesture**: a roundabout is a mark and riding it backwards is an **undo**; pausing is the primary gesture, and duration plus surroundings plus the photo library at that timestamp is nearly enough to infer intent. **Velocity is the register dial** — address-by-address detail is wasted at speed and earned when you stop. Receipts: Selker's dwell-time next-item prediction, reimplemented as pie-menu slice lingering. Pauses are the natural cleavage points, so segmentation is free and DWIM moves fall out; **every self-crossing is an event**. Resumption is start/continue/branch — git on wheels. Privacy is an editing pass with three gates, not one |
| [`SIGNED-ASSESSMENTS.md`](SIGNED-ASSESSMENTS.md) | Rating as a compiled tagsonomy. The unit is an **assessment record — author, target, dimension, value, date, evidence** — signed, owned, and free to conflict, never universal metadata on a node. Dimensions are parent tags, rungs are their closed value sets, and [the tagsonomy compiler](../TAGSONOMY-COMPILER.md) crystallizes them into a static index, so it renders with no backend. Slashdot's typed moderation and Leary's Mind Mirror are the ancestors; bridging aggregation replaces counting; reader-turnable knobs are one rendering rather than the thesis |
| [`CONTRIBUTION-BOT.md`](CONTRIBUTION-BOT.md) | **The commit is the conversational turn** — pushing to a branch is the utterance, not the storage under it. A bot makes the branch, writes the commits, opens the PR and runs the checks, so a reader with no GitHub account participates in the normal PR workflow without seeing it. Git's thirty-year-old **author/committer split** is the primitive: the bot holds the credential, the contributor holds the claim — but an author string is a *claim, not an identity*, which for a project that portrays real people is the primary abuse case, so identity is two-tier and a claimed name colliding with anyone in the corpus is rejected at submission. Commits are cheap and constant; the **PR is the reviewable bundle**, opened at a boundary and generated with its checks already run, because forty one-typo PRs turn a gift into a chore. *Obvious case* is a predicate, not a vibe: merging someone's own signed opinion into their own namespace is not a judgment about whether they are right, and everything touching shared content is human. The bot's own auto-decisions are signed assessments in its own namespace, so its false-accept rate is measurable and a rejection is contestable |
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
| **Atkinson / HyperCard** | Stacks, cards, direct-manipulation editing, and a scripting language millions of end users actually wrote | The ancestor of all of it |
| **van Hoff / HyperLook** | HyperCard rebuilt on NeWS: every object scriptable, flip a *running* program into edit mode, property sheets that are themselves stacks, plugins that are documents, and a sealed runtime for shipping | [`HYPERLOOK.md`](HYPERLOOK.md) |
| **Kay** | The browser should have been an OS running real objects; **symmetry** between reading and writing; views as watchers; gray boxes that pop open; and a criticism of the NeWS work that stands | [`kay/`](kay/) |
| **NeWS** | The window as a scriptable object; PostScript as code, graphics and data; pie menus everywhere | The shell itself |

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

## Status

Design, not implementation. No code in this directory. The parts are being specified so they can be
built as one system rather than assembled from seven half-systems that never met — which is the
entire complaint that produced it.

Named for **Ground Up Software**, which is what you call a company when the prescription is
"rewrite it from the ground up" and you have been doing that since before the prescription.

↑ [designs](../README.md)
