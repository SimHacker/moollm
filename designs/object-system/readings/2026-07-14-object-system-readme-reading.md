# Reading: The Object System README — Don Hopkins (2026-07-14)

**Video:** [MOOLLM Designs: Object System README](https://www.youtube.com/watch?v=0uBO6ZAcVTE)
**Text being read:** [designs/object-system/README.md](../README.md)
**Runtime:** ~33 min · "After a fresh cup of coffee, I read and explain the object-system
README, but I digress..."

This is the corrected, proofread transcript — the human-readable cream layer. No timestamps:
they're a distraction for the human consumer (and the LLM). The high-fidelity structured
source of truth — timestamps, chapter index, the ASR corrections ledger, and media-event
injection points for links, definitions, and preconfigured simulations — lives in the sibling
[2026-07-14-object-system-readme-reading.yml](2026-07-14-object-system-readme-reading.yml).
Stay in the cream; the machinery hums underneath.

The raw YouTube ASR mangled most proper nouns (Drescher → "Dresser", Densmore → "Dinsmore",
K-lines → "kines", LambdaMOO → "lambdaoo", CLOS → "clots", greppable → "greable"); those are
fixed throughout. One correction is the author's own, from the video comments: he said
"shadow DOM" and meant **virtual DOM**. Digressions are kept — they're the good part.

Link policy: same-repo references are relative paths (they survive forks, clones, and offline
reading); cross-repo references (MicropolisCore, WillWrightShowForFood) are absolute GitHub
URLs so excerpts survive being pasted into email; people and systems link to their canonical
homes.

---

## MOO for LLMs

I'm going to take you on a deep dive into the [MOOLLM](../../../README.md) object system.
MOOLLM, just to give you an introduction, is MOO for LLMs — and MOO is inspired by
[Pavel Curtis](https://en.wikipedia.org/wiki/Pavel_Curtis)'s
[LambdaMOO](https://en.wikipedia.org/wiki/LambdaMOO), which he developed at Xerox PARC. Now,
there are a whole lot of [designs](../../README.md) here, and what we're going to dive into is
the [object-system directory](../README.md).

## The stack: filesystem, git, GitHub

MOOLLM inherits from a lot of different really good ideas, and this will take you on a tour
of them. One important thing: MOOLLM exists on the stage of a GitHub repo. Git sits over the
file system; LLMs can read and edit the file system, but git adds parallel universes —
branching and merging — and GitHub adds collaboration: PRs, code reviews, everything. That is
the stack we're building on top of. It's industrial strength.

## Self-style prototypes; the LLM as universal resolver

The MOOLLM object system — how MOOLLM does objects:
[Self](https://en.wikipedia.org/wiki/Self_(programming_language))-style prototypes over the
file system, where the LLM is a universal resolver — promoted here from where the ideas were
first proven in the field: the [cauldron META-PLAN](../../../skills/cauldron/META-PLAN.md)
skill, the [security architecture](../../SKILL-SECURITY-ARCHITECTURE.md),
[directories-as-objects](../../../kernel/DIRECTORY-AS-OBJECT.md) per the
[Opus review](../../../skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.md). [Latent-space
inheritance](../LATENT-SPACE-INHERITANCE.md) generalizes MOOLLM's inheritance model to use
the LLM as a universal resolver — the most novel thing, and the thing least specific to the
cauldron. [Cauldron](../../../skills/cauldron/) is just a skill for designing — for
structuring designs so you can work with a high-power LLM to design, and then use lower-power
models to execute that design step by step.

## Heritage: SOAR, Flavors, CLOS, and the MOP

[SELF-AND-MOOLLM](../SELF-AND-MOOLLM.md) explains how MOOLLM uses a Self-inspired object
system. The mechanism, the heritage: Self as an object-oriented RISC instruction set — via
[Dave Ungar](https://en.wikipedia.org/wiki/David_Ungar)'s SOAR, the Smalltalk-On-A-RISC
project he did before Self. Then the Lisp lineage:
[Flavors](https://en.wikipedia.org/wiki/Flavors_(programming_language)), from the MIT Lisp
Machines — and when Common Lisp said "we've got all these different object systems in Lisp,
because you can roll your own and there are many approaches — how can we make an object
system for designing object systems?" — that's the
[Meta-Object Protocol](https://en.wikipedia.org/wiki/The_Art_of_the_Metaobject_Protocol). The
[Common Lisp Object System, CLOS](https://en.wikipedia.org/wiki/Common_Lisp_Object_System),
inherits from Flavors and other things like LOOPS, and the MOP reifies how it all works — the
reflective tower.

## Piaget → Minsky → Drescher → Leela AI: the grounding wall

[Gary Drescher](https://en.wikipedia.org/wiki/Gary_Drescher)'s
[schema mechanism](../../../skills/schema-mechanism/) inspired this too. He was
[Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky)'s PhD student, and he's
[Leela AI](https://leela.ai)'s advisor — we've discussed this with him.
[Piaget](https://en.wikipedia.org/wiki/Jean_Piaget) inspired Minsky, who inspired Drescher,
who inspired Leela AI ([the lineage](../../../skills/leela-ai/reference/drescher-lineage.yml))
— and it's all about how children learn by playing, and how you can make an algorithm that
does that. But it was missing something. Drescher wrote it in Lisp; Henry Minsky — my
colleague at Leela, Marvin's son — wrote a
[Python implementation](../../../skills/schema-factory/examples/henry-minsky-blocksworld.yml).
All of them hit the wall of grounding. And LLM grounding finally arrived.

## NeWS, TNT, HyperLook, and the Densmore–Rosenthal patent

I worked at Sun on [NeWS](https://en.wikipedia.org/wiki/NeWS) — The NeWS Toolkit — and at the
Turing Institute with [Arthur van Hoff](https://en.wikipedia.org/wiki/Arthur_van_Hoff) on
HyperLook. Owen Densmore and [David Rosenthal](https://blog.dshr.org) at Sun filed
[a patent](https://patents.google.com/patent/US5187786A/en) at that time on treating the Unix
file system — the shell, the paths — as a multiple-inheritance object-oriented programming
system, just like the one in NeWS that we used to build TNT, and then HyperLook, which was
inspired by [HyperCard](https://en.wikipedia.org/wiki/HyperCard).

## From LLOOOOMM to Anthropic skills — and the extensions

Taking these ideas together, taking a step back: I did a prototype called
LLOOOOMM — that's kind of hard to spell — and that
was something to learn from. Then
[Anthropic skills](https://www.anthropic.com/news/skills) came along, and I realized I had to
throw all that away and start from scratch on top of Anthropic skills, because they are
fucking awesome — they're composable. But I wanted to add things to make them more powerful.
We've added — I think we're on ten extensions at this point and counting. The really important
ones: you can **instantiate** a skill ([prototype](../../../skills/prototype/)). And we have
**multiple inheritance** — prototype-based, Self-like multiple inheritance — so an instance
can inherit from several skills.

## COM, OLE, ActiveX, XPCOM: there is something to it

Then, looking at the abomination that is Microsoft
[COM](https://en.wikipedia.org/wiki/Component_Object_Model) / OLE / ActiveX — type libraries —
even Mozilla looked at that and said "hey, we need something like that":
[XPCOM](https://en.wikipedia.org/wiki/XPCOM); I've used it. Companies like Macromedia looked
at it and said "that's a great plug-in system" and made MOA. There are like twelve different
COM clones, because there is something to it.

## Character rooms: Pee-wee's Playhouse

Character rooms: a directory has interfaces, like a COM object with multiple interfaces, or a
Java object. Those interfaces are UPPERCASE files —
[CHARACTER.yml](../../../skills/character/), [ROOM.yml](../../../skills/room/) — that declare
the directory as providing that interface
([DIRECTORY-AS-IUNKNOWN](../../DIRECTORY-AS-IUNKNOWN.md)). So you can look at one directory
as both a character and a room at the same time — which is great if you're doing
[Pee-wee's Playhouse](https://en.wikipedia.org/wiki/Pee-wee%27s_Playhouse) and you want a
talking room that remembers what happens inside it. There are applications of that, and we'll
get to them.

## Naming and structure as reflection

Naming and structure as reflection: a consistent big-endian naming system, where you list the
most important thing first, and you think about how names will alphabetically sort so related
things end up next to each other — implied structure through shared prefixes. Listing a
directory is asking it: what interfaces and state do you have?

Files and directories are named as self-describing, big-endian, human- and LLM-friendly
[K-lines](../../../skills/k-lines/). K-lines are a
[concept from Marvin Minsky](https://en.wikipedia.org/wiki/K-line_(artificial_intelligence)):
a token — a string you pull — that points not just to an idea but to the whole cloud of
concepts around it, and what you were thinking at the time. The idea is to define — and more
importantly, to **reuse** — well-known words as K-lines. They're like pointers. In a directory
listing, the K-lines are the file names and subdirectory names — pointers to files and
subdirectories. The name explains itself.

## The Sims' advertisements

Something we borrow that's really powerful:
[Will Wright](https://en.wikipedia.org/wiki/Will_Wright_(game_designer)) and Jamie Doornbos
invented this thing in [The Sims](https://en.wikipedia.org/wiki/The_Sims_(video_game)) called
[advertisements](../../sims/sims-object-model.md) — which sounds on its face obscene. NeWS
called them event interests: a template for an event you'd like to receive, and what to do
when you get it. Sims advertisements live on objects, and they're the key to the Sims'
plug-in extensible object system — what allowed it to be so successful, enabling players to
make their own objects and EA to make expansion packs that drop into the base game and just
work, seamlessly.

They're capability announcements: "I'm a stove, and you can cook on me — and if you're hungry,
you probably want to." An advertisement is the name of some function the object provides, plus
parameters, plus code that **scores** how much you want to do it based on context — who you
are, what relationships you have, what your mood is
([Find Best Action](../../sims/sims-find-best-action.md)). The toilet advertises that it can
relieve you if you need to go to the bathroom — but not if you don't. The bed: you remember
which side of the bed to sleep on, because sleeping on that side builds a relationship with
the bed that improves every time you do — assuming you have decent experiences — and that
weighs the "sleep in me" advertisement of that side of the bed. By doing it, you increase the
chances you'll do it again.

## The LLM program counter; K-lines are greppable

Think of the LLM as having a
[program counter of what to look at next](../SELF-AND-MOOLLM.md#naming-and-structure-as-reflection--guiding-the-llms-program-counter),
and all these advertisements — whether they're a file name, a directory name, or something out
there in associative memory, the fuzzy search, the vector store — and here's the important
thing: **K-lines are greppable.** You can do a very cheap, very fast "find me all references
to the word advertisement in these twelve repos." The LLM does that to decide what to look at
next, what to add to its context.

## Latent-space inheritance

[Latent-space inheritance](../LATENT-SPACE-INHERITANCE.md) — this is the great thing. Self,
and the many languages it inspired, point to a set of parents, and those parents are made out
of the same stuff. But within an LLM we can have parents that are concrete files — Anthropic
skills, MOOLLM skills, whatever prototypes — and we can **also** inherit from abstract
concepts, like love; or more concretely, Microsoft COM
[IUnknown](https://en.wikipedia.org/wiki/IUnknown); or the Google GCS file-access API; or "a
function that returns a pointer to an array of strings." We can inherit from single words that
name something well-documented in the training data — that's what matters. Or even looser
natural-language inheritance: "I inherit from a taco — crisp shell, warm filling, overflowing
with cheese, fresh vegetables and sauces." Maybe I'm defining a new food, and it wants this
particular kind of taco that I can describe in a few words as a parent, and we start from
there. Mixing literally different kinds of inheritance — from the very concrete to something
in the training data that you only have to ask for by name. K-line.

They're in the training data: you can inherit a whole language, a protocol, another object
system. When I define the MOOLLM object system, I want to inherit Self's object system just by
saying one of my parents is "Self's object system" — and another parent is
"[US Patent 5,187,786](https://patents.google.com/patent/US5187786A/en), filed by David
Rosenthal and Owen Densmore," about converting a file system — the shell, the paths — into an
executable tree of objects. You can inherit by referring to a US patent. And hopefully that
patent has expired, or it's in your name, or you might have legal troubles — fortunately
Rosenthal and Densmore's patent has expired. It helps to have some naming discipline; and
there are failure modes, and graceful degradation.

## YouTrackDB: inherit, don't "versus"

There was an interesting Hacker News discussion about YouTrackDB. I think "versus" is too hard
a word — I want to [inherit the great things about YouTrackDB](../YOUTRACKDB-VS-MOOLLM.md) and
build on top of them. I'm not saying this is an alternative to it; they're very different.
YouTrackDB is JetBrains' class-based object-oriented graph database, and we compare in order
to inherit what each is better at.

## The machine-language move

And the machine-language move: the Java VM executes YouTrackDB — we're being executed by an
LLM. (We'll get to the Dublin Core thing later; we do want a machine-executable core.) So we
can make adapters, bridges, and emulators to different object systems. Any Python programmer
who has used [PyGTK](https://en.wikipedia.org/wiki/PyGTK) knows the GObject wrapper brings
GTK's object system into Python; or [SWIG](https://en.wikipedia.org/wiki/SWIG), to plug in a
library — maybe one with its own object system — and make bridges so you can subclass objects
defined in another object system. All of this has been done with C and C++. We are
purposefully doing it in the LLM execution engine — the virtual machine. LLMs can just imagine
virtual machines, and then **be** them.

## Live objects in public: Soul City and adventure-4

[Live object examples](../LIVE-OBJECTS-EXAMPLES.md): we're using these for actual things, and
learning from them. GroundUp Software is my company, and that's how we do it — from the ground
up. Like a hamburger. Or used coffee beans. The system is running in public: Soul City on
[MicropolisCore](https://github.com/SimHacker/MicropolisCore) — soul content, human-LLM
collaboration — and [adventure-4](../../../examples/adventure-4/), the built-in example world.

## Dublin Core, the adventure compiler, and the good Scott Adams

[The Dublin Core and the adventure compiler](../DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md):
the strict machine-executable core under the rich semantic overlay — natural-language guards
compiled to guard_js by an LLM resolving linter warnings; instance-first, not yet lifted. And
the [Scott Adams](https://en.wikipedia.org/wiki/Scott_Adams_(game_designer)) lineage — the
good, creative Scott Adams, who made
[Adventureland](https://en.wikipedia.org/wiki/Adventureland_(video_game)) on the TRS-80 and
Apple ][ — not the evil racist one.

## Humansplaining

Now I have a new buzzword for you: **[humansplaining](../HUMANSPLAINING.md)**. Its meaning is
obvious. It's the complement — the other direction — of AI slop. The named anti-pattern:
wasting tokens telling an LLM what it already knows. AI slop's mirror image. The Skillscript
case study. Capability confinement belongs in the runtime, not the grammar. We'll get into
humansplaining ([the skill](../../../skills/no-ai-humansplaining/)).

## The annotated bibliography: one ladle of cream

Then I'll provide an [annotated bibliography](../ANNOTATED-BIBLIOGRAPHY.md): every YAML source
cited by this series, annotated as human-readable prose with links back to the live files —
one ladle from the repo's cream layer. "Ladle" is a K-line that refers to the
[cauldron](../../../skills/cauldron/) skill. We'll get to that later too.

## The heritage table, one line each

Reading order: first [SELF-AND-MOOLLM](../SELF-AND-MOOLLM.md), then
[LATENT-SPACE-INHERITANCE](../LATENT-SPACE-INHERITANCE.md), then the case studies, then the
[annotated bibliography](../ANNOTATED-BIBLIOGRAPHY.md) as the side table — consult it when a
citation points into YAML and you don't want to context-switch. The heritage, one line each:
**Self** — Ungar and Smith, 1987 — clone, override, delegate: the RISC core that everything
lowers to. **SOAR** — Smalltalk On A RISC — Ungar and
[Patterson](https://en.wikipedia.org/wiki/David_Patterson_(computer_scientist)), Berkeley,
1983–85: the minimal-primitive discipline Self kept. The **Lisp lineage** — from Lisp Machine
Flavors to Common Lisp CLOS to the Meta-Object Protocol: Howard Cannon, David Moon,
[Gregor Kiczales](https://en.wikipedia.org/wiki/Gregor_Kiczales), and company — mixins, method
combination, multiple dispatch, open implementations, before/after/around daemons.

## NeWS shipped it: TNT, HyperLook, SimCity

**[NeWS](https://en.wikipedia.org/wiki/NeWS)**: TNT — The NeWS Toolkit — and HyperLook,
inspired by HyperCard. This was a shipping window system; a shipping end-user user-interface
construction and editing system, like HyperCard; and a shipping game —
[SimCity](https://github.com/SimHacker/MicropolisCore) — on top of all of those. Owen
Densmore, [James Gosling](https://en.wikipedia.org/wiki/James_Gosling), David Rosenthal, me —
[Don Hopkins](https://donhopkins.com) — Arthur van Hoff, who after that ended up writing the
Java compiler, in Java. It used multiple-inheritance object-oriented PostScript — inspired by
Smalltalk, of course — shipped as system software; a HyperCard-like editable, scriptable UI;
and SimCity as live objects — you could deconstruct the game's user interface and build it
back up.

## The patent: dictionary stack ≅ shell paths

After doing the NeWS object system, Densmore and Rosenthal realized something. See, NeWS took
Smalltalk's objects and implemented them on what
[PostScript](https://en.wikipedia.org/wiki/PostScript) was already doing — which includes a
dictionary stack for looking up names, and that's all you need. Attention is all you need; we
would say the PostScript dictionary stack is all you need to implement multiple inheritance.
And guess what: that's isomorphic to a shell path in a file system. You can do objects that
way. That is what [this patent](https://patents.google.com/patent/US5187786A/en) is about.
Boom — we can inherit from this. This is a K-line to the patent that explains everything.
This is it, right here.

## Society of Mind: colocated agents, not carrier pigeons

Gary Drescher — Marvin Minsky's graduate student — wrote *Made-Up Minds* in 1991, and that
inspired us at [Leela AI](https://leela.ai) (Henry Minsky is my colleague and the CTO —
Marvin's son, of course) to build a
[schema mechanism](../../../skills/schema-mechanism/). The wall — in Lisp or in Python — was
grounding: there was no way to do grounding. Well, guess what an LLM does really well.

Earlier, Minsky wrote about
[K-lines](https://en.wikipedia.org/wiki/K-line_(artificial_intelligence)) — which I touched
on — and especially
[*Society of Mind*](https://en.wikipedia.org/wiki/Society_of_Mind), which gives you a much
better perspective: a way to frame and **colocate agents in the same LLM call**
([society-of-mind skill](../../../skills/society-of-mind/)). Not a whole bunch of agents
talking to each other by serializing and deserializing, paying per token. That's like
prisoners in solitary confinement exchanging notes written in lipstick on wet napkins, sent
back and forth by carrier pigeon — instead of having everyone in the same room together. The
distortion and the cost of serializing and deserializing what are essentially
high-dimensional vector pointers to ideas — the noise you introduce, the fucking climate
change you're perpetrating — for an incredibly inefficient thing, when you could just put
them together and let them point at each other's ideas in the same LLM call, in GPU memory.
Applying Society of Mind to LLMs: there are really good ideas here that make things much more
efficient — and not just efficient; you can do things you couldn't do before. The activation
mechanism, and the agency model: an agency composed of multiple agents that communicate
efficiently — telepathically, if you like. They're literally in the same spark of — call it
consciousness or not, it doesn't matter — the same LLM completion call, the same context.

## QueryInterface: COM vtables → FOO.yml

Now here's where it gets retro:
[COM](https://en.wikipedia.org/wiki/Component_Object_Model) and ActiveX — multiple interfaces
per object. Java — a Self-inspired language, like JavaScript — made a crippled implementation
of this; they all had their design trade-offs and, shall we say, time constraints. Java
doesn't do multiple inheritance of implementation; it separates that out into interfaces
without implementation — so does C# — so you multiply-inherit interfaces and implement them
behind the scenes. C++ supplies this directly: COM is simply C++ multiple-inheritance
vtables — objects with multiple interfaces have a sequence of vtable pointers, and
QueryInterface casts a pointer between them, QueryInterface being the first function in every
vtable, letting you pivot between interfaces. This is a great idea — as horrible as where it
led. I didn't even put DCOM in here, because that's where it gets really grisly. But there
are some great ideas in there.

(My cat's meowing.)

QueryInterface translates to: is there a FOO.yml in this directory that declares and
implements the FOO interface
([SELFISH-COM-IMPLEMENTATION](../../../kernel/SELFISH-COM-IMPLEMENTATION.md))? It can contain
any state FOO needs — and you also have the entire directory for shared state, like the C++
concrete implementation class behind the facade of multiple interfaces.

## The constructor stack: skills implementing all this

Skills implementing this — these are MOOLLM skills.
**[prototype](../../../skills/prototype/)** defines how directories, files, and skills
themselves are prototypes for other directories — and classes are just something you can
implement with prototypes by treating them a certain way. The
[object system](../../../skills/object/), defined within the object system.
**[artifactory](../../../skills/artifactory/)** — objects that make other objects, the
protocols they follow, and how they relate to the other skills.
**[skill](../../../skills/skill/)** — the meta-skill, the skill skill. Everybody's got a
skill skill; Anthropic even has a skill for how to make Anthropic skills — but these are more
than Anthropic skills; there's a lot in the skill skill.
**[file-system-object](../../../skills/file-system-object/)** — the K-line I explained.
**[society-of-mind](../../../skills/society-of-mind/)**.
**[incarnation](../../../skills/incarnation/)** — a protocol for creating characters richly
and ethically. **[character](../../../skills/character/)**, of course. And
**[empathic-templates](../../../skills/empathic-templates/)**: instead of Mustache templates
with special syntax, you just explain to the LLM what you want filled in. If you're running
it through an LLM anyway, why also run it through some very limited template system? And
**[schema-mechanism](../../../skills/schema-mechanism/)** is Gary Drescher's schema
mechanism; **[schema-factory](../../../skills/schema-factory/)** goes with it.

## Schemapedia: a circle drawn around schema

Schema — oh my god, schema is a hot topic here. Leela AI is where I work with Henry. Schema is
a very general term; there are many different types of schema. This is worth hopping into: a
veritable **[schemapedia](../../../skills/schema/)**. An encyclopedia is a circle of general
knowledge — consider this a schemapedia: a circle drawn around "schema," in every MOOLLM sense
that needs a name and a shelf. There are a lot of different schemas, and we're trying to
catalog them all — or at least the good ones. Not the W3C-listed ontology repository catalogs,
like BioPortal and so on; and there's an old "schemapedia" out there that is not this — we're
just reusing the name. What kinds of schemas are there? Mechanisms — look at this: COM/XPCOM,
cursor-mirror, dataset, Drescher, git, GitHub, JSON Schema, K-lines, Minsky frames, Postgres,
RELAX NG, Self, shell orchestration, Society of Mind, SQL, SQLite. Plug your own schemas in.
We love [Zod](https://zod.dev) schemas — why do we love them? Schemapedia: zod. Argument.

## YAML jazz: comments are precious

Ah — I wanted to introduce you to [YAML jazz](../../../skills/yaml-jazz/). This example
doesn't have a lot of comments, but the point is: you don't have a schema. You're making up
schemas from the ground up, and if they're useful, they propagate and get copied — and later
you play, you learn, and then you **lift** into formal schema definitions that are reusable
and composable ([play-learn-lift](../../../skills/play-learn-lift/)). These, we just pulled
out of our ass — in fact, LLMs are great at pulling things out of their ass — but you can
understand this by reading it, and so can the LLM. And the thing you don't see here:
end-of-line comments saying *why did I set this to this? what was it before?* — and multi-line
comments of any number of lines. It's an arbitrarily high-bandwidth, out-of-band overlay of
semantic information that humans and LLMs can read and write. In general, you want your tools
to **preserve comments**, because comments are precious.

But I digress. Back to Zod and mechanisms: this is a skill all about schemas in general —
knowledge we can draw from, be inspired by, and refer to with paths — very concrete, instead
of just abstract K-lines. Because if I just say "dataset," sure, you can Google it and read
why it's so cool — but now we've reified it into our concrete thing: formally defined what
it's named, how it works, and where to go for more information. That's what we're doing here.
But I digress.

## Leela AI: neurosymbolic; neat versus fuzzy

[Leela AI](https://leela.ai): we do neurosymbolic AI — manufacturing intelligence, real-time
computer vision. Computer vision is the neat AI — mathematical, a black box, fuzzy in
practice; we don't know how or why it works — we do not know from whence they come. And
neurosymbolic AI layers and sandwiches and mixes in symbolic AI — the old school. It's like
physics versus biology: physics can be explained with mathematics, but biology is all
exceptions and ad-hoc rules. That's the
[fuzzy-versus-neat](https://en.wikipedia.org/wiki/Neats_and_scruffies) AI distinction — and
the conclusion, back when those terms were coined and argued over, is that we need both. Each
is good at things the other isn't.

## The kernel constitution

The [kernel](../../../kernel/) directory: the objects — the
[Self-ish COM implementation](../../../kernel/SELFISH-COM-IMPLEMENTATION.md) I touched on —
and we have a [constitution](../../../kernel/constitution-core.md): **lean into the training
data**; don't make shit up, like Gas Town, for no fucking reason. We'll get into that.

## Garnet, Amulet, OpenLaszlo: real reactive programming

Prior designs with Self-ish influence: the
[Garnet/Amulet prototype system](../../GARNET-AMULET-PROTOTYPE-SYSTEM.md). I worked with
[Brad Myers](https://en.wikipedia.org/wiki/Brad_A._Myers) at CMU — in CMU Common Lisp, of
course — on a user-interface system that used constraints, with the KR
knowledge-representation system. Lisp could parse your expressions, figure out what they
depended on, and automatically wire up a dependency network. Garnet used **pull**
constraints — when you need a value, you read it, and it recomputes if anything it depends on
has changed — while [OpenLaszlo](https://en.wikipedia.org/wiki/OpenLaszlo) used **push**,
because that was more efficient to implement in the Flash engine. Garnet and OpenLaszlo were
prototypes of reactive programming — which React claimed. But all React is, is iterating and
diffing on a virtual DOM. No reactions, no reactive programming, no constraint tracking.
While [Svelte](https://svelte.dev) — especially Svelte 5 — actually ships a reactive system
in the spirit of Garnet and OpenLaszlo.

*(Author's correction from the video comments: "by 'shadow DOM' I meant 'virtual DOM' — shadow
DOM is something else entirely, so shameful that I will never speak of it again.")*

## The linguistic motherboard: Warnock, Densmore, Gosling

[Prototype/fragment/config](../../PROTOTYPE-FRAGMENT-CONFIG.md) directory as IUnknown;
[MOO heritage](../../MOO-HERITAGE.md) from LambdaMOO — Pavel Curtis's work at Xerox PARC. And
the **[linguistic motherboard](../../postscript/LINGUISTIC-MOTHERBOARD.md)** —
[John Warnock](https://en.wikipedia.org/wiki/John_Warnock)'s invention and intention for
[PostScript](https://en.wikipedia.org/wiki/PostScript): it's a motherboard for plugging in
cards. The first card he plugged in was graphics — stencil/paint,
[Porter-Duff](https://en.wikipedia.org/wiki/Alpha_compositing), rendering to a bitmap to
print. But there's also a networking card — and now we've got an LLM inference card.

When Owen Densmore worked at Apple, making Apple's printing system, he went over to Adobe and
worked with all those people to understand what the hell they were doing with PostScript, and
how the Mac operating system could support it and ship a product like the
[LaserWriter](https://en.wikipedia.org/wiki/LaserWriter) — which fucking revolutionized
desktop printing and publishing. That's where he got the linguistic-motherboard idea. Then he
went to Sun. James Gosling took a step back, looked at all the window systems, and asked: how
can we make a window system that sends **code** instead of a limited command set, like
[X Windows](https://en.wikipedia.org/wiki/X_Window_System)? And Owen saw it: PostScript.
PostScript is like Lisp crossed with
[Forth](https://en.wikipedia.org/wiki/Forth_(programming_language)) — but more Lisp than
Forth, because its data is polymorphic arrays and dictionaries, exactly the same as JSON,
instead of typed binary crap. I love Forth, but it's very low-level. In one page of PostScript
code, Owen implemented a Smalltalk-like class system — an object-oriented programming
system — on top of which we built user-interface toolkits, applications, even HyperLook, in
several versions: GoodNeWS, HyperNeWS, then HyperLook. User-editable environments, built from
an object system designed to run on a PostScript interpreter. It also ran on the printer. I
have really cool pictures.

## Wrap-up

And we also draw from the lineage of
[visual programming](../../VISUAL-PROGRAMMING-LINEAGE.md) — don't even get me started.
Anyway, this is broken up — this was just the [README](../README.md). I will go over the rest
of the series next.

---

*Transcript corrected from YouTube ASR by MOOLLM + human review. Chapter titles here match the
chapter index in the [YAML overlay track](2026-07-14-object-system-readme-reading.yml), which
carries the timestamps, the corrections ledger, and the media-event injection points.*
