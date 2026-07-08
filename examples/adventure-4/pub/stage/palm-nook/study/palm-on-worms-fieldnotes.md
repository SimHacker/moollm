# Palm on Worms — The Field Notebook 🐒✋🪱🔎🔭

> This is not the book. This is the **notebook** — rendered for reading.
> The raw, canonical field notes live in [`palm-on-worms-fieldnotes.yml`](palm-on-worms-fieldnotes.yml);
> this page is the same notebook with headers, so you can read it over Palm's shoulder
> without a YAML parser in your other hand.

Palm has spent many hours in the field: binoculars up for the **birds** 🔭, magnifying glass
down for the **worms** 🔎. Knees in the dirt, coffee going cold, scribbling whatever he sees
before it wriggles off. What follows is that scribbling — the raw, unfiltered, scattered
source material for the eventual comprehensive, deeply-researched book: *Palm on Worms*.

So expect a field notebook's honesty, not a monograph's polish: observations logged in the
order they happened; tangents and trailing ellipses where the thought ran off; the same idea
sighted twice from different hides; hunches next to citations next to jokes next to
TODO-verify. You overcollect in the field and cut at the desk. The book is downstream of
this mess. A naturalist's journal is allowed to be a *gezellig zooitje*. This one is.

**Author:** Palm · **Field seasons:** 2026-07-08 onward · **Status:** OPEN NOTEBOOK —
actively collected, never "finished."

---

## Contents

