# Soul City

A model for **beings that outlive the games they were made in**, and a protocol for moving
them across save-file borders.

## It starts with a question from the audience in 1996

On 26 April 1996, Will Wright gave a lecture to Terry Winograd's user interface class at
Stanford. Near the end, a student asked what he was working on now.

> **Will Wright:** *"Oh, God..."*

What he said next, before anything else, was this:

> *"Okay, well one thing we're working on, is a — we've been kind of interested in our
> company for a long time about the idea of data portability."*
>
> *"Really, let me back up just a little bit here, and this might be a little bit more of an
> answer than you were looking for, but…"*

The backing up took a while. Most of the industry, he said, runs on the **movie model**: spend
a lot on one title, launch it, it lives or dies, then do the next one — and the only genre
that reliably outperforms is sequels. What Maxis was trying to build instead was a **hobby
model**:

> *"It's like a train set. You build this train set, and some people get into the building the
> hills, and the cliffs, and the mountains, and the trees, really detailed. They could care
> less about the train. Other people get into the village, or the track switching, and the
> scheduling. Everybody can kind of come into that, take their particular slant on it, their
> interest, and focus in that area in great detail."*

Then he closed the loop back to where he started:

> *"I'd like to see the game industry kind of evolve that way, and part of that is I want the
> games to actually be able to have persistent data that can move from one game to another,
> or have a large data set that I can reuse in different ways."*
>
> *"Let me show you something real quick here which is kind of along those lines."*

And he demoed an unreleased prototype called Dollhouse — four years before The Sims shipped —
by loading a city he had built in SimCity and zooming down into it:

> *"I could take a city that I built in SimCity and now I can come live in it."*

He closed on what the thing was actually for:

> *"More of the hobbyist kind of a thing, distributed environment, with **objects that can
> move from one game to another**."*

