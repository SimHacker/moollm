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

| Realm | Mind | Corner mirrored (dilated one move) |
|-------|------|------------------------------------|
| [`ZORK-TROLL-ROOM.yml`](ZORK-TROLL-ROOM.yml) | [zork-mind](../minds/zork-mind.yml) | Trap door → cellar → Troll Room → East-West Passage → Round Room, plus one step into the maze |
| [`ADVENTURE-CHASM-BRIDGE.yml`](ADVENTURE-CHASM-BRIDGE.yml) | [adventure-mind](../minds/adventure-mind.yml) | Winding corridor → chasm → rickety bridge → far side → long corridor → the fork, plus the audit office beneath |

Each realm is **dilated one move outward** from the home room into its
canonical neighbors, selectively: an **entrance hall** to walk down (the
slamming trap door; the winding corridor with its clink of approaching
treasure), an **exit hall** to leave through (the East-West Passage; the long
corridor with its faint volcano rumble), and **one good fork** for local
branching (the Round Room, spinning, all exits but one in fog; the fork in the
path, where the left prong is hearsay of a breath-taking view and the right
prong is mist that lumbers). Rooms are tagged with their `role:` — entrance,
exit-hall, branching, one-step-in — so the excerpt reads as a ride, not a
diorama.

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

## The pattern: block quotes of other worlds

A realm is a **block quote** — a procedural rhetorical excerpt from another
work of literature (in this case, adventure games). The whole apparatus of
quotation maps onto it:

| Quotation | Realm |
|-----------|-------|
| The excerpt | the mirrored rooms — his corner, not the whole map |
| The ellipsis (…) | the fog and mist at the boundary — where the quote ends |
| The citation | `canon:` and provenance fields — game, year, source |
| Fair-use sizing | quote a passage, not the book: seven rooms, not the Great Underground Empire |
| Quoting from memory | descriptions are the mind's recollection, lightly editorialized ("my decor, my resume") |

The same pattern at other scales:

- **Disneyland dark rides.** Mr. Toad's Wild Ride, Peter Pan's Flight, Snow
  White's Scary Adventures — navigable block quotes of a story's famous
  corners, compressed into a track. A realm is a dark ride through a
  character's memory of the game he lived in.
- **Holodeck historical reenactments.** Mount the excerpt as a visitable
  simulation, walk in, interview the inhabitants. The realm's boundary fog
  is the holodeck wall you agree not to touch.
- **Cyberpunk 2077 braindances.** Volumetric reality captures of a scene —
  walkable, scrubbable, glitch-fuzzed at the edge of the recording. A realm
  is a braindance of a game: the capture volume is the dilated excerpt, and
  the fog is where the sensor data ends.
- **Prose itself.** An epigraph at a chapter head is a tiny mounted realm:
  someone else's world, quoted, with a citation, changing how you read what
  follows.

Any character can quote any world this way: excerpt the corner that matters,
fence it in ellipsis, cite the source, and let people walk around inside the
quotation.
