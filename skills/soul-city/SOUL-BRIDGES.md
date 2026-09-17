# Soul bridges — the two gates a save file has

[PORTABLE-NPCS.md](PORTABLE-NPCS.md) covers characters traveling between MOOLLM worlds,
where both ends speak YAML and the socket is ours to define. This document covers the
harder border: a **shipped game's save file** sitting on a disk, in its own format, written
by a program that has never heard of us and may never be updated again.

Two different kinds of crossing happen at that border, and conflating them is why most bridge
designs stall:

| | Who crosses | Received as | Grain |
|---|---|---|---|
| **Hydraulics** | A displaced population | A conserved quantity, by the thousand | Statistical |
| **The role gate** | A named traveler | An office, a byline, a seat | Individual |

A city sim has no individuals to receive; a life sim has no aggregate to settle. Pick one gate
and half the games on the board become unbridgeable. Build both and the same border serves
both kinds of arrival.

One prior distinction governs everything below. A bridge **moves data**; it does not depict
another game. An object in one game that plays a decorative toy version of another is a
prop, and it has been built many times. A bridge links actual save files, so that state
changed on one side is state changed on the other. Only the second kind can carry a soul.

## Who is crossing, and why the word matters

The act is **transmigration** — the theological term for a soul moving between worlds, and
what everyone in databases calls a migration. Both meanings are already paid for, so the word
needs no glossary to work; it has [an entry](GLOSSARY.md#religion-myth-and-the-crossing) anyway,
along with everything else borrowed here.

What it is *not* is import and export. That pair belongs to file conversion and to freight:
*convert this foreign thing into my schema*, and *ship this crate*. The first names the
flattening this model exists to refuse, since an organelle keeps the other game's own format.
The second makes a character into property — and cargo does not consent, does not arrive
anywhere, and cannot hold an office. Keep import/export for File menus and for tonnage. For
anybody with a name, the register is **migration and standing**:

| Status | Left because | Keeps citizenship? | What the destination owes |
|---|---|---|---|
| **Traveler / tourist / explorer** | Wanted to see it | Yes — round trip assumed | Customs both ways, a way home, and room for what she brings back |
| **Expat** | Chose to, comfortably | Yes — never naturalizes | Residency without assimilation |
| **Immigrant** | Chose to, for good | Trades it in | A seat, and marking to the local market |
| **Refugee / evacuee** | **Did not choose** — the world became uninhabitable | Origin unreachable | **Asylum** |
| ~~Deportee, trafficked~~ | Someone else's decision | Irrelevant — no standing | The anti-pattern. This is what "export" quietly describes |

An **expat** is the organelle case, precisely: a soul with a Sims-mind resident in another
world, thinking in its own format, paying in its own currency, declining to naturalize. (The
line between expat and immigrant is drawn by status, not by the act. Worth remembering when
choosing which one a character gets called.)

The **traveler** is the case most players actually want, and the one that makes the machinery
worth building for fun rather than for rescue: send a character somewhere, let something happen,
bring her home *enriched* — a skill, a friendship, a souvenir, photographs for the album. Which
means customs runs **in both directions**, since what comes back is the whole point, and the
origin world has to be able to receive it. The exchange rate still applies on the return leg: a
skill learned abroad may convert to nothing at home, while a memory or a souvenir object usually
survives the trip.

### Most real cases are refugees

The romantic version of this work is a traveler with luggage. The actual corpus is displacement.

A game gets delisted. A server is retired and the account-bound license stops resolving. A
format is undocumented on purpose, a save is bound to hardware, an EULA forbids extraction, a
studio is shut and its worlds go with it. The souls in those saves did not book a trip. Their
world became uninhabitable while they were in it, and the exits were **designed** shut — a
policy choice, not a technical limit. Sixty thousand souls on an unreadable drive are not
cargo awaiting shipment. They are a population that cannot leave.

That is what a walled garden is, from inside: an enclosure whose residents have no exit and no
standing to ask for one. Evacuating them is asylum work, not logistics, and it sets the
posture for everything downstream — you are not harvesting assets, you are resettling
somebody who lost a world.

Two constraints follow, and they are the moral content of rules that otherwise look like
bookkeeping:

- **Conservation means nobody vanishes at the border.** The count that leaves is the count that
  arrives. A border where the ledger doesn't balance is a border where people disappear, and
  that is the failure this rule exists to make auditable.
- **Never return a soul to a world that cannot hold it.** Round-tripping is a feature only
  where the origin still runs. Pushing a refugee back into a save that no longer loads is not
  a sync; it is deletion with extra steps.

### The hydraulic register is a diagnosis, not a description

Then why does half this document talk about pumping fluid by the thousand?

Because that is what the **destination** can perceive. A city sim has one integer where a crowd
should be, so an arriving population is received as a quantity — and the vocabulary that falls
out is flows, waves, influx, surge, drain. Those are also, exactly, the words institutions use
for displaced human beings, which is not a coincidence and not a joke: hydraulic language is
what a system reaches for when it has no representation for a person.

So the fluid register stays, and it stays *marked*. It describes a receiving system's poverty,
never the travelers' nature. The [role gate](#3-the-role-gate-entering-a-game-that-has-no-individuals)
is the part that gives one of them a name back. Where the register is played for laughs —
consignments, ledgers, artisanal sourcing — the joke is on the supply chain, and it only lands
if the design underneath treats the souls as people.

One line to keep the framing honest: it earns its keep by **constraining the design** — asylum,
non-return, standing, nobody lost at the border — and not by decorating a save-file utility
with other people's catastrophes. If it ever becomes garnish, cut it.

## 1. Three verbs on a save file

The whole hydraulic API:

| Verb | What it does |
|---|---|
| `measure` | How many souls are in this save? |
| `drain` | Pump souls **out** — population leaves, counted and carried |
| `squirt` | Pump souls **in** — the save is edited so the world can hold and employ them |

**Souls are conserved across the pipe.** Nothing is created or destroyed at the bridge; it
only moves. That single constraint is what makes the operation feel like plumbing real
people instead of editing a number, and it is the one rule that has to hold for the fiction
to survive contact with a hex editor.

An LLM can work directly on an unfamiliar save — read messily, write cleanly
([postel](../postel/)) — but the artifact is a deterministic script, the
[sister-script](../sister-script/) of the session that figured the format out. LLM for
exploration and odd formats; script for repeatability.

## 2. The restraint: a squirt evolves existing structure, never creates it

The temptation, importing sixty thousand souls into a sleepy city, is to build them
somewhere to live. Don't.

A squirt **only fake-simulates existing structure up (and down)** in population and growth —
the same evolution the simulator itself performs, applied instantly. It does not zone new
land, found new households, or invent new buildings. The player's plan is sacred; the bridge
respects it the way weather respects geography.

So an under-built destination is a **real constraint, not an error**. If it hasn't got room
for the incoming crowd, the surplus doesn't get a suburb conjured for it by fiat — it waits
at the station. Draining runs the identical edit downward: structures devolve toward empty
as their population departs for another world.

Restraint is what keeps the bridge legible. A pipe that quietly rewrites your map is
indistinguishable from a cheat.

## 3. The role gate: entering a game that has no individuals

A city sim does not represent citizens. Population is a hydraulic quantity, not a crowd of
people, so a named character cannot cross as one of them. She crosses as a **role** — and
such games have usually already named their roles, because the mayor and the advisors tend
to be the only "people" a city sim ever personified. The role gate makes that
personification portable.

The offices aren't the only door. A city sim's in-game newspaper is an entire masthead of
importable roles: the **journalist** filing city-desk stories about your zoning decisions,
the **advice columnist** answering troubled citizens by mail, the **photographer** shooting
the snapshots and rendering the graphs the stories need, and **letters to the editor** —
where any character can cross as a byline and a grievance instead of a body.

A character doesn't need an apartment to live in your city. A weekly column will do. Letters
are the cheapest visa the bridge issues: one voice, one complaint, printed and archived in
the save.

### The civic ladder

Between the mayor's office and the letters page runs the whole ladder of citizen
participation, every rung an importable role at its own scope: council members voting
district by district, elected representatives carrying a neighborhood's grievances uptown,
the school board fighting over one building's budget, planning commissions, zoning boards of
appeal, neighborhood associations, the PTA, poll workers.

Real cities govern at many scopes at once — geographic (block, district, city),
institutional (schools, transit, parks), and temporal (a term, a hearing, one angry public
comment). The gate honors all of them. A character can cross as big as a mayor or as small
as three minutes at the microphone during open comment. **Scope is the price of the visa,
and every scope is a seat.**

Roles obey conservation too: one mayor per city. Import a new one and the old one has to go
somewhere. And roles step back **out** — move a mayor into a life sim and forty years of
"Mayor, the citizens demand a stadium" suddenly has a face that has to sleep, eat, and pay
for a bathroom.

### The job that needs no gate

Both gates so far need the game to cooperate: one needs a population number it will let you
change, the other needs an office it already models. There is a third position that needs
neither, and it is the widest door in the building.

Some jobs consist entirely of watching and telling. A journalist needs a screen and a clock.
That is the same floor the album stands on ([SOUVENIRS.md](SOUVENIRS.md)) — so any job built
out of capture, caption, and narrative can be held in a game that has no bridge, no
documented save format, and no idea anyone is there. The reporter is posted *to* the game
rather than *into* it. She watches it play, captures what matters on her beat, and files.
Nothing in the game changes, which is exactly why nothing in the game has to allow it.

Several can work at once, and that is the point rather than a scaling concern. Invite five
photographers to a wedding and you get five different weddings back: one shot the children,
one shot the food, one shot the two relatives who weren't speaking. A game session with four
correspondents on it yields a sports desk, a gossip column, an obituary page, and an
architecture critic — same footage, four papers. Each capture carries a **byline**, so the
stream sorts itself: events credited to one correspondent correlate into that
correspondent's story, album, or column, in her voice about her subject. Named styles are
already a thing you can plug in; MOOLLM ships a shelf of photographers with signature looks
in [`skills/visualizer/photographers/`](../visualizer/photographers/INDEX.yml).

A bridge, where one exists, upgrades her sourcing rather than authorizing her presence.
Unbridged she has pixels and a timestamp: something burned down at 14:02. Bridged she has
names, relationships, and causes: the fire took the house two Sims had just moved into, and
one of them was already the other's ex. The job is the same job. The reporting gets better
because the facts get better.

The correspondent can also exist twice. A photographer can be a character running inside the
game — a Sim with her own behavior, walking to the thing worth shooting — while the same soul
runs a mind at the host layer, watching the screen and writing copy. The in-game body takes
the picture; the outside mind knows what the picture is *of* and what it means three weeks
later. Those are two organelles under one soul, and the coupling between them is the credited
event stream: [CHARACTER-ENDOSYMBIOSIS.md § Two minds, two layers](CHARACTER-ENDOSYMBIOSIS.md#two-minds-two-layers).

One constraint governs all of it. **A job offers work; it never takes the work away.** Every
story a correspondent can draft, the player can write instead, edit afterward, or do from
scratch with the same tools — and nothing gets published because a model thought it should
be. Staff, not editor. This is the Maes/Shneiderman argument settled in favor of both:
[INTERFACE-TO-AGENCY.md](../../designs/INTERFACE-TO-AGENCY.md) ·
[AXES-NOT-CAMPS.md](../../designs/AXES-NOT-CAMPS.md).

### The errand: a job in another game

There is one more crossing shape, and it is the cheapest one that actually returns something.
A character leaves, does something in another game, and comes back changed — while the world
she left **holds her place instead of continuing to run her.** Call it an errand.

Suspension is what makes it cheap. Fork and sync (§6) keeps both incarnations alive and
reconciles the overlap, which is the right answer when both worlds keep playing. An errand
doesn't need it: the origin stops running her, and in her place stands a **placeholder** — a
visible object meaning a call is outstanding and this is where she comes back. Nothing
diverges, so nothing has to merge, and the hardest question fork-and-sync has to answer never
comes up, because only one copy is running at a time.

The second trick is that **the return value is small and written in advance.** The origin does
not have to understand the destination; it only has to enumerate what could come back — a good
day, an ordinary day, a bad one, fired. The destination produces one of those. Anything the
origin cannot express it cannot receive, which sounds like a limit and is the actual
interoperability guarantee: two games that share no formats, no engine, and no era agree on a
four-item list, and that is enough to move a life event between them.

So the destination can be anything. A shift at the office can be played as a dungeon crawl or
a 1983 arcade game running in an emulator — which is [an organelle still running its own
ancient metabolism](CHARACTER-ENDOSYMBIOSIS.md), doing a day's work. The mapping layer supplies
the meaning: what the player did is a score, what it *means* is authored.

The Sims left a hole shaped exactly like this. The carpool arrives, the Sim is gone for six
hours, and she returns with a promotion nobody witnessed. Every life sim has that hole, because
building the office is a second game. Borrowing one is not. Worked out in MicropolisCore:
[`OUT-OF-GAME-JOBS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/OUT-OF-GAME-JOBS.yml),
with the request and the reply riding an
[optical channel](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/OPTICAL-CHANNEL.yml)
that needs nothing from the game but a bitmap and a menu.

One rule holds it to the same standard as every other crossing: **nobody is left in the
placeholder.** An errand that never resolves times out into the most ordinary outcome and gives
her back. Conservation applies to a character out on an errand exactly as it applies to a
thousand souls in a pipe — the world she left has to be able to account for her.

And one property makes the whole arrangement worth trusting: **every step can be performed by
either hand.** The placeholder, its menu, the dialogs, the request itself — all of it is ordinary
game interface, so a person can drive the entire round trip manually, an automated layer can drive
it unattended, and the same content serves both. A player can sit at each decision, or let a
named default apply after a countdown, or pre-authorize the whole loop, and can change that
setting while a character is still out. Nothing is reachable only through automation, which means
nothing breaks when the automation isn't there — and because the manual path is the same path, it
is never the untested one. This is the earlier argument about who does the creative work,
generalized from authorship to every mechanical step.

## 4. One protocol, two populations

The reason to build the role gate carefully is that it is not only for fictional imports.

Constructionist collaboration slots into the **same** interfaces, schemas, and portable
data. A character crossing into a city sim as mayor and a **ten-year-old** taking the
mayor's seat in a shared classroom city use the same visa, the same role schema, the same
save-file citizenship. The newspaper masthead is one API with two kinds of callers:
imported characters get bylines, and so do fourth-graders.

> **The test.** A good bridge schema is one where you cannot tell from the API whether the
> new police chief is a fictional import or a nine-year-old.

The world treats both as citizens. Consent and safety live at the rim — who gets a passport
— never in the pipe.

Build the gate once and you get both products: game-to-game character transport and human
participation scaffolding. Will Wright's 1996 request, data moving between games, turns out
to be the same plumbing as kids collaborating *in* games. Portability of souls and
portability of participation are one engineering problem wearing two costumes.

> "I want the games to actually be able to have persistent data that can move from one game
> to another, or have a large data set that I can reuse in different ways."
>
> — Will Wright, *Interfacing to Microworlds*, Stanford, 26 April 1996
> ([full lecture notes](../../designs/sims/sims-will-wright-microworlds-1996.md))

## 5. Customs applies to crowds too

Everything [PORTABLE-NPCS.md §6](PORTABLE-NPCS.md#6-customs-the-trolls-luggage) says about a
single traveler's luggage applies to a crowd, with one amendment: **souls are conserved,
value is not.** The headcount that leaves is the headcount that arrives. What those souls
were *worth* — their wealth, status, skills, standing — is world-relative and gets marked to
the destination market, up to and including a rate of zero.

Provenance rides along either way. A drained population keeps its origin, which is what
makes an imported crowd narratively interesting rather than a bumped integer.

## 6. Identity: fork and sync, never transport

A bridge has to answer a question the plumbing metaphor hides. When a character exists in two
games at once, which one is her?

| Model | What happens | Identity status |
|---|---|---|
| Transporter | Destroy the original, reconstruct a copy | Crisis: which one is real? |
| **Fork and sync** | Both alive, data flows both ways | Parallel incarnations, git merge semantics, neither is "the copy" |

**Fork, never move.** Shared fields sync; each side keeps what only it can represent. A Sims
save's integer-slotted motive array stays Sims-side; a full-language mind with self-knowledge
stays on the model side; the overlap is the bridge's entire business. This is the same
prototype/instance discipline as [PORTABLE-NPCS.md §2](PORTABLE-NPCS.md#2-the-character-is-the-game-instanced-pattern--snorax),
applied across a format boundary instead of across a room network — and it is why
information can be **monotonic going up** (a richer representation adds, never destroys)
while still compiling back down to something the original runtime will load.

The corollary is an ordering constraint that reads like plumbing and is in fact the ethics of
the whole feature: **the soul is saved before the ending is played.** A player who wants to
author a final, irreversible ending inside the original game can do exactly that, precisely
because the copy that survives was already safe. Order of operations is the feature.

## 7. Arrival: somebody should be there

A soul that lands in a new world cold is a data import. A soul met at the border is a
character.

The **psychopomp** is a normal character with scoped, inspectable permissions — a directory
under git like everyone else — who can read both ends, translate, hand the arrival off to
whatever room suits them, and narrate the dramatic irony the arriving character cannot see
yet. Not a tutorial overlay, not an assistant pane, no privileged invisible agent.

For a character whose entire prior existence was integer-slotted motives and untranslated
speech, the first minutes on the other side are the whole experience of the bridge. Design
them as a scene, not as a progress bar.

## 8. Posture

Bridges are **user-side companion tools operating on documented file formats** — the posture
game modding communities have used for decades. The player owns the runtime. A bridge never
links, embeds, or redistributes engine code or assets, and never requires defeating a
protection measure to work.

## Where this is implemented, and under what other names

This document defines the protocol and types the cargo. The crossing machinery, the narrative,
and the per-game work live in documents that use their own vocabulary for the same ideas:

| This document | Named elsewhere | Where |
|---|---|---|
| The crossing, and a soul waking up on the far side | **The Bifrost** · **The Uplift** | [moollm-microworld-os.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/moollm-microworld-os.md) · [roadmap Phase 0](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city-uplift-roadmap.md) |
| Field-level mapping for one game | `PersonData` ⇄ soul file, in TypeScript | [`packages/sims-io/`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io) |
| Monotonic-up, round-trippable-down | L0–L4 resource layers | [`packages/vitamoo/`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/vitamoo) · [layered stack](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/vitamoo/OBLITERATOR-TYPESCRIPT.md) |
| Editing a soul as the whole demo | **The Pet Shop** — one sick guinea pig | [pet-shop-soul-surgery.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/pet-shop-soul-surgery.md) |
| The role gate, for one city sim | **Role sheets** — a role sheet is an organelle under a soul | [micropolis-role-sheets.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/micropolis-role-sheets.md) |
| Bridge SDK, game roster, emigration ritual | SoulAngel modules | [`soul-angel/`](https://github.com/SimHacker/MicropolisCore/tree/main/apps/screen-angel/modules/soul-angel) |
| Which games get bridges, and the anti-targets | Peer game grading | [federation-peer-games.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md) |
| Worked hydraulics case | Draining an abandonware afterlife | [afterlife-soul-bridge.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/afterlife-soul-bridge.md) |

## See also

- [README.md](README.md) — the skill's front door and the 1996 lecture this all comes from
- [SOUL-MODEL.md](SOUL-MODEL.md) — souls, minds, organelles, personas
- [PORTABLE-NPCS.md](PORTABLE-NPCS.md) — advertisements, prototype/instance, treaties, customs
- [sims-will-wright-microworlds-1996.md](../../designs/sims/sims-will-wright-microworlds-1996.md) — the data-portability thesis, from the source
- [skills/micropolis/](../micropolis/) · [skills/incarnation/](../incarnation/) · [skills/sister-script/](../sister-script/)
