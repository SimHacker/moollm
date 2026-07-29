# Soul Model

A **soul** is the thing that walks around with your stuff — one body, one backpack, zero or more minds arguing in your head.

**Soul City** is a place those souls can walk: rooms, shops, tools, roads, parties. Games keep their own rules; souls can still know people across games.

---

## Soul

One location. Shared inventory. **Zero or more minds.**


| Minds | Shape                                               |
| ----- | --------------------------------------------------- |
| 0     | Mindless — walks, carries, persists                 |
| 1     | Single-minded                                       |
| N     | Multi-minded (angel/devil shoulders, committees, …) |


Robots can have souls. Zombies swap in a zombie mind. Remote-control is a mind stub. You author the architecture — mindless, single, or multi.

Souls can know characters, personas, and minds that live in *other* games. Free form.

Characters can **wear personas** — that’s where you describe look / costume / role ([persona](../persona/)). adventure-4 doesn’t force costumes into a special object type. Want a hat you can equip, trade, or drop? Make an **object** — a file or directory — and put it in inventory. Same for anything wearable or tradable ([object](../object/) · [inventory](../inventory/)).

---



## Soul City

The city: rooms, roads, plazas, shops, tools, objects, vehicles, parties — and souls hanging out in it.

Many cities. Bootstrap map: [adventure-4](../../examples/adventure-4/) · [Soul Plaza](../../examples/adventure-4/street/lane-neverending/e2/soul-plaza/) (create / publish / share shops).

---



## Examples

A **soul** can borrow *pieces* of famous characters, like Mickey Mouse, Donald Duck, Gandalf the Wizard — the hat, the mission, how a name sounds — and leave the rest. Different souls can borrow different pieces of multiple real and fictional people, animals, or abstract concepts like love itself.


| Who                           | Combination                                      | What was borrowed                                              | More                                                                                              |
| ----------------------------- | ------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Jesus Mouse**               | **Jesus Christ + Mickey Mouse** (+ Wizard props) | One soul, one body — look, mission, mouse costume, wizard gear | [memorial](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/jesus-mouse)   |
| **Duckmouse** (Donald Michie) | **Donald Duck + Mickey Mouse**                   | Name *sounds* only — nothing else from the cartoons            | [memorial](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-michie) |


Each list below is a recipe, not a program you run. Read a line as: from *this famous figure*, take *this one trait*, call it *this*.

### Jesus Mouse — Jesus Christ + Mickey Mouse soul

From a Haight Street street-performance memoir: **Jesus Christ + Mickey Mouse** as one person (America’s two biggest shared characters) — plus Wizard props (scepter, sequined spell book) in the same backpack.

In plain words:

- from Jesus → soul, long hair, long beard, mission (sell treasures for the poor)
- from Mickey → mouse soul, hat, long tail
- from Wizard → walking stick as scepter, sequined spell book
- one body; all of that is the look

```
from jesus_christ take soul → jesus
from jesus_christ take long hair, long beard
from jesus_christ take mission (liquidate treasures for the poor)
from mickey_mouse take mouse soul, hat, long tail
from the_wizard take walking stick → scepter, sequined spell book → spell_book

JesusMouse is Jesus + MickeyMouse + Wizard
look = hair + beard + hat + tail + scepter + spell_book
body = 1
```

Parents in short form:

```
parents: Jesus, Mickey Mouse, Wizard
```

