# 🪞 Mind Mirror

> *"Mirrors should reflect a little before throwing back images."* — Jean Cocteau

**Quick Links:**
- [Full Specification](SKILL.md) — complete personality system (Leary + Sims)
- [Ethics](ETHICS.md) — representation ethics for personality modeling
- [Template: EXTENSIONS.yml](EXTENSIONS.yml) — extension template

## Overview

**Mind Mirror** (1985) was Timothy Leary's software for digitizing consciousness. Published by Electronic Arts, it brought academic psychology to personal computers decades before modern personality apps.

This skill combines Leary's **Four Thought Planes** with Will Wright's **Sims traits** for complete character modeling.

## The Two Systems

### Leary's Four Planes (1950/1985)
*How you approach interactions*

- **Bio-Energy** — Vitality, mood, temperament
- **Emotional-Insight** — Interpersonal style
- **Mental-Abilities** — Creativity, knowledge
- **Social-Interaction** — Class, sophistication

### The Sims Traits (2000)
*What you gravitate toward*

| Trait | Low | High |
|-------|-----|------|
| Neat | Sloppy | Tidy |
| Outgoing | Shy | Social |
| Active | Lazy | Energetic |
| Playful | Serious | Fun |
| Nice | Grumpy | Kind |

**Note:** Sims traits use 25 total points distributed across all 5 axes (original game rule).

## The Prison Escape

In 1970, Leary was given the psychological test he himself designed upon prison intake. Understanding what it measured, he answered strategically to appear mild-mannered. Result: minimum security → outdoor detail → escaped over the fence.

**Lesson:** Understanding how you're measured gives you power.

## YAML Jazz Integration

Numbers alone are dead data. Numbers + YAML Jazz comments = **living character**:

```yaml
sims_traits:
  neat: 3        # Tolerates mess. "Organized chaos."
  playful: 7     # Everything's a game. Cannot resist a quip.
```

## Related Skills

- [representation-ethics](../representation-ethics/) — ethical personality models
- [hero-story](../hero-story/) — cards can include Mind Mirror profiles
- [character](../character/) — characters embed Mind Mirror data
- [soul-chat](../soul-chat/) — Mind Mirror influences voice
- [needs](../needs/) — Sims-style fluctuating needs
