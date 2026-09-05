# Gwern: the publishing engine

gwern.net is the most complete working answer to "what should a long-lived personal corpus look
like on the web," and it was built by two people over fifteen years with no funding, no cult, and no
courses. It is the reference implementation this hub inherits from.

## What is here

- [**`NENEX.md`**](NENEX.md) — his 2026 proposal for a **neural personal wiki**: the wiki as an
  append-only log of *edits*, a local model continuously finetuned to imitate your editing, actions
  serialized as Lisp s-expressions, semantic constraint propagation to find pages your latest edit
  made wrong, and daemon personas that critique. The engine half of the webtop, with a Twitch-style
  chat pane where its interface should be.

## Where the founding study lives

Kept at its original URL because it has been shared publicly:
[**`../../webtop-gwern-inheritance/`**](../../webtop-gwern-inheritance/)

| File | What it is |
|---|---|
| [GWERN-WHAT-TO-INHERIT.md](../../webtop-gwern-inheritance/GWERN-WHAT-TO-INHERIT.md) | The extraction: what gwern.net does that we should take |
| [MOOLLM-WEBTOP-VISION.md](../../webtop-gwern-inheritance/MOOLLM-WEBTOP-VISION.md) | What it becomes as a webtop |
| [K-PYRAMID-ATTENTION-MAPS.md](../../webtop-gwern-inheritance/K-PYRAMID-ATTENTION-MAPS.md) | The semantic pyramid worked out |
| [MEMORY-PALACE-PIE-MENUS.md](../../webtop-gwern-inheritance/MEMORY-PALACE-PIE-MENUS.md) | Rooms, gestures, spatial memory |
| [REVERSE-OVER-ENGINEERING.md](../../webtop-gwern-inheritance/REVERSE-OVER-ENGINEERING.md) | The method: over-engineer backwards from the artifact |
| [ANALYSIS-WORKFLOW.md](../../webtop-gwern-inheritance/ANALYSIS-WORKFLOW.md) | How the study was conducted |
| [TEMKIN-CALL-2026-08-05.md](../../webtop-gwern-inheritance/TEMKIN-CALL-2026-08-05.md) | Call notes where these threads first met |
| [MAURICE-BACK-ROOM.md](../../webtop-gwern-inheritance/MAURICE-BACK-ROOM.md) | Back room notes |
| [sources/](../../webtop-gwern-inheritance/sources/) | Harvested primary material |

Character room, for the show:
[`characters/gwern/`](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/gwern)
— portrayed under the pen name only, no speculation about identity, location, or appearance.

## The three things worth restating

**The ladder.** From [gwern.net/xanadu](https://gwern.net/xanadu), on where Xanadu's interface went
wrong: transclusion *"should have been 'vertical' with popups, and 'zooming in' and 'zooming out' at
different levels of abstraction (link-icon → title → abstract → section etc.)"* — the spine of this
whole hub.

**The footnote that unblocked it.** Outliners never caught on for hypertext because they *"wind up
foisting too much work on the author"* — but LLMs can *"automatically summariz[e]/expand[] to build a
full hierarchy while the human author writes just what is necessary."* The author writes one rung;
the machine generates the rest on demand.

**The pin test.** gwern.net's popups can be pinned, and the implementation is a class flag on the
same window object rather than a separate pinned-window type — architecturally the same decision Don
made for TNT OPEN LOOK pin-up menus, arrived at independently about thirty years apart. Convergence
on the same answer by two people who never discussed it is the strongest evidence available that
**a popup is a window**, and should be a real one from the start.

## What we add — under his own principle

The design doc's miscellaneous principles include **"give the reader agency"**, in the cluster under
`reader > author`. Everything in this section is that line carried further than gwern carried it, not
a foreign agenda: he named the principle and implemented the reading half of it.

Five affordances gwern.net has none of, each with machinery already in MOOLLM: **playability**
(actions whose consequence is a tracked diff), **explorability** (a place with altitude and unvisited
exits, not a link graph), **inventory** (`TAKE REF` carries a weightless pointer — transclusion as a
game verb), **multi-userness** (other readers' paths as content, agents as inhabitants rather than a
chat pane), and **persistent reading cursors** (a position that is an object you can keep, name, and
hand to someone). The mechanism is that an article *is* a room: one directory exporting the document
interface and the ROOM interface simultaneously, no rewrite. See
[PLAYABLE-CORPUS.md](../PLAYABLE-CORPUS.md).

**The fourth thing worth restating, and it is a receipt.** gwern.net's `demo-mode` keeps a per-reader
model in LocalStorage — use-counts per site feature, so the theme-switcher hint stops animating after
*n* visits. It is a static site with no backend and no account, and it already carries durable
per-reader state. That state has never been pointed at *where you were reading*: dark mode and reader
mode persist, and your place in the argument does not. The mechanism is built and aimed at the
furniture. See [READING-CURSORS.md](../READING-CURSORS.md).

## The ornament rule, which is an order of operations

Two adjacent principles from the design doc do more work than they look like:

> you must earn your ornaments — if you go overboard on minimalism, you may barely be mediocre

> visual differences should be semantic differences

The footnote spells out the sequencing: *"One earns the right to add 'extraneous' details by first
putting in the hard work of removing the actual extraneous details; only after the ground has been
cleared — the 'data-ink ratio' maximized, the 'chartjunk' removed — can one see what is actually
beautiful to add."*

**Removal is the prerequisite, not the product.** Data-ink is a *ratio*, and the common failure is
driving the denominator to zero and calling it finished. gwern says so directly — *"many 'minimalist'
designs proud of their simplicity are merely simple-minded"*, and Rams' "as little design as
possible" fails when *"designers focus on the first part, and forget the second part."* A minimalism
that cannot hold more than a few paragraphs and a hero image *"has not solved the design problem, and
is merely a sub-genre of illustration."*

This connects to the returns-to-design parabola in the same document, and that is the sharp version:
**minimalism-as-ideology delivers you to the middle of the sigmoid and then confiscates the
vocabulary for the spike.** "Barely mediocre" is not a slur, it is a position on his own curve — the
region where nothing is broken, nothing is noticed, and there is no move left that the style permits.

The second principle is the diagnostic for the flat-design era specifically, and it fails in the
*converse* direction: a borderless button makes a **semantic** difference (tappable versus inert)
carry **no visual** difference. That is not ornament removal, it is the deletion of the interface's
syntax, and it is the direct-manipulation regression Shneiderman's whole position predicts — visible
objects with visible actions is the requirement, and the objects went invisible while the actions
stayed. Ornament added later without clearing that up is the same error inverted: unearned.

Inherited here as a lint with an order, not a taste: strip first, and no decorative element exists
until the removal pass is clean — then what you add is legible against the cleared ground. MOOLLM's
own `no-decorative-comments` rule stated only the first half until this was noticed; the earning
clause is now attached to it in `.cursorrules`.

## What we do not inherit

The static-site build. gwern.net compiles Markdown to HTML with popups layered on; the webtop treats
the page as a live object in a window manager, with the shell — tabs, stacks, pie menus, rooms — as
first-class rather than as progressive enhancement. Gwern's discipline about **degrading to plain
readable HTML** is inherited absolutely; his choice of the document as the top-level unit is not.

↑ [webtop hub](../README.md) · [temkin](../temkin/) · [winer](../winer/) · [hyperties](../hyperties/) · [objections](../OBJECTIONS.md)
