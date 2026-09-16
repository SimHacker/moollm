# Dwarf Fortress: generating the dimension lattice

*Part of the [Korz cauldron](../../README.md). Sidecar: [`df-procedural-magic.yml`](df-procedural-magic.yml).
**Spectrum: self-contained** — a shipped game's announced design is the canon,
with every claim sourced to the developers' own words.*

**What this teaches.** Every other example in this collection *declares* its
dimensions: [`layered-rules`](layered-rules.md) declares `topology`,
[`margolus-rules`](margolus-rules.md) declares symmetry and iteration order,
[`mtg-layers`](mtg-layers.md) prints them on cards. Dwarf Fortress's **Myth
and Magic** work generates the dimensions **per world, from a creation myth,
before play begins** — and can flip them mid-game. It is also, already, the
cleanest shipped demonstration of Korz's subjective-projection thesis:
**one simulated world, three modes that gather it along different axes.**

## The announcement

Tarn Adams, in the trailer that dropped 26 August 2026, describing the goal
in one sentence a language designer could have written:

> Procedural magic systems that go beyond combining spell effects and go
> straight to the fundamental cosmological makeup of the universe. This
> allows magical situations that you cannot get any other way. […] everything
> that makes fantasy what it is, with every piece tied into how that
> particular universe works down to its bones.

