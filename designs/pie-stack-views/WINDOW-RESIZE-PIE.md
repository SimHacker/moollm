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
menu was worth building in NeWS before anyone asked for it. Don's own statement of why the domain
fits:

> Window managers tend to have directional commands: open on left or right side, **resize from
> bottom right corner**, move to top or bottom layer, etc, which correspond nicely to pie menu
> directions, so they're obvious, easy to learn, remember, and use without looking or waiting.

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
your cursor's absolute position is never consulted at any point in the interaction. It buys more than
the missing jump, too: it opens the gap where
[friction strips and physics](#friction-strips-snapping-that-never-gets-ahead-of-the-gesture) live.

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

### Inferred per gesture, never enforced

The adjacency graph is **computed at grab time from where the windows actually are**, and thrown away
when the gesture ends. That is the whole difference from a tiling window manager: a tiling WM makes
you live inside its layout tree, and every window you open has to find a home in it. Here windows
float, overlap, and sit at whatever gaps you left them; the tree is a *momentary interpretation* of
the current arrangement, produced to answer one question and then discarded.

So you get tiling behavior on demand without the straightjacket, and the cost is honest: **inference
can guess wrong.** Which gives the overlay highlight its real job — it is not decoration, it is the
guess made visible *before* it acts, so a wrong interpretation is corrected by pulling back in rather
than undone afterward.

**Recruited edges keep their offsets.** This is the difference between a constraint and a snap:
capture each edge's offset when the scope locks, apply one delta to all of them, and the gaps survive
exactly as the user left them. Snapping would collapse them into a kiss, destroying spacing that was
probably intentional — the failure mode of most "smart guides." What is being preserved is a
relation, which is [Declare's](../webtop/temkin/README.md#declare-sql-for-interfaces) argument
arriving in a window manager: state the invariant, let the solver keep it true.

## Friction strips: snapping that never gets ahead of the gesture

Snapping usually ruins this, and the reason is specific. Naive snap-dragging is **position-based
capture**: get near a target and you are taken. Which means the values *near* the target become
unreachable — you cannot park an edge three pixels off a guide, because the field eats it — and the
interface has quietly decided that your intent was the round number. Every over-eager alignment
system has this bug, filed as a feature.

The fix is **hysteresis instead of gravity.** Do not move the edge to the value; **hold it there and
consume motion** until enough has accumulated to escape. Quantization by effort supplied rather than
by proximity achieved. Every value stays reachable, because the snap costs a little push to leave and
nothing to pass through slowly.

**Relative control is what makes this possible at all**, and this is the deeper payoff of the nulling
fix above. Under absolute tracking the object must stay under the cursor, so any hold opens a visible
gap between the two — you have reintroduced nulling to implement snapping. Under relative control the
edge was never tied to the cursor, so there is somewhere to stand between input and effect:

```
raw delta ──▶ [ transfer function ] ──▶ applied delta
                 friction · detents · gain · physics
```

Two strips are enough for most of it:

- **Zeroing strip (a detent).** Contributes nothing until accumulated motion through it passes a
  threshold, then releases. One real decision inside it: the consumed motion is either *discarded*
  (clean, costs the user a little input) or *credited* (continuous, but the edge lurches on exit).
  Discard, with a short ramp, is almost certainly right — the lurch is the thing being avoided.
- **Damping strip.** Gain below one across a region, so precision rises near interesting values
  without any value being forbidden. This is the control-to-display ratio becoming a function of
  position instead of a constant.

### Tog's menu bar was a zeroing strip all along

Tognazzini's Fitts's law argument for the Mac menu bar — that it is effectively a thousand miles
tall, because you can slam the pointer at the top of the screen and the edge catches you — describes
**a detent with an infinite escape threshold.** The mouse keeps moving; the cursor does not; the
excess delta is discarded. Overshoot is free, so the target's effective height is unbounded and
acquisition costs nothing.

Which means the most celebrated Fitts's law win in interface history is **not a property of the
display, it is a line in the pointer's transfer function.** It was always software, always a
parameter, and there was never a reason to have exactly four of them nailed to the physical borders.

> **The pointer transfer function is where Ted Selker did his life's work.** The TrackPoint is
> isometric rate control, so unlike a mouse *nothing* about its mapping is given by physics — the
> transfer function is the entire device. Selker's answer was two **plateaus**: a wide band of light
> pressure mapping to one exact slow predictable speed, and a wide band of harder pressure mapping to
> a fast speed held just below eye-tracking, because above that you lose the cursor.
>
> **A plateau is a detent one derivative up.** Both take a wide range of input, flatten it onto one
> output, and thereby convert motor noise into stability instead of error — Selker's makes a *speed*
> easy to hold, a friction strip makes a *position* easy to hold. And his two-plateau coarse/fine
> pair is the same shape as [eyeball-then-dial](RADIAL-DIMENSIONS.md#the-precision-pie-and-the-problem-it-was-built-for).
>
> The story, from Don's accounts: [TrackPoint transfer
> function](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-selker/sources/trackpoint-transfer-function.md)
> — including his father the material scientist designing the non-skid rubber, IBM refusing to ship
> until it measured as efficient as a mouse, and the bag of spare Joy Buttons he kept in the car.
The proof by regression is multi-monitor: the moment two displays share an edge, the wall evaporates
and the menu bar stops being infinite — a hardware accident deciding an interface property.

Generalize it and the whole family is one mechanism with two parameters:

| | Capture depth | Escape threshold | |
|---|---|---|---|
| **Screen edge** | unbounded, one-sided | ∞ | Tog's wall |
| **Groove** | unbounded along, narrow across | finite | slide freely, [pull off to leave](GROOVES-AND-SPIKES.md#a-groove-is-a-1-d-manifold-with-a-policy) |
| **Detent** | narrow | finite | catches a value, releases with effort |
| **Damping strip** | wide | n/a — gain, not capture | precision without prohibition |

So Don's generalization is exact: put a wall **anywhere**, make it as **deep** as you want, and —
unlike a physical edge, which has only one side — approach it **from any direction**, including from
both sides, which is what makes a groove a groove rather than a border.

And it only works under relative control. A clamp is by definition a discarded delta, so a system
that insists the object track the cursor absolutely cannot have walls at all — which is the nulling
argument arriving a third time, from the direction of Fitts's law.

**It already shipped, in PSIBER, in 1989.** Objects on the deck had tabs you dragged onto a stack
spike:

> It implements a mutant form of "Snap-dragging", that **constrains non-vertical movement when an
> object is snapped onto the stack, but allows you to pop it off by pulling it far enough away** or
> lifting it off the top. [Bier, Snap-dragging]

A zeroing strip on one axis plus an escape threshold, thirty-seven years ago, credited to Bier and
Stone's *Snap-Dragging* (SIGGRAPH 1986) — whose own contribution was already an indirection, since
gravity there acts on a **caret** and objects follow the caret rather than the cursor. Bier put a
layer between input and effect and spent it on gravity; the friction strip spends the same layer on
hysteresis, which is the version that does not eat nearby values.

The overlay highlighting has a shipped ancestor too, with a reason attached:

> …previewing and highlighting **in the overlay plane** (which was much faster to draw interactively
> than moving and resizing the live windows themselves).

Recruitment preview is therefore not a new cost — it is cheaper than the thing it replaces.

### The seam is the point

Once a transfer function exists, arbitrary **middleware** fits in it: momentum, springs, viscosity,
magnetism-with-escape, or a full physics simulation. That reframes the claim of this whole document.
Relative control is not merely a fix for a jump — **it is the seam where interaction middleware
becomes possible at all**, and absolute control has no seam, because position is just position.

Taken to its limit the cursor stops being a coordinate and becomes an object in a simulated world —
the multiplayer games where your cursor rides an inflatable raft drifting downstream, and steering
means negotiating with the current. Same seam, used maximally.

The **Precision Pie** is this same transfer function built as visible geometry — gain you can watch,
because it is the bend of a lever rather than a curve in a driver. Documented with the demo and
transcript in [Radial Dimensions](RADIAL-DIMENSIONS.md#the-precision-pie-and-the-problem-it-was-built-for).

*(Still needed from Don: the **virtual cursor** design for pie menus, and the title of the dynamic 
cursor game.)*

## Radius now means three things, and they must not collide

The radial dimension is the cluster's most reused resource, and this doc adds the third claim on it:

| Meaning | Where |
|---|---|
| **Precision** — arc length grows with radius, buying angular accuracy | [RESELECTION.md](RESELECTION.md) |
| **Appetite** — further out asks for more detail about the item | [PUMPING-UP-PIE-MENUS.md](PUMPING-UP-PIE-MENUS.md#distance-as-appetite) |
| **Scope** — further out applies the operation to more objects | this document |

They coexist partly because they belong to different kinds of menu: appetite suits a *navigational*
pie where the item is a place, scope suits an *operational* pie where the item is a verb with an
operand. Precision is free and compatible with both, being a property of the geometry rather than a
semantics assigned to it.

**But "one menu may not claim two" is too strong**, and the Precision Pie disproves it — it ships
leverage before the hinge and flexibility after, in one stroke, unambiguously. The real rule is
narrower: **radius has one meaning per level, and an anchor is where it may rebind.** Worked out in
[Radial Dimensions](RADIAL-DIMENSIONS.md), which is also how a resize gesture entering
`resize(edge, scope, delta)` stays legible across three dimensions.

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
