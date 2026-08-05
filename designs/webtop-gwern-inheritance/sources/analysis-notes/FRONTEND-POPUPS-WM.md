# Gwern.net frontend: the pop-frame window system

**Source:** `~/GroundUp/git/gwern.net/js/` — 39 files, ~29k hand-written lines (plus
generated bundles `script-GENERATED.js` ~24k and `head-GENERATED.js` ~7k). No framework:
vanilla JS, global module objects, an event bus. This is the closest existing thing to the
MOOLLM webtop's window layer, so it gets the deepest read.

## Module map

```
initial.js (1354)  boot, GW namespace, notificationCenter, load/inject pipeline
utility.js (1886)  DOM helpers, doAjax, rect math
    |
content.js (2031)      polymorphic content loaders (15 types)
annotations.js (445)   annotation fragment fetch + parse
transclude.js (2587)   include-link engine + template DSL
rewrite.js (4803)      post-load DOM rewriting (phased)
layout.js (1584)       content-aware block layout processors
    |
extracts.js (952) + extracts-content.js (1304) + extracts-annotations.js (289)
    |                  "what opens in a window" — target-type registry
popups.js (2719)       desktop window manager
popovers.js (733)      mobile stacked-sheet manager
    |
sidenotes.js (1325)    margin-note geometric packer
collapse.js (1248)     disclosure/collapse blocks
image-focus.js (980)   lightbox
dark-mode.js, reader-mode.js, misc.js (2784), typography.js, color.js, console.js
```

## Pop-frames: one API, two window models

`Extracts.popFrameProvider` is either `Popups` or `Popovers` (chosen at load:
mobile/small-viewport/localStorage-forced → Popovers). Both implement: `addTarget`,
`newPopup/newPopover`, title bars, loading states, `setPopFrameContent`,
`containingPopFrame`. Every pop-frame gets a **shadow DOM** content document
(`popups.js:312-337`) with site stylesheets re-injected — style isolation with native look.

| | Popups (desktop, 2719 lines) | Popovers (mobile, 733 lines) |
|--|--|--|
| Trigger | hover (750ms delay), cancel on click/scroll | tap |
| Placement | float in `#popup-container`, z-index stack | injected into document flow, stacked sheets |
| Chrome | pin, zoom/tile submenu, minimize, collapse, resize, drag | close, stack counter, "open in new tab" |
| History | none | pushState; hash encodes open stack `;id1:id2` |
| Escape | unpin, else despawn | pop top of stack |

### Desktop WM vocabulary (popups.js)

- **Pin/unpin** — pinned popups detach from the hover lifecycle and survive; unpinning
  re-attaches to the spawning target. Alt+pin acts on all unminimized popups.

  **The TNT test — passed.** `pinPopup` (`popups.js:1083-1098`) is a class swap on the
  same DOM element: same frame, same titlebar, no reparent, no rewrap, no resize. Only
  ownership changes (leaves parent `popupStack`, detaches from spawning target). This is
  exactly Don's TNT OPEN LOOK pin-up menu architecture — menu frames as a subclass of
  window frames, promotion by flag — and NOT the olwm/ICCCM anti-pattern where the WM
  lives in a separate process with no shared class hierarchy, forcing a visible
  rewrap-move-resize dance when a menu becomes a window. Gwern gets this right for the
  same reason TNT did: one codebase owns both the transient thing and the window manager.

  Two real transient/persistent separations remain, and those are the anti-inherits:
  (1) **mortality on navigation** — pinned popups survive mouseleave but not page
  navigation; pin promotes for the page visit, not onto a persistent desk; and
  (2) **the provider split** — Popups vs Popovers is two windowing engines by device
  class, not one window class with adaptive chrome.

  Aesthetic gap, confirmed: the pin button is an icon/tooltip swap
  (`popups.js:1472-1475`); no OPEN LOOK push-in rotation. The rotating pin wasn't
  decoration — it was the affordance that taught the promotion semantic.
- **Collapse** — titlebar-only (window shade). Distinct from **minimize** — docked to
  screen bottom in horizontal/vertical arrangements.
- **Resize** — pinned only; edge/corner hit-testing with per-region cursors.
- **Stacks** — each popup carries a `popupStack` shared with descendants spawned from links
  inside it: parent/child window groups, lightweight MDI. Spawning despawns non-pinned
  popups outside the new stack.
- **Tiling** — `zoomPopup(place)` snaps focused popup to
  `top-left|top|top-right|left|full|right|bottom-left|bottom|bottom-right`. Snap-maximize,
  not a tiling WM, but a real screen-region vocabulary.

### Keyboard tiling map

Configurable keystring, default `"aswdqexzfrcvtgb"`, persisted in localStorage
(`popups.js:907-911`):

| Keys | Action |
|------|--------|
| `a s w d` | tile left/bottom/top/right half |
| `q e x z` | quarters |
| `f` / `r` | maximize / restore |
| `c` / `v` / `t` | pin / collapse / minimize |
| `g` / `b` | pin + bring backmost forward / send focused back |
| Esc | unpin, else despawn |

