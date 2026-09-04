# Tree navigation — start with the tree, derive the tab

*Tab order flattens a tree into a line, which is the original error. Then in-and-out navigation gets
bolted on per widget, inconsistently, so there is no grammar to learn. The fix is to define the
structural command set first and make tab a **projection** of it.*

Related: [`winer/README.md`](winer/README.md) · [`hyperties/FOCUS-FLOW.md`](hyperties/FOCUS-FLOW.md) ·
[`hyperties/LINK-RESOLUTION.md`](hyperties/LINK-RESOLUTION.md) ·
[`../pie-stack-views/RESELECTION.md`](../pie-stack-views/RESELECTION.md) ·
[`../pie-stack-views/VIEWS-AS-TESTIMONY.md`](../pie-stack-views/VIEWS-AS-TESTIMONY.md)

## The diagnosis

Everything worth navigating is a tree. Outlines, the DOM, the filesystem, menu hierarchies, YAML,
an index of scoped namespaces, a room and its contents. **Tab order takes that tree and emits a
sequence.** The flattening is lossy in exactly the dimension that matters: level. After it, "next"
is ambiguous — next sibling, next node in document order, or first child? — and the interface picks
one silently.

Then, because the loss is intolerable in practice, in-and-out navigation gets added back
piecemeal: arrow keys inside a listbox but not between listboxes, <kbd>F6</kbd> between panes in one
app, <kbd>Ctrl</kbd>+arrow in another, <kbd>Escape</kbd> to leave a grid cell except where
<kbd>Escape</kbd> cancels the dialog. Each addition is locally reasonable. Collectively there is no
grammar, so **the user cannot learn the system, only its exceptions.** That is the crippling part —
not any single missing key, but the absence of a rule that predicts the next one.

## Start with the structural command set

Six primitives on three axes, defined on the tree, before any key is assigned:

| Axis | Commands | Notes |
|---|---|---|
| **Siblings** | `PREV-SIBLING`, `NEXT-SIBLING` | stays at level; the common case |
| **Depth** | `OUT` (to parent), `IN` (to first child) | the axis tab order destroys |
| **Extremes** | `FIRST-SIBLING`, `LAST-SIBLING`, `ROOT` | cheap, and they prevent repeat-key drumming |

Plus two that are not spatial and are usually forgotten:

- **`BACK` / `FORWARD`** — history, not position. Where you came *from* is a different question
  from where you are next to, and every deep tree needs it. This is the browser's one genuine
  contribution to tree navigation, and outliners mostly lack it.
