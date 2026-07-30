# Soul Model

How beings are layered in Soul City — the full stack, how the pieces coexist, and where plurality is allowed.

Written for anyone walking into the model cold. Skills live under `skills/<name>/`; this page is the composed picture.

**About the word "soul":** it's used here in its plain, utilitarian, everybody-already-knows-it sense — the continuity that makes a character *someone*; the thing that persists and that minds ride in. No position is taken on religion, on whether souls are real, or on whether an AI, robot, or game character "really" has one — the same way programmers say "daemon" without theology. You bring your own beliefs; the model just gives you shapes to build with.

## One character, sketched

Before the tables, a concrete tree. Robin is a courier — invented for this page, and live on disk at [examples/characters/robin/](examples/characters/robin/) if you'd rather walk the real thing:

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

One body, one costume currently worn, one soul, three minds — two homegrown agencies plus one that carries a whole game's version of Robin. Every number in that tree is adjustable, and the rest of this page is about which numbers you can turn and what the shapes mean.

## The stack

Default grain, outside → in (or map → wearer → continuity → agencies):

```
Soul City / room / vehicle     place the body walks (or rides)
        │
   character                   body — moves on the map
        │                      location (a property that changes), inventory, hands, home, relationships
        ├── persona(s)         costumes worn on the body (0..N over time; usually one current)
        │     └── accessories  trees that transclude with the costume (parrot, fleas, …)
        │
        └── soul (usual: 1)    continuity — history; can jump bodies in stories that allow it
              └── mind(s)      resident agencies — 0, 1, or N
                    └── …      sub-minds, organelles, stubs, nested containers (optional)
```

| Term | Role | Skill |
|------|------|--------|
| **Soul City** | Liminal place: rooms, roads, shops, tools, objects, vehicles, parties | [soul-city](../soul-city/) |
| **Room** | Venue / framing on the map; atmosphere inherits down the tree | [room](../room/) |
| **Character** | The **body** that walks — location, inventory, relationships; hosts soul(s) | [character](../character/) |
| **Persona** | A **costume** the character wears — look, voice, role; may bring accessory trees | [persona](../persona/) |
| **Inventory / object** | What the body carries; objects may also orchestrate several characters (hot tub, maze) | [inventory](../inventory/), [object](../object/) |
| **Vehicle** | Movable thing with seats — embark; can pair with a multi-person persona (pantomime horse) | [vehicle](../vehicle/) |
| **Soul** | Continuity inhabiting a character — history + `minds[]`; rides along or jumps | [soul](../soul/) |
| **Mind** | Resident **agency** under (or beside) a soul — well, cup, organelle, stub, zombie, … | [mind](../mind/) |
| **Party** | Several characters / souls traveling together | [party](../party/) |

**Persona ≠ mind.** Costume changes presentation; mind is who is thinking. Switching pirate clothes does not swap the angel on your shoulder.

**Character ≠ soul.** Body walks and holds pockets; soul is the continuity that can leave the body. Usual case: one soul in one character, walking with its minds.

## Pluralities (all first-class)

| Layer | Typical | Also valid |
|-------|---------|------------|
| Character ↔ soul | 1 soul per character | **0** — uninhabited shell (prop, puppet, parked body) · soul-jumping · more than one soul aboard |
| Soul ↔ mind | 1 mind | **0** mindless · **N** multi-minded (shoulders, committees, one mind per game, …) |
| Character ↔ persona | One worn at a time | Wardrobe of many; multi-person persona + vehicle (two seats, one costume) |
| Mind nesting | Flat under soul | Mind hosts sub-minds / sub-souls / organelles; Self models anything |
| Place | One city instance | Many cities; games keep their own rules; souls may know people across games |

Worked shapes: robot (soul optional minds), zombie (replace `minds[]` with a zombie mind), remote-control (mind stub to an external pilot), pantomime horse (one persona, two characters), Sims group object (slots + piggyback social).

Multi-minded isn't an edge case bolted on for fiction — plenty of people model their own thinking as a society of inner agencies, and Minsky wrote the book on it ([Society of Mind mapping below](#minsky--society-of-mind)). The model treats every cardinality as a normal shape you can author.

**Jump to what you care about:**

