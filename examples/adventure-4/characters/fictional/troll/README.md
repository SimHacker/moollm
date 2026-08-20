# Two-Toll the Troll

**a.k.a. the Cross-Platform Troll.** One soul. Two minds. **Two heads.** Two of the oldest jobs in adventure gaming.

In **Colossal Cave Adventure** (Crowther & Woods, 1977) a burly troll stands by the
bridge across the fissure and insists you throw him a treasure. One per crossing.
He keeps it. Skin as tough as rhinoceros hide; afraid of exactly one bear.

In **Zork I** (Infocom, 1980) a nasty-looking troll brandishes a bloody axe in the
Troll Room and blocks all passages out. Pay in steel. When defeated he vanishes in
a cloud of sinister black fog.

This character makes the obvious joke canonical: **they were the same troll all
along**, commuting between two dungeons, context-switching protocols like anyone
with two jobs. The dual soul isn't a gimmick — it's the honest ontology of the
"gatekeeper who demands payment" archetype, which shipped twice in five years with
different currencies and has been reinstantiated in every boss door, toll bridge,
and paywall since.

And he is **literally two-headed** — one head per mind, retconned canonical on
2026-08-20, though of course he always was: both games shipped in text, you never
asked how many heads, he never volunteered. The axe-side head is zork-mind's; the
ledger-side head is adventure-mind's. **Head size displays the live fronting
weight** — front one mind and you get one great head and one raisin; blend
`{zork: 0.7, adventure: 0.3}` and the heads hold that ratio. Seasoned adventurers
read the heads the way sailors read the sky: when the bridge-toll head shrinks and
the fighting head expands, leave. Heads are addable — a new mind buds a new head,
raisin-sized until it earns weight. This is
[korz-prime's `ambiguity: blend`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime.md)
worn on the neck: dispatch weights as visible anatomy.

## The shape

```
troll/
  CHARACTER.yml        # the soul — arbitrates fronting, carries the aggregate
  minds/
    zork-mind.yml      # combat-gate organelle — currency: violence
    adventure-mind.yml # toll-gate organelle — currency: treasure
  realms/              # the soul's interiors — each mind's home turf mirrored inside him
    ZORK-TROLL-ROOM.yml       # the Troll Room corner, edges ending in black fog
    ADVENTURE-CHASM-BRIDGE.yml # the chasm crossing, edges ending in white mist
  inventory/
    axe.yml            # bloody axe — fight, throw, catch, eat
  stomach/             # pocket universe (Donnie Darko recursive)
    STOMACH.yml        # eat / recover / location:=self protocol
    contents/          # adventurers, treasures, axes, himself
  instances/           # per-world state: which edge, which mind fronts, toll ledger
```

The realms are the newest organ: **each mind's local corner of its game,
reproduced as an embedded map inside him** — not all of Zork or Colossal Cave,
just his neighborhood, dilated one move into the canonical neighbors: the
slamming trap door down through the Troll Room to the spinning Round Room; the
winding corridor across the rickety bridge to the fork where the right prong
is mist that lumbers. He can literally retreat into either of his soul's
realms (`location: realms/ADVENTURE-CHASM-BRIDGE.yml#beneath-the-bridge`);
exits beyond each excerpt end in black fog or white mist, because memory blurs
where he never went. Inside the mirror, the edge he guards becomes a room he
can stand on. See [realms/README.md](realms/README.md).

The axe is a playing piece he fights with, throws, catches, and eats
(Zork gift protocol — weapons preferred). Eaten gear lands in `stomach/`.
Setting `location` to himself enters that pocket universe; he may still
front a mind from inside. One stomach directory; nesting is narrative depth.

Each mind is an **organelle** in the [soul-city](../../../../../skills/soul-city/SOUL-MODEL.md)
sense — bound to one game's schema, holding that game's version of him in that
game's own format. Neither is flattened into the other. On arriving in a new world
he samples the local advertisements: combat verbs present, zork-mind bids to front;
treasure scoring present, adventure-mind bids. Both present, the adventurer picks
the currency. Neither present, he falls back to riddles — the species-level
protocol, older than both games.

## Why he matters

He completes the portability archetype set in this directory:

| Character | Pattern | Travels by |
|---|---|---|
| [the grue](../grue/) | ambient field | predicate-matching world properties (`lighting: none`) |
| [Snorax](../wumpus-snorax/) | instanced beast | pointer file + growing a save file |
| **Two-Toll** | **instanced border** | pointer file bound to an **edge**, not a node |

And he is the working answer to two documents:

- [SOUL-MODEL.md](../../../../../skills/soul-city/SOUL-MODEL.md) — "one mind per
  game" was described with a hypothetical Jesus Christ + Mickey Mouse two-minds
  shape ("not a playable adventure character yet"). The troll is the playable one.
- [PORTABLE-NPCS.md](../../../../../skills/soul-city/PORTABLE-NPCS.md) — §6
  ("Customs: the troll's luggage") used a hypothetical traveling troll to derive
  the wealth-lives-in-the-instance rule. He is no longer hypothetical, and yes,
  his pockets are empty at every border. He grumbles. He complies.

## WWSFF

He appears as a menagerie guest in
[WillWrightShowForFood](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/menagerie/troll)
via the overlay protocol — thin local file, canonical soul here.
