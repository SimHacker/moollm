# P-line attention maps: the webtop view as first-class shareable content

The webtop's defining user-created content type: a **P-line** — a saved attention map over
the entire site, named for the K-line that stores a P-pyramid's mask
([P-PYRAMID](../P-PYRAMID.md): save view = mint K-line; speak the name = reopen the
pyramid). Users don't just read the corpus; they construct **curated views** of it —
desktop layouts of opened, zoomed, nested objects plus their own comment trees — and those
views are objects: saved, copied, made permanent, shared, diffed, and traded.

## The rendering: two zooms, one weight

Every node in view carries an attention weight 0..1. The weight drives **both zooms at
once**:

- **Geometric** — PSIBER Space Deck point size. Partial attention renders *smaller*. A
  whole wing of the site you're only peripherally aware of sits legibly in the corner at
  6pt.
- **Semantic** — pyramid mip level. The same weight selects how much summary you get:
  README at 1.0, SKILL at 0.8, CARD at 0.5, GLANCE at 0.2 — and below GLANCE, two new
  levels this design adds (see UI summary pyramid below).

### The narrowed hallway

Drilling deep is not a teleport and not a full-size Russian-nesting descent. The **path**
to a deep node is rendered as a narrowed hallway: each uninteresting intermediate level
shrinks — small font, thin, compressed, but *present and clickable* — and when you arrive
at the node of interest it blooms back to full size. Attention is spent at the destination,
not the route; but the route stays visible as breadcrumb geometry you can walk back up.
This is the fisheye/DOI move (Furnas) done with the pyramid: the hallway isn't elided
(Quora's sin, below), it's *diminished*.

## Layout + comments = the content type

A P-line is:

1. **The mask** — which objects are open, at what weight, in what spatial arrangement
   (windows, tabs, stacks, rooms visited). The
   [moocroworld attention-tree](../../skills/moocroworld/ATTENTION-TREE.md) YAML
   serialization plus `agent:` and per-node `attention:` is already the file format.
2. **The commentary** — trees of comments attached to any node, contributed by the author
   and by other users, and *themselves* open/close/zoomable objects with the same weight
   semantics. A comment thread is part of the pyramid, not a second-class sidebar.

So a P-line is a **curated tour + marginalia**, stored as data, versioned in git like
everything else. A tutorial is a guided sequence of P-lines. A code review is two people
diffing their P-lines over the same graph. A conversation is *trading edits to one*.

## The Quora indictment (named anti-pattern: EPHEMERAL PYRAMID)

Reading Alan Kay's Quora answers is the counter-example that motivates all of this.
Quora's UI has three or four *different* mechanisms by which trees and comments abbreviate
themselves — collapsed answers, "more" folds, hidden reply chains, truncated comments —
each with its own expansion gesture, none coordinated. Reconstructing the full thread is
laborious manual pyramid-building. And the result is **ephemeral and fragile**: one stray
click navigates away and the entire painstakingly-opened attention state is destroyed,
unrecoverable, because the platform owns the view state and doesn't consider it worth
keeping.

The rule this violates, stated positively: **the reader's attention state is theirs, it is
valuable work, and it must be a first-class object.** Gwern's popups commit a milder form
of the same sin — pinned windows die on page navigation (see
[analysis](sources/analysis-notes/FRONTEND-POPUPS-WM.md), anti-inherit #1). The webtop
must not: every view is continuously serialized; "save" is just naming what already
persists; navigation is never destructive because the pyramid *is* the navigation.

## Correspondence webtops

Because a P-line is a permanent copyable object, two people can discuss a topic by
**trading edits to the same webtop configuration**: you send me your view with the
economics section blown up and annotated; I return it with your section shrunk to a
hallway, a counter-example room opened at full weight, and comments threaded on your
comments. Correspondence chess played on attention itself. The git mechanics are already
there — a P-line diff is a diff, a shared curated view is a PR, a fork of someone's tour
is a fork.

This is also the Repo Show participation mechanic: an episode ships with the host's
P-line over the repo; viewers extend it, re-weight it, and send it back.

## The UI summary pyramid: two levels below GLANCE

The standard MOOLLM pyramid (README → SKILL → CARD → GLANCE) bottoms out at ~5 lines.
Zoomable UI needs shorter:

| Level | Size | Used for |
|-------|------|----------|
| GLANCE | 5-70 lines | smallest readable document |
| **LABEL** | 1-4 words | tab title, window title when shaded, tree node, breadcrumb |
| **GLYPH** | 1 word / icon | iconified window, pie menu slice, minimap dot |

When a window iconifies to a tab, it must still show a *sensible short word* — not a
truncated URL. These levels are generated, cached in frontmatter/K-line files like any
other pyramid level, and regenerated when content changes.

### The menu item summarizer (set-contrastive labeling)

The key insight for LABEL/GLYPH generation: items must be summarized **together, as a
set**, not independently. Eight pie menu slices each summarized in isolation might all
come out as "Settings"; summarized jointly, the LLM is instructed to make them mutually
unambiguous, parallel in grammar, and aligned in register — the way a good menu designer
labels by *contrast within the set*. Same for a tab strip and for sibling rooms on a map.

This is a perfect LLM micro-task in the Gwern guardrail style
([LLM-IN-THE-LOOP](sources/analysis-notes/LLM-IN-THE-LOOP.md)): small context, judgment
call, mechanically checkable (word count, uniqueness within set), cache the results,
`""` on doubt falls back to the existing title. A `menu-summarizer` sister script:
input the set of items with their GLANCEs, output the aligned label set.

LLMs summarizing UI text strings is the general enabler for the whole design: zoomable,
incrementally self-revealing interfaces need text at *every* scale, and no human authors
seven sizes of every label. The pyramid gets compiled, like mip levels of a texture.

## Minsky checkpoints (theory → feature)

| P-PYRAMID principle | Webtop feature |
|---------------------|----------------|
| K-line stores the mask | Save/name a view; P-line file in user state |
| Level-band restoration | Reopening a shared P-line restores the middle band — structure, not stale leaf content; leaves re-render from current corpus |
| Fringes attach weakly | Shared views merge softly with your own open state instead of clobbering it |
| Cross-exclusion groups | Tab stacks; restoring a P-line forces one member per group |
| Dispositions | Workspace presets = pre-activated subsets ("reading mode", "review mode") |
| Conflict → zoom out | Two comments fighting at one level is a cue to open the parent |
| K-recursion | New P-lines composed from existing named P-lines — tours citing tours |

## Implementation notes (minimum viable)

1. Serialize continuously: window/tab/zoom/collapse state → attention-tree YAML in
   localStorage; export = write the file; share = commit it.
2. Weight → render: CSS `font-size`/`transform: scale()` for geometric; pyramid-level
   fetch for semantic. One slider per node (or per subtree), pie menu on every titlebar.
3. Comments as nodes: same open/close/weight machinery; threads live in the repo
   (issues/discussions or files) so they survive and belong to the conversation.
4. LABEL/GLYPH generation: menu-summarizer sister script, cached, set-contrastive.
5. Load a shared P-line: apply level-band policy — restore structure and weights, refetch
   content, merge weakly with current state.

↑ [design pack README](README.md) · theory: [P-PYRAMID](../P-PYRAMID.md) ·
UI rendering: [MicropolisCore p-pyramid-attention-overlay](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/p-pyramid-attention-overlay.md)
