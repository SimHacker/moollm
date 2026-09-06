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

One structural caveat on the thesis, established later and worth knowing up front: a field is owned by
the *space*, but the seam can also be filled by an object that owns its own mapping — a
[**vehicle**](#the-vehicle-owns-the-mapping-so-input-is-routed-rather-than-reduced). Vehicles nest
inside fields, and pie menus turn out to be vehicles.

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

A **ratchet plus restitution above one is a motor**, and a cursor can then be pumped without bound by
a user who finds the loop. The obvious fix is an energy budget — cap the returned impulse, or allow
gain above one only on walls that are not one-way — and it is the wrong fix, because it treats speed
as the danger.

Don's kinetic-navigation work says otherwise. MediaGraph's
[aimable, interruptible cannon](PIE-MENU-MEMORY-PALACES.md#kinetic-navigation-the-aimable-interruptible-cannon)
launches the view ballistically and lets the user **grab, brake, pan or throw it mid-flight** without a
mode switch. Under that contract unbounded velocity is not a loss of control, it is fast travel:

> **The invariant is not bounded energy, it is continuous grabbability.** A runaway is only a runaway
> if it cannot be caught. Cap unrecoverability, not speed.

Which also settles when gain above one is legitimate. A user pumping *themselves* is playing — they
supplied the energy and can stop any time. A field pumping the user *unprompted*, with no handhold, is
the [dark-pattern case](#the-same-mechanism-weaponized) wearing physics. Same coefficient, and the
difference is who initiated it and who can end it.

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
- **Derived from world state** — not noise at all, but a field computed from the model, which changes
  when the model changes. Better than seeded noise rather than worse, because it is both learnable
  *and* informative: the terrain updates because the world changed, not because a seed did. This is
  where the Sims placement tool lives, and it gets its own section
  [below](#the-field-belongs-to-the-pair-not-the-space).
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

## The field belongs to the pair, not the space

Don's observation that closes the loop: in the Sims,
[placing indoor-only and outdoor-only objects produces **opposite** regimes over the same lot](WINDOW-RESIZE-PIE.md#the-sims-placement-tool-the-transfer-function-renders-the-constraint-model).
A rug snaps inside the house and goes smooth-and-red in the yard. A tree does the exact reverse. Same
geometry, inverted field.

Which means the field is not a property of the space at all. **It is a property of the verb and its
operand** — `F(position, delta, held_object)`. The lot has no friction landscape; the lot-plus-a-rug
has one, and the lot-plus-a-tree has its complement.

Two things follow, and the second is the good one.

**The wall is a groove in validity space.** Because indoor and outdoor are complements, one exterior
wall serves both regimes, approached from opposite sides depending on what you are carrying. That is
[the two-sidedness that makes a groove a groove rather than a border](WINDOW-RESIZE-PIE.md#togs-menu-bar-was-a-zeroing-strip-all-along)
arriving from the semantic direction instead of the geometric one — the same structure, derived twice
from unrelated starting points.

**The dimensionality of the valid set picks the interaction primitive.** Every placeable object
carries a predicate, and the solution set of that predicate has a dimension:

| Valid set | Example | Interaction that falls out |
|---|---|---|
| 2-D region | rug on a floor | snap lattice in two axes |
| **1-D curve** | picture on a wall | **a groove** — slide along it |
| 0-D points | object that fits one slot | **a detent** — a single target |
| empty | tree indoors | all smooth, all red |

So grooves and detents are not separate designs to be authored. They are **what a validity predicate
looks like when its solution set is low-dimensional** — which retro-justifies the whole groove
vocabulary and adds a third origin for constraints alongside
[inference and declaration](GROOVES-AND-SPIKES.md#promotion-inference-is-a-draft-of-a-constraint):
**derivation**. Hanging a painting slides along a groove nobody drew.

And it runs backwards as information. Since the snapping regime traces the valid region, dragging a
rug around **reveals the floor plan through the motor channel**, and dragging a tree reveals its
negative — the yard. You feel out the building's topology using the held object as a probe.

The budget: the predicate must be evaluable at input rate. The Sims could afford it because the checks
were cheap grid lookups. The general answer is to evaluate the predicate over the visible region once
at drag start and whenever the world changes, giving a mask — which is cheap, and is also why a
*semantic* field costs no more per frame than a geometric one.

## The ocean: tacking, and why friction is the power source

A region of the plane is **ocean**, and entering it turns the cursor into a **boat**: angle the sail,
hoist or reef it, and there is a **wind** with a direction. If the wind blows from where you are going,
you cannot point at your destination and arrive. You must **tack.**

This section was drafted as the maximal case of a field and is better read as the first instance of a
different thing — a **vehicle**, which owns its own mapping. That generalization is
[below](#the-vehicle-owns-the-mapping-so-input-is-routed-rather-than-reduced); the boat's specifics
here stand either way.

This is the case that uses the `state` term the opening signature declares and nothing else in this
document needs. A wall reads position; a damping strip reads position; a validity field reads the held
object. A boat carries **heading, sail trim, sail area and momentum between frames**, and the wind is
a field it converts rather than merely suffers. The cursor stops being a point that gets perturbed and
becomes a **dynamical system with its own configuration space**.

### Tacking is a nonholonomic constraint, and that is a new kind of restriction

Sailing upwind is impossible; sailing *to* a point upwind is easy. The no-go zone forbids a set of
**instantaneous directions** while leaving the set of **reachable positions** total — which is
precisely a nonholonomic constraint, the same structure as parallel parking a car. You can get
anywhere. You cannot get there directly.

That is a third axis of restriction, and the two the document already had do not cover it:

| Restricts | Constructs |
|---|---|
| where you may **be** | walls, minimum sizes, validity fields |
| how **fast** you get there | gain, damping strips, plateaus |
| **which way you may move right now** | **tacking, and nonholonomic fields generally** |

Note what it costs the user: **nothing is forbidden and nothing is slowed.** Only the path is
constrained. Which makes it the most humane restriction in the whole taxonomy — it never says *no*, it
says *not that way, not yet* — and it is the only one that makes the route itself into content.

### The wind that opposes you is the wind that moves you

The cluster already cites the multiplayer games where your cursor rests on an inflatable raft drifting
downstream. The raft is **passive**: the current carries you and you negotiate with it. The boat is
**active**: you extract work from the wind by angling against it, which promotes the field from an
obstacle to a **resource**.

And it is the case that proves the document's thesis as mechanics rather than as rhetoric. A sail
generates drive from the pressure difference across it, held against a keel's lateral resistance —
remove the resistance and you do not go faster, you go **sideways**. A frictionless ocean is
unsailable. So:

> **Friction is not the cost of manipulation. It is the enabling condition.** The wall you push
> against is what lets you push at all.

Which is Bogost's *Play Anything* argument about the pleasure of limits, arriving in the motor channel
with a physical proof attached instead of an appeal to taste.

### The controls are the two dimensions the pies already have

Don's "turn around and hoist and lower by moving the mouse around somehow appropriate" resolves into
the cluster's existing vocabulary, with no new input model:

- **angle** → sail trim. Direction selects, exactly as in a pie.
- **radius** → sail area. Hoist and reef, which is
  [distance as appetite](PUMPING-UP-PIE-MENUS.md#distance-as-appetite) meaning literal appetite for
  wind.

Reefing in heavy weather is therefore **the user choosing a damping strip** — less input authority in
exchange for more control — which is the one case in this document where the gain knob belongs to the
user rather than to the designer. Worth noticing that this is the honest version of every "sensitivity"
slider ever shipped.

The eBike Safari case is the same structure with the metaphor removed, since a bicycle is
nonholonomic, headwinds are literal, and hills are a potential field you climb or spend. See
[the path grammar](../webtop/EBIKE-PATH-GRAMMAR.md).

### Honest costs, which are steep

- **Tacking must be taught.** A user who does not know that upwind requires tacking experiences a
  broken interface, not a constraint. So the no-go zone and the wind need a **telltale** — which
  promotes *render the state, not the geometry* from a calibration aid to a comprehension requirement.
- **It is a toy unless the journey is the content.** Sailing to reach a menu item is charming once and
  intolerable on the hundredth repetition. This belongs where traversal is what the user came for — a
  map, a route, a corpus being explored — and nowhere near a control panel.
- **The wind must be deterministic** — authored, seeded, or modelled — or it is the drunkenness case
  with extra steps. Stable wind makes routes learnable, which sailors call local knowledge and this
  document calls terrain.
- **Motor memory does not survive it.** A gesture whose path depends on carried state cannot be
  rehearsed the way a pie stroke can, which forfeits the property the rest of the cluster is built to
  protect.

## The vehicle owns the mapping, so input is routed rather than reduced

Don's correction, which demotes the section above from *maximal case* to *first instance*. While you
are on the raft, your input is not attenuated and not discarded — **it is routed to the raft**, which
applies its own algorithm mapping cursor motion into a raft-in-stream simulation. The sailboat is not
a bigger version of that. It is a sibling: another vehicle, another mapping, same architecture. Any
vehicle can carry its own motion-to-dynamics parameterization.

This kills the question of whether the drift is gain zero or reduced gain. Both answers presuppose
that your input is competing with the current for control of *your position*, and it is not. Your
authority is **mediated**: total over the paddle, nil over the water.

| | Field | Vehicle |
|---|---|---|
| Owner of the mapping | the space, or the verb-and-operand pair | the object you are riding |
| Shape | `F(position, delta, state)` | `vehicle.map(delta)` → controls, then `vehicle.step()` |
| Your authority | direct over position, modulated | indirect — over the vehicle's controls |
| Composition | fields sum | vehicles nest *inside* fields |

```
input ──▶ vehicle.map ──▶ controls ──▶ vehicle.step (inside the field) ──▶ your position
```

Three stages, and only the first belongs to you. The field never disappears — the stream still acts,
but it acts on the raft, not on you.

### This is the Sims object model, one level in

A Sim does not know how to use a toilet; the toilet knows, and supplies the behaviour for the duration
of the interaction. A vehicle is that pattern applied to the **cursor**: while you are aboard, the
object supplies your control code. So `vehicle` is a prototype and `raft` and `sailboat` are children
overriding one method, which is the plural-typed-container discipline this repo already runs on —
motion mapping as polymorphic dispatch on the thing you are standing in.

And the dispatch is **two-sided**. Don's cursors-as-limbs proposal types the *cursor* by the surface it
is working on; a vehicle types the mapping from the other end. The general form takes both, which makes
the mapping a multimethod on `(cursor, vehicle)` — the same shape as
[the field belonging to the verb-and-operand pair](#the-field-belongs-to-the-pair-not-the-space),
reached this time from the object direction rather than the semantic one. Third independent derivation
of the same structure in this document.

### The pie menu was a vehicle the whole time

An open pie menu captures input and supplies its own interpretation of motion: angle selects, radius
sets a parameter. The
[Precision Pie](RADIAL-DIMENSIONS.md#the-precision-pie-and-the-problem-it-was-built-for) supplies a
stranger one — poke out to snapshot a direction, then work a hinged fine adjustment anchored where you
poked. Nobody would call either a vehicle, but structurally they are identical to the raft: transient,
input-capturing objects that own the map from motion to meaning. **Popping a pie and boarding a raft
are the same operation.** This cluster has been designing vehicles and calling them menus.

### Boarding is a mode, and an honest one

Tesler's objection applies with full force: the same wiggle means different things aboard and ashore,
which is the definition of a mode. It survives for the reason the Sims red tint survives — the mode is
**an object you can see yourself inside of**, spatially located, entered deliberately, with a visible
exit. The dishonest version of a vehicle is one with no depiction, which is just an input handler that
changed behind your back.

### What it costs

- **Every vehicle is a control scheme to learn.** The mitigation is the cluster's standing discipline:
  the vehicle must *display* its mapping. A sail shows its trim; a paddle shows its stroke. Visible
  mechanism, as in the Precision Pie's lever.
- **Nulling returns at full strength.** Aboard, your drawn position may not track your hand at all.
  Either show the true pointer or concede that acquisition is off the table while riding. Cursor Camp
  concedes it, correctly, because nothing there needs aiming at — a menu does not get that exemption.
- **The handoff needs continuity.** Boarding and leaving should carry velocity across, or each
  transition is a lurch. Exactly the argument from
  [velocity credit](#dons-velocity-credit-paying-the-debt-as-an-impulse), applied to a rebinding rather
  than a wall.
- **Motion-only control is an accessibility dead end.** A vehicle's controls must also exist as
  discrete commands, or riding is mouse-users-only.

### The vehicle's dynamics fix the alphabet of the gesture grammar

The eBike Safari consequence, and the reason this is not only a screen concern. Real vehicles have
mappings you cannot edit. A walker can self-cross inside a metre; a bicycle needs several and must lean
to do it; a car cannot make the tight roundabout figure at all. So the set of
[gestures a path can express](../webtop/EBIKE-PATH-GRAMMAR.md) is a function of the vehicle, and the
same route ridden, walked and driven yields three different expressible vocabularies. The grammar does
not get to choose its own alphabet — the dynamics choose it.

### The testable version of the Cursor Camp question

Which supersedes the one asked earlier: if input is routed to the raft rather than dropped, then
wiggling while aboard should produce **some** raft response — rocking, a heading change, a wake —
rather than nothing at all. Nothing at all means the input really is discarded and the raft is
scenery. Any response means the raft is a vehicle in this sense.

## Where the seam is in a browser: warping was the lurch all along

Don's practical payoff, and it retires a workaround that has been load-bearing since NeWS. **The pie
menu edge problem:** pop a menu near a screen or window edge and some slices land outside, so they
cannot be selected. The classic fix is to **warp the pointer** — `XWarpPointer`, `SetCursorPos` —
teleporting the cursor inward far enough that the menu fits.

Don stated the problem and its limit on his own pie-menu retrospective thread, in the same breath as
the touch case:

> With a mouse, you can do things like "warping" the mouse pointer to a new location when the user
> tries to click up a pie menu near the screen edge, but **there's no way to forcefully push the
> user's finger towards the center of the screen.**
>
> — Don Hopkins, [HN 17106103](https://news.ycombinator.com/item?id=17106103), 2018-05-19, on
> *Pie Menus: A 30-Year Retrospective*

**Warping is absolute tracking's version of a friction field**, and specifically it is the bad
version: a one-shot position step, which is precisely the
[credit-as-position policy](#dons-velocity-credit-paying-the-debt-as-an-impulse) whose defining defect
is that it lurches. That is not a coincidence — it is the same fact twice. When you do not own the
mapping from hand to pointer, the *only* way to change the relationship between them is to teleport
one of them. Warping is what a transfer function looks like when you are not allowed to have one.

Browsers provide no warp at all, which sounds like a regression and is not. They provide
**Pointer Lock**: `requestPointerLock()` hides the system cursor and delivers `movementX`/`movementY`
— the raw delta stream, which is exactly the left-hand side of `F`. You draw your own **virtual
cursor** and integrate the deltas yourself.

So the edge problem is not solved, it is **dissolved.** There is no system cursor position left to be
trapped against an edge; the virtual cursor lives in a coordinate space you own, and that space can
be clamped, wrapped, offset, or allowed to run past the viewport while the menu stays inside it.
Nothing needs teleporting because nothing was tethered.

And the same API is what makes every construct in this document implementable on the web, since all
of them are `applied = F(raw)` and Pointer Lock is the only browser API that hands over `raw`.

**One correctness requirement, easy to miss.** Request `{ unadjustedMovement: true }`. Without it the
OS pointer-acceleration curve has already been applied to the deltas, so your field composes *on top
of* an unknown transfer function — two in series, and every threshold in this document silently
becomes a function of the user's mouse settings. Raw deltas are not an optimization here, they are the
difference between a designed field and an undefined one.

**Multiple cursors fall out for free.** Once you are integrating a delta stream, integrating several
is not a new capability, and this supplies exactly the abstraction that
[Selker's two-TrackPoint prototype could not get from OS/2](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-selker/sources/trackpoint-transfer-function.md)
— the hardware existed, the pointer model did not. Under pointer lock **you are the OS for pointers**,
so the absent abstraction can simply be supplied, which is also what the
[reading cursors](../webtop/READING-CURSORS.md) design needs underneath it.

### The shipped receipt: Cursor Camp

**[Cursor Camp](https://neal.fun/cursor-camp/)** by **Neal Agarwal** (neal.fun, May 2026;
[HN 47949939](https://news.ycombinator.com/item?id=47949939), 1215 points, 195 comments) is this
document's thesis running in production for a mass audience. You *are* your cursor, in a shared camp
world with everyone else's cursors, each flagged by country. No text chat — cursor motion is the
entire social channel.

The two details that make it a receipt rather than an example, both from the top HN comment:

> I particularly like the points where **the mouse control is taken away from you**, i.e. when you
> float downstream, or when you go down a slide. It's also particularly genius how the mouse can
> **'teleport' around the screen** (i.e. when you go into a door and come out somewhere else).

"Control taken away" is how it reads from outside, and the mechanism is
[a vehicle](#the-vehicle-owns-the-mapping-so-input-is-routed-rather-than-reduced): input is routed to
the raft, which maps it into a raft-in-stream simulation. Middleware in the seam, shipped and enjoyed
rather than merely proposed. And teleporting through a door is **warping**, the thing browsers do not offer, which
proves the cursor is virtual: the real one is hidden and the game draws its own, because a drawn
cursor can be moved anywhere and a system cursor cannot.

**Whether it uses Pointer Lock, I could not verify** — Cloudflare blocks scripted fetches of the
bundle, and Neal Agarwal does not publish source (his stack is React, Node and MongoDB on Netlify, per
his [Uses This interview](https://usesthis.com/interviews/neal.agarwal/), and none of neal.fun is open
source, so **there is no repo to read**). Plain `mousemove` with the real cursor hidden would explain
everything observed. If that is what it does, then the drawn cursor *diverges* from the physical
pointer during the drift — which is nulling, and is fine here precisely because there is no acquisition
task. Nobody is aiming at a 4-pixel target while riding the raft. A menu system does not get that
exemption, which is the case for Pointer Lock in the paragraphs above.

The precedent it names in its own thread is older and still online: **cursordanceparty.com**, built
around 2011. And the social reading is the one this cluster keeps arriving at — the PC Gamer writeup
describes wiggling a cursor in time to music and a stranger in India copying it, which is
[communitas](PIE-MENU-MEMORY-PALACES.md#the-graph-is-a-liminal-space) with no vocabulary but position
and motion.

*Two disambiguations, since the name collides: the Reddit/Devvit "Cursor Camp" is a different project
by someone else, and spunky.games is an SEO aggregator page, not the game. Also worth knowing —
[Sam Arbesman](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/sam-arbesman/README.md)
interviewed Agarwal on The Orthogonal Bet in August 2025, which is a warm path if one is ever wanted.*

### What it costs, honestly

- **Latency.** A hardware cursor is drawn by the compositor and arrives almost immediately; a virtual
  cursor waits for your animation frame. This is the real reason virtual cursors feel worse than
  system ones, it is perceptible, and it is not fixable from JavaScript. Every field in this document
  is being paid for in milliseconds of cursor lag.
- **Escape is not yours.** Pointer lock requires a user gesture to enter and surrenders `Esc` to exit,
  so a menu system cannot own that key or that gesture.
- **Accessibility.** Hiding the system cursor breaks assistive technology that tracks it. There must be
  an unlocked fallback mode in which the fields degrade to no-ops rather than to nonsense — which is
  survivable precisely because the field is a *transformation*, and the identity transformation is a
  valid member of the family.
- **Touch has neither warp nor lock.** A finger cannot be pushed, so the edge problem is *real* on
  touch rather than dissolved, and pie menus there need a layout answer instead of a pointer answer.
  The only honest alternative is hardware: Iwata's movable-touchscreen haptic interface, which
  supplies reaction force by moving the screen under stationary fingers — the same
  [heavy-handed direction](https://www.youtube.com/watch?v=YCZPmj7NtSQ) Don pointed at in the same
  comment.
- **Gesture libraries assume a button is down.** Don's note on hammer.js: pie menus must track while
  the button is *up*, which touch-first gesture frameworks did not support, forcing a hack. Anything
  built on a gesture library inherits its model of when tracking is allowed to happen.

## The procedural rhetoric of direct manipulation

Don's frame, and it is the right name for everything above. Ian Bogost's **procedural rhetoric**
(*Persuasive Games*, MIT Press, 2007) holds that computational media make arguments through
*processes* — the unit of expression is the rule, and a system persuades by modelling how something
works and letting you inhabit the model. Bogost's own description of where it came from is
[an unholy blend of Will Wright and Aristotle](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ian-bogost/README.md),
which is the correct ancestry for this cluster too.

Direct manipulation's transfer function is exactly that, one derivative down: **arguments delivered
in the motor channel, felt rather than read.**

The asymmetric thresholds turn out to be **deontic operators** — the modalities of permission and
obligation, expressed as thresholds instead of prose:

| Construct | The claim it makes |
|---|---|
| symmetric detent | *this value is notable* |
| guard rail | *permitted, but discouraged* |
| trap | *you probably want to stay* |
| ratchet | *this is irreversible — decide now* |
| hard wall | *forbidden* |
| restitution < 1 | *this boundary is expensive* |
| restitution > 1 | *this boundary wants you through* |
| **velocity credit** | ***your effort was not wasted*** |

That last one is worth dwelling on: repaying consumed motion as an impulse is a claim about the user's
labour, made in the velocity domain. No affordance, no message, no dialog — you push, and the system
gives it back. Which is also the humane version of the
[warning nobody asked for](../../skills/no-ai-moralizing/GLANCE.yml): a guard rail does not lecture,
it charges. Let them through and make it cost something.

**The referent is present, which makes this rhetoric checkable.** Bogost's cases argue about systems
you cannot inspect — agribusiness, municipal debt — so the model's fidelity has to be taken on faith.
A placement field argues about *the artifact on screen*. If the friction claims a wall is there and
you can see no wall, the argument is falsified on the spot. Direct manipulation is therefore the rare
case of procedural rhetoric with a **verifiable referent**, which is the structural reason it can be
honest at all.

### The same mechanism, weaponized

Bogost's own warning applies: rhetoric persuades, and persuasion is manipulable. Every construct here
inverts cleanly into a dark pattern, and the code is identical.

The original sin was already named at the top of the friction-strip section — position-based capture
*quietly decides that your intent was the round number*. That is a rhetorical claim, and a false one:
the interface asserts an intent you did not have. Scale it up and you get a damping strip on
*unsubscribe* and gain above one on *buy*, which is the identical machinery pointed at the vendor.

So the legitimacy test is not about the mechanism, since the mechanism is neutral:

> **Does the field model the world, or the interest of whoever shipped it?** The Sims wall resists
> because the wall is there. A cancellation flow resists because churn is expensive. Same construct,
> opposite ethics.

That test is not quite the right one, though, and [the ocean](#the-ocean-tacking-and-why-friction-is-the-power-source)
is what breaks it: a wind models nothing outside the artifact, and is obviously legitimate anyway.
What distinguishes it is that the wind is **present in the world the user is in** — perceivable,
reasonable-about, and therefore exploitable. The unsubscribe damping is invisible by construction, and
that invisibility is not incidental to the abuse, it *is* the abuse.

> **Legibility, not fidelity, is the ethical line.** A field the user can perceive is terrain they can
> master, whatever it depicts. A field they cannot perceive is being used on them.

Which promotes [render the state, not the geometry](#visual-thickness-is-independent-of-both) from a
usability rule to the load-bearing ethical requirement of the whole document. It was always the
interesting half.

Which gives the determinism criterion a second axis, and learnability stops being purely good:

| | models the world | models the vendor |
|---|---|---|
| **learnable** | a **tool** — masterable terrain | the worst case: you learn helplessness and rehearse it |
| **not learnable** | a bug, or an honest depiction of impairment | ordinary hostile design |

The uncomfortable cell is top-right. Friction that is consistent, teachable and adversarial is more
effective than friction that is merely annoying, because the user builds an accurate model of a
landscape built to defeat them. Nothing in the technique prevents this. Only the referent test does,
and it is a judgement rather than a check.

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
