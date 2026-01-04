# Adventure 1: The Minimal Quest

> *"Every journey begins with two rooms."*

The simplest possible adventure: one hero, two rooms, one door.

**...that grew into a 30-file grue-infested costume-wearing food-dropping gold-hoarding masterpiece.**

---

## 🎬 How This World Was Bootstrapped

This adventure was built **entirely through conversation**. Starting from nothing, each chat message added a new feature. The README you're reading IS the chat log — a record of collaborative world-building between human and LLM.

### The Bootstrapping Philosophy

1. **Start minimal** — Two rooms, one hero, one door
2. **Add features incrementally** — Each request extends the world
3. **Document as you go** — The README grows with the world
4. **Coherence check** — Periodically verify everything links correctly
5. **The chat IS the tutorial** — Anyone can follow along

### What Makes This Special

- **No templates used** — Built from scratch through dialogue
- **Every file has a story** — We can trace why each thing exists
- **Iterative refinement** — Files were modified multiple times
- **Human + LLM collaboration** — Ideas flow both directions

---

## 📜 Complete File History

### Files Created (32 total)

| File | Created In | Purpose |
|------|------------|---------|
| `README.md` | Chat 1 | The creation story (this file!) |
| `player.yml` | Chat 1 | The hero |
| `start/ROOM.yml` | Chat 1 | Starting room |
| `end/ROOM.yml` | Chat 1 | Goal room |
| `start/lamp.yml` | Chat 2 | Light source |
| `end/treasure.yml` | Chat 2 | The MacGuffin |
| `maze/README.md` | Chat 4 | Maze documentation |
| `maze/room-a/ROOM.yml` | Chat 4 | Maze room (puddle) |
| `maze/room-b/ROOM.yml` | Chat 4 | Maze room (echo) |
| `maze/room-c/ROOM.yml` | Chat 4 | Maze room (scratches) |
| `maze/room-d/ROOM.yml` | Chat 4 | Maze room (glow) |
| `maze/room-e/ROOM.yml` | Chat 8 | Maze room (cobwebs) |
| `maze/room-f/ROOM.yml` | Chat 8 | Maze room (cold) |
| `maze/room-g/ROOM.yml` | Chat 8 | Maze room (face) |
| `maze/room-h/ROOM.yml` | Chat 8 | Maze room (mushrooms) |
| `maze/room-i/ROOM.yml` | Chat 8 | Maze room (skeleton) |
| `maze/room-j/ROOM.yml` | Chat 8 | Maze room (crossroads) |
| `kitchen/README.md` | Chat 8 | Kitchen documentation |
| `kitchen/ROOM.yml` | Chat 8 | Kitchen room |
| `kitchen/fridge.yml` | Chat 8 | 20 food items |
| `kitchen/stove.yml` | Chat 8 | Decorative stove |
| `kitchen/sink.yml` | Chat 8 | Eternal dishes |
| `kitchen/table.yml` | Chat 8 | Mother's note |
| `coatroom/README.md` | Chat 9 | Costume docs |
| `coatroom/ROOM.yml` | Chat 9 | Costume emporium |
| `coatroom/mirror.yml` | Chat 9 | See your costume |
| `coatroom/mannequin.yml` | Chat 9 | Costume consultant |
| `coatroom/costume-racks.yml` | Chat 9 | Infinite costumes |
| `kitchen/fridge.yml` | Chat 10-12 | EAT mechanic + transformations |
| `maze/room-j/lamp-vendor.yml` | Chat 13 | ACME Lamp Refueling — tribute to Colossal Cave battery vendor |
| `maze/room-f/gold-pile.yml` | Chat 14 | 100 gold coins — the skeleton's fortune! |
| `start/README.md` | Consistency check | Navigation & documentation |
| `end/README.md` | Consistency check | Navigation & documentation |

### Evolutionary History of Key Files

#### `player.yml` — 6 Versions

| Version | Changes |
|---------|---------|
| v1 | Generic "Hero", location: start, empty inventory |
| v2 | Renamed to "Bumblewick Fantastipants", added Hobbit-style backstory, Pee Wee catchphrases, traits (spoon_enthusiast, tuesday_rhymer, waistcoat_devotee) |
| v3 | Added score: 0, deaths: 0, moves: 0 for reincarnation tracking |
| v4 | Added costume state (wearing, accessories), updated notes to mention all 3 exits |
| v5 | Added trait: `catastrophic_digestion` for the eating mechanic |
| v6 | Added `gold: 10` — enough for refills, snacks, and bribes! |

#### `start/ROOM.yml` — 5 Versions

| Version | Changes |
|---------|---------|
| v1 | Simple chamber, exit north → end |
| v2 | Added Zork-style description, scratched initials (WC+DW '76, SA '78, XYZZY), lamp on shelf |
| v3 | Exit north changed to → maze/room-a, added grue_safe: true, magical lighting |
| v4 | Added respawn_point: true, respawn_message for reincarnation |
| v5 | Added west exit → kitchen, east exit → coatroom, description updated to list all 3 exits |