- **`EXPAND` / `COLLAPSE`** — a first-class operation, not a display toggle, because the expansion
  state *is* document content ([OPML's `expansionState`](winer/README.md), and
  [view state as authored material](../pie-stack-views/VIEW-STATE-ANCESTORS.md)). Collapsing is
  editing the view, and the view is citable.

**Then define tab as derived.** `TAB` = *next node in flattened document order* — a depth-first walk
expressed as a single command. Keep it: it is thirty years of muscle memory and the whole assistive
technology stack depends on it. But keep it as a **projection of the tree walk, not as the model.**
Everything unpleasant about focus management follows from having it the other way around.

That inversion is the entire proposal. Once the tree walk is primary, the flattened order is a
derived view — one of several, computed rather than authored — and
[focus flow](hyperties/FOCUS-FLOW.md) can *show* it, which is how you discover that your tab order
is wrong.

## The tradition already solved keyboard/mouse parity

This is not speculative design. The outliner lineage got there and the web lost it:

**ThinkTank** (Winer, Peter Winer, Doug Baron; Apple ][) was **keyboard-driven** — structural
navigation had to be complete because there was no alternative. **MORE** (Mac, 1986) then added
*drag-and-drop rearrangement without spoiling the keyboard interface*
([winer pack](winer/README.md)). That clause is the requirement, met forty years ago: direct
manipulation was **added** to a complete keyboard command set rather than replacing it. **Frontier**
finished the argument by making the outline the syntax for code and data alike, so structural
navigation was navigation of the program.

What "not a second-class citizen" means concretely, then, is a **testable invariant**:

> Every structural operation is reachable three ways — keyboard, pie menu, and direct manipulation —
> and all three invoke the same named command.

Drag-only operations are inaccessible. Keyboard-only operations are undiscoverable. An operation
that exists in only one surface is a bug, and since the command set is enumerable, **this is a
lint** rather than a matter of taste.

## Edit mode, and why modes are usually hated

Structural navigation and text entry want the same keys. Arrow keys move the caret or move between
nodes; typing inserts characters or selects a node. So there are modes, and pretending otherwise
produces the inconsistency described above.

Modes are hated for two fixable reasons, and neither is modality itself. **They are invisible** —
which is the same sin as the [hidden clipboard](../pie-stack-views/VIEWS-AS-TESTIMONY.md): state you
cannot see and therefore cannot reason about. And **entry and exit are inconsistent** across
contexts, so the gesture that leaves a cell does something else in a dialog.

The requirements follow directly:

1. **Mode is visibly displayed**, always, at the focus — not in a distant status bar.
2. **One gesture in, one gesture out**, identical everywhere. <kbd>Enter</kbd> descends into
   editing; <kbd>Escape</kbd> returns to structure. No exceptions, including dialogs.
3. **Typing in navigate mode does something useful** rather than beeping — which is type-ahead,
   below. This is what makes the mode boundary forgiving instead of punishing.
4. **A new empty document starts in a usable state**: open it, type, and you are writing an outline.
   No mode picked, no template chosen, no widget instantiated. If the empty case needs a decision,
   the grammar is wrong.

## Type-ahead is the resolution protocol

"Full type-ahead" means typing in navigate mode selects the node you name. That is not a separate
feature — **it is name resolution over the visible subtree**, and the corpus already has the design:
candidates ranked by scope proximity, with a title and a description per candidate, presented rather
than guessed at ([LINK-RESOLUTION.md](hyperties/LINK-RESOLUTION.md)).

So type-ahead, link resolution, and method dispatch are one mechanism with three entry points. The
ranking is the same, the description pane is the same, the ambiguity-is-a-menu rule is the same, and
a chosen candidate is recordable as a synonym in all three cases. Building one builds the others,
which is the argument for doing resolution properly once.

## Pie menus at the node

The pie menu carries the structural command set at the point of focus, which solves the
discoverability problem a rich keymap otherwise creates: the commands are *visible where you are*,
with their keyboard equivalents on the labels, so the menu teaches the keyboard.

Three properties matter here specifically. **Customizable**, so a user's own operations join the
same vocabulary rather than living in a separate macro system. **Reselectable** — browse the items
before committing, per [RESELECTION.md](../pie-stack-views/RESELECTION.md) — with the description
pane populating from whatever is pre-selected. And **interruptible**, since a pie invoked mid-drag
during a subtree move has to accept being seized in flight
([PIE-MENU-MEMORY-PALACES.md](../pie-stack-views/PIE-MENU-MEMORY-PALACES.md)).

Because pie menus are customizable, the keymap is no longer universal — which means configurations
are shareable artifacts, and therefore content, and therefore forkable like everything else.

## Cut, paste, drag: all the same operation on subtrees

Moving material is one operation with three input surfaces, and the unit is a **subtree**, never a
line. Promote, demote, move-up, move-down, cut, paste, and drag are the same small set of
tree edits; drag is direct manipulation of them and the keyboard commands are the same edits named.

The clipboard this uses is the visible, addressable, editable, multi-slot one — so it holds a
**forest**, and each clipping is a subtree you can open and edit *while it sits there*, which is the
whole point of not hiding it. Paste is then a tree operation with a target and a position (as child,
as sibling, before, after) rather than an insertion point, and the ambiguity about which is resolved
by the same ranked-candidate mechanism as everything else.

## Honest costs

**Assistive technology expects the flat order.** Screen readers and browsers consume linear tab
sequence, and some already have real tree semantics (ARIA treeview roles) that must be aligned with
rather than reinvented. The derived-projection design is what makes this tractable — emit the
flattened order for AT, keep the tree as the model — but it has to be emitted correctly, and that is
work, not a footnote.

**A rich keymap is undiscoverable on its own.** The pie menu is not a nicety here; it is the only
thing that makes the command set learnable. Ship them together or the keyboard layer is dead weight.

**Modes will still be resented** by anyone who has been burned, and the visible-state requirement is
easy to under-build. A mode indicator that is subtle enough to look elegant is a mode indicator that
does not work.

**Customizable keymaps fragment the shared vocabulary.** The upside is shareable configurations; the
downside is that documentation and muscle memory diverge per user, and "press Enter" stops being
advice. Defaults have to be good enough that most people never leave them.

**Tab compatibility constrains the tree walk.** Existing pages have focus orders authored by hand
and by accident; a correct tree walk will disagree with them, visibly. That is the lint
[focus flow](hyperties/FOCUS-FLOW.md) provides and also the migration cost it exposes.

## Status

Design. The primitives and the three-surface invariant are specifiable now and testable as a lint.
The resolution machinery type-ahead needs is specified in
[LINK-RESOLUTION.md](hyperties/LINK-RESOLUTION.md); the clipboard it needs is in
[VIEWS-AS-TESTIMONY.md](../pie-stack-views/VIEWS-AS-TESTIMONY.md); the visualization that audits it
is [FOCUS-FLOW.md](hyperties/FOCUS-FLOW.md). What is missing is a reference implementation, and the
honest target is the one Frontier hit: open an empty document, start typing, and have an outline.

↑ [webtop hub](README.md)
