# K-pyramid attention maps: saved attention as first-class shareable content

The webtop's defining user-created content type: **saved attention over the site**, using
Minsky's vocabulary from AI Memo 516 correctly, with a Nelsonian metadata layer
piggybacked on top for annotation, curation, visualization, retrieval, and intertwingling.

## Minsky's terms, used right

From [K-Lines: A Theory of Memory](../P-PYRAMID.md) (AIM-516, 1979; OCR cached at
[skills/k-lines/sources/](../../skills/k-lines/sources/aim-516-k-lines-1979-ocr.txt)):

| Term | What it is | Webtop mapping |
|------|-----------|----------------|
| **P-agent** | An activatable agent in the P-net — the things | A site node: room, doc, window, comment, simulation |
| **P-pyramid** | The hierarchical *view from P* over the (non-hierarchical) graph | The user's live rendered view, right now — transient |
| **K-node** | A new agent minted by the act of memorizing | A saved view: one named snapshot object |
| **K-line** | The K-node's wire, attached excitatorily "to every currently active P-agent" | The snapshot's payload: the weighted attachment set — which nodes, how much |
| **K-pyramid** | "The K-nodes grow into a structure whose connections mirror those of the P-pyramid, except that information flows the other way… Thus forms a K-pyramid, lying closely against the P-pyramid" | The user's accumulated, composed corpus of saved views — **the thing we save and share** |

