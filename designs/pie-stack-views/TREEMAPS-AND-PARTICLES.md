# Treemaps and particles: area selects the rung

**One claim.** Give every node a weight, let a space-filling layout turn weights into area, and let
**available area select which rung of the semantic pyramid gets drawn.** Then a big-endian emoji string
is a progressive encoding that squishes from the right as area shrinks, and at the bottom of the ladder
it stops being text at all and becomes a colored particle — continuously, with no second renderer.

Three existing pieces, joined:

| Piece | Contributes | Where it already lives |
|---|---|---|
| **Treemaps** (Shneiderman, HCIL, 1990–92) | a weight on every node, and a layout that fills the space | new here; see below |
| **Dasher** (Ward, Blackwell, MacKay, UIST 2000) | continuous steering, and area allocated by a model | [the Dasher pivot](PUMPING-UP-PIE-MENUS.md#the-dasher-pivot) |
| **The rung ladder** | what to draw at each size, authored rather than computed | [`../../skills/ties/RUNGS.yml`](../../skills/ties/RUNGS.yml) |

## Treemaps: the weight, and the complaint that motivated them

Shneiderman's own account of why treemaps exist is the `ls` problem, stated in 1991
([HCIL treemap history](http://www.cs.umd.edu/hcil/treemap-history/), TR 91-03):

> Most operating systems display the contents of one node at a time with names of the files and
> subdirectories or icons to represent them. [...] even elegant tree-like layouts of the hierarchical
> structures [...] soon overwhelm the available display space and **users cannot grasp the entire
> picture.**

He was staring at an 80 MB disk shared by fourteen users, wanting to know what was big. The answer was
a recursive alternating horizontal/vertical split — six lines of algorithm, a few days to convince
himself it always worked — and it required exactly one thing of the data:

> Treemaps require that a weight be assigned to each node.

**That weight is `cost:`.** The `inside[]` entries in a TIES.yml already carry one per child, and the
scarce resource has changed from disk blocks to context tokens without changing the question. Same lab,
same directory tree, same complaint, thirty-five years apart.

`what treemaps do not solve:` labels. A standard treemap draws text until the rectangle is too small
and then draws nothing, so the smallest cells — often the most numerous — are semantically blank. That
gap is the whole opportunity here.

## Dasher: area by model, and selection by arrival

Dasher sized its boxes by language-model probability and let you steer into them, growing what you
approached, with mid-course correction available the entire way — *selection by arrival*, no commit
event. Already argued in [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md#the-dasher-pivot), including the
point worth keeping: model-weighted interface geometry is not an LLM-era novelty, and it inherits
Dasher's obligation — **the model proposes the sizes, the user steers.**

What Dasher adds to a treemap is **continuity**. A treemap is a still frame; you click and the world
changes. Dasher never changes discontinuously, so a rung transition can happen *while* a cell grows
rather than as a consequence of arriving somewhere. Combined with the ladder, the two give what neither
has alone: a treemap that is navigable without clicks, whose cells become more articulate as you
approach them.

## The ladder as a progressive encoding

`glyphs` is specified big-endian — *type glyph first, then holistic impression, then qualifiers,
strictly decreasing importance* — with the rule that **truncation is rendering, never data loss**
([RUNGS.yml](../../skills/ties/RUNGS.yml)). Under an area-driven renderer that rule stops being a
convention and becomes the mechanism:

| Area available | Rung drawn | Example |
|---|---|---|
| a page | `body` | the file itself |
| a card | `description` | the CARD |
| a few lines | `definition` | "should I go there" |
| a line | `name` | `design-sense` |
| a few characters | `label` | `Design Sense` |
| a small square | `glyphs` entire | 🛠️👁️🎛️ |
| a smaller square | `glyphs` truncated from the right | 🛠️👁️ then 🛠️ |
| a few pixels | **the particle** | a colored dot |

Because the string is big-endian, every truncation removes the least important thing available, so
**every prefix is a valid coarser view.** The ladder is not a set of alternative renderings to choose
between; it is one encoding read to varying depth, which is why authoring it once serves every zoom
level.

This is the same shape as Engelbart's viewspecs and the **shrink factor** in the PSIBER Space Deck,
already recorded in [Peripheral Views](PERIPHERAL-VIEWS.md): point size plus a per-subtree shrink, with
inheritance and override — *my scale is 80% of my parent's*.

**Area selects the rung, it does not determine it.** [Transclusion
Frames](TRANSCLUSION-FRAMES.md) establishes that semantic level of detail and visual point size are
**independent axes whose useful cells are off the diagonal** — a glyph blown up huge as a landmark, or
full text held at a tiny size for scanning. Both hold, and the table above is the *default policy* along
the diagonal, not the mechanism. Area picks a rung when nobody says otherwise; an overlay parameter
overrides it per subtree, exactly as a viewspec does. A renderer that couples the two axes with no
override collapses a 2-D space to its diagonal and loses the cells that were most worth having.

## The particle is the emoji, at low resolution

The bottom of the ladder does not need a new encoding, and this is the part that makes the whole thing
cheap. **An emoji drawn at three pixels is already a colored blob whose hue is the glyph's dominant
color.** So the transition from glyph to particle is not a renderer switch or a fallback path — it is
the same draw call with a smaller transform, and the semantics survive as color because color is what
survives.

Consequences, in rough order of how much they matter:

**A pile becomes a color region.** Members of one pile share their first glyph — 35 lenses all leading
with 👁️ — so at particle scale the pile is a *patch of one hue*, and a corpus's structure is visible as
color texture before any text is legible. That is the payoff for a rule that otherwise looks like
tidiness, and it is why the shared-lead rule is scoped to the pile and not to a type globally: skills
are addressed individually and each wants a distinct hue, while pile members are read as a set and want
a shared one. Both are right at their own scale. (The lint check enforces exactly this scope; see
[`../../skills/ties/scripts/ties_lint.py`](../../skills/ties/scripts/ties_lint.py).)

**The legibility floor gets weaker, in a good way.** The PSIBER rule was *"the point size is not allowed
to shrink smaller than 1, so that labels will never have zero area, and it will always be possible to
select them with the mouse."* That floor existed because an illegible label is an unclickable label.
A particle breaks the coupling: **a colored dot is illegible but still selectable**, and still carries
type. So the floor moves from "big enough to read" down to "big enough to hit", which is a Fitts
question rather than a typography one, and buys one or two more orders of zoom.

**Color wants to come from the glyph, not from a palette.** Deriving the particle's hue by sampling the
rendered emoji keeps one source of truth and makes the encoding self-maintaining: change the glyph and
the particle follows. A separate `color:` field would be a second place for type to be declared and
therefore a second place for it to drift — the undeclared-cache sin in
[TIES-SCHEMA.yml](../../skills/ties/TIES-SCHEMA.yml).

**Motion survives where text cannot.** A particle can pulse, drift or brighten, so attention weight and
read state remain expressible at a scale where no rung is readable — which connects to the candles in
[`../webtop/READ-UNREAD.md`](../webtop/READ-UNREAD.md) and to the attention mask in
[`../P-PYRAMID.md`](../P-PYRAMID.md), where the weight is already the plotter point size.

## Honest costs

- **Emoji are not a designed glyph set.** They are inconsistent in weight, hue and silhouette across
  platforms, so hue-derived particles will be less separable than a purpose-built vocabulary. The
  Pseudo Scientific Visualizer's hand-designed typed glyphs — array a circle, dictionary a circle with a
  dot, string *a line whose length encodes the string's length* — were better engineered for this, and
  the parameterized-glyph proposal in [`../webtop/GLYPH-BENCHMARK.md`](../webtop/GLYPH-BENCHMARK.md) is
  the route to having both.
- **Area-to-rung thresholds are guesses until measured.** Follow the lab that produced treemaps: run
  the experiment rather than arguing. The obvious test is a find-the-node task across zoom levels,
  against a labelled treemap and against text-only, which is the [glyph
  benchmark](../webtop/GLYPH-BENCHMARK.md) with a layout attached.
- **Treemap aspect ratios get ugly.** Slice-and-dice produces slivers; squarified treemaps fix the shape
  but destroy stable ordering, and stable position is what makes a view rehearsable. Unresolved, and the
  tradeoff is real rather than a matter of picking the newer algorithm.
- **Nothing here is implemented.** This is a design note joining three documented pieces. The weight
  exists in real manifests today; the layout and the renderer do not.

## Related

- [`../../skills/ties/RUNGS.yml`](../../skills/ties/RUNGS.yml) — the ladder, weights, big-endian glyphs
- [`PUMPING-UP-PIE-MENUS.md`](PUMPING-UP-PIE-MENUS.md) — the Dasher pivot, and per-cursor models
- [`PERIPHERAL-VIEWS.md`](PERIPHERAL-VIEWS.md) — viewspecs, shrink factor, the legibility floor, typed glyphs
- [`SPARSE-VIEW-OVERLAYS.md`](SPARSE-VIEW-OVERLAYS.md) — projection as an overlay parameter
- [`TEMPORAL-SEMANTIC-ZOOM.md`](TEMPORAL-SEMANTIC-ZOOM.md) — warping axes other than space
- [`../webtop/GLYPH-BENCHMARK.md`](../webtop/GLYPH-BENCHMARK.md) — whether glyph strings actually work
- [`../P-PYRAMID.md`](../P-PYRAMID.md) — the attention mask whose weight this layout renders
- [`../../skills/ties/README.md`](../../skills/ties/README.md) — the Shneiderman lineage in full
