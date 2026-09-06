# Grooves and Spikes: constraint objects you draw on the desktop

**Thesis:** This is a **geometry manager, not a window manager** — windows, tabs, pie menus, and
glyphs are all made of geometry, so one constraint vocabulary reaches all of them and the window
frame stops being a boundary between two incompatible layout systems. A **groove** is a
one-dimensional subspace you draw on the desktop, collapsing three normally-separate subsystems —
**docking target, layout container, and constraint** — into one object, because all three are the
same question about a 1-D manifold. The **spike** is the ordered special case, and PSIBER shipped it
in 1989. The bridge from the resize pie is that an **inferred** relationship can be **promoted** to a
declared one, so nobody has to build a constraint network from scratch to end up with one.

Part of the **pie-stack-views** cluster ([README](README.md)). The gesture that discovers
relationships: [WINDOW-RESIZE-PIE](WINDOW-RESIZE-PIE.md). The escape behavior:
[friction strips](WINDOW-RESIZE-PIE.md#friction-strips-snapping-that-never-gets-ahead-of-the-gesture).

---

## It is a geometry manager, not a window manager

That is the reframe, and it is not a rename. **The window frame is currently a hard boundary between
two incompatible geometry systems.** Inside a window, a geometry manager negotiates — Tk's `pack`,
`grid`, `place`, or a widget tree's layout pass, where an element does not choose its own position
and a manager arbitrates. Outside the window, a *window manager* solves the same problem with an
entirely different vocabulary, no compositional layout, and no constraints at all.

Nothing about geometry justifies that boundary. It exists because of the client/server split and the
window-manager protocol, not because a window's position is a different kind of question from a
button's. Delete the boundary and one manager handles both, which is the whole content of the
reframe — and the reason the resize pie, grooves, spikes, tabs, and menu layout belong in one
cluster instead of five places.

**Windows, tabs, pie menus, glyphs, and grooves are all made of geometry**, so the same vocabulary
reaches all of them. One consequence lands immediately and retroactively:

> **A tab was always a constraint.** NeWS tabs draggable to any position along any edge are an object
> constrained to the window's perimeter — a closed 1-D manifold, which is to say **a groove that was
> already there.** The feature shipped in 1990 without the vocabulary that explains it.

The test of whether the claim is real is self-application: **the geometry manager's own interface
must be laid out by the geometry manager.** Its grooves, its menus, its handles, all ordinary
geometry subject to the same constraints. If any of it needs a privileged layer, everything is
geometry *except* the part that matters, and PSIBER — where the debugger's own views were
manipulable objects — is the standing proof that this is achievable rather than aspirational.

### Uniform substrate, differentiated policy

The failure mode of "everything is one thing" has a name and a body of experience: **Morphic**.
Everything is a Morph, uniformly composable, directly manipulable, submorphs all the way down — and
the cost was that everything became *possible* while nothing remained *conventional*. Structure ends
up accidental, because a system that permits any composition offers no reason to prefer one.

So geometry is the substrate, not the semantics. A menu is transient, grabs input, and dies on
release; a window persists, holds focus, and participates in z-order. Those differences are real and
must live somewhere — in the **type**, which carries policy, while geometry stays uniform underneath.
Uniformity buys the shared constraint vocabulary; typing keeps the desktop from becoming a pile of
interchangeable rectangles.

### The performance objection is already answered

Constraint-solving the whole desktop instead of one widget tree sounds expensive, and Sutherland's
relaxation on a TX-2 was. It is settled now: **Cassowary** — Badros and Borning's incremental
solver — is what Apple's Auto Layout runs on, solving view geometry constraints continuously on a
billion phones. The scale in question here is a desktop with tens of constrained objects, which is
smaller than what ships in a single app.

---

## The spike, which already exists

PSIBER's deck put the PostScript operand stack on screen as a physical object — a spike, the
short-order cook's order spindle — with objects' tabs pinned onto it:

> There is a text window onto a NeWS process… PostScript is a stack based language, so the window has
> a **spike sticking up out of it**, representing the process's operand stack. Objects on the
> process's stack are displayed in windows with their tabs pinned on the spike… You can perform
> direct stack manipulation, **pushing it onto stack by dragging its tab onto the spike, and changing
> its place on the stack by dragging it up and down the spike.**

The spike is not a metaphor for the stack, it *is* the stack — pushing is a drag, reordering is a
drag, and popping is pulling far enough away. Which means the interaction and the semantics were
never separate things that had to be kept in sync.

## A groove is a 1-D manifold with a policy

Generalize the spike by dropping the ordering semantics and allowing any orientation — vertical,
horizontal, diagonal, or a curve. What you get answers three normally-separate questions at once:

| Question | Answer for a groove |
|---|---|
| **Docking** — where does a dropped thing go? | projection onto the manifold |
| **Layout** — how do many things arrange? | distribution along it, per policy |
| **Constraint** — what may still move? | stay on it; one degree of freedom remains |

Three subsystems in most toolkits, one object here, and the unification is not a trick — they are the
same geometry asked three ways. The **policy** is what varies: free sliding, even distribution,
pack-from-one-end, gravity-settled, ordered-by-index. A spike is the groove whose policy is *ordered,
index-carrying, vertical*.

And a groove is exactly where a container-placement negotiation belongs — the contained object, the
groove, and the caller of `place` each get a say, which is the OpenLaszlo placement protocol arriving
in a window manager rather than a widget tree.

**Grooves are where friction strips live.** Sliding along a groove is free; leaving one costs an
escape threshold. That is the PSIBER behavior exactly — *constrain non-vertical movement while
snapped, pop off by pulling far enough away* — and it means the whole
[hysteresis discipline](WINDOW-RESIZE-PIE.md#friction-strips-snapping-that-never-gets-ahead-of-the-gesture)
transfers with no new machinery.

It also makes a groove **a screen edge you can put anywhere.** Tognazzini's thousand-mile-tall menu
bar is a clamp in the pointer's transfer function with an infinite escape threshold; a groove is the
same mechanism, two-sided and escapable —
[the parameterized family](WINDOW-RESIZE-PIE.md#togs-menu-bar-was-a-zeroing-strip-all-along). So
drawing a groove is drawing a Fitts's law wall, and every object docked to it inherits an infinitely
deep target for free. That is the strongest practical argument for grooves over ordinary snapping:
they do not merely organize, they make things **easier to hit**.

## Promotion: inference is a draft of a constraint

The resize pie
[infers adjacency per gesture and throws it away](WINDOW-RESIZE-PIE.md#inferred-per-gesture-never-enforced).
Grooves are declared and persist. Those look opposed and are not — they are two ends of one pipeline,
and the connection between them is the most useful idea here:

> **A gesture's inferred relationship is a draft constraint. If you liked it, pin it.**

Which solves the discoverability problem that has killed every general constraint UI: nobody wants to
sit down and build a constraint network, but everybody will keep one they made by accident and
liked. You resize a seam, the system shows you the adjacency it inferred, and one command turns that
momentary interpretation into a real groove. Play, then lift — the same escalation the rest of this
system uses, applied to layout.

Demotion has to be equally cheap, or the desktop silts up with constraints nobody remembers agreeing
to.

## Sketchpad-class power, and the Sketchpad-class failure

Full construction on tabs, pins, corners, edges, and centers — coincidence, alignment, distance,
midpoint, parallel, perpendicular — is Sutherland's Sketchpad (1963) with windows as the geometry,
and Jackiw's Geometer's Sketchpad is the proof that ordinary people will build these networks when
construction *is* the authoring act. There is no reason window layout should be less expressive than
a high-school geometry tool.

But the power arrives with its failure attached, and it is worth naming before building:
**over-constraint is invisible.** You build a network, it quietly becomes rigid, you drag something,
nothing moves, and the system tells you nothing. Two requirements follow, both cheap:

- **Show residual degrees of freedom.** A window on a groove has one; pinned at a corner it has none.
  Whatever visual verb the [radial dimensions](RADIAL-DIMENSIONS.md#previewing-selection-and-dimension-at-the-same-time)
  rules assign, remaining freedom must be visible *before* the drag, not discovered by its absence.
- **Name the binding constraint when a drag is refused.** "This cannot move because it is pinned to
  the left edge of B" is a debuggable answer; a window that simply does not budge is not. Same
  discipline as [`whence`](../MOOFS-NAMESPACE.md#proc-introspection-with-no-new-verbs) — the system
  must be able to explain a resolution it performed.

This is [Declare](../webtop/temkin/README.md#declare-sql-for-interfaces) with a desktop as the
domain: state the invariant, let the solver keep it true, and require the solver to account for
itself.

## Cartoon physics, and ARK's honest lesson

Gravity settling things into grooves, a flick that docks, momentum that carries a tab to the spike —
convenient, and the qualifier *cartoon* is doing real work. The reference case is Randall Smith's
**Alternate Reality Kit** at Xerox PARC, where interface elements were literal physical objects with
mass and momentum. Smith's own retrospective is titled for the problem he found:
*"Experiences with the Alternate Reality Kit: An Example of the Tension Between Literalism and
Magic"* (CHI+GI 1987). Literalism cost usability. Making a thing physical made some operations
harder, not easier, because physics is indifferent to what you meant.

So the rule is **physics where it buys convenience, magic where it does not**, and one hard
requirement separates a tool from a toy:

> **Determinism.** The same flick twice must settle in the same place. Physics here is a layout
> heuristic wearing an animation, not a simulation — the animation exists to show you *why* the thing
> ended up where it did, and if the answer differs run to run, it was never an explanation.

Everything else follows from that. Momentum yes, because it makes a flick reach. Bouncing no, unless
the resting position is unaffected. Randomness never.

*(Smith went on to co-create Self with Ungar, which is the same instinct — directness and uniformity
— applied to the object model instead of the desktop.
See [KORZ-LLM-EVALS](../KORZ-LLM-EVALS.md).)*

## Honest costs

**Drawn constraints are invisible clutter waiting to happen.** A groove is a line on the desktop that
does something; ten of them are a diagram nobody can read. Grooves need the same treatment as any
other view — hideable, nameable, and grouped into saved arrangements, which is what the
[public square](PUMPING-UP-PIE-MENUS.md#the-public-square) already does for menu configurations.

**Constraint networks outlive the intent that produced them.** A layout rigged for one task follows
you into the next one, and the promotion path above makes that *more* likely by making constraints
cheap to create. Expiry, or at least a listing of what is constraining the current desktop, is not
optional.

**None of this is implemented.** The spike shipped in PSIBER in 1989; grooves, promotion, and the
construction vocabulary are design.

---

## Related

- [WINDOW-RESIZE-PIE.md](WINDOW-RESIZE-PIE.md) — the gesture that infers relationships, and friction strips
- [RADIAL-DIMENSIONS.md](RADIAL-DIMENSIONS.md) — visual verbs, and previewing in the substrate
- [PERIPHERAL-VIEWS.md](PERIPHERAL-VIEWS.md) — PSIBER in depth: the deck, tabs, and view characteristics
- [SPARSE-VIEW-OVERLAYS.md](SPARSE-VIEW-OVERLAYS.md) — constraint inheritance and the escalating guardrail spectrum
- [../webtop/temkin/README.md](../webtop/temkin/README.md) — Declare: constraints that stay true
