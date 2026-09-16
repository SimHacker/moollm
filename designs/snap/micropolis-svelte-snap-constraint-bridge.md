# Micropolis × Svelte runes × Snap! — the constraint bridge

Code: `MicropolisReactive.svelte.ts`

## The braid (four decades, one idea)

| Era | System | You declare… | System keeps… |
|-----|--------|----------------|---------------|
| ~1992 | **Garnet** (Brad Myers, CMU) | KR constraints between UI slots | Truth via constraint solver |
| 2000s | **OpenLaszlo** (Henry Minsky, LZX) | XML attributes + constraint graph | Client UI synced to model |
| 2020s | **Svelte 5** | `$state`, `$derived`, `$effect` | Truth via compiled reactive graph |
| 2026 | **MicropolisReactive** | Callback fields + `poke` API | WASM engine ↔ Svelte UI ↔ Snap! blocks |

Don worked Garnet and OpenLaszlo; MicropolisCore now ships the modern form. Snap! is the **authoring**
layer Brian and Jens wanted in 2018 — blocks that call the same bridge kids can watch update live.

## MicropolisReactive.svelte.ts — bidirectional binding

The module is a **`.svelte.ts` runes store** — not a component, a shared reactive façade:

**Push (engine → UI):** The C++ sim fires Embind callbacks on `MicropolisReactiveCallback`. Each
handler assigns `$state` (`updateFunds`, `updateMap`, `showZoneStatus`, `sendMessage`, …). Any
Svelte component that reads `micropolisReactive.totalFunds` or `$derived(...)` updates automatically.

**Pull (UI/tools → engine):** `peek.scalars`, `peek.tile`, `syncFromEngine` read the authoritative
`Micropolis` object when callbacks aren't enough.

**Write (authoring → engine):** `poke.doTool`, `poke.setCityTax`, `poke.setTile`, … mutate through
Embind and bump `mapRevision` / `syncFromEngine` so observers redraw.

**Revision counters:** `mapRevision`, `budgetRevision`, … are coarse invalidation signals — spiritually
like Garnet **demons** firing when a constrained slot changes, without every panel polling WASM every
frame.

**Memory:** `memory.mapU16` / `mopU16` expose zero-copy views into WASM linear memory — advanced Snap!
blocks (or CAM6 overlays) can scan the map directly.

**Snapshot:** `getSnapshot()` returns plain JSON — the natural **Snap! reporter** surface and MCP/test
harness.

```typescript
// GameHud.svelte — constraint-style binding, zero manual sync
const funds = $derived(micropolisReactive.totalFunds);
const dateLabel = $derived(
  `${micropolisReactive.cityMonth}/${micropolisReactive.cityYear} · ${micropolisReactive.cityName || 'Micropolis'}`
);
```

OpenLaszlo doc mapping (same repo family):
openlaszlo
— OL constraints → Svelte runes; AMF bridge → `MicropolisReactive`.

## Three visual paradigms, one constructionist platform

| Paradigm | Tool | Micropolis role |
|----------|------|-----------------|
| **Blocks** (control flow) | Snap! | Author rules: tax policy, tool scripts, glass-box lessons |
| **Patch-cords** (dataflow) | Bounce / Rebounce | Wire Micropolis streams to CAM6, VitaMoo, media |
| **Constraints** (declare truth) | Svelte 5 runes | HUD, panels, disaster UI track sim without spaghetti |
| **Engine** | WASM C++ | Authoritative city simulation |

They're complementary, not competing. Snap! blocks **author** behavior; runes **bind** presentation;
Bounce **routes** live streams between engines.

## Bridging into Snap!

Snap! already runs JavaScript in the browser (Morphic.js). Integration path:

1. **Reporter blocks** — `city tax`, `funds`, `demand R/C/I`, `tile at (x,y)` → read
   `micropolisReactive` / `getSnapshot()` / `peek.tile`.
2. **Command blocks** — `set tax`, `place road`, `pause sim` → `micropolisReactive.poke.*`.
3. **Live inspection** — watchers on reactive fields; gray rings on block AST for metaprogramming
   rules that *emit* poke sequences (Brian's CSLS program-as-data thread).
4. **Future constraint blocks** — "when crime > N, highlight zone" — compile to `$derived`-like
   dependencies in the Svelte layer or Bounce **enable** subgraphs for stream gating.

Brian's Sep 2020 dataflow forum hang-up (CPS for conditionals) has a parallel here: **Bounce**
handles dataflow conditionals; **Snap!** handles control flow; **runes** handle declarative UI
constraints — three orthogonal mechanisms, same platform.

## Show beats

- **Brad Myers:** draw a Garnet constraint → same relationship as `$derived` in `GameHud.svelte`.
- **Brian + Jens:** finish 2018 Micropolis × Snap! with a live block palette over `poke`/`getSnapshot`.
- **David Temkin / OpenLaszlo reunion:** what AMF forced us to hack (client tile animation) vs what
  Wasm + runes made trivial.
- **Alan Kay glass-box:** rules visible in blocks *and* in reactive snapshot — not a black-box city.

## Deeper links

- Garnet → Svelte lineage (short)
- [Snap! visual engines vision](snap-visual-engines-fundable-goals.md)
- Bounce dataflow control
- Brian/Jens 2018 thread
- Constructionist response
- Pair show

↑ [Snap! index](README.md)
