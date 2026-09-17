# Character Endosymbiosis

*How moving characters, rooms, environments, objects, and stories between games is the same
trick life used to build complex cells.*

This is where the word **organelle** comes from, everywhere else in this skill.

---

## The idea in one breath

Treat each game as a **cell**. Treat each piece of content — a character, a room, an object, a
story — as something that can **live inside a membrane, cross it, and take up residence
somewhere else**. Treat **Soul City** as the shared cytoplasm all the cells float in and trade
through. Suddenly "moving a Sim into Stardew" isn't a file conversion — it's cell biology.

## A two-minute biology detour

A billion-odd years ago, life was simple cells. Then something profound happened: a big cell
engulfed a smaller free-living microbe and — instead of digesting it — **kept it alive and put
it to work**. That guest became the **mitochondrion**, the powerhouse that still carries its
own DNA inside your cells right now. The same story gave plants their **chloroplasts**. This is
**endosymbiosis**, the theory Lynn Margulis fought to establish: *the complex cell is a
confederation of once-independent lives living together behind shared membranes.* Evolution by
cooperation and merger, not only by competition.

Three facts from that world do all the work for us:

1. **Membranes are selectively permeable.** They decide what crosses, which way, and under what
   conditions.
2. **Things diffuse.** A concentration in one compartment bleeds into its neighbors.
3. **Trade needs currency.** Cells run on ATP and shuttle value across membranes with carriers
   and exchangers.

## The mapping

| Biology | Here |
|---|---|
| Cell / organelle | A **game** (Sims, Spore, Stardew, Mind Mirror, Afterlife…) |
| Cytoplasm / host | **Soul City** — the git-checked-in hub everything floats in and trades through |
| Organelles, **parallel and nested** | **Sub-directories** — the filesystem *is* the cell; nesting is organelles within organelles |
| Membrane | Each game's **import/export boundary** — selectively permeable |
| Molecules / genes | **Characters, rooms, environments, objects, stories** — the content that moves |
| Diffusion | A trait, mood, relationship, or story beat **bleeding into sibling** content |
| Selective permeability | Player-defined **constraints, workflows, transformations** — the channels and pumps |
| Active transport | **Import/export** — round-tripping content out through Soul City and into another game |
| Currency exchange | **Schema mapping** between games with different economies — the exchange rate |

**Organelles ⇔ sub-directories** is the line the whole architecture rests on. A directory is a
membrane-bound compartment. Put a directory inside a directory and you have an organelle inside
an organelle — a mitochondrion with its own internal structures, its own little genome (its own
files and rules). The tree is alive.

## Diffusion, constraints, and the exchange rate

When a character crosses from one game into another, three things happen, exactly as at a cell
membrane:

- **Permeability decides if it crosses at all.** Your constraints are the membrane's channels:
  this game accepts faces and relationships but not inventory; that one wants needs and skills.
- **Diffusion spreads what got through.** A personality reading doesn't just sit in one
  character — it can **diffuse into siblings**, nudging a whole household. High concentration
  here, lower there, and the gradient does the rest.
- **Currency exchange reshapes the values.** Two games rarely share units. Crossing the border
  means **changing money**: a transform maps one game's schema to another's. Schema
  *recognition* is the exchange rate; a **lossless round-trip** is a fair, reversible rate that
  never quietly skims your character on the way through.