- Full inventory: [latent-imports.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/jesus-mouse/sources/latent-imports.md)
- Memoir: [hn-34398396.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/jesus-mouse/sources/hn-34398396.md)
- HN: [item?id=34398396](https://news.ycombinator.com/item?id=34398396)



### Duckmouse — Donald Duck + Mickey Mouse sounds

Donald Michie — nickname **Duckmouse** (Telegraph; British Library). Combination: **Donald Duck + Mickey Mouse**, but only the *sounds* of the names:

- “Donald” like Donald Duck → DON-ald
- “Michie” like Mickey Mouse → MICK-ee
- nickname: Duckmouse

Nothing else from Donald Duck or Mickey Mouse — not the costume, not the soul, not the mission.

```
from donald_duck take how "Donald" sounds → given name
from mickey_mouse take how "Mickey" sounds → surname
nickname = Duckmouse
```

- Memorial: [donald-michie](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-michie)
- Record: [duckmouse-pronunciation-on-the-record.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/donald-michie/sources/duckmouse-pronunciation-on-the-record.md)



### Same two — Jesus Christ + Mickey Mouse — as two minds

Jesus Mouse lived as **one** Jesus Christ + Mickey Mouse soul. You could also put Jesus Christ and Mickey Mouse in **two minds** on one soul (they can argue). Not what he lived — just another shape:

```
soul
  minds
    jesus-mind ← parents: Jesus
    mouse-mind ← parents: Mickey Mouse
```

Other shapes exist too (personal *Jesus Mouse* mind, name alone, blend plus shoulders, game hooks). Memorials and design notes — not a playable adventure character yet.

---



## Shoulders — angel and devil

Multiple minds, one location:


| Shoulder | Pure well (examples)                             | Personal cup      |
| -------- | ------------------------------------------------ | ----------------- |
| Angel    | `"shoulder angel"`, `"cartoon conscience angel"` | `minds/my-angel/` |
| Devil    | `"shoulder devil"`, `"cartoon temptation devil"` | `minds/my-devil/` |


May argue over a **bridge**. Soul is player-in-the-middle. Either side can mute.

[society-of-mind](../society-of-mind/)

---



## Inheritance (optional depth)



### Pure well

```yaml
parents:
  - "biblical Jesus"
```

Any named archetype works the same way (Buddha, Mary, shoulder angel, shoulder devil, …).

### Personal cup

```yaml
parents:
  - "biblical Jesus"   # the well
  # optional: file archetype + local overrides
  - loves: tacos
  - hates: pickles
```

More: [Latent-Space Inheritance](../../designs/object-system/LATENT-SPACE-INHERITANCE.md) · [Self and MOOLLM](../../designs/object-system/SELF-AND-MOOLLM.md)

---



## What we mean / don’t mean

Organizational model — not a claim that souls are theologically “real.”


| We mean                                                  | We don’t mean                             |
| -------------------------------------------------------- | ----------------------------------------- |
| Soul = useful container: place, backpack, history, minds | Souls are metaphysical fact               |
| Multiple minds are first-class                           | Everyone has exactly one indivisible mind |
| Zero or more minds                                       | Minds require a soul; nesting forbidden   |
| Soul City = useful place                                 | Every game must become Soul City          |


Default: soul contains minds. Also fine: nested minds, sub-souls, bridges into other games.

---



## Vocabulary


| Term          | Meaning                                                               |
| ------------- | --------------------------------------------------------------------- |
| **Soul**      | Walks, carries stuff, holds minds                                     |
| **Soul City** | Place: rooms, shops, tools, roads, souls, …                           |
| **Mind**      | A voice / agency in (or beside) a soul                                |
| **Character** | Body / directory; may host a soul; can wear personas                  |
| **Persona**   | Worn look / role / costume description on a character                 |
| **Object**    | File or directory you can equip, wear, trade, drop — invent as needed |
| **Organelle** | A mind (or part of a mind) that keeps a game’s own layout and rules inside you — like a cell that swallowed another cell and kept its DNA |
| **Bridge**    | Channel between minds, souls, characters, games                       |
| **Well**      | Shared archetype already in training (say the name)                   |
| **Cup**       | Your personal mind that inherits a well + local changes               |

### Organelles, minds, directories

Biology’s sideways inheritance: mitochondria weren’t born as you — they were other cells that moved in and stayed. **Endosymbiosis.** Same idea here for games.

An **organelle** is a folder that holds one game’s way of organizing a person — The Sims album fields, a Micropolis mayor sheet, a CK3 character — without smashing those games into one shared format. Sync across; don’t flatten.

| Shape | On disk |
|-------|---------|
| Parallel minds (angel + devil, two agencies side by side) | **Sibling directories** under the soul |
| Nested mind (a mind inside a mind) | **Subdirectory** of the outer mind |
| Game / type as organelle (Sims mind, Micropolis mind, …) | **Directory** with that game’s files inside |
| Parts of a mind, or several games inside one mind | **Nested organelle directories** — each game keeps its own representation and organization |

Example sketch (paths are illustrative):

```
soul/
  minds/
    angel/                 ← sibling mind
    devil/                 ← sibling mind
    traveler/
      sims/                ← organelle: Sims layout stays Sims
      micropolis/          ← organelle: city-sim layout stays city-sim
      dents/               ← nested mind (subdirectory)
```

---

## Adventure as memory palace

Maps of rooms and exits are the old [method of loci](https://en.wikipedia.org/wiki/Method_of_loci). Adventureland’s Scott Adams and Don Hopkins discussed the lineage of adventure games, method of loci, mind mapping, and programming as navigation through code as places: [HN comment](https://news.ycombinator.com/item?id=29330901).

---



## Map instances

Bootstrap seed: `[examples/adventure-4/](../../examples/adventure-4/)` — one Soul City instance, not the prototype itself.


| Place                                                                           | What it is                                                                                                                                     |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [Soul Plaza](../../examples/adventure-4/street/lane-neverending/e2/soul-plaza/) | Shops for create / publish / share on Lane Neverending                                                                                        |
| [adventure-4 README](../../examples/adventure-4/README.md)                      | World layout (pub, coatroom, street, maze…)                                                                                                    |
| [ADVENTURE.yml](../../examples/adventure-4/ADVENTURE.yml)                       | Live simulation state                                                                                                                          |
| Nested minds seed                                                               | [don-hopkins/](../../examples/adventure-4/characters/real-people/don-hopkins/) — `dents/` + `slats/` under a host                              |
| MicropolisCore                                                                  | Product compose — engine + Sims companion ([design](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city.md)) |
| WWSFF catalog                                                                   | [create·publish·share](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city)                                        |


Directory = room. Character directory = soul or mind. YAML comments are data.

Many Soul Cities may exist; each supplies its own rooms, roads, plazas, vehicles.

---



## Cross-game (endosymbiosis)

Sideways inheritance again: a soul in Soul City can carry a Sims family album, a Micropolis mayor, a CK3 character, a memorial room — each as its own **organelle** (directory), linked by **bridges**. The Sims keep Sims organization; Micropolis keeps Micropolis. You copy and sync; you don’t force one mega-schema.

Soul containing minds is common. Also fine: nested minds, sub-souls, several game organelles under one traveler mind.

- [CHARACTER-ENDOSYMBIOSIS.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/CHARACTER-ENDOSYMBIOSIS.md)
- [Soul City catalog](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city)

---



## Minsky / Society of Mind


| SoM term              | Here                                                         |
| --------------------- | ------------------------------------------------------------ |
| Agents / agencies     | minds (and skill-agents elsewhere in MOOLLM)                 |
| K-lines               | names that activate latent prototypes or file paths          |
| B-brain               | a mind that watches the society                              |
| Censors / suppressors | shoulder mute, bridge attenuation, player-in-the-middle veto |
| Made-up minds         | blank cups that grow                                         |


[society-of-mind](../society-of-mind/README.md) · [LIVE-OBJECTS examples](../../designs/object-system/LIVE-OBJECTS-EXAMPLES.md)

---



## Play

1. Soul: `CHARACTER.yml` or template [player](characters/abstract/player/).
2. Rooms; inventory on the soul.
3. Mind = cup (subdirectory or co-located join).
4. Forks: shoulders may speak.
5. Game schema on a mind: **Import How…**, bridges, player-in-the-middle.

---



## Links


|                      |                                                                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jesus Mouse          | [memorial](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/jesus-mouse) · [HN](https://news.ycombinator.com/item?id=34398396) |
| Duckmouse            | [memorial](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-michie)                                                     |
| Soul Plaza / catalog | [WWSFF Soul City](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city)                                                    |
| Cross-game           | [CHARACTER-ENDOSYMBIOSIS](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/CHARACTER-ENDOSYMBIOSIS.md)                            |
| Adventure ↔ loci     | [HN 29330901](https://news.ycombinator.com/item?id=29330901)                                                                                          |
| Product              | [MicropolisCore soul-city](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city.md)                                  |


