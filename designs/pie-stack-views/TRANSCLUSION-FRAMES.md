# Transclusion Frames

*Don Hopkins · September 2026*

**Thesis:** A page is not a document, it is a **transclusion frame** — a parameterized sparse
overlay that pulls nodes out of the graph and arranges them. *View source* and *source view* are
antipodal items in one pie, and they are the read and write directions of the same relation.

Part of the **pie-stack-views** design cluster ([README](README.md)). The data model is
[Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md); the publication layer this bridges to is
[Two-Layer View Source](../webtop-gwern-inheritance/TWO-LAYER-VIEW-SOURCE.md).

---

## The pie has opposite items, and that is the argument

A pie menu puts meaning in **direction**, and the strongest thing direction buys is that antipodes
are free. The stroke and its reverse are the same motor act run backwards, so putting inverse
operations at 180° means the *gesture* carries the inversion and not just the label. Edges and
corners in the directions they live is the operational case ([The Window Resize
Pie](WINDOW-RESIZE-PIE.md)); this is the navigational one.

- **North — view source.** *View* is the verb, *source* is the noun. Take me to what produced this.
- **South — source view.** *View* is the noun, *source* is the verb. Make this view a source: name
  it, commit it, cite it, hand it to someone who can argue with it.

The pair is read and write. Reversing the stroke reverses the direction of provenance, which is
about as literal as a mnemonic gets.

### It answers the contribution-set problem

[Two-Layer View Source](../webtop-gwern-inheritance/TWO-LAYER-VIEW-SOURCE.md) left this undecided:
a compiled page has a *contribution set* rather than a source, and showing a reader five files and
asking them to pick one is a UI problem that can end up worse than a single wrong edit link.

A pie is the right shape for a small set. The sources fan radially off the view-source pole, each in
a direction that says what *kind* of source it is — prose here, `CARD.yml` there, the character file
somewhere else, another repo behind. Reselection means the reader browses the set before committing
to any of it, so the choice costs nothing until it is made. A fan of five is legible; a list of five
demands a decision before you know what you are deciding between.

Sources the frame may not name — the private-repo half of its own provenance — are slices that exist
and are closed. A visibly locked door is honest in a way that a silently shortened menu is not.

## A page is a frame

Nelson's transclusion: content lives in one place and appears in many by reference. Take that
seriously at the publication layer and the consequences are not cosmetic.

**The site is a mapping from URLs to canonical views.** A URL names a view, the view is data, and
data is saveable, diffable and forkable — so canonicity is an entry in the mapping rather than a
property of the material, and one URL having a canonical view does not make it the only view. That
is what makes *source view* a real operation rather than a metaphor: you are not exporting a
rendering, you are committing an overlay and proposing a change to the mapping.

**Cross-repo transclusion becomes the normal case, not an edge case.** So the frame needs a
**clearance** parameter alongside its layout parameters: which halves of its own provenance it is
permitted to name. This is the same field [QUOTES.md](../QUOTES.md) needs for attributed playback,
and it should be one mechanism rather than two.

## What the frame is parameterized by

The overlay already carries scale, projection, and summary scale. Written out as an inventory, the
parameters group into four kinds:

| Kind | Parameters |
|---|---|
| **Windowing** | which nodes open, into which windows, placed where |
| **Relation** | how they connect and relate — and the direction a child opens in is itself the claim about what kind of relation it is |
| **Layout** | the projection dial, radial through linear, continuous rather than switched |
| **Attention** | where the focus sits, and what is therefore peripheral — the saveable, shareable object of [K-Pyramid Attention Maps](../webtop-gwern-inheritance/K-PYRAMID-ATTENTION-MAPS.md) |
| **Representation** | the semantic token pyramid, below |

## Semantic level of detail and point size are two axes

The summary ladder in [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md) steps a node's
self-description down from a paragraph to a sentence to a tab label to a few emoji to one emoji.
That is level of detail **in meaning**. Visual point size is a **separate** axis, and conflating
them is the standard mistake: shrink the box and systems truncate the text, as though small meant
less to say.

The useful cells are off the diagonal. A single glyph at slice size carrying a long essay behind it.
A full-bleed illustration with a one-word caption. Six-point type holding a complete argument
because the argument is what is scarce and the pixels are not. Both axes belong in the overlay,
dialable independently, recorded when set.

The representation rungs, with the thing that actually distinguishes them:

| Rung | Recognition test | Machine-generatable |
|---|---|---|
| Single emoji | tells apart at pie-slice size | natively — it *is* a token |
| Glyph / icon | distinct from its neighbors on the same street | natively, as SVG |
| SVG diagram | structure survives the shrink | natively — SVG is source code |
| Thumbnail | photographic gist | separate image model |
| Full raster render | the real thing | separate model, expensive |

**Emoji and SVG are in a language model's native output modality; raster is not.** So the rungs it
can fill on demand are exactly the ones made of text — which turns SVG-first iconography from an
aesthetic preference into a structural argument. The representation ladder gets generated in the
same pass as the summary ladder, from the same node, with the same provenance, and lands in git as a
**reviewable diff**. A raster thumbnail is an opaque blob in version control; an SVG icon is a
change someone can object to specifically. The eval that follows from this is
[the glyph benchmark](../webtop/GLYPH-BENCHMARK.md).

## Where this goes

Unsettled: whether the antipodal discipline scales past one pair. Two poles carrying inverses is
clean; eight items where four oppositions all have to hold simultaneously is a constraint problem,
and it is not obvious the good pies are the ones that satisfy it. Also unsettled: whether readers
ever want *source view* unprompted, or whether it only makes sense once they already have a view
worth defending.

---

## Related

- [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — the data model this is an application of
- [Views as Testimony](VIEWS-AS-TESTIMONY.md) — why committing a view is an argument
- [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md) — the summary ladder, and semantic zooming
- [The Window Resize Pie](WINDOW-RESIZE-PIE.md) — direction-as-meaning in the operational case
- [The Tower](THE-TOWER.md) — the crown as glyph rung, the skyline as contact sheet
- [Two-Layer View Source](../webtop-gwern-inheritance/TWO-LAYER-VIEW-SOURCE.md) — the publication layer
- [The glyph benchmark](../webtop/GLYPH-BENCHMARK.md) — the eval the SVG rung implies
