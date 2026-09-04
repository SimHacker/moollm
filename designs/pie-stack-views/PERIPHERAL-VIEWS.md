# Peripheral Views

*Don Hopkins · September 2026*

**Thesis:** The overlay model was built and shipped in 1989. PSIBER's peripheral views — editors and computed views attached *beside* an object rather than contained in it — are the direct ancestor of the sparse view overlay, and they worked because PostScript is homoiconic: the browser that displays data displays code, so a view can be executable structure. Naming the enabling condition matters, because the webtop does not inherit it for free.

Part of the **pie-stack-views** design cluster ([README](README.md)). The data model this is the ancestor of: [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md). The social layer: [Views as Testimony](VIEWS-AS-TESTIMONY.md).

---

## What a peripheral view is

*The Shape of PSIBER Space* (1989) calls them peripheral controls: associated views attached to an object but not contained within it — editor buttons, computed views, related objects — living in the view tree and visually distinct from the data they operate on. The separation does the same work the pie menu's figure-ground separation does one level down ([Reselection](RESELECTION.md)): commentary must read as commentary, not as part of the thing commented on.

Four instances from the paper are worth quoting, because each one is a property the overlay model later generalized.

**The view parameters are themselves objects with views.** The step editor increments by a parameter Step, the shift editor multiplies by Shift, and those parameters *"appear in the peripheral views as normal editable numbers, to which you can attach other numeric editors, nested as deep as you like."* The overlay is reflexive at the widget level: there is no privileged configuration layer, because configuration is just more data with more views on it.

**The widget's behavior is editable data.** The boolean editor has a `Random` button, and *"since the button functions are just normal data, you can open up the `Random` button and edit the probability embedded in the function `{random 0.5 lt}`."* HyperCard's browse/edit toggle, applied to the control itself rather than to the document.

**The definition editor resolves a name to all of its meanings at once** — *"editable references to every definition of the name on the dictionary stack (or in the context to which the enclosing class editor is attached)."* One name, every binding, in scope order, all editable. This is the answer to name collision as a *scoped view* rather than a dialog, and it is the right shape for any name with several live readings.

**The canvas editor is a live minimap.** It *"gives you a graphical view of the canvas's relation to its parent, and an array of the canvas's children. You can grab the graphical view of the canvas with the mouse and move the canvas itself around"* — and canvas views can be attached to the children too, recursively. A window's icon inside its parent, draggable, moving the real thing.

## View characteristics: viewspecs with a legibility floor

The section immediately before it, *View Characteristics*, is Engelbart's viewspecs made per-subtree: point size plus a **shrink factor** applied as structure gets deeper, elements drawn either to the right of the label or indented below it, and the rule worth stealing outright — *"the point size is not allowed to shrink smaller than 1, so that labels will never have zero area, and it will always be possible to select them with the mouse."* A legibility floor is what makes aggressive semantic zoom safe: nothing can shrink to unclickability.

