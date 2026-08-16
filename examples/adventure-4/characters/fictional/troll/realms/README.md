# Realms — the soul's interiors

Two-Toll carries a **mirror of each mind's home turf inside himself** — not the
whole map of either game, just his little corner of it, reproduced as an
embedded topology (same pattern as the
[Wumpus 2 caves](../../wumpus-snorax/topologies/)). He can literally retreat
into either of his soul's realms:

```yaml
location: realms/ZORK-TROLL-ROOM.yml#troll-room        # sulk with the axe
location: realms/ADVENTURE-CHASM-BRIDGE.yml#beneath-the-bridge   # audit in peace
```

| Realm | Mind | Corner mirrored |
|-------|------|-----------------|
| [`ZORK-TROLL-ROOM.yml`](ZORK-TROLL-ROOM.yml) | [zork-mind](../minds/zork-mind.yml) | The Troll Room and its three blocked passages |
| [`ADVENTURE-CHASM-BRIDGE.yml`](ADVENTURE-CHASM-BRIDGE.yml) | [adventure-mind](../minds/adventure-mind.yml) | The chasm, the rickety bridge, and beneath it |

Rules of the interior:

- **Realms are memory, not the live game.** Each mirrors only the rooms the
  mind actually inhabited; exits beyond the corner end in mist (Adventure) or
  sinister black fog (Zork) — memory blurs where he never went.
- **The edge becomes a room.** Outside, he binds to an edge in the world graph
  (his location IS a rule). Inside, the bridge is a place he can stand. A
  border guard's inner life is standing on his own bridge with nobody coming.
- **Stomach is gut; realms are soul.** [`../stomach/`](../stomach/README.md)
  holds what he ate. Realms hold where he's *from*. Both are pocket universes;
  only one has digestive juices.
- **Interior tourism.** Either mind may visit the other's realm. zork-mind
  finds the bridge scenic and the pricing absurd. adventure-mind finds the
  Troll Room's decor ("bloodstains, deep scratches") bad for property value.
  Counsel continues inside (see `counsel_to_sibling` in both minds).
- **Fronting from inside is allowed**, same as from the stomach. Retreat is
  not resignation; the toll booth reopens when he steps out.
- **Players can jump in too.** A world may mount a realm as a visitable
  microworld — meet the troll in his natural habitat, on his home planks,
  by his own bloodstains. Two games, two habitats, one troll to interview
  in either.
