# Temkin call agenda — webtop, Declare, Gwern (2026-08-05 18:00)

**Attendees:** Don Hopkins, David Temkin  
**Context:** [Declare constraints thread](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-temkin/sources/2026-08-03-declare-constraints-thread.md)

## Goal

Align on whether **Declare Desktop**-shaped chrome is the right shell for a Gwern-class publishing
site with OpenLaszlo-style **webtop** navigation (tabs, windows, pies, rooms, zoom).

## Show David

1. [This design pack README](README.md) — Gwern praise + inheritance, not fork
2. [Gwern /help](https://gwern.net/help) — popup tiling keys (their WM spec)
3. [Declare Desktop demo](https://davidtemkin.github.io/declarelang/) — press Desktop
4. [pie-menus-window-management article](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/sources/articles/pie-menus-window-management.md)
5. Micropolis [reverse-diagrams](https://github.com/SimHacker/MicropolisCore/tree/main/apps/micropolis/website/pages/reverse-diagrams) — iceberg content model

## Questions

### Declare as webtop shell

- Is **in-browser WM** (Desktop demo) the right target for donhopkins.com / Repo Show / Micropolis?
- Nested windows + transclusion: Declare-inside-Declare vs markdown **islands** + JSON bridge?
- Layout for tab strip + window layer — custom Declare classes (not flexbox)?

### OpenLaszlo webtop memory

- What did LZX **webtop** get right that we should explicitly re-spec?
- OL 5.0 Explorer vs Declare Calendar/Desktop — which patterns port first?

### Overlay vs in-page (recap)

- Kando-style **native overlay** vs **page-scoped webtop** — David's Aug 3 boundary still accurate?
- If JSON bridge is the cross-boundary path: what schema for "open this markdown path in a window"?

### Publishing (Gwern vs Repo Show)

- Gwern: static, solo, archive-heavy. Us: git MMORPG, async Repo Show.
- Does Declare data binding fit **100K-item corpus** sidebar (room listing) without instantiating all views?

## Outcomes hoped

- [ ] David reacts to Gwern inheritance thesis (popup = window)
- [ ] Pick one spike: Declare Desktop fork vs embed markdown transclusion
- [ ] Schedule follow-up or Repo Show segment on "webtop publishing"
- [ ] Note any Declare API gaps for WM/tab/pie primitives

## Don's one-liner for the call

> Gwern built the best popup hypertext reader; OpenLaszlo built the webtop; NeWS built pie menu
> window managers; I want the same publishing virtues inside a classic WIMP shell — and I'm asking
> if Declare is how we chrome it.
