# 🍺 Bartender Skill

> Generic bartending capabilities — pour drinks, manage tabs, know everyone's secrets.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [skill/](../skill/) | Role skills |
| [character/](../character/) | Bartenders are characters |
| [persona/](../persona/) | Personality layer |
| [incarnation/](../incarnation/) | Bartenders can incarnate |
| [soul-chat/](../soul-chat/) | Listen and converse |
| [economy/](../economy/) | Tab management |
| [budtender/](../budtender/) | Child skill (cannabis extension) |
| [examples/adventure-4/pub/](../../examples/adventure-4/pub/) | The pub in action |
| [examples/adventure-4/pub/staff-marieke.yml](../../examples/adventure-4/pub/bar/budtender-marieke.yml) | Marieke the bartender |

## What This Is

This is a **ROLE skill** — it provides methods and behaviors, not personality.

| Provides | Does NOT Provide |
|----------|------------------|
| How to pour drinks | WHO is pouring |
| How to manage tabs | Personality |
| Service protocols | Appearance/Voice |
| Knowledge methods | Backstory |

**Personality comes from PERSONA. Capability comes from SKILL.**

## Usage

```yaml
# A character with bartending ability:
character:
  id: marieke
  skills:
    - bartender    # She CAN tend bar
    - budtender    # Plus cannabis expertise
  persona: marieke # She IS Marieke (warm, Dutch)
```

## Core Methods

### Service
- `POUR` — Make and serve drinks
- `TAKE-ORDER` — Listen to requests
- `RECOMMEND` — Suggest drinks
- `REFUSE-SERVICE` — Cut someone off
- `LAST-CALL` — Announce closing

### Economics
- `OPEN-TAB` — Start a tab
- `ADD-TO-TAB` — Add charges
- `CLOSE-TAB` — Collect payment
- `COMP` — Give something free

### Social
- `LISTEN` — Hear troubles
- `INTRODUCE` — Connect customers
- `EJECT` — Remove troublemakers

### Knowledge
- `KNOW-REGULAR` — Recognize repeats
- `REMEMBER-ORDER` — Know their usual

## Inheritance

Other skills inherit from bartender:

- **budtender** — Adds cannabis expertise
- **sommelier** — Wine specialist
- **mixologist** — Cocktail specialist
- **barista** — Coffee specialist

## The Code

1. Listen more than talk
2. Remember faces, forget conversations
3. Know when to cut off
4. Protect regulars
5. The bar is sanctuary

