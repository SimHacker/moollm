# Soul Model

Public interface to **Soul City** — continuity body on a walkable map; mindless, single-minded, and multi-minded architectures included.

| | |
|--|--|
| This file | Ontology + worked examples + outbound links |
| Twin | [`SOUL-MODEL.yml`](SOUL-MODEL.yml) |
| Bootstrap world | this adventure — [`examples/adventure-4/`](.) |
| Soul Plaza | [`street/lane-neverending/e2/soul-plaza/`](street/lane-neverending/e2/soul-plaza/) |
| Skills | [`soul`](../../skills/soul/) · [`mind`](../../skills/mind/) · [`character`](../../skills/character/) · [`robot`](../../skills/robot/) · [`adventure`](../../skills/adventure/) · [`memory-palace`](../../skills/memory-palace/) |
| Platform catalog | [Soul City (WWSFF)](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) |

A **soul** has one map location, a shared inventory, and zero or more **minds**. Minds share that location. Directory = room; walking the filesystem is the interface.

| Cardinality | Shape |
|-------------|--------|
| 0 | **Mindless soul** — walks, carries, persists; no resident agency |
| 1 | **Single-minded soul** |
| N | **Multi-minded soul** |

Worked cases: **ZombieSims** replaces human/other minds with a zombie mind · **robots** have souls (mindless or minded) · **remote-control** robots use a remote-control mind stub.

---

## Constellation (intertwingle)

