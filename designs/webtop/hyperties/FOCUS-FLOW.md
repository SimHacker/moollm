# Focus flow — reveal-all-links, plus the order

*Don Hopkins · September 2026*

**Thesis:** HyperTIES' reveal-all-links answers *where are the links*. It does not answer *in what
order*, because a set of pop-out targets on an image has no reading order. Animate the tab sequence
through them — OpenLaszlo's chevrons between tab stops — and one gesture shows the entire input focus
flow: every link, and the path through them, text and graphics on the same path. Keyboard navigation
stops being an accessibility afterthought and becomes the map.

The crossover is worth naming: **Shneiderman's lab supplies the reveal, Temkin's supplies the flow.**
Two packs in this hub, joined at a feature neither of them shipped.

---

## What HyperTIES already had

Click or press the page background and every link highlights at once — text buttons inverting,
graphical targets popping out together. The mechanism was **pop-out**: offset the object slightly
in both axes and drop a shadow beneath it, so it lifts off the page.

The 1991 paper set three requirements, and they still bind anything built here: unambiguously
identify location and scope, do not interfere with comprehension of the image, and demand little user
effort. The trigger was derived from watching people fail:

> when confronted with an image with hidden targets, they tend to sweep across the image until a
> target is highlighted, or try to select what they think might be a target until one is found. This
> suggested that the system could highlight all of the targets automatically whenever it appears that
> the user is searching for targets, as when sweeping the display, **or clicking in non-target areas.**

A failed click is a request for the map. See [HN-ARCHIVE.md § 3](HN-ARCHIVE.md) for the full receipts.

## What it did not have: order

Text links inherit an order for free — prose has a reading direction, so the sequence of links in a
paragraph *is* the sequence of the sentences. That is the same free lunch synonyms give text and deny
graphics: the paper's phrase is that graphical targets "are not self-naming, as in the text case"
([ARTICLE-SCHEMA.md](ARTICLE-SCHEMA.md)).

Graphical targets fail at both. Six pop-out targets on an exploded Space Telescope diagram are a
**set**, not a sequence. Nothing tells you which is first, whether you have seen them all, or where
"next" goes. Reveal-all makes them visible and leaves them unordered, and an unordered set of six is
exactly the situation where a reader gives up and reads the prose instead.

## The chevron flow

OpenLaszlo animated chevrons between tab stops to draw the eye from → to. Applied here, and extended
from a pair to the whole sequence:

- **Reveal all links, and the path through them, in one gesture.** The trigger is already specified
  by the 1991 finding — the failed background click.
- **Text and graphics on one path.** Prose links and pop-out image targets are stops on the same
  flow, so an embedded diagram's pieces take their place in the document's focus order instead of
  living in a separate keyboard universe.
- **Gradient along the path.** Direction is encoded by the gradient's travel and by chevron motion,
  not by an arrowhead at one end. Dense prose gets a ribbon or region; sparse graphical targets get a
  line.
- **Tab is now legible before you press it.** The map tells you what the key will do. That is
  [reselection](../../pie-stack-views/RESELECTION.md) applied to the keyboard: browse the
  consequence before committing to it.

## Why the animation is load-bearing, not decoration

The 1991 paper already validated motion as the perceptual channel, in its argument for pop-out over
static highlighting:

> in addition, **the slight movement of the object makes it readily detectable to the eye.**

Pop-out uses motion to encode *position*. Chevron flow uses motion to encode *sequence* — which is
the one thing a static line genuinely cannot do, because a line between two points does not say which
end is first. Same mechanism, one dimension over, and the empirical support for the mechanism is
thirty-five years old.

Two constraints follow from the paper's own requirements. The overlay must not **interfere with
comprehension** (requirement two), which pop-out already respects by offsetting rather than
occluding — so the flow must route around targets rather than across them. And it must be
**interruptible**: the instant a key is pressed the animation yields to the user, per the kinetic
navigation contract in [Pie Menu Memory Palaces](../../pie-stack-views/PIE-MENU-MEMORY-PALACES.md).
Automatic while unattended, manual the moment it is touched.

## Prior art, honestly

Tab-order visualization exists and ships — browser devtools and accessibility extensions draw
numbered badges and polylines over a page. But it is a **debugging overlay for developers**: static,
deliberately ugly, opt-in through a devtools panel, and aimed at finding bugs rather than at reading.
The shipped reader-facing state of the art is the focus ring and the skip link, both of which are
strictly per-element and tell you nothing about the whole.

So the novelty claimed here is narrow and real: **the same artifact serving as reader affordance and
as accessibility map, triggered by a reading gesture rather than a developer tool.** Not the
visualization — the audience and the trigger.

## Honest costs

**It will expose that your tab order is wrong.** Real documents have focus orders that jump around,
skip regions, and trap. Visualizing it advertises the bug — which is a lint worth having and a hazard
worth admitting, because the first honest render of a complex page will be embarrassing.

**The flow is a tree, not a line.** Nested tab groups, focus traps in dialogs, and a pie menu inside
a page mean "next" is contextual. Rendering a tree as a single ribbon is a lie; the honest render
shows the current group's path and the exits from it, which is the sparse-overlay scoping rule from
[Sparse View Overlays](../../pie-stack-views/SPARSE-VIEW-OVERLAYS.md).

