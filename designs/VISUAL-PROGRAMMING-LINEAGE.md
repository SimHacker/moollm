# Visual Programming Lineage: From Smalltalk to MOOLLM

A trail of ideas connecting constructionist education, visual programming,
character simulation, and modern LLM orchestration.

## The Thread

### 1960s: Pioneers

**Sketchpad** (Ivan Sutherland, MIT, 1963)
- Early interactive graphical interface
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

These are two independently written dataflow languages. Levitt wrote Hookup at MIT for
MIDI and music; Blanchard wrote Body Electric at VPL, in Pascal, for virtual
reality. The one code descent is the second arrow: when VPL broke up Levitt
acquired Body Electric, renamed it Bounce, and he and Don carried it forward.

| | Author | Where | For | Relationship |
|---|---|---|---|---|
| **Hookup** | David Levitt | MIT | MIDI, music, Director content | Independent |
| **Body Electric** | Chuck Blanchard | VPL | VR, devices, Swivel3D trees | Independent |
| **Bounce** | Levitt, then Don | Levity, Interval | Multimedia, components | Body Electric, renamed and extended |

What connects them is a person and a library. Levitt integrated Macromedia's
MMP library into Hookup himself, and after joining VPL he added it to Body
Electric too. The same engineer used the same library in two unrelated
languages built for different industries.

A direct answer to the claim that visual programming never produced real work
comes from Body Electric's main user:

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

Lanier could write C. He attributes the difference to seeing the effect
immediately, which is a property of the environment rather than of the pictures.

### VPL was named after the language

VPL stood for Visual Programming Language. Lanier described how the
September 1984 *Scientific American* cover used one of his visual programming
experiments as its illustration, and an editor called in a panic because
contributors must list an affiliation:

> "I blurted out '**VPL Research**' (for **Visual Programming Language, or Virtual
> Programming Language**), and thus was born VPL. After the issue's publication,
> investors came calling, and a company came to exist in reality."

`verified: Lanier, "Virtually There," Scientific American, April 2001.`

He gives both expansions, with singular *Language* and visual first. The
Wikipedia article gives only "Virtual Programming Languages," plural, cited to a
C-SPAN page that is a video listing and does not expand the acronym. Don has
filed the correction on the talk page.

So visual programming was not something VPL Research added later for its VR
hardware. The language came first and the company was named after it, which
argues against reading Body Electric as a scripting layer added to a VR
product.

### Hookup's descendants

Hookup is listed here because of Levitt rather than for itself. A 2000 interview
with Mark Coniglio, who built Interactor and Isadora, gives it a more central
place:

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

These claims are not equally well supported.

| Claim | Status |
|---|---|
| Coniglio's own work descends from Hookup | Direct. He watched Subotnick use it, was hired to reimplement its ideas, and says he set out to copy its interface. Interactor 1987 → Isadora. |
| Hookup was first to the patch-cord metaphor | Hedged by the claimant: "the first program *I know of*." He then names the real ancestor: "For those in the world of early analog, patch-cord programmed synthesizers, this was a familiar interface." |
| Max inherits it from Hookup | Unsupported as stated. Puckette's Max work at IRCAM is contemporaneous with Hookup, not downstream of it. Coniglio is generalizing from his own case. |

What the record supports is proximity. Levitt shared an office with Miller
Puckette at MIT, at 545 Technology Square, in the room known as the Music
Hackers Hangout. Hookup and Max are siblings from one room.

The machines used that name too. "Music Hackers
Hangout" was the registered location of the Lisp machine in that office, so it
appeared as the site whenever you listed the Lisp machines or checked who was
logged in from one. Don slept on the beanbag chair next to the Lounge Lizard Lisp
Machine on the ninth floor.

`verified: Don Hopkins, from memory and personal experience. First-hand, not
documentary — the Lisp machine host tables would settle the location string if
anyone has a surviving dump.`

This places Levitt early in the patch-cord line in music software. He later carried the MMP library, and then Bounce, out of that
world and into VR and multimedia. Hookup's own descendants are Interactor and
Isadora.

Coniglio also names the property that others in this file describe:

> "Part of the thing I reacted to in Hookup was the way you could easily drop
> modules into the program and try things; a lot like you could do with the
> patch-cord synthesizers. I may not have realized it explicitly then, but this
> ability to **program improvisationally** allowed for that kind of artful
> playfulness that is so important."

Coniglio's improvisational programming, Don's "extremely fun and productive
zone," and Lanier's "debugging is as much a pleasure as making new stuff" all
describe liveness rather than pictures.

### How Bounce differs from Max

Don described in 2000 what separates the two:

> "Bounce is similar to Max in many ways, but also quite different. It's **more
> data flow oriented than control flow oriented**, so it's like a whole
> electrical circuit all running at once, with data flowing between processing
> modules through wires, rather than control flow (the program counter) jumping
> from module to module through wires, like Max."

