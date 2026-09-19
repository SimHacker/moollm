# The room where the drawer is empty

![A warm dim working room at night. On the left wall, aged architectural survey plates pinned overlapping, one bearing a worn illegible red stamp. On the back wall, a gilt-framed still life of artist's tools and a gilt three-panel triptych of draped figures. At the right, under a hanging lamp, a large painted theatrical flat of a top-hatted melodrama villain above a ribbon reading VILLAIN, its paint flaking away; below it an oak board of pale wooden joinery test pieces on iron brackets. In the centre foreground a mahogany card-index cabinet with brass-framed drawer cards reading WHO, WHAT, WHEN, WHERE, HOW and WHY, with one drawer pulled fully out and completely empty, green felt bare inside](headline-mystery-and-art.png)

**Plate for:** [*Case study: mystery as dispatch*](../README.md) — the whole argument ·
**Girders:** [`headline-mystery-and-art.yml`](headline-mystery-and-art.yml) ·
**Pile:** [`INDEX.yml`](INDEX.yml)

**One drawer is open and there is nothing in it.** That is the essay.

Every row of the mystery table is a different empty drawer. The whodunit leaves `rcvr` unbound; the
howcatchem hands it to you on page one and empties `HOW` instead; the whydunit empties `purpose`; the
cosmic-horror story empties `WHAT` and then discovers the drawer was never in the cabinet. **The form
you are reading is the name on the open drawer.** Which is why genre is not a property of a text —
the words are the same on both readings — but a fact about which coordinate the text declines to bind
and how long it declines for.

`WHY` is the one standing open here because the whydunit is the detective genre of the dimension this
repo is arguing should exist
([purpose-dimension.md](../../korz-prime/examples/purpose-dimension.md)), and because an unbound
purpose is the least bearable of the gaps. A reader will sit with an unknown *who* for three hundred
pages quite happily. An unexplained *why* itches.

## The room is the gather

The plates are not arranged here, they are **kept** here: pinned, hung, propped, leaning against the
wall where someone left them. Survey plates on one wall, gilt oils on another, a scenery flat and a
joiner's trial board on the floor.

That is deliberate and it is the repo's own architecture drawn once. A directory is a room; a room is
an activation context; [`INDEX.yml`](INDEX.yml) is a gather over a flat pile. **This is that gather
rendered** — which is the only reason the four [registers](INDEX.yml) are allowed to disagree with
each other. A working room is the one container in which a technical survey sheet, a Victorian oil, a
rotting theatre flat and a board of broken dovetails can all sit without any of them being in the
wrong style. The room is why the plates can come from four traditions.

`generated LAST and FROM the pile, per Don's instruction: the tip of the pyramid composed from the`
`plates rather than guessed before them. Four plates went in as reference images, one per register`
`family, and they came back as objects on the walls — the still life is` [art-in-the-blood](art-in-the-blood.md)`,`
`the flaking villain is` [melodrama-and-tragedy](melodrama-and-tragedy.md)`, the survey sheets are the`
[locked room](locked-room-missing-axis.md)`, and the trial board is` [the Bildungsroman](bildungsroman-binding-your-own-setpoint.md)`.`

## One known flaw, left in

**`WHY` appears twice.** It is correct on the open empty drawer, and it is also sitting on a small
closed drawer at the upper right, where it should not be. Five generations failed to shift it: the
model kept re-anchoring on its own previous output, and each attempt to blank the stray card blanked a
different one instead, once deleting `WHEN` and once stripping the label off the open drawer. I stopped
rather than keep grinding.

It is not a reading, it is an artifact. Worth saying only because there **is** a tempting reading
available — the repo really does split the why-axis into `purpose` and `whose_purpose`, so a second
`WHY` drawer, closed, is a thing the argument could absorb — and claiming that was the plan would be a
lie about provenance. If it bothers you, the fix is a fresh generation from the `.yml` with no
reference image and a cabinet of exactly six drawers.

**Up:** [the essay](../README.md) · **Pile:** [`INDEX.yml`](INDEX.yml) — all eleven plates, four
registers, and the one concept that was declined
