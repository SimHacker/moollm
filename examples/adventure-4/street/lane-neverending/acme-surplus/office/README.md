# 📋🔄💔 The Upstairs Office

> "IT WORKS. THAT'S THE PROBLEM."

**PIVOT PLANNING — DO NOT DISTURB**

## The Whiteboards

Every wall is covered. Layers of plans, abandoned mid-sentence:

```
"PIVOT TO SOCIAL" (crossed out)
"PIVOT TO MOBILE" (crossed out)  
"PIVOT TO CRYPTO" (crossed out, angry scribbles)
"PIVOT TO AI" (underlined, then crossed out)
"ACME FINAL FORM" (circled, arrows to nothing)
```

## Trap Deployment

| Theme | Catalog Section | Mood |
|-------|-----------------|------|
| Illusion | `disguises` | Things aren't what they seem |
| Identity | `detection_devices` | Who are you really? |
| Psychological | `mystery_items` | Existential dread |

**DM draws from**: `w1/acme-catalog.yml` → disguises, detection_devices, mystery_items

## Irony Patterns

- Player reads the plans → plans read the player
- Player sits in the chair → becomes middle management (debuff)
- Player erases whiteboard → whiteboard erases something of theirs

## Hazards

- **Existential Dread**: Reading too many pivots = Wisdom save or 1d4 psychic
- **Middle Management Curse**: Sitting in CEO chair = disadvantage on creativity

## 🎭 Example Instantiation

```yaml
# 💥 TRAP INSTANTIATED: ACME Thought Bubble Reader
trap_instance:
  prototype: $KITCHEN/acme-catalog.yml#detection_devices/thought_bubble_reader
  location: "Activated when player sat in the CEO chair"
  triggered_by: "Player assumed the position of power"
  
  state:
    active: true
    thoughts_visible_to: "everyone in the room"
    
  malfunction_roll: 62  # vs 25% threshold
  malfunction_occurred: true  # YOUR thoughts become visible
  
  poetic_justice: "They wanted to know management's secrets.
                   Now everyone knows THEIR secrets."
```

> "A cartoon thought bubble materializes above your head.
>  It shows... oh no. Everyone can see what you're thinking.
>  'I wonder if there's gold in here' floats for all to read."

---

*The spiral staircase leads back to [the sales floor](../).*