The negative half of that sentence is the interesting half. *Not* a list of
effects to combine. The alternative he rejects — "you could come up with a
list of effects, but you can't use those unless you generate a magic system
of some kind, or just put in one magic system like we have with the
necromancers, and that's what we want to avoid"
([PC Gamer interview](https://www.pcgamer.com/dwarf-fortress-creator-tarn-adams-talks-about-simulating-the-most-complex-magic-system-ever/))
— is precisely the design Magic: The Gathering shipped and has been paying
for ever since.

## The Korz move, one level up

The subtraction in the [Korz README](../../README.md) runs: Smalltalk said
everything is an object but classes ruled them; **Self** removed the classes;
**Korz** removed the object boundary. Each step deleted a privileged
structure and got more expressiveness back than it gave up.

Dwarf Fortress deletes the privileged **effect list**. What remains is a
cosmology that generates both the axes and which slots exist along them.
Tarn's example is exact about the mechanism:

> If the forest became alive because the primordial god died and sprinkled
> its blood on it, but that primordial god has other traits as well, those
> other traits could come in and influence what forest spirit magic is
> actually like. And it would be completely unique to that world.

Read as Korz: the myth generates coordinates (*this* god, *these* spheres,
*that* death event); forest-spirit magic is a set of slots guarded on those
coordinates; and the guards are not authored, they are **fitted** — "a
natural grouping of say 20-30 effects […] They'll be different in every
world. Some worlds won't have raising the dead at all. Some worlds will have
so much dead raising that everyone's practically immortal."

**Where the analogy needs a correction, and it is a productive one.** Korz's
dimensions are declared by a programmer at design time; the paper's whole
demonstration is that a *new* dimension can be added to a running design
without touching intermediate code. Dwarf Fortress generates the dimension
set itself, per world, and — see below — mutates it during play. That is past
what Korz specifies, and it lands exactly in [Korz′](../README.md)'s
territory: the soft tier improvising coordinates the strict tier never
declared. Which makes this the best available target for the question "what
would it mean for the *lattice* to be generated?"

## The pop()/assertions trick, fired in anger

The Korz paper's showpiece: `main()` turns assertions on, a more specific
`pop()` starts winning, and **no intermediate code mentions assertions** —
the binding flows implicitly down every send beneath.

Tarn, describing a mid-game mythological event:

> They might accidentally trigger something that flips it back, and changes
> the rules. And suddenly people's teleport spells don't work anymore, and
> they'd have to be able to deal with that. All these social clubs break down
> because no one can visit each other anymore.

One coordinate unbinds at the top. Thousands of agents re-dispatch
underneath, and nothing in between was written to know about it. That is the
paper's example with a body count. It is also the thing Korz is *for*: not
that the flip is possible, but that no intermediate layer had to anticipate
it.

The upstream case is the same shape, without the drama. "If teleportation is
easy, that changes everything about the world. That changes economy,
diplomacy, espionage, everything." And most of it is free:

> If someone says "I want to go here" and then they're like "oh, I just can,"
> then it will work that way […] I didn't have to program anything, except
> for the teleport effect, and they know that it's linked to moving around.

## Which is the Sims advertisement economy, generated

That last quote is the bridge to the other shipped dispatcher in this
collection. Tarn's agents do not read the code; each action **advertises what
it is for**, and agents interrogate the advertisement:

> It's how we do it now when we have the cat licking itself. It knows that
> action is about cleaning contaminants off their body. […] We give them
> helpful hints, so they don't have to read the code themselves.

Then the scoring, when the effect is not free — teleportation that costs a
week of nausea and a quarter of your blood:

> There's still cases where teleport is valuable. So then you need to teach
> them a cost/benefit analysis type thing […] There's a cost to this
> movement, and the cost is, "how much do I value my blood?"

[The Sims advertisement economy](sims-advertisements.md) is that auction, in
shipped commercial software, and the two systems converge from opposite
directions: The Sims hand-authors the advertisements and scores them against
frozen motive dimensions; Dwarf Fortress **generates the effects, their
advertisements, and the dimensions they score against** from a myth. Same
dispatch-as-auction mechanism, with world-gen moved underneath it.

## The three gathers of one sea

The subjective-projection claim — gather the sea along `rcvr` and you see
objects, along `assertions` and you see the checking layer, along `user` and
you see one person's view — is usually demonstrated with a toy. Dwarf
Fortress ships it, and has for years, which nobody seems to say out loud:

| Mode | The gather | Structure |
|------|-----------|-----------|
| **Fortress** | the map, tile by tile | a lattice |
| **Adventure** | one body walking between sites | a room graph |
| **Legends** | the history, as prose and lineage | a record |

One simulated world; three coordinate systems; no mode is the real one.
Tarn notes that a whole class of players never touches the first two — "they
just do archaeology on the worlds they've generated." That is a population
of users who live entirely in the third projection.

And it settles a debt in this directory. [`grid-as-rooms`](grid-as-rooms.md)
argued that a cellular automaton and an adventure map are one structure at
opposite ends of an exit-wiring regularity axis, and that "the middle is
empty, and that is where the interesting systems are." Dwarf Fortress is not
in the middle — it is **both ends over one world**, with a lattice view and a
room-graph view of the same sea. The specimen that example wanted is a game
that has shipped since 2006.

## The dispatch bill

Korz-shaped systems have a characteristic cost, and Dwarf Fortress pays it in
public. From a detailed community explanation in the
[HN thread](https://news.ycombinator.com/item?id=49467636) on the magic
announcement: every person and animal has an opinion of every other, mood
changes fire on *seeing* someone they like or dislike, and the opinion
depends on interaction history and degree of consanguinity — so each movement
triggers line-of-sight checks against everyone visible, and a relatedness
computation for each. "The fundamental O(n²) behavior remains, but caching
has greatly improved performance."

That is symmetric multi-dimensional dispatch — guards on viewer, viewed,
kinship, shared history — evaluated continuously, and the fix was a
**cache**. The same crystallization story as the traffic light in
[`mfm-city`](mfm-city.md) turning out to be a polymorphic inline cache, and
the same one Self's JIT told about types.

The player-side mitigations are funnier and more instructive: cut the
population, cage the animals behind closed doors, and break long corridors
with corners so fewer pairs are ever in scope. Fortress architecture as
**dispatch-domain engineering** — and the reported outcome is that
zigzag-corridor forts run fast and "feel terrible to the player," which is
what optimizing the dispatcher at the expense of the program looks like from
inside.

## Technical sources, ranked

Primary, in the developers' own words:

| Source | Why it matters |
|--------|----------------|
| [Bay 12 dev notes](https://bay12games.com/dwarves/dev.html) | The roadmap Tarn maintains; myths and magic "probably through the avenues of covens and religion" |
| **Future of the Fortress** monthly Q&A | Tarn answers technical reader questions directly; the January 2026 round covers spheres of an item determining which magic is available, and remnants from the myth generator becoming artifacts |
| GDC 2016, Tarn Adams with Tanya Short — procedurally generated mythology | The myth generator demonstrated live, including the cosmic egg whose fragments become continents in the map generator ([writeup](https://procedural-generation.isaackarth.com/2016/04/06/mythology-and-procedural-generation-no-one-seemed.html)) |
| [PC Gamer, "the most complex magic system ever"](https://www.pcgamer.com/dwarf-fortress-creator-tarn-adams-talks-about-simulating-the-most-complex-magic-system-ever/) | The long interview quoted throughout this page — myth-first design, per-world effect sets, teleportation, rule flips |
| [PC Gamer, creative mode and homemade gods](https://www.pcgamer.com/future-dwarf-fortress-creative-mode-will-let-you-sculpt-whole-worlds-create-homemade-gods/) | "The system like a giant debugger […] it has to have an API that hooks into as much stuff as you can in the game. Can you make a love potion that would actually affect thoughts and relationships that already exist?" |
| [Kitfox devlog](https://kitfoxgames.itch.io/dwarf-fortress/devlog/886081/next-steps-for-dwarf-fortress-patch-5105-dwarf-fortress-dev-news) | Release sequencing; the Lua upgrade as the foundation for Myth and Magic |

**The best source is code, and it is now readable.** The July 2025 scripting
overhaul, driven largely by Putnam, exposed procedural generation that had
been hard-coded for fifteen years as moddable Lua — forgotten beasts, divine
curses (vampires and werebeasts), divine items, necromancers and their
experiments, evil weather. Tarn: "Now the algorithms and data are available
for modding"
([PC Gamer](https://www.pcgamer.com/games/sim/dwarf-fortress-just-made-it-easier-for-modders-to-add-their-own-procedural-creatures-items-curses-and-more-all-of-these-things-have-been-hard-coded-in-dwarf-fortress-inaccessible-to-modders-now-the-algorithms-and-data-are-available/)).
A procedural generator whose guard structure you can read, in a scripting
language, shipped inside the game — that is the artifact this example should
be built against next. ⚠ The install path and the scripts' actual shape are
unverified here; that is the first research action, not a claim.

Community-technical, useful but secondary: Blind's video essay on how
procedural magic will change the game, the
[wiki's Sphere page](https://dwarffortresswiki.org/index.php/Sphere) for the
current coordinate vocabulary, and DFHack, whose existence is itself evidence
about which internals are addressable.

## Open

1. **Read the Lua.** Do the exposed generators dispatch on sphere-like coordinates, or switch on enumerated types? The answer decides whether this example is a Korz reading or a Korz proposal.
2. **What is a sphere, formally?** The wiki lists them as flavors attached to deities and items. If item spheres determine available magic, spheres are the coordinate space and the lattice is enumerable.
3. **Does the myth generator produce a lattice or a story?** Korz needs the former. Tarn describes narrative events with mechanical consequences, which may be the same thing viewed from the other end — the honest answer needs the generator's output format.
4. **Balance.** "We don't care about balance, here." Magic cares enormously, and pays in layers. Worth asking whether legislated order is a *tournament* artifact rather than a dispatch necessity.

*See also:* [`mtg-layers.md`](mtg-layers.md) for the same problem with the
dimensions printed on cards and a total order legislated over them;
[`case-zork.md`](../../case-zork.md) for the adventure-game line this joins;
[`ask-david.md`](../../ask-david.md) for the generated-lattice question in the
form to put to David.
