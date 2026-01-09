# The Coat Room

> *"Be anyone you want!"*
> — The Fantastipants Costume Emporium

A vast circular chamber of infinite costume possibilities. Transform your **appearance** AND your **personality**!

**Inspired by The Sims' Create-a-Sim screen** — and appropriately located right near the entrance! Just like starting a new Sims game, you can customize your character before the adventure begins. Change your appearance, add accessories, mix and match personas. The adventure awaits, but first: *who do you want to be?*

**The Mind Mirror** — Based on Timothy Leary's 1985 software, the ornate mirror in the center doesn't just show your costume — it shows your SOUL. View, edit, and try on personalities as easily as clothes. Natural language interface. No sliders. Just **talk to the mirror**.

**Also an NPC factory!** Generate new characters, dress them up, accessorize them, give them personality profiles, and dispatch them into the world. Need a rival adventurer? A helpful guide? A suspicious merchant? Create them here, costume them, mind-mirror them, and send them off to populate your adventure.

---

## How It Works

The coat room rewrites your **entire identity** — name, pronouns, backstory, costume. All changes persist in your character directory (`characters/abstract/player/`) throughout the adventure!

This isn't just dress-up. It's **becoming who you want to be**.

### Commands

| Command | Effect |
|---------|--------|
| `WEAR [description]` | Become that costume! |
| `WEAR RANDOM` | Surprise costume! |
| `COMBINE [a] WITH [b]` | Mash-up two costumes! |
| `ADD [accessory]` | Add to current costume |
| `ADD TO INVENTORY [item]` | Get a costume-appropriate item |
| `REMOVE COSTUME` | Back to default appearance |
| `LOOK IN MIRROR` | See your current appearance |
| `CHANGE NAME [name]` | Choose a new name |
| `CHANGE PRONOUNS [pronouns]` | Set your pronouns (they/he/she/it/any/fluid) |
| `REWRITE BACKSTORY` | Tell or invent your story (interactive) |
| `FULL TRANSFORMATION` | Name + pronouns + backstory + costume — become anyone |
| `SAVE LOOK [name]` | Save current identity as a card in this room |
| `LOAD LOOK [name]` | Restore a previously saved identity |
| `COMPOSE LOOKS [a] WITH [b]` | Mix elements from different saved identities |
| `SHARE LOOK [name]` | Copy a look to another room or character |

### Mind Mirror Commands

| Command | Effect |
|---------|--------|
| `MIND-MIRROR` | See your full psychological profile |
| `EDIT-MIND [request]` | Adjust personality naturally ("make me braver") |
| `GENERATE-MIND FOR [description]` | LLM creates a profile for any character |
| `WEAR-MIND` | Adopt the generated/edited personality |
| `RANDOM-MIND` | Generate completely random personality |
| `COMPARE-MINDS [a] WITH [b]` | Side-by-side comparison |
| `SAVE-MIND` | Save personality as a card |
| `RESTORE-MIND` | Return to original personality |
| `VOCABULARY-MODE` | Toggle Plain Talk / Shrink-Rap |

### Identity Commands

| Command | Effect |
|---------|--------|
| `DESCRIBE-ME` | See ALL your data in narrative + table form |
| `CHANGE-MY-FILE-NAME [name]` | Rename your character file (stays in `characters/`) |
| `CHANGE-MY-NAME [name]` | Change your character name |

**DESCRIBE-ME** shows everything:
- Your file path (e.g., `characters/abstract/player/CHARACTER.yml`)
- Character name, persona, costume
- Full Mind Mirror profile (Sims traits + Leary planes)  
- Current needs, wants, aspirations
- Inventory, relationships, gold, score, effects

**CHANGE-MY-FILE-NAME** is fundamental:
- In MOOLLM, you ARE your file. The filesystem IS the world.
- Renames your character directory within the appropriate category
- Cannot overwrite existing character files
- Characters are organized by type: abstract/, fictional/, real-people/, animals/, robots/

---

## Examples

**Simple:**
```
> WEAR pirate captain

You are now Captain Bumblewick "Blackwaistcoat" Fantastipants!
Tricorn hat, brass buttons, foam cutlass, and a parrot puppet
that squawks unconvincingly.
```

**Combination:**
```
> COMBINE astronaut WITH Victorian gentleman

You emerge as Space Explorer Sir Bumblewick Fantastipants III,
in a silver spacesuit with a top hat sealed to the helmet and
a monocle painted on the visor.
```

**Custom:**
```
> WEAR a sentient cloud of bees wearing a tiny crown

The mannequin nods approvingly. Somehow, this exists.
You are now... The Bee Emperor. Buzz buzz.
```

**Add accessories:**
```
> ADD a jetpack

Your costume now includes a jetpack! (Decorative only. 
Or is it? Try pressing the button in the maze...)

> ADD TO INVENTORY rubber chicken

You now have: Rubber Chicken (squeaks when squeezed)
```

**Mind Mirror - edit personality:**
```
> MIND-MIRROR

The mirror shows four circular diagrams — your SOUL mapped:
  BIO-ENERGY: Energetic (5), Cheerful (4), Restless (3)...
  EMOTIONAL: Confident (3), Friendly (5), Proud (4)...
  MENTAL: Creative (6), Well-Informed (4), Impractical (5)...
  SOCIAL: Uninhibited (4), Worldly (3), Respectable (5)...

> EDIT-MIND make me more confident and less cautious

The mirror ripples... Your profile shifts:
  confident: 3 → 5
  cautious: 5 → 3
  
You feel different. Bolder. Ready.
```

