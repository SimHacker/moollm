# Party Skill

Companions and group dynamics.

**Motto:** *"You're never alone. Unless you want to be."*

## Key Concepts

- **Companions have relationships** with you AND each other
- **Emergent creation** — asking about family CREATES them
- **Maintenance** — companions have needs too
- **Selection** — commands directed to selected targets (zero, one, many)

## Simulation State

In `SIMULATION.yml`:

```yaml
party:
  members:
    - characters/don-hopkins/
    - pub/cat-cave/terpie.yml
  leader: characters/don-hopkins/
  formation: line

selection:
  targets: [pub/cat-cave/terpie.yml]  # Always a list
```

**Selection targets:** Characters, rooms (rooms are characters too!), objects, concepts.

## Recruitment

| Method | How |
|--------|-----|
| Ask NPCs | Request they join |
| Family | Ask Mother about relatives |
| Summon | Use skill/ability |
| Hire | Pay gold |

## Roles

| Role | Types |
|------|-------|
| Frontline | Fighter, Guardian, Tank |
| Support | Navigator, Light-Bearer, Pack Mule |
| Specialist | Photographer, Chef, Merchant |
| Mystic | Oracle, Medium, Postal Savant |
| Wildcard | Pet, Sibling, Reformed Grue |

## Commands

- `SELECT [target]` / `DESELECT`
- `PARTY` / `RECRUIT` / `DISMISS`
- `PARTY FORMATION [line/circle/defensive]`
- `HOLD / FOLLOW / SCATTER / REGROUP`
- `[COMPANION] GUARD / SCOUT / FETCH`

## See Also

- [character](../character/) — Companions are characters
- [needs](../needs/) — Companions have needs
- [room](../room/) — Rooms can be selection targets