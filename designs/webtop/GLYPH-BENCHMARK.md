# The glyph benchmark

**Proposal: a better LLM eval than the pelican on a bicycle.**

> Make an SVG icon glyph for each of these 1,000 random documents — and the rest of the semantic
> pyramid, so it's easier for humans to judge by looking at the top levels. Looking at the tip of a
> semantic pyramid is a great way to grok something. — Don

Simon Willison's "draw an SVG of a pelican riding a bicycle" is the best-known informal LLM
comparison test, and it earns its place: cheap, memorable, hard to game, and it exposes the gap
between describing a thing and constructing one. But it has no **referent**. There is no fact of the
matter about what a pelican on a bicycle should look like, so scoring is vibes, and the only failure
it can detect is incompetence.

Ask for the glyph of a *specific document* and the referent appears. Now the question is not "is
this a good drawing" but **"is this a drawing of that?"** — and that has an answer.

## Why this is the right test for this design

The glyph is the top rung of the pyramid ([hub](README.md#the-semantic-pyramid)), the one below
gwern's link-icon: small enough to be a pie slice, a graph node, or a symbol on a map. It is also
the rung with the least prior art and the highest leverage, because it is the only rung that can be
**apprehended in parallel**. A page of a thousand abstracts is read serially and takes an afternoon.
A contact sheet of a thousand glyphs is scanned pre-attentively, in seconds, and the outliers jump
out. That asymmetry is the entire reason to want glyphs, and it is why judging glyphs is fast enough
to be a benchmark at n=1000.

The other reason: **you cannot fake a glyph by extraction.** A model can produce a passable abstract
by lifting the topic sentence, and a passable title by copying the heading. Neither requires
understanding what the document *is*. Compression to a single mark has no extractive shortcut. There
is no phrase to steal. Either the model knows what the thing is about or it draws a gear.

## The scoring protocol

The user's framing hands you a metric almost directly. Generate the pyramid — glyph, title,
abstract — for each document. Then:

1. **Blind match.** Shuffle glyphs and titles separately; ask a human to pair them. Report top-1
   accuracy. This is objective, fast, and requires no rubric.
2. **Distinctness.** Count near-duplicate glyphs across the corpus. Report the duplicate rate and
   the entropy of the visual vocabulary. A model that renders 1,000 documents as 40 distinct icons
   has failed even if each icon is individually reasonable.
3. **Legibility at size.** Render at 16px, 24px, and pie-slice size, monochrome, and re-run the
   blind match. A glyph that only reads at 256px is decoration, not a rung.
4. **Contact-sheet grok.** Show a human the sheet for a corpus they know and ask them to find a
   named document, and to describe what the corpus is about. Time both. This tests the claim that
   the tip of the pyramid is where understanding happens.
5. **Misleading rate.** Separate from wrong: how often does a glyph confidently suggest the wrong
   subject? This is the only metric that matters for shipping, because a wrong glyph is worse than
   no glyph — it is the thing people navigate by.

Steps 1 and 2 are the core. Everything else is diagnostic.

There is a variant with a scoring function that needs no human raters at all — the bingo card, whose
squares can be scored by hit rate against comparable documents, with maximum information at *p* = ½.
See [SUMMARY-GENRES.md](SUMMARY-GENRES.md#why-the-bingo-card-is-a-better-benchmark-than-the-glyph).

## The predicted failure, which is the point

Mean regression. The ambient `no-ai-slop` diagnosis — *specific becomes generic, nuanced becomes
puffed* — should show up here as a **visual** phenomenon, which makes it measurable in a way prose
slop is not. Expect gears, lightbulbs, documents-with-folded-corners, and abstract network graphs,
distributed roughly according to how much the model has given up on the document.

That is the benchmark's real value: it renders the model's laziness in a form a human detects
instantly. You cannot skim 1,000 abstracts to find where the model stopped trying. You can see it in
a glyph grid immediately, as a field of gray gears with a few good marks scattered in it.

## One correction to the proposal

A thousand distinguishable glyphs is not achievable and should not be the target. Visual vocabulary
saturates long before that — this is the same wall icon designers hit in large toolbars, and the
reason file managers still ship a generic document icon. Past a few hundred, collisions are
mathematically forced, not a model failure.

So the honest target is not uniqueness. It is:

- glyph **plus title** as the unit, which is what an icon with a label is, and what a pie slice is;
- collisions **detected and reported** rather than silently shipped.

## Parameterized glyphs: don't draw a thousand, blend them

The correction above ends by guessing that the right answer may be "a designed vocabulary plus a
per-document parameter, not a thousand drawings." **That machinery exists, it was built at Interval
Research, and its patent expired in 2016.**

Tom Ngo's **Embedded Constraint Graphics** puts example images at the **vertices of a simplicial
complex** and represents any intermediate state as **barycentric blend weights** over them — drag a
feature and the system solves for the weights. Ngo's own framing of why the structure generalizes:

> Gluing high-dimensional simplices at their edges and faces is an extremely general way to
> represent blending manifolds — in the same way that gluing polygons together has done us so much
> good in 3D modeling.

Applied to the glyph rung, that changes the model's job from *drawing* to *locating*, and every hard
problem in this document improves at once:

- **Saturation stops being a wall.** A dozen hand-designed extreme targets and a continuous weight
  vector yield a thousand *distinct* glyphs without a thousand drawings. Distinctness becomes a
  distance in the configuration space rather than a visual-similarity judgment.
- **Mean regression becomes impossible by construction.** A model emitting barycentric coordinates
  over designed targets *cannot* draw a generic gear, because no gear is in the space. The failure
  mode changes to landing near the **centroid** — the blend of everything, which is the visual
  average — and that is measurable as a number. Distance from the centroid replaces a human rater
  for the laziness check, which is the metric this benchmark most needed.
- **The output is inspectable and editable.** A weight vector is a handful of declared numbers, so a
  wrong glyph is corrected by nudging coordinates rather than by redrawing SVG. This is exactly the
  "open it up and edit the `0.5`" property, and it is why parameterized glyphs belong to the
  [homoiconicity](../object-system/HOMOICONICITY.md) argument as much as to this one.
- **The task is better conditioned for a language model.** Emitting coordinates in a known basis is
  classification into a designed vocabulary, not free-form image synthesis — far closer to what
  models are reliable at, and far cheaper to review.
- **Glyphs can encode scalars, continuously.** PSIBER already did the one-dimensional case: *a string
  is a line whose length depends on the length of the string.* That is a 1-simplex. ECG is the
  general form, so a glyph can carry size, age, link count, and controversy as positions along
  designed axes.

The division of labor is the appealing part: **a human designer defines the space, and the model
places documents in it.** The designed vocabulary keeps the PSIBER virtues — a small closed set,
chosen for discriminability at size, with jokes where jokes aid memory — while the parameterization
supplies the per-document specificity the closed set cannot.

Provenance and status: [US5933150](https://patents.google.com/patent/US5933150), *System for image
manipulation and animation using embedded constraint graphics*, filed 6 August 1996, **expired
roughly August 2016**. Don's write-up is in WWSFF at
`characters/don-hopkins/tom-ngo-embedded-constraint-graphics-at-interval.md`, with the Breakfast
Simplex as the worked example — recipes parameterized by `{egg, milk, flour}` ratios on a simplex,
where adding an ingredient adds a dimension and changing prep method creates an adjacent region. A
paired repo-show with Tom Ngo and Golan Levin on ECG and Mouther is already seeded.

That second point is the same mechanism the synonym compiler needs: two articles claiming one name
is a link error, and two documents claiming one glyph is a link error, and in both cases the right
move is a build-time diagnostic offering a small set of choices at a known position. The glyph
namespace and the synonym namespace have the same collision problem and want the same resolver.

### The grounding: this is blend shapes, and everyone already has the intuition

Before the theory, the reference that makes it free. **This is facial blend shapes.** ARKit's
blendshape coefficients, FaceIt-style rigs, and mesh morph targets in general are exactly this
construction, shipped and familiar: a set of hand-authored extreme poses, and any expression is a
weighted combination of them. Nobody sculpts a face per frame; they name the dimensions once and
drive the weights.

Naming it that way imports the whole intuition at no cost, including the parts that matter here:

| Blend shapes | This benchmark |
|---|---|
| Hand-authored extreme poses | The designed morph targets |
| Coefficient vector per frame | Blend weights per document |
| Targets chosen to be independently meaningful | The distinctness requirement below |
| All-weights-averaged gives a mushy neutral face | The centroid, i.e. a portrait of slop |
| Rig authored once, drives unlimited animation | Basis authored once, glyphs any number of documents |

The 2D cases are the same construction with fewer dimensions: Tom Ngo's ECG, and Golan Levin's
facial-expression targets. Which is why the ECG connection is not an analogy — a glyph basis is a rig,
and generating a glyph is posing it.

### Let the model generate the basis, and lint the basis

The division of labor above — human designs the space, model places documents in it — assumes a human
draws every morph target. Don's extension: **ask the model to generate the morph targets themselves.**
Name the dimensions you want combined, and let it draft the vertices.

That changes the human's job from drawing to *naming*, which is the part only the human can do. You
say the dimensions — `historical ↔ speculative`, `technical ↔ social`, `first-person ↔ surveyed`,
`built ↔ proposed` — and the model drafts a target for each pole. Then you curate, and only then does
it place documents. A three-step with review at the *space* level rather than the artifact level,
which is dramatically cheaper: reviewing eight basis targets is an afternoon; reviewing a thousand
glyphs is never.

The naming step is also where the interesting control lives, because the dimensions are combinable on
demand — "blend between pivots, reamplifications, and views," in Don's phrasing. A **pivot** is
already this corpus's word for a reversible turn into another projection
([the Dasher pivot](../pie-stack-views/PUMPING-UP-PIE-MENUS.md#the-dasher-pivot)); a
**reamplification** is re-weighting a dimension you already have, which is a blend-weight change and
not a redraw. So the same basis serves many cards, and switching which dimensions are amplified is a
parameter edit rather than a regeneration.

**But this relocates mean regression rather than eliminating it, and that is the thing to say out
loud.** The earlier claim in this section — that a model emitting coordinates over designed targets
*cannot* draw a generic gear — holds only if the targets are genuinely distinct. If the model drafts
eight mutually similar basis vertices, every blend of them is generic and no amount of clever
weighting recovers specificity. Regression moves up a level, from the artifact to the basis.

Which is good news, because it moves the failure somewhere auditable. **Eight things to check
instead of a thousand**, and the check is the same distinctness lint already specified for glyph
collisions and [synonym collisions](hyperties/LINK-RESOLUTION.md): pairwise distance across the
basis, with a floor, failing the build when two vertices are too close. Plus one new diagnostic that
falls out for free — **render the centroid and look at it.** The blend of everything is the
maximally generic output of the space, so it is a portrait of the slop this construction exists to
avoid, and if the centroid looks *fine* the basis is too narrow.

And the generated basis is an artifact: inspectable, editable, diffable, versioned. Warm generation
at build time, frozen vocabulary at run time — [the compiler thesis](../TAGSONOMY-COMPILER.md)
applied to the drawing vocabulary itself.

### The user-editable type: paths through distortion, clipping, and expansion maps

The type this wants is not "an SVG." It is **ECG paths mapped through distortion, clipping, and
expansion maps** — a deformable vector object whose deformations are themselves data.

Three ancestors, and the middle one is the direct-manipulation model:

**Kai's Power Goo** (Kai Krause, MetaCreations) made warping a *toy* — you smear an image with your
finger and it goes where you push, continuous and immediate with no dialog and no numeric fields.
Correct interaction model, wrong substrate: it warps pixels, so it does not scale.

**Glenn Reid's TouchType** (NeXT, ~1990, Display PostScript) is the one to steal from, and its key
property is subtle. It took the Illustrator draw-program metaphor and extended it to individual
characters of a text object — but *without dissolving the text into loose shapes*. The 1990 BaNG
meeting review puts it exactly: the `a` in `BaNG` can be moved independently of the rest of the word,
**yet TouchType still remembers that the `a` is associated with the other three letters.** Automatic
and manual kerning, sliders for size, leading and width, and an option to snap everything back to a
single baseline — so the deformation was always reversible and the string was always still a string.

That is **the dual-interface property this hub keeps rediscovering**, in typography: the object is
simultaneously a text string and a set of independently placeable geometric objects, and neither view
is a lossy export of the other. Same shape as a directory that is both document and room, and as a
README that is both prose and a directory listing. Reid got there in 1990, in six weeks, on Display
PostScript.

**Illustrator and Flash** supply the third piece — vector graphics and text as a resolution-
independent medium — which is what makes goo-style warping over TouchType-style structure
"smoothly and infinitely scalable" rather than a raster effect.

Combine them and the type is: a path basis, blend weights over it, and a stack of deformation
maps — **all three of which are inspectable, diffable artifacts.** Which makes the deformation
itself environment-as-data, the property [HOMOICONICITY.md](../object-system/HOMOICONICITY.md#the-forgotten-half-postscripts-environment-was-also-data)
identifies as the forgotten half. A glyph stops being an opaque drawing and becomes an openable
expression: *this basis, these weights, these distortions*, each editable by hand or by direct
manipulation, and each surviving into the next render.

Don's characterization of TouchType is that it was font-appreciation paraphernalia — "a bong for
text" — and the joke has a real point inside it: the app's purpose was *appreciation*, not
production. It made typography pleasurable to fiddle with, which is why people remember a six-week
NeXT app thirty-six years later.

Two history notes worth keeping. Adobe shipped a "Touch Type Tool" in Illustrator decades later,
spelled with a space, **without credit or royalty to Reid** — Don's own HN comment on this is in the
corpus's Winer-sweep data. And per a NeXTSTEP collector's sale listing, **Adobe lost the TouchType
source code**, apparently well before 2010. So the exemplar of the property survives as a
description, a manual, and a few floppies, which is this hub's linkrot argument arriving in the one
place that stings.

## Where it fits the debt argument

Borretti's strongest hit is that every node is a debt and every link doubly so
([OBJECTIONS.md](OBJECTIONS.md#every-node-is-a-debt)). The answer this hub gives is that generated
rungs nobody maintains are not debt. **The glyph benchmark is how that answer gets tested rather
than asserted.** If generated glyphs score badly on blind matching, then the rungs are not free — a
human has to fix them, and the debt is back. The claim and its test are the same artifact.

And glyphs are compile-time artifacts: generated once, reviewed in a batch, committed as text,
served with no model in the loop. Nondeterminism at build time, determinism at run time.

## Prior art, from inside this corpus

The glyph rung is not new here, and the earlier attempt sets a bar worth measuring against. The
Pseudo Scientific Visualizer in *The Shape of PSIBER Space* (1989) drew PostScript data structures
as a fisheye — *"arbitrarily large, arbitrarily deep structures, in a fixed amount of space"* — with
a hand-designed typed glyph vocabulary: an array is a circle, a dictionary is a circle with a dot, a
name is a triangle, a boolean is a peace sign or an international no sign, an event is an envelope,
a process is a Porsche, and **a string is a line whose length depends on the length of the string.**

Three things that vocabulary got right, which the benchmark above should require:

- **A small closed set, chosen for discriminability at size,** not one bespoke mark per object.
  The n=1000 test measures whether a model can do better than this; it may well be that the right
  answer is a designed vocabulary plus a per-document parameter, not a thousand drawings.
- **A glyph that encodes a scalar.** String length as line length means the mark carries data, not
  just category. Nothing in the protocol above asks for that, and it should — a glyph that shows a
  document's size, age, or link count is strictly more useful than one that shows only its topic.
- **A joke that survives shrinking.** A process is a Porsche. Distinctiveness and memorability are
  the same property as legibility here, and the funny glyph is the one you remember in the grid.

The relevant view rule from the same paper is the legibility floor, stated as an invariant: *"the
point size is not allowed to shrink smaller than 1, so that labels will never have zero area, and it
will always be possible to select them with the mouse."* Step 3 of the protocol is that rule turned
into a measurement. See [`pie-stack-views/PERIPHERAL-VIEWS.md`](../pie-stack-views/PERIPHERAL-VIEWS.md#the-glyph-rung-already-typed)
and [`../pie-stack-views/`](../pie-stack-views/README.md).

## Honest costs

- **Contamination.** The pelican's virtue is that it is uncontaminated. A thousand real documents
  may be in the training set, which inflates scores in ways the pelican never could. Any serious
  run needs a held-out corpus and should report which. The private repos in this constellation are
  the usable held-out set, since visibility here is inferable from the name — `DonHopkins`, and any
  repo with "private" in it, are private and therefore in no training set. Being uncontaminated is
  a second, unrelated reason to keep them that way.
- **Cost.** A thousand pyramids per model is not a tweet-sized test. This is an eval, not a party
  trick, and it will not spread the way the pelican did.
- **Human in the loop.** Steps 1 and 4 need people. Automating the blind match with a
  vision model measures agreement between two models, which is a different and much weaker claim.

## Status

A proposal, not a result. Nothing here has been run. The corpus is available — this constellation of
repos is thousands of `CARD.yml`, `GLANCE.yml`, and `README.md` files with human-written titles and
descriptions already in place, which is exactly the ground truth a blind match needs.

↑ [webtop hub](README.md) · [objections](OBJECTIONS.md) · [article schema](hyperties/ARTICLE-SCHEMA.md)
