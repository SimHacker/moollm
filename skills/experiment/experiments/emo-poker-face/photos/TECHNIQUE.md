# Photo-Hands Analysis Technique

## Overview

Time-travel photography of key poker moments, capturing tells in visual form.

## Process

### 1. Schematic Prompt (YML)

Create structured reference with pointers:

```yaml
photo:
  id: "H01-bumblewick-aces"
  source:
    run: "four-player-001.yml"
    hand: 1
    phase: "preflop"
    line_range: "76-95"
    
  scene:
    ref: "SCENE.yml#setting"
    lighting: "tension"
    
  camera:
    angle: "over_shoulder"
    subject: "bumblewick"
    shows: ["bumblewick cards", "opponents faces"]
    
  characters:
    bumblewick:
      ref: "SCENE.yml#characters.bumblewick"
      state: "nervous"
      tells_active: ["trembling hands", "ear droop"]
      cards_visible: [A♠, A♥]
      
    opponents:
      - don: { ref: "SCENE.yml#characters.don_hopkins", expression: "curious" }
      - palm: { ref: "SCENE.yml#characters.palm", expression: "alert" }
      - donna: { ref: "SCENE.yml#characters.donna_toadstool", expression: "skeptical" }
      
  moment: "First raise with pocket aces, trembling"
```

### 2. Resolve References

Expand all `ref:` pointers into full descriptions.

### 3. Synthesize Visual Prompt

Combine into coherent image generation prompt:
- Scene setting (lighting, atmosphere)
- Camera position and framing
- Subject character (detailed)
- Background characters (expressions)
- Key objects (cards, chips, cheese)
- Emotional tone

### 4. Generate Image

Use visualizer skill or image generation tool.

### 5. Mine Tells

Analyze generated image for:
- Facial expressions
- Body language
- Hand positions
- Object interactions
- Micro-expressions
- Environmental tells (steam, shadows)

## Photo Catalog Structure (Flat, Big-Endian)

```
photos/
├── SCENE.yml                           # Canonical scene cache
├── TECHNIQUE.md                        # This file
├── H01-bumblewick-first-aces.yml       # Schematic prompt
├── H01-bumblewick-first-aces.txt       # Resolved prompt
├── H01-bumblewick-first-aces.png       # Generated image
├── H01-bumblewick-first-aces-tells.yml # Tell mining results
└── ...
```

All files for one photo share the same base name (big-endian: H##-description).

## Generating Images

Use the visualizer skill to generate images from prompts:

```bash
# Set API key first
export GOOGLE_API_KEY=...  # or OPENAI_API_KEY, etc.

# Generate from YML context files
cd skills/experiment/experiments/emo-poker-face/photos
python3 ../../../../visualizer/visualize.py H01-bumblewick-first-aces.yml SCENE.yml -p google -v detailed

# Or use the resolved .txt prompt directly
python3 ../../../../visualizer/visualize.py SCENE.yml --raw-prompt "$(cat H01-bumblewick-first-aces.txt)" -p google
```

The image will be saved with the same base name (big-endian):
- `H01-bumblewick-first-aces.yml` → `H01-bumblewick-first-aces.png`

## Key Moments to Photograph

| ID | Hand | Moment | Subject | Tells to Capture |
|----|------|--------|---------|------------------|
| H01 | 1 | First aces raise | Bumblewick | Trembling, ear droop |
| H03 | 3 | Palm eliminates Donna | Donna | Throat pouch, standing |
| H05 | 5 | Donna's slowplay reveal | Donna | Controlled stillness |
| H07 | 7 | "Donna showed me the trap" | Bumblewick | Steady hands, pride |
| H09 | 9 | Cheese knife with set | Don | Multitasking confidence |
| H11a | 11 | Kings revealed | Bumblewick | Putting down cheese |
| H11b | 11 | Wheel hits | Palm | Fur ripple, first smile |
| H11c | 11 | Graceful loss | Bumblewick | No tears, cheese nibble |

## Scene Coherency Rules

1. **Consistent characters**: Same clothing, proportions across shots
2. **Consistent setting**: Same table, chairs, lighting style
3. **Chip stacks reflect game state**: Match actual stack sizes
4. **Cards accurate**: Use real hands from run data
5. **Cheese board state**: Progressive consumption
6. **Time of night**: Lighting shifts subtly (bright → intimate)