So: P's are nodes (activatable things); K's are the triggers, wires, nerves that
re-activate them. The live view is a P-pyramid. Pressing "save" mints a **K-node whose
K-line records the current weighted activation**. And because of the recursion principle —
new K-lines attach *to currently-active K-nodes*, not to raw P-agents ("new memories are
composed mainly of ingredients from earlier memories") — a user's saved views compose into
a **K-pyramid**: their personal memory structure lying against the site, information
flowing down where perception flows up. That K-pyramid is the shareable artifact.
Activating any node of it re-arouses the P-agents, band-limited (see below), and the
webtop re-renders the P-pyramid it remembers.

## The `weight` parameter: one scalar, two-way mapping

Every node in the attention tree carries a single canonical **`weight: 0.0-1.0`**. All
view properties are *derived* from it, and direct manipulation writes *back* to it —
a two-way mapping, so the weight is the model and everything else is projection:

| Derived from weight | Mapping |
|---------------------|---------|
| Font / point size | PSIBER pretty-plotter scaling — partial attention renders smaller |
| Level of detail | Pyramid mip level: README 1.0 · SKILL 0.8 · CARD 0.5 · GLANCE 0.2 · LABEL/GLYPH below |
| Window state | open ↔ shaded ↔ tab ↔ icon thresholds |
| Opacity / lighting | fog-of-war dimming at the fringes |

Direct manipulation runs the other way: stretch a window and its weight rises; shrink a
subtree into a hallway and the weights fall; iconify to a tab and the weight drops to the
LABEL band. The user never edits "weight" as a number unless they want to — they *are*
editing it whenever they zoom, resize, open, or collapse. This is what makes the
serialization honest: the saved K-line is exactly what the user sculpted by hand.

### The narrowed hallway

Drilling deep is neither a teleport nor a full-size nested descent. The **path** to a deep
node renders as a narrowed hallway: uninteresting intermediate levels shrink — small font,
compressed, but present and clickable — and the destination blooms to full size. Weight is
spent at the destination, not the route; the route stays visible as breadcrumb geometry
you can walk back up. Fisheye/DOI done with the pyramid: the hallway is *diminished*,
never elided (Quora's sin, below).

## The Nelsonian piggyback layer

Minsky's core stays pure: nodes, wires, weights. Everything else rides on top as
user-editable metadata — this is deliberately **intertwingled**, in Ted Nelson's sense:
annotation, curation, visualization, and retrieval are not separate systems but layers
over one structure, every piece deeply linked to every other:

- **Annotation** — trees of comments attached to any node, contributed by the author and
  other users, themselves weighted/zoomable nodes (a comment thread is part of the
  pyramid, not a sidebar).
- **Curation** — names, ordering, grouping, dispositions (workspace presets), guided
  sequences (a tutorial is a path through K-nodes).
- **Visualization** — per-node render hints (color, icon, pinned position) that override
  the weight-derived defaults without replacing them.
- **Retrieval** — tags, K-line names as speakable activators, full-text over the
  annotations; speaking the name reopens the pyramid.
- **Intertwingling** — transclusive links between K-pyramids: my saved view can embed a
  subtree of yours by reference, Nelson-style, with visible provenance.

## Layout + comments = the content type

A saved K-node serializes as an attention-tree file (the
[moocroworld attention-tree](../../skills/moocroworld/ATTENTION-TREE.md) YAML plus
`agent:` and per-node `weight:`): which objects are open, at what weight, in what spatial
arrangement, with which comment trees. Versioned in git like everything else. A tutorial
is a guided sequence of K-nodes. A code review is two people diffing their K-pyramids
over the same graph. A conversation is trading edits to one.

## The Quora indictment (named anti-pattern: EPHEMERAL PYRAMID)

Reading Alan Kay's Quora answers is the counter-example that motivates all of this.
Quora's UI has three or four *different* mechanisms by which trees and comments
abbreviate themselves — collapsed answers, "more" folds, hidden reply chains, truncated
comments — each with its own expansion gesture, none coordinated. Reconstructing the full
thread is laborious manual pyramid-building. And the result is **ephemeral and fragile**:
one stray click navigates away and the entire painstakingly-opened attention state is
destroyed, unrecoverable, because the platform owns the view state and doesn't consider
it worth keeping.

The rule this violates, stated positively: **the reader's attention state is theirs, it
is valuable work, and it must be a first-class object.** Gwern's popups commit a milder
form of the same sin — pinned windows die on page navigation (see
[analysis](sources/analysis-notes/FRONTEND-POPUPS-WM.md), anti-inherit #1). The webtop
must not: the view is continuously serialized; "save" is just minting a K-node for what
already persists; navigation is never destructive because the pyramid *is* the navigation.

## Correspondence webtops

Because a K-pyramid is a permanent copyable object, two people discuss a topic by
**trading edits to a shared webtop configuration**: you send me your view with the
economics section blown up and annotated; I return it with that section narrowed to a
hallway, a counter-example room opened at full weight, and comments threaded on your
comments. Correspondence chess played on attention itself. The git mechanics come free —
a K-pyramid diff is a diff, a shared curated view is a PR, a fork of someone's tour is a
fork.

This is also the Repo Show participation mechanic: an episode ships with the host's
K-pyramid over the repo; viewers extend it, re-weight it, and send it back.

## Trains of thought: the Family Album that configures the live site

A sequence of K-nodes is a **train of thought** — and its publishing shape is the Sims
Family Album, upgraded: **each album page, instead of showing a JPEG, configures your
live site browser page.** The Sims album (2000) was a linear chain of captioned
screenshots; millions shared them on the Exchange. The webtop album's "photo" is a K-line
activation — open these rooms, at these weights, with this hallway, these comments in
view. The snapshot is alive: the reader lands *inside* the moment, can turn the page to
ride the train, or step off and wander.

MicropolisCore already designed the graph this rides on —
[family-album-as-storymaker](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/family-album-as-storymaker.md):
scenes as captioned moments with the live data behind them, directed edges (continuation,
aftermath, alternate-reality, dream, crossover), storylines as author-curated paths
through a shared scene pool, and append-only `vote.yml` / `comment.yml` records. Swap
"Sims screenshot + IFF data" for "K-line over the site" and it is the same schema.

What this yields, in ascending granularity of sharing:

- **Blogs, but much more granular** — a post decomposes into scenes; a scene can be as
  small as one window opened on one paragraph with one remark. Publish a moment, not
  only an essay.
- **Multiplayer discussions** — a Hacker News-style comment tree hangs off every scene,
  and the comments are themselves weighted, open/close/zoomable nodes (no EPHEMERAL
  PYRAMID: the thread state is yours and persists).
- **StoryMaker scenes with votes** — user comment trees and votes on each scene, exactly
  the [storymaker](https://github.com/SimHacker/MicropolisCore/tree/main/documentation/designs/storymaker)
  / Bar Karma writers-room mechanic: propose scenes, thread reactions, vote storylines
  toward canon.

And this is the **Urban Safari recreation**:
[Urban Safari](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/urban-safari/overview.md)
was field geo-capture on the StoryMaker stack — walk the city, capture scenes where you
stand, thread them into shared stories. The webtop safari walks the **site's map instead
of the city's**: rooms for GPS fixes, K-lines for photographs, trains of thought for the
safari log, comment trees and votes for the expedition party. Same stack, same social
mechanics ([WWSFF storymaker scenes-and-stories](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/storymaker-stories-and-scenes.md),
[ShowMaker](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/showmaker-network.md) —
a show is a graph walk over StoryMaker content, and a Repo Show episode is a guided
safari), new territory: the corpus.

## The UI summary pyramid: two levels below GLANCE

The standard MOOLLM pyramid (README → SKILL → CARD → GLANCE) bottoms out at ~5 lines.
Zoomable UI needs shorter:

| Level | Size | Used for |
|-------|------|----------|
| GLANCE | 5-70 lines | smallest readable document |
| **LABEL** | 1-4 words | tab title, shaded window title, tree node, breadcrumb |
| **GLYPHS** | emoji sequence, truncatable to 1 | iconified window, pie menu slice, tab badge, minimap dot |

When a window iconifies to a tab it must still show a *sensible short word* — not a
truncated URL. These levels are generated, cached like any other pyramid level, and
regenerated when content changes.

### GLYPHS: big-endian, purposefully truncatable

GLYPHS is not one icon — it is a **big-endian sequence of emojis, abstract to specific**:
the **type glyph first**, then holistic impressions and obviously useful qualifiers, in
strictly decreasing order of importance. The view truncates from the right, keeping the
first character(s), to whatever length fits — truncation is a rendering decision, never
data loss:

```
🚪🏛️🎹📜   room: a hall, music, documents
👤🎩🕹️     character: the guy with the hat and the games
🛠️🧵📌     skill: sewing... pinning... (pin-up menus)
🗺️🏙️🔥     map: city, fire disaster active
```

- Truncate to 1 → the pure type icon (minimap dot, tiny tab).
- Truncate to 2-3 → type + identity (pie slice, tab badge).
- Full sequence → icon caption, hover, tree node decoration.

Same big-endian discipline as yaml-jazz naming: most significant symbol first, so any
prefix is a valid coarser summary. And the same set-contrastive rule applies: the first
glyph must be *consistent* across siblings of the same type (all rooms lead with the same
type glyph), while the following glyphs must *distinguish* within the set.

### The menu item summarizer (set-contrastive labeling)

LABEL/GLYPHS generation must summarize items **together, as a set**, not independently.
Eight pie menu slices summarized in isolation might all come out "Settings"; summarized
jointly, the LLM is instructed to make them mutually unambiguous, parallel in grammar,
aligned in register — the way a good menu designer labels by *contrast within the set*.
Same for tab strips and sibling rooms.

A perfect LLM micro-task in the Gwern guardrail style
([LLM-IN-THE-LOOP](sources/analysis-notes/LLM-IN-THE-LOOP.md)): small context, judgment
call, mechanically checkable (word count, uniqueness within set), cached, `""` on doubt
falls back to the existing title. A `menu-summarizer` sister script: input the set of
items with their GLANCEs, output the aligned label set.

LLMs summarizing UI text is the general enabler: zoomable, incrementally self-revealing
interfaces need text at every scale, and no human authors seven sizes of every label. The
pyramid gets compiled, like mip levels of a texture.

## Minsky checkpoints (theory → feature)

| AIM-516 principle | Webtop feature |
|-------------------|----------------|
| K-line stores the weighted attachment set | Save/name a view; attention-tree file in user state |
| Level-band principle | Reopening a shared view restores the middle band — structure, not stale leaves; leaves re-render from the current corpus (no hallucinating old pages) |
| Fringes attach weakly | Shared views merge softly with your open state instead of clobbering it |
| K-recursion | New saved views attach to existing K-nodes — tours citing tours; this is what makes it a K-pyramid |
| Cross-exclusion groups | Tab stacks; restoring a view forces one member per group |
| Dispositions | Workspace presets = pre-activated subsets ("reading mode", "review mode") |
| Conflict → zoom out | Two comments fighting at one level is a cue to open the parent |

## Implementation notes (minimum viable)

1. Serialize continuously: window/tab/zoom/collapse state → attention-tree YAML with
   per-node `weight:`; export = write the file; share = commit it.
2. Weight → render, render → weight: CSS `font-size`/`transform: scale()` and pyramid-
   level fetch derived from weight; resize/zoom/collapse gestures write weight back.
3. Comments as nodes: same weight machinery; threads live in the repo (issues,
   discussions, or files) so they survive and belong to the conversation.
4. LABEL/GLYPHS generation: `menu-summarizer` sister script, cached, set-contrastive;
   GLYPHS emitted big-endian so views can truncate freely.
5. Load a shared view: level-band policy — restore structure and weights, refetch
   content, merge weakly with current state.

↑ [design pack README](README.md) · theory: [P-PYRAMID](../P-PYRAMID.md) ·
[k-lines skill](../../skills/k-lines/) ·
UI rendering: [MicropolisCore p-pyramid-attention-overlay](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/p-pyramid-attention-overlay.md)
