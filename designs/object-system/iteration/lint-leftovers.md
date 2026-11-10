# Lint leftovers

`python3 skills/prototype/scripts/resolve.py lint --strict --verbose` from the repo root, exit 1. 2687 YAML files, 0 unparseable. Strict fails on 13 legacy spellings and 8 broken path refs (5 distinct). Cycles 0.

Verbose `broken:` lines name one file per distinct path (the first). The other hits are listed below.

## Legacy spellings

Mechanical.

Eleven are envelope wraps. `flatten.py` without `--write` on these files: would flatten 11, skipped 0. That is the M8 flatten: drop the wrapper key and dedent its block.

Two are `parent:`, which becomes `inherits:`.

### Envelopes

`archive/sim-obliterator/skill/CARD.yml` — `envelope card:`

```yaml
card:
```

`skills/experiment/experiments/turing-chess/characters/slats/CHARACTER.yml` — `envelope character:`

```yaml
character:
```

`skills/experiment/experiments/fluxx-chaos/engine/DEALER.yml` — `envelope dealer:`

```yaml
dealer:
```

`skills/no-ai-ideology/EXPORT.yml` — `envelope export:`

```yaml
export:
```

`examples/old/adventure-3/kitchen/fridge.yml` — `envelope object:`

```yaml
object:
```

`examples/old/adventure-3/kitchen/tomtomagotchi.yml` — `envelope object:`

```yaml
object:
```

`examples/old/adventure-1/coatroom/mannequin.yml`, `examples/old/adventure-2/coatroom/mannequin.yml`, and `examples/old/adventure-3/coatroom/mannequin.yml` — `envelope object:` (line 4 in each)

```yaml
object:
```

`examples/old/adventure-3/pub/ROOM.yml` — `envelope room:`

```yaml
room:
```

`skills/room/TOPOLOGY.yml` — `envelope topology:`

```yaml
topology:
```

### `parent:`

`examples/adventure-4/characters/real-people/don-hopkins/stupid-fun-club-one-minute-movies.yml` — `parent:` → `inherits:`. The sibling `stupid-fun-club.yml` is present.

```yaml
parent: stupid-fun-club.yml
```

`skills/no-ai-ideology/EXPORT.yml` — `parent:` → `inherits:`. The key sits inside the `export:` block; lint sees it after the envelope is read flat.

```yaml
  parent: no-ai-ideology
```

The `parent:` at line 32 of that file is a heading under `skills:` (the tier-0 bundle entry). Lint does not count it.

## Broken path refs

Judgment. Each value is an `inherits:` entry whose path names no directory. `skills/game`, `skills/turtle`, `skills/creature`, `skills/companion`, and `skills/narrator` are absent. `designs/object-system/tasks/objsys-001-reconcile-vocabularies.yml` still leaves this open: write the skills, or respell as K-lines.

`examples/adventure-4/characters/fictional/grue/CHARACTER.yml`

```yaml
  - skills/game           # IS a game, not just plays in one
```

`examples/adventure-4/characters/fictional/troll/CHARACTER.yml`

```yaml
  - skills/game           # Each mind carries a complete game protocol
```

`examples/adventure-4/characters/fictional/wumpus-snorax/CHARACTER.yml`

```yaml
  - skills/game          # IS a game, not just plays in one
```

`examples/adventure-4/characters/animals/logo-turtle/CHARACTER.yml`

```yaml
  - skills/turtle
```

`examples/adventure-4/characters/animals/turtle-theo/CHARACTER.yml`

```yaml
  - skills/turtle
```

`examples/adventure-4/characters/real-people/richard-bartle/pets/heuristic/CHARACTER.yml`

```yaml
  - skills/creature          # A being, not a tool
  - skills/companion         # Bound to Richard
```

`examples/adventure-4/characters/abstract/narrator/CHARACTER.yml`

```yaml
  - skills/narrator       # Future skill for narration protocols
```