In Bounce the wires carry values and everything evaluates continuously; in Max
the wire is where the program counter goes next. Diagrams that look the same
mean different things.

He also describes the cost of the pure-dataflow choice:

> "To implement conditionals, Bounce has a switching module like a relay, with
> one output that switches between two inputs under control of a third input; or
> you can enable and disable modules and nested sub-modules, using an implicit
> 'power' switch that turns modules on and off. To implement loops, it has a
> special nested container that executes its contents repeatedly until it returns
> a false value, **but that was pretty unwieldy.**"

Continuous evaluation makes flow easy to express and control awkward. A
conditional becomes a relay and a loop becomes a container with an unusual
contract, both borrowed from circuits, because the model is a circuit. This is
related to the state problem described below: pure dataflow expresses flow
directly and everything else by analogy.

### How Levitt came to own it

Levitt acquired the basis of Bounce in settlement of a debt:

> "David Levitt legally acquired the rights to Body Electric when VPL broke up,
> **instead of money they owed him for Hookup.**"

This is why rights and authorship came apart: Levitt held the rights
legitimately, and Blanchard was the author.

### Two more provenance details

- Body Electric was written in Pascal, and "at some time it got converted to
  C through some automatic translator on an HP unix system." Don later described
  cleaning up "C code translated from Pascal, that no human had ever touched
  before." Anyone building Chuck's source tree should expect machine-translated C.
- Liveness, as Don described it: "the simulation ran while you were
  editing it, so programming was very interactive, **like soldering on a live
  circuit, or defusing an atomic bomb.**"

`verified: all quotes in these four sections from bounce-notes.txt, mirrored at
[sims/rescue-raw/bounce-notes-2000.txt](./sims/rescue-raw/bounce-notes-2000.txt).`

### Who did what

Lanier credits Body Electric's design primarily to Chuck Blanchard, and Don says
the same in his own words ("Chuck Blanchard (who wrote Body
Electric)"), so the lineage should name three people rather than one:

| | |
|---|---|
| Hookup | David Levitt: MIDI visual programming, at MIT |
| Body Electric | Chuck Blanchard wrote it, at VPL. Lanier was its principal user |
| The Macromedia Director Player (MMP) library | Levitt integrated it into Hookup, then into Body Electric after joining VPL. It later became the browser plugin known as Shockwave |
| Bounce | Levitt again, post-VPL at Levity: Body Electric acquired in lieu of money owed him for Hookup, then renamed and extended |
| Bounce, ported and extended | Don: PowerPC port, user interface, the COM plug-in and type extension system, multimedia support, at Levity and Interval |

`verified: Don Hopkins to Eric Hosick and a VPL mailing list including Brad
Myers, Ben Shneiderman, Alan Kay, Henry Lieberman, Ben Bederson and Arthur van
Hoff, 2014-03-07; Lanier to Don, 2007-01-03.`

### MMP and Shockwave

Packaged as a browser plugin, MMP was renamed Shockwave, and in the late 1990s it
was a common way to put animation on the web. In the browser it mostly ran in
its simplest mode.

Shockwave played prepared Director files. Body Electric used the same library
the other way round: sprite and sound modules placed cast members on the stage
directly, and the animation was generated as it ran. Same playback engine, and the
difference is whether the frames exist before the program does.

Lingo could also work this way, but it was seldom used like that. The capability
was in Director all along; the usual working style was timelines, `go to frame`,
and simple expressions. So the dynamic mode of the library got more use in a
dataflow VR language than in the multimedia authoring tool it shipped with.

Don was spending time with Marc Canter (MacroMind's founder, whose VideoWorks
became Director) when Canter described what the Score is:

> A Director Score is a BASIC program rotated ninety degrees counter-clockwise,
> with line numbers and gotos.

`verified: Don Hopkins, recalling Marc Canter. The Score is Director's timeline
window: frames are the numbered columns, channels are the rows. Stewart Sharp, a
Director artist and programmer who worked with Canter, would stop by and show off
recent work.`

Rotate a BASIC listing counter-clockwise and the line numbers, which ran down,
now run across: that is the frame ruler. `GOTO 400` becomes `go to frame 400`.
The channels stacked underneath are what BASIC did not have, parallel tracks at
each line number. That made it good for animation and left it a numbered-line
language everywhere else.

In this sense the timeline is the opposite of dataflow. A Score fixes what happens at time *t* in advance; a patch graph
describes relationships and lets time fall out of evaluation. Levitt carried one
library into both worlds, and in Bounce it ended up serving the model the
timeline was built to avoid.

The wire types explain the COM extension. Body Electric's native data types
were integers, floating point numbers and Swivel3D trees, and nothing else, so
the extension Don built was needed:

