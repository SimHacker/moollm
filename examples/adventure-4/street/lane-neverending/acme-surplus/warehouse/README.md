# 🏭📦♾️ The ACME Warehouse

> Bigger on the inside. Mail-order reality.

**AUTHORIZED PERSONNEL ONLY — HARD HAT AREA**

## The Space

Shelves stretch into darkness, far beyond the building's exterior walls. The ceiling is lost in shadow. Forklifts hum somewhere in the distance.

This is ACME's distribution network. Infinite inventory. Impossible logistics.

## The Tunnel (Again)

The painted tunnel from outside is HERE — from the inside. Packages launch through it constantly. Forklifts drive through casually.

You still cannot use it. It's not fair.

## Trap Deployment

| Theme | Catalog Section | Mood |
|-------|-----------------|------|
| Industrial | `traps_and_devices` | Heavy things fall |
| Propulsion | `adventure_gear` | Things launch you |
| Spatial | — | Impossible geometry |

**DM draws from**: `w1/acme-catalog.yml` → traps_and_devices, adventure_gear, hunting

## Irony Patterns

- Player dodges one thing → launches into another
- Player hides behind boxes → boxes ARE the trap
- Player follows safe path → path IS the trap (conveyor)
- Player reaches for valuable → item is bait

## Infinite Inventory

If a player asks "is there a [product]?" — **yes**.

The question is: can they get it without triggering it?

## Automated Hazards

- **Falling Inventory**: Every significant action → something falls
- **Conveyor Traps**: Floor markings lead to something worse
- **Autonomous Forklifts**: Don't see you. Treat you as a package.

## 🎭 Example Instantiation

```yaml
# 💥 TRAP INSTANTIATED: ACME Rocket Skates
trap_instance:
  prototype: $KITCHEN/acme-catalog.yml#adventure_gear/rocket_skates
  location: "Floor between shelving units — player stepped on them"
  triggered_by: "Player walked the 'safe' path between shelves"
  
  state:
    ignited: true
    velocity: 0  # accelerating
    direction: "toward the tunnel (you still can't use it)"
    fuel_remaining: "plenty"
    
  malfunction_roll: 15  # vs 40% threshold
  malfunction_occurred: false  # They work perfectly (no steering)
  
  poetic_justice: "They tried to walk carefully. Now they're flying."
```

> "Your feet lock into something. Straps tighten. You look down—
>  ROCKET SKATES.
>  
>  *FWOOOOSH*
>  
>  Velocity: 10 mph. 30. 50. The shelves blur past.
>  You're headed straight for the painted tunnel.
>  
>  *THWACK*
>  
>  Plywood. It was always plywood. Velocity: 0.
>  You slide down, adding your silhouette to the collection."

---

*Back through: [The Back Room](../back-room/) — where the ticking continues.*
