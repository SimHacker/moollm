# The Window Resize Pie: direction selects, displacement manipulates, radius scopes

**Thesis:** Resizing a window is two separate problems that every window manager solves as one and
therefore solves badly — *which edge* and *by how much*. Split them. A pie menu names the edge by
**direction**, so acquisition costs nothing; the drag that follows is **relative**, so nothing jumps;
and **radial distance selects how far the operation reaches**, turning a single-window resize and a
tiling-panel seam drag into the same gesture at different radii.

Part of the **pie-stack-views** cluster ([README](README.md)). Reversibility model:
[RESELECTION.md](RESELECTION.md). The other meanings of radius:
[PUMPING-UP-PIE-MENUS.md](PUMPING-UP-PIE-MENUS.md#distance-as-appetite).

---

## The pie: eight items, and no one has to learn them

Four edges and four corners, each in the direction it lives:

```
        NW    N    NE
           ╲  │  ╱
        W ─── ● ─── E
           ╱  │  ╲
        SW    S    SE
```

Orthogonals are edges, diagonals are corners. The mapping is not a mnemonic to memorize, it is the
thing itself — which is the property pie menus have and lists do not, and the reason this particular
menu was worth building in NeWS before anyone asked for it.

## Two problems, usually conflated

A conventional resize handle fails twice, and it is worth separating the failures because they have
different fixes.

**Acquisition.** You must place the cursor on a border a few pixels wide. That is a Fitts's law
target with a tiny `W`, made worse by being at the window's extremity, and it is why every toolkit
eventually fattens the hit zone and thereby breaks something adjacent. The pie removes the target
entirely: **direction has no width.** Pop the menu anywhere over the window and flick northeast; you
never go near the corner.

**Nulling.** Buxton's nulling problem: with absolute control, when you take hold of something the
device's position and the controlled value must be reconciled, so either the value jumps to meet you
or you must first move to meet it. A resize that snaps the edge to the cursor is the jumping variant,
and it is why grabbing a border in some systems yanks the window by a few pixels before you have
asked for anything.

Relative control has no nulling problem, because only the delta means anything. So after the
direction is chosen, **you push the edge** — it starts where it is and moves as far as you move, and
your cursor's absolute position is never consulted at any point in the interaction.

That is the general form worth keeping: **direction selects the operand, displacement supplies the
quantity.** The pie is good at the first and terrible at the second; a drag is the reverse. Using
each for what it is good at is the whole trick.

## Radius as scope: the rings are hops, not pixels

The new part. Pull out a little and you have one edge. Pull further and the gesture recruits the
edges *adjacent* to it, so a shared seam moves as one and the layout behaves like a tiling window
manager's panel splitter. Overlay highlighting shows exactly what is currently recruited, so the
scope is browsed before it is committed — [reselection](RESELECTION.md) applied to the extent of an
operation rather than the choice of one.

The quantization should be **graph distance in the adjacency graph**, not a tolerance in pixels:

| Ring | Scope |
|---|---|
| 1 | this edge alone |
| 2 | + every edge sharing this seam |
| 3 | + the full column or row the seam belongs to |
| 4 | + the screen's whole partition along that axis |

Hops are learnable and stable; a pixel radius is neither. And the adjacency that defines a hop is
**"near enough," not touching** — edges within a tolerance are neighbors, so windows with deliberate
gaps between them still move together.

**Recruited edges keep their offsets.** This is the difference between a constraint and a snap:
capture each edge's offset when the scope locks, apply one delta to all of them, and the gaps survive
exactly as the user left them. Snapping would collapse them into a kiss, destroying spacing that was
probably intentional — the failure mode of most "smart guides." What is being preserved is a
relation, which is [Declare's](../webtop/temkin/README.md#declare-sql-for-interfaces) argument
arriving in a window manager: state the invariant, let the solver keep it true.

## Radius now means three things, and they must not collide

The radial dimension is the cluster's most reused resource, and this doc adds the third claim on it:

| Meaning | Where |
|---|---|
| **Precision** — arc length grows with radius, buying angular accuracy | [RESELECTION.md](RESELECTION.md) |
| **Appetite** — further out asks for more detail about the item | [PUMPING-UP-PIE-MENUS.md](PUMPING-UP-PIE-MENUS.md#distance-as-appetite) |
| **Scope** — further out applies the operation to more objects | this document |

They coexist only because they belong to different kinds of menu: appetite suits a *navigational*
pie where the item is a place, scope suits an *operational* pie where the item is a verb with an
operand. A menu that tries both at once is ambiguous and should be considered a design error rather
than a feature. Precision is free and compatible with both, being a property of the geometry rather
than a semantics assigned to it.

## The open seam: what locks the scope

If radius selects scope and the same continuous motion must also supply the resize displacement, they
compete for one dimension. Three resolutions, none free:

- **Press-drag-release, then drag.** Selection ends on release; a second relative drag resizes. Two
  gestures, unambiguous, and it matches how the NeWS pies already behaved — but it spends a clutch.
- **Monotonic-outward lock.** Scope grows while moving outward and locks on reversal. Elegant, and
  it **conflicts directly with reversibility**: pulling back in is supposed to *un*-recruit, and here
  it would commit. Reconcilable with a dwell, at the cost of the thing dwell always costs.
- **Modifier for scope.** Cheap, learnable, and it puts a chord in a gesture designed to avoid them.

The honest position is that this has not been tested and the first option is the safe default. It is
also exactly the sort of question the [tracking-hook channel](RESELECTION.md#tracking-hooks-the-candidate-channel)
exists to make measurable rather than arguable.

## Why it belongs in this cluster

The [tree-navigation invariant](../webtop/TREE-NAVIGATION.md) says every structural operation must be
reachable by keyboard, pie menu, **and** drag, all dispatching one named command. Window layout is a
tree — panels, splits, seams — and this is what the pie leg of that invariant looks like for it:
`resize(edge, delta, scope)`, with the pie supplying `edge` and `scope`, the drag supplying `delta`,
and a keyboard binding able to supply all three. If the resize pie cannot be expressed that way, the
invariant was decorative.

---

## Related

- [RESELECTION.md](RESELECTION.md) — browsing a decision before committing; the highlight-scope model
- [PUMPING-UP-PIE-MENUS.md](PUMPING-UP-PIE-MENUS.md) — radius as appetite, the other claim on the dimension
- [../webtop/TREE-NAVIGATION.md](../webtop/TREE-NAVIGATION.md) — one command set across keyboard, pie, and drag
- [../DYE-A-TRIBE.md](../DYE-A-TRIBE.md) — the critique of interfaces that removed affordances without replacing them
