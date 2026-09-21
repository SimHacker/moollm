# Song form: the hypertext everybody already reads

Every literate musician has been reading a nonlinear document with loops, named labels, jump
instructions, conditional branches, and optional passages -- for centuries, from a single sheet of
paper, in real time, while playing an instrument, without anyone calling it complicated.

It is called sheet music. The structure is called song form. And it is the frame to use on anybody who
finds the rest of this repo daunting, because they already know it and they learned it without
studying it.

## Why this frame and not a diagram

The other frames fail on real people:

| Frame | Why it fails |
|-------|--------------|
| Graph diagram | Reads as work. Nobody navigates a picture of a graph for pleasure. |
| Mind map | Nelson's objection, verified: "mind maps don't seem to fill a bill." No point of view, no sendable unit, unlabeled links. See [PAIRED-LINKS.md](PAIRED-LINKS.md). |
| Memory palace | A retrieval trick for one person's own recall. Not portable, not authored for a reader. |
| Outliner or Scrivener | Nelson looked at Scrivener and was daunted by the complexity. Says he is lazy. Most people are, and are right to be. |
| **Song form** | Already installed in everyone. Zero explanation. Sendable. Has a point of view. Loops on purpose. |

A song passes all three of Nelson's tests for a document, stated at BayCHI in 2021: it can be **sent to
another person**, it **expresses a point of view**, and **a person made it**. A graph of your notes
passes none.

## The notation is already a link language

Musical notation is a small, stable, widely-read instruction set for nonlinear traversal. It was
standardized in the Baroque era and a session player still sight-reads it cold:

| Notation | What it is |
|----------|------------|
| Repeat signs `𝄆 𝄇` | A loop. Play the enclosed span again. |
| Volta brackets (1st / 2nd endings) | A **conditional branch on loop iteration.** Different ending depending on which time through. |
| `D.C.` (da capo) | Jump to the head. |
| `𝄋` segno, `D.S.` | A **named label** and a jump to it. |
| `To Coda`, `𝄌` | A forward jump out of the loop into the tail section. |
| `Fine` | Halt, which is not the last thing on the page. |
| "Vamp till cue" | `while` loop, exit condition supplied live by a human. |
| *Ossia* | An **alternate passage printed on a staff directly above the original.** Take either. |
| Lead sheet / fake book chart | The **structure alone**, melody and chords, with the performance left to you. |

Read that table again as a spec and it is a bytecode with labels, loops, conditional jumps, and
variant blocks. Musicians do not find it hard. They find it *less* work than writing the notes out
straight, which is the actual argument for structure over linearity, and it was settled three hundred
years before anybody had a computer to argue about.

*Ossia* deserves special attention when talking to Nelson, because it is **parallel alternatives shown
side by side on the page**, and side-by-side parallel presentation is the thing he says hypertext is
for.

## The chorus is transclusion, and nobody is confused by it

A three-minute pop song has one chorus. It appears four times.

Nobody believes there are four choruses. Nobody thinks the second one is a copy of the first. If the
songwriter changes a word in the chorus, it changes in all four places, because **there is one chorus
and it is included by reference four times.** That is transclusion, Nelson's mechanism and his word,
already understood by the entire population, with no jargon and no diagram.

This is the single best on-ramp we have. Transclusion is not an exotic hypertext feature. It is how a
chorus works.

## Rondo is the loop stack

The traversal mechanism we want is this: you are reading along a thread, you take a link off to the
side, you reach the end of that side thread, and **you pop back to where you were and keep going**, so
you never lose your place while visiting several links in turn. Nested, with a stack, so it works at
any depth.

Music has had that form since the Baroque and calls it **rondo**: `A B A C A D A`. The refrain `A` is
the main thread. `B`, `C`, `D` are excursions. After every excursion you return to the refrain and
continue. The da capo aria is the two-level case, `A B A`.

Bush described the same shape for the Memex in 1945 as a **main trail** with **side trails**:

> Thus he goes, building a trail of many items. Occasionally he inserts a comment of his own, either
> linking it into the main trail or joining it by a side trail to a particular item.

So the mechanism has two independent precedents, one musical and one hypertextual, and both are older
than the web's back button, which is the degenerate one-level-deep version of it that loses your place
the moment you branch twice.

Concretely, a traversal stack whose frames are `(rank, position, mask)`:

```yaml
traversal:
  - { rank: d.chorus-thread, at: 3, mask: full }      # the refrain you keep returning to
  - { rank: d.cites, at: 0, mask: excerpt-only }      # an excursion, pushed
  # reaching the end of the top frame pops it and resumes the one below, at: 3
```

Push on following a link, pop on exhausting a rank, and resume. "Loop over these links" is one frame
with a ring in it. **You cannot lose your place**, which is the entire complaint people have about
following links, and it is fixed by a stack that any musician's reading habits already model.

## The attention mask is which verses you sing tonight

Nobody sings the third verse. Everybody knows nobody sings the third verse. The verse is still printed
and still there and still part of the song, and tonight it is skipped.

