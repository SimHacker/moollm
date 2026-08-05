# Reverse over-engineering Gwern.net (self-aware)

**Method:** Download with respect. Praise in prose. Infer mechanisms from source + behavior.
Mark speculation as speculation. Do not confuse aesthetic polish with architectural simplicity —
the [gwern.net repo](https://github.com/gwern/gwern.net) is large because the problem is large.

## Self-aware rules

1. **Surface polish is a feature** — Gwern's UI quality is part of the thesis; studying it is not
   "missing the point."
2. **Underneath is still static** — Hakyll + Pandoc + generated HTML + vanilla JS pub/sub
   ([unofficial docs summary](https://gwern.pleometric.net/)). No React; intentional.
3. **We are not forking Gwern** — we inherit patterns into MOOLLM/Micropolis/Repo Show.
4. **Reverse over-engineering** — Will Wright's phrase: infer design intent from behavior +
   artifacts; hold hypotheses lightly.

## Mirror targets

| Target | Purpose |
|--------|---------|
| [github.com/gwern/gwern.net](https://github.com/gwern/gwern.net) | Build pipeline, JS modules, templates |
| [gwern.net/design](https://gwern.net/design) | Feature catalog + philosophy |
| [gwern.net/help](https://gwern.net/help) | Keybinding / popup WM behavior spec |
| Built pages under `/doc/` on live site | Screenshots, CSS, popup demos |

Local mirror: sister repo at `~/GroundUp/git/gwern.net/` (house convention — repos side by side,
added to the Cursor workspace) — see [ANALYSIS-WORKFLOW.md](ANALYSIS-WORKFLOW.md).

## Repo anatomy (verified against sister clone, 2026-08-05)

Cloned at `~/GroundUp/git/gwern.net` (315 MB shallow). Actual top level:

```
gwern.net/
├── build/                     # Haskell build modules: LinkArchive.hs, LinkBacklink.hs,
│                              #   LinkMetadata.hs, Annotation/, Typography.hs, Tags.hs,
│                              #   GenerateSimilar.hs, Interwiki.hs, Inflation.hs, XOfTheDay.hs …
├── js/                        # 38 frontend modules — the interesting WM lives here:
│                              #   popups.js, popovers.js, extracts*.js (annotation popups),
│                              #   transclude.js, collapse.js, sidenotes.js, layout.js,
│                              #   content.js, rewrite.js, reader-mode.js, dark-mode.js,
│                              #   image-focus.js, initial.js, utility.js
├── css/                       # typography, layout, dark mode
├── template/                  # Pandoc/Hakyll HTML shells
├── include/, font/, img/      # assets
├── nginx/                     # server config
└── asset.php                  # asset pipeline entry
```

Key split confirmed: **desktop popups (`popups.js`) vs mobile popovers (`popovers.js`)** are
separate engines; `extracts*.js` decides *what* goes in a pop-frame, popups/popovers decide *how
it behaves as a window*. `transclude.js` + `collapse.js` are the semantic-zoom pair. The Haskell
side is heavier on link infrastructure (archive, backlink, metadata, similar-links) than on
layout — the moat is the **link pipeline**, exactly as hypothesized.

**Frontend event bus:** pub/sub coordinates popups, transclusion, theme — study coupling before
copying. MOOLLM equivalent: skill advertisements + `lookto` / room activation.

## Behavioral spec to capture (from /help)

Treat as acceptance tests for MOOLLM webtop:

| Key / action | Behavior |
|--------------|----------|
| Click link | Open popup with excerpt or full transclusion |
| Drag title bar | Move popup |
| Edge drag | Resize |
| Pin icon | Sticky (survives mouse leave) |
| `a/s/w/d` | Tile to half screen |
| `q/e/x/z` | Tile to quarter |
| `f` | Fullscreen popup |
| `t` | Minimize / restore stack |
| `g` / `b` | Cycle popup z-order |
| `Esc` | Close focused popup |
| Gear → speech bubble | Disable popups/popovers |

**Our delta:** same semantics, but windows live in a **tab strip + pie menu** shell; optional
**room** behind the desk (memory palace directory listing).

## Analysis outputs

| Output | Location |
|--------|----------|
| Grep notes (popups.js, transclusion) | `sources/analysis-notes/` |
| Module dependency sketch | append to this file after clone |
| Side-by-side table Gwern vs MOOLLM | [MOOLLM-WEBTOP-VISION.md](MOOLLM-WEBTOP-VISION.md) |
| Public article draft | `sources/article-draft.md` (later) |

## Hypotheses to validate (not facts yet)

- Popups are a lightweight WM with a single global z-order list, not a full scene graph.
- Transclusion is fetch + DOM graft + backlink injection at parse or runtime.
- "Semantic zoom" is mostly CSS collapse + JS toggle, not a separate zoom engine — our zoom
  will be **literal** (Mesa/Declare calendar continuity).
- Archive pipeline is the secret moat — budget time if we want parity.

## Article angle (working title)

**"Gwern's popups are a window manager: what MOOLLM inherits and what we add"**

Sections: praise → popup-as-WM proof → publishing substrate (git vs Hakyll) → webtop vision →
Declare Desktop demo → open questions for Temkin.
