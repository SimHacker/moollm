# Typed data islands

**A markdown document with typed data embedded in it, read by an extensible renderer that
dispatches each type to a viewer.** The format the webtop reads, presents and edits. HyperTIES
pictures and targets are the first hard test of it, and they fit — but only after one thing is
settled that the 1988 format left implicit.

Four decisions, all of which lean on machinery that already exists here.

| Question | Decision |
|---|---|
| How does an island declare its type? | Second word of the fence info string: ` ```yaml Picture ` |
| How does it point outward instead of embedding? | `$ref`, resolving a **name** in the island's namespace — not a path, not a new tag |
| Can targets overlay any image, or only a `Picture`? | Any island that declares itself a **stage**. `Picture` is the first of several |
| How do targets bind to the thing they overlay? | Implicit on the way in, explicit in the resolved model — [postel](../../skills/postel/) |

## The fence carries the type

````markdown
```yaml Picture
name: Founders
src: images/founders.png
```
````

Lowercase first word is the language, CapWords second word is the type. No spec needed to read
that; the casing carries it.

**This is safe with parsers that know nothing about it.** CommonMark defines the info string as
everything after the fence and reserves only the convention that the first word names the language,
so highlighters take word one and ignore the rest. The pattern is well-trodden: Docusaurus writes
` ```js title="x.js" `, VitePress writes line ranges there, MDX passes the whole string as meta,
Pandoc takes `{.yaml #id}`. GitHub will syntax-highlight the YAML and render the block as a code
block, which is **the graceful degradation `apps/ties/FORMAT.md` already claims as a virtue** (in
WillWrightShowForFood): a reader without the applet layer still sees something true.

`markdown-it` puts the full info string in `token.info`, so the type is already in hand wherever
fences are processed. Types are `yaml`, `json` or `csv` bodies as convenient; the type name says
what the data *is*, the language says how to parse it.

## Pointing outward: `$ref`, and it resolves a name

The question was how to point at external content without hoisting it into an island and without
scattering magic URL tags through the prose. A typed wrapper is the right instinct. Two corrections
to it, both from decisions already made in this hub.

**Spell it `$ref`, not `PROXY`.** JSON Schema, OpenAPI and AsyncAPI all run on `$ref` with exactly
the semantics wanted — *replace this node with what it points at*. [korz addressing](../korz/korz-prime/addressing.md)
already cites it as "the `$ref` idiom JSON Schema runs on". A new word for a known thing is a cache
miss that never fills ([no-ai-humansplaining](../../skills/no-ai-humansplaining/)); `$ref` is
prepaid vocabulary.

**Point by name, not by path.** This is the load-bearing correction.
[LINK-RESOLUTION.md](hyperties/LINK-RESOLUTION.md) settles that references are names resolved in a
scope, with **type coming from position**, and the island's declared type *is* a position. So:

```yaml Picture
$ref: Founders
```

resolves `Founders` in the pictures namespace by the scope walk, the same way `~Founders~` resolves
in prose. A path is the escape hatch, not the norm — recognised by carrying a slash or an extension:

```yaml Picture
$ref: ./pictures/founders.yml    # a file, when you genuinely mean a file
```

Name-first matters for the translation specifically: **the 1988 storyboards reference pictures and
targets by name, because that is all Weiland's index could resolve.** Converting those references to
relative paths would throw away the property that makes the corpus survivable, and then the
conversion would have to be undone later to get synonyms back.

`$ref` works at any depth, which answers the narrow version of the question: a pointer does not need
an island of its own. Put it at the leaf of an otherwise-inline island.

```yaml Picture
name: Founders
shapes:
  - $ref: HSP
  - $ref: Spectrograph
```

**Siblings override.** JSON Schema 2020-12 and OpenAPI 3.1 both allow keys beside `$ref`, and that
is exactly what the scaling case needs — one shared picture, sized per article:

```yaml Picture
$ref: Founders
size: [507, 598]
```

**Transparency is a property of the loader, not the syntax.** Refs resolve before the renderer sees
anything, so a viewer cannot tell whether its data was inline or fetched. That is what makes the
embed-or-point choice free to change later. Deferred loading of something enormous — a city, a video
— is then the *viewer's* decision, not a second kind of pointer.

## Stages: what a target actually needs

The direct question was whether targets can overlay any old image or div, or only a special
`Picture`. **Neither. They overlay anything that declares itself a stage, and `Picture` is simply
the first type that does.**

A target does not need an image. It needs three things:

1. **A containing block** — something with its own box for the overlay to be positioned against.
2. **A declared coordinate space**, so geometry means something.
3. **An identity**, so a target can say which stage it belongs to.

Requiring a `Picture` fails the interesting cases immediately: a hotspot on an ebike-safari map, a
region of a Micropolis city, a moment in a video. Accepting "any image or div" fails differently —
a markdown `![](…)` inside a paragraph has no positioning context and no declared intrinsic size, so
normalized geometry would anchor to a box that may be inline, wrapped, or zero-height.

So: **opt-in.** Any island type may be a stage by declaring a `space`. A plain markdown image is not
one, and is promoted by wrapping it — one line, explicit:

````markdown
```yaml Picture
$ref: images/founders.png
```
````