Help (`?`) and Search (`/`) themselves spawn as pop-frames via `GW.popFrameSpawnWidgets` —
documentation is just another window.

## Extracts: the target-type registry

A **target** is an eligible `a[href]` in the body/TOC/navbar. `Extracts.targetTypeDefinitions`
(`extracts.js:314-348`) is an ordered list of
`[typeName, predicate, targetClasses, fillFunction, popFrameClasses]` — first match wins:

`ANNOTATION`, `ANNOTATION_PARTIAL`, `LOCAL_PAGE` (same-site pages/sections), `FOOTNOTE`,
citation-context, `LOCAL_IMAGE/VIDEO/AUDIO/DOCUMENT/CODE`, `REMOTE_IMAGE/VIDEO`
(YouTube/Vimeo), `CONTENT_TRANSFORM` (Wikipedia, tweets, GitHub issues), `FOREIGN_SITE`
(live iframes for whitelisted domains), `AUXILIARY_LINK`, `DROPCAP_INFO`.

Fill functions don't build DOM directly — they synthesize **include-links** and let
Transclude + Content/Annotations load asynchronously. Recursive popups resolve pathnames
against already-open pop-frame shadow documents.

**Webtop mapping:** this registry is "what opens in a window" as declarative data — the
same role our advertisements/K-lines play. A MOOLLM webtop target registry would add:
room (directory), character (CHARACTER.yml), skill (CARD.yml), simulation (wasm canvas).

## Transclude: include-links as IR

`<a class="include" href="…">` is replaced at runtime by fetched, sliced, templated
content. Options as classes: `include-strict` (eager), `include-lazy`, `include-annotation`
vs `include-content`, `include-unwrap`, `include-block-context`, `data-include-selector`,
`data-include-template`. Lazy loading via IntersectionObserver against the nearest scroll
container (page or pop-frame); collapsed regions gate loading.

Templates are a tiny DSL (`<{var}>`, `<[IF x]>…<[IFEND]>`) compiled from
`template/include/*.tmpl` into `transclude-templates-GENERATED.js`.

Page footers use the same mechanism: backlinks, similar-links, and link-bibliographies are
include-links into `/metadata/annotation/…` fragments — the page assembles itself.

## Content and annotation loaders

`content.js` keys 15 content types (`localPage`, `wikipediaEntry`, `githubIssue`, `tweet`,
`localCodeFile`, `remoteVideo`, …) each with fetch + parse + cache; same-page content clones
from the live DOM with no network. `annotations.js` fetches
`/metadata/annotation/<encoded-url>.html` fragments and parses them into reference data for
templates. Everything announces itself on the event bus (`Content.contentDidLoad`, etc.).

## The event bus: GW.notificationCenter

`initial.js:254+`. Pub/sub with **phase-ordered handlers**: content processing registers
into named phases (`transclude → rewrite → eventListeners`) so DOM injected later (popup
bodies, transcluded blocks) flows through the identical pipeline as the initial page.
Key events: `GW.contentDidLoad/contentDidInject`, `Popups.popupDidSpawn`,
`Collapse.collapseStateDidChange`, `Layout.layoutProcessorDidComplete`,
`DarkMode.didSetMode`.

This is the mechanism that makes windows-spawning-windows tractable — the exact problem a
webtop multiplies.

## Sidenotes: margin as UI surface

`sidenotes.js` moves footnotes into margin columns at viewport ≥ 1761px. Layout is a real
geometric packer: build "proscribed vertical ranges" from full-width figures/tables
intersecting the columns → derive free cells → assign notes to cells near their citations →
pack with fixed spacing; overflow notes get scrollbars; total failure falls back to
footnotes (log line: `TOO MUCH SIDENOTES. GIVING UP`). Re-runs on resize/collapse/inject
via requestIdleCallback coalescing.

## Everything else, briefly

`rewrite.js` (4803 lines) is the post-load transformation suite: tables sortable, figures
thumbnailed, TOC built, link icons attached, footnote helpers, copy processors.
`layout.js` classifies paragraphs (first/last graf, dropcap eligibility, spacing
multipliers) — content-aware typesetting, not window layout. `collapse.js` is page-level
disclosure with deep-link auto-expansion and an "iceberg" progress indicator.
`reader-mode.js` masks link decoration until Alt is held. `dark-mode.js` toggles
auto/light/dark with selective image inversion.

## Inheritance verdict

Steal the **architecture**, not the code: (1) pop-frame interface separate from window
chrome providers; (2) declarative target-type registry; (3) include-link IR so windows and
pages share one content path; (4) phased event bus; (5) tiling keystring + pin/collapse/
minimize as the minimum desktop vocabulary. Skip: Hyphenopoly, paper-marble, seasonal
flourishes, tablesorter (unless needed).

↑ [ARCHITECTURE.md](ARCHITECTURE.md)
