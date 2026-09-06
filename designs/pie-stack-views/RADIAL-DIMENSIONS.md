# Radial Dimensions: the hinge is a gear shift

**Thesis:** Radial distance is not one dimension with one meaning that other meanings must not
collide with — it is a **stack of dimensions, rebound at every anchor the user plants.** The
Precision Pie shipped this in NeWS: poke out to fix a coarse angle, and past that anchor the radius
stops meaning *leverage* and starts meaning *flexibility*, on a lever you can see bending. One
continuous stroke, two semantics, separated by a visible hinge.

Part of the **pie-stack-views** cluster ([README](README.md)). Prior claims on the radius:
[RESELECTION](RESELECTION.md) (precision), [PUMPING-UP](PUMPING-UP-PIE-MENUS.md#distance-as-appetite)
(appetite), [WINDOW-RESIZE-PIE](WINDOW-RESIZE-PIE.md#radius-as-scope-the-rings-are-hops-not-pixels)
(scope).

---

## The Precision Pie, and the problem it was built for

[**Precision Pie Demo**](https://www.youtube.com/watch?v=c0scs59va4c) — Don Hopkins, NeWS, research
under Mark Weiser and Ben Shneiderman.

The setup is the ordinary pie-menu leverage property, pushed until it breaks:

> …an experiment in exaggerating the extra precision that you get with distance. As you move out
> further from the center of a pie menu, normally the further you go from the center the more control
> you have over the angle. But if you want to input an exact number like an angle, you might want to
> get it down to a certain number, but **you run out of screen space before you get enough leverage**
> to change the number to what you want.

Leverage scales with radius, and the screen does not. Which makes plain radial leverage useless
exactly when you need it most — for the last few units of a precise value.

The fix is a hinge:

> …when you poke out it makes a **flexible lever** that the further out you go, the more flexible it
> becomes, and you have much finer control over the number. So as I move around, back in and out,
> I'll poke it into a different place and just come out further to get a lot of leverage and dial
> exactly the number I want… **and as you get nearer it gets less and less flexible.**

And the resulting two-phase working style, in the demonstrator's own words:

> …generally you'd kind of eyeball it and then get it exact — like 93, well there's 93, or 273,
> there's 273.

**Eyeball, then dial.** Coarse angle is snapshotted at the poke-out point; everything past the anchor
is deflection of a floppy hair rooted there, with flexibility increasing outward. Stiffness returns
on the way back in, so the whole thing is reversible without a mode.

## Why this matters more than a precision widget

The Precision Pie is the [damping strip](WINDOW-RESIZE-PIE.md#friction-strips-snapping-that-never-gets-ahead-of-the-gesture)
**implemented as visible geometry rather than as a number.** Position-dependent gain is normally an
invisible curve in a driver; here the gain *is* the bend, so you can see how much precision you
currently have by looking at how floppy the hair is. That is the property worth generalizing: a
transfer function you can watch.

And it quietly refutes an overreach in the resize-pie doc. That doc said radius's three meanings
"must not collide" and that a menu claiming two at once is a design error. **Too strong.** The
correct rule is narrower:

> **Radius has exactly one meaning per level. The anchor is where it may rebind.**

Ambiguity was only ever a problem *within* a level. The Precision Pie already ships two meanings in
one gesture — leverage before the hinge, flexibility after — and is not ambiguous for one second,
because the hinge is visible and the user planted it.

## Nesting: the stroke is an argument list

Once anchors rebind the radius, a nested pie tree can alternate dimensions by level: direction picks
the branch, radius means one thing until the next anchor, then another. What that produces is not a
menu selection but a **tuple entered in a single continuous stroke**:

```
flick NE ──● snapshot edge=NE
           │  radius → scope, fan preview shows recruited seams
           ●─ anchor at ring 2
              radius → displacement, relative, through friction strips
                 ⟹ resize(edge: NE, scope: 2, delta: +37)
```

Which lands directly on the [tree-navigation invariant](../webtop/TREE-NAVIGATION.md): every
operation is one named command reachable by keyboard, pie, and drag. The gesture is not *choosing* a
command, it is **constructing its argument list**, so the keyboard binding and the gesture are
provably the same call. If a pie stroke cannot be written down as a call with its arguments, the
gesture has state the command does not, and that is a bug rather than a flourish.

This is also [the Dasher pivot](PUMPING-UP-PIE-MENUS.md#the-dasher-pivot) with heterogeneous
dimensions — continuous nested selection with no commit event, except that each level steers a
different kind of quantity instead of all of them steering probability mass.

## Previewing selection and dimension at the same time

Don's question: what affords real-time in-world preview of *both* what you are selecting and what the
current radial dimension is doing? Three rules cover most of it.

**1. Every dimension gets its own visual verb.** If two dimensions both render as "the line gets
longer," the stroke is unreadable. They must differ in kind:

| Dimension | Visual verb | Reads as |
|---|---|---|
| leverage / coarse angle | **extension** of a stiff spoke | reach |
| fine adjustment | **bending** of a floppy hair — *shipped* | delicacy |
| scope | **fanning** — the spoke splits into one line per recruited object | breadth |
| appetite | **accretion** — detail grows around the center | depth |
| magnitude | **thickness** or a filling bar along the spoke | force |
| discrete steps | **notches** crossed, rings drawn where they are | counting |

Bending versus extension is the pair that matters most, for a reason the demo states outright:
**extension runs out of screen and bending does not.** So deep trees should alternate *toward*
bend-like verbs, and a level that needs a long pull should be near the root.

**2. The preview renders in the substrate the dimension acts on, not in the menu.** The menu shows
what you are steering; the *world* shows what will happen. Fine angle previews as the number at the
tip of the hair. Scope previews as highlighting on the recruited window edges. Displacement previews
as a ghost outline of the resulting layout. Appetite previews as the detail itself appearing. A menu
that renders its own consequences is a menu the user has to translate.

The [NeWS receipt](WINDOW-RESIZE-PIE.md#friction-strips-snapping-that-never-gets-ahead-of-the-gesture)
says this is cheap: previewing in the overlay plane was *faster* than moving the live windows.

**3. The anchor announces the rebinding.** The moment radius changes meaning, the anchor must say so
— a distinct mark per dimension, planted where the user poked out. Without that, level two is a mode
the user entered without being told, which is the failure the whole cluster exists to avoid.

## Honest costs

**Anchors are commits, and commits need undo.** Retracing inward must un-anchor, not just reduce the
value — otherwise a stroke accumulates state you can only escape by aborting. The Precision Pie gets
this right (stiffness returns on the way in); a nested version has to get it right at every level.

**Rehearsability degrades with depth.** Direction sequences are rehearsable because they are motor
memory. Radial *semantics* per level are not — you cannot feel that ring 2 means scope. Two levels is
probably the practical limit for eyes-free use, and beyond that the menu is a visual instrument
rather than a gesture.

**One shipped receipt, one demo, no user study.** The Precision Pie was demonstrated, not evaluated;
the nesting proposal has neither. The [tracking-hook channel](RESELECTION.md#tracking-hooks-the-candidate-channel)
is how it becomes measurable, and dwell timing is already instrumented in the OpenLaszlo and OLPC
implementations.

---

## Related

- [WINDOW-RESIZE-PIE.md](WINDOW-RESIZE-PIE.md) — the worked operational pie, friction strips, and the collision this document resolves
- [RESELECTION.md](RESELECTION.md) — reversibility as reselection; leverage as the base property
- [PUMPING-UP-PIE-MENUS.md](PUMPING-UP-PIE-MENUS.md) — appetite, and the Dasher pivot
- [../webtop/TREE-NAVIGATION.md](../webtop/TREE-NAVIGATION.md) — one named command across keyboard, pie, and drag
