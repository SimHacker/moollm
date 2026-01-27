# Connections Tour: Maps, Frames, Schemas, Microworlds in MOOLLM
## Why This Document Exists

The “map/territory risk” is not just a philosophical slogan. It is the core failure
mode of any system that uses simplified internal models to navigate a complex world.
MOOLLM treats that risk as an engineering constraint: you **must** build mechanisms
that keep the map revisable, grounded, and corrigible.

This document narrates the lineage (Papert → Minsky → Drescher → MOOLLM), then
anchors each step in concrete artifacts inside this repo so the ideas are testable.

---

## Connection 1: The Turtle That Became a World (Papert → Rooms)

Seymour Papert’s constructionism is not just an education philosophy; it is an
operational method: learn by **building in a microworld** you can inspect and modify.
MOOLLM takes that literally: the filesystem is the microworld, directories are rooms,
and agents learn by moving through it and editing it.

The bootstrap connections tour explicitly makes this mapping, and the protocol index
records the core microworld/room primitives that make it real.

- Connections tour (Papert → filesystem as microworld):
  [skills/bootstrap/CONNECTIONS.md](../skills/bootstrap/CONNECTIONS.md)
- Protocols index (rooms, vehicles, turtles, spatial navigation):
  [PROTOCOLS.yml](../PROTOCOLS.yml)

Concrete illustration: the Leela Manufacturing world is a working microworld where
each room is a modeling sandbox. The lobby explains that the world is a “poetic
representation” of real Leela deployments, which makes the map/territory boundary
explicit.

- Live microworld root:
  [examples/adventure-4/.../leela-manufacturing/ROOM.yml](../examples/adventure-4/street/lane-neverending/leela-manufacturing/ROOM.yml)

---

## Connection 2: K-Lines That Became Protocols (Minsky → Symbols)

Marvin Minsky’s K-lines are the mechanism that turns named concepts into **reactivated
mental states**. MOOLLM turns that into a protocol system: a symbolic name invokes a
tradition and its behavioral constraints.

This is the map/territory guardrail: **naming is not truth**, but it is a deliberate
activation of a constrained model.

- Protocol symbols explicitly described as K-lines:
  [PROTOCOLS.yml](../PROTOCOLS.yml)
- Connection narrative showing “type the name → invoke tradition”:
  [skills/bootstrap/CONNECTIONS.md](../skills/bootstrap/CONNECTIONS.md)

This same mechanism enables safe invocation of historical lineages (Papert, Minsky,
Ungar, Kay) without pretending the system is the person: the symbol activates the
tradition, not the identity.

---

## Connection 3: Schemas as Causal Units (Piaget → Drescher → MOOLLM)

Piaget formalized how schemas update via assimilation/accommodation, but Gary
Drescher made the update algorithm explicit: **Context → Action → Result**, with
statistical tracking to discover prerequisites, side effects, and hidden state.
This is the repair loop for maps that fail.

MOOLLM’s schema-mechanism skill spells out the causal learning loop in implementable
terms and maps it directly to Play‑Learn‑Lift:

- **PLAY** = act + observe
- **LEARN** = attribute causes and preconditions
- **LIFT** = spin off a refined schema

References:

- Schema mechanism (full algorithm, marginal attribution, synthetic items):
  [skills/schema-mechanism/SKILL.md](../skills/schema-mechanism/SKILL.md)
- Schema mechanism quick overview (K-line links and rationale):
  [skills/schema-mechanism/README.md](../skills/schema-mechanism/README.md)

Live illustration: the **Insight Furnace** in Leela Manufacturing is explicitly
described as “Drescher’s gift, Minsky’s dream,” and it spells out the neural → symbolic
→ causal transformation as a concrete pipeline.

- Insight Furnace room (explicit Drescher/Minsky language):
  [examples/adventure-4/.../floor-2/ROOM.yml](../examples/adventure-4/street/lane-neverending/leela-manufacturing/floor-2/ROOM.yml)

---

## Connection 4: Play‑Learn‑Lift as Governance (Repair Loop, not Vibes)

Play‑Learn‑Lift is not a motivational slogan; it is the governance layer that forces
models to stay revisable. The LEARN phase explicitly separates observation from change,
and LIFT requires provenance and review. That is a procedural check on map/territory
collapse: you can’t “just upgrade the map” without evidence.