**Long documents overflow the gesture.** Sixty links on one page is not a viewable path. It needs
windowing or semantic zoom — show the flow near focus in full and the remainder collapsed to a
direction and a count.

**Motion is not available to every reader.** Since animation is doing real encoding work here rather
than ornament, `prefers-reduced-motion` cannot simply switch it off — it has to degrade to something
that still carries sequence, which means static numbered chevrons plus the gradient. Sequence
survives, the motion channel does not.

**The legibility floor applies.** PSIBER's rule — nothing shrinks below selectable size
([Peripheral Views](../../pie-stack-views/PERIPHERAL-VIEWS.md)) — governs chevrons too. A chevron too
small to see is worse than absent, because it implies the flow continues where the eye cannot follow.

## The same problem on a map: eBike Safari route overlays

Directionality on a route overlay is this identical encoding problem, and it is worth stating that
plainly because the solution transfers whole. **A drawn line between two points does not say which
end is first.** A GPS track rendered as a polyline is exactly that: correct geometry, no sequence.
Arrowheads at intervals are the usual patch and they are the static-highlighting answer — they
work, they clutter, and at low zoom they collide into noise.

Chevron flow answers it the same way it answers tab order: **motion encodes sequence, and the map is
where that is least ambiguous**, because a route already has a natural direction of travel and a
rider already reads motion along a path as progress. Animated chevrons marching along the track say
*this way* without adding a single labeled element, and the gradient carries the same information
redundantly for anyone who cannot see the motion.

What transfers from the focus-flow design, point for point:

| Focus flow | Map overlay |
|---|---|
| Motion encodes tab sequence | Motion encodes direction of travel |
| Gradient as the static fallback | Gradient along the polyline: start pale, end saturated |
| The flow is a tree, not a line | A ride is a line, but a *session* is a tree — branches, out-and-backs, repeated segments |
| Windowing when 60 links overflow | Windowing by zoom: animate near the viewport, collapse the rest to a direction and a distance |
| `prefers-reduced-motion` → numbered static chevrons | Same, plus the gradient, which the map has room for |
| Legibility floor: no chevron below selectable size | Chevron spacing must be a screen-space constant, not a world-space one, or zooming out shreds it |

Two things the map adds that the document did not have. **Time is real here**, so the animation has
an honest speed to run at — chevron velocity can encode actual pace, making a climb visibly slow,
which is encoding a second variable in the same channel for free. And **the track is already
annotated**: keyframes, clustered transcripts, and now souvenirs sit on it
([`DISPENSERS-AND-SOUVENIRS.md`](../DISPENSERS-AND-SOUVENIRS.md),
[`urban-safari/DATA-CONTRACT.md`](../../../skills/urban-safari/DATA-CONTRACT.md)), so the flow has to
route *through* markers rather than under them — which is the same nested-group problem as a pie menu
inside a page, one medium over.

The honest cost specific to the map: repeated segments. Ride the same street four times in a session
and four overlapping flows animate through each other into garbage. That needs either offsetting the
polylines, or picking one pass as canonical and rendering the rest as static shadows — and it is the
first thing to build a test case for, since it is the common case in a small town and not the
exception.

**Offsetting the polylines now has a principled form**, developed for a different purpose and arriving
here as the answer: a position on a path can be addressed as a blend of its endpoints plus a
**weighted offset expressed in the path's own frame**, whose *normal* component is which lane you are
in. Give each pass a distinct normal offset and repeated segments separate instead of overlapping;
tie the sign of that component to the direction of travel and an out-and-back ride separates
*automatically*, with no pass having to be nominated as canonical. See
[the offset is blendable too, which buys lanes](../../pie-stack-views/PIE-MENU-MEMORY-PALACES.md#the-offset-is-blendable-too-which-buys-lanes).

That also supplies the static fallback this section wanted, since **lane position encodes direction
without motion** — which matters most at exactly the zoom levels where chevrons collide into noise.

---

## Related

- [HN-ARCHIVE.md § 3](HN-ARCHIVE.md) — reveal-all-links, pop-out highlighting, and the failed-click finding
- [ARTICLE-SCHEMA.md](ARTICLE-SCHEMA.md) — why text is self-naming and graphics are not
- [LINK-RESOLUTION.md](LINK-RESOLUTION.md) — `~phrase~` (and the FORTH-era `.~ phrase~`), and links as phrases in prose
- [temkin pack](../temkin/README.md) — OpenLaszlo, LZX, and Declare, where the chevrons come from
- [Reselection](../../pie-stack-views/RESELECTION.md) — browse before committing; figure-ground separation
- [Pie Menu Memory Palaces](../../pie-stack-views/PIE-MENU-MEMORY-PALACES.md) — the interruptible-motion contract
- [Sparse View Overlays](../../pie-stack-views/SPARSE-VIEW-OVERLAYS.md) — scoped overlays, inheritance and override

↑ [hyperties pack](README.md)