> "One direction we took Bounce from its Body Electric roots was to extend it to
> support MacroMedia MOA plug-in objects (like cross platform COM components) for
> plug-in components and data types you could read and write on wires, and then
> we added components for loading structured data from text files (the equivalent
> of XML/JSON/YAML) and representing it as IMoaDict/IMoaArray interfaces (the
> equivalent of JSON) that you could pass between components on wires. It really
> made Bounce a lot more powerful, since **its original native data types were
> not nearly as flexible.**"

Compare the reflection section below. Adding dictionaries and arrays to the
wires is the same step PSIBER took, making the aggregate a first-class thing you
can pass around and open, reached by a different route under production
pressure, about a decade later.

### The sweet spot, and Shneiderman's objection

Don's summary is a claim about a design point that can be reached, rather than
about one product:

> "I know there are a lot of visual programming languages, and that most of them
> really suck, but I don't think that's endemic to all VPLs. After using Body
> Electric / Bounce, **I know there is a sweet spot that's possible, where you
> can visually create and edit live programs while they're running**, which
> really enables you to get into an extremely fun and productive zone."
>
> "**Programming languages are user interfaces for programmers, not just abstract
> mathematical models**, and good user interface design is even more important
> for visual programming languages."

Ben Shneiderman raised an objection in the same thread:

> "Visual languages have struggled to make commercial impact, but it has been a
> tough road. One issue is the **remarkable compactness of textual languages
> which offer easy search & replace, plus cut and paste.** So we still need some
> breakthroughs and the right situations to make VPL more widespread, but I'm a
> great fan of this direction."

Don makes the same complaint about SimAntics: *"acres of bizarre
spaghetti code"* with no way to list it as text, grep it or diff it. Both of
them, after years of building visual languages, name the same missing feature.
Text is the substrate that search, replace, copy, diff and version control are
built on, and a visual language that cannot round-trip to text loses all of
them.

This is the argument for the position this repository takes (files first, with
structure), and the reason Don's proposal to Lanier was a language whose
underlying form is serializable, with the visual editor as one view of it.
Lanier's counter-argument, that serialization endangers update latency, is in
the same section below.

### Guido van Rossum's request for a comparison

Guido van Rossum made a related point seven years earlier, as a question that
is still open. March 2007, OLPC Sugar list: a subthread had formed
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

Two points are worth separating. In the parenthesis he declines to claim that
his own preference is better, which makes this a request rather than a
position. And the question is not about pictures: it is about which
representation is the ground truth, because the canonical one is the one that
keeps formatting and comments. He had just described the concrete answer for
his side, the tool that became `2to3`, which does source-to-source
transformation and *"retains the exact formatting, comments
etc. of the input source code."* Text stays canonical, and transformations are
functions on text.

No one in the thread wrote the comparison. This file is a partial answer,
nineteen years later. The thread contains three positions:

| Position | Ground truth | Advocate, in that thread |
|---|---|---|
| Text, transformed | Source text; tools parse and re-emit it | Guido: formatting and comments survive, and every existing tool works |
| Structure, rendered | The tree; text is one view of it | the AST subthread; Ian Bicking's reading of Boxer as a middle — *"indentation is already a visual structure,"* plus non-text literals, *"all of that can be serialized to text"* |
| A separate visual notation, compiled down | Neither; the visual language is its own language | Don |

Don's, stated at the end of the thread, is the one this repository builds on:

> "I like the idea of having **visual meta-languages that are compiled into
> Python**, which avoids the problems of editing Python text or parse trees
> directly, and can support simplified '**kindergarten**' languages as well as
> more advanced forms."

`verified: sugar@laptop.org 001947, 20 March 2007.`

This avoids the ground-truth question rather than settling it. If the visual
language compiles to Python instead of being a view of Python, then Python text
stays canonical for everything Guido cares about, and the visual notation is free
to be as unlike Python as a nine-year-old needs, including deliberately weaker.
The cost is a compiler and a debugging story across two levels, which is the
price the "one faithful view" position does not pay.

He also argued against a simplified dialect underneath:

