# Nodes with the code inside them

Somebody asked Ted Nelson at BayCHI in 2021 whether his ideas could be applied to understanding
computer code -- you look at a function and it calls something else and something else, and no tool
visualizes it in an intuitive way. His answer is the shortest statement of MOOLLM's thesis on record,
and it came from a man who had no idea MOOLLM would exist:

> My answer is, I don't know. Certainly automatic understanding of computer code is hard. That's why
> documentation of the computer programs used to be so important -- it probably still is -- and that's
> by **the author actually putting it into the words**.

https://www.youtube.com/watch?v=dOLXLk8TbxQ

Not a visualizer. Not inferred structure. **The author putting it into the words**, in the artifact,
on purpose, as the primary act rather than the chore you skip.

Then Ted Selker, hosting, supplied the engineering history that makes it a field rather than an
opinion.

## Selker's answer: the environment changes how people write

> Interlisp-D with LOOPS was a programming environment that made nodes for all the different objects,
> and embedded all of the code inside of those nodes, and used structure editors -- and it literally
> changed the style of programming for the people that used it. Smalltalk also had a visual metaphor
> for its tools that changed the way people wrote their code. They made much deeper code -- anyway,
> more balanced code -- in LOOPS. There's a whole field of people using visualization. Mike Travers, on
> our talk, has been involved with this as well. It's a very very important topic you just brought up,
> and it's a field, so it's an interesting field too.

Four claims in there, and each one is a design constraint:

1. **A node per object.** The unit of the environment is the thing, not the file.
2. **The code lives inside the node.** Not in a parallel file tree that has to be kept in sync.
3. **Structure editors.** You edit the structure, not a flat rendering of it.
4. **It changed the style of programming.** The environment is not neutral. It selects for a kind of
   code -- Selker's words, "much deeper code, anyway more balanced code."

Claim 4 is the load-bearing one and the least discussed. Nobody chooses a style of programming; the
environment hands you one. Which means the environment is the design surface, and MOOLLM is an
environment.

## MOOLLM is this, with directories as the nodes

The mapping is close enough to be uncomfortable:

| Interlisp-D + LOOPS | MOOLLM |
|---------------------|--------|
| A node per object | A directory per skill, room, character, playset |
| Code embedded in the node | `SKILL.md`, scripts, examples, evals, all inside the skill directory |
| Class/instance, multiple inheritance | Skills as prototypes you instantiate; ambient skills as mixins |
| Structure editor (DEdit, SEdit) | The agent editing YAML and markdown as structure, plus a linter |
| Browser over the class graph | `INDEX.yml`, `GLANCE.yml`, the directory listing as the advertisement |
| Active values, annotated values | `yaml-jazz`: comments are first-class semantic data |
| Residential environment -- the image *is* the program | The repo *is* the program, and git makes it durable |

Two differences worth naming rather than hiding.

**The renderer is a reader, not a picture.** LOOPS drew a graph. MOOLLM's "visualization" is prose and
structured text an LLM reads directly, which is why the pyramid is GLANCE → CARD → SKILL → README
rather than a zoomable diagram. This is Ted's answer and Selker's mechanism combined: nodes with code
inside, and the author putting it into the words, because the thing reading it reads words natively.

**The image is a repo.** The famous failure mode of residential environments is that the world lives in
a memory image nobody else can diff, review, or merge. Git is the fix, and it is the same argument as
[editing-history/](editing-history/README.md): content-addressed, blamed, branchable, reviewable.
Interlisp-D's environment was better than ours at editing and worse at *sharing*, and that trade no
longer has to be made.

## Mike Travers, whom Selker named, and who was in the room

Travers is the third leg, and he is the closest ancestor MOOLLM has. His doctoral work at the MIT Media
Lab was **agent-based visual programming**: AGAR, then LiveWorld, environments where you build behavior
out of many small concurrent agents and watch them run, with the agents as manipulable objects rather
than text. The thesis is *Programming with Agents: New Metaphors for Thinking about Computation* (1996),
supervised in Minsky's orbit, and it is Society of Mind made into a thing you can direct-manipulate.

Which is what MOOLLM's skills are. An ambient skill is an agent that is always watching; a K-line is
Minsky's term and we took it on purpose. Travers had already asked the question we are answering: what
does an environment look like when the unit of composition is an agent rather than a procedure?

He was in that BayCHI audience, and he has known Nelson since 1975, when he was a high school student
in Evanston helping open Nelson's **itty bitty machine company**. Which makes him a live thread between
Nelson's hypertext and Minsky's agents, and a person to actually talk to rather than a citation.

## The field Selker was pointing at

"It's a field, so it's an interesting field too." Worth enumerating, because this repo keeps
reinventing pieces of it:

- **Interlisp-D / LOOPS** (Bobrow, Stefik, Xerox PARC) -- nodes, embedded code, structure editing;
  LOOPS fed CommonLoops and then CLOS.
- **Smalltalk** -- the class browser as the primary interface to the system, the image as the world.
- **Boxer** (diSessa, Abelson) -- the box is both the container and the code, recursively. Closer to
  the directory-as-node idea than anything else on this list.
- **NoteCards** (Halasz, Xerox) -- a card per idea, typed links, browsers over the link graph, and
  guided tours. Read it next to [PAIRED-LINKS.md](PAIRED-LINKS.md); the overlap is total.
- **LiveWorld / AGAR** (Travers) -- agents as manipulable objects, behavior as composition.
- **HyperCard and HyperLook** -- stack/background/card/object namespaces, scripts attached to the object
  they animate. Don's own lineage.
- **Self, and Ungar's work** -- prototypes over classes, which is what a MOOLLM skill actually is.

The shared claim across all of them is Selker's claim 4: change where the code lives and you change
what people write.

## What this buys us that is actionable

Three concrete things, not vibes:

1. **Stop splitting a node across trees.** If a skill's tests, examples, evals, and scripts are not
   inside the skill directory, the node is fictional. This is already the convention; the LOOPS
   precedent is the argument for enforcing it in a linter.
2. **The author writes the words, and that is the deliverable, not a tax.** Ted's answer. The GLANCE
   and CARD levels exist because the author's overview is the thing no analyzer can recover. A
   generated summary is not a substitute and should be marked when it happens.
3. **Judge the environment by the code it produces.** Selker's "deeper, more balanced code" is an
   empirical claim about an environment's output. The equivalent question for MOOLLM: do skills written
   inside it come out better than skills written outside it? That is what the eval harness is for, and
   it is the only honest way to know whether any of this works.

## Back to the question that started it

The question was whether hypertext could make code comprehensible, and the expected answer was a
diagram. What Nelson said instead was that comprehension comes from **the author putting it into the
words**, and what Selker added was that you get that by building an environment where the words and the
code live in the same node.

That is the entire architecture of this repo, stated by two people in 2021 who were talking about
Interlisp-D.

## Related

- [PAIRED-LINKS.md](PAIRED-LINKS.md) -- the link model; NoteCards' typed links and guided tours
- [SONG-FORM.md](SONG-FORM.md) -- how to explain any of this to somebody who is busy
- [editing-history/](editing-history/README.md) -- why the node graph lives in a repo
- [`skills/yaml-jazz/`](../skills/yaml-jazz/) -- comments as first-class data, which is annotated values
- [`skills/sniffable-python/`](../skills/sniffable-python/) -- structuring code so a reader can sniff it
- Full talk digest with attributions:
  https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-nelson/sources/2021-08-10-baychi-hci-constructs-transcript-digest.md
