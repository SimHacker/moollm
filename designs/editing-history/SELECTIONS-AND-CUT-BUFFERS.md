# The ring that shipped, and the slot that won

X11 specified an **eight-deep clipboard ring with a backward rotate**, in the same standard that
specified the selection mechanism which displaced it. The ring is not folklore and not a proposal.
It is Chapter 3 of the *Inter-Client Communication Conventions Manual*, it uses the word "ring",
it defines the rotate in both directions, and it stores the data in the server where it outlives
the client that put it there.

Then everything anyone actually shipped used a mechanism with one slot that dies when its owner
exits. This document is the receipt, quoted from the standard.

It stands alone. Everything below is sourced to the ICCCM text or to a dated public message; no
claim here rests on another document in this repository.

## The standard, and who wrote it

*Inter-Client Communication Conventions Manual*, X Consortium Standard, Version 2.0:

https://www.x.org/archive/X11R7.7/doc/xorg-docs/icccm/icccm.html

Title page: **David Rosenthal, Sun Microsystems, Inc.**, edited by **Stuart W. Marks, SunSoft,
Inc.** Copyright 1988, 1991, 1993, 1994 X Consortium. The Preface to Version 1.1 describes how it
was made:

> David Rosenthal had overall architectural responsibility for the conventions defined in this
> document; he wrote most of the text and edited the document, but its development has been a
> communal effort. The details were thrashed out in meetings at the January 1988 MIT X Conference
> and at the 1988 Summer Usenix conference, and through months (and megabytes) of argument on the
> wmtalk mail alias.

The same preface credits the sections separately. For the Selection section: Jerry Farrell, Phil
Karlton, Loretta Guarino Reid, Mark Manasse, Bob Scheifler. **For the Cut-Buffer section: Andrew
Palay.** The ring has an author.

## The sentence that predicts the whole outcome

Chapter 1, first line of the introduction:

> It was an explicit design goal of X Version 11 to specify mechanism, not policy.

Then it lists what the conventions govern, and the second item is the one everybody forgot:

> Being a good citizen in the X Version 11 world involves adhering to conventions that govern
> inter-client communications in the following areas: Selection mechanism · Cut buffers · Window
> manager · Session manager · Manipulation of shared resources · Device color characterization

And the disclaimer that is the cause of death:

> This document proposes suitable conventions without attempting to enforce any particular user
> interface.

A history was specified. A face for it was explicitly out of scope. Nobody else took the job. This
is the identical failure documented in [UNDO-TREES.md](UNDO-TREES.md), where Vim and Emacs both
shipped a branching undo structure and left the visualization to third-party packages.

## Chapter 3: the ring

ICCCM distinguishes the two mechanisms by who does the work:

> The cut buffer mechanism is much simpler but much less powerful than the selection mechanism. The
> selection mechanism is active in that it provides a link between the owner and requestor clients.
> The cut buffer mechanism is passive; an owner places data in a cut buffer from which a requestor
> retrieves the data at some later time.

"Passive" is doing a lot of work in that sentence. Passive means **the data is just sitting there**,
in the server, in a place with a name, not held hostage by a running process:

> The cut buffers consist of eight properties on the root of screen zero, named by the predefined
> atoms CUT_BUFFER0 to CUT_BUFFER7. These properties must, at present, have type STRING and format
> 8.

Storing is specified as a rotate-then-write, and the standard calls the structure by its name:

> A client that stores data in the cut buffers (an owner) first must rotate the ring of buffers by
> plus 1 by using RotateProperties requests to rename each buffer; that is, CUT_BUFFER0 to
> CUT_BUFFER1, CUT_BUFFER1 to CUT_BUFFER2, ..., and CUT_BUFFER7 to CUT_BUFFER0. It then must store
> the data into CUT_BUFFER0 by using a ChangeProperty request in mode Replace.

Reading is `CUT_BUFFER0`. And then, the operation that makes it a history rather than a buffer:

> In response to a specific user request, a client may rotate the cut buffers by minus 1 by using
> RotateProperties requests to rename each buffer; that is, CUT_BUFFER7 to CUT_BUFFER6, CUT_BUFFER6
> to CUT_BUFFER5, ..., and CUT_BUFFER0 to CUT_BUFFER7.

That is `M-y`. That is walking back through your last eight clippings, in the window system, defined
in 1988.

The chapter even closes by telling implementors that the user has a mental model of this thing and
is entitled to see which operations move data:

> Data should be stored to the cut buffers and the ring rotated only when requested by explicit user
> action. Users depend on their mental model of cut buffer operation and need to be able to identify
> operations that transfer data to and fro.

## What the ring actually gets you

Read against the five failure modes in [ONE-DIMENSIONAL.md](ONE-DIMENSIONAL.md), the 1988 cut
buffer ring beats the 2026 system clipboard on two of them outright.

| Property | Cut buffer ring | Selection (PRIMARY / CLIPBOARD) |
|---|---|---|
| Depth | Eight | One |
| History walk | `RotateProperties` by minus 1 | None |
| Survives source client exit | Yes, the data is server-side | No, unless a manager catches it |
| Where the data lives | Root window of screen zero, named | Inside the owning client's process |
| Inspectable from outside | Yes, it is a named property on a known window | Only by asking the owner to convert |
| Content types | `STRING`, format 8, and only that | Negotiated via `TARGETS`: text, images, files, anything |
| Large transfers | No provision | `INCR`, chunked |

