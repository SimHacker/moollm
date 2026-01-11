---
name: image-mining
description: "I mine pixels for atoms. Reality is just compressed resources."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
related: [visualizer, logistic-container, postal, adventure]
---

# Image Mining

> *"I mine pixels for atoms. Reality is just compressed resources."*
>
> *"Every image is a lode. Every pixel, potential ore."*

**Image Mining** extends the Kitchen Counter's DECOMPOSE action to **images**.

Your camera isn't just a recorder — it's a **PICKAXE FOR VISUAL REALITY**.

---

## The Core Insight

```
📷 Camera Shot  →  🖼️ Image  →  ⛏️ MINE  →  💎 Resources
```

Just like the Kitchen Counter breaks down:
- `sandwich` → `bread + cheese + lettuce`
- `lamp` → `brass + glass + wick + oil`
- `water` → `hydrogen + oxygen`

**Images** can be broken down into:
- `ore_vein.png` → `iron-ore × 12` + `stone × 8`
- `forest.png` → `wood × 5` + `leaves × 20` + `seeds × 3`
- `treasure_pile.png` → `gold × 100` + `gems × 15`
- `sunset.png` → `orange_hue × 1` + `warmth × 1` + `nostalgia × 1`

---

## Two Image Sources

### 1. Generated Images (AI creates from prompt)

```yaml
postal:
  type: text
  to: "visualizer"
  body: "Take a photo of that ore vein on the wall"
  
  attachments:
    - type: image
      action: generate
      prompt: "Rich iron ore vein in cavern wall, glittering..."
```

### 2. Real Photos (Upload from phone/camera)

```yaml
postal:
  type: text
  to: "miner"
  body: "Here's a photo of the treasure room"
  
  attachments:
    - type: image
      action: upload
      source: "camera_roll"      # Or file upload
      file: "treasure-room.jpg"
```

**Both become mineable resources!**

---

## How Mining Works

### Step 1: ANALYZE (LLM scans for resources)

The LLM looks at the image AND checks what resources are **currently requested** by the logistics network:

```yaml
analyze:
  image: "treasure-room.jpg"
  
  # LLM knows what's NEEDED from logistics requesters
  logistics_context:
    active_requests:
      - { item: "gold", requester: "forge/", needed: 100 }
      - { item: "gems", requester: "jewelry-shop/", needed: 50 }
      - { item: "iron-ore", requester: "smelter/", needed: 200 }
      
  # LLM identifies what CAN BE MINED that matches requests
  analysis_prompt: |
    Look at this image. What resources can you identify?
    Prioritize resources that match these requests: {requests}
    For each resource, estimate quantity available.
```

### Step 2: INSTANTIATE (Resource map attached to image)

The LLM returns a resource mapping that gets stored ON the image:

```yaml
image:
  id: "treasure-room-photo"
  file: "treasure-room.jpg"
  type: mineable-image
  
  # === RESOURCE MAP (instantiated by LLM analysis) ===
  resources:
    gold:
      total: 150           # Total available
      remaining: 150       # Not yet mined
      per_turn: 10         # Can extract 10 per turn
      
    gems:
      total: 45
      remaining: 45
      per_turn: 5
      
    ancient-coins:
      total: 30
      remaining: 30
      per_turn: 3
      rare: true           # Bonus find!
      
    dust:
      total: 500
      remaining: 500
      per_turn: 50
      value: low
      
  # Metadata
  analyzed_at: "2026-01-10T14:30:00Z"
  exhausted: false
```

### Step 3: MINE (Progressive extraction, N per turn)

Each turn, you can mine resources from the image:

```yaml
action: MINE
target: "treasure-room-photo"

# This turn's extraction (limited by per_turn rates)
result:
  extracted:
    - item: gold
      quantity: 10         # per_turn limit
      destination: "forge/"
      
    - item: gems
      quantity: 5
      destination: "jewelry-shop/"
      
  # Image state updated
  image_state:
    resources:
      gold:
        remaining: 140     # Was 150, mined 10
      gems:
        remaining: 40      # Was 45, mined 5
    exhausted: false
```

### Step 4: EXHAUSTION (Sucked dry!)

After enough mining turns, resources run out:

```yaml
# After 15 turns of mining gold...
image_state:
  resources:
    gold:
      total: 150
      remaining: 0         # EXHAUSTED!
      per_turn: 10
      exhausted: true
      
    gems:
      total: 45
      remaining: 0         # EXHAUSTED!
      per_turn: 5
      exhausted: true
      
    ancient-coins:
      total: 30
      remaining: 0
      per_turn: 3
      exhausted: true
      
  exhausted: true          # Whole image sucked dry!
  
  # Narrative
  description: |
    The treasure room photo has been thoroughly mined.
    Every glinting surface has been extracted, every
    coin accounted for. The image looks... drained.
    Faded. Like a photocopy of a photocopy.
```

