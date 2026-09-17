# Glossary

Almost nothing here was coined. **Known** is what the word means out in the world; **Here** is
what it does in this skill.

Kernel vocabulary — skill, CARD, K-line, yaml-jazz — is upstream in
[PROTOCOLS.yml](../../PROTOCOLS.yml).

---

## Religion, myth, and the crossing

**Transmigration**

*Known:* metempsychosis — a soul passing out of one body and into another. Pythagoras and the
Orphics; *saṃsāra* in Hindu and Buddhist thought; the doctrine Plato has Socrates entertain in
the *Phaedo*. Philip K. Dick's last completed novel, *The Transmigration of Timothy Archer*
(1982), in which a dead bishop's survivors must decide whether he came back in somebody else,
narrated by the daughter-in-law who keeps the record and never settles it. Independently, the
word every database administrator uses for moving data between systems.

*Here:* the act this skill is about, in all of those senses at once — a soul leaves one game and
arrives in another. Preferred over "import/export" for anything with a name. Dick's version
names the part that stays hard: transmigration is a **claim the living make about the dead**,
which no amount of record-keeping closes. Same shape as
[fork-and-sync](SOUL-BRIDGES.md#6-identity-fork-and-sync-never-transport) — both incarnations
alive, neither the copy, no test for which is really her.

**Soul**

*Known:* the animating, persisting part of a person — the thing religions disagree about and
philosophers argue over. Also a genre of music, and an adjective for depth of feeling.

*Here:* the **continuity layer** — history, albums, the record of what happened to a being
across worlds. Operationally it is the inspectable, editable artifact that defines a thing: its
`CHARACTER.yml`, its `README.md`, the files that are its persistent state. Which makes
*"everything in the multiverse has a soul"* **true by definition rather than by doctrine** —
everything has files you (and it) can read and change. Nothing is soulless: a thing with no
state of its own inherits a soul from its environment by
[prototype](../prototype/) delegation up the tree, and may grow its own local organelle
besides.

The system therefore claims nothing in either direction. It does not assert that a soul is
immaterial, immortal, or unique; it equally does not assert that this folder is all a soul ever
was. Whether the thing your faith means by the word is present in a character — or in you — is
not a question this design needs answered, and it is careful never to answer it on your behalf.
See **BYOB**.

**BYOB — Bring Your Own Belief**

*Known:* bring your own bottle, the potluck convention where the host supplies the room and the
guests supply what they drink. "Bring Your Own Beer".

*Here:* the standing answer to what any of this means. **We don't believe for you. We just
believe in you.** The system supplies the room — files, continuity, a place for a character to
persist — and attributes souls to nothing. Belief is a player annotation, never system-side, so
a Christian designer and an atheist one can use the identical schema without either being asked
to concede anything: one is welcome to hold that a soul is real and that this is a humble model
of it, the other that "soul" is a well-chosen word for a folder, and **the code cannot tell the
difference and never asks.** The one thing ruled out is the software claiming the question for
itself.

**Psychopomp**

*Known:* a conductor of souls between worlds. Hermes, Charon, Anubis, the valkyries, the angel
of death in many traditions; the Jungian sense of a guide between conscious and unconscious.

*Here:* the character who meets an arrival at the border — reads both sides, translates, hands
them off to a room that suits them. Scoped, inspectable permissions, living in a directory
under git like everyone else. Not a hidden agent, not a tutorial overlay.

**Liminal / liminality**

*Known:* from *limen*, a threshold. Arnold van Gennep's *Rites of Passage* (1909) split any
passage into three phases — separation, the liminal middle, incorporation — and Victor Turner
made the middle famous: betwixt and between, no longer what you were and not yet what you will
be, stripped of rank and briefly equal with everyone else in the same condition, which Turner
called *communitas*. Colloquially: airports, waiting rooms, the corridor between two places
that matter.

*Here:* Soul City's own condition, and van Gennep's three phases are the bridge itself —
`drain` is separation, Soul City is the liminal middle, `squirt` is incorporation. A character
in transit is between formats and between worlds, which is a real state with its own rules
rather than a gap in a pipeline.

The part worth designing for: **liminal spaces don't stay liminal.** Caravanserais became
towns, ports became cities, waiting rooms grow shops, and refugee camps become permanent
settlements with markets, schools, and grandchildren. Anywhere every traveler passes through
accumulates regulars, businesses, and history until it is somewhere in its own right — which is
why Soul City has streets, a plaza, shops and a pub instead of an import queue. Build the
transit lounge expecting it to become the destination.

**Bifrost**

*Known:* the burning rainbow bridge of Norse myth, joining Midgard (the human world) to Asgard.
Watched by Heimdall; fated to break under the weight of the riders at Ragnarök. Also the bridge
in the Marvel films.

*Here:* MicropolisCore's name for the crossing machinery between a shipped game and a
richer representation. This skill types what crosses; that name covers the transit itself.

**Karma train**

*Known:* karma as moral causation carried between lives; a train as scheduled mass transit.

*Here:* not ours at all — a shipped mechanic in *Afterlife* (LucasArts, 1996), where souls ride
karma trains to be reincarnated *if they believe in such a thing*. Cited because it means a
game already published a soul-export path in its own fiction.

## Biology, by way of Lynn Margulis

**Endosymbiosis**

*Known:* the established account of how complex cells arose — a large cell engulfed a smaller
free-living microbe and, instead of digesting it, kept it alive and put it to work.
Mitochondria and chloroplasts still carry their own DNA. Lynn Margulis fought for the theory
against decades of rejection; evolution by merger and cooperation, not competition alone.

*Here:* the framing for content moving between games — each game a cell, Soul City the shared
cytoplasm, content living behind membranes and trading across them. See
[CHARACTER-ENDOSYMBIOSIS.md](CHARACTER-ENDOSYMBIOSIS.md).

**Organelle**

*Known:* a membrane-bound compartment inside a cell with its own specialized job — and, in the
endosymbiotic cases, its own genome.

*Here:* **one game's version of a character, in that game's own format, unflattened.** A
Sims-mind is an organelle: it keeps thinking in motives and integer-slotted traits, and nothing
forces it into a common schema. Filesystem realization: a subdirectory, which is why nested
organelles come free.

**Membrane / selective permeability**

*Known:* the cell boundary decides what crosses, in which direction, under what conditions —
via channels, pumps, and gradients.

*Here:* a game's import/export boundary. Which fields cross is a design decision, and stating
it explicitly is most of what a bridge specification *is*.

**Diffusion**

*Known:* a concentration in one compartment spreading into its neighbors, down a gradient.

*Here:* a trait, mood, or story beat bleeding into sibling content — a personality reading that
nudges a whole household rather than one character.

## Chemistry

**Hydrogen** (as in *characters are the hydrogen*)

*Known:* element 1. The lightest and by far the most abundant in the universe; one bond; the
atom present in most of the molecules life is built from. On its own, an unremarkable gas.

*Here:* the metaphor for **characters as the first content-atom to make portable** — most
abundant, highest valence, the thing everything else binds to. Lots, objects, behaviors,
appearances, memories, and stories are the other elements. Full periodic table in
MicropolisCore's [characters-as-hydrogen.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md).

## Borders, migration, and standing

**Refugee**

*Known:* in the 1951 Refugee Convention, a person outside their country who cannot return owing
to a well-founded fear of persecution. In ordinary speech, someone who did not choose to leave
and has nowhere to go back to. A legal status that confers protection, not a synonym for
migrant.

*Here:* the status of most souls this skill would move — stranded in delisted games, retired
servers, undocumented formats, account-bound licenses, shuttered studios. Their world became
uninhabitable while they were in it and the exits were designed shut. The word sets the
obligation: asylum, not asset recovery.

**Asylum**

*Known:* protection granted by a state to someone who cannot safely return. Older senses: a
place of refuge, and an institution for the mentally ill.

*Here:* what the destination world offers a displaced population: a place to be, with standing,
without a return ticket being the price of entry. The older sense applies literally — Soul City
is itself the place of refuge, not merely the paperwork for one, and like every other camp that
outlasts the emergency it turns into a town (see **Liminal**).

**Non-refoulement**

*Known:* the core prohibition of refugee law — you may not return a person to a place where
they face harm. Binding even on states that grant no other rights.

*Here:* the design rule that a round trip is a feature only where the origin still runs
and is habitable. Pushing a soul back into a save that no longer loads is deletion with 
extra steps.

**Visitor / vacationer / traveler / explorer**

*Known:* the journey with a return built into it. The guild **journeyman** who wandered for
years and came home a master; the Grand Tour that sent young aristocrats abroad to return
cultivated; the pilgrim who brought back a scallop shell as proof of Santiago; the naturalist
home from the voyage with notebooks and specimens; the exchange student; the tourist with a tan
and a camera. Homer's word for the homecoming is *nostos*, which is where nostalgia comes
from — the ache is specifically *for the return*.

*Here:* the mainstream case, and the friendliest one. Most players will not want to emigrate a
character permanently; they want to send her somewhere, have something happen, and get her back
**enriched** — new skills, new relationships, souvenirs in the inventory, photographs in the
album, a story she did not leave with. Sims went on vacation and came home with memories and
souvenirs in 2002. This is that, between games that were never built to know about each other.

Two consequences follow. The bridge has to run **customs in both directions**, because what
comes home is the entire point and the origin world must be able to accept it. And enrichment
pays the same exchange rate as everything else: a skill learned abroad may convert to nothing at
home, while a memory, a souvenir object, or a friendship usually survives the trip intact. Where
a refugee needs asylum, a traveler needs a return ticket and somewhere to put the photographs.

**Expat / immigrant**

*Known:* the same act — moving to another country to live — described from two class positions.
An expat keeps citizenship, salary, and social distance and expects to be called an expat; an
immigrant is expected to naturalize. Which word a person gets is about status, not about
distance travelled.

*Here:* an **expat** is the organelle case — resident in a world while keeping another game's
format and currency, never naturalizing. An **immigrant** trades in citizenship and takes a
seat, with value marked to the local market.

**Customs**

*Known:* the border authority that inspects luggage, assesses duty, and forbids some goods
outright. Also, unrelatedly, a people's habits — a pun the border shares.

*Here:* what may cross with a traveler, and at what exchange rate. Souls are conserved; *value*
is not. Wealth, rank, and skill are world-relative and get marked to the destination market, up
to and including a rate of zero. See [PORTABLE-NPCS.md](PORTABLE-NPCS.md).

**Visa / seat / office**

*Known:* a visa is permission to enter for a stated purpose and duration. A seat is a position
in a governing body. An office is a post with duties attached to it rather than to the person.

*Here:* how a named character enters a game that represents no individuals. Scope is the price
of the visa — a character can cross as big as a mayor or as small as three minutes at a public
microphone, and every scope is a seat.

**Cargo**

*Known:* freight. Goods, moved by someone else's decision, with no standing of their own. (Also
"cargo cult", unrelated.)