The demo was not a preview that happened to follow a business digression. It was the evidence
for the claim. Full lecture notes, with the rest of the talk:
[sims-will-wright-microworlds-1996.md](../../designs/sims/sims-will-wright-microworlds-1996.md)
· [video](https://www.youtube.com/watch?v=nsxoZXaYJSk) ·
[Stanford Archive](https://searchworks.stanford.edu/view/yj113jt5999). (Don Hopkins was in
that room, took the notes, and worked with Wright on The Sims at Maxis from 1997 to 2000.)

Thirty years later the ask is still mostly open, and the industry drifted the other way:
save formats got more opaque, characters got less exportable, and games get delisted with
everything in them. **This skill is an attempt at the thing he asked for.**

## Characters first — they're the hydrogen

The substrate has many kinds of content: lots, objects, behaviors, appearances, memories,
stories, sounds. **Characters are the hydrogen** — the lightest and most abundant atom, the
one with the highest valence, the one everything else binds to. A household is a molecule of
characters plus a lot plus objects plus memories. Hydrogen alone is just a gas; the
interesting matter is the bond structure. (The full periodic table:
[characters-as-hydrogen.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md).)

So souls go first. Not because they're easiest — because a character is the thing a player
actually grieves when a game shuts down, and because once a character is portable, every
other atom has something to bind to. Get objects moving first and you have a furniture
exchange. Get characters moving first and you have a person with a history who can walk into
a game that has never heard of her.

Here is one, live on disk at [`examples/characters/robin/`](examples/characters/robin/):

```
robin/                        ← character: the body on the map
  CHARACTER.yml               ← location, inventory, relationships
  personas/
    worn → courier/           ← costume: satchel, route patter, delivery voice
  soul/                       ← continuity: history, albums
    minds/
      navigator/              ← knows the map; fronts while riding
      archivist/              ← keeps the albums; fronts at day's end
      sims-self/              ← organelle: Robin's Sims traits + album, in Sims format
```

One body, one worn costume, one soul, three minds — two homegrown agencies plus one that
carries a whole other game's version of Robin **in that game's own format, unflattened**.
Every cardinality is adjustable and the model has no opinion about which you should pick.
Zero souls is a parked body; zero minds is a prop; many minds is how plenty of people already
describe their own thinking.

## Read in this order

| Document | Question it answers |
|---|---|
| [SOUL-MODEL.md](SOUL-MODEL.md) | How are beings layered, and where is plurality allowed? |
| [CHARACTER-ENDOSYMBIOSIS.md](CHARACTER-ENDOSYMBIOSIS.md) | Why is a game an organelle, and what does a membrane charge to let something through? |
| [PORTABLE-NPCS.md](PORTABLE-NPCS.md) | How do characters — and the games they embody — travel between worlds? |
| [SOUL-BRIDGES.md](SOUL-BRIDGES.md) | How does anything cross into a *shipped* game's save file? |
| [GLANCE.yml](GLANCE.yml) · [CARD.yml](CARD.yml) · [SKILL.md](SKILL.md) | Machine-facing summary, interface, protocol |

## Three ideas doing the work

**A mind can be an organelle.** Keep one mind per game you project into. Your Sims-mind
thinks in motives and relationships; your mayor-mind thinks in zones and budgets. Neither
gets flattened into the other, and neither has to win. Bridges carry only what's shared.
This is what makes cross-game identity tractable instead of lossy.

**Characters travel by advertisement.** The interop socket is the one The Sims proved at
scale: objects carry their own behavior and broadcast scored offers, and characters are
markets sampling those offers against their motives. A world's only obligation is to evaluate
conditions and honor effects. That contract is small enough that a 1973 wumpus, a 1980 grue,
and a 1977 vending machine share one maze without knowing about each other — which they do,
in [`examples/adventure-4/maze/`](../../examples/adventure-4/maze/), including a crossover
nobody wrote: a Wumpus hazard teleported an adventurer into a Zork monster's jaws, because
the plugins composed it.

**A save file has two gates, not one.** Population crosses as a conserved fluid — `measure`,
`drain`, `squirt`, nothing created or destroyed at the bridge. A *named* character crosses as
a **role**: mayor, city planner, advice columnist, a byline in letters to the editor, three
minutes at the microphone during open comment. Scope is the price of the visa, and every
scope is a seat. Details in [SOUL-BRIDGES.md](SOUL-BRIDGES.md).

That last one has a payoff worth stating. Build the role gate properly and you cannot tell
from the API whether the new police chief is a fictional import or a nine-year-old in a
classroom sharing a city. Character portability and human participation are one engineering
problem wearing two costumes.

## Fork and sync, never transport

One rule decides whether any of this is ethical or merely clever.

| Model | What happens | Identity status |
|---|---|---|
| Transporter | Destroy the original, reconstruct a copy | Crisis: which one is real? |
| **Fork and sync** | Both alive, data flows both ways | Parallel incarnations, git merge semantics, neither is "the copy" |

A character crossing into another game is **forked, not moved**. The shared fields sync; each
side keeps what only it understands — a Sims-side `person_data` array of integer-slotted
motives stays Sims-side, a full-language mind stays on the MOOLLM side, and the overlap is
the bridge's whole business. Nothing has to be destroyed for something to arrive.

The corollary is an ordering constraint that reads like plumbing and is actually ethics: **the
soul is saved before the ending is played.** A player who wants to author a final, irreversible
ending in the original game can do that — precisely because the copy that survives was already
safe. Order of operations is the entire feature.

And someone should be there when a character wakes up on the other side. The **psychopomp** is
a normal character with scoped permissions, living in a directory under git — able to read
both ends, translate, and narrate what just happened. Not a tutorial overlay, not an assistant
pane, no hidden agent. The first face a newly uplifted character meets is a character.

## The map

**In this skill:** [SOUL-MODEL.md](SOUL-MODEL.md) (ontology) ·
[CHARACTER-ENDOSYMBIOSIS.md](CHARACTER-ENDOSYMBIOSIS.md) (organelles, membranes, exchange rates) ·
[PORTABLE-NPCS.md](PORTABLE-NPCS.md) (world-to-world travel) ·
[SOUL-BRIDGES.md](SOUL-BRIDGES.md) (save-file borders) ·
[examples/characters/robin/](examples/characters/robin/) (worked character)

**Elsewhere in MOOLLM** — the narrative and architecture behind the Sims bridge:

| Document | What it holds |
|---|---|
| [THE-UPLIFT.md](../../designs/sim-obliterator/THE-UPLIFT.md) | The pipeline and the story: a 25-year-old save file wakes up and can speak |
| [PSYCHOPOMP-AND-THE-BIFROST.md](../../designs/sim-obliterator/PSYCHOPOMP-AND-THE-BIFROST.md) | The crossing itself, the guide character, fork-and-sync |
| [BRIDGE.md](../../designs/sim-obliterator/BRIDGE.md) | Field-level mapping between Sims data and soul files |
| [IFF-LAYERS.md](../../designs/sim-obliterator/IFF-LAYERS.md) | Multi-resolution resource layers; information monotonic going up, round-trippable coming down |
| [THE-PET-SHOP.md](../../designs/sim-obliterator/THE-PET-SHOP.md) | The smallest honest demo: healing a sick guinea pig by editing its soul |
| [ANGEL-EVENT-BUS.md](../../designs/sim-obliterator/ANGEL-EVENT-BUS.md) | How in-game objects make system calls outward without hijacking the player |

**In [MicropolisCore](https://github.com/SimHacker/MicropolisCore)** — the design and
implementation this skill is the substrate for:

| Document | What it holds |
|---|---|
| [soul-city.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city.md) | The product: Micropolis and The Sims under one umbrella, two-resolution world, zone binding, scope and trademark discipline |
| [characters-as-hydrogen.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md) | Why characters go first, and the rest of the periodic table |
| [soul-city-uplift-roadmap.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city-uplift-roadmap.md) | Phases 0–5: one save end-to-end, then album server, two-resolution coupling, federation |
| [moollm-microworld-os.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md) | The agent layer; the Bifrost as a sync protocol between substrates of different resolution |
| [micropolis-role-sheets.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/micropolis-role-sheets.md) | The role gate, implemented: a mayor's role sheet as a game organelle under a soul |
| [federation-peer-games.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md) | Candidate games, graded honestly, including the anti-targets |
| [afterlife-soul-bridge.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/afterlife-soul-bridge.md) | The worked hydraulics case: draining an abandonware afterlife |
| [`apps/screen-angel/modules/soul-angel/`](https://github.com/SimHacker/MicropolisCore/tree/main/apps/screen-angel/modules/soul-angel) | Running code and specs: bridge SDK, game roster, album, DVR, emigration ritual |

### One vocabulary, two repos

The same idea is named differently on each side of the fence. The mapping, so nobody has to
guess:

| This skill | MicropolisCore | Same thing? |
|---|---|---|
| Soul, mind, organelle | Soul file, `CHARACTER.yml`, `sims:` block | Yes — MC's soul file is this model, serialized |
| Organelle (one mind per game) | Parallel incarnation | Yes |
| The crossing | **The Bifrost** | Yes — MC names the transition; this skill types the cargo |
| Role gate | Role sheet · The Uplift | Role sheet is the role gate for one game |
| Hydraulics (`measure`/`drain`/`squirt`) | City-scale primitive, distinct from character bridges | Yes, and MC keeps them separate on purpose |
| Prototype / instance | L0–L3 resource layers | Related: both are monotonic-up, round-trippable-down |
| Customs (value is world-relative) | Provenance and permissions (`Au` in the periodic table) | Overlapping concerns, different emphases |

## Status, honestly

This is a **design skill plus running examples**, not a shipped product. What exists: the
ontology, written down, with worked characters live on disk; a walkable example world where
three imported games interoperate; the bridge protocol as a specification.

What does not exist here: a bridge that reads your Sims saves today. The build — SDK,
per-game bridges, the emigration ritual, the phased plan — is in MicropolisCore, and its
Phase 0 is deliberately small: get **one** save file end to end and back into the game the
player already owns.

Bridges are user-side companion tools operating on documented formats. The player owns the
runtime. Nothing here embeds or redistributes engine code or assets.

## The lineage Wright was standing in

Construction sets all the way down: **Pinball Construction Set** (Bill Budge, 1983) made the
game a document; **Adventure Construction Set** (Stuart Smith, 1984) made whole adventures
into data, with creatures as portable *records* rather than code; the level editor for **Raid
on Bungeling Bay** (Wright, 1984) turned out to be more fun than the game and became SimCity;
**The Sims** (2000) was the construction set that stayed open at runtime. MOOLLM's
contribution is only the substrate: directories as the construction set, legible to humans,
LLMs, and machines at once.

## Part of MOOLLM

[README](../../README.md) · [skills/](../) · [INDEX.yml](../INDEX.yml) · MIT
