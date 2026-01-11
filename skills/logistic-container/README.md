# 📦 Logistic Container

> Factorio-style logistics boxes for MOOLLM adventures.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [designs/factorio-logistics-protocol.md](../../designs/factorio-logistics-protocol.md) | The source design |
| [room/](../room/) | Rooms inherit from containers |
| [container/](../container/) | OpenLaszlo-style inheritance |
| [prototype/](../prototype/) | Grid rooms inherit logistics config |

## The Big Idea

**Logistic containers live at the QUADRANT level, not in each cell!**

The diagonal directions (NW/NE/SW/SE) of the pie menu open into grid quadrants.
Each quadrant has a `LOGISTIC-CONTAINER.yml`. Grid rooms **inherit** from it.

## 🏙️ The Urban Metaphor

**Grid rooms are CITY BLOCKS at street intersections!**

```
           N (street north)
           ↑
    ┌──────┼──────┐
    │  NW  │  NE  │  ← BUILDINGS you ENTER
    │ 🏭   │  📦  │
W ──┼──────●──────┼── E (streets east/west)
    │  📦  │  🚚  │    
    │  SW  │  SE  │  ← BUILDINGS you ENTER
    └──────┼──────┘
           ↓
           S (street south)
```

- **Streets** = Cardinal exits (N/S/E/W) — you TRAVEL
- **Intersection** = The room you're in
- **Buildings** = Diagonal quadrants — you ENTER them
- **Building Interior** = Grid cells within quadrant

## Structure

```
wizard-study/                    # Intersection (pie menu center)
  ROOM.yml
  nw/                            # NW Building (warehouse)
    LOGISTIC-CONTAINER.yml       # ← Building config!
    iron-ore/
      ROOM.yml                   # ← Room inside building!
    copper-ore/
      ROOM.yml
  ne/                            # NE Building (factory)
    LOGISTIC-CONTAINER.yml       # Different purpose
  sw/
    LOGISTIC-CONTAINER.yml
  se/
    LOGISTIC-CONTAINER.yml
```

## Pie Menu = Street Intersection

```
        N (street to Great Hall)
        │
   NW ←─●─→ NE      ← ENTER BUILDINGS (diagonals)
   🏭   │   📦        
        │
   W ←──┼──→ E      ← TRAVEL STREETS (cardinals)
   🏠   │   🌳
        │
   SW ←─●─→ SE      ← ENTER BUILDINGS (diagonals)
   📦   │   🚚
        │
        S (street to Cellar)
```

## Factorio Box Types

| Mode | Color | Use Case |
|------|-------|----------|
| `passive-provider` | 🟡 Yellow | Pantry, armory, ore storage |
| `active-provider` | 🔴 Red | Factory output, mail outbox |
| `requester` | 🔵 Blue | Workbench, player inventory |
| `storage` | ⬜ White | Overflow, junk drawer |
| `buffer` | 🟢 Green | Loading dock, staging |

## Quadrant Example

```yaml
# nw/LOGISTIC-CONTAINER.yml — Ore Storage
logistic-container:
  id: ore-storage
  name: "Ore Storage Quadrant"
  mode: passive-provider
  
  provides:
    - tags: ["ore"]
    
  grid:
    enabled: true
    auto_create_cells: true
    stack_limit: 10000
```

## Grid Room (Inherits!)

```yaml
# nw/iron-ore/ROOM.yml
room:
  inherits: ["../"]       # ← Inherit from quadrant!
  
  stacks:
    iron-ore: 2500        # Just the data
    
  exits:
    SW: ../../            # Back to main
    N: ../copper-ore/
```

**No logistics config needed — inherited!**

## Files

- `LOGISTIC-CONTAINER.yml.tmpl` — Main template
- `CELL.yml.tmpl` — Grid cell template (non-room)
- `CARD.yml` — Skill card
- `SKILL.md` — Full documentation

