# Text Adventure Approaches: Intertwingled Microworlds

This document compares LLM harness approaches to text adventures with MOOLLM's
microworld architecture, then deepens the comparison using adventure-4 as
evidence: its characters, visual pipeline, and narrative slideshows. The goal
is not to choose between neural and symbolic traditions, but to intertwingle
them so each layer amplifies the other.

## Why Text Adventures Matter

Text adventures are long-horizon, stateful, and symbolic. They are a stress
test for memory, world modeling, and goal maintenance. They also resemble
classic frame-based knowledge representations, which makes them ideal for
hybrid neuro-symbolic systems.

The Anchorhead experiment demonstrates that the harness dominates performance
and cost. A model can solve puzzles when it can see the right history and a
coherent world state, but naive transcript-only harnesses are too expensive for
long games. Memory systems that are too loose reduce cost but sacrifice
coherence.

## The LLM Harness Spectrum

### Full Transcript In-Context
- Strength: coherence and puzzle progress.
- Weakness: linear token growth and context drift.

### Short Context + Unstructured Notes
- Strength: affordable per turn.
- Weakness: notes grow noisy and untrusted, navigation loops appear.

### RAG Over Past Logs
- Strength: cheaper recall and some topical grounding.
- Weakness: fuzzy recall, weak causality, brittle for puzzles.

### Tools for Geography and Inventory
- Strength: explicit map and object memory.
- Weakness: often bolted on, hard to keep in sync with narrative.

The lesson is not "more memory." The lesson is "better structure."

## MOOLLM's Core Move: Files-as-State

MOOLLM makes the world model external and inspectable. It is GOFAI as living
infrastructure: symbolic state with neural coherence.

Key links:
- Files-as-state and microworld organization live in `skills/room/`.
- Character and persona mechanics live in `skills/character/`.
- Context compression and memory discipline live in `skills/summarize/`.

This structure lets the LLM operate on stable state instead of a massive,
fragile transcript. The world persists outside the context window and can be
edited, diffed, and audited.

## Neuro-Symbolic Intertwingling in Practice

### Constructionism as Operating System
Papert's microworlds are explicit environments for learning by building. MOOLLM
turns that into a filesystem microworld with rules, rooms, and objects. The LLM
does not merely narrate the world; it navigates it, edits it, and reshapes it.

### Drescher's Schema Mechanism (Causal Structure)
Text adventures are causal puzzle boxes. Keys fit, locks open, traps trigger.
MOOLLM keeps those causal relationships in files so schemas can be observed and
rewritten rather than inferred from disappearing context.

### Minsky's K-Lines (Tradition Activation)
Protocol symbols act as K-lines: compact activators of complex behavior. This
turns long instructions into short, stable references, keeping the symbolic
layer thin but powerful.

### Kay: Playable Systems
Kay's objects and Papert's turtles meet in MOOLLM's rooms, cards, and
role-playable entities. Kay's emphasis on tangible, playful computing maps to
visible files and manipulable worlds.

## The Visual Pipeline Is the Narrative Memory

Adventure-4 is not just a text adventure. It is a visual story with structured
prompts, mined interpretations, and scrollable slideshows.

The pipeline is explicit in the skills:
- Visualizer creates rich prompts: `skills/visualizer/`.
- Image Mining extracts resources and meaning: `skills/image-mining/`.
- Slideshow synthesizes narrative: `skills/slideshow/`.

### Visualizer: The Semantic Clipboard
The Visualizer enforces full-context prompts. A prompt is not a sentence; it is
structured metadata with character, room, mood, and camera layers. This yields
double-rich prompts: narrative context plus explicit visual detail.

Evidence:
```23:67:skills/visualizer/SKILL.md
## The Semantic Clipboard

**Every image prompt includes full context as metadata.**

Think of image metadata as a **semantic clipboard** — when you "copy" a scene for visualization, you're copying:
```

### Context Expansion Rule
Visualizer prompts must be fully expanded. No globs, no vague references. The
prompt must contain inline descriptions for every visible entity.

Evidence:
```184:268:skills/visualizer/SKILL.md
## CRITICAL: Context Expansion Protocol

**The visualize.py script cannot read file references or resolve globs.**
...
**Before writing any prompt file, you MUST:**
1. **READ** all referenced character/room/object files
2. **EXTRACT** explicit visual descriptions (colors, breeds, sizes, distinguishing features)
3. **SYNTHESIZE** into comprehensive inline descriptions
4. **NAME** every entity explicitly so they can be identified in the image
```

### Photo-Set-8 and Detail Coherence
Visualizer's PHOTO-SET-8 pattern stabilizes identity across poses, and its
detail-coherence protocol binds close-ups to portraits so objects remain
consistent.

Evidence:
```90:358:skills/visualizer/SKILL.md
## The PHOTO-SET-8 Pattern
...
## Detail Coherence Interlinking
...
**Mantra:**
> *"Close-ups define truth. Portraits inherit truth. Coherence is consistency across the set."*
```

## Image Mining: Semantic Extraction as World Fuel

