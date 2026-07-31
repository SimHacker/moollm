# Troll instances — per-world state

The prototype (../CHARACTER.yml) is immutable and shared. Each world that
imports the troll grows an instance file here, diverging like a save file.

The troll is an **instanced border**: his instance binds to an *edge* in the
room graph (a bridge, a doorway, a passage), not to a room. Instance shape:

```yaml
prototype: ../CHARACTER.yml

instance:
  network: <world id>
  guards: <edge — e.g. "room-c <-> room-d" or "the chasm bridge">
  fronting: <zork-mind | adventure-mind | both | riddles>

toll_ledger: []      # one entry per crossing: who, what was paid, which mind collected

customs:
  arrived_with: empty_pockets   # wealth lives in the instance, never the prototype
  exchange_rate: <world policy — zero is legal ("zorkmids are souvenirs here")>
```

The pointer file in the world's room directory is the visa; an optional
`imports:` block is the customs declaration. See
[PORTABLE-NPCS.md §6](../../../../../../skills/soul-city/PORTABLE-NPCS.md).

No instance is placed in the adventure-4 maze yet — the maze has no bridge,
and the troll refuses to price an edge beneath his standards. When a world
gives him a chokepoint worth guarding, the first save file lands here.
