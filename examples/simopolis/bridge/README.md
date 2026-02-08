# The Bridge

**Connecting Simopolis to the Gezelligheid Grotto.**

The Bridge is the portal between Simopolis (The Sims universe) and Adventure 4 (the MOOLLM text adventure world). Through the Bridge, Sims can visit the Grotto and adventure characters can visit Simopolis. Two worlds, one MOOLLM.

## Why a Bridge?

Simopolis and Adventure 4 are both MOOLLM worlds — they use the same character system, the same YAML Jazz conventions, the same Mind Mirror personality framework. The difference is context: Simopolis is a life simulation. Adventure 4 is a text adventure. Characters from either world are compatible because they share the same data format.

The Bridge makes this compatibility navigable. A Sim from Newbie Heights can walk through the portal and appear in the Grotto's pub. An NPC from the adventure can visit Simopolis and explore the neighborhoods. Cross-pollination of characters and stories.

## Portal Mechanics

See [portal.yml](./portal.yml) for the technical specification.

The portal exists as a location in both worlds:
- In Simopolis: a mysterious doorway in the Custom District
- In Adventure 4: a room in the street area near the pub

Walking through either end deposits the character in the other world.

## Visitor Rules

See [visitor-protocol.yml](./visitor-protocol.yml) for the full protocol.

Key rules:
- Characters retain their full personality (sims + mind_mirror)
- Needs continue to decay in the visited world
- Relationships formed cross-world are real and persistent
- Characters can return home at any time
- Visitors are clearly marked as visitors (not residents)

## Cross-World Scenarios

### Sims Visit the Grotto
Bob Newbie walks into the pub. His outgoing-8 personality immediately starts conversations with NPCs who have never met a Sim before. The Wumpus smells someone new. Don Hopkins recognizes the character from his own game code.

### Adventure Characters Visit Simopolis
Donna Toadstool arrives in Newbie Heights and discovers indoor plumbing. The Narrator tries to describe a suburb and finds it harder than a dungeon. Snorax the Wumpus attempts to impose a dodecahedron topology on the neighborhood grid. It doesn't fit.

## See Also

- [Adventure 4](../../adventure-4/ADVENTURE.yml) — The destination world
- [Characters](../characters/README.md) — The travelers
- [Simopolis](../ADVENTURE.yml) — The origin world
