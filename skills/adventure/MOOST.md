# MOOST

*The superlative.*

```
███╗   ███╗ ██████╗  ██████╗ ███████╗████████╗
████╗ ████║██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝
██╔████╔██║██║   ██║██║   ██║███████╗   ██║   
██║╚██╔╝██║██║   ██║██║   ██║╚════██║   ██║   
██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║   ██║   
╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   
```

## The Name

**MOO** — MUD Object-Oriented. The lineage of LambdaMOO, MediaMOO, collaborative text worlds where objects had verbs and rooms had souls.

**LLM** — Large Language Model. The intelligence that makes the world breathe, think, respond, remember.

**MYST** — The monumental ambition. Pre-rendered islands of mystery. Ages you could fall into. Journals that whispered secrets. The feeling of being *somewhere*.

**MOOST** — The superlative form. The MOOST. Not just another virtual world. *The* world.

---

## What MOOST Is

### Not a game. A place.

You don't *play* MOOST. You *go* there.

### Ages that talk back

Myst gave you one camera angle per scene. Beautiful. Frozen. Silent.

MOOST gives you:
- The photographer's eye (`PHOTO.yml`)
- The wanderer's impression (`MINING-don.md`)
- The satellite's cold gaze (`MINING-satellite.md`)
- The soundscape's hum (`MINING-sound.md`)
- The local's gossip (`MINING-passersby.md`)

Every scene is a **prism**. Look from different angles, see different truths.

### Descriptions that think

```javascript
function pickDescription(lod) {
  const { world, self } = this;
  
  // The description KNOWS things
  // The description REMEMBERS
  // The description RESPONDS
  
  if (world.flags.player_insulted_ada) {
    return "The plant's vines are very still. Watching.";
  }
  
  return "Ada II sways gently, humming something tuneless.";
}
```

Static text is dead. MOOST descriptions are **closures over reality**.

### Characters that perform

Ada II doesn't just exist. She **sings**:

```
[ADA II switches to NARRATOR voice]
"In the LLOOOOMM Archive Greenhouse..."

[ADA II switches to DON voice]  
"Seymour, meet Audrey II!"

[ADA II switches to SEYMOUR voice]
"A learning organism that grows through construction?"

[ADA II switches to her OWN voice]
"FEED ME, SEYMOUR! Feed me all night long!"
```

One plant. All the voices. A **one-plant show**.

### Signs that mean three things

```
    ██████████████████████████████████████████████████
    █                                                █
    █     ███╗   ██╗ ██████╗                         █
    █     ████╗  ██║██╔═══██╗                        █
    █     ██╔██╗ ██║██║   ██║                        █
    █     ██║╚██╗██║██║   ██║                        █
    █     ██║ ╚████║╚██████╔╝                        █
    █     ╚═╝  ╚═══╝ ╚═════╝                         █
    █                                                █
    █      █████╗ ██╗                                █
    █     ██╔══██╗██║                                █
    █     ███████║██║                                █
    █     ██╔══██║██║                                █
    █     ██║  ██║██║                                █
    █     ╚═╝  ╚═╝╚═╝                                █
    █                                                █
    █     ████████╗ ██████╗ ██╗    ██╗███████╗██████╗█
    █     ╚══██╔══╝██╔═══██╗██║    ██║██╔════╝██╔══██║
    █        ██║   ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
    █        ██║   ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
    █        ██║   ╚██████╔╝╚███╔███╔╝███████╗██║  ██║
    █        ╚═╝    ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
    █                                                █
    ██████████████████████████████████████████████████
```

Is it a protest? **"NO AI!" (tower)**
Is it possessive? **"NO's AI TOWER"** (Dr. No's property)
Is it ironic? **The tower IS the sign**

In MOOST, meaning is **layered**. You don't get the answer. You get the question, and the question has depth.

---

## The Lineage

```
1976  Adventure (Colossal Cave)     — rooms with descriptions
1978  MUD (Multi-User Dungeon)      — rooms with people  
1890s Monet's Rouen Cathedral       — same place, infinite light
1990  LambdaMOO                     — rooms with verbs, objects with souls
1993  Myst                          — rooms as art, mystery as navigation
1996  The Campanile Movie           — morphing between photographs
1997  Rouen Revisited (Interval)    — projections on architecture
2024  MOOST                         — rooms that think, characters that perform
```

We stand on the shoulders of:
- **Will Crowther** — who put a cave in a computer
- **Pavel Curtis** — who gave objects verbs
- **Rand & Robyn Miller** — who made silence meaningful
- **Seymour Papert** — who knew learning was construction
- **Don Hopkins** — who keeps the flame weird
- **Claude Monet** — who painted Rouen Cathedral 30+ times, same facade, different light
- **Paul Debevec** — SUPER GENIUS. HDR, Light Stage, image-based rendering. The Campanile morphs. Interval Research kiosk projecting onto 3D architecture. Now capturing faces for films.
- **Golan Levin** — SUPER GENIUS. Interactive art, audiovisual performance, computer vision as poetry. Machines that see and respond.

### The Rouen Principle

Monet didn't paint 30 different cathedrals. He painted ONE cathedral, THIRTY ways.

```
Same stone.
Different dawn.
Different noon.
Different storm.
Different season.
Different year.
Different eye.
```

Paul Debevec took this digital — morphing between photographs, projecting onto physical models at Interval Research (Paul Allen's lab). The architecture doesn't move. The *light* transforms. The *rendering* shifts. Reality becomes a spectrum you can slide through.

MOOST inherits this: **One place. Infinite views.**

```
Stand in the florist.
Watch Ada II shift from peaceful to hungry.
Watch the room go from morning to noir.
Watch the window show rain, then clear sky, then the sign glowing.
Watch uploaded sketches morph into AI paintings.

The room is one room.
The room is infinite rooms.
```

---

## The Principles

### 1. Semantic Stereo Vision
Every scene described from multiple angles. Reality emerges from triangulation.

### 2. Progressive Detail
`brief` → `look` → `examine` → `study` → `taste`

The more you attend, the more you see. Attention is rewarded.

### 3. Separation of Voices
Rooms describe space. Objects describe themselves. Characters perform their nature.

### 4. Living Descriptions
Not strings. Closures. The description knows the world state and responds.

### 5. Impersonation
One performer, many voices. Ada II can be everyone in the play.

### 6. The Mystery Remains
Not everything is explained. The sign means three things. Let it.

---

## The Places (So Far)

### Lane Neverending
The street that goes on forever. Dusk light. Neon buzz.

- **NO AI TOWER** — The sign that towers over a one-story building
- **Florist** — Where Ada II waits, hungry for bad code
- **ACME Everything** — Products for problems you didn't know you had
- **Infinite Fountain** — The water that never stops

### The Pub
Where characters gather. Where mirrors reflect.

### More Ages Coming...

---

## The Invitation

```
> look sign

You squint. The building is barely taller than you. A single story.
You could almost reach the gutters. But rising from its roof, 
blazing against the twilight: forty feet of hot pink neon 
spelling out in three massive lines:

    NO
    AI
    TOWER

The letters buzz and flicker. Each one is taller than a person.
The sign weighs more than the building.
The sign probably cost more than the building.
The sign IS the tower.

> examine sign

[The description deepens. The mystery unfolds. 
 But the answer? The answer stays just out of reach.]
```

---

*Welcome to MOOST.*

*The Ages talk back now.*