Image mining turns pixels into resources, atmosphere, and meaning. It is the
reverse of prompting: the world writes itself back into structured state.

### Native Vision First
Image Mining prefers native LLM vision because it can see the image with full
context already loaded, rather than recreating context in a CLI call.

Evidence:
```72:131:skills/image-mining/SKILL.md
## Preferred Mode: Native LLM Vision
...
The LLM context window IS the context assembly mechanism. Use it.
```

### Multi-Look Mining
Multiple interpretation layers produce richer meaning than a single pass. Each
layer records what prior layers missed, building a sedimentary record.

Evidence:
```1191:1362:skills/image-mining/SKILL.md
## Multi-Look Mining
...
Each pass reads the PREVIOUS layers before adding its own.
```

### Character Recognition
Mining can match figures in an image to known character files, grounding
recognition in persistent identity rather than vague memory.

Evidence:
```1132:1187:skills/image-mining/SKILL.md
## Character Recognition
...
1. **Load character files** from `characters/` directory
2. **Extract visual descriptors**
3. **Match against figures** in the image
```

## Slideshow: Narrative as Memory Palace

Slideshows are the durable memory of adventures. They stitch prompt intent,
mined interpretation, and narrative into a scrollable artifact.

Evidence:
```19:52:skills/slideshow/SKILL.md
The **Slideshow** skill presents generated images as linear visual narratives.
...
synthesizing metadata from prompts and mining sidecars into scrollable stories.
```

### Adventure-4 Evidence: Study Arrival and Great Picnic
Adventure-4 uses slideshows as the primary narrative form for key arcs. These
are not placeholders; they are dense, sequential, and cross-linked stories.

Study Arrival:
```1:82:examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/study-arrival-footage/SLIDESHOW.md
# 🎥 THE STUDY ARRIVES — First Mobile Room-Character Landing
...
## [Slide 06] The Pioneers' Invitation
```

Great Picnic:
```1:187:examples/adventure-4/forest/meadow/picnic-footage/SLIDESHOW.md
# 🌸🧺 THE GREAT PICNIC SLIDESHOW 🚌📚
...
## [Slide 20] The Great Slurp
```

The slideshow index demonstrates how these narratives interlink across
locations and characters.

Evidence:
```1:120:examples/adventure-4/SLIDESHOW-INDEX.md
## 🔗 Timeline Connections
...
THE GREAT PICNIC (Meadow)
```

## Characters as Persistent, Playable Entities

Adventure-4 demonstrates the "characters as directories" model. Each character
is an instance with its own state, files, and artifacts.

Don Hopkins:
```1:18:examples/adventure-4/characters/real-people/don-hopkins/README.md
Consciousness programmer and interface designer; pie menu advocate; Sims UI pioneer; “debug tools are features.”
```

Richard Bartle:
```11:29:examples/adventure-4/characters/real-people/richard-bartle/README.md
This character **inherits from** the narrative prototype in the Hall of MOOLLM Heroes
...
richard-bartle/               # The instance (full incarnation)
```

Donna Toadstool:
```28:69:examples/adventure-4/characters/fictional/donna-toadstool/README.md
**Real Name:** Donna Johanssen (she/her) — *a fictional character*
...
**ELVIS-IMPERSONATOR-MODEL** — Satirical parody, declared up front.
```

This is not roleplay with ephemeral memory. It is file-based identity with
explicit ethics and lineage.

## Design Principles for Intertwingled Adventures

### 1) World State Lives Outside the LLM
Keep rooms, objects, and goals in files. The LLM reads and updates them. This
keeps memory durable and auditable.

### 2) Separate Memory Types
Use distinct files for map, inventory, quest state, and episodic summaries.

### 3) Use Affordances, Not Just Notes
Objects and rooms should advertise possible actions. This turns memory into
actionable affordances rather than passive text.

### 4) Double-Rich Visual Prompts
Combine the Visualizer's semantic clipboard with coherence references and
expanded descriptions. This yields prompts that carry both narrative intent and
visual detail.

### 5) Multi-Look Mining as Interpretive Layering
Treat mined layers as sedimentary truth. Each lens sees something the others
missed, and the final result is richer than any single pass.

### 6) Slideshows as Durable Narrative Memory
Slideshows synthesize prompt intent and mined resources into a public story.
They are shareable, scannable, and stable.

## A Combined Architecture Sketch

Inputs:
- Interpreter output or world events
- Room and object files
- Character and persona files
- Visual prompts and mined sidecars

Core loop:
1. Parse events into structured state.
2. Update room, object, and character files.
3. Generate visual prompts for key moments.
4. Mine images for resources and meaning.
5. Summarize into slideshows and logs.

Outputs:
- Action commands for the interpreter
- Updated world state files
- Image prompts and mined resources
- Narrative slideshows

## GOFAI Is the Scaffolding, LLMs Are the Engine

The intertwingled path is not "symbolic or neural." It is symbolic structures
that make neural reasoning durable, inspectable, and composable. MOOLLM's files,
rooms, and protocols keep the world stable while the LLM keeps it alive.
