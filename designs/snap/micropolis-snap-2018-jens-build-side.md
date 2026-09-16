# Micropolis × Snap! — Jens on the build side

**Brian's write-up:** ../../brian-harvey/sources/micropolis-snap-2018.md ·
**Pair show:** snap-logo-brian-jens

---

## The gist

Don asked Brian about driving **Micropolis** (open SimCity) and **CAM6** cellular automata from
**Snap!** blocks. Brian forwarded to Jens — the person who would actually wire blocks to live
simulation parameters.

| Field | Value |
|-------|-------|
| First contact | 2018-05-15 |
| Participants | Don Hopkins, Brian Harvey, Jens Mönig |
| Consent | not_yet_asked (public-safe digest only) |

Same constructionist thread as Alan Kay's Nov 2007 OLPC "SimCity Rules" — glass-box sim, not black box.

## Jens's angle (engineering)

Implementation questions on Jens's side:

- **Morphic.js hooks** — where block primitives meet the live IDE
- **Block extensions** — custom reporters/commands as JavaScript primitives
- **Live parameter binding** — city tax, tools, map state without polling spaghetti
- **Schemas for structured simulation data** — Don's Snap!Con Barcelona talk as follow-on

**2026 implementation path:** [`MicropolisReactive.svelte.ts`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/micropolis/src/lib/MicropolisReactive.svelte.ts)
+ `poke` / `getSnapshot` — see
[constraint bridge digest](micropolis-svelte-snap-constraint-bridge.md).

## Show hooks

- **Micropolis × Snap! demo** — city zoning from blocks, live.
- **CAM6 CA rules** as a visual-programming lesson — Norman Margolus orbit.
- **Schemas for Snap!** — Barcelona talk as solo vertical.
- **Distributed messaging / actors in Snap!** — where blocks meet concurrency.

## Deeper links

| Topic | Where |
|-------|--------|
| Brian's digest | ../../brian-harvey/sources/micropolis-snap-2018.md |
| Brian correspondence | ../../brian-harvey/correspondence.yml |
| Palm Q7 — Micropolis metaprogramming | ../../../repo-shows/snap-logo-brian-jens/audience/palm/questions.md |
| MicropolisCore | [MicropolisCore](https://github.com/SimHacker/MicropolisCore) |
| Constructionist response | ../../../process/constructionist-simcity-response.md |

↑ [Snap! index](README.md)
