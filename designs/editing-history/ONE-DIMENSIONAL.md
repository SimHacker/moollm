# The line that forgets

Every shipped editing history is a **line**. You can walk backward along it and you can walk
forward along it, and the moment you step sideways it forgets everything ahead of where you stand.
Both halves of the mechanism have this shape: the clipboard is a line one item long, and the undo
stack is a line that truncates on divergence.

The five failure modes, which recur in every system below:

| Failure | What it means |
|---------|---------------|
| **One-dimensional** | A sequence, not a tree. There is one way back and one way forward. |
| **Breakable** | Diverge from the line and the rest of the line is discarded. |
| **Forgettable** | Dies with the process, the logout, or the phone call. |
| **Invisible** | No representation on screen. You cannot point at your own history. |
| **Solitary** | One user, one machine, no review, no provenance, no discussion. |

## Xerox Star, 1981: the dedicated keys already shipped

Star is the honest ancestor, and it matters here because it **already had the dedicated hardware
keys** that people periodically wish Apple would add. MOVE, COPY, DELETE, SHOW PROPERTIES, COPY
PROPERTIES, AGAIN, UNDO, HELP, each with a key devoted to it on the keyboard, in the left function
cluster where Engelbart's NLS and the Alto had a chord set.

And the model under those keys was **better than the clipboard**, because there was no clipboard.
Star was noun-verb: select the object, press MOVE, indicate the destination. The source stayed
selected and highlighted while the system prompted for a destination. Nothing was ever stashed in a
place you could not see, because nothing was stashed at all -- the operation ran from the visible
selection to the visible destination.

Star's undo was multi-level: "A user may undo several successive commands by repeatedly invoking
Undo." It was also honest about its limits: "Not all commands are totally reversible."

What Star still had was a **line**. A sequence of successive commands, walked backward, per
session, with no representation on the screen, for one user. Three of the five failure modes,
which by 1981 standards was excellent and is still the ceiling most software lives under.

Quotes and citations: [SOURCES.md](SOURCES.md).

## Lisa and Macintosh, 1984: the line becomes one item long

The clipboard replaced the visible source-to-destination gesture with an invisible intermediate
buffer, and took the writers' words for the physical process as its name. Nelson's four properties,
from 1999 and c. 1995: you cannot see it, it holds one object, whatever you put there destroys what
was there, and if the phone rings you lose the contents.

This is the line compressed to length one. Every copy is a destructive overwrite of a history you
were never shown, and the overwrite is one fat-fingered `C`-instead-of-`V` away at all times.

Undo on the same platform was single-level for years, which is the same line at the same length,
in the other direction.

## Windows: the line plus a second key

`Ctrl+Z` and `Ctrl+Y` give you a bidirectional walk along one line. Diverge and the forward half is
gone. The clipboard remains one slot.

The interesting exception is Microsoft Office, which shipped a **visible, multi-item clipboard**
task pane holding a couple dozen clippings. It is the most-shipped counterexample in existence, it
is confined to one application suite, and it exists because users obviously want a stack. Nelson
asked for exactly that -- "made it visible and made it a stack for rearrangement" -- and the
industry's answer was to ship it in a word processor and not in the system.

## X11 and Linux: eight slots nobody used, then three selections nobody agrees on

X had **cut buffers** before it had selections: `CUT_BUFFER0` through `CUT_BUFFER7`, properties on
the root window of screen zero, with `RotateProperties` to rotate the assignments around the ring
without copying the data. ICCCM Chapter 3 calls it a ring in those words, and specifies the rotate
in **both** directions, the backward one being for walking back through your own clippings on
explicit user request. Eight slots, a history walk, and server-side storage that survives the exit
of the client that wrote it. Standardized in 1988, effectively unused, and still eight times better
than one invisible slot.

Then ICCCM standardized three selections -- `PRIMARY`, `SECONDARY`, `CLIPBOARD` -- with type
negotiation through `TARGETS`, incremental transfer for large data, and timestamps for concurrent
claims. A real protocol for a real problem, and a byword for pain ever since. `PRIMARY` is at least
honest about where the data lives: the selection is **owned by the source window**, so the content
is visibly highlighted in the application that has it, and middle-click pastes from there. Its
failure mode is the other end of the same rope -- the owner exits and the selection evaporates,
unless a clipboard manager was sitting there to catch it.

Which is the tell. On every platform, the fix is a **third-party clipboard manager** that users
install to get history back. The demand is universal and the system never supplies it.

The ICCCM text for all of this, quoted at length, with the eight-deep ring and the backward rotate
in the standard's own words: [SELECTIONS-AND-CUT-BUFFERS.md](SELECTIONS-AND-CUT-BUFFERS.md).

## The universal tell: redo discarded on divergence

The clearest statement of the bug is not in a critique. It is in Vim's release notes, describing
what Vim did before version 7:

> Previously there was only one line of undo-redo. If, after undoing a number of changes, a new
> change was made all the undone changes were lost. This could lead to accidentally losing work.

That is still the behavior in nearly every editor, IDE, word processor, and drawing program
shipping today. Undo three steps, type one character, and a future you might have wanted is gone
with no gesture to recover it. Nothing warned you, because there was nothing on screen to warn you
about.

Git solved this exact problem for source code, visibly and by default, and the solution never
crossed the street into the editing gesture. See [UNDO-TREES.md](UNDO-TREES.md) for the two
editors that got halfway, and [BRANCHING-TIMELINES.md](BRANCHING-TIMELINES.md) for the rest.
