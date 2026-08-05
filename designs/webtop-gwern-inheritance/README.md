# Webtop: Gwern inheritance and MOOLLM reinterpretation

**Status:** Design (active)  
**Date:** 2026-08-05  
**Author:** Don Hopkins  
**Temkin call:** 2026-08-05 18:00 Don time — [agenda](TEMKIN-CALL-2026-08-05.md)

Self-aware **reverse over-engineering**: respect Gwern.net's surface polish, read generously
into what it solves, inherit the publishing virtues, reimagine the shell as a classic WIMP
webtop — tabs, windows, pie menus, rooms, zoom, memory palaces — not because Gwern got the
desktop wrong, but because he was solving different (excellent) problems.

## Reading order

| Doc | What |
|-----|------|
| [GWERN-WHAT-TO-INHERIT.md](GWERN-WHAT-TO-INHERIT.md) | Praise and explicit inheritance list — publishing, hypertext, archives, semantic zoom |
| [REVERSE-OVER-ENGINEERING.md](REVERSE-OVER-ENGINEERING.md) | Mirror workflow, repo anatomy, what to measure, self-aware limits |
| [MOOLLM-WEBTOP-VISION.md](MOOLLM-WEBTOP-VISION.md) | Our shell: WIMP webtop, pie/tab windows, rooms, Declare vs Svelte vs OL |
| [TEMKIN-CALL-2026-08-05.md](TEMKIN-CALL-2026-08-05.md) | OpenLaszlo webtop, Declare Desktop demo, JSON bridge, overlay WM vs in-page |
| [ANALYSIS-WORKFLOW.md](ANALYSIS-WORKFLOW.md) | Clone, mirror, grep, article pipeline |
| [sources/analysis-notes/](sources/analysis-notes/README.md) | **Source deep dive (done):** architecture, popup WM + TNT pin test, GTX link pipeline, LLM guardrails, styling/delivery |
| [sources/README.md](sources/README.md) | Captured notes, links, sister-repo mirror pointer |

## One-line thesis

**Gwern solved long-form hypertext publishing and reader attention; we solve the same backing-store problems via Repo Show + git, and add a Self/NeWS/OpenLaszlo-class webtop for navigating it.**

## Related MOOLLM / Micropolis / WWSFF

- [GITHUB-AS-MMORPG.md](../GITHUB-AS-MMORPG.md) — publishing substrate
- [HOME-AUTOMATION-MEMORY-PALACE.md](../HOME-AUTOMATION-MEMORY-PALACE.md) — rooms as directories
- [object-system/README.md](../object-system/README.md) — directory-as-object, advertisements
- [MicropolisCore PIE-TAB-WINDOWS](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/notes/PIE-TAB-WINDOWS.md) — Cards, tabs, Chaim diagrams
- [pie-menus-window-management](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/sources/articles/pie-menus-window-management.md) — overlay WM lineage
- [David Temkin Declare thread](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-temkin/sources/2026-08-03-declare-constraints-thread.md)
- [Declare live](https://davidtemkin.github.io/declarelang/) — press **Desktop**
- [Gwern design essay](https://gwern.net/design) · [gwern/gwern.net repo](https://github.com/gwern/gwern.net)

## Deliverables (planned)

1. **Design pack** (this directory) — done as scaffold
2. **Mirror analysis** — **done** — sister clone at `~/GroundUp/git/gwern.net`, deep dive in [sources/analysis-notes/](sources/analysis-notes/README.md)
3. **Article** — praise + inheritance + contrast table (Repo Show vs gwern.net)
4. **Prototype spikes** — Declare Desktop-shaped shell; Micropolis site as webtop; Kando overlay WM (Electron) as stretch
