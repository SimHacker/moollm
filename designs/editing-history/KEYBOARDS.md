# The keys are not the model

Periodically somebody proposes dedicated Copy and Paste keys. The history says the keys are
orthogonal to the thing that is broken. Two traditions spent their key budget in opposite ways, and
**the one that shipped dedicated Copy and Paste keys is the one with the invisible clipboard, while
the one with no editing keys at all is the one that never lost a clipping.**

| Tradition | Keys spent on | Transfer model | History kept |
|-----------|---------------|----------------|--------------|
| NLS, Alto | chord keyset (5 keys, separate device) | selection to destination | no |
| Xerox Star, ViewPoint | **verbs**: MOVE, COPY, AGAIN, UNDO, PROPS | selection to destination, no buffer | multi-level undo |
| Sun | **verbs**: Copy, Paste, Cut, Undo, Again, Props, Find | invisible clipboard | no |
| MIT Knight, Space Cadet, Symbolics | **modifiers**: Control, Meta, Super, Hyper, Top, Greek | editor's kill ring | every kill, in a ring |

Read the last two rows together. Sun had the dedicated keys and no history. The Lisp Machine had no
dedicated editing keys whatsoever and kept everything.

## NLS and Alto: a separate chord device

Engelbart's NLS and the Alto used a five-key **chord keyset** as a second input device alongside the
keyboard and mouse: left hand chords a command, right hand points. Not verb keys, not modifiers -- a
whole extra keyboard for the operation half of a two-handed gesture.

kps put the succession precisely on HN:

https://news.ycombinator.com/item?id=31740860

kps> The left function cluster replaced the chord set of Engelbart's NLS and the Alto, while retaining the same two-handed style of operation: mouse on the right to select the object, keys on the left to select the operation.

## Xerox Star, 1981: verb keys, and no clipboard to put them on

Star spent keys on **generic commands**, one key each, in a cluster under the left hand. MOVE, COPY,
DELETE, SHOW PROPERTIES, COPY PROPERTIES, AGAIN, UNDO, HELP. Noun first, then verb: select the
object, press the key, indicate the destination. The Byte article counts the hardware: "The keyboard
has 24 easy-to-understand function keys."

The keycaps and the command names are **not the same list**, and the difference is the most
interesting thing on the keyboard. COPY PROPERTIES is invoked by a key labeled **SAME**:

> You select them with the mouse. You push the MOVE, COPY, or DELETE key. You push the OPEN key to
> see their contents, the PROPERTIES key to see their properties, and the SAME key to copy their
> properties.

> You can select the object(s) to be changed, push the SAME key, then designate the object to use as
> the source. COPY PROPERTIES makes the selection look the "same" as the source.

`SAME` is named for **what the user wants to be true afterward**, not for the operation the system
performs. Select the things to fix, press SAME, point at the one that already looks right. Nothing
since has shipped a better name for that operation, and most systems make you do it with an
eyedropper, a format painter, or a right-click submenu.

Note also that `OPEN` is a key that is not in the generic-command list, and that per the same
article "(HELP and UNDO don't use a selection.)" So the eight generic commands, the 24 function keys,
and the keycap legends are three different sets, which is worth knowing before anyone claims Star was
tidier than it was.

There was no clipboard, so there was no key for one. The dedicated keys people ask for existed
**before** the mechanism that makes them regrettable.

ViewPoint carried the same model forward on the 6085.

Quotes and citations: [SOURCES.md](SOURCES.md). Longer treatment: [ONE-DIMENSIONAL.md](ONE-DIMENSIONAL.md).

## Sun, 1987 onward: Star's keys wired to the Mac's model

The Sun Type 4 keyboard put ten named function keys down the left side, and the Type 5 kept them
while dropping the L-numbers. From Sun's own product notes (800-6802-12, October 1993):

https://vtda.org/docs/computing/Sun/hardware/800-6802-12_Type5KeyboardandMouseProductNotes_RevA_Oct93.pdf

| Key | L-number |
|-----|----------|
| Stop | L1 |
| Again | L2 |
| Props | L3 |
| Undo | L4 |
| Front | L5 |
| Copy | L6 |
| Open | L7 |
| Paste | L8 |
| Find | L9 |
| Cut | L10 |

> The L-keys are no longer labeled with the L-key number on the Type 5 keyboard. They are still
> marked with their functional names (Stop, Again, etc.) and function the same.

Look at that list next to Star's. **Again** and **Props** are Star's words, not Unix words; the
lineage is not in dispute. Sun kept Star's key cluster, kept AGAIN and UNDO and PROPS, and then
replaced Star's MOVE and COPY -- selection straight to destination, nothing buffered -- with **Cut,
Copy, Paste**, which is the Macintosh model with a hidden buffer in the middle.

So the experiment has already been run, at scale, for a decade, on hundreds of thousands of
workstations: **dedicated Cut, Copy, Paste and Undo keys, in a comfortable cluster, under the left
hand.** It did not fix anything, because the keys were wired to an invisible one-slot buffer. A key
is a faster way to invoke a verb. It cannot make the verb mean something better.

The keysyms outlived the keys. `xkeyboard-config` still ships `SunCopy`, `SunPaste`, `SunCut`,
`SunAgain`, `SunProps`, `SunFront`, `SunOpen`, `SunFind` alongside `XF86Copy`, `XF86Paste` and
`XF86Cut`, so every Linux machine can still name keys almost nobody has.