**Mind Mirror - generate for character:**
```
> GENERATE-MIND FOR a confident space pirate

The mirror swirls with starlight and saltwater...

  BIO-ENERGY: Energetic (6), Easy-Going (5), Restless (6)
  EMOTIONAL: Forceful (6), Confident (7), Proud (5)
  MENTAL: Innovative (5), Impractical (4), Creative (5)
  SOCIAL: Uninhibited (7), Uncultured (5), Worldly (6)
  
"A bold one, this profile. WEAR-MIND to become this."

> WEAR-MIND

You step into the mirror... or it steps into you.
Your soul has a new shape. Arr.
```

---

## Featured Costumes

| Costume | Description |
|---------|-------------|
| **Dread Pirate** | Tricorn hat, cutlass, parrot puppet |
| **Space Explorer** | Silver suit, ray gun, bubble helmet |
| **Detective** | Upgraded waistcoat, deerstalker, magnifying glass |
| **Three Corgis** | Trenchcoat, tiny hat, surprisingly convincing |

---

## Categories Available

- **Historical**: Roman, Egyptian, Victorian, 1920s...
- **Fantastical**: Wizard, fairy, dragon, superhero...
- **Professional**: Chef, astronaut, detective, scientist...
- **Theatrical**: Harlequin, Phantom, Shakespeare...
- **Absurdist**: Banana, hotdog, "concept of time"...
- **Custom**: If you can describe it, you can wear it!

---

## Personas — Wearable Personality Overlays

See [../personas/](../personas/) for **wearable personas** that modify your character!

A persona is NOT a character — it's a **mask** that changes whoever wears it:

| Aspect | Your Character | The Persona |
|--------|----------------|-------------|
| **What** | Who you ARE | Who you're PLAYING |
| **Contains** | Full traits | Trait MODIFIERS (+/-) |
| **Permanent** | Yes | No — put on, take off |
| **Location** | Has a room | No location (shared!) |

```yaml
# In your character file:
current_persona: personas/captain-ashford.yml

# Or in the coatroom:
> WEAR PERSONA captain-ashford
> DON captain-ashford
> REMOVE PERSONA
```

**Don Hopkins** wearing Captain Ashford is a different Ashford than **Bumblewick** wearing Ashford. Your base personality shows through!

| Persona | Style |
|---------|-------|
| [captain-ashford.yml](../personas/captain-ashford.yml) | Belter space pirate |

**Why personas live at adventure level (not in rooms):**
- Multiple characters can wear the same persona simultaneously
- Personas have no physical location
- Characters reference personas by path

---

## Saved Looks — Identities as Cards

Save any identity as a **playable card** in this room!

```
coatroom/
  captain-swagger-look.yml    # The saved identity
  captain-swagger-look.svg    # LLM-generated portrait
  space-disco-look.yml        # Another saved look
  space-disco-look.md         # Backstory notes
```

**Cards can be:**
- **Loaded** — instantly become that persona
- **Composed** — mix elements from multiple looks
- **Shared** — give to NPCs or copy to other rooms
- **Visualized** — LLM generates portraits, fashion illustrations

```
> COMPOSE LOOKS captain-swagger WITH space-disco

Maurice proposes: "Space Pirate Swagger" — holographic eyepatch,
robot parrot, coat with star maps in the lining.

[ACCEPT] [MODIFY] [TRY DIFFERENT MIX]
```

---

## The Objects

| Object | What It Does |
|--------|--------------|
| **[mirror.yml](./mirror.yml)** | Mind Mirror — shows appearance AND personality |
| **[mannequin.yml](./mannequin.yml)** | Maurice — helps you transform |
| **[costume-racks.yml](./costume-racks.yml)** | The infinite collection |
| **[*-look.yml](.)** | Saved identities (cards you create) |

---

## Why Costumes?

- **Roleplay differently** through the adventure
- **Get into character** for puzzles and challenges
- **Add inventory items** that match your persona
- **Learn skills!** Using the costume racks teaches `costume-combining`, costumes come with skills
- **Drag performance art!** Become someone fabulous. Work it. Take a strut in my shoes.
- **Have fun!** The maze is scary. Costumes are fun.

## Skills You Can Learn Here

Interacting with objects in the coatroom can teach persistent skills:

| Interaction | Skill Learned | Carries To |
|-------------|---------------|------------|
| `COMBINE` costumes | `costume-combining` | Any room with costumes |
| `WEAR RANDOM` repeatedly | `style-improvisation` | Social encounters |
| Help the mannequin | `fashion-consulting` | NPC interactions |
| `ADD TO INVENTORY` | `accessorizing` | Equipment management |
| `MIND-MIRROR` | `self-awareness` | All NPC interactions |
| `EDIT-MIND` | `personality-crafting` | Character creation |
| `GENERATE-MIND FOR` | `psychological-profiling` | NPC analysis |
| `COMPARE-MINDS` | `empathy` | Understanding others |

These skills persist in your character file and travel with you!

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| 🚪 **West** | [start/](../start/) — Chamber of Commencement |
| 🧬 **North** | [characters/](../characters/) — Hall of Bodies |
| 🎭 **South** | [personas/](../personas/) — Wardrobe of Masks |
| 📚 **East** | [skills/](../skills/) — Skill Nexus |
| 🍳 (via start, west) | [kitchen/](../kitchen/) — Food for maze mapping |
| 🌀 (via start, north) | [maze/](../maze/) — The grue-infested maze |