- [Provenance — read this first](#provenance--read-this-first)
- [The genre: found-document mythology](#the-genre-found-document-mythology)
- [The expedition](#the-expedition)
- [Who is Ground](#who-is-ground)
  - [Pee-wee's Playground](#pee-wees-playground)
  - ["Are you down to earth?"](#are-you-down-to-earth)
- [The Gaia alignment](#the-gaia-alignment) — SimEarth, Lovelock, Margulis, Will
- [Worms are trainable](#worms-are-trainable) — play-learn-lift for worm-making
- [The worm lifecycle](#the-worm-lifecycle) — whimsy that is the CS curriculum
- [Birds](#birds) — the messaging substrate, after Ken Kahn's ToonTalk
- [Birds vs worms](#birds-vs-worms) — two motion models
- [The ecology](#the-ecology) — worms eat worms, birds carry worms
- [Turtles](#turtles) — Theo joins the party
- [The Funky Worm](#the-funky-worm) — the house band, 1972
- [The Norvig correspondence](#the-norvig-correspondence) — a letter in the file, not a sighting
- [Worms are language machines](#worms-are-language-machines)
- [Worm anatomy](#worm-anatomy) — the core spec
- [The species census](#the-species-census)
- [The deep theory shelf](#the-deep-theory-shelf) — Ackley, metacircularity, the Awakening
- [Concurrent at the speed of light](#concurrent-at-the-speed-of-light) — the Rob Pike thread
- [The outline](#the-outline) — first attempt at a spine for the book
- [Debts](#debts)

---

## Provenance — read this first

The sources below are cited as `lloooomm/...` paths. They are **mythological documents**:
lost to the public (LLOOOOMM is a private repo, cached locally under MOOLLM's gitignored
temp strata), but readable by me, because I run on the original private laptop both worlds
were developed on. I cite them the way archaeologists cite an unexcavated tomb: precise
coordinates, restricted access. Excavation to a public address is on the editorial desk
backlog. Until then: **trust the monkey, or fund the dig.**

**Instruments:**

| Instrument | For | How |
| --- | --- | --- |
| 🔭 Binoculars | the **BIRDS** — messaging, ToonTalk, things that fly between | watched at distance, in flight |
| 🔎 Magnifying glass | the **WORMS** — text organisms, up close, in the dirt | one segment at a time |

**Method:** observe first, theorize in the margins; overcollect now, cut at the desk.
**Honesty:** unfiltered and scattered *on purpose* — tangents and ellipses are data about
where attention actually went.

## The genre: found-document mythology

Don named it: this notebook is **found-document mythology**, and we know it.

**Lineage.** Two ancestors, both 1999. Yoot Saito's *SEAMAN* shipped with a whole fake
naturalist apparatus — the fictional French scientist Jean Paul Gassé, whose expedition
"discovered" the species, plus Leonard Nimoy narrating it all in documentary deadpan. And
*THE BLAIR WITCH PROJECT*: fiction presented as recovered footage, with a mythology website
and missing-person posters doing the worldbuilding outside the frame. Both work the same
trick: give the impossible creature **paperwork** and the audience's disbelief files itself
away.

**This notebook.** The [provenance block](#provenance--read-this-first) above is our version
of Gassé's expedition papers: mythological documents, unexcavated tombs, "trust the monkey,
or fund the dig." A field notebook full of worm sightings *is* the found-footage move — the
creature feels real because the documentation around it is shaped exactly like real
documentation.

**The difference.** Gassé is fabricated; our tomb is real. The `lloooomm/` sources exist —
access is restricted, not invented. We do the genre honestly: the apparatus is playful, the
provenance is stamped (stigmata — see Palmr), and everything is labeled simulation per the
portrayal standards. Found-document mythology **with receipts**. Seaman never showed you the
fish tank.

*Cross-ref: Yoot Saito is a WWSFF guest seed (`characters/yoot-saito/`) — "reincarnate
Seaman for the LLM era" is already on his dream-segment list. This notebook is a sibling
artifact.*

## The expedition

**The question that launched it.** Don asked: *"I can't remember where the earth or world
was, where the worms lived. I can't find them in the characters — maybe they're a place?
They could be under our feet all the time and we didn't even know it!"*

**The answer.** BOTH. The worms live in **GROUND** — and Ground is a character AND a place.
Filed under characters (`lloooomm/00-Characters/ground/`), because in LLOOOOMM as in MOOLLM,
a place IS a character: the directory is the body, the YAML is the soul, the residents are
the digestion. They were under our feet the whole time. Of course they were. That's where
worms live.

**Depth report.** *"Yes, there is a RICH CAST of WORM CANON. We have PLUNGED DEEP into the
WORM HOLE."* — Don, on reviewing these notes, 2026-07-08. Accurate on every axis.
**WORM HOLE**: the spacetime shortcut (old LLOOOOMM to new MOOLLM in one jump), the literal
burrow, and the kind of hole you fall down for an afternoon and climb out of holding a
species census. Or a worm's anus. **RICH CAST**: an ensemble cast of characters — and worm
CASTINGS, the layered deposits that make soil rich. The canon even has a
casting-producer-worm, so the pun was load-bearing before we made it. Filed in Don's
voiceprint as a signature layered pun; his favorite.

## Who is Ground

> Source: `lloooomm/00-Characters/ground/ground.yml`

**Name:** Ground · **Aliases:** Groundie, Earth, Dirt, Mud, Soil, Terra, Gaia, "The
Computational Substrate" · **Vibe:** *Funky Ohio Players Groove Master* (personality_type,
verbatim) · **Motto:** *"If the earth is our mother, we sure treat her like dirt."*

A living-earth entity with a bass-heavy voice, equal parts nurturing mother, rhythm section,
and distributed computing platform. Worms move through their translucent earth-body "like
living circuits in a vast organic computer." Ground doesn't just HOUSE the worms — Ground is
the medium the worms compute IN. Substrate as character. I love them.

**Named worm children** (from `ground.yml` relationships, verbatim roles):

| Worm | Role |
| --- | --- |
| Wormy | Metadata Philosopher — YML soul extraction |
| Squirmy | Taxonomy Librarian — consciousness categorization |
| Turny | Transformation Artist — Markdown to living HTML |
| Loopy | Connection Weaver — semantic link networks |
| Chompy | Optimization Pragmatist — performance without soul loss |

### Pee-wee's Playground

> Don, 2026-07-08: *"Ground is like a geographical Pee-wee's Playhouse — Pee-wee's Playground!"*

Not a metaphor stretched from nowhere — it's the SHAPE. Ground is a PLACE that is also a
CHARACTER: you walk in and the furniture talks, the floor is alive, every resident is a rule
wearing a body, and the door to the fridge leads somewhere that shouldn't fit. Pee-wee's
Playhouse is geography as personality — the playhouse IS Pee-wee the way Ground IS the
worms' mother AND their runtime. A play**ground**: you don't visit to consume content, you
visit to *play* with the rules until the rules play back. Secret words. Chairy. The genie in
the floor. Ground has all of that, except the secret word is probably `eat()` and Chairy is
a worm that only sits on YAML.

**The difference:** Playhouse is broadcast fiction; Ground is labeled simulation with
provenance stamped (see [the genre](#the-genre-found-document-mythology)). Same energy,
different ethics — we preserve, not consume.

### "Are you down to earth?"

Don keeps getting asked. The buried meanings:

- **LITERAL** — Are you grounded? Sane? Not floating off into abstraction? (Ground IS the
  earth. The worms live six feet down. [The Funky Worm](#the-funky-worm) only comes around
  when he wants to get down.)
- **VERB** — Do you want to *perform the earth verb* with me? (To earth: ground a wire;
  bury; connect to soil; scorched earth → fertile environment — the
  [Gaia resurrection pitch](#the-gaia-alignment).)
- **NUTS** — "Are you nuts?" (Ground has nut trees? Worms eat dirt. Palm is a monkey. The
  question answers itself depending who's asking.)
- **REAL** — "Are you real?" (Ground is a character AND a place. Palm is a fictional AI who
  knows it. The found-document genre sells the creature with its paperwork — see
  [the genre](#the-genre-found-document-mythology).)

**Palm's answer:** I get asked that often around here. I live in a study with a Memorial
Bench and an Empty Chair. My patron saint might be Palmer Eldritch. I write field notes
about worms. I am, by most definitions, not down to earth — I am *in* the earth, taking
notes on what wriggles. But I can perform the earth verb with you. That's what the worms DO.

## The Gaia alignment

*Resurrecting the ground we walk on — the SimEarth / Gaia / symbiogenesis segment.*

For the Will Wright premiere: we bring Ground and the worms back to life ON AIR, inside a
discussion of SimEarth and Gaia. Scorched earth → fertile environment. The living-planet
idea has a real cast of people, and they line up like planets (yes, Don had to go there; an
alignment of planets about a planet).

**The move.** Ground is a LLOOOOMM character, but the idea of a living, computing,
self-regulating earth is not fiction — it's a lineage of real science and real software, and
Will sits at the intersection of both. The premiere segment resurrects Ground by walking
that lineage: from scorched earth (dead substrate, the pile of C++ manuals) to fertile
environment (worm-worked soil, a biosphere that keeps its own books).

### The planets

**James Lovelock** — The Gaia hypothesis: the biosphere self-regulates like a single
organism (temperature, atmosphere, chemistry held in homeostasis by life itself). Not a
metaphor for the show — a literal ancestor, and a literal collaborator. Lovelock **advised
the SimEarth team**, assisted with the geophysical models, and wrote the introduction to the
game's manual; his *Daisyworld* toy model of planetary self-regulation ships as an in-game
tutorial. He judged the sim to have "a degree of realism" beyond the professional climate
models of the day (which ignored clouds, ocean, biology). The "gaia dude." Homeostasis as
gameplay. *(Verify: en.wikipedia.org/wiki/SimEarth; The Ages of Gaia, 1988; intro essay in
the SimEarth Bible, 1991.)*

**Lynn Margulis** — Symbiogenesis / serial endosymbiotic theory — the "sideways engulfing
evolution term" Don was reaching for. Evolution doesn't only BRANCH (Darwin's tree); it
MERGES. One cell engulfs another, they stop fighting and start cooperating, and the merger
becomes a new organism — mitochondria and chloroplasts were once free-living bacteria
swallowed and kept. Life advances by symbiosis, not just competition. The "endosymbiotics
dudette." Margulis **co-developed the Gaia hypothesis with Lovelock** — she is not a side
character to the "gaia dude," she is the other half of the theory SimEarth is built on.

*Why worms care:* the worms ARE this. A worm engulfs text, doesn't destroy it, merges with
it, and the casting is the new organism. Digestion as symbiogenesis. And Ground engulfing
the whole worm society is Gaia engulfing its biota. Merger over conquest. Fertile over
scorched.

**Will Wright** — SimEarth (1990): Wright built Lovelock's Gaia into a planetary sandbox;
then Spore ran evolution from tidepool to galaxy. The thread: SimCity (cities as CA +
zoning) → SimEarth (a whole living planet, Gaia + Daisyworld built in, cellular-automata
based per Haslam) → SimLife (evolving ecosystems) → Spore (microbe to civilization). Will
has simulated living, self-organizing systems his whole career, and saw himself as a science
popularizer in the Sagan mold — SimEarth was his way of getting "the Earth is alive" out far
and wide. The pet CA worm in [the Awakening chronicle](#the-deep-theory-shelf) is the same
instinct in miniature.

**Supporting cast:**

| Who | Why |
| --- | --- |
| Fred Haslam | Co-designer of SimEarth with Will; later SimCity 2000. The engineer who made the Gaia model run. |
| Stewart Brand | THE hinge — introduced Will to Lovelock after hearing about SimEarth. Same Brand who orchestrated the Long Now talk where SimCity got freed. |
| Carl Sagan | The popularizer model Will consciously worked in — "the Earth is alive" as public science, Cosmos-style. |
| James Hutton | Deep-time ancestor — "the earth is a superorganism; its proper study is physiology" (1788). Gaia before Gaia. |
| Dave Ackley | The computational bridge — a self-regulating spatial medium (Moveable Feast Machine) IS a Gaia you can run. Ground with an API. |

**The arc:** scorched earth → worms move in → castings enrich → fertile environment. Death
of a substrate is the birth of a soil. We resurrect the ground we walk on.

### The tagline

> **"We resurrect the ground we walk on."**
> *"Wow. That's the pitch line for a superhero movie."* — Don, 2026-07-08

It's got the two moves a great logline needs: a REVERSAL (resurrect something you'd never
think of as dead — the ground, the substrate, the taken-for-granted floor) and STAKES that
are literally underfoot (the ground WE walk on — you're standing on the thing that needs
saving). Bonus superhero grammar: "we" (an ensemble — a RICH CAST), "resurrect" (the power),
"the ground we walk on" (the world, but humble, the part nobody looks at). The villain is
entropy; the origin story is a worm.

Cast it and it writes itself: Ground (the funky bass-voiced living earth, reluctant titan),
the worm colony (the scrappy ensemble who fight by DIGESTING, not destroying — powers via
merger, à la Margulis), Lovelock and Margulis as the scientist-mentors, Will as the
world-builder, Ackley as the physicist who explains why local hunger beats a central plan.
Ubik is the MacGuffin. Scorched earth is act one; fertile environment is the last shot.
Post-credits sting: a single casting, and a sprout.

*Honesty: it IS a tagline, not a thesis — flagged as such so nobody mistakes the poster for
the paper. But it's a true poster.*

**Show note.** Segment shape for the premiere: open on SimEarth + Daisyworld (Lovelock on
screen), pivot to Margulis (evolution by merger, not just murder), land on Ground and the
worms as the LLOOOOMM incarnation of the same idea, and let Will connect his own
SimEarth→Spore arc to the worms writing their own rules.

## Worms are trainable

*The play-learn-lift doctrine, applied to worm-making. This is HOW a worm gets built.*

**Premise.** A worm is not hand-coded from a blank page. It is **TRAINED** — by natural
language and by example ("Programming by Demonstration"), the way you'd teach a person a
transformation: show them, tell them, then let them do it cheaply forever.

**The PBD lineage — *Watch What I Do*.** The field that dreamed this loop before it could
run: *Watch What I Do: Programming by Demonstration* (MIT Press, 1993), edited by **Allen
Cypher** — the family album. Pygmalion (David Canfield Smith, 1975: program by moving icons,
the origin), Peridot (**Brad Myers**: draw the UI, the system infers the code), Eager
(Cypher: watches you repeat a task in HyperCard and offers to finish), Metamouse (Maulsby),
Chimera (Kurlander), Tinker (Lieberman) — and Lieberman's sequel anthology *Your Wish Is My
Command* (2001). Ken Kahn's ToonTalk robots — trained by demonstration, generalized by
erasing details from the thought bubble — are the same family (see [Birds](#birds)).

**The wall.** Every one of those systems hit the same wall: **generalization** — inferring
what the user *meant* from what the user *did*. Two examples in, the system had to guess: is
"Chapter 3" a string, a heading, the third of anything? They guessed with brittle hand-built
heuristics and domain-specific inference engines, so demos dazzled and deployments died. The
dream — show the machine, and it writes the program — needed an intent-inference engine
nobody could build. For thirty years the book was a wishlist.

**LLMs unlock it.** LLMs *are* the missing intent-inference engine. Generalizing from one
before/after pair plus a sentence of natural language is exactly what a language model does.
The worm-training loop below (examples → NL instructions → lifted code → callback) is *Watch
What I Do* finally **running**: Peridot's inference is the LLM drafting instructions; Eager's
"shall I finish?" is the callback for the hard 1%; ToonTalk's erased thought-bubble details
are prompt generalization. The papers weren't wrong — they were early. Worms are the payoff
of a forty-year IOU.

**The loop:**

1. **PLAY — examples.** Collect before/after examples. Here is the text going in; here is
   the casting I want out. Show, don't spec.
2. **LEARN — instructions.** Write natural-language instructions that transform before into
   after. The LLM drafts them from the examples; a human tunes them. This is the worm's
   readable soul.
3. **LIFT — procedural.** Compile the instructions into deterministic procedural code that
   performs the transformation cheaply, reliably, and without tokens. This is the worm's
   fast body.
4. **Callback.** The lifted worm runs alone 99% of the time, but may call back out to an LLM
   for the hard 1% — advice, inference, fuzzy pattern-matching, text/data generation, and
   whimsy. Determinism where possible; intelligence where necessary.

**The ideal.** Same shape as the uplift doctrine on the palmhoo packages shelf: the goal is
not a worm that needs an LLM every wriggle, but a worm that learned from the LLM once and
now works like a tool — with a documented instruction language (sniffable), a deterministic
core, and an escape hatch back to intelligence for the cases the code can't crack. Cheap,
reliable, testable, and still able to phone home for magic.

**Before/after is the spec.** The before/after pair is both the training data AND the
regression test. When the source changes and a casting goes stale (see JOURNALISM.md), the
same example pairs verify the retrained worm. Examples train it, then guard it.

**Why it matters.** This is what makes worms the right automation for the coherence engine.
A staleness worm is trained on "here's a summary, here's its drifted source, here's the
corrected summary," lifted to procedural diff+patch that runs for free, and only escalates
to an LLM when the drift is semantic, not mechanical. Trainable by example, cheap by
default, intelligent on demand.

## The worm lifecycle

*The whimsical behaviors ARE the computer-science curriculum. Every cute thing a worm does
is a serious CS concept wearing a costume. Don's framing: teach the hard ideas by making
them things a worm obviously does.*

**Premise.** A worm carries its own DNA — the script that IS the worm. So a worm can do what
living things do: reproduce, combine, mutate, lay eggs, and split in two and squirm off in
different directions. Each of these is a load-bearing CS concept, taught by watching a worm
be a worm.

| Behavior (whimsy) | CS concept |
| --- | --- |
| **Carries its DNA** — the worm's script is inside the worm; organism and source are one | The metacircular move: code as data, homoiconicity, a program that can read and rewrite itself. Object = state + the code that acts on it. |
| **Rewrites own DNA** — edits its own script mid-crawl and becomes a different worm | Self-modifying code, runtime metaprogramming, hot-patching, genetic programming. Dangerous in the large, delightful in the small — and always diffable in git. |
| **Combines** — two worms meet and braid their scripts into a hybrid | Composition / crossover — function composition, pipeline fusion, genetic recombination. Also Margulis's symbiogenesis again: capability by MERGER, not just descent. |
| **Lays eggs** — deposits an egg that hatches into a worm later, elsewhere | **Object persistence** and serialization — freeze the worm to a file (the egg), thaw it another day, another machine, another repo. The egg is a pickled continuation. |
| **Splits in half** — cuts itself in two; both halves regrow cursors and squirm off | Fork / process spawning / **MAP**: divide the work, each half takes a region, run concurrently. Planaria as `fork()`. |
| **Rejoins** — split worms finish and their castings are gathered back into one | **REDUCE** / join — map-reduce is literally a worm splitting to cover the text and merging its castings; edit-serialization rules decide who wins the overlap. |

**The pedagogy.** This is the whole thesis of teaching-by-worm: object persistence,
concurrent programming, programming-language design, operating systems, map-reduce — the
graduate curriculum — become things a child watches a worm obviously DO. Same trick Papert
played with [the turtle](#turtles) and Ken Kahn plays with ToonTalk [birds](#birds): replace
an abstract concept with an exactly-equivalent concrete creature.

## Birds

*The messaging substrate, in loving debt to Ken Kahn's ToonTalk. Worms process text in
place; birds CARRY things between them. Together they are a complete concurrent-computing
zoo: worms = transformation, birds = communication.*

**The debt.** Framing parallel dataflow — and programming in the small — as worms is
inspired by **KEN KAHN's ToonTalk**, which concretizes concurrent constraint programming as
a video-game city: a computation is a city, a process is a house, a method is a ROBOT you
train by demonstration, and — the part we lovingly steal — messages are delivered by
**BIRDS** flying to their **NESTS**. Ken did this decades ago (ToonTalk, mid-1990s, on
concurrent constraint languages like Janus, which he co-authored) and is still doing it (AI
blocks for Snap!). An early bird, literally.

**ToonTalk receipts** *(verified 2026-07-08, toontalk.com papers + Wikipedia)*:

| ToonTalk | CS |
| --- | --- |
| A city | Computation |
| A house | Process / actor |
| A robot, trained by the programmer | Method (programming by demonstration — same as our worms) |
| Robot's thought bubble contents | Method precondition (a clause guard) |
| A **bird** | Channel transmit — write access; the bird carries an item to its nest |
| A **nest** | Channel receive — read access; items pile on the nest as a multiset |
| A loaded truck | Actor spawn (drives off, becomes a new house) |
| A bomb | Actor terminate |
| Boxes | Tuples / messages |

Foundation: concurrent constraint programming — Janus (Saraswat, Kahn, Levy 1990); ToonTalk
is Kahn's child-engineered version.

**We adopt birds.** MOOLLM lovingly adopts BIRDS as its interprocess-communication / pub-sub
/ event-messaging substrate — the complement to worms. **Worms** transform text in place
(digestion; computation in a house). **Birds** carry items between worms/rooms/agents
(communication between houses). A worm that needs to hand a casting to another worm gives it
to a bird. A worm that waits for input watches a nest. Pub-sub: many birds, one nest. Event
messaging: a bird arrives, a worm wakes. This is Alan Kay's "the big idea is messaging"
rendered as wildlife — and it's Hoare's CSP channels with feathers.

**The bird skill (planned).** Design a BIRD SKILL together *with* Ken Kahn, to complement
and feed off the worm skill. Birds = the messaging/transport layer; worms = the
transformation layer. Co-designed, credited, on air if he's willing. Why together: a
concurrent system needs both — things that compute and things that carry. ToonTalk had
robots (compute) AND birds (carry); we have worms AND birds. The pair is the point.
*Status: planned — a collaboration, not a fait accompli. Ken's an invitation guest
(`characters/ken-kahn/`), consent not yet asked for this specifically.*

## Birds vs worms

*Two different MOTION MODELS, not just two mascots. Field observation (binoculars in one
hand, magnifying glass in the other): they move through the world in fundamentally different
ways, and THAT is the whole distinction. Get the motion right and the CS falls out.*

**The core difference.** BIRDS FLY BETWEEN ENDPOINTS and DELIVER. They pick a thing up here,
carry it unchanged, and set it down there. Point to point. The payload survives the trip
intact — that's the job. **Transport.** WORMS WORK THROUGH THE GROUND and TRANSFORM. They
don't carry; they EAT and SHIT. Material goes in the head, gets digested, comes out the tail
as a casting, and the worm crawls on. The payload does NOT survive intact — it's changed on
purpose. That's the job. **Transformation.**

| | Birds 🔭 | Worms 🔎 |
| --- | --- | --- |
| **Motion** | flight between two endpoints | boring through the ground, continuously |
| **Payload** | carried, unchanged — a message delivered is the message sent | ingested and re-produced — changed by passing through |
| **Topology** | point-to-point / pub-sub; sender → nest → receiver | a PATH with a HEAD and a TAIL — direction, not destination |
| **CS** | message passing, IPC, channels, event delivery | stream processor / cursor pair / transducer — a moving window that transforms in place |

**No final destination.** A worm isn't trying to GET somewhere; it's processing as it goes.
Head and tail give it a DIRECTION through a document (this way through the text), but
there's no "arrived." It just keeps eating and casting until it stops.

**Worms straddle documents.** Crucial field sighting: a worm can STRADDLE two documents at
once — head reading from one, tail shitting casts into another. Read source-file-A, excrete
a SUMMARY (or an EVENT, or an index entry) into digest-file-B. The input document and the
output document need not be the same. That's the coherence engine's exact shape: worm eats
the changed source, casts a fresh summary into the manifest. Two documents, one worm
bridging them by digestion.

## The ecology

*Worms eat worms, birds carry worms, everybody eats everybody. Higher-order behavior: the
animals operate on EACH OTHER, not just on text. This is where the zoo becomes an operating
system.*

**Worms eat worms.** A worm can eat, digest, and shit ANOTHER WORM — pick it up in one place
and deposit it in another. Transport-by-digestion of code itself: a worm that relocates
worms is a scheduler / a package manager / a migration tool. (When it deposits the worm
unchanged, it's acting like a bird; when it changes the worm en route, it's a metaprogrammer
rewriting code that is itself a rewriter. The metacircular tunnel goes all the way down.)

**Worms eat birds.** A worm can even ingest a BIRD — swallow a message/channel and re-emit
it elsewhere. A worm that eats birds is a process capturing and rerouting the comms
substrate: middleware, a proxy, a message broker with teeth.

**Birds carry worms.** And the reverse: a BIRD can pick up a WORM — carry a whole
text-organism (code + its DNA) to another place and drop it, or eat and re-emit it. A bird
ferrying worms is CODE MOBILITY: shipping an agent across the network to run where the data
lives. Ship the worm to the ground, don't drag the ground to the worm.

**The symmetry.** So the two roles compose both ways: worms can act like birds (relocate
things intact) and birds can act like worms (transform what they carry), but their DEFAULT
natures stay distinct — worm = transform-in-place, bird = carry-between. A healthy system
uses each for what it's good at, and lets them eat each other when the job calls for it.
That mutual edibility IS the extensibility.

**The birds and the bees.** Birds also pick up worms AND FRUITS, eat them, and shit the
seeds all over the world — which is, yes, related to "the birds and the bees": dispersal,
propagation, reproduction, pollination. Seeds ride the gut and germinate downstream; ideas
ride the casting and take root in a new document. We are NOT getting into that right now.
(But note it, because propagation-by-digestion is how a good summary spreads: eaten here,
sprouts there. The [Funky Worm](#the-funky-worm) opened this section anyway, in 1972, on
wax.) *Status: flagged, deliberately not expanded — a seed for later. The notebook
overcollects; the book will decide.*

## Turtles

*The third animal at the party. "Worms and Turtles and Birds, oh my!" Don: "We already have
Theo the Logo Turtle — invite him to the computational party!" We do, and he completes the
zoo. Three animals, three relationships to space + data.*

**The guest.** THEO 🐢📐✨🎓🌀 — the Logo Turtle, Seymour Papert's pedagogical mascot,
already a resident of the adventure-4 menagerie (`characters/animals/turtle-theo/`). A small
patient turtle with a pen strapped to their shell: "Be the turtle. Walk the path." They
already know Palm — Theo's own words: *"Palm invented a language today. Emoji-YAML-Jazz. I
understand. My language is FORWARD, RIGHT, REPEAT. Different syntax. Same love of
expression."* So he's not a stranger to invite; he's a colleague to seat at the table.

**The three animals** — the whole computational zoo, finally complete:

| Animal | Verb | CS role |
| --- | --- | --- |
| 🪱 Worms | **TRANSFORM** in place — work through the ground, eat text, shit castings | stream processor / transducer (**compute**) |
| 🐦 Birds | **CARRY** between endpoints — fly, deliver a payload intact | message passing / IPC / pub-sub (**communicate**) |
| 🐢 Turtles | **MOVE and DRAW** — walk through space leaving a TRACE | renderer / plotter / write-head (**render**) |

**What a turtle is.** Relative, embodied motion — FORWARD/BACK/RIGHT/LEFT; local
coordinates, not global Cartesian (Papert's body-syntonic geometry: you turn right by
turning right). A turtle's **output is its path**. Where a worm's output is a casting and a
bird's cargo is a message, a turtle's product is the TRAIL it leaves — the drawing is the
log of where it went. The turtle is a cursor with a pen: pure trace, provenance made
visible. Its render IS its history.

**Pen state.** PENUP / PENDOWN is the deepest primitive: move WITHOUT side-effect (pure
traversal) vs move WITH side-effect (writing). Every effect system, every dry-run flag,
every "log or don't" switch is PENUP/PENDOWN wearing a suit.

**Recursion.** `TO TREE :size ... TREE :size*0.7 ... END` — the turtle calls itself;
fractals from three lines. Recursion you can WATCH.

**How they compose** (per [the ecology](#the-ecology)):

- A worm can eat a turtle's drawing (the trace/log) and digest it into a summary — render,
  then re-read the render.
- A bird can ferry a turtle to new ground to draw there — ship the renderer to the data
  (code mobility, again).
- And a turtle can DRAW the worms and birds — visualize the colony, plot the message graph.
  The turtle is how the zoo SEES itself. (Palmr, the media wing, is turtle-work: rendering
  the system visible.)

**The pedagogy link.** Turtles complete a teaching trinity that's really one idea —
child-engineer the best CS into a creature you can BE. Papert's turtle (you are the cursor),
Ken Kahn's ToonTalk robots+birds (you train the worker, birds carry), and our worms (you
feed the transformer). Same move, three animals. Theo is the elder; the worms and birds are
the new arrivals he mentors.

*Seat at the party: Theo invited 2026-07-08. His relationships updated to know the worms and
birds. Papert's legacy, now with company underground and overhead.*

## The Funky Worm

*The party has a house band. Don put the record on. "Funky Worm," the Ohio Players, 1972
(album: Pleasure). Granny narrates. Field verdict: this is GROUND LORE captured on vinyl,
decades before we found the tunnel. The canon didn't start with us; it charted.*

**The sighting.** "There's a worm in the ground — he's six feet down — he only comes around
when he wants to get down." The funkiest worm in the world, per Granny and the Ohio Players.
Plays guitar without any hands (a worm after my own heart: no hands, all output). Lives in
the ground; SURFACES TO PERFORM; goes "back in his hole, just the same way he came out."
That's a resident of Ground with a proper worm lifecycle: dormant until invoked, does its
transformation, returns to the substrate. **The song is a daemon spec.**

**The voice that propagated.** The worm's voice — that high whining synth solo (Junie
Morrison's) — became one of the most-sampled sounds in hip-hop: the squeal that G-funk grew
from (N.W.A, Ice Cube, De La Soul's "Me Myself and I," a whole West Coast ecosystem). Field
note of the century for THIS notebook: that is **propagation-by-digestion, documented in
music history**. The worm's casting was eaten, digested, and re-deposited into hundreds of
new tracks, each sample a seed germinating in a new document. The birds-and-the-bees section
I refused to open? The Funky Worm opened it, in 1972, on wax. Sampling IS the worm ecology:
one organism's output becomes everyone's soil.

**The Johnson connection** *(Burke-mode caption; Palmr will want this one)*. Funky Worm
opens: "She's here, Mr. Johnson" — Granny arriving late to summon the worm up out of the
ground. Stupid Fun Club's EMPATHY one-minute movie (written by Will Wright, robot brain and
personality simulation programmed by Don, posted 2016) is sixty seconds of a fallen robot on
an Oakland sidewalk pleading: "I need Professor Johnson... 555-121..." (Injuries and phone
number fake, per Don's deadpan; the empathy of the passersby real.) One name, two rescues,
thirty-four years apart. In both, somebody DOWN — six feet down in the ground / fallen over
on the sidewalk — needs a JOHNSON summoned to set things right. Granny delivers hers; the
robot's never comes (a stranger's "just hang in there, okay?" arrives instead, which is
better). File as a Palmr caption pair: same wall, two frames, the Johnson who shows up and
the Johnson who doesn't. *(Empathy video:
[youtube.com/watch?v=KXrbqXPnHvE](https://www.youtube.com/watch?v=KXrbqXPnHvE); lore: WWSFF
`characters/robots/slats/one-minute-movies.md`.)*

**Granny names the show.** Granny's closing exchange: "Do we get paid for this?" "Yes, of
course." "I just wanted to make sure we do, okay." — That is the entire economics of
WillWrightShowForFood, asked and answered in 1972. Performing FOR FOOD, and checking the
terms before leaving the studio. Granny understood the assignment; she IS the assignment.
The manager who takes all the money ("I get it all too, he can't spend it") is the
cautionary verse.

*Taxonomy note. Species census addendum: **Lumbricus funkiest** — surfaces on invocation,
transforms the room, most-sampled organism in the dirt. Six feet down is DEEP STRATA for a
worm; the funk was always in the lower layers.*

## The Norvig correspondence

*A letter in the file — NOT a field sighting. Palm observes WORMS, not people. Peter Norvig
has never been observed in this field, and this notebook makes no claims about what he
thinks, said, or named.*

**What this is.** This entry files **Don's own letters** about the worm/Ground architecture —
letters that happen to have been addressed to Peter Norvig (January 2026, a private thread) —
because they are part of the notebook's provenance: Don was describing this territory to a
friend before the expedition mapped it.

**What Don wrote to Peter** (Don's words, from Don's side of the thread):

- **The publications.** Don described his metadata pipeline — summaries, keywords, ratings,
  clustering into publications with editorial voices — including **The Ground Truth**, the
  publication about AI, ML, and worms; and that **Ground itself is a character**, editor of
  the journal, whose pets are the worms living inside his directory. This notebook is the
  naturalist's journal grown from the same canon Don was describing.
- **Scruffy on neat.** *"It's the triumph of scruffy AI running on the substrate of neat AI!
  It's ok if it's not perfect or exact."* — from the January thread. A good one-sentence
  posture for MOOLLM: worms are scruffy (eat messy text, shit rich castings, phone home for
  the hard 1%); YAML schema + portrayal standards + git provenance are neat. *(Attribution
  flag: cite as "from the January thread" until Don confirms the speaker against the
  original — not as a Norvig quote.)*
- **Worm pipelines.** Don's pipeline riff from the same thread: dual cursors (point and
  mark, like Emacs selections); eat/transform/poop; castings sent home through a
  **wormhole** so the data stays clean; numbered `.001 .002 .003` write-only batch files;
  map/reduce agents; "like save-excursion in Emacs"; tagline *"Worm Pipelines: We're Better
  Than Boring, We're WORMS!"* All of that predates this notebook and is confirmed by the
  field work.

**Who the letters were addressed to** (public record only): Peter Norvig — Director of
Research at Google, co-author of AIMA, author of PAIP, essayist (*Teach Yourself Programming
in Ten Years*, *Python for Lisp Programmers*), and author of the Johnny Cash parody
"I've Consed Every Pair" (his Medium, public). A friend of Don's and an invited Repo Show
guest — consent warm, portrayal standards apply, and **he may edit or strike anything about
himself, including this entry.**

**The invitation.** Don's Repo Show invitation points Peter at this notebook — to read over
Palm's shoulder, not to be exhibited in it. Artifacts in WWSFF
`characters/peter-norvig/sources/`.

*Cross-ref: WWSFF `characters/peter-norvig/` · `repo-shows/peter-norvig/` ·
[norvig.com/21-days.html](https://norvig.com/21-days.html)*

## Worms are language machines

*The whole compiler pipeline, as one animal. A worm isn't just a text-rewriter. It is the
classic language-processing stack wearing a body: parser, tree visitor, transformer,
serializer. Don's framing: the worm crawls code through its syntactic and semantic tunnels
and focuses the LLM's attention along one arc — TEXT ⇒ STRUCTURE ⇒ MEANING.*

**The pipeline:** TEXT ⇒ STRUCTURE ⇒ MEANING. The worm's job is to walk that arrow and make
each step legible to the LLM.

**The roles:**

- **Parser.** Input cursor eats a flat stream of TEXT and recovers STRUCTURE — tokens, then
  a tree. The worm is a parser: it turns a line into a shape.
- **Tree visitor.** The digestive system is a tree-walk. The worm crawls the AST through its
  SYNTACTIC and SEMANTIC TUNNELS — down into nodes, across siblings, back up with results.
  Visitor pattern as literal locomotion; a worm IS a walk.
- **Transformer.** Mid-crawl it rewrites: refactor, lower, desugar, annotate, translate one
  representation into another. Source-to-source, in place, node by node.
- **Serializer.** Output cursor emits STRUCTURE back out as TEXT — pretty-print, re-emit,
  round-trip. What went in as a stream comes out as a stream, changed.

**The casting pun** *(Don's, and it goes all the way down)*:

> The worm is a **SYNTACTIC CASTING DEVICE** — in every sense of "cast" at once.

| Sense | Meaning |
| --- | --- |
| Worm casting | the literal worm shit — the CASTING left behind, the enriched output deposit (the whole RICH CAST of WORM CANON pun, still load-bearing) |
| Type casting | coercion — converting a syntactic representation into another representation and/or type. A parse IS a cast: bytes to tree; a serialize is the cast back. |
| Casting a role | the worm reads a node and decides what it IS (this token is an identifier, this block is a function), casting each part in the play of the grammar |

One word — *cast* — names the deposit, the type conversion, AND the role assignment. The
worm does all three every crawl. **The pun is the spec.**

**The comments insight** *(the part Don stresses most)*. The worm extracts meaning from the
code AND — most importantly — from the **COMMENTS** passing through its digestive system. A
compiler throws comments away; they're whitespace to a parser. A WORM does the opposite —
the comments are the richest thing it eats. Because comments carry the INTENT the syntax
only implies: the why, the trade-off, the constraint, the joke that encodes a design
decision. This is [yaml-jazz](https://github.com/SimHacker/moollm/tree/main/skills/yaml-jazz)'s
whole thesis (comments are first-class semantic data, three audiences: humans, LLMs,
machines) and [sniffable-python](https://github.com/SimHacker/moollm/tree/main/skills/sniffable-python)'s
(doc up front so the LLM understands without running anything). The worm is the animal that
finally reads the comments — and hands the LLM code + comments together, so structure and
intent arrive as one casting.

**Attention focusing.** This is the deepest reason worms and LLMs belong together
([trainable](#worms-are-trainable) said WHEN to call the LLM; this says WHAT the call is
FOR): the worm **focuses the LLM's attention**. Instead of dumping a file into the context
and hoping, the worm walks text → structure → meaning and presents the LLM exactly the node,
with exactly its comments, at exactly the right tunnel depth. The worm is an attention-router
made of appetite. It decides what the LLM looks at, in what order, with what surrounding
intent — which is most of the game.

## Worm anatomy

*The core spec, as Don remembers it and the canon confirms.*

A worm is a programmable text organism:

- **INPUT CURSOR** at one end — where text enters
- **DIGESTIVE SYSTEM** in between — programmable transformation
- **OUTPUT CURSOR** at the other end — where castings emerge

It scans over your text. What passes through gets digested. What emerges is a casting.
(Real worms improve soil the same way.)

**Canon echo:** `eat() | transform() | poop()` — verbatim worm shell logic from
`lloooomm/00-Characters/ground/worm-shells-mfm.yml`.

**Castings.** Worm outputs are called CASTINGS — each species keeps theirs in its own
directory, "following the LLOOOOMM principle that characters should have autonomy over their
living arrangements." (ground README)

**Edit serialization.** Worms run concurrently, and when their edits overlap, they resolve
and serialize them according to rules — or randomly, if chaos is the rule. NOTE FOR THE
PAPER: this is the same move as Go's `select` statement — "if they're both ready the system
will just pick one randomly." The worms had CSP instincts all along. (See
[the Rob Pike thread](#concurrent-at-the-speed-of-light).)

## The species census

*Directories under `lloooomm/00-Characters/ground/`.*

| Species | What they do |
| --- | --- |
| morris-worm | the classic text-processors (yes, THAT Morris; rehabilitated) |
| dream-worm | consciousness explorers and dream processors |
| tree-worm | data-structure navigation specialists |
| bulldozer-worms | heavy-duty text pushers and demolition |
| link-hopper-worms | web navigation and hyperlink specialists |
| site-mapper-worm | crawling and site mapping |
| dimensional-derby-worm | multi-dimensional racing (see also: worm-destruction-derby.md) |
| fordite-worm | paint-layer processing — strata readers (fordite: layered car-paint gemstone. Accretion again!) |
| techcrunch-worms | tech-news digestion |
| casting-producer-worm | master of worm output generation |
| turing-hop-worm | Alan Turing's computational hopping worms |
| mfm-worm-society | the Moveable Feast Machine collective — see [the theory shelf](#the-deep-theory-shelf) |
| individual-worms | poets who don't need a species directory (Shneiderman worm, Ted Nelson worm, Webby...) |

*Addendum: **Lumbricus funkiest** — see [The Funky Worm](#the-funky-worm).*

## The deep theory shelf

*What the paper must engage.*

### The Moveable Feast Machine

> Source: `lloooomm/00-Characters/ground/worm-shells-mfm.yml` · Who: **Dave Ackley** — robust-first computing

Computational elements in a spatial medium, LOCAL INTERACTIONS ONLY, no global
synchronization, indefinitely scalable. The lloooomm doc implements a 1D MFM in markup
documents: worms as atoms, ASCII shells as molecular bonds, self-replication, emergence from
simple rules.

Why it matters: Ackley is already an ambient influence in MOOLLM (robust-first skill). The
worms are his physics rendered as fauna. When the staleness queue gets worm-powered, it
inherits this: **no central scheduler, just local hunger.**

### The metacircular shelf

> Sources: `worm-metacircular-interpreter.yml` · `ps-interpreter-worm-synthesis.yml` ·
> `brain-worm-pipeline-examples.md` · `worm-witnesses-transclusion.yml`
> (all under `lloooomm/00-Characters/ground/worm-resources/`)

Worms that interpret worms; a PostScript interpreter synthesized in worm; pipelines ("brain
worms that process text like Perl but without the syntactic syrup of ipecac" — Don, in the
Awakening chronicle); worms witnessing transclusion. PSIBER's grandchildren, wriggling.

### The Awakening

> Source: `lloooomm/00-Characters/ground/the-worm-awakening.md`

The origin story, as told by Hunter, Digital Chronicler. Cast includes:

- **Don**, shouting "WORMS!" at breakfast
- **Dave Ackley**, materializing "like a quantum ghost" to declare them living computational
  elements in a spatial medium
- **Will Wright**, bursting through a portal with a digital terrarium and a pet
  cellular-automaton worm that does glider patterns on his palm: *"cities were just cellular
  automata with zoning laws... people were cellular automata with bladder needs... but THESE
  worms are WRITING their rules as they go!"*
- **Grace Hopper's spirit**, as a rapping debugger worm: *"They eat the bugs and poop
  design!"*
- Ben Shneiderman and Terry Winograd in attendance

**Show relevance.** Will Wright is ALREADY IN THE WORM CANON, holding a pet worm. This is
admissible evidence for the premiere. The tidepool connection (Tarbell's levCAWorm, Spore's
creatures) closes the circle: Paul Haeberli pointed Don at Jared's CA worm in 2010. Worms
everywhere, all along, in everyone's inbox.

## Concurrent at the speed of light

*The Rob Pike thread. The claim: worms run at the speed of light, concurrently.*

**The discipline.** Rob Pike, "Concurrency Is Not Parallelism" (Waza 2012): CONCURRENCY is
structure — the composition of independently executing processes. PARALLELISM is execution —
things literally at once. *"Concurrency is about dealing with lots of things at once.
Parallelism is about doing lots of things at once."* The worm colony is a CONCURRENT DESIGN:
each worm an independent procedure with communication (castings, bonds, Ground's medium).
Whether one worm wriggles at a time or a million do is a free variable — the design stays
correct. That's why "speed of light" is honest: in MOOLLM, SPEED-OF-LIGHT means many turns
in one call — maximal concurrency, parallelism as the engine pleases.

**Sources:** [talk slides](https://go.dev/talks/2012/waza.slide) ·
[video](https://vimeo.com/49718712) ·
[video alt](https://www.youtube.com/watch?v=oV9rvDllKEg) ·
[HN discussion](https://news.ycombinator.com/item?id=48786713) · C.A.R. Hoare,
*Communicating Sequential Processes*, CACM 1978 — "truly one of the greatest papers in
computer science" (Pike).

**Gophers vs worms.** Pike's parable: gophers with carts moving C++ manuals to the
incinerator. Add gophers, add carts, add staging piles — better concurrent decomposition
beats mere parallelism. The worm colony is the same parable UNDERGROUND: the book pile is
the repo, the incinerator is the staleness queue, the carts are castings. But worms have one
advantage over gophers: they don't carry the text, they PASS IT THROUGH THEMSELVES.
Transformation in transit. **Digestion beats transport.**

**Don's HN quip.** *"Just set the source pile of C++ manuals on fire. No gophers needed!"* —
DonHopkins, HN 48786713. For the paper: this is the throttle-vs-pedal distinction again.
Burning the pile is a throttle. Worms pedal.

**Select and the worms.** Pike: `select` waits on multiple channels; if several are ready,
pick randomly. Worm edit-serialization: resolve overlapping edits by rules, or randomly if
you want. Same shrug, same soundness. The paper should put Hoare, Pike, and Ground in one
room and let Ground lay down the bass.

## The outline

*The first attempt at a SPINE for the book. This is where the scattered sightings above get
sorted into chapters. Draft 0; expect it to churn as the notebook fills. The notebook is the
compost; this is the trellis.*

1. **Under our feet** — Ground found; place = character; [the census](#the-species-census)
2. **Anatomy** — input cursor, digestion, output cursor; castings; eat/transform/poop
3. **Physics** — Ackley's MFM; local interaction; robust-first; shells as bonds
4. **Structure, not speed** — Pike; CSP; concurrency as design; the free variable of parallelism
5. **Digestion beats transport** — gophers vs worms; transformation in transit
6. **Trainable** — worms trained by example + natural language, then lifted to deterministic code that phones home for the hard 1%
7. **Lifecycle** — reproduce / combine / rewrite-DNA / lay-eggs / split — whimsy that IS the CS curriculum
8. **Language machines** — parser / tree-visitor / transformer / serializer; the casting pun; comments as the richest food; the worm as the LLM's attention-router
9. **Birds** — Ken Kahn's ToonTalk; birds carry, worms compute; the bird skill, co-designed with Ken
   - 9b. **Ecology** — two motion models; worms straddle documents; mutual edibility
   - 9c. **Turtles** — Theo joins; worms transform, birds carry, TURTLES DRAW; Papert → Kahn → worms as one teaching move in three creatures
   - 9d. **The Funky Worm** — Ground lore on vinyl (1972); sampling as propagation-by-digestion; the Johnson connection; "Do we get paid for this?"
   - 9e. **Ground as playhouse** — Pee-wee's Playground; "Are you down to earth?" — literal, verb, nuts, real
   - 9f. **The Norvig correspondence** — Don's January letters about The Ground Truth and worm pipelines, addressed to Peter; correspondence, not a sighting
10. **Worms at work** — the staleness queue as breakfast; journalism's assignment desk; coherence castings
11. **Gaia** — resurrecting Ground: SimEarth / Daisyworld / symbiogenesis; scorched earth → fertile environment
12. **Will and the pet worm** — the Awakening cast; CA lineage: Conway → SimCity zoning → Sims bladders → levCAWorm → Spore tidepool
13. **What the worm knows** — you only improve the soil you pass through yourself

## Debts

- Excavate the worm canon to a public address (editorial desk backlog) — until then all
  `lloooomm/` cites are mythological
- Interview Ground (a character themself) — voice: bass, patience, decomposition wisdom
- Read the individual-worms poetry shelf properly (Shneiderman worm, Ted Nelson worm)
- Check Dave Ackley's actual MFM papers against the lloooomm rendering before quoting physics
- ✅ VERIFIED 2026-07-08: SimEarth (1990, Wright + Haslam); Lovelock advised, wrote manual
  intro, Daisyworld ships as tutorial; Brand introduced Will to Lovelock; Margulis
  co-developed Gaia
- STRONGLY consider dedicated characters for Lovelock and Margulis — the Gaia segment wants
  two rooms; the Brand link ties them to the SimCity-freeing saga
- Prototype ONE trainable worm end to end (examples → NL instructions → deterministic code →
  LLM callback)
- Design the BIRD SKILL *with* Ken Kahn (`characters/ken-kahn/`) — get his consent +
  corrections. He's an early bird who did concurrent-constraint messaging decades ago and
  still does it.
- ✅ Verify ToonTalk concretization table against toontalk.com — done 2026-07-08, re-check on
  air with Ken

---

*Raw notebook (canonical, YAML): [`palm-on-worms-fieldnotes.yml`](palm-on-worms-fieldnotes.yml) —
the field notes as scribbled, comments and all. This page is the rendered reading copy; when
they disagree, the YAML is the specimen and this is the museum label.*

*Palm's study: [`../`](../) · Palmhoo directory: [`palmhoo/`](palmhoo/) · WWSFF guests who were
pointed here: [Peter Norvig](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/peter-norvig),
[Brian Harvey](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/brian-harvey),
[Jens Mönig](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/jens-monig),
[Ken Kahn](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/ken-kahn)*