**Once exhausted, you can't mine that image anymore!**

---

---

## Demand-Driven Discovery

**The LLM prioritizes what the logistics network NEEDS!**

```yaml
# The smelter is requesting iron ore
logistic-container:
  id: smelter
  mode: requester
  request_list:
    - { item: "iron-ore", count: 200, priority: high }
    - { item: "coal", count: 100, priority: medium }

# Player takes a photo of a cave wall
# LLM analyzes and finds:
analysis:
  image: "cave-wall.jpg"
  
  found_resources:
    iron-ore: 80           # "I see iron ore veins! The smelter needs this!"
    copper-ore: 30         # Also present but not requested
    quartz: 50             # Background mineral
    cave-moss: 100         # Organic material
    
  priority_matching:
    - resource: iron-ore
      matches_request: true
      requester: "smelter/"
      highlight: "⭐ HIGH PRIORITY — Smelter needs this!"
```

The LLM acts as a **smart prospector** that knows what's valuable based on current demand!

### Discovery Modes

| Mode | What LLM Looks For |
|------|-------------------|
| `demand` | Only resources with active requests |
| `opportunistic` | Requested resources + valuable extras |
| `thorough` | Everything mineable in the image |
| `philosophical` | Abstract concepts, emotions, meanings |

```yaml
mine:
  target: "sunset-beach.jpg"
  mode: philosophical
  
  # LLM finds abstract resources
  resources:
    nostalgia: 15
    warmth: 30
    passage-of-time: 5
    beauty: 20
    sand: 10000          # Also the literal stuff
```

---

## Mining Yields

Different image types yield different resources:

### 🏔️ Natural Resources

| Image Type | Yields |
|------------|--------|
| Ore vein | `iron-ore`, `copper-ore`, `gold`, `gems` |
| Forest | `wood`, `leaves`, `seeds`, `birds` |
| Ocean | `water`, `salt`, `fish`, `seaweed` |
| Mountain | `stone`, `minerals`, `snow`, `air` |
| Desert | `sand`, `glass`, `heat`, `mirage` |
| Sky | `clouds`, `light`, `space`, `dreams` |

### 🏛️ Constructed

| Image Type | Yields |
|------------|--------|
| Building | `stone`, `wood`, `glass`, `inhabitants` |
| Machinery | `gears`, `pipes`, `steam`, `purpose` |
| Treasure pile | `gold`, `gems`, `artifacts`, `curses` |
| Library | `books`, `knowledge`, `dust`, `secrets` |

### 🎨 Abstract/Artistic

| Image Type | Yields |
|------------|--------|
| Sunset | `colors`, `warmth`, `nostalgia`, `time` |
| Portrait | `personality`, `mood`, `secrets`, `stories` |
| Abstract art | `shapes`, `feelings`, `confusion`, `inspiration` |
| Text/writing | `words`, `meaning`, `intent`, `language` |

### 🌌 Philosophical (Deep Mining)

Just like the Kitchen Counter goes from `practical` → `chemical` → `atomic` → `philosophical`:

| Depth | What You Mine |
|-------|---------------|
| Surface | Objects, materials |
| Deep | Emotions, concepts |
| Sensations | Colors, smells, attitudes, feelings |
| Quantum | Probabilities, observations |
| Philosophical | Meaning, existence, narrative |

```yaml
deep_mining:
  target: "sunset.png"
  depth: philosophical
  
  yields:
    - item: "the-passage-of-time"
      quantity: 1
      type: abstract
      
    - item: "mortality-awareness"
      quantity: 1
      type: existential
      warning: "This may cause introspection"
      
    - item: "beauty-that-fades"
      quantity: 1
      type: poetic
```

### 🎨 Sensation Mining

Extract colors, smells, textures, moods:

```yaml
sensation_mining:
  target: "farmers-market.jpg"
  depth: sensations
  
  yields:
    # Colors
    - item: "tomato-red"
      quantity: 40
      type: color
      hex: "#FF6347"
      
    - item: "basil-green"
      quantity: 25
      type: color
      hex: "#228B22"
      
    # Smells (imagined from visual cues)
    - item: "fresh-bread-aroma"
      quantity: 10
      type: smell
      intensity: warm
      
    - item: "ripe-fruit-sweetness"
      quantity: 30
      type: smell
      
    # Attitudes/Feelings
    - item: "weekend-morning-calm"
      quantity: 5
      type: attitude
      
    - item: "abundance"
      quantity: 20
      type: feeling
      
    # Textures
    - item: "rough-burlap"
      quantity: 15
      type: texture
      
    - item: "sun-warmed-wood"
      quantity: 8
      type: texture
```

