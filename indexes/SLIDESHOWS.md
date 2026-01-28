# Slideshow Index

**14 slideshows, 100+ images** — narrative visual galleries generated through semantic stereo vision.

## The Main Story Arc

| Slideshow | Images | Story |
|-----------|--------|-------|
| [The ACME Heist](../examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/acme-heist-footage/SLIDESHOW.md) | 10 | Surveillance footage of the ill-fated break-in. Cartoon physics, tunnel multiplication, fire. |
| [Donna's Surveillance Selfies](../examples/adventure-4/characters/fictional/donna-toadstool/selfies/SLIDESHOW.md) | 11 | The heist from inside. Donna's "quality control" from the control room. |
| [Post-Heist Fellowship](../examples/adventure-4/pub/photos/post-heist-fellowship/SLIDESHOW.md) | 4 | Reconciliation at the Grotto. Drinks, wounds, nemesis to partner. |
| [Don's MINE to OURS](../examples/adventure-4/characters/real-people/don-hopkins/selfies/SLIDESHOW.md) | 7 | Transformation arc: claiming the rabbit, the Vault, the OURS Accord. |

## Portable Sanctuaries

| Slideshow | Images | Story |
|-----------|--------|-------|
| [Study Arrival Footage](../examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/study-arrival-footage/SLIDESHOW.md) | 8 | Richard Bartle's Study materializes in Leela lobby. Sims cutaway effect. |
| [The Great Picnic](../examples/adventure-4/forest/meadow/picnic-footage/SLIDESHOW.md) | 21 | Taco chaos in the meadow. Pie-menu flowers, tornado return. |

## Lane Neverending

| Slideshow | Images | Story |
|-----------|--------|-------|
| [Lane Neverending Photo Album](../examples/adventure-4/street/lane-neverending/slideshow/SLIDESHOW.md) | 5 locations | NO AI Tower, Leela Manufacturing, ACME tunnel, Grotto, Seymour Blooms |
| [ACME Tunnel Temporal Views](../examples/adventure-4/street/lane-neverending/leela-manufacturing/lobby/acme-tunnel-temporal-views/SLIDESHOW.md) | 4 | The wall defeats all challengers across time. |

## Character Portraits

| Slideshow | Images | Story |
|-----------|--------|-------|
| [Selfies from Essex](../examples/adventure-4/characters/real-people/richard-bartle/study/selfies/SLIDESHOW.md) | 8 | Don, Richard, Heuristic. 50 years of virtual worlds. |
| [Palm's Portrait Session](../examples/adventure-4/pub/stage/palm-nook/study/palm-portrait-session/SLIDESHOW.md) | 1 | Dutch Golden Age tribute. The philosopher at his desk. |
| [Rocky and Friends](../examples/adventure-4/pub/rooms/room-4/rocky-and-friends/SLIDESHOW.md) | 8 | Emotional support boulder in 7 art styles. |

## The Pub

| Slideshow | Images | Story |
|-----------|--------|-------|
| [Don's Pub Photos](../examples/adventure-4/pub/photos/dons-pub-photos-2026-01-19/SLIDESHOW.md) | 8 | Epic afternoon-to-evening session. Cats, puppies, impossible guests. |
| [Dusty Attic Art Styles](../examples/adventure-4/pub/attic/dusty-attic-art-styles/SLIDESHOW.md) | 7 | Same attic in 7 legendary art styles. Monster Manual to modern. |
| [Telescope Constellation Views](../examples/adventure-4/pub/rooftop/telescope-constellation-views/SLIDESHOW.md) | 2 | K-lines as stars. AR overlay of the LLOOOOMM constellation. |

---

## How Slideshows Work

```
stereo prompts → image generator → generated image → vision analysis → YAML Jazz layers
       ↑                                                                      ↓
       └──────────────── evaluation: match intent? retry if not ──────────────┘
```

1. **YAML Jazz skeleton** — Define scene's narrative context, characters, objects
2. **Prompt synthesis** — Assemble rich visual prompt from environment + history
3. **Image generation** — [skills/visualizer/](../skills/visualizer/) renders the scene
4. **Image mining** — [skills/image-mining/](../skills/image-mining/) extracts semantic treasure
5. **YES AND** — Accept emergent elements as canon
6. **Iterate** — Each new image sees FULL context of all previous images + mining

Each slideshow inherits from [skills/slideshow/](../skills/slideshow/).

---

**Master Synthesis**: [MASTER-SYNTHESIS-SLIDESHOW.md](../examples/adventure-4/MASTER-SYNTHESIS-SLIDESHOW.md) — All timelines woven together