### What the keys were actually wired to: three kinds of selection, two of them transient

Calling it "the Mac's model" is too kind. SunView had **more selection states than it had rendering
styles to spare**, and which one a key operated on depended on what was held down at the time. This
is all in the `textedit(1)` man page, which is the primary and is still online:

https://cmgm-new.stanford.edu/man2html/textedit.1.html

> There are two types of selections: a primary selection is indicated by video-inversion of the span
> of characters, and tends to persist. A secondary selection is indicated by underlining the span of
> characters and only exists while one of the four function keys corresponding to the commands Cut,
> Find, Paste, or Copy, is depressed.

That is the one that is hard to remember because it is barely a thing: the **secondary selection**
exists only while your finger is on the key, and the operation completes when you let go. Underlined
rather than inverted, so the two selections are visually distinguishable, which is more than the
modern clipboard manages.

Then a third state, orthogonal to both:

> In addition, a selection can be "pending-delete," as indicated by overlaying the span of characters
> with a light gray pattern. A selection is made pending-delete by holding the CTRL key while clicking
> the LEFT or MIDDLE mouse buttons. If a primary selection is pending-delete, it is only deleted when
> characters are inserted, either by type-in or by Paste or Copy. If a secondary selection is
> pending-delete, it is deleted when the function key is released, except in the case of the Find,
> which deselects the secondary selection.

Three visual renderings for selection state: **video inversion, underline, gray wash.** Two
lifetimes: persistent, and only-while-held. One modifier that changes what happens on release. And
the keys resolve their operand dynamically, which the same man page documents key by key:

| Key | Operand, per `textedit(1)` |
|-----|----------------------------|
| Copy (L6) | "either to the Clipboard or at the closest end of the secondary selection" |
| Paste (L8) | "either the secondary selection or the Clipboard" |
| Find (L9) | "in order, the secondary selection, the primary selection, or the Clipboard" |
| Cut (L10) | "either the primary or the secondary selection" |

`Find` has a **three-level fallback chain** in the keycap. Nobody holds that in their head.

Underneath, the selection service made the ranks explicit. XView's compatibility layer lists them as
`SELN_CARET`, `SELN_PRIMARY`, `SELN_SECONDARY`, `SELN_SHELF`, and `SELN_UNSPECIFIED`, where the shelf
is the clipboard and the caret is the insertion point as a selection in its own right. The
documentation for the last one states the modality outright: if you ask for `SELN_UNSPECIFIED` the
client "wants whichever of the primary or secondary selections is appropriate given the current state
of the function keys."

**The selection you get is a function of which keys are currently down.** That is five ranks, three
renderings, and a keyboard-state-dependent resolver, in a window system whose entire user-visible
promise was copy and paste.

And then it was reimplemented, repeatedly, by teams who did not agree: SunWindows and `suntools`,
SunView, NeWS, X11/NeWS, XView, OPEN LOOK, OLIT, and MoOLIT, the last of which existed to let one
binary switch between OPEN LOOK and Motif look-and-feel at runtime. Each generation carried some of
the selection semantics and dropped others. The reasonable conclusion is not that any one of these
was badly built; it is that **five ranks nobody can name is what a fifteen-year committee produces
when the thing being standardized is the wrong thing.** Compare Chapter 3 of the ICCCM, which had a
plain eight-slot ring with a rotate, in
[SELECTIONS-AND-CUT-BUFFERS.md](SELECTIONS-AND-CUT-BUFFERS.md).

## MIT: Knight, Space Cadet, Symbolics -- all modifiers, no verbs

The other tradition spent its entire key budget on **extending the alphabet** rather than naming
operations. The Knight keyboard (Tom Knight, MIT AI Lab) helped popularize **Meta**. The space-cadet
keyboard added **Super** and **Hyper**, giving four bucky bits plus Shift, Top and Greek, laid out in
rows so one hand could chord all of them while the other hand hit a key.

The full function key list on the Lisp Machine, from the manual:

https://tumbleweed.nu/r/lm-3/uv/operat.html

> ABORT, BREAK, CALL, CLEAR-INPUT, CLEAR-SCREEN, DELETE, END, HELP, HOLD-OUTPUT, LINE, MACRO,
> NETWORK, OVER-STRIKE, QUOTE, RESUME, RETURN, RUBOUT, STATUS, STOP-OUTPUT, SYSTEM, TAB, TERMINAL

The most lavishly keyed computers ever built -- APL glyphs, Greek, roman numerals, seven modifiers --
and **not one key for copy, paste, cut, undo, or again.** Those were bucky chords interpreted by
Zmacs, and what Zmacs had underneath was the **kill ring**: every kill retained, `M-y` walking back
through them. See [UNDO-TREES.md](UNDO-TREES.md).

The tradition with no editing keys is the tradition that never threw a clipping away.

## What this settles

Dedicated keys are an **invocation** question. Visible, multiple, editable, durable, shared history
is a **model** question. They are independent, and the historical record is the proof:

- Star: good model, dedicated keys, no persistence.
- Sun: bad model, dedicated keys. Keys did not help.
- Lisp Machine: good history, zero dedicated keys. Absence did not hurt.

Adding Copy and Paste keys to a laptop in 2026 would reproduce the Sun result exactly. Fix the
model, then argue about the keycaps -- and when you do, note that the pie menu is the
[paired-links](../PAIRED-LINKS.md) answer to invocation anyway, since it puts the verbs in your hand
without needing a keycap for each one.
