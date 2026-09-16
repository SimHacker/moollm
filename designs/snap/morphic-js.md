# Morphic.js — Jens Mönig's live IDE substrate

**Live code:** [src/morphic.js](https://github.com/jmoenig/Snap/blob/master/src/morphic.js) (single file, ~13k lines, AGPL) ·
[docs/morphic.txt](https://github.com/jmoenig/Snap/blob/master/docs/morphic.txt) (programming guide, last changed March 2025) ·
[Snap! source](https://github.com/jmoenig/Snap) · [snap.berkeley.edu](https://snap.berkeley.edu/)

**Version tag in source (2026):** `morphicVersion = '2026-May-11'`

---

## The hook

Direct-manipulation objects all the way down — in the browser, no install. Snap! isn't just blocks
on a canvas; the **IDE itself** is malleable Morphic-style, inheriting Smalltalk's live-system ethos
without requiring Squeak on every student's laptop.

## Heritage

```
Self Morphic → Squeak/Scratch morphs → Dan Ingalls Lively Kernel → Morphic.js → Snap!
```


| Step                 | Who / what                     | Note                                                            |
| -------------------- | ------------------------------ | --------------------------------------------------------------- |
| **Self**             | David Ungar & Randall Smith    | Object soup on screen — morphs you grab and reshape             |
| **Squeak / Scratch** | MIT lineage                    | Morphs in every student's hands before blocks languages split   |
| **Lively Kernel**    | Dan Ingalls                    | Full live system — `lively-kernel-morphic.md` |
| **Morphic.js**       | Jens Mönig                     | Single-file kernel; Snap!'s canvas, menus, halos, IDE chrome |
| **Snap!**            | Jens + Brian Harvey's pedagogy | Blocks on top; Morphic underneath                               |


Alan Kay's test: NeWS was "the right way to go — **except it missed the live system underneath**."
Snap! + Morphic.js is the browser answer — see
Alan Kay on MVC, Morphic, and watchers.

## What Morphic means here (not MVC)

- **Morph** — every on-screen thing is an object you can pick up, resize, embed, script.
- **Not an application** — a soup of morphs; the environment is editable while it runs.
- **Contrast with MVC** — textbooks teach controllers; Morphic teaches **direct manipulation** and
**watchers** (Alan Kay's post-PARC stance in Don's 2011 email thread).

Jens's path: MIT Scratch → **GP under Alan Kay** ([lineage digest](gp-alan-kay-lineage.yml)) →
architected Snap! on his own Morphic.js with Brian shaping "first-class everything"
([snap-first-class-everything.yml](snap-first-class-everything.yml)).

---

## Architecture (from inline docs in morphic.js)

Jens's own summary: **"Canvas and JavaScript — it is just Morphic, nothing else."** Not a line-for-line
port of Squeak Morphic, but many methods (e.g. `fullCopy()`) were copied almost literally, comments included.
Ingalls's **Lively Web** (`core/lively/morphic/`) is the
**full live-system** reference; morphic.js is the **distilled kernel** Jens built for Snap!.

### Kernel (the big picture)

| Mechanism | Role |
|-----------|------|
| **`requestAnimationFrame` + `world.doOneCycle()`** | Main loop: step morphs, run animations, redraw dirty rects |
| **`step()` / `fps`** | Per-morph time-sharing; illusion of concurrency on one browser thread |
| **`broken[]` dirty rectangles** | Progressive display — only damaged regions redrawn each cycle |
| **Morph tree (`Node` → `Morph`)** | Submorphs nested; z-order by child list |
| **`WorldMorph`** | One world per `<canvas>`; can host multiple worlds on one page |
| **`HandMorph`** | Invisible cursor/finger; dispatches mouse/touch/drop to morphs under pointer |
| **`keyboardFocus`** | Single text-entry focus per world (`CursorMorph`, `MenuMorph`) |

**Explicitly not in the kernel:** general morph rotation/transforms (planned for separate morph types or
`microworld.js`). **`PenMorph`** provides LOGO turtle graphics on any parent morph's pen-trails layer.

### Class hierarchy (core)

```
Node → Morph
  WorldMorph, HandMorph, FrameMorph, ScrollFrameMorph, ListMorph
  MenuMorph, MenuItemMorph, InspectorMorph
  StringMorph, TextMorph, CursorMorph
  BoxMorph, SliderMorph, DialMorph, TriggerMorph
  PenMorph, HandleMorph, ShadowMorph, …
Point, Rectangle, Color, Animation
```

### Event model (direct manipulation)

**Mouse (via Hand):** `mouseDownLeft/Right`, `mouseClickLeft/Right`, `mouseDoubleClick`, `mouseMove`,
`mouseScroll`, enter/leave (+ dragging variants). Handlers are optional methods on morph prototypes;
bubble with `escalateEvent()`. **`lockMouseFocus()`** keeps events on a morph after pointer leaves bounds
(sliders, resize handles).

**Drag & drop:**

- `isDraggable` — pick up and re-parent on drop.
- **`isTemplate`** — palette pattern from Scratch: non-draggable template **peels off** a `fullCopy()` that
  *is* draggable (`reactToTemplateCopy` hook). Snap! blocks use this.
- Drop targets: `acceptsDrops` / `wantsDropOf()`; callbacks `justDropped`, `reactToDropOf`, `prepareToBeGrabbed`.
- External file drops: `droppedImage`, `droppedSVG`, `droppedAudio`, `droppedText`, `droppedBinary`; PNG
  metadata can embed Snap! block payloads (`embedMetadataPNG`).

**Keyboard:** routed to `keyboardFocus`; hidden `<textarea id="morphic_keyboard">` shared across worlds for
IME/copy-paste. **`world.currentKey`** enables shift-click / modifier-click behavior.

**Text editing:** `reactToKeystroke`, `reactToInput`, `reactToEdit`, `accept`/`cancel`; optional Bret-Victor
**scrubbing** via slider under numeric fields (`useSliderForInput`).

### Dev mode vs user mode

`world.isDevMode` switches context menus:

- **User:** `userMenu()` / `customContextMenu` on each morph.
- **Dev:** `developersMenu()` — inspect, duplicate, pick up, attach, resize handles, live eval in
  **`InspectorMorph`** (Smalltalk-style property browser + eval pane).

Ship with dev mode off for end users; toggle for builders.

### ScrollFrameMorph — inertial pan (MediaGraph cousin)

`ScrollFrameMorph` supports **drag-to-scroll** with optional **velocity decay** (`hasVelocity`, friction
0.8) — same interaction family as MediaGraph flick-to-set-velocity. Also auto-scroll while dragging near
edges (`startAutoScrolling`), mouse-wheel `mouseScroll`.

### Animations & scheduling

`Animation` objects with easing functions; registered on `world.animations`. Helpers: `glideTo()`, `fadeTo()`,
`slideBackTo()`, `world.schedule()` (once, lockstep with display cycle), `world.once()` (conditional).

Global **`ZOOM`** (≥ 1) via `world.zoom(factor)` for accessibility magnification.

### Acknowledgements (Jens, in source)

| Person | Credit |
|--------|--------|
| **Randy Smith & John Maloney** | Original Morphic in **Self** |
| **John Maloney & Dan Ingalls** | Squeak port; Ingalls → **Lively Kernel** JS ("Gold Standard" self-sustaining system morphic.js *does not aspire to meet*) |
| **John Maloney** | Mentor for Morphic experiments |
| **Evelyn Eastmond** | DesignBlocksJS inspiration |
| **Brian Harvey** | Submenu design in MenuMorph |

Contributors include Nathan Dinsmore (mouse wheel, perf), Bartosz Leper (retina), Bernat Romagosa, Michael Ball, etc.

### Minimal embed pattern

```html
<canvas id="world" tabindex="1" style="position: absolute;"></canvas>
<script src="morphic.js"></script>
<script>
  var world;
  window.onload = function () {
    world = new WorldMorph(document.getElementById('world'));
    world.isDevMode = true;
    loop();
  };
  function loop() {
    requestAnimationFrame(loop);
    world.doOneCycle();
  }
</script>
```

---

## Ebike Safari / map UI parallels

| Morphic.js | Ebike Safari design |
|------------|---------------------|
| `ScrollFrameMorph` inertial drag + friction | MediaGraph inertial pan — grab map anytime, flick velocity |
| `MenuMorph.popUpAtHand` / keyboard menu nav | Pie menu smell-steer — default wedge pre-selected |
| `isTemplate` peel-off copies | Pinball construction-set palette — peel gadgets onto map |
| `world.isDevMode` + `InspectorMorph` | Demo/debug tools *inside* the playable game |
| `world.schedule()` / stepping | Replay scrubber, smell diffusion ticks, animal herding sim |
| External `droppedImage` + PNG metadata | Drop YAML-jazz / peerboard stains onto map morphs |

Full lineage map: Alan Kay — morphic-lineage.md.

---

## Show hooks

- **Morphic.js demo** — edit the IDE while you're teaching in it.
- **Kay's live-system criterion** — Snap! as the browser answer.
- **Morphic vs MVC cargo-cult** — why textbooks teach controllers, not morphs.
- **Pair with Brian** — the turtle (Logo) and the morph (Smalltalk) in one classroom tool
(pair show).



## Deeper links


| Topic                              | Where                                                                                                                 |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| GP → Snap! under Kay               | [gp-alan-kay-lineage.yml](gp-alan-kay-lineage.yml)                                                                    |
| Blocks + metaprogramming           | [Brian's macros digest](snap-macros-metaprogramming.md)                                    |
| Micropolis × Snap! (2018)          | micropolis-snap-2018.yml · readable |
| Constraint bridge (runes + blocks) | [micropolis-svelte-snap-constraint-bridge.md](micropolis-svelte-snap-constraint-bridge.md)  |
| Dan Ingalls — Lively lineage       | Dan's Lively Web digest |
| David Ungar — Self / Morphic birth | David's room                                                                           |
| Palmhoo shelf                      | Code & Craft — Morphic.js                                                |
| Palm's Snap! questions             | questions.yml                                 |


↑ [Snap! index](README.md)