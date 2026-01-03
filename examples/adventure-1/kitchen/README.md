# The Kitchen

> *"The food is for DROPPING IN THE MAZE, not for EATING."*
> — Petunia Fantastipants

An exact replica of the Fantastipants family kitchen from Wobblebrook-upon-Squiggle, mysteriously recreated underground. How thoughtful! And slightly creepy!

---

## Why a Kitchen?

**The classic maze-mapping technique:**

1. Take food from the fridge
2. Enter the maze
3. DROP a unique item in each room
4. When you return to a room: "I see a Wheel of Cheese here!"
5. You know you've been here before!

**20 foods ÷ 10 maze rooms = 2 markers per room (if needed)**

---

## The Fridge (20 Items!)

| # | Item | Drop in Room... |
|---|------|-----------------|
| 1 | Suspiciously Perfect Apple | A (puddle) |
| 2 | Wheel of Aged Cheese | B (echo) |
| 3 | Loaf of Crusty Bread | C (scratches) |
| 4 | Jar of Pickled Herring | D (golden glow) |
| 5 | Leftover Shepherd's Pie | E (cobwebs) |
| 6 | Bunch of Purple Grapes | F (cold spot) |
| 7 | Pot of Mysterious Stew | G (carved face) |
| 8 | Wedge of Blue Cheese | H (mushrooms) |
| 9 | Cold Roast Chicken | I (skeleton) |
| 10 | Jar of Strawberry Jam | J (crossroads) |
| 11-20 | (Extras for backup!) | As needed |

---

## Other Objects

| Object | Purpose |
|--------|---------|
| **Stove** | Decorative. Adventures come first. |
| **Sink** | Contains eternal dishes. Don't wash them. |
| **Table** | Has a note from Mother with instructions. |

---

## Mother's Note

> "Dearest Bumblewick,
>
> If you're reading this, you've been transported to another
> mysterious underground adventure. AGAIN.
>
> The food is for DROPPING IN THE MAZE to mark your path,
> **NOT FOR EATING.**
>
> You know what happens when you eat. Your "constitution."
> I'm not cleaning it up this time.
>
> Don't forget your lamp. Don't get eaten by grues.
>
> Your loving Mother"

---

## ⚠️ EATING THE FOOD — A Creative Strategy!

**Mother warned you. But consider this:**

If you EAT any food item, something *hilarious* happens. The food traverses your legendary Fantastipants digestive system and emerges... **transformed**. 

Actually, this is a GREAT maze-marking technique! Each food:
- 🎭 Has a unique journey (the DM describes it dramatically)
- ✨ Transforms into something memorable
- 🧠 Can add properties to Bumblewick
- 📍 Becomes an even BETTER maze marker (no two are alike!)

### Examples of What Happens:

| Food | Transforms Into | Adds to Player |
|------|-----------------|----------------|
| Apple | Puddle of Applesauce | `fairytale_immunity: 5` |
| Herring | VERY Pickled Herring | `herring_aura: true`, `smell_radius: 3` |
| Mysterious Stew | Sentient Stew (alive!) | `stew_creator: true`, `mysterious_glow` |
| Birthday Cake | Singing Cake Slice | `birthday: "today"`, `cake_whispers` |
| Salami | Mystical Salami | `old_country_dreams`, `accent: foreign` |
| Olives | Hollow Olives | `pimento_quota: 20` (they're inside you now) |

By the end of the maze, Bumblewick might have: herring aura, sardine followers, mysterious internal glow, and dreams of The Old Country. 

**This is character development!**

### Context Matters!

Effects vary by **costume**, **room**, **objects present**, and **history**:

| Context | Example Effect |
|---------|----------------|
| 🧛 Vampire costume | Apple becomes Blood Apple |
| 🏴‍☠️ Pirate costume | All liquids become rum |
| 🔦 In dark maze room | "The SOUNDS are concerning" |
| 🦴 Skeleton nearby | Existential commentary from skeleton |
| 🐟 Already have herring aura | All subsequent food smells |
| 👻 Ghost costume | Food phases through floor to room below |
| 🤡 Clown costume | Everything becomes confetti |

### State is PERSISTENT!

When you eat, the DM updates YAML files:
- `player.yml` — gains new properties
- `ROOM.yml` — gains transformed food
- New files created — sentient stew needs a file!

The world **evolves** as you eat!

See [fridge.yml](./fridge.yml) for all transformations, contextual modifiers, and persistence rules.

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| 🚪 East | [start/](../start/) — Back to Chamber of Commencement |
| 🎭 (via start) | [coatroom/](../coatroom/) — Costumes! |
| 🌀 (via start) | [maze/](../maze/) — The grue-infested maze |
| ⬆️ Up | [adventure-1/](../) |
