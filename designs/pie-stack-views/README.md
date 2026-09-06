# Pie Stack Views: reselection, overlays, and the Atkinstown stack

**Status:** Design (active)
**Date:** 2026-08-28
**Author:** Don Hopkins

One design cluster covering the constructive program behind [DYE-A-TRIBE](../DYE-A-TRIBE.md): what pie menus inherit from, lack from, and add to direct manipulation; the sparse view overlay data model; views as testimony and argument; the HyperCard-shaped center stack; and zoom in space, meaning, and time.

## Reading order

| Doc | What |
|-----|------|
| [RESELECTION.md](RESELECTION.md) | The foundation: reversibility as reselection; the inherit/lack/add property analysis vs. Shneiderman; tracking hooks and dwell timing (Selker; shipped in OpenLaszlo/OLPC Micropolis); feedback in the center and in the world; designer-editable configuration |
| [PIE-MENU-MEMORY-PALACES.md](PIE-MENU-MEMORY-PALACES.md) | The menu promoted to object of interest: rooms kissed together edge to edge; DreamScape (ScriptX), MediaGraph (Unity/SFC), iLoci (iPhone); aimable, interruptible kinetic navigation |
| [SPARSE-VIEW-OVERLAYS.md](SPARSE-VIEW-OVERLAYS.md) | The data model: view-configuration trees over graphs; open-as-selector and path promotion (GitHub collapse, OpenLaszlo proxy slots); constraint inheritance with an escalating guardrail spectrum; projection as a dialable parameter; simplicial folding geometry; doorways and serendipity |
| [VIEWS-AS-TESTIMONY.md](VIEWS-AS-TESTIMONY.md) | The social layer: views as opinions; scale as testimony with media queries; argument by interpolation; the Korz connection; StoryMaker / Urban Safari / eBike Safari tours; PSIBER peripheral views; visible clipboards and Factorio conveyors — views of what passes through, dataflow spreadsheet over the overlay tree, *Save as PDF* as a factory feeding a document assembly line |
| [VIEW-STATE-ANCESTORS.md](VIEW-STATE-ANCESTORS.md) | The lineage and the record format: OPML 2.0 `expansionState` as a shipped receipt (and its line-number flaw); Engelbart's viewspecs; Bush's trails; vertical transclusion after gwern's Xanadu reading; DreamScape turning the browser URL and return stack into an editable tree; Wave's ownership and crediting failures; the `view:` YAML record, `collapsed_deliberately`, and reply-with-a-view |
| [PERIPHERAL-VIEWS.md](PERIPHERAL-VIEWS.md) | The 1989 ancestor in depth: PSIBER's peripheral controls; view parameters that are themselves editable objects; editable widget behavior; the definition editor resolving one name to every binding; the canvas minimap; view characteristics with a legibility floor of 1; the PSV typed glyph vocabulary; and homoiconicity as the enabling condition, with the NeWS debugger dict as the case — plus the honest gap for YAML |
| [THE-TOWER.md](THE-TOWER.md) | The pyramid as a building: cards carrying both lateral and `up`/`down` links; the lane as a 1D CA neighborhood (`w3…center…e3`); the signed vertical axis (up is how it presents, down is what holds it up); the crown as glyph rung and the skyline as contact sheet; typed connectors; the underground embassy tunnel; the three-file fractal; *Manufacturing Intelligence* as a name with many bindings; and the memory palace that was wired in only one direction |
| [PUMPING-UP-PIE-MENUS.md](PUMPING-UP-PIE-MENUS.md) | Semantic zooming (Pad → Pad++ → Jazz/Piccolo); distance as appetite; Amsterdam rising around de Dam; the public square and NOMODES; the **Atkinstown stack** (stack ⇔ menu, background ⇔ slice, card ⇔ item); the Dasher pivot |
| [GROOVES-AND-SPIKES.md](GROOVES-AND-SPIKES.md) | **A geometry manager, not a window manager** — the window frame is a boundary between two incompatible layout systems and nothing about geometry justifies it; a **tab was always a constraint** (an object on the window perimeter, a groove that shipped in 1990 without the vocabulary). A **groove** is a 1-D manifold that unifies docking, layout, and constraint; the **spike** is the ordered case, shipped in PSIBER 1989. Inference promotes to declaration, so constraints get made by accident and kept. Sketchpad-class power with its failure named — over-constraint is invisible, so show residual degrees of freedom and name the constraint that refused a drag. Cartoon physics with ARK's literalism-versus-magic lesson and determinism as the tool/toy line; Morphic as the warning against uniformity without types; Cassowary as the answer to the performance objection |
| [RADIAL-DIMENSIONS.md](RADIAL-DIMENSIONS.md) | The **Precision Pie** documented from the demo — poke out to snapshot a coarse angle, then a floppy lever anchored there grows *more* flexible the further out you go, because plain leverage runs out of screen exactly when you need the last few units. Eyeball, then dial. Generalizes to the rule the resize doc got wrong: radius has **one meaning per level, and the anchor is where it rebinds**, so nested pies can alternate leverage, scope, appetite and fine adjustment in one stroke — which makes a gesture an **argument list** rather than a selection. Plus a visual verb per dimension (extension, bending, fanning, accretion, notches), the rule that previews render in the substrate the dimension acts on, and why bending scales where extension cannot |
| [WINDOW-RESIZE-PIE.md](WINDOW-RESIZE-PIE.md) | The worked operational pie: eight items for four edges and four corners in the directions they live; acquisition and Buxton's **nulling problem** as two separate failures of a resize handle, fixed by direction-selects and displacement-manipulates; **radius as scope**, quantized as hops in the seam-adjacency graph, recruiting neighbors that are near enough rather than touching and preserving their gaps instead of snapping; the three colliding meanings of radial distance; and the untested seam of what locks the scope |
| [FRICTION-FIELDS.md](FRICTION-FIELDS.md) | **The transfer function is a landscape, not a curve.** Walls, grooves, detents, damping strips and drunken spaces are one field distinguished by where it has support and which derivative it acts on. Threshold is a function of **direction**, so the family includes traps, guard rails and one-way ratchets, and a hard wall is just a detent at infinity. Don's **velocity credit** dissolves the discard-versus-lurch tradeoff by repaying consumed motion as a decaying impulse — an invisible spring that pumps you out the far side — putting the three policies at three derivative orders, with restitution as the knob and a ratchet-plus-gain-above-one as the runaway hazard. Thickness, threshold and *visual* thickness are three independent axes, which forces the rule **render the state, not the geometry**. Perlin terrain is the area-support case, learnable when seeded and position-locked, drunkenness when re-rolled |
| [TEMPORAL-SEMANTIC-ZOOM.md](TEMPORAL-SEMANTIC-ZOOM.md) | Zoom keyed to time: wow tags; MediaFlow (Marc Davis, Interval) and MediaGraph time warping; *one joke per five seconds*; the eBike Safari playback case and the signals/conditioning/bindings API; natural-language warps via the adventure-compiler pattern |