**Use these in crafting:**
- Combine `tomato-red` + `canvas` → painted artwork
- Combine `fresh-bread-aroma` + `room` → ambiance modifier
- Combine `weekend-morning-calm` + `character` → mood buff

---

## The Mineable Property

Any object or image can have a `mineable` property:

```yaml
object:
  name: Ancient Ore Painting
  type: artwork
  
  description: |
    A painting of a rich ore vein. But wait...
    is that actual ore embedded in the canvas?
    
  mineable:
    enabled: true
    yields:
      - item: iron-ore
        quantity: [5, 15]    # Range: 5-15 per mine
        
      - item: copper-ore
        quantity: [2, 8]
        
      - item: artistic-essence
        quantity: 1
        rare: 0.3            # 30% chance
        
    exhaustion:
      max_mines: 3           # Can mine 3 times before exhausted
      diminishing: 0.5       # Each mine yields 50% less
      regenerates: false     # Once exhausted, stays exhausted
      
    side_effects:
      - "The painting fades slightly with each extraction"
      - "You feel the artist's disappointment"
```

---

## Mining Tools

Different tools affect mining yields:

### 📷 Camera (Default)

```yaml
tool: camera
efficiency: 1.0
specialty: "Captures visual resources"
can_mine: [images, scenes, visible_objects]
```

### 🔬 Analyzer

```yaml
tool: analyzer
efficiency: 1.5
specialty: "Chemical/atomic resources"
can_mine: [materials, substances, compounds]
```

### 🔮 Oracle Eye

```yaml
tool: oracle_eye
efficiency: 2.0
specialty: "Abstract/philosophical resources"
can_mine: [emotions, concepts, meanings, futures]
```

### ⛏️ Reality Pickaxe

```yaml
tool: reality_pickaxe
efficiency: 3.0
specialty: "Everything, but dangerous"
can_mine: [anything]
warning: "May collapse local reality"
```

---

## Integration with Logistics

Mined resources flow into the logistics system:

```yaml
mining_config:
  default_destination: "inventory"
  
  routing:
    # Route by resource type
    - match: { tags: ["ore"] }
      destination: "nw/ore-storage/"
      
    - match: { tags: ["organic"] }
      destination: "ne/organic-materials/"
      
    - match: { tags: ["abstract"] }
      destination: "sw/concepts/"
      
  postal_delivery:
    enabled: true
    method: text        # Instant delivery!
```

---

## Camera Phone Integration

Your phone camera is THE mining interface:

### Real Photo Workflow

```yaml
phone_mining:
  # 1. CAPTURE: Take photo or upload
  capture:
    sources:
      - camera: "Take new photo"
      - gallery: "Upload from camera roll"
      - url: "Import from web"
      
  # 2. ANALYZE: LLM scans for resources
  on_capture:
    action: analyze
    context: logistics_requests    # What's needed?
    show_preview: true
    
  # 3. CONFIRM: Accept resource mapping
  on_confirm:
    action: instantiate
    attach_resources: true         # Store on image
    
  # 4. MINE: Extract over time
  on_mine:
    per_turn: true                 # N resources per turn
    auto_route: logistics          # Send to requesters
```

### Example: Photo Mining Flow

**1. You take a photo of a rock formation:**

```
📷 *snap*

Analyzing photo for mineable resources...
Checking logistics requests...

Found in image:
├── 🪨 granite     × 200   (10/turn)
├── �ite iron-ore   × 45    (5/turn)  ⭐ NEEDED by smelter!
├── 💎 quartz      × 12    (2/turn)
└── 🦎 fossil      × 1     (rare find!)

[MINE] [CANCEL]
```

**2. You confirm. Resource map attached:**

```yaml
image:
  id: rock-formation-001
  file: "IMG_2847.jpg"
  resources:
    granite: { total: 200, remaining: 200, per_turn: 10 }
    iron-ore: { total: 45, remaining: 45, per_turn: 5 }
    quartz: { total: 12, remaining: 12, per_turn: 2 }
    fossil: { total: 1, remaining: 1, per_turn: 1 }
```

**3. Each turn, you mine:**

