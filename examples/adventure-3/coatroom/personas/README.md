# Personas

> *"Who do you want to be today?"*

A **persona** is a wearable costume + personality overlay. It's NOT a character — it's a **mask** that modifies whoever wears it.

---

## Character vs. Persona

| Aspect | Character | Persona |
|--------|-----------|---------|
| **What** | Who you ARE | Who you're PLAYING |
| **File** | `characters/don-hopkins.yml` | `personas/captain-ashford.yml` |
| **Contains** | Full Mind Mirror traits | Trait MODIFIERS (+/-) |
| **Permanent?** | Yes — your core identity | No — put on, take off |
| **Backstory** | Your real history | The role's fictional history |

---

## How It Works

```
BASE CHARACTER + PERSONA MODIFIERS = PERFORMED PERSONALITY

don-hopkins.yml          captain-ashford.yml
  playful: 9        +       playful: +1         =    playful: 10 (capped)
  confident: 6      +       confident: +2       =    confident: 8
  cautious: 3       +       cautious: +2        =    cautious: 5
```

The **base personality shows through** the persona. Don Hopkins wearing Ashford is a MORE playful, pie-menu-enthused Ashford than Bumblewick wearing Ashford.

---

## Wearing a Persona

In your character file:

```yaml
current_persona: coatroom/personas/captain-ashford.yml
```

Or in the coatroom:

```
> WEAR captain-ashford
> DON captain-ashford     # Same thing
> REMOVE PERSONA          # Back to your real self
```

---

## What a Persona Modifies

### Trait Modifiers
```yaml
sims_trait_modifiers:
  playful: +1       # More gallows humor
  neat: -2          # Belters don't fuss

mind_mirror_modifiers:
  emotional:
    forceful: +2    # Captains give orders
    confident: +2   # Project confidence
```

### Appearance
```yaml
appearance:
  description: "Weathered Belter captain in leather long coat..."
  costume_pieces: [...]
  body_language: [...]
```

### Speech Patterns
```yaml
speech:
  dialect: "Belter patois"
  vocabulary: { sa_sa: "I understand"... }
  catchphrases: ["Sa-sa ke, kopeng?", ...]
```

### Skills Granted
```yaml
skills_granted:
  - name: "BELTER-PATOIS"
  - name: "CAPTAIN-PRESENCE"
```

---

## Available Personas

| Persona | Style | Source |
|---------|-------|--------|
| [captain-ashford.yml](./captain-ashford.yml) | Belter space pirate | The Expanse |
| *(create more!)* | | |

---

## Creating New Personas

1. Copy `captain-ashford.yml` as template
2. Define trait **modifiers** (not absolute values!)
3. Write appearance, speech patterns, role backstory
4. List skills the persona grants

```yaml
persona:
  name: "Your Persona Name"
  
  sims_trait_modifiers:
    playful: +2     # How this persona changes playfulness
    
  appearance:
    description: "..."
    
  speech:
    catchphrases: [...]
```

---

## Philosophy

> *The persona is a lens, not a replacement.*

- Your BASE self determines the foundation
- The persona adds flavor, modifiers, skills
- A serious person playing a clown is a DIFFERENT clown than a playful person
- You can slip out of character — the real you shows through
- Multiple characters can wear the same persona differently

This is how actors work. The role shapes you, but you also shape the role.

---

## Dovetails With

- [../](../) — The Coatroom (where you try on personas)
- [../../characters/](../../characters/) — Character files that wear personas
- [../../../../skills/mind-mirror/](../../../../skills/mind-mirror/) — The trait system