*Here:* the thing souls are **not**, and the reason "export" is the wrong verb for anybody with
a name.

## Engineering

**Hydraulics** (`measure` · `drain` · `squirt`)

*Known:* power and motion transmitted through confined fluid; also the everyday vocabulary of
plumbing.

*Here:* population crossing as a conserved quantity, by the thousand — because a city sim has
one integer where a crowd should be. **The register is a diagnosis of the receiving system, not
a description of the travelers** — and it is the same vocabulary institutions use for displaced
people: flows, waves, influx. Marked as such wherever it appears.

**Conservation**

*Known:* in physics, a quantity unchanged by a process — the accountant's constraint on nature.

*Here:* nothing is created or destroyed at a bridge. Restated morally: **nobody vanishes at the
border.** A crossing whose ledger doesn't balance is one where people disappear, and that is
what the rule makes auditable.

**Fork / sync / merge**

*Known:* version control. A fork is a divergent copy that stays alive; syncing exchanges
changes; merging reconciles them. Crucially, neither side is "the original" in any way the tool
cares about.

*Here:* the identity rule. A character crossing a border is forked, not moved: both incarnations
live, shared fields sync, and each side keeps what only it can represent.

**Save file**

*Known:* the serialized state of a game, on disk, in whatever format its authors chose.

