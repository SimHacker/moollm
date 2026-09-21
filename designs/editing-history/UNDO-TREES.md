# Forkable is not navigable

Two editors solved the hard half of this problem decades ago. Emacs never loses a state, and Vim
keeps an actual tree of them across sessions. Neither will show it to you, neither lets you name a
branch, and neither lets you hand one to another person. The data structure is right and the
interface is missing, which is why almost nobody uses the capability they already have.

## Warren Teitelman got there first, and he had the history list too

UNDO was in Interlisp, alongside DWIM, long before any of the systems in
[ONE-DIMENSIONAL.md](ONE-DIMENSIONAL.md). The idea that a system should be able to take back what
it just did to you is as old as the idea that it should guess what you meant, and it is the same man's
idea: Teitelman built both, in the **Programmer's Assistant**, which kept a **history list** of what
you had done and let you `UNDO` it, `REDO` it, `FIX` it, or `USE` it again with substitutions.

A history you could print and re-execute, in 1972. Everything in this directory is an argument for
getting back to that. (His MIT thesis was titled *PILOT: A Step Toward Man-Computer Symbiosis*, which
is also the correct title for the argument.) Teitelman also turns up in the middle of this lineage in
the 1985 Alvey window-management retrospective, naming a dozen systems in one room that had each
invented their own vocabulary for the same gestures.

## Emacs: nothing is lost, and you cannot see any of it

Emacs's undo is not natively a tree. It is a list, with one twist that changes everything: **undoing
is itself a change, and it is recorded.** Redo is not a separate mechanism; redo is undoing the
undos. The consequence is that no state is ever discarded by divergence. The future you would have
destroyed in any other editor is still in there, reachable by continuing to undo.

Reachable is not navigable. There is no display. To return to a state you remember, you walk, and
while walking you pass through states that look almost like the one you want, and the thing you are
navigating is invisible, so you lose your place. In practice people give up and retype.

(Honest limit: the history is subject to `undo-limit`, `undo-strong-limit` and `undo-outer-limit`,
so it is bounded, not eternal. Bounded and invisible beats unbounded and destroyed.)

`undo-tree.el` (Toby Cubitt, GNU ELPA) makes the implicit tree explicit and draws it, with a
visualizer you can move around in, plus diffs between nodes. It is the right idea, it is a
third-party package, and its existence is the argument: the tree was always there, it just had no
face.

## Emacs already had Nelson's stack

Nelson asked for a clipboard that is visible and "a stack for rearrangement". Emacs has had the
data structure since the 1970s:

- **The kill ring** -- every kill is retained, sized by `kill-ring-max`, and `M-y` (`yank-pop`)
  walks back through them after a yank. A stack of clippings, in the editor, for fifty years.
- **The mark ring** -- `C-u C-SPC` pops back through previous marks; the global mark ring
  (`C-x C-SPC`) crosses buffers.
- **Registers** -- `C-x r s` and `C-x r i` save and fetch text by **name**, which is the one thing
  on this page that gives a clipping an identity.

Every one of them is invisible. You interact with the kill ring by pressing a key repeatedly and
watching the buffer change, which is the same blind walk as undo. Registers have names but no list
you can look at without asking for one. The capability shipped; the representation never did.

## Vim: the tree is real, persistent, and undisplayed

Vim 7.0 (2006) shipped undo branches, announced in exactly the terms that make the point:

https://marc.info/?l=vim-announce&m=114708043011893

> Undo branches: never accidentally lose text again

Diverge after undoing and Vim keeps the abandoned line as a branch. Changes are numbered and
timestamped, so `g-` and `g+` walk chronologically through every text state regardless of branch,
`:earlier 10m` goes to the text as it was ten minutes ago, `:earlier 1f` goes back one file write,
and `:undolist` lists the leaves of the tree. Vim 7.3 (2010) added `undofile`, so the whole tree
**survives closing the file**, with a hash check to reject a stale history.

That is persistence, branching, and time-travel by wall clock and by save point. It is more than
git gives you for uncommitted work. And here is Vim's own documentation, in the same release notes:

> There is no graphical display of the tree with changes, navigation can be quite confusing.

The `undotree` plugin exists to supply the missing display, exactly as `undo-tree.el` does for
Emacs. Two independent communities each wrote the visualizer the core left out.

## What the trees still do not have

This is the gap that [BRANCHING-TIMELINES.md](BRANCHING-TIMELINES.md) closes. Emacs and Vim give
you a branching, persistent, non-destructive history. They do not give you:

| Missing | Why it matters |
|---------|----------------|
| **Names** | A branch is a number. You cannot say "the version where the lead worked". |
| **Messages** | No place to record *why* this state exists. The reason is the most perishable part. |
| **Diffs between branches** | You can visit two states; you cannot see what separates them. |
| **Merge** | Two good branches cannot be combined. You retype one into the other. |
| **Sharing** | The history is yours alone. It cannot leave the machine or the process. |
| **Review** | Nobody can comment on a state, request a change, or approve one. |

Every item in that table is a solved problem in git, and every one of them is solved *visibly*.
The editing gesture never got wired to it.
