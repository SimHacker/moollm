# Sparse shadow trees — null means "ask your parent"

*Part of the [Korz cauldron](../README.md). A name for a pattern the
[design](README.md) keeps using without naming — and the resolution of
the one null that [epistemics.md](epistemics.md) doesn't ban.*

A **sparse shadow tree** is a secondary hierarchy that shadows a dense
primary tree but only materializes nodes where a value actually
*changes*. Everywhere else the slot is empty, and empty means
**delegate up** — fall through to the nearest materialized ancestor.

## The type specimen: ScriptX clocks over views

ScriptX was Kaleida Labs' multimedia language (Apple × IBM, early
'90s; Don was there). Every view has a clock slot; the root view has
the root clock. A subview's clock is either null — inherit your
(grand\*)parent's clock — or an explicit reference, which may just
point at the same clock the parent uses; same effect either way. The
default is inherit, so you never end up with unnecessary clocks: the
clock tree stays a sparse shadow of the dense view tree, materialized
only where somebody actually needed a new timebase (a paused panel, a
reversed movie, a slow-motion inset). Time inheritance rides the
containment hierarchy for free, and overriding it costs exactly one
node.

The same term describes MOOLLM's **placement hierarchy**: the
containment tree of *rooms holding things* is a sparse tree over the
physical directory tree, skipping the intermediate chrome —
`sources/`, `media/`, organizational directories that exist for
filing, not for meaning. Placement materializes only at the
semantically load-bearing nodes; everything between them is
fall-through.

## N dimensions, one tree

This answers a Korz scaling worry directly: won't N dimensions demand
N parallel trees? No — **one dense tree, N sparse shadows, each nearly
empty.** Every dimension (time, style, provenance, security, mood)
keeps its own shadow over the same files, materializing a coordinate
only where it changes; absence delegates up. This is prototype
delegation projected onto containment — don't copy, don't materialize,
fall through — which is why it feels Self-shaped: the shadow tree is
to the containment tree what the parent slot is to the object.

**Ethics is one of the shadows.** A MOOLLM directory can optionally
declare an ethical scope — consent levels, portrayal rules, forbidden
topics, what may be quoted — or declare nothing and inherit from its
**ethics-parent**. A child scope *refines*: it makes the inherited
rules more specific, tightens them, or sandboxes its subtree entirely,
exactly the way a ScriptX child clock transforms its parent's time —
offset it, scale it, even reverse it — without ever escaping the
parent's timeline. The refinement is one-way by default: a subtree can
always forbid more than its parent, but loosening what the parent
forbids requires explicit consent recorded *at the parent*. A sandbox
is then nothing special — just a directory whose scope says "stricter
in here" — and a private annex is a shadow node materialized where the
public default stops being true. One dense tree of files; the ethics
ride above it as a nearly empty shadow, materializing only at the
doors where the rules change.

## Prior art is everywhere once it has a name

**CSS inherited properties** (set `color` on one node; ten thousand
descendants read it without storing it), **X resources** falling
through the widget hierarchy, **git config** (system → global → repo →
worktree), **process environments** (fork inherits; override one
variable), **Emacs buffer-local variables** shadowing globals. The
dense counterpart is the scene-graph transform, where *every* node
composes; the sparse shadow is what you build when most nodes have no
local opinion. (Not to be confused with the DOM's "shadow tree," which
is encapsulation — walls. This is the opposite: transparency by
fall-through.)

## But which parent? "Ask your parent" is a big ask

In a soup, "parent" has a lot of subjective and objective meanings at
once: the same node is embedded in many hierarchies simultaneously —
physical directory parent, placement parent, time parent, style
parent — and may have **multiple parents within one hierarchy**
besides. An unqualified fall-through instruction would be a dangling
pointer of a different flavor.

The resolution is that the null is **dimension-indexed**: empty
doesn't mean "ask *the* parent," it means "ask my predecessor **along
the tree whose shadow this is**." So: a null clock means **inherit
from your time-parent**. A null placement means ask your
**place-parent**; a null style, your **style-parent**. The hyphenated
compound is the dimension index made visible in the name — big-endian
naming applied to kinship, so the word itself carries the guard. Each
sparse shadow supplies its own parent function; the time-parent climbs
the view tree, the place-parent climbs the room tree, and they can
disagree about who your parent is without conflict, because they are
different questions. ScriptX and CSS never noticed the problem only
because their hosts were single-parent trees — the degenerate case
where all the parent functions coincide and "parent," unqualified, is
harmless.

And when a single dimension genuinely offers multiple parents (ordered
delegation, Self-style), fall-through lands in machinery the design
already built: **ordered parents** resolve it the way Self's parent
priorities do, and a genuinely unordered tie is just **ambiguity**,
handled by the standing policies — `error` in the strict tier,
`sample` or `blend` in the soft tier
([design.md](README.md); for blending, see the
[troll example](examples/troll-blend.md)). Whether that's a feature or
a horror is a per-dimension guard decision, which is exactly where
Korz likes to put such decisions.

## The benign null

One more resolution for the null question in
[epistemics.md](epistemics.md): *this* null is the benign kind. It
isn't Hoare's billion-dollar "value that explodes when touched" — it's
a **delegation instruction**, "no local opinion, ask my parent along
this dimension." Absence-as-delegation is the one null that was never
a mistake; Self bet the whole language on it — though Korz has to say
*which* parent, because it dissolved the privilege of having only one.

---

*The ScriptX history continues in Don's
Kaleida notes.*
