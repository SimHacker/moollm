# Link pumps: writing with links from a pie menu

*Don Hopkins · November 2026*

**Thesis:** A link is a pipe, not a doorway. Select some text and a pie menu offers the tools for
linking it: pull out one way to expand the text and the other way to summarize it, or pick a
destination from a tree of related content. Once the link exists, it has a pie menu of its own,
which pulls an explanation through the link from the destination or pushes redundant text out
through it. The writer is Maxwell's demon at the valve, deciding which meaning belongs on which
side. What comes out is plain text with links, so readers need no model to read it.

Part of the [webtop](README.md) hub. It builds on
[Pumping Up Pie Menus](../pie-stack-views/PUMPING-UP-PIE-MENUS.md) (distance as appetite),
[Transclusion Frames](../pie-stack-views/TRANSCLUSION-FRAMES.md) (opposite items are inverse
operations), the [HyperTIES article schema](hyperties/ARTICLE-SCHEMA.md) (every article carries a
definition), and the [Nelson](nelson/README.md) notes (the bridge that popups still don't draw).
Written with Anthropic's Claude, from Don's description.

---

### Where this comes from

Chuanqi Sun's [Spaceship](https://github.com/chuanqisun/spaceship) steers a language model while
it writes: future knobs pull out of a main knob, where the direction picks what to change and the
distance picks how much. That's the gesture of the pull-out font pie menu Don made for NeWS, where
the direction picked the font and the distance picked the size. [Dasher](../DASHER.md) steers
through a language model one letter at a time.

Both steer the writing of new sentences. Most of what a writer does with a corpus is something
else: deciding what to link, what to explain in place, what to leave to the destination, and what
to cut because it's already said somewhere better. This design gives that work the same kind of
controls.

### The selection pie

Select text and press, and a pie menu opens on the selection. Its commands depend on what's
selected, the way objects in [Verbs and Rubrics](VERBS-AND-RUBRICS.md) advertise their own verbs:
a phrase that matches a page title or synonym offers to link to it, a long paragraph offers to
summarize, a single word offers to define.

Two submenus carry most of the weight: one for resizing the text and one for linking it.

### Expand and summarize: one gesture, two directions

The resize submenu has at least two items, opposite each other. Pull out one way to expand the
selection and the other way to summarize it. As [Transclusion
Frames](../pie-stack-views/TRANSCLUSION-FRAMES.md) argues, putting inverse operations 180 degrees
apart means the gesture carries the inversion: reversing the stroke undoes the intent.

Distance sets how much. A little way out, a summary drops a clause; farther out, it steps down the
summary scale from [Pumping Up Pie Menus](../pie-stack-views/PUMPING-UP-PIE-MENUS.md#semantic-zooming),
to a sentence, a phrase, a title, and a glyph. Expanding works the same way in the other direction.
The text in the document previews the result as you move, the way the font menu showed the font in
the document during mouse-ahead, and you can move back toward the center to back off. Release to
keep the result; return to the center to cancel. That's [reselection](../pie-stack-views/RESELECTION.md):
you browse the choice before committing to it.

The other directions are free for more axes. [Summary Genres](SUMMARY-GENRES.md) is the obvious
one: the same length in a different register.

### Link to: a tree of related content

The link submenu is generated when it opens: a tree of related content in the corpus, so each
level is a submenu, from topic to document to section. Three sources feed it:

- **Names.** HyperTIES let you link by writing an article's title or one of its synonyms. A
  selection that matches one goes at the top.
- **Similarity.** gwern.net already computes "similar links" from embeddings at build time; here
  they're offered at the moment you're deciding what to link.
- **Backlinks.** Documents that already link to the destination you're near.

Slice widths can follow relevance, as the [Fitts optimizer](../pie-stack-views/FITTS-OPTIMIZER.md)
lets them, so the likely destinations are the easy ones to hit, as Dasher gives likely letters the
big boxes. Hovering over a slice shows the destination's description, so you can see what you're
about to link to. Choosing a leaf makes the link.

### A link is a portal with its own pie

Once it exists, a link isn't only a way to go somewhere. Click it and you get a pie menu for working
the connection the link declares between two places: follow it, or pull, push, describe, annotate,
and sign it.

**Pull** brings content from the destination to here: a summary of what the destination says that
matters at this point, sized by distance, from a clause to a paragraph. It's how you explain the
link in context without sending the reader away.

**Push** is the opposite direction, and the opposite item. Text around the link that's redundant
with the destination goes out through the link. If the destination already says it, the text is
cut here and the link carries the reader there. If the text says something the destination
doesn't, it can be merged into the destination.

### Maxwell's demon at the valve

James Clerk Maxwell imagined a demon at a door between two chambers of gas, letting fast molecules
through one way and slow ones the other, sorting the gas into hot and cold. A writer working a link
is that demon for meaning, at the door between two documents. The pumps are the demon's moves:

- **Mixing:** merging what both sides say about the same thing into one account.
- **Distilling:** separating them: the general explanation goes to the destination, and the
  application to this context stays here.
- **Deduplicating:** keeping one copy and linking to it.
- **Duplicating:** quoting the destination here, ideally as transclusion, so the quote stays
  connected to its source.
- **Summarizing:** pulling a short version through the link.

The physics carries a warning. Leo Szilard, Rolf Landauer, and Charles Bennett showed that the
demon can't sort for free: the information it acts on has a cost. Here the cost is the writer's
judgment about what belongs on which side, and that cost is the point, because the judgment is the
writer's agency.

Stanisław Lem told the other half in *The Cyberiad*, whose
[demon of the second kind](../../examples/adventure-4/characters/robots/README.md) sorts true facts
out of the motion of air molecules and buries the pirate Pugg under paper tape full of them. A pump
running without anyone at the valve is that demon: everything it writes may be true and nobody
needs it. So every pump previews, waits for the writer to release it, and can be taken back.

### Read-write and read-only destinations

A link into your own corpus is a two-way valve. Pull, push, merge, and dedupe all work.

A link into a page you can't edit, such as someone else's site, works one way. You can pull
summaries and quotes from it, with attribution and a link to the passage they came from. Pushing
can only mean cutting your redundant text and linking to theirs. Anything you'd want to add to the
destination, such as a description or a correction, goes in the [top](README.md#the-name-is-the-architecture),
the webtop's layer over documents you can't edit. That layer is private by default and shared on
purpose, which is the hub's conclusion from the public annotation layers that died.

### Three kinds of words around a link

A link can carry three different texts, and they belong to different things.

- **The description belongs to the destination.** It says what the destination is, and it's the
  same wherever the destination is linked from. It's the HyperTIES definition, shown on a single
  click in 1988, and shown here on hover.
- **The note belongs to the link.** It says why you might follow the link in this context, and how
  what's at the other end applies to what's being said here. It can show on hover, or sit inline
  as a sentence or paragraph before or after the link.
- **The sign belongs to the reader's route.** It announces what's coming before the reader gets
  there.

The note is the important one, because it's the part nobody has built. The Nelson notes concede
that "a popup is a better jumplink, not a bridge. You still cannot see the relationship, only the
destination." A description of the destination doesn't draw the bridge. A note about why it's
linked here does, in words.

The lowest-tech version already works in Markdown: a link title, `[text](url "note")`, shows on
hover in every browser.

### Signs on the highway

Highways announce exits before you reach them, mark the exit itself, and name the intersections, so
drivers can decide without slowing down. Text can do the same:

- **Advance notice:** before a dense passage, a line saying what's coming and where the background
  lives, so a reader who needs it can take that exit first.
- **The exit sign:** the note at the link.
- **Intersections:** where this document crosses another that covers the same ground, from the
  backlinks, so a reader can see the junction without leaving the road.

Too many signs is the same as none. Signs are rationed by what a reader would actually miss, and
the pie can propose them but the writer places them.

### Who gets the controls

The writer gets the valve: what to link, what to explain in place, what to send away, and what to
cut. The reader gets the signs, descriptions, and notes needed to decide whether to take an exit.
Neither of them hands the decision to a model. These are
[interfaces to agency, not agents instead of interfaces](../INTERFACE-TO-AGENCY.md).

### The model runs at write time

The pumps call a language model while the writer works. What the writer keeps is committed as plain
text and links, so reading needs no model, which is the [tagsonomy compiler](../TAGSONOMY-COMPILER.md)
principle applied to prose.

Two bits of bookkeeping keep that honest:

- **Provenance.** Generated text is marked as generated until the writer accepts or rewrites it,
  as [Read/Unread](READ-UNREAD.md) insists a model's guess and a person's mark be distinguishable.
- **Staleness.** A pulled summary records which version of the destination it summarized. When the
  destination changes, the summary is flagged, not silently wrong. Unread is a diff, and so is a
  stale summary.

### Status

Design, not implementation.

↑ [webtop](README.md)
