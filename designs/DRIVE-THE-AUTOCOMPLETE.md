# Drive the autocomplete

*Don Hopkins · November 2026 · written with Anthropic's Claude, from Don's description*

**Don't let autocomplete drive. Drive the autocomplete.** A chat box is a taxi: you describe the
text you want, wait, and read what comes back. This is a design for writing with a language model
the other way around. The text stays in front of you, and you steer the model with gestures, pinned
words, and short spoken instructions, every one of which can be undone.

## Where it comes from

- **[Spaceship](https://github.com/chuanqisun/spaceship)**, by Chuanqi Sun at the MIT Media Lab,
  steers a model while it writes. Knobs pull out of a main knob: the direction picks what to change,
  such as tension, pace, or tone, and the distance picks how much. Turn a knob and the text
  regenerates. You can also pin words as **anchors** that lead what it writes next.
- **[Dasher](DASHER.md)**, by David MacKay, writes by steering through a language model. The
  possible next letters are boxes sized by how likely they are, and you fly into the one you want,
  with a mouse, your eyes, or one button. It's compression run backwards.
- **Pie menus.** Spaceship's knob is a pull-out pie menu, the gesture of a font menu I made for
  NeWS where the direction picked the font and the distance picked the size, shown live in the
  text as you moved.

## The moves

**Pull to expand or summarize.** Select text, and a pie menu opens on it. Pull one way to expand
it and the opposite way to summarize it; the distance says how much, from dropping a clause down to
a single title. The text previews the result as you pull, and moving back to the center cancels.
Opposite directions are inverse operations, so reversing the stroke reverses the intent.

**Drag the edges.** Spaceship grows text at the bottom. You can also select any passage and drag
its edges, outward to expand it and inward to summarize it, like resizing a window. Expansion
draws on what the passage is attending to: the anchors, the links inside it, and the text around
it. Change any of those and the expansion re-forms, the way Spaceship regenerates when you turn a
knob.

**Pin anchors.** An anchor can be a word, a name, a link, or a whole document. Summaries keep the
anchored phrases, expansions build on them, and everything else below favors them.

**Dasher at every level.** Dasher works letter by letter, so it can write anything, even names no
model would guess. The same zooming works above letters, with boxes for likely words, phrases,
sentences, and paragraphs. You fly through whole sentences when the model is right and drop down a
level when it isn't, to words and finally letters, then fly back up. Keith Vertanen and MacKay's
[Speech Dasher](https://www.keithv.com/pub/sd/speechdasher.pdf) did this for words in 2010, and
expert users wrote 40 words per minute with only their voice and their eyes. Names you've already
used get bigger boxes, and so do your anchors.

**Links are pumps.** A link isn't only a way to go somewhere; it's a pipe between two documents,
with its own pie menu. *Pull* brings a summary of the destination to here, sized by distance.
*Push* sends text that the destination already covers out through the link. The commonest move is
to pump a whole passage out into its own document and say how much stays behind: a heading and a
summary, a sentence, or just a link. So move and copy aren't two commands anymore but one dial:
because the model rewrites both sides, each keeps a version written for its own context, and the
anchors decide what each one attends to.

**Pumps have filters, and run both ways.** Pump a passage out, click two names on the far side,
and pump back only what's about them. Select a region on the receiving side to mean "more like
this" or "not this again." Writing becomes refinement by iteration: steer, back off, steer again.

**Say what to do with it.** When no menu item fits, select the text and speak or type an
instruction on a separate channel over the document: "expand this from that link, but keep the
second anchor," or "pull back only what's about MacKay." Every anchor, link, and knob has a
speakable name. That's Richard Bolt's
["Put-That-There"](https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf)
from MIT's Architecture Machine Group in 1980, the Media Lab's predecessor: pointing says *which*,
the voice says *what*. Watch Chris Schmandt's
[1979 demo](https://www.youtube.com/watch?v=RyBEUyEtxQo) to the end for why everything here must be
easy to undo. What the vocabulary understands runs the same commands as the menus; what it doesn't
goes to the model as a free instruction.

## Nothing is lost

Every pump is a git commit, and the instruction that caused it is the commit message. The clipboard
isn't the invisible single-slot buffer Ted Nelson rightly rails against. It's a folder of files in a
repo, so it's visible, editable, branching, and shareable, and a new clipping can never overwrite an
old one. Throwing text away moves it to a trash folder you can open.

What comes out is plain text with links. The model runs while you write, so your readers don't
need one.

## Direct manipulation, all four points

Ben Shneiderman drew
["an integrated portrait"](https://www.cs.umd.edu/~ben/papers/Shneiderman1983Direct.pdf) of direct
manipulation in 1983, in four points. This design meets all four. A chat box meets only the
fourth.

1. **"Continuous representation of the object of interest."** The text never leaves the screen,
   and neither do the anchors, the links, or the clipboard.
2. **"Physical actions … or labeled button presses instead of complex syntax."** Direction picks
   the operation and distance picks how much. Speech names things you can see and runs the same
   commands your hand could, so it's pointing by name, not programming.
3. **"Rapid, incremental, reversible operations whose impact on the object of interest is
   immediately visible."** Everything previews, and every pump can run back.
4. **"Layered or spiral approach to learning that permits usage with minimal knowledge."** Start
   with select and pull. Anchors, filters, Dasher, and the vocabulary come when you want them.

## Who decides

The writer decides what to link, what to explain in place, what to send away, and what to cut. The
model proposes and previews, but never decides. That's what I mean by an
[interface to agency, not an agent instead of an interface](INTERFACE-TO-AGENCY.md): no capability
is reachable only by asking the model.

## More

- [Link pumps](webtop/LINK-PUMPS.md), the full design: the link tree, Maxwell's demon at the valve,
  read-only destinations, and the three kinds of words around a link.
- [Dasher: driving a language model](DASHER.md), with the history and sources.
- [An interface to agency](INTERFACE-TO-AGENCY.md), from The Sims to MOOLLM.