```
Turn 1: Mined 10 granite, 5 iron-ore, 2 quartz
        → Iron ore sent to smelter (requester)
        → Granite sent to storage
        
Turn 2: Mined 10 granite, 5 iron-ore, 2 quartz
        Remaining: granite 180, iron-ore 35, quartz 8

...

Turn 9: Mined 10 granite, 5 iron-ore (last 5!)
        ⚠️ Iron-ore EXHAUSTED
        
Turn 20: Mined last 10 granite
         📷 IMAGE FULLY MINED — no more resources!
```

**4. Exhausted image:**

```yaml
image:
  id: rock-formation-001
  exhausted: true
  
  visual_effect: |
    The photo appears faded, almost translucent.
    Like the minerals were literally pulled out of it.
    A ghost of a photograph.
```

### AR Overlay (Future)

```yaml
ar_overlay:
  # Point camera at scene
  live_view:
    show_resources: true
    icons_float: true
    
  # Visual indicators
  indicators:
    - resource_type: "icon + label"
    - quantity: "number overlay"
    - priority: "⭐ for requested items"
    - exhaustion: "fade as mined"
    
  # Example view:
  #   🪨 200  ⚫ 45 ⭐  💎 12
  #   (floating over rock formation)
```

---

## DECOMPOSE vs MINE

| DECOMPOSE (Counter) | MINE (Camera) |
|---------------------|---------------|
| Physical items | Images, scenes, visuals |
| Requires counter | Requires camera/tool |
| Consumes item | May or may not consume |
| Returns components | Returns resources |
| Kitchen-focused | World-focused |

**They're complementary!**

- DECOMPOSE the **physical object** on the counter
- MINE the **image/representation** of anything

---

## Reality Mining (Advanced)

At the deepest level, you're not just mining images — you're mining **reality itself**:

```yaml
reality_mining:
  level: transcendent
  
  # The image IS the territory
  insight: |
    When you mine an image, you're extracting
    compressed information. But all reality is
    compressed information. Images are just
    explicit about it.
    
  implications:
    - "Mining a photo of gold doesn't create gold — it REVEALS gold"
    - "The ore was always there, encoded in the pixels"
    - "Your camera doesn't capture reality — it DECOMPRESSES it"
    
  warning: |
    At this level, the distinction between
    "mining an image" and "mining reality"
    becomes philosophical.
```

---

## Actions

### MINE

```
MINE [target]
MINE [target] WITH [tool]
MINE [target] TO [destination]
```

### SCAN

```
SCAN [target]           # Preview yields without mining
SCAN AREA               # Scan visible area for mineable resources
```

### PROSPECT

```
PROSPECT [direction]    # Check for mineable resources in direction
PROSPECT DEEP           # Deep scan for rare/hidden resources
```

---

## Example: Mining the Maze

```yaml
# Player in dark maze corridor
# Takes photo with lamp light

action: MINE "dark-corridor.png"

result:
  yields:
    - item: darkness
      quantity: 100
      type: abstract
      note: "Bottled darkness, useful for stealth"
      
    - item: fear
      quantity: 15
      type: emotion
      note: "Crystallized fear, grue-adjacent"
      
    - item: mystery
      quantity: 5
      type: narrative
      note: "Pure narrative potential"
      
    - item: stone-dust
      quantity: 50
      type: material
      
  rare_find:
    - item: "ancient-writing"
      quantity: 1
      note: "Hidden message in the shadows!"
      unlocks: "Secret passage revealed"
```

---

## The Mining Economy

Resources have value and flow:

```yaml
resource_economy:
  # Raw resources → processing → products
  
  chains:
    - ore → smelter → ingots → forge → tools
    - wood → sawmill → planks → workshop → furniture
    - images → mining → resources → crafting → items
    
  # Images as a resource type!
  image_value:
    unique_photo: high      # Original content
    copy: low               # Duplicated content
    AI_generated: medium    # Generated on demand
    
  # Mining generates content
  content_creation: |
    When you MINE an image, you're not just extracting
    resources — you're creating YAML files for them.
    Each resource becomes a game object.
```

---

## Dovetails With

- **[Visualizer](../visualizer/)** — Images to mine
- **[Logistic Container](../logistic-container/)** — Resource storage
- **[Postal](../postal/)** — Camera integration, delivery
- **[Kitchen Counter](../../examples/adventure-4/kitchen/counter.yml)** — DECOMPOSE pattern
- **[Adventure](../adventure/)** — World integration

---

## Philosophy

> *"In Minecraft, you punch trees to get wood."*
> *"In MOOLLM, you photograph ore to get resources."*
>
> The camera is a cognitive tool that **extracts meaning from reality**.
> Mining is just making that extraction explicit and measurable.
>
> Every image is a compressed representation of resources.
> Mining decompresses it.

---

*See YAML frontmatter at top of this file for full specification.*