That last point is the biological reading of
[PORTABLE-NPCS.md §6 — customs](PORTABLE-NPCS.md#6-customs-the-trolls-luggage), which arrives at
the same rule from the economics side: value is world-relative, wealth lives in the instance,
provenance rides along, and a rate of zero is legal. Two vocabularies, one constraint.

Some organelles are extraordinary. An **emulated runtime** — a real Apple ][ binary running in a
web emulator, say Timothy Leary's *Mind Mirror* (1986) — is an organelle **still running its own
ancient metabolism**: a living mitochondrion you feed a character and read back transformed.

That one is not a hypothetical, and it is closer than it looks: the `mind_mirror` block every
soul carries — four thought planes, eight traits each — is named after that program and copied
from its model. Sending a character to *visit the shrink*, letting the player edit a mind in the
1986 app, reading the floppy back, and diffusing the result onto her Sims stats is the first
errand worth building, because the outbound mapping is nearly an identity. It also audits us:
a `mind_mirror` block that cannot survive a round trip through the program it was named after
has drifted from the schema, which the
[62-character survey](../../designs/mind-mirror-survey-2026-02-07.md) found is the normal
condition. Worked out in
[`OUT-OF-GAME-JOBS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/OUT-OF-GAME-JOBS.yml).

### Three honest ways to compute a transform

The exchange rate above is a *policy*, and it can be computed three ways. Thirty-two trait values
becoming five Sims axes is a lossy projection with no single correct answer, so the mechanism is a
choice the player should get to make and see:

| Way | What it is | What you get | What you give up |
|---|---|---|---|
| **Linear** | A weight matrix, authored once | Offline, instant, free, identical on every machine forever, explainable term by term | Interactions between traits that a matrix flattens |
| **Learned** | A small model fit to examples, including the player's own corrections | Catches those interactions, still local, still repeatable | Line-by-line explainability |
| **Imagined** | A language model reads the whole profile and history and proposes changes with reasons | Judgment: that *this* profile on *this* character means she came home quieter | Determinism, and the arithmetic audit |

Linear is the default and the fallback, because a character's stats should not depend on network
weather. The other two are things the player asks for. Whichever runs, the diffusion arrives as a
**proposal with its method named** rather than as a silent side effect — which is the same
discipline the whole skill applies to arrival, publication, and crossing.

## Two minds, two layers

Every organelle so far has been a game. But there is one more site a mind can live in, and it
isn't a game: **the layer that watches the games.** The overlay, the recorder, the album — the
thing holding the screen and the clock. A soul can keep an organelle there too, and for some
characters that is the more interesting half.

Take a photographer. Inside the game she is a character with her own behavior: she walks to the
thing worth shooting and takes the picture the game knows how to take. Outside, in the layer,
the same soul runs a mind that watches the screen, holds a beat, and writes the copy. The body
takes the picture; the outside mind knows what the picture is *of*, and what it will mean three
weeks later when it is page four of a story.

**They are not redundant, because they have different senses and different clocks.** The in-game
mind perceives only what the game represents — a Sim cannot notice that a moment is a good lede,
because "lede" is not in the world's ontology. The outside mind sees the screen, the history, the
album, and every other game, and cannot walk across a room or exist in a save file. Neither one
is the real one. Squashing them together would mean throwing away one of the two sensoriums.

The coupling is not shared memory. It is a stream of **credited events**: the inside raises them,
the outside receives them and attaches them to a beat. The membrane holds — neither mind reads
the other's internals, which is the same discipline every other organelle boundary obeys. And
either half runs alone: an in-game photographer with no outside mind still takes in-game
pictures, and an outside correspondent with nobody in the game still watches the screen and
files.

The word for this shape is **bicameral** — two chambers, with one voice arriving from somewhere
the other chamber cannot see. We borrow Jaynes's picture, not his theory about ancient minds.

The same structure explains why a character can be *away*. When she goes on an errand into
another game, what's left behind is an in-game organelle standing in for a mind that is
temporarily elsewhere — a placeholder that can still be talked to
([SOUL-BRIDGES.md § The errand](SOUL-BRIDGES.md#the-errand-a-job-in-another-game)). And it
explains the limit that keeps the whole arrangement honest: an outside mind has no hands inside
the game except the ones the membrane offers it, which is usually a menu.

## Why this framing earns its keep

It fuses three vocabularies into a single intuition — the **filesystem** (directories and data),
**biology** (cells, organelles, membranes, diffusion), and **economics** (currency and exchange)
— and it explains the architecture *without a spec sheet*: permeable membranes, diffusion,
selective transport, honest exchange rates.

And it reframes "data portability" as something far older and more alive. Complex life didn't
scale by one cell doing everything; it scaled by **letting independent things live together,
keep their own nature, share a medium, and trade across membranes**. That is exactly the
proposal: rich worlds composed by letting content live in many membranes at once —
round-trippable, diffusing, trading — the trick evolution used to put a world inside a cell.

> Build the generic hub and spokes first: every game round-trips cleanly with Soul City. *Then*
> grow the shortcuts — direct fast paths and mutual schema recognition between compatible games,
> the way symbionts evolve dedicated channels to the partners they trade with most.

## Kindred vision — Lem's Trurl, building worlds in boxes

Stanisław Lem got here first, in fiction. In a passage of *The Cyberiad* left out of the English
translation, the constructor **Trurl** tries to build happy worlds — first whole cultures, then
a civilization in a small box, then **hundreds of miniature worlds on microscope slides** he has
to watch through a lens. The slide-worlds even achieve **inter-slide travel** (spokes between
organelles), and eventually Trurl builds a computer to do the research, which instead **expands
itself** and spawns sub-Trurls. Microworlds in boxes, traffic between them, a self-replicating
medium — the same shapes, told as a cautionary fable. (Summary of the untranslated passage:
[HN 12634472](https://news.ycombinator.com/item?id=12634472).)

## See also

- [SOUL-MODEL.md → Organelles, minds, membranes](SOUL-MODEL.md#organelles-minds-membranes) — the ontology this doc explains
- [PORTABLE-NPCS.md](PORTABLE-NPCS.md) — the same border, read as economics: treaties and customs
- [SOUL-BRIDGES.md](SOUL-BRIDGES.md) — what actually crosses into a shipped game's save file
- [MicropolisCore → characters-as-hydrogen.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md) — the chemistry companion to this biology
