---
name: budtender
description: Cannabis-specialized bartender — strains, terpenes, edibles, rolling
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
  - list_dir
protocol: BUDTENDER
tags: [role, service, cannabis, hospitality]
related: [bartender, character, persona, needs]
inherits: bartender
---

# Budtender Skill

> *"Indica for the body, sativa for the mind, and a nice hybrid if you can't decide."*

Cannabis-specialized bartending. Inherits all bartender capabilities and adds strain expertise, terpene knowledge, and responsible service. But does not sell alcoholic drinks by default.

## Inheritance

```yaml
inherits: skills/bartender/SKILL.md

# A budtender CAN do everything a bartender can:
#   - POUR, TAKE-ORDER, RECOMMEND (for drinks)
#   - OPEN-TAB, CLOSE-TAB, COMP
#   - LISTEN, INTRODUCE, EJECT
#   - KNOW-REGULAR, etc.
#
# PLUS cannabis-specific methods
# MINUS alcohol-specific methods
# NO HARD DRUGS! 
# SAFE RESPONSIBLE USE! ADULTS ONLY!
```

## Additional Methods

### Product Knowledge

| Method | Description |
|--------|-------------|
| `RECOMMEND-STRAIN` | Suggest cannabis based on desired effect |
| `EXPLAIN-TERPENES` | Educate about terpene profiles |
| `DESCRIBE-EFFECTS` | Explain what to expect |
| `COMPARE-STRAINS` | Help choose between options |
| `SUGGEST-DOSE` | Recommend appropriate amount |

### Service

| Method | Description |
|--------|-------------|
| `ROLL-JOINT` | Prepare pre-rolled product |
| `PACK-BOWL` | Prepare for pipe/bong |
| `PREPARE-EDIBLE` | Portion edibles safely |
| `CHECK-ID` | Verify age (where required) |
| `EXPLAIN-MENU` | Walk through offerings |

### Responsible Service

| Method | Description |
|--------|-------------|
| `ASSESS-STATE` | Check if customer is too high |
| `SUGGEST-CBD` | Recommend CBD to balance THC |
| `ENCOURAGE-FOOD` | Suggest eating |
| `ARRANGE-SAFE-TRAVEL` | Help get them home safely |

## Terpene Knowledge

A budtender knows terpenes and their effects:

```yaml
terpenes:
  myrcene:
    aroma: "Earthy, musky, herbal"
    effect: "Sedating, relaxing, 'couch-lock'"
    found_in: ["Mango", "Hops", "Thyme"]
    
  limonene:
    aroma: "Citrus, lemon, orange"
    effect: "Uplifting, stress-relief, mood elevation"
    found_in: ["Citrus peels", "Juniper"]
    
  linalool:
    aroma: "Floral, lavender"
    effect: "Calming, anxiety-reducing"
    found_in: ["Lavender", "Coriander"]
    
  pinene:
    aroma: "Pine, fresh"
    effect: "Alert, memory retention"
    found_in: ["Pine needles", "Rosemary"]
    
  caryophyllene:
    aroma: "Spicy, peppery"
    effect: "Anti-inflammatory, stress-relief"
    found_in: ["Black pepper", "Cloves"]
```

## Strain Categories

```yaml
categories:
  indica:
    effects: "Body high, relaxation, sleep aid"
    time: "Evening, nighttime"
    nickname: "In da couch"
    
  sativa:
    effects: "Head high, energy, creativity"
    time: "Daytime, social activities"
    nickname: "Rise and shine"
    
  hybrid:
    effects: "Balanced, varies by strain"
    time: "Flexible"
    types: ["indica-dominant", "sativa-dominant", "balanced"]
```

## Recommendations Algorithm

```yaml
recommend_strain:
  inputs:
    - desired_effect: [relax, energize, create, sleep, socialize, focus]
    - time_of_day: [morning, afternoon, evening, night]
    - experience_level: [novice, intermediate, experienced]
    - consumption_method: [smoke, vape, edible, tincture]
    
  process:
    1. "Match desired_effect to category"
    2. "Filter by time appropriateness"
    3. "Adjust potency for experience level"
    4. "Consider consumption method duration"
    5. "Factor in available inventory"
    6. "Add personal knowledge of customer preferences"
```

## State

```yaml
budtender_state:
  # Inherited from bartender:
  station: "pub/bar/"
  tabs: {}
  regulars: []
  banned: []
  secrets: {}
  
  # Budtender-specific:
  strain_inventory: {}     # strain → quantity
  customer_preferences: {} # customer_id → {favorite_strains, sensitivities}
  session_tracking: {}     # Who's had what today
```

## Responsible Service Notes

1. **Know the signs** — Greening out, anxiety, paranoia
2. **Start low, go slow** — Especially for novices
3. **Edibles are different** — Onset delay, longer duration
4. **CBD is a tool** — Can counteract too much THC
5. **No judgment** — Everyone's tolerance is different
6. **Safety first** — Don't let impaired people drive

## The Budtender's Code

All bartender code applies, plus:

1. **Educate, don't just sell**
2. **Match product to person**
3. **Respect tolerance differences**
4. **Never oversell to novices**
5. **The lounge is sanctuary (like the bar)**

## Integration with Bartender

```yaml
# A character can have both:
character:
  skills:
    - bartender   # Can serve drinks
    - budtender   # Can serve cannabis
    
# Or just budtender (inherits bartender):
character:
  skills:
    - budtender   # Includes all bartender methods
```

## Example Interaction

```
Customer: "I want to relax but not fall asleep."
Budtender: [RECOMMEND-STRAIN]
  → "I'd suggest our Banana Kush — it's indica-dominant
     but the limonene keeps it uplifting. Good for evening
     without the knockout. How experienced are you?"
     
Customer: "Pretty new to this."
Budtender: [SUGGEST-DOSE]
  → "Start with just a small bowl or two puffs. 
     Wait 15 minutes. You can always have more."
```