Coordinate spaces, which is where this generalisation pays for itself:

| `space` | Geometry means | Used by |
|---|---|---|
| `normalized` | 0..1 of the content box, stretched (`preserveAspectRatio="none"`) | `Picture` — the 1988 default |
| `pixel` | device pixels against a declared intrinsic `size` | scanned pages, pixel art |
| `geo` | longitude / latitude | `Map` |
| `cell` | integer tile coordinates | `Micropolis`, any grid |

`normalized` is why one 1988 geometry served renderings at 450x337, 507x598 and 533x509. Keep it as
the default and resolution independence comes along for free.

**The stage is the media element's content box, not the wrapper.** This is already learned the hard
way in `src/lib/TargetApplet.svelte`, whose comment records it: anchoring the overlay to the
`figure` instead of the `img` stretches normalized geometry over the caption too and shifts every
shape downward. The contract has to name the box.

## Binding: implicit in, explicit out

In 1988 a `.picture` was followed by any number of `.target`s that implicitly overlaid it — 38
pictures carrying 187 targets across the archive, so roughly five targets per picture, none of them
naming their host. Authoring wants to keep that. An editor cannot rely on it.

The rule: **a target binds to the nearest preceding stage in the same section.** Prose between them
is fine, because the storyboards interleave. A heading resets it, because a heading is where a
reader believes a new subject starts and is the boundary an editor will respect.

Then two obligations:

- **Resolve to an explicit stage id in the parsed model, always.** Viewers and editors see a bound
  pair, never an adjacency they have to re-derive.
- **Write the explicit `stage:` back only when the implicit reading would be wrong** — when
  something moved and adjacency no longer says what the author meant. Converted files stay as clean
  as the source until an edit makes them lie.

A target with no stage in scope is **an error the converter reports**, matching FORMAT.md's existing
promise that an unresolved name is never silently dropped. Silence here means an invisible hotspot,
which is the worst possible failure: the page looks fine and a link is gone.

### Why this is a new question

Worth noting that the current converter dodged it by **merging**: one ` ```target ` island carries
`picture:` plus a `shapes:` list, so binding is structural and free. The cost is the reason to move —
you cannot add a target without rewriting the picture's block, two articles cannot share a picture
while overlaying different targets on it, and nothing but a picture can host a target. Separating the
islands is what buys editability and live stages, and binding is the bill for it.

## Worked example

The Sun founders photo with two hotspots, as the three islands the converter would emit:

````markdown
```yaml Picture
name: Founders
synonyms: [the founders photo, Sun founders]
$ref: images/founders.png
space: normalized
size: [507, 598]
```

Vinod Khosla, Andy Bechtolsheim, Bill Joy and Scott McNealy, ~Sun Microsystems~, 1982.

```yaml Target
name: Bill Joy
to: Bill Joy
shape: shapes/joy.svg      # normalized 0..1, y already flipped
```

```yaml Target
name: Andy Bechtolsheim
to: SUN workstation
shape: shapes/bechtolsheim.svg
```
````

Both targets bind to `Founders` implicitly. Each is **a named, resolvable node in the targets
namespace** — which is what makes single-click-shows-definition work, and what lets prose elsewhere
say `~Bill Joy~` and land on the same entity.

The same two targets over a live map, unchanged except for the space they live in:

````markdown
```yaml Map
name: Canal ring ride
space: geo
center: [4.89, 52.37]
```

```yaml Target
to: Leliegracht horse hoist
at: [4.8846, 52.3751]
```
````

## What it costs

Smaller than it looks, because the shape is already there. `src/lib/markdown.js` already splits a
body into segments and hands `{kind:'target', spec}` to a Svelte component. The changes are:

1. Parse the info string instead of matching the literal `​```target`, yielding `{kind, type, data}`.
2. Replace the hardcoded `TargetApplet` dispatch with a **type → viewer registry**, which is the
   hookable renderer. Unknown type renders as a code block, which is the degradation already relied on.
3. Resolve `$ref` in the loader, against the index the corpus already builds.
4. Add the stage pass: bind targets, report orphans.

Steps 1 and 2 are a refactor of about thirty lines and are worth doing even if nothing else here is
adopted, because they are what let a `Map` or a `Micropolis` island exist at all.

## Open questions

- **Does `name:` inside an island register it in the namespace, or does only the file's front matter
  do that?** Registering from islands is what makes a target addressable, but it means the index
  must parse bodies, not just front matter.
- **Can an island be a stage *and* a target of another stage?** A map inside a picture region is
  absurd until someone wants an inset.
- **CSV islands with a type** — ` ```csv Rides ` — need a column contract somewhere. Probably a
  `$schema` sibling, which is the same borrowed vocabulary again.
- **Editing round-trip fidelity.** The rule above keeps converted files clean, but an editor that
  reformats YAML will still churn them. yaml-jazz comments are fieldwork and must survive; that
  likely means a comment-preserving writer, not `js-yaml`'s dump.

↑ [webtop hub](README.md) · [article schema](hyperties/ARTICLE-SCHEMA.md) · [link resolution](hyperties/LINK-RESOLUTION.md) · [yaml jazz](../../skills/yaml-jazz/)
