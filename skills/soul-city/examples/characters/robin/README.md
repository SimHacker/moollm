# Robin — the courier

The character sketched at the top of [SOUL-MODEL.md](../../../SOUL-MODEL.md), incarnated so you can walk the tree instead of imagining it.

| Path within `robin/` | Role |
|---|---|
| `CHARACTER.yml` | Body on the map: location, inventory, relationships |
| `personas/worn` → `courier/` | Costume: satchel, route patter, delivery voice |
| `soul/` | Continuity: history and albums |
| `soul/albums/route-log/` | Numbered beats: the archivist's pages |
| `soul/minds/navigator/` | Knows the map; fronts while riding |
| `soul/minds/archivist/` | Keeps the albums; fronts at day's end |
| `soul/minds/sims-self/` | Organelle: Robin's Sims traits and album, in Sims format |

One body, one costume currently worn, one soul, three minds. Every number is adjustable; the model page explains which numbers you can turn.

## What each piece demonstrates

| Piece | Model concept |
|-------|---------------|
| `CHARACTER.yml` | Body — `location` is a property that changes; the directory stays put |
| `personas/worn → courier/` | Worn costume as a pointer; take it off, the satchel patter goes with it |
| `soul/SOUL.yml` | Continuity — history and `minds[]`, riding the character's map pin |
| `minds/navigator/`, `minds/archivist/` | Sibling minds under one soul; fronting rotates by scene |
| `minds/sims-self/` | Organelle — one mind per game; Sims format kept intact, bridged not flattened |
| `albums/route-log/01-…, 02-…` | Enumerated membrane — bubbles in a line; each beat its own file |

## Fronting, in Robin's day

- Morning ride: **navigator** fronts; archivist rides along, occasionally counsels ("that alley flooded last week").
- Day's end: **hand off** to **archivist**, who writes the day into `albums/route-log/`.
- When Robin projects into The Sims: **sims-self** fronts, thinking in motives and relationship scores. The other two mute or ride along.

Nothing ranks them. Fronting is a role, not a hierarchy.