Because the buffers are properties on the root window, they are readable by any client that wants
to look, which includes the ordinary command line property inspector (`xprop -root CUT_BUFFER0`).
That is a direct consequence of the spec's own sentence about where they live, and it means the
much-demanded **visible clipboard with history** has been technically available on Unix, from a
shell prompt, since before the Macintosh had color.

The ring's real defect is the narrow one: `STRING` and format 8 means 8-bit text, full stop. No
images, no rich text, no negotiation, no large-object protocol. The selection mechanism was built
because that defect is fatal for a general window system, and it was the right call. The mistake
was not building selections. The mistake was letting the depth and the persistence go when the
type system was fixed, and then never bringing them back.

## Chapter 2: why selections win, and how they lose

Selections solve the type problem by making the transfer a live conversation:

> Selections are the primary mechanism that X Version 11 defines for the exchange of information
> between clients, for example, by cutting and pasting between windows. Note that there can be an
> arbitrary number of selections (each named by an atom) and that they are global to the server.

The cost is in the next sentences, and it is the whole Unix copy-paste user experience:

> Each selection is owned by a client and is attached to a window. Selections communicate between an
> owner and a requestor. **The owner has the data representing the value of its selection**, and the
> requestor receives it.

The data never leaves the source application until somebody asks for it. Close the source and there
is nothing to ask. Every Linux user who has copied a URL, quit the browser, and pasted nothing has
met that sentence. It is not a bug and it is not an oversight, it is the architecture: an arbitrary
number of selections, each a promise to convert on demand, and a promise is only as durable as the
process making it.

The three predefined selection names, from the name-space table, are `PRIMARY`, `SECONDARY`,
`CLIPBOARD`. Two mechanisms and three selections is five ways to hold a clipping, none of which is
the eight-deep ring, and the ring was in the same book.

One more line from Chapter 2, which is the most civilized sentence in the standard and is worth
keeping in mind next time an application will not let you select its text:

> In particular, displaying text in a permanent window without providing the ability to select and
> convert it into a string is definitely considered antisocial.

## The implementor's verdict

The standard's reputation among the people who implemented it is a matter of public record. Conrad
Parker, to `slug-chat`, 12 July 2001, after Jeff Waugh told Sean Neakums to "Go read the ICCCM. Come
back when you're done crying":

https://github.com/porridgewithraisins/x11cp/blob/main/rant

> I've recently spent my nights in pain implementing the selection mechanism. WHY OH WHY OH WHY? why
> me? why did I choose to do this? and what sick evil twisted mind wrote this damn spec?

> So what if they use Atoms for everything. So what if there's no explicit correlation between the
> target type of a SelectionNotify event and the type of the property it indicates? So what if the
> distinction is ambiguous?

> Name one fucking program in the whole world that uses MULTIPLE selections by choice? [...] And
> XA_SECONDARY? Who the fuck uses the SECONDARY selection? and who actually queries TARGETS? All
> anyone ever fucking does with the selection is COPY TEXT!!

> The ICCCM is the coding equivalent of the Medieval rack, except its advertised as some kind of X11
> swingers party.

Parker's complaint and this document's complaint are the same observation from opposite ends. He is
angry that the general mechanism is enormous when all anyone does is copy text. The other half of
that sentence is that the simple mechanism, sized exactly for copying text, was right there in
Chapter 3 with eight slots and a history walk, and the ecosystem built on the enormous one anyway
and then gave users less than the simple one offered.

## What this establishes

The usual story about clipboard history is that nobody thought of it, or that it is hard, or that
users would not understand it. None of those survive contact with Chapter 3.

Multiple clippings, a defined order, an operation to walk backward through them, storage that
outlives the process that wrote it, a location any program can read, and an explicit instruction to
implementors that the user needs to be able to tell when data moves. Written down, standardized,
shipped in the reference implementation, and then declined.

It was declined because the standard said "mechanism, not policy" and meant it, and because no layer
above it ever claimed the policy. The ring is still in the protocol. `RotateProperties` is still
there. What never existed is a single pixel of interface for it.

## Sources

Inter-Client Communication Conventions Manual, Version 2.0, X Consortium Standard:

https://www.x.org/archive/X11R7.7/doc/xorg-docs/icccm/icccm.html

Conrad Parker, ICCCM rant, `slug-chat`, 12 July 2001, canonical copy:

https://github.com/porridgewithraisins/x11cp/blob/main/rant

Related in this directory: [ONE-DIMENSIONAL.md](ONE-DIMENSIONAL.md) for the five failure modes and
the per-platform survey, [UNDO-TREES.md](UNDO-TREES.md) for Emacs's kill ring as the same data
structure in a different address space, [BRANCHING-TIMELINES.md](BRANCHING-TIMELINES.md) for what a
content-addressed replacement looks like, and [SOURCES.md](SOURCES.md) for the quote ledger covering
the rest of the argument.
