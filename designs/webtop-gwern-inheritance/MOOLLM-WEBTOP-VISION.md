# MOOLLM webtop vision (Gwern + OpenLaszlo + NeWS)

Classic **WIMP** on purpose. Not reinventing the desktop metaphor — **completing** what Gwern's
popups hint at and what OpenLaszlo's **webtop** shipped twenty years ago.

## Two deployment surfaces (same object model)


| Surface            | Runtime                                                 | Use                                                |
| ------------------ | ------------------------------------------------------- | -------------------------------------------------- |
| **Browser webtop** | Any tab — SvelteKit or **Declare** app embedded in site | micropolisweb.com, donhopkins.com, Repo Show pages |
| **Overlay webtop** | Electron (Kando lineage) + OS accessibility APIs        | Frame native windows, pie menus over desktop       |


David Temkin's Aug 2026 line: in-app WM (**Declare Desktop** demo) is in scope today; native
overlay needs **JSON/cell bridge** + Electron hooks — design for it, ship browser-first.

## Shell ingredients



### Tabs (document-centric)

- Repo Show episode, character room, design doc, running simulation = **tabs**
- Tab pie menu: close, detach to window, move to stack, "open in git"
- Heritage: NeWS tabbed frames, OWM, PSIBER Space Deck tab edges



### Windows (Gwern popups done right)

- Gwern popups + `/help` tiling keys → **first-class window class**
- Pin = sticky; minimize = icon tray; transclusion = "open linked doc in new window"
- Recursive popups = MDI / floating palette pattern



### Pie menus (spatial command selection)

- Window frame pies (NeWS ICCCM WM), Kando overlay, Micropolis **PIE-TAB-WINDOWS**
- Directional layout for WM commands: front/back, grab corners, move axis



### Rooms (memory palace)

- Directory listing = **room activation** ([HOME-AUTOMATION-MEMORY-PALACE](../HOME-AUTOMATION-MEMORY-PALACE.md))
- Zoom into room → subdirectory; objects = files; characters = `CHARACTER.yml`
- GitHub repo browser IS the adventure map ([GITHUB-AS-MMORPG](../GITHUB-AS-MMORPG.md))



### Zoom (semantic + geometric)

- **Gwern:** collapse sections, expand in place
- **Mesa / Declare calendar:** one surface, continuity zoom ([Temkin Mesa notes](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/david-temkin/sources/mesa-and-in-formation.md))
- **Micropolis:** map zoom + Chaim reverse-diagram Cards drill-down
- **MOOLLM:** yaml-jazz pyramid — GLANCE → CARD → SKILL → README



## Stack options (Temkin call topics)


| Layer      | Candidate               | Role                                                              |
| ---------- | ----------------------- | ----------------------------------------------------------------- |
| Shell UI   | **Declare**             | Desktop demo, constraint layout, no HTML/CSS — pure webtop chrome |
| Shell UI   | **Svelte 5 runes**      | MicropolisCore already; wasm Simulator bridge                     |
| Content    | **Markdown/yaml rooms** | Git-native, Gwern-like corpus                                     |
| Hypertext  | **Transclusion skill**  | Fetch + graft + backlink                                          |
| WM overlay | **Kando + Electron**    | Pie menus over OS windows (stretch)                               |
| Publishing | **Repo Show**           | Issues/PRs as quests; better for collaboration than solo Hakyll   |


**Declare fit:** David's Desktop demo is an in-browser WM. Our webtop could be a Declare app
that hosts transcluded markdown islands via JSON bridge — ask today whether nested Declare +
markdown corpus is the happy path.

**OpenLaszlo fit:** LZX webtop was literally "desktop in the browser." OL 5.0 revival + Declare
heir = two layers to compare on the call.

## Contrast table (working)


| Concern        | Gwern.net                         | MOOLLM webtop                            |
| -------------- | --------------------------------- | ---------------------------------------- |
| Corpus storage | Hakyll source + generated HTML    | Git repos, yaml-jazz                     |
| Collaboration  | Solo (+ PRs on gwern.net repo)    | GitHub MMORPG, Repo Show                 |
| Navigation     | Popups, tags, search              | Rooms, tabs, pies, zoom                  |
| Simulation     | —                                 | Micropolis wasm, Soul City               |
| LLM role       | Python LLM text tools in pipeline | LLM as resolver, cauldron, cursor-mirror |
| Aesthetic      | Minimal monochrome                | Classic WIMP + optional retro chrome     |




## Minimum viable webtop (browser)

1. One **desk** page with tab strip + empty window layer
2. Open any `website/pages/**/README.md` in a window (Micropolis content plugin)
3. Link click → popup window with transclusion (Gwern semantics)
4. Pie menu on window title bar (close, tile left/right, pin)
5. "Room" sidebar = current repo directory listing (memory palace)

Ship in Micropolis site first; extract package later.