# Turn Tables — the only control you need 🎛️🎚️

*Don's coinage and design. A general-purpose interface control: rotational selection,
real-time gesture, and continuous parameter tracking, in one primitive.*
Portrayal standards

> **Turn Table** *(n.)* — a control you **turn** to **index a table**. Discrete selection and
> continuous parameter tracking are the same gesture at different resolutions, so one control
> does both, plus transport.

**Two Turn Tables and a microphone.** That's the whole rig.

## The four puns

| Reading | What it means | What it buys |
|---|---|---|
| **Turntable** (the DJ instrument) | A performance surface you play with your hands, in real time, in front of people | This is the VJ interface argument: the solved version of "expose a large parameter space to a human under performance pressure with no manual" |
| **Turn** (rotate) | Angle is the input | Angle is unbounded, relative, reversible, and has no travel limit — which is why knobs outlived faders on every instrument that has to be played |
| **Table** (lookup table) | The thing being indexed | The CAM-6 contract, the kernel bank, the rule table, the color map. Turning literally rotates you through a lookup table |
| **Pie menu** | Angular selection with detents | Don's own 1988 control, which is a Turn Table with the quantizer switched on — see pie menus and gesture space |

## The claim underneath the joke

A pie menu is **a quantized angle**. A knob is **an unquantized angle**. They have always
been the same control, and the industry shipped them as unrelated widgets in different
toolkits with different APIs, different visual languages, and no path between them.

Put the quantizer on a dial and the distinction dissolves:

- **Detents off** → a knob. Continuous parameter, full resolution.
- **Detents on, N of them** → a pie menu with N items. Discrete selection, muscle memory by
  direction, self-revealing on hesitation, mouse-ahead for experts.
- **Detents variable** → a quantizer, which is a *musical* control. Snap to eight
  neighborhoods, or to the twelve rules you've starred, or to nothing.

One widget, one gesture vocabulary, one thing to learn. A student who can turn a knob can
already work every control in the system, including the ones that pick between rules.

## Three modes, same surface

1. **Select.** Turn to a detent, you've chosen an entry. Which rule, which neighborhood,
   which kernel, which scheduler.
2. **Tune.** Turn freely, you're driving a parameter. Zoom, decay, focus, diffusion rate.
3. **Scrub.** Turn *fast and back and forth* and you're a transport, not a selector — because
   a real turntable is also a tape head. Scrub the simulation's history, scrub recorded
   parameter automation, scrub the phase sequence. **Scratching is a legitimate way to
   interrogate a dynamical system**, and it's the gesture people already know from every
   video player.

Mode three is the one nobody builds and it's free once angle is your input.

## Indirection and indexing (the 6502 was right)

The essence of a Turn Table is not rotation. **It's indirection.** You turn a thing over
*here* to change which thing is read over *there*. That's a pointer, operated by hand.

The 6502 had exactly two indirect addressing modes, and they are precisely the two ways to
compose a Turn Table:

**Indexed indirect** — `LDA ($40,X)`
Add the index *first*, then dereference. You are indexing **a table of pointers**, then
following the one you landed on. This is a **dispatch table**.
→ *The turn chooses **which table** you're reading.* Which rule set, which bank, which
instrument.

**Indirect indexed** — `LDA ($40),Y`
Dereference *first*, then add the index. You follow a pointer to a base address, then index
**within** the thing it points at.
→ *The table is already chosen; the turn picks **which entry**.* Which kernel of the sixteen,
which opcode, which color.

These are not the same operation and the difference is the entire architecture. One selects
context, the other selects content. Wire them in the wrong order and the machine is still a
machine, just a different one.

## So: two Turn Tables and a microphone

**Two**, because two composed indirections is the interesting number. One Turn Table chooses
the bank, the other chooses within it — indexed indirect feeding indirect indexed, a hand on
each. That covers the whole space the
[CAM Construction Set](cam-construction-set.md) needs, including the nested case where a
selector's source is another bank's output. Three would be showing off. One isn't enough to
express context-plus-content.

