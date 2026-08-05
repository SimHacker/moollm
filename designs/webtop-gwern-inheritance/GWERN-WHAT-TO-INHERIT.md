# What to inherit from Gwern.net

Gwern.net is one of the best demonstrations that **static sites can behave like a research
environment**, not a pile of PDFs. The [design essay](https://gwern.net/design) is honest about
trade-offs: Hakyll + Pandoc + custom JS, bandwidth on a dedicated server, complexity bought for
reader time and attention.

We are not competing on minimalism. We are **inheriting the problems Gwern solved well** and wrapping them in a different shell (classic WIMP webtop + tabs + pies + MOOLLM rooms + memory palace navigator/reader/editor).

## Problems Gwern solves brilliantly

### 1. Long-form publishing that respects the reader

- **Semantic zoom / iceberg pages** — most depth hidden; drill down on demand ([design](https://gwern.net/design))
- **Progressive enhancement** — core reading works without JS; popups are acceleration
- **Reader mode** — strip chrome when the typography is "too much"
- **Typography as infrastructure** — sidenotes, dropcaps, inflation-adjusted currency, link icons

**Inherit:** treat every essay, Repo Show character room, and design doc as an iceberg with
collapsed depth; default calm surface, instant drill-down.

### 2. Frictionless hypertext (1980s dream, 2020s implementation)

- **Link popups / popovers** — previews, annotations, recursive popups ([help keybindings](https://gwern.net/help))
- **Transclusion** — embed another page's content without leaving context
- **Popups as first-class windows** — drag, resize, pin/sticky, minimize, **half-screen zoom**
(`a/s/w/d/q/e/x/z/f` tiling), cycle focus (`g`/`b`)

**Inherit:** popups are not tooltips — they are **windows in a desktop**. Gwern's popup chrome is
the seed of our webtop window manager.

**Verified in source (the TNT pin test):** Gwern's pin is a class flag on the same window
object — no rewrap, no reparent (`popups.js:1083`). Same architecture as Don's TNT OPEN LOOK
pin-up menus (menu frames subclass window frames; promotion = flag), and the opposite of the
olwm/ICCCM rewrap dance forced by a separate-process WM with no shared class hierarchy.
**Anti-inherit, two real transient/persistent splits that remain:** (1) pinned popups die on
page navigation — pin must instead promote onto a persistent, serialized desk; (2) desktop
Popups vs mobile Popovers are two windowing engines — we want one window class with adaptive
chrome. **Aesthetic fix:** pin button is a bare icon swap; restore the OPEN LOOK push-in /
pull-out pin rotation — the animation IS the affordance that teaches promotion.

### 3. Linkrot and provenance

- Local archives, metadata on links, bidirectional backlinks, tag/directory navigation
- Build-time extraction (Arxiv, Crossref, etc.) + hand annotations with consistent rewrite rules

**Inherit:** git + Repo Show already IS provenance; add **archive mirrors** and **backlink index**
as first-class repo artifacts (cursor-mirror, sister-script).

### 4. Single author, decades of corpus, one voice

- Stable URL space, index pages, "about the site" as living document
- Feature demo pages (Lorem Ipsum stress test) — self-documenting UI

**Inherit:** MOOLLM + Will Wright Show For Food + MicropolisCore as **one navigable corpus** with
consistent house style (telecine jiggle, yaml-jazz, portrayal standards).

## What we deliberately reimagine (not a critique)


| Gwern choice                                         | Our reinterpretation                                                    |
| ---------------------------------------------------- | ----------------------------------------------------------------------- |
| Popup frames feel "desktop-ish" but aren't a full WM | **Real WIMP webtop** — tabs, stacks, pie menus, z-order                 |
| Gear menu for theme/popup toggles                    | **Pie menu + menu bar**; settings as a room                             |
| Semantic zoom within one page                        | **Semantic zoom across repos** — Soul City, rooms, zoom into simulation |
| Haskell Hakyll build                                 | **Git-native** — markdown/yaml in repo; LLM + cauldron as compiler      |
| Monochrome minimal aesthetic                         | **Classic Mac/NeWS/SunView nostalgia** optional; content-first          |
| Mobile popovers vs desktop popups                    | Same code, **Declare or Svelte** layout classes per form factor         |




## Explicit inheritance checklist

- [ ] Popup = window (drag, resize, pin, minimize, tile halves, fullscreen)
- [ ] Recursive transclusion with stable back navigation
- [ ] Link metadata + local archive fallback
- [ ] Backlinks generated from repo graph (not just HTML)
- [ ] Reader/calm mode vs expert/chrome mode
- [ ] Keyboard chord table published like `/help`
- [ ] Iceberg TOC — section collapse, expand in place or new window
- [ ] "Design of this site" page always current (this directory + live demo)



## Credit line (use everywhere)

> Hypertext popup and archiving patterns inspired by [Gwern.net](https://gwern.net/design)
> (Gwern Branwen; frontend by Said Achmiz). Shell reinterpretation: MOOLLM webtop —
> OpenLaszlo / NeWS / Self lineage.