Reference:

- The full methodology and explicit LEARN sub‑phases:
  [skills/play-learn-lift/SKILL.md](../skills/play-learn-lift/SKILL.md)

---

## Connection 5: Factorio as the Systems Vocabulary (Materialized Cognition)

The Factorio design doc is the most technical “bridge language” in the repo. It maps
abstract learning and dataflow into a concrete, throughput‑oriented system that LLMs
already understand deeply. This is where “schema learning” becomes “factory logic.”

Key reason: systems reasoning becomes literal — bottlenecks, backpressure, queues,
blueprints. It’s not analogy; it’s a constrained vocabulary for causal reasoning.

Reference:

- Factorio → MOOLLM → Leela translation and Drescher schema table:
  [designs/FACTORIO-MOOLLM-DESIGN.md](./FACTORIO-MOOLLM-DESIGN.md)

Live illustration: the Leela factory world described in the Factorio design is
implemented as rooms with named floors (intake, factory, shipping) that represent
the causal pipeline. It is a microworld that **runs the metaphor** as a system.

- Leela factory lobby (explicit mapping):
  [examples/adventure-4/.../leela-manufacturing/ROOM.yml](../examples/adventure-4/street/lane-neverending/leela-manufacturing/ROOM.yml)

---

## Connection 6: Map/Territory as a Layered Ontology (Elastic Architecture)

The strongest explicit map/territory analysis is in the Don Hopkins “elastic
architecture” session. It distinguishes three layers — repo structure, exit network,
and the imagined world — and lands on the MOOLLM stance:
**“the map both is and is not the territory.”**

This is the precise formulation that reconciles symbolic architecture with lived
experience: the YAML is the world **for the agent**, but remains a representation
for the architect. Two truths, one system.

Reference:

- Elastic architecture session (map/territory table and claims):
  [examples/adventure-4/.../elastic-architecture.md](../examples/adventure-4/characters/real-people/don-hopkins/sessions/2026-01-23-09-00-00-elastic-architecture.md)

---

## Connection 7: The Documentary Proof of Synthesis (Design Transcript)

The raw design transcript records the moment when Minsky, Ungar, Kay, Papert,
Hofstadter, Curtis, and others were explicitly invoked as architectural sources.
It documents the conscious act of synthesis — not just the outputs.

Reference:

- Foundational transcript with explicit lineage and K‑line activation:
  [designs/raw-chats/moollm-design.txt](./raw-chats/moollm-design.txt)

---

## How the Pieces Interlock (High‑Level Synthesis)

1) **Microworld substrate** (Papert): the filesystem becomes the space of play.  
2) **Symbolic activation** (Minsky): protocol names act as K‑lines that activate
   traditions and constraints.  
3) **Causal learning loop** (Drescher): schemas refine through evidence and surprise.  
4) **Governed upgrades** (Play‑Learn‑Lift): changes must be observed, justified, and
   lifted with provenance.  
5) **Systems vocabulary** (Factorio): causal pipelines are described in a shared,
   quantitative language (throughput, buffers, backpressure).  
6) **Map/territory guardrail** (Elastic Architecture): the world is symbolic but
   must remain corrigible; the map is powerful but never final.

The result is a live example: a microworld that can be played in, debugged, and
reconfigured while preserving a rigorous account of how each model was formed.

---

## Quick Links: Best Illustrations

If you only click five, click these:

1) Papert → microworlds → rooms  
   [skills/bootstrap/CONNECTIONS.md](../skills/bootstrap/CONNECTIONS.md)

2) Minsky → K-lines → protocol symbols  
   [PROTOCOLS.yml](../PROTOCOLS.yml)

3) Drescher → schema mechanism → Play‑Learn‑Lift mapping  
   [skills/schema-mechanism/SKILL.md](../skills/schema-mechanism/SKILL.md)

4) Insight Furnace (live schema mechanism in-world)  
   [examples/adventure-4/.../floor-2/ROOM.yml](../examples/adventure-4/street/lane-neverending/leela-manufacturing/floor-2/ROOM.yml)

5) Map/territory formalization (elastic architecture)  
   [examples/adventure-4/.../elastic-architecture.md](../examples/adventure-4/characters/real-people/don-hopkins/sessions/2026-01-23-09-00-00-elastic-architecture.md)