#### `end/ROOM.yml` — 4 Versions

| Version | Changes |
|---------|---------|
| v1 | Simple end chamber, exit south → start |
| v2 | Added dramatic description, empty pedestals, golden light, "please deposit in well house" |
| v3 | Exit south changed to → maze/room-d, added grue_safe: true |
| v4 | Description clarified: "south leads back into the maze" not "back to beginning" |

#### `start/lamp.yml` — 3 Versions

| Version | Changes |
|---------|---------|
| v1 | Brass lamp, lit: true, oil: 400, GET/LIGHT/EXTINGUISH/RUB actions, genie joke |
| v2 | Added oil_warning: 50, oil_critical: 10, CHECK OIL action, LIGHT/EXTINGUISH responses |
| v3 | **Floating-point oil system!** Oil consumption rates by action type, environmental modifiers (cold room = 2x drain), DM instructions for applying oil costs each turn |

#### `end/treasure.yml` — 2 Versions

| Version | Changes |
|---------|---------|
| v1 | Jeweled Chalice, points: 10, GET/EXAMINE/DRINK_FROM actions |
| v2 | Added victory response on GET, score update logic |

#### `maze/room-*.yml` — 3+ Versions

| Version | Changes |
|---------|---------|
| v1 | Basic room with feature and tangled exits |
| v2 | Added grue_event with death message |
| v3 | Added MC Frontalot lyrics + YouTube link, reincarnation message |

#### `maze/room-j/` & `maze/room-i/` — Special Updates

| Room | Change |
|------|--------|
| room-j | Added `lamp-vendor.yml` — ACME Lamp Refueling Co. |
| room-j | Description updated to mention the vending machine |
| room-i | Skeleton now has "3 gold pieces (enough for THREE refills)" |
| room-i | Added `skeleton_note` — "They were SO CLOSE to room-j" |

---

## The Chat That Created This

**User:** Create a first "adventure-1" subdir. Instantiate a new adventure there with an initial player, with two rooms — south is "start" and north is "end" and they have links back and forth. The player starts in start. They are the generic hero protagonist.

**DM:** Creating the minimal adventure...

---

## What Was Created

```
adventure-1/
├── README.md           # You are here (the creation story)
├── player.yml          # Bumblewick Fantastipants, reluctant hero
├── start/              # Chamber of Commencement
│   ├── README.md       # Room documentation & navigation
│   ├── ROOM.yml        # Exits: N→maze, W→kitchen, E→coatroom
│   └── lamp.yml        # The classic brass lamp (400 moves)
├── kitchen/            # Fantastipants Family Kitchen (WEST)
│   ├── ROOM.yml        # Magically lit, safe from grues
│   ├── fridge.yml      # 20 FOOD ITEMS for maze mapping!
│   ├── stove.yml       # Not in use (adventures first)
│   ├── sink.yml        # Eternal dishes
│   └── table.yml       # Note from Mother
├── coatroom/           # Costume Emporium (EAST)
│   ├── ROOM.yml        # Infinite costume possibilities
│   ├── mirror.yml      # See your transformation
│   ├── mannequin.yml   # Helpful costume consultant
│   └── costume-racks.yml # Every costume imaginable
├── maze/               # A Maze of Twisty Little Passages (10 rooms!)
│   ├── README.md       # Map, solution, grue warnings
│   ├── room-a/         # Puddle (S→start)
│   ├── room-b/         # Echo
│   ├── room-c/         # Scratches
│   ├── room-d/         # Golden glow (N→end)
│   ├── room-e/         # Cobwebs
│   ├── room-f/         # Cold spot
│   ├── room-g/         # Carved face
│   ├── room-h/         # Mushrooms
│   ├── room-i/         # Skeleton
│   └── room-j/         # Crossroads
└── end/                # Treasury of Modest Proportions  
    ├── README.md       # Room documentation & navigation
    ├── ROOM.yml        # Dramatic lighting, triumph achieved
    └── treasure.yml    # The Jeweled Chalice (10 points!)
```

---

## The Artifacts

### [player.yml](./player.yml) — Bumblewick Fantastipants

*"Adventures make one late for dinner."*

Your character. Reluctant hero, spoon enthusiast, waistcoat devotee.

- **Location:** start (the Chamber of Commencement)
- **Inventory:** empty (the lamp awaits! his spoons do not)
- **Gold:** 10 pieces (for refills, snacks, and bribes!)
- **Goal:** reach the end, claim the treasure, make Mother insufferable
- **Mood:** bewildered but optimistic

### [start/ROOM.yml](./start/ROOM.yml) — Chamber of Commencement

*"You are standing in a small chamber carved from living rock..."*

- **Exit north:** into darkness, toward glory (or grues)
- **Features:** Scratched initials (WC+DW '76, SA '78, XYZZY WAS HERE)
- **Contains:** The brass lamp

### [start/lamp.yml](./start/lamp.yml) — The Brass Lamp

