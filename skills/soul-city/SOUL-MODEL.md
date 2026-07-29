# Soul Model

**Character** and **soul** are different levels.

- A **character** is the body that walks around — backpack, hands, costume. It **wears personas** and holds **inventory**.
- A **soul** is what inhabits that body — continuity, history, and **zero or more minds** riding along.
- Usually one soul per character. Fiction is full of souls jumping bodies; theoretically a character could host more than one.

That is the mind/body split as **soul / character**: the soul can move; the character is the vessel; the minds come along inside the soul.

**Soul City** is a place characters walk (rooms, shops, tools, roads, parties) with their souls aboard. Games keep their own rules; souls can still know people across games.

---

## Character

The body / directory ([character](../character/)). Walks the map. Carries stuff ([inventory](../inventory/)). Wears look / role / costume as a **persona** ([persona](../persona/)).

adventure-4 doesn’t force costumes into a special object type. Want a hat you can equip, trade, or drop? Make an **object** — a file or directory — and put it in the character’s inventory ([object](../object/)).

---

## Soul

What lives in the character — continuity and minds ([soul](../soul/)). **Zero or more minds.** The soul rides with the character’s location while inhabited; it can leave or jump in stories and models that allow it.


| Minds | Shape                                               |
| ----- | --------------------------------------------------- |
| 0     | Mindless — persists with the character; no resident agency |
| 1     | Single-minded                                       |
| N     | Multi-minded (angel/devil shoulders, committees, …) |


Robots can have souls. Zombies swap in a zombie mind. Remote-control is a mind stub. You author the architecture — mindless, single, or multi.

Souls can know characters, personas, and minds that live in *other* games. Free form.

---

## Soul City

The city: rooms, roads, plazas, shops, tools, objects, vehicles, parties — characters walking it, souls aboard.

Many cities. Bootstrap map: [adventure-4](../../examples/adventure-4/) · [Soul Plaza](../../examples/adventure-4/street/lane-neverending/e2/soul-plaza/) (create / publish / share shops).

---



## Examples

A **soul** can borrow *pieces* of famous characters, like Mickey Mouse, Donald Duck, Gandalf the Wizard — the hat, the mission, how a name sounds — and leave the rest. Different souls can borrow different pieces of multiple real and fictional people, animals, or abstract concepts like love itself.


| Who                           | Combination                                      | What was borrowed                                              | More                                                                                              |
| ----------------------------- | ------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Jesus Mouse**               | **Jesus Christ + Mickey Mouse** (+ Wizard props) | One character, one soul — look, mission, mouse costume, wizard gear | [memorial](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/jesus-mouse)   |
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

Jesus Mouse lived as **one** Jesus Christ + Mickey Mouse soul. You could also put Jesus Christ and Mickey Mouse in **two minds** on one soul (they can counsel or disagree). Not what he lived — just another shape:

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


May speak over a **bridge**. Soul is player-in-the-middle. Either side can mute.

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


| We mean | We don’t mean |
|---------|----------------|
| Character = body that walks, carries, wears personas | Character and soul are the same thing |
| Soul = continuity that inhabits a character; holds minds | Souls are metaphysical fact |
| Usually one soul per character; jumps / multi-soul possible | Every being has exactly one fixed soul forever glued to one body |
| Multiple minds are first-class | Everyone has exactly one indivisible mind |
| Soul City = useful place | Every game must become Soul City |

Default: character ⊃ soul ⊃ minds. Also fine: nested minds, sub-souls, bridges into other games, soul moves between characters.

---



## Vocabulary


| Term          | Meaning                                                               |
| ------------- | --------------------------------------------------------------------- |
| **Character** | Body that walks; inventory; wears personas; usually hosts one soul    |
| **Soul**      | Continuity that inhabits a character; holds zero or more minds; can jump |
| **Mind**      | A voice / agency riding in a soul                                     |
| **Soul City** | Place: rooms, shops, tools, roads, characters (souls aboard), …       |
| **Persona**   | Worn look / role / costume on a **character**                         |
| **Object**    | File or directory a character can equip, wear, trade, drop            |
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

1. Character: `CHARACTER.yml` or template — walks, inventory, persona.
2. Soul inhabits the character; zero or more minds ride in the soul.
3. Rooms on the map; stuff in the character’s backpack.
4. Shoulders / other minds may speak.
5. Game schema on a mind: bridges, player-in-the-middle.

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