> "I think it would be wonderful to have a visual interface that **faithfully
> represented the full power and semantics of Python** (without trying to put a
> 'kid friendly' facade over it) […] Of course there's still a need for many
> different simple application-specific 'kid friendly' visual languages, but
> **when you drill down to real code, it's best to get the real thing** […]
> instead of some annoying watered-down half-baked ersatz Python (like 'safe
> python' in Zope, or smarty templates in PHP)."

`verified: sugar@laptop.org 001809.`

Simplified notations on top, the full language underneath. Kay's
"pop the hood on practically everything" and Shneiderman's round-trip requirement
lead to the same architecture.

- Hookup: Atari Cambridge/MIT Media Lab era, MIDI visual programming
- Body Electric: VPL Research, inherited MMP (Macromedia Director player)
- VR integration: Flock of Birds, Polhemus, DataGlove, Convolvotron
- Swivel3D articulated trees for bodies, hands, gesture recognition
- Broadcast positions via UDP to two SGI workstations (one per eye)
- Jaron Lanier performed with VR musical instruments live
- Bounce: David's post-VPL version at Levity, Don Hopkins did UI
- COM/ActiveX integration: new wire types for JSON-like nested data
- Solved six-input-limit with polymorphic dictionary objects
- Don ported Bounce to PowerPC Mac and built a cross-platform plug-in
  architecture on COM, porting the ActiveX Template Library to the Mac to do it

The people who built it report a negative result: pure dataflow becomes
unwieldy once complex state is involved, and the fix was to let opaque
objects (COM components) sit inside the graph and hold state, with richer wire
types to carry nested data between them.

The cost is in the word "opaque". The fix bought state and paid for it in
reflection: you can see the wire but not inside the box. A patch graph makes
flow visible while hiding what the flow passes through. The next section is
about that trade.

That is the same shape as the resolution in
[AXES-NOT-CAMPS.md](./AXES-NOT-CAMPS.md): a visual layer for the connections
and a symbolic layer for the state, each doing what it does well. A patch graph
expresses flow well and memory badly.

Lanier, who performed music with a dataflow language, is also the source of the
augmentation/automation axis in that file. The instrument was a case of
augmentation.

## Reflective depth: how far down does it go?

"Visual programming" groups systems by how they look. A property that matters
more for what you can do is reflective depth: how much of the running system is
reachable as a first-class object you can see, inspect, name and edit, using the
same machinery you use for everything else.

The question is whether you can drill down to everything, or whether the drill
hits a floor.

| System | The floor |
|---|---|
| Max/MSP, Body Electric, Bounce | The patch is visible; the objects in it are opaque. Flow is transparent, state is dark |
| Scratch | Scripts and sprites are visible; the interpreter and the block definitions are not |
| Snap! | Much lower: first-class functions, lists, continuations, and blocks that build blocks. First-class data is the design principle |
| Smalltalk | Nearly none: objects all the way down, classes are objects, the compiler is an object, the debugger edits live frames |
| Self / Morphic | None in the UI either. Every visible thing is a morph you can halo, open, and restructure; there is no separate editor mode because there is no separate editor |
| SK8 | Apple's answer to the same question: an object system where everything authorable is an object, with a full language underneath |
| eToys / Squeak | Halos on every morph, viewers that expose an object's variables and scripts to a child |
| PSIBER Space Deck | The extreme case, below |

The property is uniformity rather than visibility. Smalltalk and Self are on
this list not because they are graphical (Smalltalk's syntax is text) but
because there is no privileged layer that the ordinary tools cannot open.

### PSIBER: removing the floor

> **The Shape of PSIBER Space: PostScript Interactive Bug Eradication Routines**
>
> "The PSIBER Space Deck is an interactive visual user interface to a graphical
> programming environment, the NeWS window system. It lets you **display,
> manipulate, and navigate the data structures, programs, and processes living
> in the virtual memory space of NeWS**."

`verified: Don's own abstract, quoted from his 2006-10-29 mail to Bill Joy.
Paper and PostScript archived at art.net/~hopkins/Don/psiber/; demo film at
donhopkins.com/home/movies/PSIBERDemo.mov`

"Data structures, programs, **and processes**" is the important part. It is a
direct interface to the system in its live memory space, rather than a
visualization of it: the thing on screen is the thing itself.

Dictionaries show what this allows. In PSIBER a PostScript dictionary could be
used as a command palette: the same object is a data structure when you inspect
it and a menu when you use it, with no conversion step and no separate
palette-definition format. Under a partial object model you need a palette
format, a palette editor, and glue mapping entries onto functions. Under a total
one the dictionary already serves all three purposes, because a name bound to
executable code is what a menu item is.

The design intent, in Don's words on the OLPC list in 2007:

> "**The idea wasn't to invent a new visual language, just to implement a faithful
> visual representation of how the language really is**, with a direct
> manipulation interface for editing data and executing code."

The aim was a full-fidelity view of an existing language, not a new notation.
That is why PostScript suited it (*"a lot like Lisp […] because PostScript
programs are simply executable arrays containing names, literals, primitive
operators, nested arrays"*), and why the same deck could inspect a running
thread's dictionary stack, operand stack and execution stack.

### The cost of removing the floor

Don also described the cost:

> "One problem with PSIBER was that it was **too easy to make a mistake dragging
> and dropping, and accidentally totally hose the internals of the window
> system**, since you were editing shared structures in the NeWS server, like
> classes and canvases and event handler threads! **It needed some kind of
> read-only safety shield or edit mode switch.**"

`verified: sugar@laptop.org 001809, 13 March 2007.`

Direct manipulation of a live system also makes it easy to break. The floor
protected the implementation from the user as well as the other way round, and
without a floor or a guard a drag gesture has the same authority as a
deliberate edit. The fix he asks for is not less reflection but a mode: a
read-only shield that you turn off on purpose.

This matches the pattern elsewhere in this file: full access, with an explicit
gate on consequential steps.

### What 3D adds

The version Don and Lanier discussed goes further: represent all data as
first-class objects in 3D, with full reflection. 3D does not make reflection
deeper, since a dictionary is no more open for being a cube. What it adds is
room: spatial arrangement, containment, adjacency and scale become available as
notation, so a large structure can be navigated by moving rather than by
scrolling a tree. The risks are also structural: occlusion, and objects that
look manipulable but are only pictures.

This is why Body Electric belongs in this section as well as the Interval one.
It went far toward objects in space that you actually operate on, then ran into
the state problem, and the fix (opaque COM components) brought the floor back.
The same system went a long way toward reflection and then had to give some of
it up to ship.

The tension is unresolved, and it is one reason this repository keeps skills as
inspectable files: a directory is a dictionary you can open, and a `CARD.yml` is
a command palette that is also just data. It is the same idea as PSIBER's, in a
substrate with no graphics.

### Lanier's assessment

Lanier's retrospective assessment appears in two places. In one sentence he
rates the same system best and worst:

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

The debugging claim is unusual among the systems in this document. Most argue
that their notation makes construction better; Lanier claims that inspection
was as pleasant as authoring. Chuck Blanchard's screenshots are consistent with
this: `Break` and `StripChart` sit in the standard primitive palette alongside
`Constant` and `Slider`, so a breakpoint and a live plot of a value over time
are things you drop onto a wire, not a separate tool you switch to. With
liveness and a graph, the debugger and the editor are the same surface. This is
the sweet spot Don described, seen from the debugging side.

Lanier's 1999 letter to Don makes a harder judgment, directed at the VRML
community:

> "There IS a community of Body Electric users. **It is STILL building the most
> interactive 3D virtual worlds of any tool** (though Alice, from Carnegie
> Mellon, is the other hot contender). **That's SHAMEFUL!** While BE sucks in
> every other way, all the more recent vr design tools, **especially the vrml
> ones, simply avoid the problem of deep interactivity. How could the community
> be so whimpy, at this late date?**"

His "SHAMEFUL" is aimed at the field, not the tool. He is saying that a
decade-old, unmaintained Macintosh program still led in interactivity, and that
this reflected badly on the tools released since.

A system can be weak in most respects and still be one of the few attempting
the hard part. Deep interactivity (the world reacting continuously to
everything, in real time, editable while running) is what BE attempted and what
the standards-track successors did not. A field can lose ground on one property
for years while individual tools improve in other ways.

VRML did not develop a deep interactivity model: its scripting stayed separate
from the scene, the successor standard X3D kept the same shape, and the format
was overtaken rather than fixed. Live 3D on the web came instead from WebGL and
game engines, without the property Lanier was asking for.

`verified: quote from Lanier to Don, 1999, mirrored at
[sims/rescue-raw/bounce-notes-2000.txt](./sims/rescue-raw/bounce-notes-2000.txt).
The assessment of what VRML and X3D did next is this document's, not his.`

### Lanier on how far down it should go

Don's argument for representing all data as first-class objects with full
reflection got a reply from Lanier that reaches a similar place from cognition
rather than from Smalltalk:

> "I had always thought the swivel tree was ridiculous, of course, but on the
> other hand I liked the idea that **the virtual world and the knowledge base
> were the same thing** — that unity encourages the **visibility and grabbability**
> of the underlying concepts. I think the brain works that way — **there isn't
> some barrier behind which everything gets abstract — instead, it's user
> interface all the way to the bottom!** What I think would be the coolest
> long-term destination of BE would be extending the scenegraph so that it was as
> powerful a knowledge base as you'd want…"

`verified: Lanier to Don, 1999-07-08, in bounce-notes.txt.`

"User interface all the way to the bottom" states this section's thesis. Lanier
reaches it from a claim about minds rather than from the Smalltalk lineage: that
there is no level at which representation stops being manipulable. In the same
passage he calls the implementation *ridiculous* (the scene graph was a poor
knowledge base) while defending the unification: the architecture was right and
the data structure was wrong. The dict/array wire types later addressed that
gap, and the opaque COM components reopened it.

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

From Richard Gabriel's *Patterns of Software*:
> "Data and control abstractions are generally best when they are codesigned,
> and this is rarely done any more."

### 1996-2000: The Sims Era

**SimAntics** (Maxis/EA), the visual programming language the characters run on.
The name is a pun on *semantics*. It is probably the most widely deployed visual
programming language in this lineage: it shipped inside a game that sold in the
tens of millions, and players edited it.

- Character simulation visual programming language
- Simple local rules → complex global behavior
- Players as authors, not just consumers

It did not start with The Sims. It came from SimCopter:

> "Edith lets you view and edit SimAntics code, which is the visual programming
> language for scripting the behavior of The Sims. […] The SymAntics [sic]
> language was used to program the people in SimCopter, and Edith evolved out of
> that."
> — Don Hopkins, SimWatch list, 2000-08-26

`verified: recovered primary source; text and provenance in
[sims/MEDIUM-RESCUE.md](./sims/MEDIUM-RESCUE.md). The email uses the early
"SymAntics" variant; the established spelling is SimAntics.`

So the sequence is SimCopter people, then the language, then The Sims, with the
editor developing alongside the language rather than added afterwards.

Two details in that sentence need care.

1. Edith did not yet exist under that name. The name arrived with the
Windows port and the integration into The Sims. SimCopter used an earlier
version of the environment, unnamed as far as anyone here recalls. Don did the
Windows port himself, which is the basis for the correction, and the naming
story dates itself, because it comes out of a Sims-specific design phase:

> "There was one terrible phase we went through, trying to frame it like a
> simulated situation comedy, complete with a laugh track. That resulted in the
> first characters being named Edith and Archie (and **I named the visual
> programming tool 'Edith' for Edit House**)."

`verified: Don Hopkins, quoted in
[sims/sims-team-history.md](./sims/sims-team-history.md). The name is downstream
of The Sims' sitcom phase, so it cannot predate The Sims — which rules out
SimCopter, 1996.`

2. "SimAntics" is probably also a later coinage. The working name was Tree
Programming, and the artifacts were tree code and tree tables, terms
that survive in the shipped Edith menus (*Tree Editor*, *Tree Tracer*) and in
the primitives documentation. When the name SimAntics was coined is unknown.

There is dated corroboration for the working name. Reviewing The Sims Design
Document Draft 3 in August 1998, two years after SimCopter shipped and with
The Sims in development, Don wrote:

> "The whole relationship design and implementation (**I've looked at the tree
> code**) is Heterosexist and Monosexist."

`verified: August 1998, quoted in
[sims/sims-inclusivity.md](./sims/sims-inclusivity.md). Note the term he reaches
for unprompted, in writing, in 1998: tree code.`

### The Himbo easter egg was written in it

Jacques Servin's easter egg in SimCopter, the "himbos" who appear and kiss,
was tree code. Apart from The Sims itself, it may be the most consequential
program written in the language: it led to Servin's firing, it prompted a
public Maxis position that the company was not anti-gay, and Don relied on that
position in the 1998 memo above. See
[sims/sims-inclusivity.md](./sims/sims-inclusivity.md) and
[../skills/no-ai-ideology/](../skills/no-ai-ideology/).

The egg was behavioral rather than cosmetic (characters spawning and
interacting), which is the layer tree code controls, so the attribution
is consistent with the architecture as well as with memory.

There is one more link than the public story includes. The position Maxis took
is part of why Don was willing to work there, so a program written in this
language affected who wrote programs in it next. Set out in full in
[sims/sims-inclusivity.md](./sims/sims-inclusivity.md).

### Open question: what was authoring actually like, and on what machine?

This is inference, not record. For The Sims, before the environment was
ported to Windows, the workflow was sneakernet and Don was there for it:

> Will would author on his Mac and carry the work in on a floppy — IFF files —
> and the team would drop them into place.

The reasonable guess is that SimCopter worked the same way, possibly with
Servin authoring on his own Mac rather than Will writing everything. The
supporting argument is an absence: porting the editor from Mac to Windows was
a large job (Don did it for The Sims), and he would expect to have heard about
it if someone had already done it for SimCopter. No such port is remembered,
so Mac-plus-sneakernet is the parsimonious explanation.

`todo: confirm with Jacques Servin and Will Wright rather than leaving this as
inference. Specifically — what OS and tools did Servin use? Was the language
called anything yet, and when was "SimAntics" coined? Was SimCopter's workflow
the same floppy-and-IFF sneakernet? Did Servin author his own tree code or hand
it to someone?`

**Edith** is the editor. It was named for Edith Bunker, the first mother Sim,
and doubles as "EDIT
House." It was compiled into The Sims rather than shipped alongside it, which
gave it the property the environment-side languages in this document aim for:

> "Edith has grown a lot and is much wiser, now that she's integrated into The
> Sims instead of running as a separate program, so she is actually able to
> **debug and edit code and data while it's running live in the game**."

That is the Smalltalk image property, reached by a commercial game studio for
production reasons. It also had the usual cost of liveness: Edith was never
publicly released, and the blocker was *documentation*. See
[AXES-NOT-CAMPS.md](./AXES-NOT-CAMPS.md) on the notation-side/environment-side
trade this exemplifies.

### What happened to the notation afterwards, over four versions

The execution model outlived the notation, and the notation was replaced twice:

| Version | How behavior is authored |
|---|---|
| The Sims 1 | SimAntics tree code, edited in Edith. Bespoke visual language |
| The Sims Online | SimAntics, later reimplemented from scratch by the FreeSO project |
| The Sims 2 | Still SimAntics BHAVs; community tools such as SimPE edit them directly |
| The Sims 3 | C# on .NET/Mono. Mods are class libraries compiled against `ScriptCore.dll`, `SimIFace.dll`, `Sims3GameplayObjects.dll`, packaged as `S3SA` resources |
| The Sims 4 | Python: gameplay ships as `.pyc` under `simulation/` and `core/`, mods package as `.ts4script` |

`verified: Sims 3's C#/.NET toolchain and Sims 4's Python confirmed against
modding documentation (Mod The Sims, SimsWiki, Sims 4 scripting templates),
2026-09-07. Sims 4 sat on Python 3.7 long enough that the whole decompiler
ecosystem targets it.`

The advertisement mechanism survived the notation changes and became
declarative. In Sims 3 it is `ITUN` (Interaction Tuning), XML resources
carrying advertised motive deltas, with an `updateType` of `ImmediateDelta` or
`ContinuousFlow`. A modding tutorial describes the consequence:

> "you can rip your sims off by telling them this interaction will be very fun,
> which in actual fact it wouldn't be!"

That is Sims 1 advertising, intact, twelve years and two languages later: an
object claims a motive payoff, the Sim chooses on the claim, and the claim can
be false. The mechanism was tied to the execution model, not to the visual
notation, which is why MOOLLM can borrow it from Sims 1 without
inheriting tree code; see
[ADVERTISEMENT-AUCTION.md](./ADVERTISEMENT-AUCTION.md).

MOOLLM models Sims 1 deliberately, not because later versions are worse but
because Sims 1 is where the mechanism can be read: design documents, tree code
and firsthand accounts. Sims 3 and 4 extended it in proprietary tuning data that
has to be decompiled to read.

Why so much effort for a language nobody outside the building used? Jamie
Doornbos wrote it; Don ported it to Windows and made it easier to use; Patrick
J Barrett III wrote the most of it and became the resident expert, adopting it
fully and making it "much more colorful"; other programmers wrote it too; and Will
Wright was among the users. The case for the investment rests on whose
iteration cost it lowered rather than on user count: tooling that speeds up a
few designers' work can change what gets designed. This is an argument for
visual programming as a leverage technology rather than a mass-adoption one.

Will Wright's progression:
- SimAnt: Too simple
- SimEarth: Too complex  
- SimCity 2000: Just right
- The Sims: simple for kids, complex for artists

Don's contributions:
- Architectural editing and object placement tools: the build-mode surface
  players spend much of their time in
- Character animation system, pipeline and tools: the path from authored
  motion to a Sim performing an interaction
- User-created content tools: the ones listed below, treated as part of the
  product rather than as an afterthought
- SimAntics ported from Mac to Windows, documented and cleaned up, made easier to
  use
- Pie menu interaction system
- Extensive testing and exploration

The first three are adjacent to the notation rather than part of it. Build mode,
the animation pipeline and the content tools are all editors over the same
object model SimAntics scripts against, which is why they belong in a document
about visual programming. The player dragging a wall and the designer wiring a
behavior tree are manipulating the same world representation at different
levels, and the animation pipeline is what makes a tree node resolve into
something visible on screen.

**User-Created Content Tools** (Don Hopkins, Maxis/EA)
- SimShow: pre-release tool for character skins, so fans could start before launch
- Transmogrifier (TMog): OLE component for custom objects without 3D Studio,
  <https://thesimstransmogrifier.com/>
- rug-o-matic: a template plus drag and drop for storytelling "rugs" (title, description and image)
- Fan communities (Yahoo Groups, personal blogs), where shared content worked as social currency
- Heather "SimFreaks" and Steve "SimSlice" met in the fan community and later married

### 2000s-2010s: Constructionist Platforms

**Scratch** (Mitchel Resnick, MIT Media Lab)
- Block-based visual programming
- Builds on Seymour Papert's constructionism
- Millions of young programmers

**Snap!** (Brian Harvey, Jens Mönig)
- First-class procedures and data
- Build Your Own Blocks
- Connects to Berkeley CS curriculum

### 2020s: MOOLLM

MOOLLM draws on these threads:

**From Self's Prototype OOP:**
- "OOP RISC microcode": simple enough that you can build other OOP systems in it:
  - Instance/class (Smalltalk)
  - Morphic composition
  - CLOS generic dispatch
  - HyperCard delegation
  - COM IUnknown / OLE IDispatch
- Multiple interfaces per directory (ROOM+CHARACTER, SKILL+CHARACTER, etc.)
- Established patterns, well represented in training data
- Addresses discovery, versioning, extension points, and aggregation
  complementing interface inheritance, multiple inheritance and latent-space
  inheritance rather than replacing any of them
- Dovetails with the other interlocking object systems
- Just another way of looking at directories full of files
- The ground truth multiverse lives in GitHub

**From COM/OLE (Microsoft) → MOOM/MOOLE:**
- IUnknown: "QueryInterface" = check if directory has ROOM.yml, CHARACTER.yml, etc.
- Multiple interfaces sharing state: one directory, many .yml schemas
- CARD.yml is like IDispatch: advertisements + interface definitions for 
  high-level polymorphic dispatch, automatically binding parameters from context,
  natural language triggers, skill composition, K-line activation
- IDispatch: late-bound method invocation = LLM interpretation of affordances
- Aggregation as well as inheritance, complementing it: tear-off interfaces
  and related techniques. It complements all three kinds at once: interface
  inheritance from IUnknown, multiple inheritance through the ordered `parents:`
  list, and
  [latent-space inheritance](./object-system/LATENT-SPACE-INHERITANCE.md) from
  named concepts in the training data. Aggregation carries implementation reuse,
  which none of the three provides
- See: [DIRECTORY-AS-IUNKNOWN.md](DIRECTORY-AS-IUNKNOWN.md)

**From Minsky's Society of Mind:**
- Debating experts, not single-voice averaging
- K-lines as tradition activation
- NO-AI-* skills guard against known failure modes

**From constructionism:**
- Microworlds for exploration
- Learning by building
- Students as researchers

**From The Sims:**
- Character simulation with emergent behavior
- Speed-of-light: 8 characters × 99 turns in one call
- Memory + reflection + planning (realized with LLMs)

**From GitHub as MMORPG:**
- Social collaboration features as game mechanics
- Characters as bots in discussions, reviews, flame wars
- Branches as parallel universes

**Layered Multi-Paradigm Integrated Object Systems:**

These interoperate, and all are well represented in training data:

| System | Contribution |
|--------|--------------|
| Self | Prototype OOP as RISC microcode |
| Morphic | Composition, direct manipulation; full family tree in [MORPHIC-LINEAGE.md](MORPHIC-LINEAGE.md) |
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
| Svelte 5 Runes | Push | Compiler-driven fine-grained reactivity |
| OpenLaszlo | Push | Declarative constraints compiled to Flash, worked with Henry Minsky |
| Garnet (Brad Myers, CMU) | Pull | Built on KR (Knowledge Representation) Lisp frames library. Structural inheritance; see [GARNET-AMULET-PROTOTYPE-SYSTEM.md](GARNET-AMULET-PROTOTYPE-SYSTEM.md) |
| React | (barely) | Virtual DOM diffing, less reactive than its name suggests |

**Push vs Pull Constraints:**

- OpenLaszlo (Push/Eager): When source changes, propagate immediately.
  Better for responsive UIs in Flash/ActionScript runtime.
  Don worked there with Henry Minsky and other MIT Lisp hackers.
  
- Garnet (Pull/Lazy): Compute only when value is requested.
  Better for high-latency environments (X11 round trips).
  Don worked on this with Brad Myers at CMU.
  Built on KR (Knowledge Representation), a Lisp GOFAI frames library.
  
- Svelte 5 Runes: reactivity handled by the compiler.
  `$state` = reactive source, `$derived` = computed value,
  `$effect` = side effects. Both business logic and UI can be reactive.

We use SvelteKit for our web stack. It is less represented in training data
than React, but Svelte has a large community.

Instance Substitution Principle (Oliver Steele at Laszlo Systems):
An instance can be replaced by its inline definition, and vice versa.
This enables Instance-First Development: build specific, then generalize.
Svelte components follow this; refactoring inline code into a component is easy.

See `MicropolisCore/laszlo/micropolis/README.md`, a long essay comparing
OpenLaszlo/Garnet constraints to Svelte 5 runes.

## The Connection to Generative Agents

The Stanford Generative Agents paper (Park et al., 2023) uses LLMs to build
mechanisms comparable to ones The Sims was designed around in 1997:

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

*This document traces ideas from Papert and Kay through The Sims to LLM-based
agents: microworlds, direct manipulation, character simulation and
constructionist learning.*