Crucially: *"Any of the view characteristics can be set for a whole window, or for any nested object and its children within that window."* That is precisely the inheritance-with-override rule in [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — *my scale is 80% of my parent's* — implemented forty years earlier, and the min/max guardrail spectrum described there has its first term already present as the floor of 1.

## The glyph rung, already typed

The **Pseudo Scientific Visualizer** in the same paper carries the smallest rung: a fisheye that draws *"arbitrarily large, arbitrarily deep structures, in a fixed amount of space,"* with a depth limit changeable **while the drawing is in progress**, and a hand-designed typed glyph vocabulary — array as a circle, dictionary as a circle with a dot, name as a triangle, boolean as a peace sign or an international no sign, event as an envelope, process as a Porsche, and a string as *a line whose length depends on the length of the string*.

That last one is a glyph encoding a scalar, which is more than most glyph schemes attempt. The vocabulary got the design principles right: a small closed set, typed rather than per-instance, one dimension carrying real magnitude, and jokes where jokes aid memory. Finished nodes became round transparent canvases that highlight on hover and offer, on click, exactly the routing choice this cluster keeps rediscovering — zoom in, pop up a description, open another view, or push it on the stack.

## Homoiconicity is what made it possible

All four peripheral-view examples share one enabling condition. PostScript is homoiconic: an executable array *is* an array, with no quoting distinction between a procedure and a list, so the same browser that displays data displays code and the same editor that edits data edits code. Views are data; data is code; therefore a view can be executable structure. The overlay is not a feature built on top of the data browser — it falls out of the data browser being applied to itself.

The paper demonstrates it in a section titled *Using Dictionaries as Command Pallets*:

> A PostScript dictionary can be used as a pallet of commands, by defining a bunch of useful functions in a dictionary, opening it up, and executing the functions with the mouse. You can open up the functions to see their instructions, and even edit them!

That works because of one line in the click handler — *"Another useful Adjust handler simply executes the object that was clicked on. This can be used to make buttons out of executable names, arrays, and strings."* A button is not a widget class; a button is an executable object plus a handler that runs whatever it lands on.

The load-bearing case is the debugger. The NeWS debugger was a PostScript program distributed with NeWS, written for `psh` from a terminal emulator, and *"notorious for being difficult to use, but quite powerful."* What the deck added was not a rewrite but a **dict**: the debugger's commands plus additional ones, opened as a pallet, clickable, and openable to read and edit each command's own code. In the paper's words it *"is much nicer in conjunction with the graphical stack, the object display, and a pallet of handy debugging commands, that you can invoke with the mouse."* A user interface for a debugger, delivered as a data structure. And then, inevitably: *"Using the deck to debug itself is an interesting experience."*

## The honest gap

Reflection is not sufficient for this; homoiconicity is what you need. JavaScript has functions as objects and `toString`, but a closure's captured environment is invisible and its source returns as *text* rather than as editable structure — so you can display a handler and still not open it up and edit the `0.5` inside it the way the `Random` button allowed.

MOOLLM does not have PostScript. It has YAML jazz, the filesystem, and an LLM as the interpreter — and the gap is real but narrower than "YAML merely describes behavior," which is how this was first put here and is too pessimistic. A declared value in YAML is as openable and editable as a PostScript procedure, and additionally diffable, reviewable and blamed. The gap opens only where behavior is *delegated to judgment* instead of declared, and its precise location is not code-versus-data at all: PostScript's **environment** was also data — the dictionary stack — which is what made the definition editor possible, and an LLM's weights and assembled context are not in the repository. Full analysis, including what can be recovered and what cannot, in [Homoiconicity, and whether MOOLLM has it](../object-system/HOMOICONICITY.md). Where the property is partly recovered is that the interpreter reads the same tree the human does, so a command, its documentation, and its invocation record are one object at three rungs — but that is the semantic pyramid, not homoiconicity, and the two should not be conflated. The escalating guardrail spectrum in [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) is the practical compromise: declarative data where it suffices, expressions where it does not, natural language compiled down at the top of the ladder.

## Sources

Most of PSIBER is already public and tracked; the figures are the part at risk.

| What | Where | State |
|---|---|---|
| Paper source (troff `-me`) | WWSFF `characters/don-hopkins/code/psiber/cyber/paper.me`, `.nr` | tracked, public |
| The PostScript implementation | same tree, 126 tracked files | tracked, public |
| `advent.map`, `arpa.map` | same tree | tracked, public — the data behind Figures 9 and 10 |
| Figure PostScript, `1-2.ps.Z` … `10.ps.Z` | `lloooomm-imports/news-tape/documents/psiber/` | **unversioned** |
| `tmac.e`, `Makefile`, `README` (to rebuild the paper) | same dir | **unversioned** |
| Scanned paper, figures rendered, 3.7 MB | `lloooomm-imports/ties/scans/PSIBER.pdf` | **unversioned** |

The figures are the part that shows the peripheral views working: Figure 6 is the digit, step, shift, boolean and canvas editors; Figure 7 is a class editor with scroller and name editors attached; Figure 8 is a Pseudo Scientific visualization of the NeWS `rootmenu` instance dictionary; Figure 9 is two views of a map of the ARPAnet; Figure 10 is two views of a map of Adventure. Because `advent.map` and `arpa.map` survived in the public repo, those two visualizations are reproducible even if the rendered figures are lost.

**Caution.** The `lloooomm` trees also contain *synthetic* PSIBER material — `psiber_overlay_ui.svg`, `psiber_space_deck_viz.svg`, `don-hopkins-psiber-space-deck.yml` and similar. Those are generated LLOOOOMM artifacts, not 1989 primary source, and must not be cited as history or mistaken for the real figures. Anyone rescuing files by filename will hit them first.

---

## Related

- [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — the model this is the ancestor of
- [Views as Testimony](VIEWS-AS-TESTIMONY.md) — the social layer; peripheral views as clipboards and conveyors
- [View State Ancestors](VIEW-STATE-ANCESTORS.md) — Engelbart's viewspecs, Bush's trails, OPML's `expansionState`
- [Reselection](RESELECTION.md) — figure-ground separation one level down
- [The Tower](THE-TOWER.md) — the pyramid as a building; the definition editor applied to a name with many readings
- [*The Shape of PSIBER Space*, 1989](https://donhopkins.com/home/catalog/psiber/data.html)
- [GLYPH-BENCHMARK](../webtop/GLYPH-BENCHMARK.md) — the glyph rung as an evaluation, with PSV as prior art
