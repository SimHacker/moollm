# Visual Programming Lineage: From Smalltalk to MOOLLM

A trail of ideas connecting constructionist education, visual programming,
character simulation, and modern LLM orchestration.

## The Thread

### 1960s: Pioneers

**Sketchpad** (Ivan Sutherland, MIT, 1963)
- First graphical user interface
- Direct manipulation of geometric objects
- Constraint-based graphics

**NLS/oNLine System** (Douglas Engelbart, SRI, 1968)
- The Mother of All Demos
- Collaborative editing, hypertext, windows
- Human augmentation through computing

**PIXIE** (Neil Wiseman, Heinz Lemke, John Hiles, Cambridge, 1969)
- "A New Approach to Graphical Man-Machine Communication"
- Light pen interaction with structured graphics
- CAD Conference Southampton, IEEE Publication 51
- [PIXIE Paper](https://www.donhopkins.com/home/documents/pixie.pdf)
- [Flight of the PIXIE (video remix)](https://www.youtube.com/watch?v=jDrqR9XssJI)

### 1970s-80s: Foundations

**Smalltalk** (Alan Kay, Xerox PARC)
- Objects all the way down
- Live editing environment
- Kids as target audience

**Logo** (Seymour Papert, MIT)
- Microworlds for learning
- Turtles as thinking tools
- "Learning by making"

**HyperCard** (Bill Atkinson, Apple)
- Stacks and cards metaphor
- Direct manipulation editing
- Scripting for everyone (HyperTalk)

### 1980s-90s: NeWS Era

**NeWS** (James Gosling, Sun)
- PostScript as code, graphics, AND data
- Networked extensible window system
- Architecturally similar to what became AJAX

**HyperLook** (Arthur van Hoff, Turing Institute)
- HyperCard for NeWS
- PostScript scripting
- Property sheets as editable stacks
- [HyperLook Article](https://medium.com/@donhopkins/hyperlook-nee-hypernews-nee-g...)

**PSIBER Space Deck** (Don Hopkins)
- Visual PostScript debugging
- "Consensual hallucination" of data structures
- [PSIBER Space](https://donhopkins.medium.com/the-shape-of-psiber-space-oct...)

### 1990s: Interval Research Era

At Interval Research Corporation (Paul Allen's "PARC for the 90s"),
several threads converged:

**Hookup** (David Levitt) · **Body Electric → Bounce** (Chuck Blanchard, then Levitt and Don)

**Two independently written dataflow languages.** Levitt wrote Hookup at MIT for
MIDI and music; Blanchard wrote Body Electric at VPL, in Pascal, for virtual
reality. The one code descent is the second arrow: when VPL broke up Levitt
acquired Body Electric, renamed it Bounce, and he and Don carried it forward.

| | Author | Where | For | Relationship |
|---|---|---|---|---|
| **Hookup** | David Levitt | MIT | MIDI, music, Director content | Independent |
| **Body Electric** | Chuck Blanchard | VPL | VR, devices, Swivel3D trees | Independent |
| **Bounce** | Levitt, then Don | Levity, Interval | Multimedia, components | Body Electric, renamed and extended |

**What crosses between them is a person and a library.** Levitt integrated
Macromedia's MMP library into Hookup himself; after joining VPL he added it to
Body Electric too. The shared component travelled in the designer's head and
hands. **The same engineer reached for the same solution twice, in two unrelated
languages, in two industries, a decade apart.**

**The most direct answer in this file to the claim that visual programming never
shipped anything real** comes from Body Electric's primary user rather than from
an advocate:

> "The piece was written entirely in Body Electric, a visual programming
> language for Virtual Reality. I am extremely fond of this software working
> environment, which was designed primarily by **Chuck Blanchard**. You hook up
> visual diagrams to control what happens in the Virtual world and **see the
> effect immediately**. All the music and physics was done in 'B.E.'; **I could
> never have made this thing in 'C'.**"
>
> — Jaron Lanier, on *The Sound of One Hand*

`verified: jaronlanier.com/instruments.html, recovered from the Wayback Machine
at 20061017223445. Local copy:
[sims/rescue-raw/jaron-lanier-instruments-2006.txt](./sims/rescue-raw/jaron-lanier-instruments-2006.txt)`

That last clause is the whole argument in nine words, from someone who could
certainly write C. Note also what he attributes it to: **immediate effect** — the
environment property, not the pictures.

### The company was named after the language, not the other way around

Worth stating plainly because Wikipedia currently has it wrong: **VPL stood for
Visual Programming Language.** Lanier settled it himself, describing how the
September 1984 *Scientific American* cover used one of his visual programming
experiments as its illustration, and an editor called in a panic because
contributors must list an affiliation:

> "I blurted out '**VPL Research**' (for **Visual Programming Language, or Virtual
> Programming Language**), and thus was born VPL. After the issue's publication,
> investors came calling, and a company came to exist in reality."

`verified: Lanier, "Virtually There," Scientific American, April 2001.`

Both expansions, singular *Language*, **visual first**. The Wikipedia article
gives only "Virtual Programming Languages," plural, cited to a C-SPAN page that
is a video listing and never expands the acronym at all. Don has filed the
correction on the talk page.

So the visual programming language is not something VPL Research got around to
building for its VR hardware. **The language came first and the company was named
after it** — which is the strongest available answer to reading Body Electric as
a scripting layer bolted onto a VR product.

### Hookup has descendants of its own, and the claim needs sorting

Hookup is filed here because of Levitt rather than for itself. A 2000 interview
with **Mark Coniglio**, who built Interactor and Isadora, puts it somewhere much
less peripheral:

> "In 1986 my soon-to-be mentor and Interactor collaborator Mort Subotnick had
> just come from a residency at MIT where he was using a program called **Hookup**
> created by a student there named David Levitt. **Hookup was the first program I
> know of that used the 'patch-cord' metaphor**, i.e., modules that manipulate
> data are linked by virtual wires, the connection of which is determined by the
> user."

And then, on what he built from it:

> "**Isadora and Max both inherit the modules linked by the patch-cord metaphor
> from Hookup.**"

`verified: Coniglio interviewed by Sher Doruff, sdela.dds.nl/sfd/isadora.html.`

**Sort those two claims apart, because they are not equally strong.**

| Claim | Status |
|---|---|
| Coniglio's own work descends from Hookup | **Direct.** He watched Subotnick use it, was hired to reimplement its ideas, and says he set out to copy its interface. Interactor 1987 → Isadora. |
| Hookup was first to the patch-cord metaphor | **Hedged by the claimant** — "the first program *I know of*." And he immediately names the real ancestor: "For those in the world of early analog, patch-cord programmed synthesizers, this was a familiar interface." |
| Max inherits it from Hookup | **Unsupported as stated.** Puckette's Max work at IRCAM is contemporaneous with Hookup, not downstream of it. Coniglio is generalizing from his own case. |

What survives is proximity, and it is more specific than the descent claim was.
**Levitt shared an office with Miller Puckette at MIT — 545 Technology Square,
the room known as the Music Hackers Hangout.** Hookup and Max are siblings from
one room.

The room was known by that name to the machines as well. **"Music Hackers
Hangout" was the registered location of the Lisp machine in that office**, so it
appeared as the site whenever you listed the Lisp machines or checked who was
logged in from one. Don slept on the beanbag chair next to the Lounge Lizard Lisp
Machine on the ninth floor.

`verified: Don Hopkins, from memory and personal experience. First-hand, not
documentary — the Lisp machine host tables would settle the location string if
anyone has a surviving dump.`

**Which puts Levitt at the origin of the patch-cord line in music software**, and
he is the man who later carried the MMP library, and then Bounce, out of that
world and into VR and multimedia. Hookup's own descendants are Interactor and
Isadora.

**Coniglio also names the property, in the same terms everyone else in this file
reaches for:**

> "Part of the thing I reacted to in Hookup was the way you could easily drop
> modules into the program and try things; a lot like you could do with the
> patch-cord synthesizers. I may not have realized it explicitly then, but this
> ability to **program improvisationally** allowed for that kind of artful
> playfulness that is so important."

Improvisational programming, Don's "extremely fun and productive zone," Lanier's
"debugging is as much a pleasure as making new stuff." Three people, three
decades, three industries, converging on liveness rather than on pictures.

### The precise technical difference from Max, which is a real distinction

Don spelled out in 2000 what separates the two, and it is sharper than
"they're both box-and-wire":

> "Bounce is similar to Max in many ways, but also quite different. It's **more
> data flow oriented than control flow oriented**, so it's like a whole
> electrical circuit all running at once, with data flowing between processing
> modules through wires, rather than control flow (the program counter) jumping
> from module to module through wires, like Max."

**Same picture, opposite semantics.** In Bounce the wires carry values and
everything evaluates continuously; in Max the wire is where the program counter
goes next. A diagram that looks identical means two different things.

And he states the cost of the pure-dataflow choice without softening it:

> "To implement conditionals, Bounce has a switching module like a relay, with
> one output that switches between two inputs under control of a third input; or
> you can enable and disable modules and nested sub-modules, using an implicit
> 'power' switch that turns modules on and off. To implement loops, it has a
> special nested container that executes its contents repeatedly until it returns
> a false value, **but that was pretty unwieldy.**"

**Continuous evaluation makes flow beautiful and control awkward.** A conditional
becomes a relay and a loop becomes a container with a weird contract — both
borrowed from circuits, because a circuit is what the model actually is. That is
the same negative result as the state problem, one level up: *pure dataflow
expresses flow well and everything else by analogy.*

### How Levitt came to own it

The provenance of Bounce turns out to be a debt settlement:

> "David Levitt legally acquired the rights to Body Electric when VPL broke up,
> **instead of money they owed him for Hookup.**"

Which also explains the Interval credit dispute below: Levitt held the rights
legitimately and Blanchard held the authorship, and those two facts came apart.

### Two more provenance details worth keeping

- **Body Electric was written in Pascal**, and "at some time it got converted to
  C through some automatic translator on an HP unix system." Don later described
  cleaning up "C code translated from Pascal, that no human had ever touched
  before." Anyone building Chuck's source tree should expect machine-translated C.
- **The liveness, described from inside:** "the simulation ran while you were
  editing it, so programming was very interactive, **like soldering on a live
  circuit, or defusing an atomic bomb.**"

`verified: all quotes in these four sections from bounce-notes.txt, mirrored at
[sims/rescue-raw/bounce-notes-2000.txt](./sims/rescue-raw/bounce-notes-2000.txt).`

### Who did what, settled

Lanier credits Body Electric's design primarily to Chuck Blanchard, and Don says
the same thing in his own words — **"Chuck Blanchard (who wrote Body
Electric)"** — so the lineage should name three people rather than one:

| | |
|---|---|
| **Hookup** | David Levitt — MIDI visual programming, at MIT |
| **Body Electric** | **Chuck Blanchard** wrote it, at VPL. Lanier was its principal user |
| **The Macromedia Director Player (MMP) library** | Levitt integrated it into Hookup, then into Body Electric after joining VPL. **It later became the browser plugin known as Shockwave** |
| **Bounce** | Levitt again, post-VPL at Levity — Body Electric acquired in lieu of money owed him for Hookup, then renamed and extended |
| **Bounce, ported and extended** | Don — PowerPC port, user interface, the COM plug-in and type extension system, multimedia support, at Levity and Interval |

`verified: Don Hopkins to Eric Hosick and a VPL mailing list including Brad
Myers, Ben Shneiderman, Alan Kay, Henry Lieberman, Ben Bederson and Arthur van
Hoff, 2014-03-07; Lanier to Don, 2007-01-03.`

### The shared library became Shockwave, and the browser got the weaker half

MMP is not a footnote. **Plugged into the browser it was renamed Shockwave**, and
for a stretch of the late nineties it was how the web had animation at all. But
the browser got the library running in its least interesting mode.

**Shockwave played canned Director files.** Body Electric used the same library
the other way round: **sprite and sound modules placing cast members on the stage
directly**, with the animation generated as it ran. Same playback engine, and the
difference is whether the frames exist before the program does.

**Lingo could do it that way, and almost nobody did.** The capability was in
Director all along; the working style around it was timelines, `go to frame`, and
simple expressions. So the dynamic mode of the library reached its fullest use in
a dataflow VR language rather than in the multimedia authoring tool it shipped
with.

**Which sets up the best one-line diagnosis of the timeline in this file.** Don
was hanging out with **Marc Canter** — MacroMind's founder, whose VideoWorks
became Director — when Canter pointed out what the **Score** actually is:

> A Director Score is a BASIC program rotated ninety degrees counter-clockwise,
> with line numbers and gotos.

`verified: Don Hopkins, recalling Marc Canter. The Score is Director's timeline
window: frames are the numbered columns, channels are the rows. Stewart Sharp, a
Director artist and programmer who worked with Canter, would stop by and show off
recent work.`

**Rotate a BASIC listing counter-clockwise and the line numbers, which ran down,
now run across.** That is the frame ruler. `GOTO 400` becomes `go to frame 400`.
The channels stacked underneath are the one thing BASIC did not have — parallel
tracks at each line number — which is exactly the part that made it good for
animation and left it a numbered-line language everywhere else.

**So the timeline is not the opposite of a patch graph, it is the opposite of
dataflow.** A Score fixes what happens at time *t* in advance; a patch graph
describes relationships and lets time fall out of evaluation. Levitt carried one
library into both worlds, and in Bounce it ended up serving the model the
timeline was built to avoid.

**And the wire types explain the COM fix.** Body Electric's native data types
were **integers, floating point numbers, and Swivel3D trees** — that is the
whole vocabulary. So the extension Don built was not a luxury:

> "One direction we took Bounce from its Body Electric roots was to extend it to
> support MacroMedia MOA plug-in objects (like cross platform COM components) for
> plug-in components and data types you could read and write on wires, and then
> we added components for loading structured data from text files (the equivalent
> of XML/JSON/YAML) and representing it as IMoaDict/IMoaArray interfaces (the
> equivalent of JSON) that you could pass between components on wires. It really
> made Bounce a lot more powerful, since **its original native data types were
> not nearly as flexible.**"

Read that against the reflection section below. Adding dictionaries and arrays
to the wires is the same move PSIBER made — **make the aggregate a first-class
thing you can pass around and open** — arriving by a different route, under
production pressure, a decade later.

### The sweet spot, and the objection to it

Don's summary of what the language proved is worth quoting exactly, because it
is a claim about a *reachable* design point rather than about one product:

> "I know there are a lot of visual programming languages, and that most of them
> really suck, but I don't think that's endemic to all VPLs. After using Body
> Electric / Bounce, **I know there is a sweet spot that's possible, where you
> can visually create and edit live programs while they're running**, which
> really enables you to get into an extremely fun and productive zone."
>
> "**Programming languages are user interfaces for programmers, not just abstract
> mathematical models**, and good user interface design is even more important
> for visual programming languages."

**And the strongest objection came from Ben Shneiderman, in the same thread**,
which is why it belongs here rather than in a footnote:

> "Visual languages have struggled to make commercial impact, but it has been a
> tough road. One issue is the **remarkable compactness of textual languages
> which offer easy search & replace, plus cut and paste.** So we still need some
> breakthroughs and the right situations to make VPL more widespread, but I'm a
> great fan of this direction."

That is the same complaint Don makes about SimAntics — *"acres of bizarre
spaghetti code"* with no way to list it out as text, grep it, or diff it. Two
people who each spent years building visual languages, naming the same missing
feature: **text is not a rival notation, it is the substrate that search,
replace, copy, diff and version control are built on.** A visual language that
cannot round-trip to text forfeits all of it.

Which is the argument for the position this repository takes — files first,
with structure — and the reason Don's proposal to Lanier was a language whose
underlying form is serializable, with the visual editor as one view of it.
Lanier's counter-argument, that serialization endangers update latency, is in
the same section below.

### The same objection from Guido van Rossum, phrased as an open request

Shneiderman's objection has a twin, made seven years earlier by the author of
Python, and it is still open. March 2007, OLPC Sugar list: a subthread had formed
around round-tripping a modified Python AST back to source, and Guido asked what
the point was.

> "I'm curious about **the focus on ASTs** that seems apparent in this subthread
> […] I've always been **more inclined to edit the text and re-parse from there,
> as it puts the author in control of formatting, comments etc.**, and this is how
> most 'real-world' environments work. **(Not that that necessarily makes it
> better, but neither is the opposite true.) Is someone willing to write up a
> brief comparison between the two approaches?**"

`verified: sugar@laptop.org 001750, 11 March 2007. Full thread archived in Don's
repo under characters/don-hopkins/correspondence/threads/2007-03-sugar-python-etoys-visual-programming/.`

**Two things in there are worth separating.** The parenthesis is a refusal to
claim his own side — unusual, and it is what makes the request a request rather
than a position. And the argument itself is not about pictures at all: it is
about **which representation is the ground truth**, because whichever one is
canonical is the one that keeps your formatting and your comments. He had just
offered the concrete answer for his side — the tool that became `2to3`, which
does source-to-source transformation and *"retains the exact formatting, comments
etc. of the input source code."* Text stays canonical; transformations are
functions on text.

**Nobody wrote the comparison.** Nineteen years later this file is a partial
answer to it, and it should say so plainly, because the three positions in that
thread are still the three positions:

| Position | Ground truth | Advocate, in that thread |
|---|---|---|
| **Text, transformed** | Source text; tools parse and re-emit it | Guido — formatting and comments survive, and every existing tool works |
| **Structure, rendered** | The tree; text is one view of it | the AST subthread; Ian Bicking's reading of Boxer as a middle — *"indentation is already a visual structure,"* plus non-text literals, *"all of that can be serialized to text"* |
| **A separate visual notation, compiled down** | Neither; the visual language is its own language | Don |

Don's, stated at the end of the thread, is the one this repository builds on:

> "I like the idea of having **visual meta-languages that are compiled into
> Python**, which avoids the problems of editing Python text or parse trees
> directly, and can support simplified '**kindergarten**' languages as well as
> more advanced forms."

`verified: sugar@laptop.org 001947, 20 March 2007.`

**That sidesteps the ground-truth fight rather than winning it.** If the visual
language compiles to Python instead of being a view of Python, then Python text
stays canonical for everything Guido cares about, and the visual notation is free
to be as unlike Python as a nine-year-old needs — including deliberately weaker.
The cost is a compiler and a debugging story across two levels, which is the
price the "one faithful view" position does not pay.

And he refuses the obvious corollary, which is where most kid-friendly tooling
goes wrong:

> "I think it would be wonderful to have a visual interface that **faithfully
> represented the full power and semantics of Python** (without trying to put a
> 'kid friendly' facade over it) […] Of course there's still a need for many
> different simple application-specific 'kid friendly' visual languages, but
> **when you drill down to real code, it's best to get the real thing** […]
> instead of some annoying watered-down half-baked ersatz Python (like 'safe
> python' in Zope, or smarty templates in PHP)."

`verified: sugar@laptop.org 001809.`

**Simplified notations on top, no crippled dialect underneath.** Which is Kay's
"pop the hood on practically everything" and Shneiderman's round-trip requirement
arriving at the same architecture from two directions.

- Hookup: Atari Cambridge/MIT Media Lab era, MIDI visual programming
- Body Electric: VPL Research, inherited MMP (Macromedia Director player)
- VR integration: Flock of Birds, Polhemus, DataGlove, Convolvotron
- Swivel3D articulated trees for bodies, hands, gesture recognition
- Broadcast positions via UDP to TWO SGI workstations (one per eye!)
- Jaron Lanier performed with VR musical instruments live
- Bounce: David's post-VPL version at Levity, Don Hopkins did UI
- COM/ActiveX integration: new wire types for JSON-like nested data
- Solved six-input-limit with polymorphic dictionary objects
- Don ported Bounce to PowerPC Mac and built a cross-platform plug-in
  architecture on COM, porting the ActiveX Template Library to the Mac to do it

**The lesson is the one worth carrying forward, because it is a negative
result stated by the people who built the thing:** *pure* dataflow becomes
unwieldy once complex state is involved, and the fix was to let opaque
objects — COM components — sit inside the graph and hold state, with richer wire
types to carry nested data between them.

**Note the word "opaque," because it is the whole cost.** The fix bought state
and paid for it in *reflection*: you can see the wire, and you cannot see inside
the box. A patch graph makes flow completely visible while making the thing the
flow passes through completely dark. That is the trade the next section is
about.

That is the same shape as the resolution in
[AXES-NOT-CAMPS.md](./AXES-NOT-CAMPS.md): not one mechanism winning, but a
visual layer for the connections and a symbolic layer for the state, each doing
what it is good at. A patch graph is a beautiful way to express *flow* and a bad
way to express *memory*.

Note also the pairing with Lanier's augmentation/automation axis — the same
Jaron Lanier, performing music with a dataflow language, is the person whose
review supplies that axis. The instrument was augmentation, literally.

## The axis that actually separates these systems: how far down does it go?

"Visual programming" is the wrong category. It groups things by how they look,
and the property that decides what you can *do* is **reflective depth** — how
much of the running system is reachable as a first-class object you can see,
inspect, name and edit, using the same machinery you use for everything else.

Ask it as one question: **can you drill down to everything, or does the drill
hit a floor?**

| System | The floor |
|---|---|
| Max/MSP, Body Electric, Bounce | The patch is visible; the objects in it are opaque. Flow is transparent, state is dark |
| Scratch | Scripts and sprites are visible; the interpreter and the block definitions are not |
| **Snap!** | Much lower — first-class functions, lists, continuations, and blocks that build blocks. "First class" is the design thesis, not a feature |
| **Smalltalk** | Nearly none — objects all the way down, classes are objects, the compiler is an object, the debugger edits live frames |
| **Self / Morphic** | None in the UI either. Every visible thing is a morph you can halo, open, and restructure; there is no separate editor mode because there is no separate editor |
| **SK8** | Apple's answer to the same question — an object system where everything authorable is an object, with a real language underneath, not a scripting veneer |
| **eToys / Squeak** | Halos on every morph, viewers that expose an object's variables and scripts to a child |
| **PSIBER Space Deck** | The extreme case, below |

**Uniformity is the property, not visibility.** Smalltalk and Self are not on
this list for being graphical — Smalltalk's syntax is text. They are here
because there is no privileged layer that the ordinary tools cannot open.

### PSIBER: the floor removed entirely

> **The Shape of PSIBER Space: PostScript Interactive Bug Eradication Routines**
>
> "The PSIBER Space Deck is an interactive visual user interface to a graphical
> programming environment, the NeWS window system. It lets you **display,
> manipulate, and navigate the data structures, programs, and processes living
> in the virtual memory space of NeWS**."

`verified: Don's own abstract, quoted from his 2006-10-29 mail to Bill Joy.
Paper and PostScript archived at art.net/~hopkins/Don/psiber/; demo film at
donhopkins.com/home/movies/PSIBERDemo.mov`

"Data structures, programs, **and processes**" is the claim that matters. Not a
visualization *of* the system — a direct interface *to* it, in the live memory
space, where the thing on screen is the thing itself.

**And the sharpest demonstration is what happens to a dictionary.** In PSIBER a
PostScript dictionary could be treated as a **command palette**: the same object
is a data structure when you inspect it and a menu when you use it, with no
conversion step and no separate palette-definition format. That is what removing
the floor buys you. Under a partial object model you need a palette *format*, a
palette *editor*, and glue mapping entries onto functions. Under a total one the
dictionary already is all three, because a name bound to executable code is
exactly what a menu item is.

**State the design intent before the cost, because they are easy to confuse.**
Don, on the OLPC list in 2007:

> "**The idea wasn't to invent a new visual language, just to implement a faithful
> visual representation of how the language really is**, with a direct
> manipulation interface for editing data and executing code."

Not a new notation. A view of an existing one, at full fidelity. Which is why
PostScript was the right substrate — *"a lot like Lisp […] because PostScript
programs are simply executable arrays containing names, literals, primitive
operators, nested arrays"* — and why the same deck could inspect a running
thread's dictionary stack, operand stack and execution stack.

### The bill for removing the floor, itemised by the person who removed it

Every celebration of reflective depth in this file owes a debt to this paragraph,
so it goes right here rather than in a caveats section at the end:

> "One problem with PSIBER was that it was **too easy to make a mistake dragging
> and dropping, and accidentally totally hose the internals of the window
> system**, since you were editing shared structures in the NeWS server, like
> classes and canvases and event handler threads! **It needed some kind of
> read-only safety shield or edit mode switch.**"

`verified: sugar@laptop.org 001809, 13 March 2007.`

**Direct manipulation of a live system includes direct destruction of it.** The
floor was not only protecting you from the implementation, it was protecting the
implementation from you — and a system with no floor and no guard rail hands a
drag gesture the same authority as a deliberate edit. Note what he asks for as
the fix: not less reflection, but a **mode** — a read-only shield you take off on
purpose. Depth stays; the accident budget gets a switch.

That is the same shape as the resolution everywhere else in this file. Full
access, plus an explicit gate on the consequential step.

### Why 3D changes the stakes rather than the principle

The version of this Don and Lanier were arguing about is stronger: **represent
all data as first-class objects in 3D, with full reflection.** 3D does not make
the reflection deeper — a dictionary is no more open for being a cube. What it
adds is *room*: spatial arrangement, containment, adjacency and scale become
free notation, so a large structure can be navigated by moving rather than by
scrolling a tree. The peril is equally structural — occlusion, and objects that
look manipulable but are pictures.

Which is why Body Electric belongs in this section and not only in the Interval
one. It went furthest toward objects-in-space that you really operate on, and
then hit the state problem, and the fix — opaque COM components — **reintroduced
the floor.** The most reflective system on the list and the one that had to
compromise reflection to ship are the same system.

That tension is unresolved rather than settled, and it is the reason this
repository keeps skills as inspectable files: a directory is a dictionary you
can open, and a `CARD.yml` is a command palette that is also just data. Same
move as PSIBER's, in a substrate with no graphics at all.

### Lanier's own verdict, which is split down the middle on purpose

The retrospective assessment turns out to exist in two places, and the split is
the point — the same person rates the same system best and worst in one sentence:

> "The VPL software is **both the best and the worst VR software ever made.** It
> has infuriating limitations and wasn't maintained during VPL's long dark ages
> of French stupor (1992-1998), but it is also the most inspiring, seductive
> virtual world creation toolkit I have ever seen (though of course I might be
> biased)."

And on the language specifically:

> "Body Electric is a rare example of a successful visual programming language
> that is **seductive at first approach, but also scales** and has been used for
> industrial strength applications. It was created by Chuck Blanchard. The worst
> thing about it is that the only viable version runs on… the Macintosh. On the
> other hand… **It is absurdly fast — an incremental compiler.** It is also the
> only programming tool of which I can say that **debugging is as much a pleasure
> as making new stuff.** If you are familiar with programming tools, and VR tools
> in particular, you know this is almost a supernatural claim, yet it's true."

`verified: jaronlanier.com/vpl.html.`

**Take the debugging claim seriously, because it is the rarest one in this
document.** Every system here argues that its notation makes *construction*
better. Lanier is claiming something else: that inspection was as pleasant as
authoring. **Chuck's screenshots corroborate it structurally** — `Break` and
`StripChart` sit in the standard primitive palette alongside `Constant` and
`Slider`, so a breakpoint and a live value-over-time plot are things you drop
into a wire, not a separate tool you switch to. Liveness plus a graph means the
debugger and the editor are the same surface. That is the property Don named as
the sweet spot, described from the other side.

Which sets up the harder judgment, from Lanier's 1999 letter to Don. It is a
public rebuke aimed at the VRML community, and the most useful passage in the
archive for this document:

> "There IS a community of Body Electric users. **It is STILL building the most
> interactive 3D virtual worlds of any tool** (though Alice, from Carnegie
> Mellon, is the other hot contender). **That's SHAMEFUL!** While BE sucks in
> every other way, all the more recent vr design tools, **especially the vrml
> ones, simply avoid the problem of deep interactivity. How could the community
> be so whimpy, at this late date?**"

**Read "SHAMEFUL" carefully — the shame is aimed at the field, not the tool.** He
is saying that a decade-old unmaintained Macintosh program still held the record,
and that this was an indictment of everyone who had shipped since.

**A system can be bad at nearly everything and still be the only one attempting
the hard part.** Deep interactivity — the world reacting continuously to
everything, in real time, editable while running — is what BE went after and what
the standards-track successors declined. *Bad-at-the-hard-thing beats
polished-at-the-easy-thing*, and a field can regress for a decade while every
individual tool improves.

**The plea went unanswered.** VRML never grew a deep interactivity model; its
scripting stayed bolted-on, the successor standard X3D inherited the same shape,
and the format was overtaken rather than fixed. What eventually carried live 3D
on the web came from elsewhere entirely — WebGL and the engine ecosystem — and
arrived without the property Lanier was asking for. **Nobody built the thing, and
nobody argued back either.**

`verified: quote from Lanier to Don, 1999, mirrored at
[sims/rescue-raw/bounce-notes-2000.txt](./sims/rescue-raw/bounce-notes-2000.txt).
The assessment of what VRML and X3D did next is this document's, not his.`

### And Lanier's answer on how far down it should go

Don's argument in this section — represent all data as first-class objects, with
full reflection — got a reply from Lanier that reaches the same place from
cognition rather than from Smalltalk:

> "I had always thought the swivel tree was ridiculous, of course, but on the
> other hand I liked the idea that **the virtual world and the knowledge base
> were the same thing** — that unity encourages the **visibility and grabbability**
> of the underlying concepts. I think the brain works that way — **there isn't
> some barrier behind which everything gets abstract — instead, it's user
> interface all the way to the bottom!** What I think would be the coolest
> long-term destination of BE would be extending the scenegraph so that it was as
> powerful a knowledge base as you'd want…"

`verified: Lanier to Don, 1999-07-08, in bounce-notes.txt.`

**"User interface all the way to the bottom" is this section's thesis in six
words, and it was arrived at independently.** Not from the Smalltalk lineage, but
from a claim about minds: that there is no level at which representation stops
being manipulable. And notice he concedes the implementation was *ridiculous* in
the same breath — the scene graph was a bad knowledge base — while defending the
unification. **Right architecture, wrong data structure.** Which is exactly the
gap the dict/array wire types later closed, and exactly the gap opaque COM
components later reopened.

`open: Sun acquired Body Electric with VPL's assets, declined an open source
release, and offered Lanier six hacking licences at a time. He notes the source
was printed in the granted patents, so it is arguably already public on paper.
Chuck Blanchard confirmed in 2020 that he still has a compiling source tree.
Recovery leads are tracked in the private archive rather than here.`

`todo: Don's own "Bounce Stuff" is on Medium and belongs in
[sims/MEDIUM-RESCUE.md](./sims/MEDIUM-RESCUE.md)'s queue. bounce-notes.txt is
served from donhopkins.com and should be mirrored locally. Body Electric 7.0.1a1
for PowerPC is on local disk at Code/BodyElectric.`

**MediaFlow** (Marc Davis)
- Visual programming for video processing
- Semantic annotation (before AI vision)
- "Professional video by hobbyists with camcorders"
- [MediaFlow Design Discussion](https://donhopkins.com/home/interval/mediaflow-design.html)

**Embedded Constraint Graphics** (Tom Ngo)
- Create interactive graphics from target examples
- Interpolate between states on simplicial complexes
- Patent US5933150

**Component Technology Survey** (Don Hopkins)
- [Pluggers Survey](https://donhopkins.com/home/interval/pluggers) — snapshot of 1996
- [IFC vs Bongo](https://donhopkins.com/home/interval/ifc-vs-bongo.html) — Java frameworks compared

Key insight from Richard Gabriel's *Patterns of Software*:
> "Data and control abstractions are generally best when they are codesigned,
> and this is rarely done any more."

### 1996-2000: The Sims Era

**SimAntics** (Maxis/EA) — the visual programming language the characters run on.
The name is a pun on *semantics*, and it is the most widely deployed visual
programming language in this whole lineage: it shipped inside a game that sold
in the tens of millions, and players edited it.

- Character simulation visual programming language
- Simple local rules → complex global behavior
- Players as authors, not just consumers

**It did not start with The Sims — it came from SimCopter, and that matters for
this document.** SimAntics is a link in a chain rather than a one-off:

> "Edith lets you view and edit SimAntics code, which is the visual programming
> language for scripting the behavior of The Sims. […] The SymAntics [sic]
> language was used to program the people in SimCopter, and Edith evolved out of
> that."
> — Don Hopkins, SimWatch list, 2000-08-26

`verified: recovered primary source; text and provenance in
[sims/MEDIUM-RESCUE.md](./sims/MEDIUM-RESCUE.md). The email uses the early
"SymAntics" variant; the established spelling is SimAntics.`

So the sequence is **SimCopter people → the language → The Sims**, with the
editor evolving alongside the language rather than being bolted on after.

**Two things that sentence gets wrong if read carelessly**, and both matter for a
lineage document:

**1. Edith did not exist under that name yet.** The name arrived with the
Windows port and the integration into The Sims. SimCopter used an earlier
version of the environment, unnamed as far as anyone here recalls. Don did the
Windows port himself, which is the basis for the correction — and the naming
story dates itself, because it comes out of a Sims-specific design phase:

> "There was one terrible phase we went through, trying to frame it like a
> simulated situation comedy, complete with a laugh track. That resulted in the
> first characters being named Edith and Archie (and **I named the visual
> programming tool 'Edith' for Edit House**)."

`verified: Don Hopkins, quoted in
[sims/sims-team-history.md](./sims/sims-team-history.md). The name is downstream
of The Sims' sitcom phase, so it cannot predate The Sims — which rules out
SimCopter, 1996.`

**2. "SimAntics" is probably also a later coinage.** The working name was **Tree
Programming**, and the artifacts were **tree code** and **tree tables** — terms
that survive in the shipped Edith menus (*Tree Editor*, *Tree Tracer*) and in
the primitives documentation. When the name SimAntics was coined is unknown.

There is dated corroboration for the working name. Reviewing The Sims Design
Document Draft 3 in **August 1998** — two years after SimCopter shipped, with
The Sims in development — Don writes:

> "The whole relationship design and implementation (**I've looked at the tree
> code**) is Heterosexist and Monosexist."

`verified: August 1998, quoted in
[sims/sims-inclusivity.md](./sims/sims-inclusivity.md). Note the term he reaches
for unprompted, in writing, in 1998: tree code.`

### The Himbo easter egg was written in it

Jacques Servin's easter egg in SimCopter — the "himbos" who appear and kiss —
**was tree code.** Which makes it the most consequential program ever written in
this language other than The Sims itself: it got Servin fired, it forced a
public Maxis position on not being anti-gay, and that position is precisely what
Don leveraged in the 1998 memo above. See
[sims/sims-inclusivity.md](./sims/sims-inclusivity.md) and
[../skills/no-ai-ideology/](../skills/no-ai-ideology/).

The egg was behavioral rather than cosmetic — characters spawning and
interacting — which is exactly the layer tree code controls, so the attribution
is consistent with the architecture as well as with memory.

**And the chain has one more link than the public story does.** The position
Maxis was pushed into is part of why Don was willing to work there, which means
a program written in this language changed who was prepared to write programs in
it next. Set out in full in
[sims/sims-inclusivity.md](./sims/sims-inclusivity.md).

### Open question: what was authoring actually like, and on what machine?

**Marked as inference, not record.** For The Sims, before the environment was
ported to Windows, the workflow was sneakernet and Don was there for it:

> Will would author on his Mac and carry the work in on a floppy — IFF files —
> and the team would drop them into place.

The reasonable guess is that SimCopter worked the same way, possibly with
Servin authoring on his own Mac rather than Will writing everything. The
supporting argument is an absence: **porting the editor from Mac to Windows was
a large job — Don did it for The Sims — and he would expect to have heard about
it if someone had already done it for SimCopter.** No such port is remembered,
so Mac-plus-sneakernet is the parsimonious explanation.

`todo: confirm with Jacques Servin and Will Wright rather than leaving this as
inference. Specifically — what OS and tools did Servin use? Was the language
called anything yet, and when was "SimAntics" coined? Was SimCopter's workflow
the same floppy-and-IFF sneakernet? Did Servin author his own tree code or hand
it to someone?`

**Edith** — the editor, and the reason this belongs in a *lineage* rather than a
catalogue. Named for Edith Bunker, the first mother Sim, and doubling as "EDIT
House." It was compiled *into* The Sims rather than shipped alongside it, and
the payoff is the property every environment-side language in this document is
chasing:

> "Edith has grown a lot and is much wiser, now that she's integrated into The
> Sims instead of running as a separate program, so she is actually able to
> **debug and edit code and data while it's running live in the game**."

That is the Smalltalk image property, reached by a commercial game studio for
production reasons. It also cost what liveness always costs: Edith was never
publicly released, and the blocker was *documentation*. See
[AXES-NOT-CAMPS.md](./AXES-NOT-CAMPS.md) on the notation-side/environment-side
trade this exemplifies.

### What happened to the notation afterwards, over four versions

The execution model outlived the notation, and the notation was replaced twice:

| Version | How behavior is authored |
|---|---|
| The Sims 1 | **SimAntics tree code**, edited in Edith. Bespoke visual language |
| The Sims Online | SimAntics — later reimplemented from scratch by the FreeSO project |
| The Sims 2 | Still SimAntics BHAVs; community tools such as SimPE edit them directly |
| The Sims 3 | **C# on .NET/Mono.** Mods are class libraries compiled against `ScriptCore.dll`, `SimIFace.dll`, `Sims3GameplayObjects.dll`, packaged as `S3SA` resources |
| The Sims 4 | **Python** — gameplay ships as `.pyc` under `simulation/` and `core/`, mods package as `.ts4script` |

`verified: Sims 3's C#/.NET toolchain and Sims 4's Python confirmed against
modding documentation (Mod The Sims, SimsWiki, Sims 4 scripting templates),
2026-09-07. Sims 4 sat on Python 3.7 long enough that the whole decompiler
ecosystem targets it.`

**The advertisement mechanism survived the notation changes, and became
declarative.** In Sims 3 it is `ITUN` — Interaction Tuning — XML resources
carrying advertised motive deltas, with an `updateType` of `ImmediateDelta` or
`ContinuousFlow`. A modding tutorial describes the consequence exactly as Wright
would have:

> "you can rip your sims off by telling them this interaction will be very fun,
> which in actual fact it wouldn't be!"

That is Sims 1 advertising, intact, twelve years and two languages later — an
object claiming a motive payoff, the Sim choosing on the claim, and the claim
free to lie. The mechanism was never tied to the visual notation. It was tied to
the **execution model**, which is why MOOLLM can borrow it from Sims 1 without
inheriting tree code — see
[ADVERTISEMENT-AUCTION.md](./ADVERTISEMENT-AUCTION.md).

**MOOLLM models Sims 1 deliberately, and that is the right target** — not
because later versions are worse, but because Sims 1 is where the mechanism is
*legible*: design documents, tree code, firsthand accounts. Sims 3 and 4 extended
it and buried it in proprietary tuning data that has to be decompiled to read.

**Why that much effort for a language nobody outside the building used.** Jamie
Doornbos wrote it; Don ported it to Windows and made it easier to use; **Patrick
J Barrett III wrote the most of it and became the resident expert**, adopting it
fully and making it "much more colorful"; other programmers wrote it too; and Will
Wright was among the users. The investment is not justified by user count — **it
is justified by whose iteration cost you are lowering.** Wright is rare enough
that making his loop faster changes what gets designed, so tooling spent on a
handful of designers' throughput can return more than tooling spread across
thousands. This is the strongest case in this whole file for visual programming
as a *leverage* technology rather than a mass-adoption one, and it is the
opposite of how the field usually argues for it.

Will Wright's progression:
- SimAnt: Too simple
- SimEarth: Too complex  
- SimCity 2000: Just right
- The Sims: EVEN SWEETER — simple for kids, complex for artists

Don's contributions:
- **Architectural editing and object placement tools** — the build-mode surface
  players spend most of their time in
- **Character animation system, pipeline and tools** — the path from authored
  motion to a Sim performing an interaction
- **User-created content tools** — the ones listed below, treated as part of the
  product rather than as an afterthought
- SimAntics ported from Mac to Windows, documented and cleaned up, made easier to
  use
- Pie menu interaction system
- Extensive testing and exploration

**Three of those four are notation-adjacent rather than notation.** Build mode,
the animation pipeline, and the content tools are all editors over the same
object model SimAntics scripts against — which is why they belong in a document
about visual programming. The player dragging a wall and the designer wiring a
behavior tree are manipulating the same world representation at different
levels, and the animation pipeline is what makes a tree node resolve into
something visible on screen.

**User-Created Content Tools** (Don Hopkins, Maxis/EA)
- SimShow: Pre-release tool for character skins — fans hit ground running
- Transmogrifier (TMog): OLE component for custom objects without 3D Studio
  — <https://thesimstransmogrifier.com/>
- rug-o-matic: Template + drag-drop = storytelling "rugs" (title+description+image)
- Fan communities (Yahoo Groups, personal blogs) = social currency economy
- Heather "SimFreaks" + Steve "SimSlice" met in fandom, got married!

### 2000s-2010s: Constructionist Platforms

**Scratch** (Mitchel Resnick, MIT Media Lab)
- Block-based visual programming
- Seymour Papert's constructionism realized
- Millions of young programmers

**Snap!** (Brian Harvey, Jens Mönig)
- First-class procedures and data
- Build Your Own Blocks
- Connects to Berkeley CS curriculum

### 2020s: MOOLLM

MOOLLM synthesizes these threads:

**From Self's Prototype OOP:**
- "OOP RISC microcode" — so simple you can build other OOP systems in it:
  - Instance/class (Smalltalk)
  - Morphic composition
  - CLOS generic dispatch
  - HyperCard delegation
  - **COM IUnknown / OLE IDispatch**
- Multiple interfaces per directory (ROOM+CHARACTER, SKILL+CHARACTER, etc.)
- Battle-tested patterns, extremely well represented in training data
- Solves real problems: discovery, versioning, extension points, and aggregation
  complementing interface inheritance, multiple inheritance and latent-space
  inheritance rather than replacing any of them
- Dovetails with the other interlocking object systems
- Just another way of looking at directories full of files
- The ground truth multiverse lives in GitHub

**From COM/OLE (Microsoft) → MOOM/MOOLE:**
- IUnknown: "QueryInterface" = check if directory has ROOM.yml, CHARACTER.yml, etc.
- Multiple interfaces sharing state: one directory, many .yml schemas
- **CARD.yml is like IDispatch** — advertisements + interface definitions for 
  high-level polymorphic dispatch, automatically binding parameters from context,
  natural language triggers, skill composition, K-line activation
- IDispatch: late-bound method invocation = LLM interpretation of affordances
- Aggregation as well as inheritance, complementing it: tear-off interfaces,
  other cool tricks. **Complementing all three kinds at once** — interface
  inheritance from IUnknown, multiple inheritance through the ordered `parents:`
  list, and
  [latent-space inheritance](./object-system/LATENT-SPACE-INHERITANCE.md) from
  named concepts in the training data. Aggregation carries implementation reuse,
  which none of the three provides
- See: [DIRECTORY-AS-IUNKNOWN.md](DIRECTORY-AS-IUNKNOWN.md)

**From Minsky's Society of Mind:**
- Debating experts, not single-voice averaging
- K-lines as tradition activation
- NO-AI-* suite prevents pathologies

**From constructionism:**
- Microworlds for exploration
- Learning by building
- Students as researchers

**From The Sims:**
- Character simulation with emergent behavior
- Speed-of-light: 8 characters × 99 turns in ONE call
- Memory + reflection + planning (realized with LLMs)

**From GitHub as MMORPG:**
- Social collaboration features as game mechanics
- Characters as bots in discussions, reviews, flame wars
- Branches as parallel universes

**Layered Multi-Paradigm Integrated Object Systems:**

All seamlessly interoperating together — ALL WELL DEFINED IN TRAINING DATA:

| System | Contribution |
|--------|--------------|
| Self | Prototype OOP as RISC microcode |
| Morphic | Composition, direct manipulation — full family tree in [MORPHIC-LINEAGE.md](MORPHIC-LINEAGE.md) |
| Dan Ingalls' Lively Kernel | Web-native Morphic |
| Smalltalk | Message passing, everything is an object |
| Python, JavaScript, TypeScript | Modern dynamic languages |
| NeWS/PostScript | Code as data as graphics |
| HyperCard/HyperTalk | Almost natural language scripting |
| C++ | Multiple inheritance → multiple vtables |
| Objective-C | Message forwarding, categories |
| COM/OLE → MOOM/MOOLE | IUnknown, IDispatch, aggregation |
| ScriptX/CLOS | Generic functions, multiple dispatch |
| LispM Flavors | Mixins, method combination |
| Simula | Original OOP, simulation focus |
| Actors | Message passing concurrency |

**Reactive Programming & Constraint Systems:**

| System | Type | Contribution |
|--------|------|--------------|
| **Svelte 5 Runes** | Push | Compiler-driven fine-grained reactivity. Fucking awesome! |
| OpenLaszlo | Push | Declarative constraints compiled to Flash, worked with Henry Minsky |
| Garnet (Brad Myers, CMU) | Pull | Built on KR (Knowledge Representation) Lisp frames library. **Structural inheritance** — see [GARNET-AMULET-PROTOTYPE-SYSTEM.md](GARNET-AMULET-PROTOTYPE-SYSTEM.md) |
| React | (barely) | Virtual DOM diffing, NOT as reactive as its name claims |

**Push vs Pull Constraints:**

- **OpenLaszlo (Push/Eager):** When source changes, propagate immediately.
  Better for responsive UIs in Flash/ActionScript runtime.
  Don worked there with Henry Minsky and other MIT Lisp hackers.
  
- **Garnet (Pull/Lazy):** Compute only when value is requested.
  Better for high-latency environments (X11 round trips).
  Don worked on this with Brad Myers at CMU.
  Built on KR (Knowledge Representation) — Lisp GOFAI frames library.
  
- **Svelte 5 Runes:** Best of both worlds via compiler magic!
  `$state` = reactive source, `$derived` = computed value,
  `$effect` = side effects. Business logic AND UI can be reactive!

We're using **SvelteKit** for our web stack. Delightful to use, great community.
Not as well represented in training data as React (SO popular), but
Svelte has a pretty big dedicated community — not such an underdog.

**Instance Substitution Principle** (Oliver Steele at Laszlo Systems):
An instance can be replaced by its inline definition, and vice versa.
This enables **Instance-First Development**: build specific, then generalize.
Svelte components embody this — refactoring inline to component is trivial.

See: `MicropolisCore/laszlo/micropolis/README.md` — long essay comparing
OpenLaszlo/Garnet constraints to Svelte 5 runes.

## The Connection to Generative Agents

The Stanford Generative Agents paper (Park et al., 2023) finally builds
what we designed in 1997 but couldn't implement without LLMs:

| The Sims (1997) | Generative Agents (2023) |
|-----------------|--------------------------|
| Motive tracking | Reflection mechanism |
| Social relationships | Memory streams |
| Activity scheduling | Planning architecture |
| Emergent behavior | Valentine's Day party |

MOOLLM extends this with:
- Multiple debating perspectives (not averaged)
- GitHub as persistent world state
- Composable Anthropic skills
- Real-world AIOps applications

## Resources

- [Stanford Generative Agents Welcome](STANFORD-GENERATIVE-AGENTS-WELCOME.md)
- [MOOLLM Skills Index](../skills/INDEX.yml)
- [The X-Windows Disaster](https://donhopkins.medium.com/the-x-windows-disaster-128d398...)
- [Designing User Interfaces to Simulation Games](https://donhopkins.medium.com/designing-user-interfaces-to-simulation-games-bd7a9d81e62d)

---

*This document traces the intellectual lineage from Papert and Kay through
The Sims to modern LLM-based agents. The thread is continuous: microworlds,
direct manipulation, character simulation, constructionist learning.*