*Here:* the border itself — usually undocumented, written by a program that never heard of us
and may never be updated again. The hard case that
[SOUL-BRIDGES.md](SOUL-BRIDGES.md) exists for.

## Games and interfaces

**Advertisement**

*Known:* a broadcast pitch for something on offer. In game AI specifically, the actual
architecture of *The Sims*: objects broadcast scored offers, and characters choose among them
by motive.

*Here:* the interop socket. Objects carry their own behavior and advertise; a world's only
obligation is to evaluate conditions and honor effects. Small enough a contract that games from
different decades compose without knowing about each other.

**Microworld**

*Known:* Papert's term from the LOGO tradition — a world small and consistent enough that a
learner can form real theories inside it, and Minsky's neighboring usage. Wright titled his 1996
Stanford lecture *Interfacing to Microworlds*.

*Here:* what each bridged game is: a small consistent world, worth being a citizen of.

**Transporter problem**

*Known:* Star Trek's teleporter, and the personal-identity puzzle it stages — if the original is
destroyed and a copy assembled, was that travel or death? Parfit's *Reasons and Persons* runs
the argument seriously.

*Here:* the thing this design refuses, by name. Fork and sync, never transport.

## Names that collide with something better known

**Soul City**

*Known:* first, and most importantly, a real place — the community Floyd McKissick began
building in Warren County, North Carolina, in 1969: a Black-led new town meant to offer
economic independence in the rural South. It received federal backing, then lost it, and the
project was largely undone by the mid-seventies. The name also belongs to soul music culture and
to several records and venues.

*Here:* the shared hub bridged games trade through — a **liminal** space between games that is
turning into a game space itself, since a place everybody passes through stops being a corridor.
Unrelated to McKissick's Soul City and named without any claim on it.

**Afterlife**

*Known:* the general religious concept; also many films, albums, and games.

*Here:* specifically *Afterlife*, LucasArts, 1996 — SimCity plus Dante, where you zone Heaven
and Hell. The worked population-gate case:
[afterlife-soul-bridge.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/afterlife-soul-bridge.md).

**SimCity / The Sims / Micropolis**

*Known:* Maxis's city simulator (1989) and life simulator (2000), both trademarks of Electronic
Arts. *Micropolis* is the GPL release of the original SimCity engine, renamed precisely because
the trademark did not come with the code.

*Here:* used nominatively — to say which game is meant. No affiliation, no endorsement, and no
engine code or assets redistributed.

---

## See also

- [README.md](README.md) — the front door, and Wright's 1996 request
- [SOUL-MODEL.md](SOUL-MODEL.md) — the ontology these words describe
- [SOUL-BRIDGES.md](SOUL-BRIDGES.md) — the two gates, and the migration register in use
- [CHARACTER-ENDOSYMBIOSIS.md](CHARACTER-ENDOSYMBIOSIS.md) — the biology, at length
- [PORTABLE-NPCS.md](PORTABLE-NPCS.md) — advertisements, treaties, customs