## One-line thesis

**Reselection — browsing a decision before committing — generalizes from a pie menu highlight to view overlays, saved perspectives, interpolated arguments, and time-warped playback; the whole stack stays designer-editable declarative data.**

## Relations

### Within moollm designs

- [DYE-A-TRIBE.md](../DYE-A-TRIBE.md) — the critique these designs answer
- [webtop-gwern-inheritance/](../webtop-gwern-inheritance/README.md) — the webtop shell these components live in; [MEMORY-PALACE-PIE-MENUS.md](../webtop-gwern-inheritance/MEMORY-PALACE-PIE-MENUS.md) (rooms/doors/parameter entry) and [K-PYRAMID-ATTENTION-MAPS.md](../webtop-gwern-inheritance/K-PYRAMID-ATTENTION-MAPS.md) (saved shareable attention — the sibling of views-as-testimony)
- [KORZ-LLM-EVALS.md](../KORZ-LLM-EVALS.md) and [KORZ-PRIME](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime.md) — subjectivity as dispatch; views as dispatch coordinates
- [object-system/](../object-system/) — directory-as-object, advertisements

### Implementations

- [MicropolisCore `PieMenu.svelte`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/micropolis/src/lib/PieMenu.svelte) — current Svelte port (dwell timing not yet restored)
- [micropolis `piemenu.lzx`](https://github.com/SimHacker/micropolis/blob/master/laszlo/micropolis/classes/piemenu.lzx) — OpenLaszlo, with per-item `enterTime`/`exitTime`/`totalTime`
- [micropolis `piemenu.py`](https://github.com/SimHacker/micropolis/blob/master/MicropolisCore/src/pyMicropolis/piemenu/piemenu.py) — OLPC Python/GTK/Cairo twin
- [WWSFF eBike Safari](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/ebike-safari) — the geolocated story-and-travel graph

### Narrative origin

The essays were drafted in Don's-voice form alongside the Dye-a-Tribe critique in Don's archive; these are the public design versions. The critique itself is indexed at [DYE-A-TRIBE.md](../DYE-A-TRIBE.md).
