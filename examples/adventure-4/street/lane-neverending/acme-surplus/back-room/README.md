# 📦⏰💀 The Back Room

> *tick tick tick*

**EMPLOYEES ONLY — AUTHORIZED PERSONNEL — DANGER**

## The Ticking

Something is ticking. Somewhere in the stacks. Rhythmic. Patient. It has been ticking for a long time.

## Trap Deployment

| Theme | Catalog Section | Mood |
|-------|-----------------|------|
| Mystery | `mystery_items` | Unknown effects |
| Experimental | `tools` | Prototype danger |
| Time-based | — | The ticking is SOMEWHERE |

**DM draws from**: `w1/acme-catalog.yml` → mystery_items, tools, detection_devices

## Irony Patterns

- Player searches boxes → finds something they weren't looking for
- Player follows the ticking → ticking stops (worse)
- Player opens "DO NOT OPEN" → as advertised

## 🎭 Example Instantiation

```yaml
# 💥 TRAP INSTANTIATED: ACME Time-Delay Dynamite
trap_instance:
  prototype: $KITCHEN/acme-catalog.yml#traps_and_devices/time_delay_dynamite
  location: "The source of the ticking — finally found"
  triggered_by: "Player investigated the ticking sound"
  
  state:
    fuse_remaining: "???"  # ACME fuses are unpredictable
    ticking: false  # It stopped when they found it (worse)
    
  malfunction_roll: 89  # vs 45% threshold
  malfunction_occurred: true  # Fuse is either 0 or infinity
  
  poetic_justice: "They found the ticking. The ticking stopped."
```

> "The ticking has stopped. That's... worse, isn't it?"

## The Box That Works

Shelf 7, Row 13, behind the returns. Labeled "ANOMALY — DO NOT SHIP."

One product that works perfectly. No malfunction. No catch.

This terrifies everyone.

---

*Deeper in: [Warehouse](../warehouse/) — where the REAL inventory lives.*
