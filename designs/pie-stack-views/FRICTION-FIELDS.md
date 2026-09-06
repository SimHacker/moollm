# Friction Fields: the transfer function is a landscape, not a curve

**Thesis:** once relative control opens a seam between raw input and applied motion, what lives in
that seam is not a curve but a **field over the plane**. Walls, grooves, detents, damping strips and
drunken spaces are not five mechanisms — they are one function distinguished by *where it has
support* and *which derivative it acts on*. Everything in this document requires
[relative control](WINDOW-RESIZE-PIE.md#two-problems-usually-conflated); under absolute tracking none
of it can exist, because a clamp is a discarded delta and absolute tracking forbids discarding.

```
raw delta ──▶ [ F(position, delta, state) ] ──▶ applied delta
```

[Friction strips](WINDOW-RESIZE-PIE.md#friction-strips-snapping-that-never-gets-ahead-of-the-gesture)
introduced two members and the wall family; this document is the general object.

---

## Threshold is a function of direction

A wall's parameter is not one number but a **threshold per direction of travel**, and the interesting
members of the family are the asymmetric ones:

| Threshold in | Threshold out | Behaviour | Use |
|---|---|---|---|
| finite | finite, equal | **detent** — symmetric catch | round numbers, alignment |
| ∞ | — | **hard wall** — never passes | minimum width, screen edge, [Tog's menu bar](WINDOW-RESIZE-PIE.md#togs-menu-bar-was-a-zeroing-strip-all-along) |
| low | high | **trap** — easy to enter, costly to leave | capture into a groove; sticky guides |
| high | low | **guard rail** — costly to enter, free to leave | protect a region without forbidding it |
| finite | ∞ | **ratchet** — passes one way only, then never returns | monotonic commits; one-way doors |
| 0 | finite | **exit toll** — free to enter, effort to leave | modal regions you fall into and climb out of |

Two consequences worth naming. First, **the hard wall is not a separate construct**, it is the
infinite limit of a detent, which is why Tog's screen edge and a minimum window width turn out to be
the same object. Second, **a one-way wall is a diode**, and a diode plus stored energy is a pump —
which becomes a real hazard in the next section rather than a curiosity.

A one-way wall may be *impassable* in the blocked direction (a true diode) or merely *expensive*
(asymmetric thresholds). The second is almost always the better product: it never traps a user in a
state with no exit, and it degrades rather than refuses.

---

## Don's velocity credit: paying the debt as an impulse

The earlier friction-strip section offers two policies for the motion a wall consumes, and calls the
question settled. It was settled for the wrong reason. The two policies were:

- **discard** — clean, but the user's input is thrown away
- **credit as position** — conserves the input, but the edge *lurches* on release

Don's third policy dissolves the dilemma: **credit the consumed motion as velocity, not position.**
You exit the wall with an impulse, decaying at a chosen rate, whose integrated displacement equals
the distance you pushed through. Nothing is discarded and nothing jumps.

```
pushed through wall: d          exit with v₀, decaying over τ
                                ∫v dt = d      ⟹      v₀ = d/τ
```

The feel is the point, and Don names it exactly: **getting pumped up by an invisible spring.** You
compress it going in and it releases on the far side. Which is not a metaphor laid over the
mechanism — it *is* the mechanism, because a spring is the thing that stores displacement and returns
it as velocity.

**This puts the three policies at three derivative orders**, which is the same ladder the TrackPoint
plateau climbed when it turned out to be
[a detent one derivative up](WINDOW-RESIZE-PIE.md#togs-menu-bar-was-a-zeroing-strip-all-along):

| Policy | Domain | Input conserved? | Continuous? |
|---|---|---|---|
| discard | position | no | yes |
| credit as position | position | yes | **no** — step discontinuity |
| **credit as velocity** | velocity | yes | yes |

So the ladder, not the choice, was the finding. And it keeps going: credit as *acceleration* buys
jerk continuity, at the cost of a feel nobody will notice.

### Restitution is the knob

Once the wall returns stored displacement, the amount returned is obviously a parameter, and it is
the coefficient of restitution:

- **< 1 — lossy.** Some effort absorbed. Reads as a heavy, damped, expensive boundary.
- **= 1 — conservative.** Displacement exactly conserved. The honest default: the wall changed *when*
  your motion arrived, never *how much*.
- **> 1 — pumping.** The wall returns more than you put in. A catapult, and legitimately useful for
  launching a panel across a screen with a short shove.

Restitution above one needs an energy budget, because a **ratchet plus restitution above one is a
motor** — a cursor can be pumped without bound by a user who discovers the loop. Cap the returned
impulse, or make gain above one available only to walls that are not one-way.

### The decay rate is a feel parameter, and τ has a floor

`v₀ = d/τ` means a deep push with a short τ produces an enormous exit velocity. Very small τ
reconstructs exactly the lurch the policy exists to avoid, so τ has a practical floor around the
duration at which motion reads as motion rather than as a jump — a few frames, not one. The
principled version is to clamp `v₀` and let τ stretch, so deep pushes take longer to repay instead of
leaving faster.

---

## Thickness and threshold are independent

A wall's **threshold** is how much input it eats. Its **thickness** is how much space it occupies.
These are unrelated axes, and Don is right that thickness may be zero, one pixel, or anything:

- **zero thickness, finite threshold** — a pure boundary that costs effort to cross. A classic detent.
- **zero thickness, infinite threshold** — a clamp. A minimum width.
- **thick, zero threshold, gain < 1** — a damping strip. No prohibition, just precision.
- **thick, finite threshold** — a region you push into and then break out of, which is the case
  velocity credit was invented for, since there is real distance to repay.

Threshold accumulates in the *delta* domain, which is why zero thickness is not a degenerate case:
there is no requirement that consumed motion correspond to traversed space.

### Visual thickness is independent of both

Don's sharpest constraint: **visual thickness is independent of cursor-distance thickness.** A wall
that eats forty pixels of input may render as a two-pixel line.

This is not a liberty, it is forced. The moment gain is anything other than 1, input space and
display space have different metrics, so there is no faithful rendering of input distance in display
distance available to be drawn. Which resolves into a positive rule:

> **Render the state, not the geometry.** The useful thing to show is not how wide the wall is but
> **how far through it you are** — a filling indicator, a brightening edge, a compressing spring.
> Without that, the threshold is unmodellable: the user cannot tell an expensive wall from a broken
> interface, because both look like nothing happening.

This is the same discipline as
[naming the binding constraint](GROOVES-AND-SPIKES.md#sketchpad-class-power-and-the-sketchpad-class-failure)
and for the same reason. A system that silently refuses motion is indistinguishable from one that
crashed.

---

## Perlin noise: fields, and what makes them learnable

Don's last item generalizes the whole document. A **Perlin noise drunken cursor space** is a field
that perturbs the delta everywhere in a region — and once that exists, the walls above are revealed as
the degenerate cases:

| Support of the field | Object |
|---|---|
| a point | detent |
| a curve | wall, [groove](GROOVES-AND-SPIKES.md#a-groove-is-a-1-d-manifold-with-a-policy) |
| a band | damping strip |
| **an area** | **terrain** — viscosity, drift, drunkenness, texture |

So the mechanism was never "strips." It is a field, and strips are what a field looks like when you
only give it 1-D support.

**The determinism question decides everything about it**, and it is exactly ARK's
[literalism-versus-magic lesson](GROOVES-AND-SPIKES.md#cartoon-physics-and-arks-honest-lesson)
arriving in the motor channel:

- **Seeded and position-locked** — the noise is a fixed landscape. Rough ground in one corner of the
  screen, glassy smoothness in another. This is **learnable**: it can be mastered, rehearsed, and
  navigated by feel, exactly as real terrain is, and it gives regions a distinguishable character
  without labelling them.
- **Re-rolled per gesture, or time-varying** — this is drunkenness. Legitimate as a *depicted
  condition* (impairment, damage, a status effect, a cursor that has had a rough day) and never
  legitimate as ambience, because it destroys rehearsability: the user cannot build a model of a
  landscape that is not there twice.

The line is the same one the whole cluster keeps landing on. Deterministic perturbation is **terrain**
and belongs to the user. Nondeterministic perturbation is an **effect** imposed on the user, and needs
a diegetic reason.

A field also gives a
[reading cursor](../webtop/READING-CURSORS.md) somewhere to keep its personality in the motor channel
rather than only in its prose — a heavy cursor whose terrain is viscous, a jittery one whose ground is
rough. Cheap, since it is a seed and a gain.

---

## Honest costs

- **None of this is implemented.** It is a design with shipped ancestors (Tog's edge, the Sims
  placement tool, the Precision Pie, the TrackPoint plateaus), not a system with users.
- **Unmodellable without the state display.** Every construct here is invisible in principle; the
  filling indicator is not a polish item but a correctness requirement.
- **Composition is unspecified.** Two overlapping fields must combine somehow — sum the perturbations,
  or let the topmost win. Sum is probably right for gains and wrong for thresholds, and nothing here
  has established that.
- **Accessibility cuts against noise.** A drunken field is a motor-precision tax, so any noise
  gain needs to reach zero from a setting, and the state display must not depend on colour alone.
- **The taxonomy could be a trap.** Six named wall types is a vocabulary, and vocabularies invite
  building all six. The ones with receipts are the hard wall and the symmetric detent.

## Related

- [The Window Resize Pie](WINDOW-RESIZE-PIE.md) — friction strips, the wall family, the Sims
  placement tool's validity-driven regimes, and minimum sizes as walls
- [Grooves and Spikes](GROOVES-AND-SPIKES.md) — the geometry manager these fields live in; grooves as
  1-D manifolds with policies
- [Radial Dimensions](RADIAL-DIMENSIONS.md) — the Precision Pie as a transfer function built as
  visible geometry, and gain you can watch
- [TrackPoint transfer
  function](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-selker/sources/trackpoint-transfer-function.md)
  — Selker's plateaus, the historical case that a pointer's mapping is entirely a design artifact
