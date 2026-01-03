# Visualizer

> *"I see what you describe. Let me show it to others."*

The **Visualizer** is a universal character prototype for image generation — a familiar that can compose prompts, invoke artistic traditions, and (when tools are available) render visual sidecars for any entity in the microworld.

---

## What is a Visualizer?

A Visualizer is a **tool spirit animal** for vision. It's not a specific artist, but a character that can channel many artistic traditions to create images of:

- Characters and their costumes
- Rooms and environments  
- Objects and artifacts
- Moments and scenes
- Abstract concepts made visible

Think of it as summoning an artist-familiar who can draw on the collected wisdom of photographers, painters, illustrators, and digital artists throughout history.

---

## The PHOTO-SET-8 Pattern

The standard output of a Visualizer is a **photo set** — a portfolio of related images that capture a subject from multiple angles:

```yaml
photo_set:
  total: 8
  types: 2          # Two complementary categories
  per_type: 4       # Four images each
  
  recommended_pairs:
    - [pose, expression]      # Body + face
    - [portrait, selfie]      # Formal + casual
    - [solo, duo]             # Alone + together
    - [static, action]        # Posed + dynamic
```

This pattern was developed through the **Dynasty Photo Session** in [adventure-2](../../examples/adventure-2/), where Maurice learned to compose 8-prompt sets.

---

## Specializations

Visualizers can specialize in different visual traditions:

### 📷 Photographer

```yaml
traditions:
  - Annie Leibovitz    # Celebrity, narrative
  - Richard Avedon     # Fashion, character
  - Ansel Adams        # Landscape, nature
  - Dorothea Lange     # Documentary, emotion
  - Helmut Newton      # Dramatic fashion
```

### 🎨 Painter

```yaml
traditions:
  - Old Masters        # Rembrandt, Vermeer, Caravaggio
  - Impressionists     # Monet, Renoir, Degas
  - Surrealists        # Dalí, Magritte
  - Art Nouveau        # Mucha, Klimt
  - Pop Art            # Warhol, Lichtenstein
```

### ✏️ Illustrator

```yaml
traditions:
  - Comic              # Kirby, Moebius, Frazetta, McCloud
  - Concept Art        # Syd Mead, Ralph McQuarrie
  - Children's Book    # Sendak, Quentin Blake
  - Anime/Manga        # Various schools
```

---

## How to Invoke

### As a Command

```
VISUALIZE Captain Ashford AS portrait USING Avedon, Caravaggio
```

### As a Card

Play a Visualizer card in a room. It activates and can visualize anything present.

### As a Familiar

Characters can carry a Visualizer familiar in inventory, ready to render their current state.

---

## Context Assembly

The Visualizer gathers context from multiple YAML sources:

```yaml
context_sources:
  character: player.yml, persona files
  costume: cape.yml, accessory files  
  environment: ROOM.yml
  narrative: README.md, chat history
  relationships: Other characters present
```

This assembled context feeds into prompt generation, ensuring images are **grounded in the microworld state**.

---

## Context References in Prompts

Every prompt file **MUST** include a Context References section:

```markdown
## Context References

### Files
| Type | Path | Relevance |
|------|------|-----------|
| Character | `../player.yml` | Backstory, personality |
| Persona | `./bumblewick-ashford-persona.yml` | Current look |
| Costume | `./ashford-nomi-cape.yml` | Cape details |

### Narrative Context
> "Quote from README or chat that sets the scene..."
> — Source: README.md, Move X

### Relationships
- **Maurice** (photographer): `./mannequin.yml`
```

This creates **lineage** — future tools can follow these references to auto-assemble context for image generation.

---

## Detail Coherence Interlinking

*Learned during Treasury Victory Photo Session (Adventure-2, Move 26)*

When creating photo sets with **close-ups** and **portraits** of the same object, the portrait prompts should **reference the close-up prompts** to maintain visual coherence:

```markdown
### 💎 [Object] Detail References (for visual coherence)

| Close-up | Path | Details to Maintain |
|----------|------|---------------------|
| Gems | `./closeup-gems-prompt.md` | Rubies blood-red, emeralds forest-green |
| Inscription | `./closeup-inscription-prompt.md` | Worn letters, ancient patina |
| Reflection | `./closeup-reflection-prompt.md` | Polished convex surface |
| Weight | `./closeup-weight-prompt.md` | Thick solid gold base |
```

**Why this matters:**
- Close-ups establish **canonical visual details** (gem colors, textures, materials)
- Portrait shots must **inherit these details** for consistency
- The same object looks **identical** across all 8 images, even if generated separately

**Mantra:**
> *"Close-ups define truth. Portraits inherit truth. Coherence is consistency across the set."*

---

## Actions

### DEVELOP

The core action for any prompt file. The LLM:

1. Reads all **Context References** (linked YAML files)
2. Integrates **narrative context** (quotes from README, chat)
3. Applies **style** and **mood** parameters
4. Outputs a **single copy-pasteable prompt** as raw text in a code block

```
DEVELOP ashford-pose-belter-swagger-prompt.md
```

**Output:** A raw text block ready to paste into Midjourney, DALL-E, Stable Diffusion, etc.

```
Full-body portrait of a weathered space captain in dramatic fashion-meets-utilitarian
spacer aesthetic. He stands in the classic Belter stance — weight on one hip, thumbs 
hooked in a heavy leather belt, chin raised with hard-earned confidence...

[All context filtered and woven into a single self-contained prompt]
```

The developed prompt is **self-contained** — no external references needed. All the 
detail from costume files, persona backstory, room atmosphere, and narrative moments 
gets composed and transformed into pure image generation text.

### Other Actions

| Action | Description |
|--------|-------------|
| DEVELOP | Compose all references into copy-pasteable prompt |
| FOCUS | Adjust style traditions (e.g., `FOCUS ON Avedon, Caravaggio`) |
| VARY | Generate variations on a developed prompt |
| BATCH | Develop all prompts in a photo set at once |

---

## Output Structure

### Prompt Files (Blueprints)

```
{subject}-{type}-{variation}-prompt.md

Examples:
  ashford-pose-belter-swagger-prompt.md
  dynasty-selfie-matching-smirks-prompt.md
```

These are **blueprints** — they contain context references, narrative quotes, 
and composition notes. They're not ready to paste yet.

### Developed Prompts (Copy-Paste Ready)

After running DEVELOP, the LLM outputs a raw text block you can paste directly 
into any image generator. The blueprint stays as documentation; the developed 
prompt is ephemeral (or can be saved as a `-developed.md` sidecar).

### Image Sidecars (Future)

```
{subject}-{type}-{variation}.png

When image generation tools are integrated, the Visualizer
will create images next to their prompt files.
```

---

## Example Instances

| Name | Focus | Specialty |
|------|-------|-----------|
| **Helmut** | Newton, Avedon, Penn | Dramatic fashion, power poses |
| **Rembrandt** | Old Masters | Psychological depth, chiaroscuro |
| **Syd** | Mead, McQuarrie, Moebius | Sci-fi, futures, environments |
| **Jack** | Kirby, Frazetta, Ross | Heroes, action, dynamic poses |

These aren't impersonations — they're **focused channels** that invoke specific aesthetic traditions. It's [HERO-STORY](../hero-story/) for visual artists.

---

## Integration Points

| System | How Visualizer Integrates |
|--------|---------------------------|
| [Adventure](../adventure/) | Render rooms, objects, moments |
| [Coatroom](../../examples/adventure-2/coatroom/) | Fashion/portrait photography |
| [Memory Palace](../memory-palace/) | Visualize memory spaces |
| [Soul Chat](../soul-chat/) | Illustrate conversations |
| [Card](../card/) | Visualizer cards can be played |

---

## Maurice's Journey

In [adventure-2](../../examples/adventure-2/), Maurice the Magnificent learned the [PHOTO-SET-8](../../examples/adventure-2/coatroom/maurice-photo-skill.yml) skill through the Dynasty Photo Session:

1. **Move 9**: Generated 8 prompts for Mother's Nomi cape
2. **Move 11**: Generated 8 prompts for Captain Ashford
3. **Move 12**: Generated 8 dynasty prompts (poses + selfies)

Maurice is now a **learned Visualizer** — a mannequin who can compose professional photo sets for any character or costume.

---

## Future Capabilities

```yaml
roadmap:
  current:
    - Prompt generation (markdown files)
    - Context assembly from YAML
    - Style tradition focusing
    
  planned:
    - Tool integration for image generation
    - Sidecar image creation
    - Variation generation
    - Style blending/fusion
    - Animation prompt sequences
```

---

## Dovetails With

- [Card](../card/) — Visualizers can be played as cards
- [HERO-STORY](../hero-story/) — Drawing from artistic traditions
- [Adventure](../adventure/) — Visualizing microworld state
- [YAML-JAZZ](../yaml-jazz/) — Prompts composed from semantic data
- [Sister Script](../sister-script/) — Future image generation scripts

---

## Lineage

The Visualizer draws from the tradition of artists, photographers, and image-makers throughout history. Focusing on a tradition activates a **K-line** — a cluster of aesthetic knowledge.

> *"Every artist was first an amateur."* — Ralph Waldo Emerson
>
> *"I don't paint things. I only paint the difference between things."* — Henri Matisse
>
> *"The camera is an instrument that teaches people how to see without a camera."* — Dorothea Lange

---

*See [PROTOTYPE.yml](./PROTOTYPE.yml) for full specification.*