*"Property of Colossal Cave, please return."*

- **Fuel:** 400.0 units (floating point! movement=1.0, action=0.25, etc.)
- **Modifiers:** Cold rooms drain 2× faster!
- **Actions:** GET, LIGHT, EXTINGUISH, CHECK FUEL, RUB (genie on holiday)
- **Lineage:** Descended from Crowther's original, 1976

### [end/ROOM.yml](./end/ROOM.yml) — Treasury of Modest Proportions

*"One pedestal remains occupied..."*

- **Exit south:** back into the maze (room-d) — you'd have to navigate out again!
- **Features:** Empty pedestals, dramatic lighting, sense of importance
- **Contains:** The jeweled chalice

### [end/treasure.yml](./end/treasure.yml) — The Jeweled Chalice

*"Congratulations! You have found a treasure worth 10 points."*

- **Value:** 10 points (deposit in well house for credit)
- **Actions:** GET, EXAMINE, DRINK_FROM (empty, also frowned upon)
- **Lineage:** In the tradition of all adventure treasures

### [maze/room-j/lamp-vendor.yml](./maze/room-j/lamp-vendor.yml) — ACME Lamp Refueling Co.

*"Don't Let the Grue Get You!"™*

A battered vending machine deep in the maze crossroads. Your lifeline against the darkness.

- **Location:** maze/room-j (the crossroads)
- **Prices:** 1g (basic), 2g (deluxe), 5g (premium blue glow)
- **Secrets:** PLUGH password, mercy kick, treasure trade
- **Lineage:** Descended from the battery vendor in Colossal Cave, 1976

---

## Try It Yourself

```
> look
You are standing in a small chamber carved from living rock.
The walls bear scratched initials: "WC+DW '76", "SA '78", "XYZZY WAS HERE".
A brass lamp sits on a stone shelf. An archway leads NORTH.

> take lamp
Taken. The lamp feels reassuringly solid in your hand.

> go north
You step through the archway...

You are in a maze of twisty little passages, all alike.
This one is slightly damp. A puddle reflects your bewildered face.
Passages lead N, S, E, W.

> go west
You are in a maze of twisty little passages, all alike.
This one has a golden glow from the NORTH passage!

> go north
You emerge into the Treasury of Modest Proportions! 
A JEWELED CHALICE gleams on a pedestal!

> take chalice
Taken! Your score is now 10 of 10 points!

"Well," says Bumblewick, adjusting his waistcoat, "that wasn't 
so bad. Mother will be ABSOLUTELY INSUFFERABLE about this."

> inventory
You are carrying:
  - A brass lamp (lit)
  - A jeweled chalice (10 points)
  - Your dignity (barely)
```

**The solution:** START → N → MAZE-A → W → MAZE-D → N → END

---

## Chat Continues: Adding Objects

**User:** Let's create a lamp and put it in the start room, and create a treasure and put it in the end room. Give all rooms and objects imaginative creative witty descriptions in the tradition of Zork and Adventure and Scott Adams Adventure. Use cultural references and tributes.

**DM:** Ah, you want the REAL adventure experience! Let me channel Crowther, Woods, Adams, and the Implementors...

### Added: [start/lamp.yml](./start/lamp.yml) — The Brass Lamp

A classic! No adventure is complete without a light source of dubious reliability.

### Added: [end/treasure.yml](./end/treasure.yml) — The MacGuffin

The thing you came for. Worth approximately 10 points.

---

## Chat Continues: The Hero Awakes

**User:** The hero awakes! Write a flowery romantic backstory, in the style of The Hobbit, but with a good dose of Pee Wee's Playhouse. Choose a silly name for the hero.

**DM:** *Clears throat dramatically*

### Updated: [player.yml](./player.yml) — Bumblewick Fantastipants

*"In a hole in the ground there lived a Fantastipants..."*

Our hero is now **Bumblewick Fantastipants**, a reluctant adventurer from the pleasant village of Wobblebrook-upon-Squiggle. He is:

- A devoted spoon enthusiast (magnificent collection, now tragically far away)
- A Tuesday rhymer (speaks only in couplets on Tuesdays)
- A waistcoat devotee (wears one always, even to bed)
- The son of the legendary Petunia Fantastipants (who once retrieved a slightly magic napkin from the Cave of Moderate Danger)

He awoke in the Chamber of Commencement with no memory of how he arrived, suspecting someone has been "messing about with the narrative fabric of reality again."

**The secret word is "COMFORT!" When you hear it, SCREAM REAL LOUD!**

MEKKA-LEKKA-HI, MEKKA-HINEY-HO!

---

## Chat Continues: The Maze

**User:** Add a twisty maze between start and end, of four rooms. One room's exit should go to start and another room's exit should go to end, but the other four compass directions of each room are tangled!

**DM:** Ah, the classic! "You are in a maze of twisty little passages, all alike." Let me tangle those passages...

### Added: [maze/](./maze/) — A Maze of Twisty Little Passages