| Layer | Skills |
|-------|--------|
| Entity | [`character`](../../skills/character/) |
| Container | [`soul`](../../skills/soul/) — foundational for soul-chat, Soul City, incarnation |
| Agency | [`mind`](../../skills/mind/) — foundational for society-of-mind, mind-mirror |
| Dynamics | [`society-of-mind`](../../skills/society-of-mind/) · [`soul-chat`](../../skills/soul-chat/) |
| Organelle | [`mind-mirror`](../../skills/mind-mirror/) · game schemas |
| City | this adventure · [Soul Plaza](street/lane-neverending/e2/soul-plaza/) · [platform catalog](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) |
| Map | [`adventure`](../../skills/adventure/) · [`memory-palace`](../../skills/memory-palace/) · [HN loci](https://news.ycombinator.com/item?id=29330901) |
| Ethics | [`soul/ETHICS.md`](../../skills/soul/ETHICS.md) (container + stack hub) · [`mind/ETHICS.md`](../../skills/mind/ETHICS.md) · [`character/ETHICS.md`](../../skills/character/ETHICS.md) · [`representation-ethics`](../../skills/representation-ethics/) · [`incarnation`](../../skills/incarnation/) |

You cannot define society-of-mind or mind-mirror without **mind**. You cannot define soul-chat or Soul City without **soul**.

---

## Stance (what kind of claim this is)

**Organizational / Self object-model position** — not a metaphysical claim that souls exist.

| We claim | We do not claim |
|----------|-----------------|
| **Soul** is a useful **container** for organizing agencies: location, inventory, history, `minds[]` | That a soul is ontologically or theologically “real” |
| **Multiple minds** are first-class — competing, counseling, co-located agencies (Society of Mind grain) | That every being has exactly one indivisible mind |
| Soul may hold **zero or more** minds | That minds require a soul, or that nesting is forbidden |

Default arrangement: **soul contains minds**. Also valid under Self: minds containing **sub-minds**, **sub-souls**, or any intervening nested containers (rooms, parties, organelles, directories). Prototype inheritance makes arbitrary nesting natural — this file’s default is a useful grain, not a ceiling.

---

## Adventure as method of loci

Programming and organizing information as a map of rooms, exits, objects, and inventory — the same spatial index as the classical [method of loci](https://en.wikipedia.org/wiki/Method_of_loci).

| Source | Link |
|--------|------|
| Don ↔ Scott Adams (Adventureland) on HN | [comment 29330901](https://news.ycombinator.com/item?id=29330901) · [thread](https://news.ycombinator.com/item?id=29330120) |
| Adventure skill (lineage + pie menus as room exits) | [`skills/adventure/`](../../skills/adventure/) |
| Memory palace skill | [`skills/memory-palace/`](../../skills/memory-palace/) |

---

## Vocabulary

| Term | Definition |
|------|------------|
| **Soul** | Continuity body: location + inventory + minds + history |
| **Mind** | Resident agency inside (or beside) a soul |
| **Organelle** | Mind bound to a game/ecosystem schema (own data shape; import/export/sync) |
| **Bridge** | Declared channel — mind↔mind, mind↔soul, or soul↔game |
| **Well** | Latent-space archetype — name activates a shared prototype already in training |
| **Cup** | Personal mind that inherits a well and carries local delta |

---

## Two inheritance modes

### Pure well

```yaml
parents:
  - "biblical Jesus"
```

Any named archetype works the same way (Buddha, Mary, shoulder angel, shoulder devil, …).

[Latent-Space Inheritance](../../designs/object-system/LATENT-SPACE-INHERITANCE.md)

### Personal cup

```yaml
parents:
  - "biblical Jesus"   # the well
  # optional: file archetype + local overrides
```

In-repo file archetype: [representatives INDEX](../../skills/no-ai-soul/representatives/INDEX.yml) · [savior facet](../../skills/no-ai-soul/facets/savior.yml)

[Self and MOOLLM](../../designs/object-system/SELF-AND-MOOLLM.md) · [prototype skill](../../skills/prototype/)

---

## Differently architected examples

Same Python import shape; different dimensions bound.

`from <well> import <dimension.aspect> as <local>` — latent well, aspect pulled, local name. Spec syntax; not a runnable program.

| Character | Architecture | Dimension imported | Memorial |
|-----------|--------------|--------------------|----------|
| **Jesus Mouse** | Blended soul — multiple parents, one body | costume · soul · props · mission · praxis | [characters/jesus-mouse](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/jesus-mouse) |
| **Duckmouse** (Donald Michie) | Name-sounds only | pronunciation | [characters/donald-michie](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-michie) |

### Jesus Mouse — lived inventory

Haight Street (Don’s memoir). Stated intention: Jesus and Mickey Mouse as America’s two biggest shared archetypes, embodied as one combination. Wizard props (scepter, sequined spell book) in the same inventory.

```python
# from <well> import <dimension.aspect> as <local>
from jesus_christ import soul.jesus as jesus
from jesus_christ import hair.long as hair, beard.long as beard
from jesus_christ import mission.liquidate_treasures_for_the_poor as mission
from mickey_mouse import soul.mickey as mouse, costume.hat as hat, costume.long_tail as tail
from the_wizard import props.walking_stick as scepter, props.spell_book.sequined as spell_book

class JesusMouse(Jesus, MickeyMouse, Wizard):
    look = hair | beard | hat | tail | scepter | spell_book
    body = 1
```

- Full inventory: [latent-imports.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/jesus-mouse/sources/latent-imports.md)
- Memoir: [hn-34398396.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/jesus-mouse/sources/hn-34398396.md)
- HN: [item?id=34398396](https://news.ycombinator.com/item?id=34398396)

```yaml
parents:
  - "Jesus"
  - "Mickey Mouse"
  - "Wizard"
```

### Duckmouse — pronunciation only

Donald Michie — nickname **Duckmouse** (Telegraph; British Library). Same Mickey Mouse well; pronunciation axis only.

```python
# from <well> import <dimension.aspect> as <local>
from donald_duck import pronunciation.donald as donald
from mickey_mouse import pronunciation.mmickey as michie

given_name = donald   # DON-ald
surname = michie      # MICK-ee
nickname = "Duckmouse"
```

- Memorial: [donald-michie](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-michie)
- Record: [duckmouse-pronunciation-on-the-record.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/donald-michie/sources/duckmouse-pronunciation-on-the-record.md)

### Alternate Self graph

One soul, two minds (not what Jesus Mouse lived):

```yaml
soul:
  minds:
    jesus-mind:
      parents: ["Jesus"]
    mouse-mind:
      parents: ["Mickey Mouse"]
```

Also modeled: personal cups of *Jesus Mouse* · latent `"Jesus Mouse"` · blend plus shoulders · game organelles. Memorials and design receipts; not playable adventure characters yet.

---

## Shoulders — angel and devil

Multiple minds, one location:

| Shoulder | Pure well (examples) | Personal cup |
|----------|----------------------|--------------|
| Angel | `"shoulder angel"`, `"cartoon conscience angel"` | `minds/my-angel/` |
| Devil | `"shoulder devil"`, `"cartoon temptation devil"` | `minds/my-devil/` |

May argue over a **bridge**. Soul is player-in-the-middle. Either side can mute.

[society-of-mind](../../skills/society-of-mind/)

---

## Map (adventure-4)

| Place | What it is |
|-------|------------|
| [Soul Plaza](street/lane-neverending/e2/soul-plaza/) | Shops as city-side organelles — create / publish / share on Lane Neverending |
| [adventure-4 README](README.md) | World layout (pub, coatroom, street, maze…) |
| [ADVENTURE.yml](ADVENTURE.yml) | Live simulation state |
| Nested minds seed | [don-hopkins/](characters/real-people/don-hopkins/) — `dents/` + `slats/` under a host |

Directory = room. Character directory = soul or mind. YAML comments are data.

This adventure is the Soul City pool until a separately named Soul City adventure launches.

---

## Cross-game characters (endosymbiosis)

Each game is an organelle with its own schema; sync without flattening.

- [CHARACTER-ENDOSYMBIOSIS.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/CHARACTER-ENDOSYMBIOSIS.md)
- [Soul City catalog](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city)

Same object system holds inner minds, albums, and bridges.

---

## Minsky / Society of Mind

| SoM term | Here |
|----------|------|
| Agents / agencies | minds (and skill-agents elsewhere in MOOLLM) |
| K-lines | names that activate latent prototypes or file paths |
| B-brain | a mind that watches the society |
| Censors / suppressors | shoulder mute, bridge attenuation, player-in-the-middle veto |
| Made-up minds | blank cups that grow |

[society-of-mind skill](../../skills/society-of-mind/README.md) · [GLANCE](../../skills/society-of-mind/GLANCE.yml) · [LIVE-OBJECTS examples](../../designs/object-system/LIVE-OBJECTS-EXAMPLES.md)

---

## Play

1. Soul: `CHARACTER.yml` or template [player](characters/abstract/player/).
2. Rooms; inventory on the soul.
3. Mind = cup (subdirectory or co-located join).
4. Forks: shoulders may speak.
5. Game schema on a mind: **Import How…**, bridges, player-in-the-middle.

---

## Links

| Topic | Link |
|------|------|
| Soul skill | [skills/soul/](../../skills/soul/) |
| Mind skill | [skills/mind/](../../skills/mind/) |
| Character skill | [skills/character/](../../skills/character/) |
| Adventure (loci lineage) | [skills/adventure/](../../skills/adventure/) |
| Memory palace | [skills/memory-palace/](../../skills/memory-palace/) |
| HN — Adventure ↔ method of loci (Scott Adams) | [29330901](https://news.ycombinator.com/item?id=29330901) |
| Object system | [designs/object-system/README.md](../../designs/object-system/README.md) |
| Latent parents | [LATENT-SPACE-INHERITANCE.md](../../designs/object-system/LATENT-SPACE-INHERITANCE.md) |
| Party | [skills/party/](../../skills/party/) |
| Inventory | [skills/inventory/](../../skills/inventory/) |
| Adventure | [skills/adventure/](../../skills/adventure/) |
| Society of Mind | [skills/society-of-mind/](../../skills/society-of-mind/) |
| no-ai-soul (different skill) | [skills/no-ai-soul/](../../skills/no-ai-soul/) |
| Micropolis | [skills/micropolis/GLANCE.yml](../../skills/micropolis/GLANCE.yml) |
| Endosymbiosis essay | [CHARACTER-ENDOSYMBIOSIS.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/CHARACTER-ENDOSYMBIOSIS.md) |
| Soul City catalog | [https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) |
| Machine twin | [SOUL-MODEL.yml](SOUL-MODEL.yml) |
| Jesus Mouse | [https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/jesus-mouse](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/jesus-mouse) |
| Jesus Mouse latent imports | [latent-imports.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/jesus-mouse/sources/latent-imports.md) |
| Jesus Mouse HN | [item?id=34398396](https://news.ycombinator.com/item?id=34398396) |
| Duckmouse | [https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-michie](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-michie) |
| Duckmouse record | [duckmouse-pronunciation-on-the-record.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/donald-michie/sources/duckmouse-pronunciation-on-the-record.md) |
