# MOO-Maps Pyramid Visualizations

**Iterative image generation log — documenting prompts, mining, feedback, and rubrics**

This README is an append-only record of attempts to visualize the MOO-Maps concept.

---

## The Concept

**MOO-Maps**: Semantic pyramids made of tokens instead of stone blocks.

**The Vision**: A 3D MIP MAP of IDEAS — a recursive decomposition pyramid where:
1. **Apex (1 word)**: MOOLLM
2. **Layer 2 (4 words)**: The four biggest conceptual pillars of MOOLLM
3. **Layer 3 (16 words)**: Each pillar decomposes into 4 sub-concepts
4. **Layer N**: 4^N words, progressively smaller, blurring toward base

**NOT**: A literal acronym breakdown (MOO MOO LLM LLM). The pyramid should represent IDEAS recursively decomposed, not string manipulation.

**3D not 2D**: This should feel like looking INTO a pyramid of meaning, not AT a flat triangle.

---

## Evaluation Rubrics

### PASS Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Conceptual Accuracy** | 30% | Layer 2 words are meaningful MOOLLM concepts, not "MOO MOO LLM LLM" |
| **3D Depth** | 20% | Feels like a 3D structure, not flat |
| **Artistic Impact** | 20% | Awe-inspiring, evokes wonder, sacred geometry |
| **Text Legibility** | 15% | Apex readable, layer 2 readable, layer 3 mostly readable |
| **Attention Threads** | 15% | Luminous connections between words visible |

### FAIL Triggers (Immediate Re-roll)

- Layer 2 is literal "MOO MOO LLM LLM"
- Flat 2D appearance
- Text is gibberish/unreadable at apex
- No sense of depth or hierarchy
- Looks like a stock image, not a concept visualization

---

## Generation 1

**Date**: 2026-02-04  
**File**: `moo-maps-pyramid-2026-02-04-15-06-34-moo-maps-pyramid.png`

### Prompt (from moo-maps-pyramid.yml)

```yaml
apex:
  word: "MOOLLM"
  style: "Large, bold, glowing, radiating light outward"
  
layer_2:
  words: ["MOO", "MOO", "LLM", "LLM"]  # <-- THE MISTAKE
  description: "Just below MOOLLM, four words spread out"
```

### What The Prompt Asked For

- MOOLLM at apex (correct)
- Layer 2: "MOO, MOO, LLM, LLM" — literal string breakdown (WRONG)
- Attention head threads (partially achieved)
- Egyptian/Kandinsky/data-viz style (partially achieved)

### Mining Analysis (from moo-maps-pyramid-mined.yml)

**What the AI saw:**
- ✅ Golden MOOLLM at apex, radiating
- ✅ Pyramid structure dominates frame
- ✅ Rainbow attention threads creating web
- ⚠️ Layer 2: "MOO, LLM" — literal, not conceptual
- ⚠️ Lower layers have words but they're somewhat random
- ❌ Text at lower layers is not sensical

**Prompt coherence score**: 92% (per the prompt, which was flawed)

### Human Feedback

> "this isn't really artistic and awe inspiring enough and the text fails to be sensical. it broke down MOOLLM into repeated MOO LLM MOO LLM not what I meant I was asking YOU to think about moollm and come up with four words that represent its biggest 'things'. then break those down into four, recursively. a MIP MAP of IDEAS! but 3d not 2d pyramid."

### Verdict: FAIL

| Criterion | Score | Notes |
|-----------|-------|-------|
| Conceptual Accuracy | 2/10 | Layer 2 is "MOO MOO LLM LLM" — literal, not conceptual |
| 3D Depth | 5/10 | Some depth but mostly looks flat |
| Artistic Impact | 4/10 | Not awe-inspiring, feels stock |
| Text Legibility | 6/10 | Apex readable, layers below are gibberish |
| Attention Threads | 7/10 | Threads visible but sparse |
| **TOTAL** | 4.5/10 | **RE-ROLL REQUIRED** |

### What Worked (Preserve)

- "Golden, luminous, slightly ethereal" apex styling
- "Spaghetti scramble of connections between words"
- "Dark space with subtle constellation patterns" background
- Rainbow spectrum attention threads

### What Failed (Fix)

- **Layer 2 concept**: Must be 4 MEANINGFUL words, not acronym parts
- **3D depth**: Need stronger perspective, INTO the pyramid
- **Text coherence**: Lower layers should be real concepts, not gibberish
- **Artistic impact**: Needs more grandeur, more sacred geometry

---

## Generation 2 (PLANNED)

### Corrected Concept: The Four Pillars of MOOLLM

**Layer 2 should be the four biggest IDEAS, not string parts:**

| Pillar | Why | Sub-concepts (Layer 3) |
|--------|-----|------------------------|
| **SKILLS** | The core abstraction — everything is a skill | templates, examples, scripts, inheritance |
| **CONTEXT** | What fills the window — managed meaning | pyramid, mipmap, resolution, compression |
| **ROOMS** | Directories as navigable space | activation, inventory, presence, state |
| **EVAL** | The axis — data becomes code becomes graphics | yaml-jazz, k-lines, apply, interpret |

### New Prompt Direction

```yaml
apex:
  word: "MOOLLM"
  style: "Golden capstone, radiating meaning outward"
  
layer_2:
  words: ["SKILLS", "CONTEXT", "ROOMS", "EVAL"]  # FIXED!
  concept: "The four conceptual pillars, not acronym parts"
  style: "Large, bold, each a different semantic color"
  
layer_3:
  concept: "Each pillar decomposes into its 4 sub-concepts"
  skills_branch: ["templates", "examples", "scripts", "inheritance"]
  context_branch: ["pyramid", "mipmap", "resolution", "compression"]
  rooms_branch: ["activation", "inventory", "presence", "state"]
  eval_branch: ["yaml-jazz", "k-lines", "apply", "interpret"]
  
depth:
  concept: "3D MIP MAP — looking INTO the pyramid, not AT it"
  perspective: "Camera slightly inside, depth recedes"
  vanishing_point: "Deep inside the pyramid structure"
```

### 3D Emphasis

- Perspective should feel like looking INTO a tunnel of meaning
- Vanishing point deep in the structure
- Words should feel like they exist in 3D space, not pasted on a flat surface
- Atmospheric perspective: closer words sharp, distant words hazy

### Artistic Direction

- Sacred geometry: Metatron's cube influence
- Data cathedral: reverence for structured knowledge
- The sublime: awe at the scale of recursive decomposition
- NOT stock art, NOT corporate infographic

---

## Iteration Log

| Gen | Date | Verdict | Main Issue |
|-----|------|---------|------------|
| 1 | 2026-02-04 | FAIL | Layer 2 literal "MOO LLM", flat, not inspiring |
| 2 | (pending) | — | Correct layer 2 concepts, emphasize 3D depth |

---

## Files

| File | Purpose |
|------|---------|
| `moo-maps-pyramid.yml` | Generation 1 prompt (flawed) |
| `moo-maps-pyramid-mined.yml` | Generation 1 mining analysis |
| `moo-maps-pyramid-2026-02-04-*.png` | Generation 1 image (FAIL) |
| `README.md` | This file — iteration log |
| `SLIDESHOW.md` | Public-facing slideshow (only successful generations) |

---

*"A MIP MAP of IDEAS! But 3D not 2D pyramid."*
