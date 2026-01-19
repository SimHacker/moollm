# ⛏️📷 Image Mining

> *"Mine pixels for atoms. Reality is compressed resources."*

## Two Modes

### Native Mode (Cursor, Claude, GPT-4V, Gemini)

**No tool needed.** The LLM has vision — it just LOOKS at the image and mines.

```
You: Look at /path/to/treasure.jpg and mine it for:
     gold, gems, danger, mood, dominant_colors
     Use philosophical depth.

LLM: *looks at image*
     *outputs YAML Jazz with quantities and insights*
```

Include `PROTOCOL.md` in context for best results.

### Tool Mode (Automation)

Use `mine.py` for scripts, pipelines, or calling external LLMs:

```bash
mine.py treasure.jpg gold,gems,danger --depth philosophical -p openai
mine.py scene.jpg --resources schema.yml -p anthropic
```

---

## Quick Reference

| Action | What It Does |
|--------|--------------|
| `MINE [image]` | Extract resources from image |
| `SCAN [image]` | Preview yields without full extraction |
| `PROSPECT [dir]` | Detect mineable resources nearby |

## The Idea

Your **camera is a PICKAXE** for visual reality.

```
📷 Photo → 🖼️ Image → ⛏️ MINE → 💎 Resources!
```

Just like the Kitchen Counter's DECOMPOSE breaks down:
- `sandwich` → `bread + cheese + lettuce`

Image Mining breaks down:
- `ore_vein.png` → `iron × 12 + stone × 8`
- `forest.png` → `wood × 5 + leaves × 20`
- `sunset.png` → `warmth × 1 + nostalgia × 1 + #FF7F50 color`

## Resource Types (Anything!)

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

| Depth | What You Mine |
|-------|---------------|
| `surface` | Objects, materials, colors visible |
| `deep` | Emotions, concepts, atmosphere |
| `sensations` | Colors (hex), textures, smells, sounds |
| `philosophical` | Meaning, existence, symbolism |
| `full` | All of the above |

## Output (YAML Jazz)

```yaml
resources:
  gold:
    quantity: 150           # Piles of ancient coins
    confidence: 0.85
    notes: "Mix of Roman and medieval"
    
  danger:
    intensity: 0.7          # Something lurks
    notes: "Shadows too dark for natural light"
    
  dominant_colors:
    - name: "treasure-gold"
      hex: "#DAA520"
      coverage: 0.45

exhausted: false
mining_notes: "Rich lode. Philosophical mining yields mortality themes."
```

## Files

| File | Purpose |
|------|---------|
| `PROTOCOL.md` | **Concise mining instructions for LLMs** |
| `SKILL.md` | Full documentation |
| `CARD.yml` | Skill card and interface |
| `mine.py` | Sister script for automation |
| `images/INDEX.yml` | Pre-analyzed mineable images |

## Making Something Mineable

```yaml
object:
  name: Ancient Ore Painting
  
  mineable:
    enabled: true
    yields:
      - item: iron-ore
        quantity: [5, 15]    # Range
      - item: artistic-essence
        quantity: 1
        rare: 0.3            # 30% chance
    exhaustion:
      max_mines: 3
      diminishing: 0.5
```

## Integrates With

- **[visualizer](../visualizer/)** — Creates images to mine (generation ↔ extraction)
- **Logistics** — Mined resources route to containers
- **Postal** — Camera triggers mining, instant delivery
- **Kitchen Counter** — DECOMPOSE pattern extended to images
