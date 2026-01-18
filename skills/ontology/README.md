# 🏷️ Ontology

> Tags, not trees. Folksonomy, not taxonomy.

## What Is This?

Characters in MOOLLM can be **many things at once**. Biscuit is both a **real dog** AND an **animal character**. An AI chatbot trained on someone's writings is simultaneously **based on a real person**, **a robot**, AND **fictional** (its responses are generated).

Traditional class hierarchies can't capture this. You'd have to pick one box.

**Ontological tags** let you pick all the boxes that apply.

## The Tags

| Tag | Emoji | Meaning |
|-----|-------|---------|
| `real-being` | 👤 | Actually exists in reality |
| `historical` | 📜 | Real being who has died |
| `fictional` | 📖 | Invented, doesn't exist |
| `animal` | 🐾 | Non-human creature |
| `robot` | 🤖 | Artificial/mechanical |
| `abstract` | 💭 | Concept personified |
| `mythic` | ✨ | From mythology/folklore |

## Why It Matters

Each tag carries **ethical implications**. When you tag a character, you're declaring what respect they're owed:

- **`real-being`** → Consent, accuracy, right to correct
- **`animal`** → Species-appropriate, no false capabilities
- **`robot`** → Transparency, no deception
- **`fictional`** → Creator authority, internal consistency

When tags combine, **the most restrictive ethics win**.

## Examples

```yaml
# Biscuit — Don's actual dog
biscuit:
  tags: [real-being, animal]
  # Real creature ethics + dog behavior

# C-3PO — fictional robot  
c3po:
  tags: [fictional, robot]
  # Creative freedom + robotic patterns

# "The Spirit of Minsky" — teaching personification
spirit_of_minsky:
  tags: [historical, abstract]
  # Legacy respect + acknowledge it's a personification

# AI trained on Don's writings
don_bot:
  tags: [real-being, robot, fictional]
  # Consent + AI disclosure + generated content
```

## Directory Structure Is Just Filing

The `characters/` directory structure:

```
characters/
  animals/dogs/biscuit/
  people/don-hopkins/
  robots/repair-demon/
```

This is **organizational convenience**, not ontological truth. Biscuit could be moved to `characters/familiars/biscuit/` without changing what he IS.

The `CHARACTER.yml` file declares the tags. That's the source of truth.

## Inheritance

Tags enable rich inheritance:

| Type | Example | What's Inherited |
|------|---------|------------------|
| **Structural** | kitten → cat → animal | Methods, behaviors |
| **Parental** | Kitten-3 → Stroopwafel | Personality, relationships |
| **Adoptive** | Puppy → Don (adopter) | Home, family bonds |
| **Familiar** | Biscuit ↔ Don | Location, goals, delegation |
| **Persona** | Don + "Professor" overlay | Presentation, vocabulary |

## Room Context

Rooms provide ethical framing that **layers onto** character ethics:

```yaml
room:
  ethics:
    frame: "whimsical adventure"
    constraints: [family-friendly]

character:
  tags: [real-being, animal]

# Result: Portray real dog in family-friendly whimsical context
```

## Quick Start

```yaml
# In your CHARACTER.yml
character:
  id: my-character
  
  ontology:
    tags: [fictional, animal]
    species: dragon
    
  # That's it! Ethics compose automatically.
```

## Related

- [representation-ethics/](../representation-ethics/) — Deep ethics guidance
- [hero-story/](../hero-story/) — Real person protocol
- [character/](../character/) — Character creation
- [incarnation/](../incarnation/) — Full character incarnation