That is an **attention mask** over a rank, and Bush's name for it is a **skip trail** -- a path that
"stops only on the salient items." Two hundred people in a room can share one song, and each performer
brings their own mask over it, and nobody needs the concept explained.

Masks are where editorial control lives, and it is subtractive as much as additive: which links you
take, which you leave, which you return to.

## Branch, remix, switch in and out

The rest of the user's list is all standard repertoire practice:

- **Covers and versions** are branches off a shared structure, each with its own point of view.
- **Alternate takes** are the abandoned branch, kept. The thing every undo stack throws away, the
  record industry ships as a bonus disc. See [editing-history/](editing-history/README.md).
- **Jazz head arrangements** are fan-mode traversal resolved at performance time: head, then solos in
  an order and a count negotiated live by eye contact, then head out. The form is fixed, the middle is
  chosen while running.
- **Mashups and medleys** are transclusion across documents.
- **A 12-bar blues** is a ringrank that a stranger can join in progress, because the structure is
  public and only the path is personal.

The recording is a **sent path**: one traversal of the structure, frozen, handed to somebody else.
Which is the deliverable this whole design has been circling. The structure is shared and boring; the
performance is the part you send.

## Groundhog Day: the loop where the second pass means something different

The ring is not a treadmill. Nelson's through-line rule -- "you start with a zinger and end by coming
back to that zinger" -- works because the return visit lands differently than the first.

That is Groundhog Day as a structure: same cells, same order, accumulating state in the reader. It is
also the last chorus of a good song, which is identical on paper to the first chorus and does not sound
identical, because three minutes happened.

For [PAIRED-LINKS.md](PAIRED-LINKS.md) this is why a throughline is a ringrank with a designated head
cell rather than a line with a summary bolted on the end.

It also sets the cost of the one-neighbor-per-dimension axiom. A closed ring is legal, because every
cell still has exactly one next. A path that **crosses itself** is not, so a literal Groundhog Day,
where one scene has several different continuations, needs each pass to be its own suffixed story id:
`day-01`, `day-02`, `day-03` as separate dimensions over shared cells. The music already agrees,
since the repeat is notated once and counted, not written out twice.

## Family albums compose into larger songs

The Sims family album is the smallest complete unit of this: a short authored sequence of captioned
moments, made by a player, about their household, sendable as a unit. Millions of them were made.

Transcluded into larger structures, they behave like verses. A neighborhood is a set of households
whose albums cross-reference each other, which is already a labeled graph with `neighbor`,
`married-to`, `descended-from` dimensions in it. Scale that up and it is the **Bar Karma** shape:
community-authored scenes, assembled into episodes, with the assembly itself an authored act, which is
what StoryMaker was for.

So the ladder runs: album, scene, episode, network -- with branching and looping at every rung, and the
same two artifacts at every rung, a **path** and a **mask**. StoryMaker's read paths and attention
paths are throughlines, and a throughline is a song.

## Harvest as you travel

The last piece, and the one that makes a tour into a deliverable rather than a performance you narrate
once and lose.

While you walk the structure, you collect. Pointers, excerpts, local caches of things that will rot,
metadata, your own contextualizing notes on *why this one*, the disagreement you found between two
sources. All of it lands in the repo as you go, on a branch, committed.

What you hand over at the end is not a link dump. It is a **path plus a mask plus the harvest**, with
provenance on every item, versioned, forkable, and reviewable. A message, an argument, a tour, or a
story, depending on how you shaped the ring -- and a pull request is how somebody argues back with the
diff in front of both of you. See [editing-history/BRANCHING-TIMELINES.md](editing-history/BRANCHING-TIMELINES.md).

That is Bush's trail blazer with a forge, and it is the job description:

> There is a new profession of trail blazers, those who find delight in the task of establishing useful
> trails through the enormous mass of the common record.

## Back to the sheet music

Every literate musician reads a document with loops, labels, jumps, conditional endings, optional
passages, and side-by-side alternatives -- from one page, in real time, while playing.

Nothing in this repo is more complicated than that, and the parts that feel more complicated are the
parts we have not yet explained in song form. The test for any MOOLLM concept, before it gets a name
or a schema, is whether it survives being explained as a piece of music to somebody who has never read
this file:

| MOOLLM | Song |
|--------|------|
| cell / scene / room | bar, section |
| dimension (paired links) | the axis you move along: next verse, up an octave, louder |
| rank | a section: the verse, the chorus, the bridge |
| ringrank | the loop |
| transclusion | the chorus |
| path | the arrangement you played tonight |
| attention mask | the verse you skipped |
| throughline | zinger first, zinger last |
| loop stack | rondo |
| fork | a cover |
| harvest | the setlist, with notes, handed to the next band |

If it does not survive that translation, the concept is probably wrong, not just badly named.

## Related

- [PAIRED-LINKS.md](PAIRED-LINKS.md) -- the model: cells, named opposite pairs, ranks, throughlines
- [editing-history/](editing-history/README.md) -- why the repo is the substrate; alternate takes kept
- [korz/](korz/) -- the structure is the territory, the path is the map
- StoryMaker scenes and cards:
  https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/storymaker-stories-and-scenes.md
