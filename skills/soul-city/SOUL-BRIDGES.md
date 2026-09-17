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
| The crossing | **The Bifrost** — Midgard ⇄ Asgard, fork-and-sync | [PSYCHOPOMP-AND-THE-BIFROST.md](../../designs/sim-obliterator/PSYCHOPOMP-AND-THE-BIFROST.md) |
| Field-level mapping for one game | Sims ⇄ soul-file field map | [BRIDGE.md](../../designs/sim-obliterator/BRIDGE.md) |
| Monotonic-up, round-trippable-down | L0–L3 resource layers | [IFF-LAYERS.md](../../designs/sim-obliterator/IFF-LAYERS.md) |
| A soul waking up on the far side | **The Uplift** | [THE-UPLIFT.md](../../designs/sim-obliterator/THE-UPLIFT.md) |
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
