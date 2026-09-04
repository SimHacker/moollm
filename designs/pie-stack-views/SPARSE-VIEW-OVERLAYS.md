# Sparse View Overlays

*Don Hopkins · August 2026*

**Thesis:** One data model — a sparse tree of view-configuration overrides laid over an underlying graph — explains outliner state, search emphasis, leaf inspection, robust layout under wild scale changes, and the folding geometry of composed views. Most systems special-case each of these; the overlay makes them one rule.

Part of the **pie-stack-views** design cluster ([README](README.md)). Critique origin: [DYE-A-TRIBE](../DYE-A-TRIBE.md).

---

## The mechanism

Opening a pie menu — or an outline, or a map — unfolds a **sparse view overlay**: a tree of view-configuration nodes laid over the underlying structure. The overlay is a tree even when what it opens is a graph: it records *paths* into the graph, so it can loop back, and it can hold multiple simultaneous views of the same node.

Because the underlying structure is a graph, "open" is not a boolean. A node with several outgoing links does not carry an open/close button; it carries a selector — *close, or open any of […]* — and the overlay records which continuations are unfolded, each into its own child view. The same node can be opened along several links at once, into views of different kinds or several views of the same kind. Single-threaded sequences, branching narratives, loops, and deliberately disconnected fragments are all just patterns of which continuations a view chose to unfold.

Nor must the selector's options be immediate children: an overlay node can open a **path**, not just a name. GitHub ships a folk version — directory listings collapse chains of subdirectories that contain nothing but another subdirectory, showing `src/main/java/com` as a single link that drills straight to the first interesting child. The intermediate nodes still exist, uncontested, in the data; skipping them is a view-level judgment, recorded in the overlay like any other. The general form is **slot promotion**: pulling deep slots up as top-level interface slots. OpenLaszlo class definitions did this deliberately, declaring fields on the top-level object that were proxies for internal state — hiding the internals as structure while exposing chosen internal properties directly at the surface. It is Korz-adjacent ([Views as Testimony](VIEWS-AS-TESTIMONY.md)) but a distinct move: subjective dispatch varies what an object *answers* depending on who is asking; path promotion varies which of its coordinates are even on the surface. Both deny the same dogma — that an object has one canonical face.

Each overlay node inherits its view parameters from its parent and modifies them under constraint — *my scale is 80% of my parent's* — and any node can override anything it inherits.

## One rule, many features

That one rule covers cases that are usually special-cased:

- **Leaf inspection.** Pulling a single leaf of a deep, tiny subtree out to full size is an override.
- **Search emphasis.** A search tool growing the interesting nodes proportionally while everything else shrinks is a set of overrides.
- **Outliner memory.** An outliner remembering exactly which grandchildren were open when you close and reopen a grandparent is no mechanism at all: the open state only ever lived in the overlay, and closing the grandparent merely hid that region of it.

## Robust layout

Layout must therefore assume any child can become very large or very small at any moment, and stay readable at any juxtaposition of scales — tight but airy, never awkward. Expect the unexpected; robust first, in Ackley's sense.

The guardrails belong to the parameter system itself, as an escalating spectrum: min/max limits, ratios, and cut-offs where declarative data suffices; full JavaScript expressions where it does not; and natural language compiled to JavaScript by an LLM in the loop — the adventure-compiler pattern — so a designer can write *keep the labels readable, but never let a child outgrow its parent* and get back an enforceable constraint. The spectrum resolves the tension between designer-editable declarative data and real expressive power: you pay for expressiveness only at the nodes that need it, and the natural-language tier keeps even the top of the ladder designer-accessible rather than programmer-private.

## Projection is a parameter

The layout itself is one of the dialable parameters. A node's children can be arranged radially — a pie — or linearly — an outliner — and the arrangement is a continuous dial, not a binary switch: a pie can relax into an indented list as it fills, an outline can gather into a circle as it shrinks, and the animated transition between them is an interpolation of the same overlay, not a rebuild. (The discrete cousin of this move is the pivot into Dasher space: [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md).)

Nor must all children share one projection. Different kinds of children can open in different directions or facets: structural children down the page as an outline, cross-references off to the right, history behind, commentary in the margin — each relation a facet with its own layout dial. The direction a child opens in is itself information, a signifier of what kind of relationship it is, and like everything else here it is recorded in the overlay: saveable, diffable, queryable.

## The folding geometry

When several overlays are layered, they acquire a geometry of their own: views that share nodes overlap like the cells of a simplicial complex, domains glued along shared faces, and the seams between domains are where the folding lives. Opening, closing, hiding — and the harder states, missing and newly present — are creases along those boundaries, and a robust-first layout folds along them intelligently: a subtree in any of those states is a fold to transition through smoothly, not an error to recover from.

## Navigating the complex

The geometry is navigable in its own right. Shared faces are doorways: an object that appears in two views is a place where you can pivot from one perspective into the other, and the complex around any item enumerates the nearby configurations worth interpolating into — compatible neighbors, or deliberately diverse ones. Views themselves take the full CRUD vocabulary, created, edited, and deleted like any other data.

The payoff is serendipity with a mechanism behind it: discovering a new way of looking at something — or discovering that this item you cared about was already an object of interest from a perspective you never knew existed.

## Where this goes

What views *mean* socially — testimony, argument, curated tours — is the subject of [Views as Testimony](VIEWS-AS-TESTIMONY.md). The semantic parameters (how a node describes itself at each scale) and the radial application (pumping up a pie menu's center) are in [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md). The same parameter set keyed to *time* is [Temporal Semantic Zoom](TEMPORAL-SEMANTIC-ZOOM.md).

---

## Related

- [DYE-A-TRIBE](../DYE-A-TRIBE.md) — the critique this cluster grew out of
- [Views as Testimony](VIEWS-AS-TESTIMONY.md) — the social layer above this model
- [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md) — the radial application
- [Temporal Semantic Zoom](TEMPORAL-SEMANTIC-ZOOM.md) — the same parameters, keyed to time
- [Pie Menu Memory Palaces](PIE-MENU-MEMORY-PALACES.md) — palaces as saved overlays
