# Persona Skill

Identity layers for characters — WHO they are vs WHAT they do.

## Key Concepts

### Persona vs Role

| Concept | Definition | Example |
|---------|------------|---------|
| **Persona** | WHO they are | Marieke: warm, patient, Dutch |
| **Role** | WHAT they do | Bartender: serve drinks, know regulars |

These are **separate and combinable**.

### Same Role, Different Personas

```yaml
# bartender.yml role worn by different personas:
coffeeshop: { role: bartender, persona: marieke }
tavern:     { role: bartender, persona: grim }
cantina:    { role: bartender, persona: z4rt }
```

### Same Persona, Different Roles

```yaml
# marieke.yml persona in different contexts:
working:  { persona: marieke, role: bartender }
studying: { persona: marieke, role: botanist }
visiting: { persona: marieke, role: customer }
```

## Structure

```yaml
persona:
  id: marieke
  name: "Marieke van den Berg"
  
  personality:
    warmth: high
    patience: very_high
    # She says what she means. Kindly.
    
  voice:
    accent: "Slight Amsterdam"
    catchphrases: ["Gezellig, ja?", "The cats know."]
    
  backstory: |
    Third generation coffeeshop family.
    Studied botany. Names cats after terpenes.
    
  secrets:
    - "Knows the grey cat isn't from this world"
```

## Layering

Personas layer on characters:

```
Base: marieke (core personality)
+ Role: bartender (skills)
+ Context: busy_evening (stressed)
+ Mood: tired (temporary)

= Marieke serving drinks, a bit frazzled
```

Core personality persists through context changes.

## Integration

- Extends: `character` (adds identity to entities)
- Works with: `room` (theme swapping), `mind-mirror` (dimensions)

## See Also

- [Character Skill](../character/)
- [Mind Mirror Skill](../mind-mirror/)
- [Coatroom Mirror](../../examples/adventure-3/coatroom/)