**And a microphone**, because the third input isn't a hand at all — it's a **live signal**.
Audio, camera, MIDI clock, body position, the cell's own value. Anything that can produce a
number can drive an index, and then the table is being turned by the world instead of by you.
That's the same distinction the
[phase matrix](cam-construction-set.md#the-phase-matrix--the-component-the-marble-rules-were-hiding)
already draws between manual selectors and signal selectors, arriving from the interface side
rather than the engine side.

It's also, exactly, what
WarpOMatic did in 2003 without having a name for
it: the performer's position and silhouette area were a microphone, wired straight to the
parameters. The body was turning the tables.

## Prior art, and it's better than what I specified

**Dave Tristram's bouncing sliders**, in
the **Panel Library** he and **Eric Raible** built at NASA Ames — the toolkit that drove
**Electropaint** live at Grateful Dead shows. Don and Dave presented at the *same* meeting:
the **USENIX Fifth Computer Graphics Workshop, Monterey, 16–17 November 1989**, where Don
gave *The Shape of PSIBER Space*. Dave mailed him the Panel Library and Electropaint source
afterward.

Each slider had **value, min, max, speed, and wrap**, adjustable and scrubbable *while
running*, in banks. Which fixes two things above:

- **A control and a signal source are one widget, not two.** This page treats "a hand on the
  dial" and "the microphone" as different selector sources. Tristram's sliders were both at
  once — running on their own, still grabbable mid-motion. That's the correct primitive, and
  it's the DJ reading taken seriously: a platter under the needle is *always* turning, and
  your hand is an interruption, not the drive.
- **`wrap` is the parameter that makes a slider angular.** With wrap it's a knob; without it,
  it reflects at the ends and bounces. So a Turn Table has *two* discretization parameters,
  not one: the **quantizer** (detents) and the **boundary** (wrap / bounce / clamp). Bounce
  is the one nobody offers and it's the reason those panels looked alive.

The Panel Editor also emitted **human-editable Scheme** next to its C — the "binding is data,
patches savable and diffable" line in the spec below, shipped in 1989.

**And then the cautionary tale.** Electropaint reached the world as an **SGI Indy
screensaver with the sliders hidden**, playing back recorded performances. The instrument
became a decoration; the panel that made it an instrument didn't ship. That's the same loss
the [CAM Construction Set](cam-construction-set.md) complains about when CA toys hide the
machine, and the same one the letter to Jim is
arguing against when it asks for the meters on the front door instead of behind an advanced
tab. **Hiding the controls is how an instrument becomes wallpaper.**

## Why this is one object, seen twice

The [CAM Construction Set](cam-construction-set.md) argues that the engine needs exactly one
core component — **a bank of behaviors plus a selector that resolves to an index** — and that
kernel banks, the anneal arbiter, RISCA opcode dispatch, and plane routing are all that
component with different selectors plugged in.

**A Turn Table is that component's face.** Same object, opposite side of the screen:

| Engine | Interface |
|---|---|
| bank | the table you're turning through |
| selector | the Turn Table |
| selector source: constant | a hand on the dial |
| selector source: clock / position / cell value / signal | the microphone |
| nested selectors | two Turn Tables, indexed indirect into indirect indexed |

Which is what "all you need are Turn Tables" claims architecturally. If
the engine really is one component repeated, then the interface really is one control
repeated, and **every knob in the system can be built, labeled, bound, and learned the same
way** — including the ones that select rules, the ones that select neighborhoods, and the
ones that select which scheduler is running.

## What a Turn Table has to provide

The spec, so the thing is buildable rather than merely named:

- **Angle in, index out**, with an optional quantizer (detent count, or a detent set).
- **Self-revealing.** Hesitate and it shows you the table — the pie menu behavior. Move
  immediately and it stays out of your way.
- **Bindable to anything**: mouse, touch, pen, jog wheel, MIDI encoder, gamepad stick, key
  pair, or a signal. The binding is data, not code.
- **Nameable and addressable**, so a patch can be saved, shared as a URL, and diffed.
- **Labeled with what it actually is** — if it's driving Crutchfield's storage decay `L`, the
  control says so and cites the equation. That's the
  crutchfield-machine `CREDITS.md` discipline
  applied to the UI: *put the citation on the slider*.
- **Instrumentable.** Log which controls get touched, so the ones nobody finds can be fixed
  rather than defended.

## See also

- [`cam-construction-set.md`](cam-construction-set.md) — the engine side: banks, selectors, schedulers, codegen
- `pie-menus-chi-88-and-beyond.md` — the quantized case, thirty-eight years of it
- `gesture-space.md` — gesture as a design space; self-revealing vs. memorized
- `connectedtv-touch-tuning-finger-pies.md` — touch tuning, the continuous case on a TV remote
- `warpomatic-video-background-removal.md` — the microphone, before it had a name
- `../jim-crutchfield/positive-feedback.md` — what the meters next to the Turn Tables should read

*Status: coinage and design. Named 2026; the parts are all older than the name.*
