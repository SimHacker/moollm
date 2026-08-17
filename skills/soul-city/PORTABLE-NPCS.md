# Portable NPCs — how characters and games travel between worlds

How can NPCs — and the games they embody — travel between worlds and plug and play
together, like Sims objects sharing a house? Adventure-4's maze already runs the answer
in production: a wumpus, a grue, superbats, a bottomless pit, and an ACME vending machine
from three different source games (Hunt the Wumpus 1973, Zork 1980, Colossal Cave 1977),
coexisting in one room network without knowing about each other in advance.

This document names the protocol they're already using.

## 1. The socket: advertisements

The interop socket is the one The Sims proved at scale: **objects carry their own
behavior and advertise it**. A Sims object ships with its code and broadcasts scored
offers — *(action, score, condition, effect)* — and characters are markets that sample
those offers against their motives. The house doesn't know what a hot tub is. It doesn't
need to. It renders advertisements.

MOOLLM characters do exactly this. From Snorax's
[`GAME.yml`](../../examples/adventure-4/characters/fictional/wumpus-snorax/GAME.yml):

```yaml
advertisements:
  - action: EMANATE-SMELL
    score: 100
    condition: "always (when instance exists)"
    effect: "Adjacent rooms get 'I smell a wumpus!' warning"
  - action: DEVOUR
    score: 100
    condition: "player enters lair"
    effect: "Instant kill. Game over."
```

The world's only obligation is to evaluate conditions and honor effects. That tiny
contract is why a 1973 wumpus and a 1980 grue can share a maze written in 2026: neither
needs the other's source code, only the other's advertisements. This is the same reason
Sims expansion packs worked — new objects plugged into old houses because the socket
never changed.

## 2. The character IS the game (instanced pattern — Snorax)