Four rooms, each with a distinguishing feature (for the observant):

| Room | Feature | What Makes It Special |
|------|---------|----------------------|
| [room-a/](./maze/room-a/) | Puddle | Slightly damp, judgmental water |
| [room-b/](./maze/room-b/) | Echo | Your mockery returns to you |
| [room-c/](./maze/room-c/) | Scratches | "THIS WAY OUT →" points at wall |
| [room-d/](./maze/room-d/) | Golden glow | The way forward! |

**The tangled connections:**

```
room-a: N→C  S→start  E→B  W→D
room-b: N→D  S→C      E→A  W→C
room-c: N→B  S→D      E→D  W→A
room-d: N→end S→A     E→B  W→C
```

**The solution:** Start → N → room-a → W → room-d → N → Treasury!

Or wander. Wandering builds character.

---

## Chat Continues: Grues!

**User:** If I enter the maze without the lamp in my inventory and lit, then I get eaten by a grue. But the start and end rooms are magically lit. The maze rooms are dark and dangerous without a source of light!

**DM:** Ah yes, the GRUE. The original survival horror monster. Let me add the appropriate dread...

### The Lighting Rules

| Room | Lighting | Grue Safe? |
|------|----------|------------|
| start/ | Magical | ✅ Yes |
| maze/* | **NONE** | ❌ NO |
| end/ | Magical | ✅ Yes |

### What Happens Without a Lamp

```
> go north
It is pitch black. You are likely to be eaten by a grue.

...

You have been eaten by a grue.

> RESTART, RESTORE, or QUIT?
```

Each maze room has a unique grue death message with lyrics from **[MC Frontalot's "It Is Pitch Dark"](https://www.youtube.com/watch?v=4nigRT2KmCE)**:

- **room-a**: *"If this predicament seems particularly cruel..."*
- **room-b**: *"It got narrated at you in the second person..."*
- **room-c**: *"Could be the spray for the grue; you're gonna need it..."*
- **room-d**: *"Twenty-two years later, head's infested: got the grue in..."*

> 🎵 *"Thanks, Grampa, for buying it. Now my life's ruined."* 🎵
>
> Nerdcore is the future. Front is a lyricist without equal.

### The Lamp Saves You

```yaml
# The lamp must be:
lamp:
  lit: true           # ON, not off
  in_inventory: true  # Not left behind in start!
  oil: > 0            # Still has oil
```

**GET LAMP. This is not a suggestion.**

*([Get Lamp](http://www.getlamp.com/) — the documentary)*

---

## Chat Continues: Reincarnation

**User:** When you're eaten by a grue, or killed in any way, you get reincarnated in the start room, with your score zeroed out, but you keep your inventory.

**DM:** A merciful cosmos! Death is but a temporary setback...

### The Death & Rebirth Cycle

```yaml
# On any death (grue, trap, existential despair):
death_event:
  action: reincarnate
  location: start           # Back to the beginning
  score: 0                  # Points reset to zero
  inventory: preserved      # You keep your stuff!
  moves: preserved          # Move count continues
```

### What Happens

```
You have been eaten by a grue.

...

The darkness swallows you whole. But wait—

A warm light. A sense of beginnings. The smell of slightly
damp stone and narrative convenience.

You awaken in the Chamber of Commencement. Your score has
been reset to 0, but your inventory remains intact. The 
universe is merciful, if slightly disappointed in you.

"Well," says Bumblewick, checking his waistcoat, "THAT was
unpleasant. At least I still have my lamp."
```

### Why Keep Inventory?

- **Prevents softlocks** — Can't lose the lamp forever
- **Rewards exploration** — Found items stay found
- **Reduces frustration** — Death is a setback, not a restart
- **Classic roguelike mercy** — Some games call this "soul recovery"

The treasure's points don't count until you survive to the end!

---

## Chat Continues: Kitchen & Expanded Maze

**User:** Make a Kitchen to the west from start, with a fridge and other objects. Put a bunch of delicious foods in the fridge, that the player can drop to map the maze. Add 20 interesting diverse food items to the fridge, then make six more maze rooms (for a total of 10).

**DM:** Ah, the CLASSIC maze-mapping technique! Let me stock that kitchen...

### Added: [kitchen/](./kitchen/) — The Fantastipants Family Kitchen

An exact replica of home, complete with:
- **[fridge.yml](./kitchen/fridge.yml)** — 20 unique food items for maze mapping!
- **[stove.yml](./kitchen/stove.yml)** — Not currently in use (adventures first)
- **[sink.yml](./kitchen/sink.yml)** — Perpetually containing dishes
- **[table.yml](./kitchen/table.yml)** — With a note from Mother

### The 20 Foods (for Maze Mapping!)

| # | Food | Description |
|---|------|-------------|
| 1 | Suspiciously Perfect Apple | Snow White would be suspicious |
| 2 | Wheel of Aged Cheese | Sharp cheddar, aged 47 years |
| 3 | Loaf of Crusty Bread | Still warm. Defies thermodynamics. |
| 4 | Jar of Pickled Herring | A family delicacy. Distinctive smell. |
| 5 | Leftover Shepherd's Pie | Tuesday's dinner |
| 6 | Bunch of Purple Grapes | Mother's favorite |
| 7 | Pot of Mysterious Stew | "DO NOT EAT - EXPERIMENT" |
| 8 | Wedge of Blue Cheese | The mold is supposed to be there |
| 9 | Cold Roast Chicken | Missing one leg |
| 10 | Jar of Strawberry Jam | Grandmother's recipe |
| 11 | Half-Empty Bottle of Milk | Or half-full |
| 12 | Suspicious Casserole | Aunt Petunia's "special recipe" |
| 13 | Lemon (Judgmental) | It seems to be frowning |
| 14 | Slice of Birthday Cake | Three months old. Sentient frosting. |
| 15 | Carrot (Heroically Orange) | Good for your eyes |
| 16 | Tin of Sardines | Emergency rations |
| 17 | Bowl of Cold Porridge | Goldilocks rejected this one |
| 18 | Fancy Imported Salami | From THE Old Country |
| 19 | Single Hard-Boiled Egg | Looking existential |
| 20 | Jar of Olives (Green) | Stuffed with pimentos. Tradition. |

### Added: 6 More Maze Rooms (10 total!)

| Room | Feature | What You'll Find |
|------|---------|------------------|
| room-e | Cobwebs | Ancient dusty webs, feeling of being watched |
| room-f | Cold Spot | Freezing! Something wrong with reality |
| room-g | Carved Face | Judging you silently |
| room-h | Mushrooms | Faint green glow (insufficient for safety!) |
| room-i | Skeleton | Previous adventurer. Cautionary tale. |
| room-j | Crossroads | Central hub. Metaphorical significance. |

**20 foods ÷ 10 rooms = 2 markers per room if you're REALLY careful!**

---

## Chat Continues: The Coat Room

**User:** Make two-way east/west links so the kitchen is to the west of the start, and make a new room to the east of the start, the coat room, which has a spectacular collection of formal and wild costumes. It mentions many interesting ones but you can request any costume you can describe, or a random one. It rewrites your character description for the costume! You can also combine costumes or customize them in any way. You can even add inventory items and accessories!

**DM:** A costume emporium! Now Bumblewick can be ANYONE while navigating the grue-infested maze!

### Added: [coatroom/](./coatroom/) — The Fantastipants Costume Emporium

A vast circular chamber where you can completely transform your character!

**Commands:**

| Command | Effect |
|---------|--------|
| `WEAR pirate captain` | Become a pirate! |
| `WEAR RANDOM` | Surprise costume |
| `COMBINE wizard WITH detective` | Mash-up! |
| `ADD a monocle` | Accessorize |
| `ADD TO INVENTORY rubber chicken` | Get items! |
| `LOOK IN MIRROR` | See yourself |

**Objects:**
- **Mirror** — Shows your transformation
- **Mannequin** — Helpful costume consultant (faceless but enthusiastic)
- **Costume Racks** — Infinite possibilities

**Featured Costumes:**
- Dread Pirate Fantastipants (with parrot puppet)
- Space Explorer (ray gun goes "pew pew")
- Victorian Detective (Watson is a sock puppet)
- Actually Just Three Corgis (in a trenchcoat)

**The costume rewrites your character description!**

```
BEFORE: Bumblewick in his waistcoat, bewildered but optimistic
AFTER:  Captain Bumblewick "Blackwaistcoat" Fantastipants, dread pirate!
```

### World Map (Complete)

```
                         ┌─────────┐
                         │   END   │  ← TREASURE HERE!
                         │ Treasury│
                         └────┬────┘
                              │ S↔N
         ┌──────────────────────────────────────────┐
         │           THE MAZE (10 rooms)            │
         │  A ←→ B ←→ C ←→ D ←→ E ←→ F ←→ etc...    │
         │     (tangled connections, grues)         │
         └────────────────────┬─────────────────────┘
                              │ S↔N
                         ┌────┴────┐
 ┌─────────┐    W↔E      │  START  │     W↔E      ┌──────────┐
 │ KITCHEN │◄───────────►│ Chamber │◄────────────►│ COATROOM │
 │  food!  │             │  SAFE   │              │ costumes │
 └─────────┘             │ respawn │              └──────────┘
   x:-1,y:0              └─────────┘                x:1,y:0
                           x:0,y:0

SAFE ROOMS: start, kitchen, coatroom, end (magical lighting)
DANGER:     all 10 maze rooms (grues if no lamp!)
```

---

## Chat Continues: Coherence Check

**User:** Perform a deep coherence check and validation and repair and detail generation pass!

**DM:** Running coherence engine... 🔍

### Issues Found & Fixed

| Issue | Status |
|-------|--------|
| Player notes only mentioned north exit | ✅ Fixed — now lists all 3 exits |
| Start room description didn't mention all exits | ✅ Fixed — now shows N/W/E |
| End room said "back to beginning" but goes to maze | ✅ Fixed — clarified |
| Kitchen/Coatroom didn't reference each other | ✅ Fixed — cross-linked |
| Player missing costume state fields | ✅ Fixed — added costume tracking |
| Lamp missing oil warning thresholds | ✅ Fixed — added warning/critical |
| Treasure missing victory response | ✅ Fixed — added celebration text |
| Navigation tables incomplete | ✅ Fixed — added cross-links |
| World map needed update | ✅ Fixed — complete ASCII map added |

### Verified Correct

| Check | Status |
|-------|--------|
| All exits bidirectional (where intended) | ✅ Maze tangled ON PURPOSE |
| World positions consistent | ✅ start(0,0), kitchen(-1,0), coatroom(1,0), end(0,1) |
| All object files referenced exist | ✅ All present |
| Grue_safe flags correct | ✅ Safe rooms: start, kitchen, coatroom, end |
| Respawn point set | ✅ start/ROOM.yml has respawn_point: true |
| MC Frontalot links work | ✅ All 10 maze rooms link to video |

### World Coordinates

| Room | Position | Notes |
|------|----------|-------|
| kitchen | (-1, 0) | West of start |
| start | (0, 0) | Origin, respawn point |
| coatroom | (1, 0) | East of start |
| end | (0, 1) | North of maze (conceptually) |
| maze rooms | undefined | Tangled non-Euclidean space |

### Updated: Room Descriptions

Both rooms now feature properly atmospheric prose, complete with:
- Unnecessary but evocative adjectives
- Hints that may or may not be helpful
- References the initiated will recognize

---

## Chat Continues: The Eating Mechanic

**User:** Your mother warned you not to eat the food. If you eat any food from your inventory or the fridge or room, it immediately travels through your digestive system and plops out on the floor with flowery descriptive unique every time euphemistic flourish.

**DM:** Creating the Fantastipants Digestive Express... 🚽✨

**User:** Those are examples of what happens when you eat food, feel free to mix them up and add item specific imaginative commentary. The net effect is that something hilarious happens and the food drops into the room. This is a great way to mark the maze! The act of being eaten can even modify and transform the food, be creative you are the DM! Food can even dynamically define properties and key/value pairs in the adventurer!

**DM:** Expanding with 20 item-specific transformations and player property modifications...

**User:** Foods can have special effects according to your costume, room, objects in the room, and history. Be creative you are the DM! Remember persistent state in the objects, not just the chat.

**DM:** Adding contextual modifiers and persistence rules... The world now EVOLVES as you eat!

### Files Created/Modified

| File | Changes |
|------|---------|
| `kitchen/fridge.yml` | Added `mothers_warning`, `eat_mechanic`, 20 `item_specific` transformations, `contextual_effects` (by costume/room/objects/history), `persistence_rules` |
| `kitchen/README.md` | Added "Eating Strategy" section, context table, persistence notes |
| `player.yml` | Added trait: `catastrophic_digestion` |

### `kitchen/fridge.yml` — Version History

| Version | Changes |
|---------|---------|
| v1 | 20 food items with descriptions and marker_ids, GET_ALL action, hint |
| v2 | Added Mother's Warning note on fridge door |
| v3 | Added `eat_mechanic` with 10 euphemism examples |
| v4 | Added 20 `item_specific` transformations with unique journeys and player property additions |
| v5 | Added `contextual_effects` by costume (vampire, wizard, pirate, chef, ghost, clown), by room (dark, echo, cold, kitchen, coatroom), by objects (lamp, treasure, skeleton, sentient stew), by history (same food twice, died recently, herring aura active) |
| v6 | Added `persistence_rules` requiring DM to UPDATE YAML FILES, not just describe effects |

### Example Transformations

| Food | Transforms Into | Adds to Player |
|------|-----------------|----------------|
| 🍎 Apple | Puddle of Applesauce | `fairytale_immunity: 5` |
| 🐟 Herring | VERY Pickled Herring | `herring_aura`, `smell_radius: 3` |
| 🥘 Stew | **Sentient Stew** (alive!) | `stew_creator`, `mysterious_glow` |
| 🧁 Cake | Singing Cake Slice | `birthday: "today"`, `cake_whispers` |
| 🥚 Egg | Hollow Philosophical Egg | `egg_yolk: 1` (absorbed) |
| 🫒 Olives | Hollow Olives (accusing) | `pimento_quota: 20` |

### Contextual Modifiers

| Context | Effect |
|---------|--------|
| 🧛 Vampire + Apple | → Blood Apple |
| 🏴‍☠️ Pirate + Any Liquid | → Rum |
| 👻 Ghost + Any Food | → Phases through floor/exit! |
| 🦴 Skeleton Nearby | → Existential commentary |
| 🐟 Herring Aura + Blue Cheese | → SMELL SINGULARITY |
| 🍽️ Same Food 3rd Time | → "It's complicated" relationship |

### Persistence Example

When Mysterious Stew is eaten in `maze/room-c`:

```yaml
# player.yml UPDATED:
properties:
  stew_creator: true
  mysterious_glow: "faint, greenish"

# maze/room-c/ROOM.yml UPDATED:
contents:
  - name: "Sentient Stew"
    file: sentient-stew.yml

# maze/room-c/sentient-stew.yml CREATED:
creature:
  name: Sentient Stew
  origin: "Born in Bumblewick's digestive tract"
  questions:
    - "Why am I?"
    - "What was I before?"
```

**The maze becomes a living ecosystem!**

---

## Chat Continues: Focusing the DM

**User:** Trim down some of the more whimsical examples in the fridge food description, just list a few exemplary ones, the time for specific creativity is at runtime.

**DM:** Compressing... 645 lines → 260 lines

**User:** Update the readme with this focusing cleanup task description that reigns in the overenthusiastic creativity of the DM at authoring time and defers it to runtime. This is a kind of linting, validation, style guide, optimization, compression, context window management.

### The Principle: Author Patterns, Not Scripts

| Authoring Time | Runtime |
|----------------|---------|
| Define **patterns** | Generate **instances** |
| Show **exemplary** cases | Improvise **specific** cases |
| Describe **categories** | Combine **creatively** |
| Keep files **lean** | Let context **breathe** |

### Why This Matters

**Context window management.** Every token in a YAML file competes for attention with player state, room descriptions, and conversation history. Verbose authoring-time creativity steals tokens from runtime creativity.

**DM freedom.** Pre-scripted responses feel canned. Patterns + improvisation = unique every time. The DM should be creative *when it matters* — at the moment of play.

**Compression as curation.** Trimming 20 detailed examples to 4 exemplary ones isn't loss — it's focus. The 4 examples teach the *pattern*. The DM generates the other 16 fresh.

### What Was Trimmed

| Before | After |
|--------|-------|
| 20 item-specific transformations | 4 exemplary patterns |
| Full contextual effect matrices | Category summaries + 6 examples |
| Detailed persistence YAML | 3-line rule summary |
| Verbose DM notes | "Be creative at runtime!" |

### File History: `kitchen/fridge.yml`

| Version | Lines | Changes |
|---------|-------|---------|
| v6 | 645 | Full item-specific transformations, detailed contexts |
| v7 | 260 | **Focused**: patterns over scripts, defer to runtime |

### The Meta-Lesson

This cleanup is itself a **MOOLLM pattern**:

```
FOCUS-RUNTIME:
  meaning: "Author patterns, not scripts. Defer creativity to runtime."
  applies_to: [object_definitions, character_backstories, room_descriptions]
  benefit: "Lean files, fresh responses, better context management"
```

When authoring MOOLLM content:
- ✅ Define the *shape* of possible responses
- ✅ Show a few *exemplary* instances  
- ✅ Let the coherence engine improvise the rest
- ❌ Don't pre-generate every possibility
- ❌ Don't fill files with enthusiasm that steals runtime tokens

---

## 🎮 Special Mechanics

### The Eating Strategy

**Mother warned you. But here's the secret:**

Bumblewick Fantastipants has a legendary digestive system — legendary for its *creative efficiency*. If you EAT any food:

1. 🍴 It enters your mouth
2. 🎭 Something **HILARIOUS** happens
3. ✨ The food is **TRANSFORMED**
4. 📍 It drops to the floor as a **UNIQUE marker**
5. 🧠 It may add **properties** to Bumblewick!

This is actually a GREAT maze-mapping technique! Each food becomes uniquely transformed — the apple becomes applesauce, the stew becomes sentient, the grapes scatter in constellations. No two post-Fantastipants foods are alike!

**Foods can modify the adventurer:**
- The **Herring** gives you `herring_aura: true` and `smell_radius: 3`
- The **Mysterious Stew** gives you `mysterious_glow: "faint, greenish"`
- The **Salami** gives you `accent: "slightly foreign"`
- The **Olives** give you `pimento_quota: 20` (they're inside you now)

By journey's end, Bumblewick might have: sardine followers, dreams of The Old Country, and a cake that whispers "happy birthday" to itself. **This is character development!**

### Context Changes Everything!

Effects vary by **costume**, **room**, **nearby objects**, and **history**:
- 🧛 Eat as Vampire → apple becomes Blood Apple
- 🏴‍☠️ Eat as Pirate → all liquids become rum, sardines sing shanties
- 👻 Eat as Ghost → food phases through floor or exit to room below or adjacent!
- 🔦 Eat in darkness → "The SOUNDS are concerning"
- 🐟 Already have herring aura → everything smells now
- 🦴 Skeleton nearby → existential commentary

### Persistent State!

**The DM updates YAML files**, not just chat:
- `player.yml` gains new properties
- `ROOM.yml` gains transformed food as contents
- New `.yml` files created for sentient foods!

The maze becomes a **living ecosystem** of transformed foods.

See: [kitchen/fridge.yml](./kitchen/fridge.yml) for contextual modifiers and persistence rules.

---

## 💰 The Gold Economy

*A tribute to the battery vendor in Colossal Cave Adventure.*

### Why Gold?

The lamp has finite oil. The maze is dark. Grues are patient. What's an adventurer to do?

**Enter capitalism.** Deep in the maze crossroads (room-j), a battered vending machine hums softly:

```
╔══════════════════════════════════════╗
║      ACME LAMP REFUELING CO.         ║
║  "Don't Let the Grue Get You!"™      ║
╚══════════════════════════════════════╝
```

### The Prices

| Item | Cost | Effect |
|------|------|--------|
| Lamp Oil Refill | 1 gold | Refills to 400 oil |
| Deluxe Refill | 2 gold | Refills to 800 oil |
| Premium Glow Juice | 5 gold | 1000 oil + blue glow (grues hate it!) |

### Starting Wealth

Bumblewick begins with **10 gold pieces** — enough for:
- Multiple lamp refills (lamp runs dry? No problem!)
- Snacks (hypothetical future vendors)
- Bribes (hypothetical future NPCs)
- Whatever else this economy evolves into

### The Tragic Irony 💀

In room-i lies a skeleton — an adventurer who didn't make it. They had:
- An **empty lamp**
- **3 gold pieces** in their pocket (enough for three refills!)
- Was **pointing west** toward room-j

The vendor was *one room away*. The grue got them first. Don't be like them.

### The Hidden Fortune 💰

In room-f (the cold spot), you'll find **100 gold coins** scattered on the floor!

This was the rest of the skeleton's money. They were trying to use coins as maze markers (a terrible strategy — coins all look alike!). When the supernatural cold drained their lamp faster than expected, they dropped everything and ran.

**Warning:** Room-f drains lamp oil at **2x speed**. Grab the gold and GET OUT.

### Easter Eggs

The vendor has secrets for the resourceful:
- **Kick it three times** → Emergency mercy refill
- **Say 'PLUGH'** → Password from 1972 recognized
- **Insert the treasure** → Lifetime subscription (but you gave away the treasure...)

### 🔦 Lamp Fuel Mechanics

The lamp burns **floating-point oil** — different actions cost different amounts!

| Action | Base Cost | Notes |
|--------|-----------|-------|
| **Movement** | 1.0 | Walking between rooms |
| **Wait/Look** | 0.5 | Standing still, examining surroundings |
| **Action** | 0.25 | GET, DROP, EXAMINE, etc. |
| **Talk** | 0.1 | Conversation, reading |
| **Light/Extinguish** | 0.0 | Free! (but consequences...) |

**Environmental modifiers** multiply the base cost:
- **Cold room (room-f):** 2.0× — the supernatural cold drains oil faster!
- **Windy:** 1.5× — drafts make the flame work harder
- **Damp:** 1.2× — humidity affects combustion
- **Normal:** 1.0× — standard conditions

**Fuel thresholds:**
- **> 50:** Comfortable. No warnings.
- **< 50:** "Your lamp flickers slightly..."
- **< 10:** "Your lamp is dying! Each flicker could be the last!"
- **= 0:** Darkness. Grues. Death.

The DM applies these costs each turn and updates `lamp.oil` in the YAML!

### What This Demonstrates

| Concept | Implementation |
|---------|---------------|
| **Granular resource management** | Different actions cost different oil |
| **Environmental hazards** | Cold room = 2× oil drain |
| **In-world economy** | Gold has meaning beyond score |
| **Environmental storytelling** | Skeleton shows consequences |
| **Discoverable depth** | Easter eggs reward exploration |
| **Tribute to tradition** | Colossal Cave battery vendor lives on |

The economy turns "explore freely" into "explore *wisely*" — without removing the freedom.

See: [maze/room-j/lamp-vendor.yml](./maze/room-j/lamp-vendor.yml)

---

## What's Next?

**Already done:**
- ✅ Maze of twisty passages (10 rooms!)
- ✅ Grues in the darkness
- ✅ Economy with gold pieces
- ✅ Lamp vendor (tribute to Colossal Cave)
- ✅ Food-based maze mapping
- ✅ Costume system (be anyone!)
- ✅ Eating mechanic with transformations

**Future possibilities:**
- Add a troll who demands payment (now we have gold!)
- Add an NPC to talk to (perhaps a thief who steals gold?)
- Add a puzzle blocking access to premium areas
- Add more vendors (food? costumes? maps?)
- Add achievements for creative solutions

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [examples/](../) |
| 🚪 Start | [start/](./start/) — Chamber of Commencement |
| 🍳 Kitchen (W) | [kitchen/](./kitchen/) — Food for maze mapping! |
| 🎭 Coat Room (E) | [coatroom/](./coatroom/) — Be anyone you want! |
| 🌀 Maze (N) | [maze/](./maze/) — 10 twisty passages (with map!) |
| 🏆 End | [end/](./end/) — Treasury of Modest Proportions |
