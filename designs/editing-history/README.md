# Editing history: the clipboard and the undo stack are the same bug

The clipboard and the undo stack are both **editing histories**, and both were built
one-dimensional, invisible, destructive, forgettable, and single-user. Fixing one without the
other is half a fix, because they are the same mechanism wearing two names: *what I took out*
and *what I did*.

Ted Nelson has been making the first half of this argument since at least 1995, in language
nobody has improved on. This directory credits him for it, keeps his words exact
([SOURCES.md](SOURCES.md)), and adds the part he did not ask for.

## The documents

| File | What |
|------|------|
| [SOURCES.md](SOURCES.md) | The quote ledger. Every quote checked against its primary, with transcript noise marked. |
| [ONE-DIMENSIONAL.md](ONE-DIMENSIONAL.md) | The indictment: Star, Lisa/Mac, Windows, X11. Why every shipped history is a line that forgets. |
| [UNDO-TREES.md](UNDO-TREES.md) | Emacs and Vim got the tree right and left it invisible. Forkable is not navigable. |
| [SELECTIONS-AND-CUT-BUFFERS.md](SELECTIONS-AND-CUT-BUFFERS.md) | X11 standardized an eight-deep clipboard ring with a backward rotate in 1988, and shipped no interface for it. Quoted from the ICCCM. |
| [KEYBOARDS.md](KEYBOARDS.md) | Dedicated Cut/Copy/Paste/Undo keys already shipped, twice. Star and Sun had them; the Lisp machines spent the key budget on modifiers and never lost a clipping. |
| [BRANCHING-TIMELINES.md](BRANCHING-TIMELINES.md) | The proposal: visible, revisioned, branching, merging, reviewable, multi-user. |

## What Nelson demanded

Two of the requirements below are **his**, not mine, in his own words at BayCHI in 2021:

> they could at least have made it visible and made it a stack for rearrangement but oh no

Visible. And a stack, meaning more than one, held for **rearrangement** rather than transport.
That is requirements 1 through 3. He named the disease too, and the naming is the load-bearing
part of his case: the functions are honestly called **hide** and **plug**, and calling them
*cut* and *paste* is what let them ship.

## What I add

Nelson's fix stops at *visible* and *more than one*. I want four more things, and they are not
a wish list -- they all fall out of one decision, which is to make the thing a **repo** and put
a **forge** in front of it:

1. **Do not hide it.** (Nelson)
2. **Do not restrict me to one of them.** (Nelson)
3. **Do not make it invisible.** (Nelson)
4. **Do not make it uneditable.** A clipping is a document. I can open it, fix it, annotate it,
   name it, keep it.
5. **Do not lose it.** Not when I copy something else, not when the phone rings, not next week.
6. **Keep the history of the clipping itself.** Every edit to it, with blame. Who changed this
   clipping, when, and why.
7. **Make it collaborative and reviewable.** Pull requests against a clipping. Discussion on the
   PR about why you are changing it. Review, commend, curate, request changes, reject. A
   clipboard with a **merge queue**.

4 through 7 are one idea, not four: *a clipboard that is a git repo with a forge on it.* The
moment the clipping is a commit, editability is free, blame is free, history is free, and review
is a workflow somebody else already built and debugged.

Git, then, but also **GitHub-class** -- the social layer is the point of 7, and plain git does not
have it. GitHub has real problems and there are self-hostable alternatives; it is dominant now so
it is what we build against, while keeping the option to move when something else materializes
and qualifies. The requirement is the workflow, not the vendor.

## Why there is no cute name for it here

I forbade metaphor names for this thing (see the naming challenge in
[WillWrightShowForFood](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-rosenthal/07-cliprepo-naming-challenge.md):
no ClipRepo, no ClipCity, no GitPaste, no MetaClip). The reason is Nelson's own doctrine, from
the same page as the clipboard rant:

> Metaphors are scraps of resemblance that tie us down.

The clipboard's original sin is that it is a **metaphor that launders a mechanism** -- a name from
the physical world that made an invisible destructive buffer sound acceptable. Naming the
replacement with a second metaphor repeats the crime at a different address. The word, when it
arrives, should suggest transclusion plus ledger plus selection-set without any of those
syllables. It is still an open assignment.

## Related in MOOLLM

- [`designs/GIT-AS-FOUNDATION.md`](../GIT-AS-FOUNDATION.md) -- git as the substrate
- [`designs/GITHUB-AS-MMORPG.md`](../GITHUB-AS-MMORPG.md) -- the forge as a social world
- [`designs/korz/`](../korz/) -- map and territory; the clipboard is a map that hides its territory

## Related in WillWrightShowForFood

Raw source catalogs and the show notes these arguments were harvested for:

- [Ted Nelson invisible clipboard rant catalog](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-nelson/sources/invisible-clipboard-rant-catalog.md)
- [Selection, clipboard, and inter-client data](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-rosenthal/selection-clipboard-lineage.md) -- per-system taxonomy and window-system nomenclature, for the show
- [WYSIWYG crime and wider highways](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-nelson/sources/wysiwyg-crime-and-wider-highways.md)

None of the arguments here depend on those. They are show prep about living people, governed by that
repository's portrayal standards; the technical case is made from primaries in
[SELECTIONS-AND-CUT-BUFFERS.md](SELECTIONS-AND-CUT-BUFFERS.md) and [SOURCES.md](SOURCES.md).