Hunt the Wumpus doesn't run *on* the maze. It arrives *inside the wumpus*.
[Snorax's directory](../../examples/adventure-4/characters/fictional/wumpus-snorax/) is
a complete, self-carrying game cartridge:

| File | What travels |
|---|---|
| `CHARACTER.yml` | The soul — personality, philosophy, relationships |
| `GAME.yml` | The complete rules — Gregory Yob's 1973 mechanics plus extensions |
| `DODECAHEDRON.yml` | The canonical topology, if the host world wants it |
| `sources/wumpus1-yob.bas` | The original BASIC — provenance in the luggage |
| `hazards/` | The game decomposed into plugin parts (see §4) |
| `instances/` | Per-world state — where Snorax actually lives |

A room that wants a wumpus writes a **pointer file**
([`maze/room-e/wumpus.yml`](../../examples/adventure-4/maze/room-e/wumpus.yml)):
`prototype:` points at the character, `instance_data:` points at this world's save
state. The prototype is immutable and shared; the instance carries local memory, local
wealth, local grudges. One Snorax prototype, any number of lairs across any number of
worlds — each instance diverging like a save file.

The game even declares its **system requirements** as a port contract: any room network
with defined adjacency, at least 7 rooms, one safe starting position. That's the whole
porting guide. Meet the contract and the wumpus game runs in your world — the pub, a
generated dungeon, any `ROOM.yml` network.

Instance game state also includes the character's **territory — a chroot for
characters**. `confined_to:` is an array of directory subtrees the instance may inhabit
and navigate (world-relative, like `lair:`). One entry confines the wumpus to the maze;
multiple entries let a character hop between subtrees (the troll commutes between two
dungeons). It's a whitelist by default; add `never:` for an explicit blacklist, and
`visiting_rights:` for places reachable by invitation rather than free roam. Because
territory lives in the **instance**, not the prototype, the same character can be
maze-bound in one world and free-range in another — and because presence is checked
against the listed subtrees at move time, there is no stale flag to forget when the
territory changes: edit the array, the walls move.

Live example: [Snorax's maze instance](../../examples/adventure-4/characters/fictional/wumpus-snorax/instances/maze-room-e.yml)
— confined to `maze/`, visiting rights at the pub, never in the house.

Topology files are **embedded worlds**, and locations into them work like browser
URLs. [`DODECAHEDRON.yml`](../../examples/adventure-4/characters/fictional/wumpus-snorax/DODECAHEDRON.yml)
and the [Wumpus 2 alternates](../../examples/adventure-4/characters/fictional/wumpus-snorax/topologies/)
(Möbius strip, string of beads, hex torus, dendrite, one-way lattice) each carry a
complete navigable room network inside one YAML file — no directory scaffolding
needed. An instance points into one with a file-plus-fragment reference
(`lair: topologies/MOBIUS-STRIP.yml#room-7`), encoding position the way a browser
encodes state in the URL; a `history:` array is the back stack. Most game state
belongs in the instance file; locations are just pointers into whatever topology
the session mounted — swap the topology file and the same cartridge runs on a
Möbius strip. (Wumpus 2's cave #6, "enter your own cave," was this exact idea in
1975: the topology is a parameter, not the game.)

And embedded worlds can live **inside characters**. Interiority is not a
privilege of scale — an Iain M. Banks Culture ship is a character containing a
city, but a troll can contain rooms just as cheaply, because containment is just
directories. [Two-Toll's realms](../../examples/adventure-4/characters/fictional/troll/realms/)
mirror each mind's home corner (Zork's Troll Room, Adventure's chasm bridge) as
embedded topologies inside him: memory palaces he retreats into
(`location: realms/ADVENTURE-CHASM-BRIDGE.yml#beneath-the-bridge`), with exits
that fade into fog where his memory ends. His
[sorting stomach](../../examples/adventure-4/characters/fictional/troll/stomach/STOMACH.yml)
is the other interior: a pocket universe with a smart placement protocol that
routes what he eats into typed sub-rooms. Small characters carrying their own
maps and microworlds is the same pattern as ships carrying cities — and worlds
may mount a realm as a visitable place, so players can meet a character in its
natural habitat.

A realm is a **block quote of another game**: a procedural rhetorical excerpt —
the corner that matters, not the whole map — with the boundary fog as the
ellipsis and the `canon:` fields as the citation. Disneyland dark rides and
holodeck reenactments are the same move at other scales: navigable quotations
of a story's famous corners. See
[the troll's realms README](../../examples/adventure-4/characters/fictional/troll/realms/README.md)
for the full quotation-apparatus mapping.

## 3. Ambient games (field pattern — the grue)

The grue is the other portability archetype, and the contrast is the design lesson.
[The grue has no instances](../../examples/adventure-4/characters/fictional/grue/CHARACTER.yml):

> Snorax is ONE creature in ONE room. The grue is THE darkness in ALL dark rooms.
> There is no grue.yml file to move around. The grue simply EXISTS wherever darkness exists.

The grue travels by **predicate binding**: it attaches to any room matching
`lighting: none` and any moment matching `player.lamp.lit = false`. Install nothing;
the grue is already in your world if your world has darkness. It is a game (three-turn
countdown, warnings, teeth) implemented as a *field* rather than an *entity* — a monster
engineered backward from a mechanic, which is exactly how Dave Lebling invented it: the
answer to "why does the dark kill you?"

Three patterns, then:

- **Instanced beast** — travels by copying a pointer + growing a save file. (Wumpus, thieves, vendors.)
- **Ambient field** — travels by pattern-matching world properties. (Grue, weather, curses, economies themselves.)
- **Instanced border** — a beast whose instance binds to an *edge* in the room graph, not a node; his location IS a rule. ([Two-Toll the Troll](../../examples/adventure-4/characters/fictional/troll/) — see §6 for his luggage.)

## 4. Games decompose into plugin hazards

Snorax doesn't just carry Hunt the Wumpus whole — the game is **factored into
single-mechanic objects** that other games can adopt à la carte:
[`hazards/SUPERBATS.yml`](../../examples/adventure-4/characters/fictional/wumpus-snorax/hazards/SUPERBATS.yml)
and
[`hazards/BOTTOMLESS-PIT.yml`](../../examples/adventure-4/characters/fictional/wumpus-snorax/hazards/BOTTOMLESS-PIT.yml).
The maze instantiates them independently of the wumpus — the bats in
[room-b](../../examples/adventure-4/maze/room-b/bats.yml) (a colony of ~200 under Old
Leatherwing, "regal but cranky"), the pit in
[room-g](../../examples/adventure-4/maze/room-g/pit.yml) (The Silent Drop, "deeper than
light travels").

And cross-game composition has already been *observed in the wild*, recorded in the
bats' instance memory:

```yaml
memory:
  relocations:
    - victim: Sir Reginald
      to: room-f
      outcome: "Found treasure. Also found grue."
```

A 1973 Wumpus hazard teleported an adventurer into a 1980 Zork monster's jaws. Nobody
wrote that crossover. The plugins composed it.

## 5. Treaties: when games overlap

Plug-and-play needs conflict resolution, and the maze's answer is **explicit treaties**
written into both characters. From the grue's `parallel_play` and Snorax's
`grue_integration`, the identical clause:

> The grue won't enter the wumpus's lair (too smelly).
> The wumpus ignores the grue (can't eat what isn't there).

Different mechanics — spatial puzzle vs. time puzzle — same adventurer, and the treaty
guarantees the two death conditions never race ambiguously. Better: composition creates
**emergent tension neither game contains alone**: "Your lamp dies adjacent to the wumpus
room. Do you stumble into the wumpus, or wait for the grue?" That worst case is the
proof that interop is working — two imported games multiplying, not just coexisting.

Treaties are the diplomatic layer of the socket. When you import an NPC, you inherit
its treaties; when treaties are missing, the border crossing (§6) is where you write them.

## 6. Customs: the troll's luggage

(The troll is no longer hypothetical: he lives at
[examples/adventure-4/characters/fictional/troll/](../../examples/adventure-4/characters/fictional/troll/)
as **Two-Toll**, a third portability archetype — the *instanced border*, whose
instance binds to an edge in the room graph rather than a room. He is also
soul-city's live one-soul-two-minds example: a zork-mind that prices passage in
violence and an adventure-mind that prices it in treasure, fronting whichever
currency the destination world speaks.)

The hard problem isn't behavior — it's **economy**. A troll who has taken one treasure
per crossing for forty years walks into a starter dungeon carrying luggage that would
upset the entire local economy. Quantitative easing with legs. NPC portability without
customs is inflation.

The maze already has a native price anchor — the
[ACME Dungeon Supply Depot](../../examples/adventure-4/maze/room-j/lamp-vendor.yml)
(tribute to the battery vending machine Don Woods himself put in Colossal Cave's maze)
posts flat prices in local gold. Imported wealth must be marked to *that* market, not
to the world it came from. Rules that fall out of the prototype/instance split:

1. **Wealth lives in the instance, never the prototype.** A traveling copy of the troll
   arrives with the prototype's personality and the *empty pockets* of a fresh instance —
   unless the destination world explicitly honors an import manifest.
2. **Customs declaration at the border.** The pointer file is the visa; an optional
   `imports:` block is the declaration. The receiving world sets the exchange rate and
   the duty — including a rate of zero ("your Zork zorkmids are souvenirs here").
3. **Value is world-relative, not conserved.** There is no global gold standard; a
   hundred-trillion-dollar note is a business card in the right world. Exchange rates
   are world policy, and "division by zero" is a legal rate (gifts from the right
   giver are beyond price).
4. **Provenance rides along.** Like the bats' relocation memory, imported treasure keeps
   its history. The luggage is also the biography — which is what makes a traveling
   troll's hoard narratively valuable even when customs zeroes its purchasing power.

## 7. The lineage: construction sets all the way down

This is not a new idea — it's the oldest good idea in the medium, refined once per
generation:

- **Pinball Construction Set** (Bill Budge, 1983) — the game is a document; parts palette + physics.
- **Adventure Construction Set** (Stuart Smith, EA 1984) — whole *adventures* as data:
  regions, rooms, creatures, and things with attributes, built in an editor, saved to
  disk, traded between players. Creatures were records, not code — the first mainstream
  proof that an NPC could be a portable data object.
- **Raid on Bungeling Bay's level editor** (Will Wright, 1984) — the editor was more fun
  than the game; the realization became **SimCity**.
- **The Sims** (2000) — the construction set that *stayed open at runtime*: objects as
  self-contained behavior + advertisements, expansion packs as proof of the socket.
- **MOOLLM** — directories as the construction set. A character directory is Stuart
  Smith's creature record, grown up: soul, rules, topology, source provenance, hazard
  plugins, and instances, all legible to humans, LLMs, and machines at once.

## 8. The name is the activation

The final portability trick is the cheapest: **latent-space inheritance**. You don't
ship the grue's implementation to a new world — "grue" is a K-line that activates
everything the model already knows from Zork's forty-five years in the training data.
The `CHARACTER.yml` doesn't teach the LLM what a grue is; it *pins the canonical
parameters* (three turns, light repels, hates being SEEN) so that every world's grue is
recognizably THE grue rather than a hallucinated cousin. Prototype files are calibration,
not education.

That's why a character can cross worlds in one line — `prototype: ../wumpus-snorax/` —
and arrive whole. The directory carries what's specific; the name carries what's
universal; the instance grows what's local.

## See also

- [SOUL-MODEL.md](SOUL-MODEL.md) — souls, minds, personas; multi-person personas as
  Sims-style objects that own activities
- [Snorax](../../examples/adventure-4/characters/fictional/wumpus-snorax/) ·
  [the grue](../../examples/adventure-4/characters/fictional/grue/) ·
  [Two-Toll the Troll](../../examples/adventure-4/characters/fictional/troll/) — the three archetypes (beast, field, border), running
- [adventure-4 maze](../../examples/adventure-4/maze/) — the shared world where they interoperate
- skills/adventure, skills/character, skills/incarnation — the construction-set skills