| If you're here for… | Go to |
|---------------------|-------|
| Many minds, one person | [Minds](#minds) — fronting, counsel, shoulders, B-brain, Society of Mind |
| Building characters from pieces of other characters | [Examples](#examples) (Jesus Mouse, Duckmouse, `from love import trust`) |
| Costumes, props, group activities (Sims-style) | [Character](#character) (pirate parrot, pantomime horse, hot tub) |
| Carrying whole games inside you without flattening them | [Organelles, minds, membranes](#organelles-minds-membranes) |
| Maps and memory | [Adventure as memory palace](#adventure-as-memory-palace) |

---

## Soul

A soul inhabits a character ([soul](../soul/)). It holds **history** and **zero or more minds** — one is the default. It rides with the character's location while inhabited; in stories and models that allow it, it can leave, jump bodies, or share one.

| Minds | Shape |
|-------|-------|
| 0 | Mindless — persists with the character; no resident agency |
| 1 | Single-minded (the default) |
| N | Multi-minded (shoulders, committees, one mind per game, …) |

Robots can have souls. Zombies swap in a zombie mind. Remote-control is a mind stub. **You author the architecture** — the model supplies shapes, not verdicts.

**Whose soul do the minds share?** Left open, on purpose. The default grain is one soul with the minds inside it. Equally valid: each mind carrying a sub-soul of its own; several souls bridged in one body; one soul spanning characters across games. If you experience or design it differently, model it the way it actually works — the directory tree bends to fit you, not the reverse.

Souls can know characters, personas, and minds that live in *other* games. Free form.

---

## Minds

A **mind** is a resident agency — a voice that notices, prefers, argues, and acts ([mind](../mind/)). It usually rides in a soul and shares the soul's location; no separate map pin.

| Kind | Meaning |
|------|---------|
| blank | Exists; no parent required |
| inherited | Parents = latent well and/or file archetype |
| cup | Personal mind: inherits a well, holds local changes |
| organelle | Bound to one game/ecosystem's schema; own DNA; syncs |
| stub | Thin agency — e.g. remote-control bridge to an external pilot |
| zombie | Infection / replacement mind; often sole survivor in `minds[]` |
| made-up / imported | Grown from nothing, or brought from elsewhere |

### One mind per game

In Soul City it's perfectly normal — expected, even — to keep **at least one mind per game you project into**. Each is an organelle: it holds that game's version of you (Sims traits and family album, a Micropolis mayor sheet, a CK3 character) in that game's own format, and it fronts whenever you're wearing that game's persona. Your Sims-mind thinks in motives and relationships; your mayor-mind thinks in zones and budgets. Neither gets flattened into the other; bridges carry what's shared. Details: [Organelles, minds, membranes](#organelles-minds-membranes).

### How minds get along

| Move | What happens |
|------|---------------|
| **Front** | One mind steers and speaks for the soul right now; the others ride along |
| **Counsel** | Minds advise the fronting mind over a bridge — suggestions, warnings, jokes |
| **Disagree** | Two minds argue; the soul (or the human at the keyboard) is player-in-the-middle and arbitrates |
| **Take turns** | Fronting rotates — by scene, by game, by mood, by agreement |
| **Mute** | Either side of a bridge can mute; censors and suppressors are standing mutes |
| **Hand off** | Fronting transfers mid-scene — a `goto` between agencies |

Nothing here ranks the minds. Fronting is a role, not a hierarchy.

### Shoulders — angel and devil

The classic two-minds cartoon, worked out:

| Shoulder | Pure well (examples)                             | Personal cup      |
| -------- | ------------------------------------------------ | ----------------- |
| Angel    | `"shoulder angel"`, `"cartoon conscience angel"` | `minds/my-angel/` |
| Devil    | `"shoulder devil"`, `"cartoon temptation devil"` | `minds/my-devil/` |

May speak over a **bridge**. Soul is player-in-the-middle. Either side can mute.

### B-brain — the mind that watches the minds

Minsky's A-brain / B-brain: the **A-brain** deals with the world; the **B-brain** watches the A-brain. It can't see the world at all — only the mind in front of it — and that limitation is exactly what makes it useful. It notices what a world-facing mind can't notice about itself: loops ("that's the fourth time you've re-read the same page"), stuck agencies, one voice drowning out the rest, a mood quietly coloring every decision.

In this model a B-brain is just another mind whose *subject* is the rest of the society. It observes, profiles, and suggests — mute this, hand off that, take a break. It doesn't outrank anyone: a B-brain that seizes fronting has just become an A-brain with a clipboard. (You can add a C-brain to watch the B-brain. Turtles are allowed; usefulness runs out fast.)

### Minsky / Society of Mind

| SoM term              | Here                                                         |
| --------------------- | ------------------------------------------------------------ |
| Agents / agencies     | minds (and skill-agents elsewhere in MOOLLM)                 |
| K-lines               | names that activate latent prototypes or file paths          |
| B-brain               | a mind that watches the society                              |
| Censors / suppressors | shoulder mute, bridge attenuation, player-in-the-middle veto |
| Made-up minds         | blank cups that grow                                         |

[society-of-mind](../society-of-mind/README.md) · [LIVE-OBJECTS examples](../../designs/object-system/LIVE-OBJECTS-EXAMPLES.md)

---

## Character

The body / directory ([character](../character/)). Walks the map. Carries stuff ([inventory](../inventory/)). Can **switch personas** — put on a look / role / costume ([persona](../persona/)).

Want a hat you can equip, trade, or drop outside a persona? Make an **object** — a file or directory — and put it in the character’s inventory ([object](../object/)).

### Personas bring stuff with them

When a character **wears** a persona, the persona can **transclude** accessories — whole little hierarchies that come along for the ride.

Classic example: wear **Pirate**. You get the clothes, the peg leg, the accent, the tag lines (“Yar!” when something triggers them) — and a **parrot on the shoulder**. That parrot is its own tree: maybe it has fleas. The fleas are under the parrot. Take off the pirate persona and the default parrot goes with it (unless you kept a personal one).

| In the pirate persona | What it is |
|-----------------------|------------|
| Clothes, peg leg | Costume / props |
| Accent, tag lines | Voice — lines fired on triggers |
| Generic parrot | Default pet under the persona |
| Fleas (optional) | Nested under the parrot |

adventure-4’s wardrobe pattern: [personas/](../../examples/adventure-4/personas/) (e.g. [Captain Ashford](../../examples/adventure-4/personas/captain-ashford.yml) — coat, scarf, speech modifiers). Coatroom / Maurice is where you try them on.

### Your parrot, not just the stock one

You can use the **generic** parrot that lives in the pirate persona, or **instantiate your own** on your shoulder — a thin shell around the generic parrot with your own data and tricks.

Same idea as well → cup: the shared pirate-parrot is the well; your shoulder parrot is the cup — local lines, methods, fleas of your own. Teach it by example (“program by example”): say the line you want, it learns a personal response. Stock parrot stays available for everyone else.

```
character/
  personas/worn → pirate/
    clothes, peg-leg, accent, taglines…
    parrot/                 ← generic (from the persona)
      fleas/
  shoulder/
    my-parrot/              ← your thin shell around generic parrot
      lines.yml             ← personal tag lines you taught it
      tricks/               ← methods you trained
```

### Multi-person personas (pantomime horse)

![Pantomime horse straddling the closing doors of a London Underground train — front end inside looking out the window, back end still on the platform. "Please don't hold the doors open."](images/pantomime-horse-tfl.png)

*Transport for London safety poster (Mayor of London / TfL). Two characters, one persona, one vehicle — and a hard lesson in what happens when the party spans a membrane while the doors close.*

The **pantomime horse** is one persona **and** a two-character [vehicle](../vehicle/) — a movable costume you both inhabit.

- **Persona:** one horse look / gag / voice shared by whoever’s inside
- **Vehicle:** two seats — **front end** and **back end** — that walk the map together
- Switch roles — “Why do I always have to be the back end? I want to try the front for once!”

```
persona+vehicle/pantomime-horse/
  persona:     one costume (the horse)
  vehicle:     walks as one body on the map
  roles/
    front/     ← sees, steers, talks (maybe)
    back/      ← walks the rear, trusts the front
  seats: 2     ← two characters EMBARK / WEAR into the same thing
```

Roles can take turns. One shared persona; one vehicle; two characters aboard.

### Group objects (Sims-style orchestration)

Same pattern as Sims objects that orchestrate several people at once: the hot tub, the pool table, the Sims Online maze puzzle. The **object** (or multi-person persona) owns the activity; characters claim **roles** / slots; they can rotate.

On top of the group activity, social behavior **piggybacks** — talking, joking, bonding, or becoming bitter enemies — while you soak, shoot pool, or solve the maze. The friendship (or feud) is a side channel riding the shared activity, not a separate appointment.

| Kind | Example | What it orchestrates |
|------|---------|----------------------|
| Persona + vehicle | Pantomime horse | One costume, two seats (front/back); walks as one |
| Group object | Hot tub, pool table, maze puzzle | Several Sims in slots; shared animation / puzzle state |
| Piggyback social | Chat while soaking | Relationship deltas on top of the activity |

Free form: invent the slots, the turns, the win conditions, the side chat.

---

## Soul City

The city: rooms, roads, plazas, shops, tools, objects, vehicles, parties — characters walking it, souls aboard.

Many cities. Bootstrap map: [adventure-4](../../examples/adventure-4/) · [Soul Plaza](../../examples/adventure-4/street/lane-neverending/e2/soul-plaza/) (create / publish / share shops).

---



## Examples

A **soul** or a **mind** can **import** *pieces* of famous characters — Mickey Mouse, Donald Duck, Gandalf the Wizard — the hat, the mission, how a name sounds — and leave the rest. Real people, animals, abstract concepts like love itself: same move.

```
from love import trust, ambiguity
```

Not the whole of love — just those two facets. Leave the rest.

**Scope** (where you put the import):

| Import into… | Who sees it |
|--------------|-------------|
| The **soul** | Shared by all minds on that soul |
| A **mind** | Only that mind (and nested stuff under it) |

Put common gear and shared mission on the soul. Put angel-only counsel on the angel mind, devil-only temptation on the devil mind.

**Open mind** vs **closed mind** — same words as in programming languages:

| Term | In languages | Here |
|------|--------------|------|
| **Open** | Module / class still accepts new imports, mixins, extensions | Mind (or soul) still allows new `from … import …` |
| **Closed** / **sealed** | No further extension; API frozen | Mind sealed — no new imports; what it has is what it runs |

Keep an open mind to learn; seal a mind when that agency should stay fixed (a finished stub, a locked organelle, a ritual voice that must not drift).

### Same words as code

This model is deliberately grounded in programming language ideas:

| PL idea | Here |
|---------|------|
| **`import` / `from … import …`** | Pull a trait from a well into a soul or mind |
| **Scope** | Soul scope (shared) vs mind scope (private to that agency) |
| **Agent** | A mind — an autonomous little program with its own bindings |
| **Closure** | A mind/cup that captured its imports and local state; carries that environment when it runs |
| **Continuation** | Where control goes next — the next beat, the next room, the next thought after a bridge returns |
| **`goto` / jump** | Soul jumps character; mind hands off; narrative teleport — same “transfer of control” instinct |

Recipes below are not programs you run. Read a line as: from *this famous figure*, take *this one trait*, call it *this*.

| Who                           | Combination                                      | What was borrowed                                              | More                                                                                              |
| ----------------------------- | ------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Jesus Mouse**               | **Jesus Christ + Mickey Mouse** (+ Wizard props) | One character, one soul — look, mission, mouse costume, wizard gear | [memorial](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/jesus-mouse)   |
| **Duckmouse** (Donald Michie) | **Donald Duck + Mickey Mouse**                   | Name *sounds* only — nothing else from the cartoons            | [memorial](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-michie) |

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



## Inheritance (optional depth)

Imports land on a **soul** (shared scope) or a **mind** (agency scope). Open minds accept more imports; closed/sealed minds do not.

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
| Usually one soul per character; jumps / multi-soul / zero-soul shells possible | Every being has exactly one fixed soul forever glued to one body |
| Multiple minds are first-class | Everyone has exactly one indivisible mind |
| Minds may share one soul or carry their own — you author it | The model rules on which arrangement is true |
| Soul City = useful place | Every game must become Soul City |

Default: character ⊃ soul ⊃ minds. Also fine: nested minds, sub-souls, bridges into other games, soul moves between characters.

---



## Vocabulary


| Term          | Meaning                                                               |
| ------------- | --------------------------------------------------------------------- |
| **Character** | Body that walks; inventory; wears personas; usually hosts one soul    |
| **Soul**      | Continuity that inhabits a character; holds zero or more minds; can jump |
| **Mind**      | A voice / agency riding in a soul                                     |
| **Fronting**  | Which mind is currently steering / speaking for the soul — a role, not a rank |
| **B-brain**   | A mind whose subject is the other minds — watches the society, suggests, never outranks |
| **Soul City** | Place: rooms, shops, tools, roads, characters (souls aboard), …       |
| **Persona**   | Worn costume/role on a **character**; may transclude accessories; may pair with a vehicle (pantomime horse = one persona + two seats) |
| **Object**    | Equip/wear/trade item — or a **group object** that seats several characters (hot tub, pool table, maze) |
| **Role / slot** | Seat in a multi-person persona or group object; turn-taking allowed |
| **Cup / shell** | Thin local layer around a shared default (your parrot over generic parrot) |
| **Organelle** | A mind (or part of a mind) that keeps a game’s own layout and rules inside you — swallowed cell with its own DNA **and membranes** |
| **Membrane** | Boundary that keeps insides inside: **directories** and **files** are membranes; they hold shape without mixing contents |
| **Endosymbiosis** | Something moves in and keeps its own organization and membranes (mitochondria; a Sims album, mind, pet, or horse-end as a folder). **Don’t flatten.** Round-trip JSON; round-trip [YAML Jazz](../yaml-jazz/) **including comments**. Pass through what you don’t understand — **don’t strip it out**. |
| **Bridge**    | Channel between minds, souls, characters, games — biology’s **membrane traffic** constellation (below) |
| **Well**      | Shared archetype already in training (say the name)                   |
| **Cup**       | Your personal mind that inherits a well + local changes               |
| **Import**    | `from well take trait` into a soul (shared) or a mind (local) — same idea as language `import` |
| **Open mind** | Still accepts new imports / extensions (open module) |
| **Closed / sealed mind** | No further imports; bindings frozen (sealed class / closed module) |
| **Scope**     | Where a binding is visible — soul-wide vs one mind vs nested folder |
| **Agent**     | A mind as a little autonomous program |
| **Closure**   | Mind/cup plus the environment it captured when imported |
| **Continuation** | What runs next after a bridge / thought / room exit |
| **Goto / jump** | Transfer of control — soul changes character, narrative teleport, handoff |

**Bridge ≈ how cells move cargo across and between membranes** ([vesicle transport](https://en.wikipedia.org/wiki/Vesicle_%28biology_and_chemistry%29), [endocytosis / exocytosis](https://en.wikipedia.org/wiki/Endocytosis)):

| Bio term | Plain | Here |
|----------|-------|------|
| **Vesicle** | Little membrane bubble carrying cargo | A package you copy / sync / ship (file, album page, save chunk) |
| **Endocytosis** | Swallow in | Import into a soul / organelle / directory |
| **Exocytosis** | Spit out | Export / publish / write back to a game |
| **Transcytosis** | In one side, out the other | Through-traffic — e.g. Sims → Soul City → Micropolis without dissolving either |
| **Channel / transporter / porin** | Selective pore in a membrane | Narrow bridge — only some fields pass |
| **Gap junction** / **plasmodesmata** | Direct cell-to-cell pores | Mind↔mind or soul↔soul side channel while both stay intact |
| **Membrane trafficking** | The whole logistics system | Bridges + sync + round-trip; don’t strip what you don’t understand |

**Membrane trafficking** is the cell’s logistics network — belts, buffers, and handoffs that move cargo without destroying the packages. That’s what [Factorio](https://www.factorio.com/) and [Dyson Sphere Program](https://store.steampowered.com/app/1366780/Dyson_Sphere_Program/) are about: factories that ingest, route, transform, and spit out materials while each station keeps its own buffers. Same philosophy here — bridges and sync are your belts; JSON / YAML Jazz packets are the cargo; unknown fields ride through untouched (a belt that shreds mystery boxes is a broken factory).

### Organelles, minds, membranes

**Endosymbiosis** — sideways inheritance: mitochondria weren’t born as you; they moved in and kept their own DNA and membranes. Same move for a parrot, fleas, Sims sheet, horse back-end, album beat — swallow it as a folder; **don’t flatten**.

How you treat the guest once it’s inside:

- Round-trip **JSON** — what goes in comes back out
- Round-trip **YAML Jazz** — including the **comments** (comments are data; see [yaml-jazz](../yaml-jazz/))
- Field or file you don’t understand? **Leave it alone.** Don’t strip unknown keys, unknown files, or “extra” comments to “clean up”
- Survive first; optimize later — a cell that dissolves its guest’s membrane kills the guest

An **organelle** is a folder that holds one game’s way of organizing a person — The Sims album fields, a **Micropolis mayor sheet** (role sheet), a CK3 character — without smashing those games into one shared format. Sync across; don’t flatten.

**Micropolis mayor / role sheets:** Micropolis does not (yet) simulate individual citizens. It **imports/exports characters** (players + agents) into **roles** — mayor, architect, bulldozer driver, zoner, city council, journalist, photographer, GitHub issue creator/reviewer, … — each role a socket for a tool or tool cluster. Experience and city screenshots ride in the character’s album (*My time as mayor of Foobaropolis*) and travel to other games. Same grain as a Sims job, orchestrable through Simplifier (dialog → screen-scrape → button RPC). Full design: [micropolis-role-sheets.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/micropolis-role-sheets.md) · skill artifact [`skills/micropolis/artifacts/role-sheets.yml`](../micropolis/artifacts/role-sheets.yml).

**Membranes on disk:**

| Membrane | What it does |
|----------|----------------|
| **Directory** | Hard membrane — inside stays inside; easy to nest |
| **File** | Membrane around one blob of stuff |
| **Shared filename prefix** among siblings | Lightweight local sub-membrane — `parrot-body.yml`, `parrot-lines.yml` group together in the tree, easy to “penetrate” (open one without crossing a new folder) |
| **Enumerated prefixes** (`01-…`, `02-…`, …) | Membrane *between* each sequential item — a **line of bubbles**; each bubble is one slot. Arrays. |

| Shape | On disk |
|-------|---------|
| Parallel minds (angel + devil) | **Sibling directories** under the soul |
| Nested mind | **Subdirectory** of the outer mind |
| Game organelle | **Directory** — that game’s membrane |
| Parts / several games in one mind | **Nested organelle directories** |
| Soft group of related files | Same **prefix** in one directory |
| Ordered list | Numbered prefixes — bubbles in a line |
| Album / blog / playlist / story | Enumerated **subdirectories** — each bubble a beat |

### Universal sequence: album · blog · storybook · playlist

Same membrane pattern everywhere people tell stories in order — and the same pattern for **any** series of objects:

| Name people use | Same shape |
|-----------------|------------|
| Family album | Pages / photos in order |
| Blog | Posts |
| Storybook | Chapters / spreads |
| YouTube playlist | Videos |
| StoryMaker sequence | Beats / scenes |
| Series of numbered folders | `01/`, `02/`, `03/`… |

**Naming convention**

| On disk | Means |
|---------|--------|
| Prefixed index (`01-…`, `02-…`) | Ordered bubble in the line |
| Name without index | The name says what it is |
| **Plural** name (`photos/`, `posts/`, `playlists/`) | A **collection** of the singular type — often backed by a skill that knows that type |
| Container directory | Conventionally the **plural** of what it holds |

So `family-albums/`, `playlists/`, `storybooks/` are containers. Inside them: items (beats, tracks, pages) plus files that declare **interface, state, metadata, inherited behaviors** — not only the enumerated kids.

**Collective views** — different ways to present the same collection:

| File / skill | Role |
|--------------|------|
| `FAMILY-ALBUM.yml` / family-album skill | Import/export Sims Family Album; render as Markdown, web page, flip book, … |
| `PLAYLIST.yml` / `STORYBOOK.yml` | Same series, different collective lens |
| `RSS.yml` | Drop-in: how to publish this container as RSS |
| `README.md` / rendered `.md` | Human view of the whole or of one beat |
| Per-type handlers in the config | “If item is a photo… if item is a video link…” |

```
family-albums/my-goths/          ← plural container
  FAMILY-ALBUM.yml               ← interface + state + import/export how-to
  RSS.yml                        ← optional publish view
  README.md                      ← rendered collective view
  01-wedding/
    README.md
    photo.jpg
    meta.yml
  02-baby/
    …
```

A **family-album** skill can own Sims album bridges and render recipes. An **RSS** config rides along without the album skill needing to be an RSS expert. A **pdf** skill owns PDF guts; [change-name](../change-name/) (or anyone else) **composes** with it instead of swallowing PDF code forever.

That composition — guest skill keeps its membrane; host uses it via bridges — **is endosymbiosis in action.**

Same whether it’s a Sims family album organelle, a memorial storybook, or a YouTube playlist folder — don’t flatten the beats into one soup.

Example sketch (minds + organelles):

```
soul/
  minds/
    angel/                 ← sibling membrane
    devil/                 ← sibling membrane
    traveler/
      sims/                ← organelle membrane: Sims stays Sims
        family-album/      ← sequence of bubbles
          01-wedding/
          02-baby/
      micropolis/          ← organelle membrane: city-sim stays city-sim
      dents/               ← nested mind
      parrot-body.yml      ← prefix sub-membrane (soft group)
      parrot-lines.yml
      01-trick-speak.yml   ← bubbles in a line (array)
      02-trick-wave.yml
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


