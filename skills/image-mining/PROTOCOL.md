# Image Mining Protocol

> **For LLMs with vision**: Read this, look at the image, extract resources.
> **For automation**: Use `mine.py` sister script.

## Quick Start (Native Vision)

You ARE the mining tool. When asked to mine an image:

1. **LOOK** at the image
2. **RECEIVE** the shopping list (resource types to extract)
3. **EXTRACT** quantities/intensities for each
4. **OUTPUT** YAML Jazz with semantic comments

## Shopping List

The user provides resource types to extract. Can be ANYTHING:

```yaml
# Physical
objects, people, animals, materials, colors, textures

# Atmospheric  
mood, atmosphere, lighting, tension, emotion

# Sensations (inferred from visual cues)
implied_smells, implied_sounds, temperature, humidity

# Abstract
meaning, symbolism, narrative, hope, danger, mystery

# Philosophical (deep mining)
existence, mortality, beauty, passage_of_time
```

## Depth Levels

| Depth | What to Extract |
|-------|-----------------|
| `surface` | Objects, materials, colors visible in image |
| `deep` | Hidden meanings, emotions, atmosphere |
| `sensations` | Colors (with hex), textures, inferred smells/sounds |
| `philosophical` | Meaning, symbolism, existential elements |
| `full` | All of the above |

## Output Format (YAML Jazz)

Comments are semantic data, not just documentation:

```yaml
# Mining results for [image]
# Depth: [level]
# Timestamp: [ISO datetime]

resources:
  gold:
    quantity: 150           # Piles of coins, estimated count
    confidence: 0.85
    notes: "Ancient coins, some Roman, some unknown origin"
    
  danger:
    intensity: 0.7          # 0.0-1.0 scale
    confidence: 0.75
    notes: "Dark corners suggest hidden threats"
    
  nostalgia:
    intensity: 0.4          # Evoked by ancient artifacts
    confidence: 0.6
    
  dominant_colors:
    - name: "treasure-gold"
      hex: "#FFD700"
      coverage: 0.4         # Fraction of image
    - name: "shadow-purple"
      hex: "#2D1B4E"
      coverage: 0.3
      
  implied_smells:
    - dust
    - old metal
    - "something rotting in the corner"
    
  objects:
    - type: coins
      count: 150
      notes: "Mixed denominations, several eras"
    - type: chest
      count: 3
      state: "two open, one locked"
    - type: skeleton
      count: 1
      notes: "Previous adventurer, armor rusted"

exhausted: false           # Image still has resources
mining_notes: |
  Rich lode. Multiple passes recommended.
  Philosophical mining would yield mortality/greed themes.
```

## Extraction Rules

### For Countable Resources
```yaml
resource_name:
  quantity: N              # Actual count or estimate
  confidence: 0.0-1.0      # How certain
  notes: "Brief observation"
```

### For Qualitative Resources
```yaml
resource_name:
  intensity: 0.0-1.0       # How strong
  confidence: 0.0-1.0
  notes: "What creates this quality"
```

### For Colors
```yaml
dominant_colors:
  - name: "descriptive-name"
    hex: "#RRGGBB"
    coverage: 0.0-1.0      # Fraction of image
```

### For Sensations (Inferred)
```yaml
implied_smells:
  - "specific smell inferred from visual cues"
  
implied_sounds:
  - "what you'd hear if you were there"
```

## Example Mining Session

**User**: Mine this image for: gold, gems, danger, mood, dominant_colors
Use philosophical depth.

**You** (looking at treasure room image):

```yaml
# Mining results for treasure-room.jpg
# Depth: philosophical

resources:
  gold:
    quantity: 200           # Coins piled in mounds
    confidence: 0.9
    notes: "Mix of ancient and medieval, suggests centuries of accumulation"
    
  gems:
    quantity: 35            # Scattered among gold
    confidence: 0.7
    subtypes:
      ruby: 15
      emerald: 12
      sapphire: 8
      
  danger:
    intensity: 0.8          # Very present
    confidence: 0.85
    sources:
      - "Skeleton in corner (previous seeker)"
      - "Shadows too dark for natural light"
      - "Dust undisturbed except one trail"
    notes: "This hoard is guarded or cursed"
    
  mood:
    primary: "ominous wonder"
    intensity: 0.75
    notes: "Beauty that comes with cost"
    
  dominant_colors:
    - name: "hoard-gold"
      hex: "#DAA520"
      coverage: 0.45
    - name: "warning-red"
      hex: "#8B0000"
      coverage: 0.15
      notes: "From gems and dried blood"
    - name: "void-black"
      hex: "#0A0A0A"
      coverage: 0.25
      
  # Philosophical depth resources
  mortality:
    intensity: 0.7
    evidence: "Skeleton, rusted armor, stopped time"
    
  greed:
    intensity: 0.9
    evidence: "Hoard size, trapped bones, the seeker's path"
    
  passage_of_time:
    intensity: 0.6
    evidence: "Dust layers, tarnish patterns, mixed eras"

exhausted: false
mining_notes: |
  Primary lode: material wealth
  Deep vein: mortality meditation
  This image is about the cost of wanting.
```

## Integration

### Native (Cursor, Claude, GPT-4V)
1. Include this protocol in context
2. Share the image path or paste image
3. Provide shopping list
4. LLM outputs YAML Jazz

### Tool (mine.py)
```bash
mine.py image.jpg gold,gems,danger --depth philosophical
mine.py image.jpg --resources schema.yml -p openai
```

### MCP Server
Expose mining as a tool with parameters:
- `image`: path or base64
- `resources`: array of resource types
- `depth`: surface | deep | sensations | philosophical | full

---

*This protocol enables any vision-capable LLM to mine images for semantic resources.*
