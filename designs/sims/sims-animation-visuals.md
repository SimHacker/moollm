# Sims Animation & Visuals → MOOLLM

> *Character Animation, Thought Balloons, Censorship*
> *Showing the inner through the outer.*

## Visual Storytelling

The Sims used visuals to communicate internal state:
- **Animations** showed what characters were doing
- **Thought balloons** showed what they were thinking
- **Speech balloons** showed conversation topics
- **Censorship pixelation** preserved dignity

MOOLLM translates these to prose, description, and metadata.

---

## Character Animation

**Sims:** Complex animation system:

| Component | Function |
|-----------|----------|
| **Suits** | Body mesh (outfit) |
| **Heads** | Face mesh + expressions |
| **Hands** | Gesture animations |
| **Bodies** | Full body motions |
| **Accessories** | Carried objects |

Animations mixed dynamically:
```
Walking + Carrying Baby + Looking Tired = 
  composite animation blending all three
```

**MOOLLM:** Description as animation:

```yaml
# characters/palm/APPEARANCE.yml
base:
  species: spider_monkey
  fur: golden
  eyes: expressive, dark
  
current_state:
  posture: relaxed
  activity: writing
  expression: contemplative
  holding: fountain pen
```

When narrating:

> "Palm sits at his desk, pen moving thoughtfully across paper. His tail curls around the chair leg for balance, ears twitching occasionally at pub sounds below."

The LLM "animates" through description.

---

## Vitaboy System

**Sims:** The Vitaboy character system:

```
Vitaboy Components:
├── Skeleton (bone hierarchy)
├── Skins (mesh data)
├── Animations (motion data)
├── Appearances (skin + textures)
└── Outfits (combined appearance sets)
```

Enabled:
- Mix-and-match character creation
- Age transitions (same character, new body)
- Career uniforms (temporary appearance change)

**MOOLLM:** Layered appearance:

```yaml
# characters/palm/APPEARANCE.yml
base:
  physical: spider_monkey, young adult
  
layers:
  - mood_modifier: when tired, drooping posture
  - activity_modifier: when writing, focused expression
  - social_modifier: when hosting, expansive gestures
  
costumes:
  casual: "natural fur, comfortable"
  drag: "Madame Palm persona — see below"
  formal: "small bowtie, dignified"
```

---

## Thought Balloons

**Sims:** Visual thought indicators:

```
💭 + 🍕 = Hungry, wants pizza
💭 + 💤 = Tired, wants sleep  
💭 + 👤❤️ = Thinking of love interest
💭 + 💀 = Scared/death-related thought
💭 + 🎮 = Wants to play
```

Quick visual read of internal state.

**MOOLLM:** Thought in MIND-MIRROR:

```yaml
# characters/palm/MIND-MIRROR.yml
current_thoughts:
  surface: "This essay is almost done"
  background: 
    - "Don would appreciate this insight"
    - "Is the banana tree getting enough light?"
  mood_indicator: focused_contentment
```

Or inline in narrative:

> Palm paused, pen hovering. *The infinite typewriters,* he thought. *Each keystroke a choice, each word a universe pruned away.*

---

## Speech Balloons

**Sims:** Conversation indicators:

```
🗣️ + ⚽ = Talking about sports
🗣️ + 🏠 = Discussing house/home
🗣️ + 👤👤 = Gossiping about someone
🗣️ + 😆 = Telling a joke
```

Showed topic without actual dialogue.

**MOOLLM:** Actual dialogue:

```markdown
## Conversation at the Bar

**Maurice:** "Your essay on consciousness — I couldn't 
stop thinking about it."

**Palm:** "Really? I wasn't sure if the typewriter 
metaphor worked."

**Maurice:** "It's perfect. Each key, each choice... 
it captures something true."
```

Real dialogue instead of icons.

---

## Censorship Pixelation

**Sims:** The famous censor blur:

```
When showing:
- Bathroom usage
- Changing clothes
- Certain intimate actions

Display: pixelated mosaic over character
```

Preserved dignity while acknowledging action happened.

**MOOLLM:** Tasteful narration:

```yaml
# skills/representation-ethics/CARD.yml
nsfw_handling:
  principle: tasteful acknowledgment
  
  techniques:
    - fade_to_black: "The door closed softly behind them."
    - time_skip: "Morning found them..."
    - euphemism: "They expressed their affection."
    - off_screen: "Sounds from the bathroom indicated Palm had found relief."
```

Dignity preserved through prose, not pixels.

---

## Invisibility

**Sims:** Some objects were invisible:

```
Invisible objects:
- Pedestrian portal (where visitors spawn)
- Sound emitters
- Controller objects
- Debug markers
```

Shown in Edith, hidden in game.

**MOOLLM:** System files vs. narrative:

```yaml
# Visible to players:
pub/bar/bartender.yml

# Hidden from narrative (but exists):
pub/.meta/spawn-points.yml
kernel/protocols/entry.yml
```

Or flagged in YAML:

```yaml
# pub/technical/sound-emitter.yml
visible_in_narrative: false
function: ambient_sound_source
```

---

## Draw Groups

**Sims:** Rendering order:

```
Draw Order (back to front):
1. Terrain
2. Floor tiles
3. Shadows
4. Furniture
5. Objects on furniture
6. Sims
7. Carried objects
8. Effects/particles
9. UI overlays
```

**MOOLLM:** Description order:

The LLM naturally describes in logical order:

> "The pub's amber lighting cast long shadows across worn wooden floors. At the bar, Marieke polished a glass. Near the window, Palm sat writing, morning light catching his fur. A half-eaten banana rested beside his notebook."

Setting → characters → details.

---

## Standard Heights (Visual)

**Sims:** Camera and placement heights:

```
Camera heights:
  WALL = eye level
  FLOOR = looking down
  ROOF = bird's eye
  
Object heights:
  GROUND = 0 (rugs, pets)
  TABLE = 2 (surfaces)
  STANDING = 6 (adult height)
```

**MOOLLM:** Perspective in prose:

```markdown
## From Palm's Perspective

The pub floor stretched below his perch. From the 
jungle gym, he could see:
- The bar counter where Marieke worked
- The stage where tonight's show would happen
- The cozy corner where Don usually sat

*A monkey's view of the world.*
```

---

## Animation Tables

**Sims:** Animation references:

```
Animation Table:
  ID | Name          | Duration | Loop
  01 | a2o-walk      | 24 frames| yes
  02 | a2o-sit       | 18 frames| no
  03 | a2o-eat       | 45 frames| no
  04 | a2o-talk      | 30 frames| yes
```

**MOOLLM:** Action descriptions:

```yaml
# skills/action-library/walking.yml
WALK:
  description: "Character moves between locations"
  
  variations:
    hurried: "Quick, purposeful strides"
    casual: "Relaxed amble, taking in surroundings"
    tired: "Slow, heavy steps"
    excited: "Almost bouncing, eager"
```

---

## Emotion Display

**Sims:** Facial expressions and body language:

| Emotion | Face | Body |
|---------|------|------|
| Happy | Smile | Upright, bouncy |
| Sad | Frown | Slouched, slow |
| Angry | Scowl | Tense, aggressive |
| Scared | Wide eyes | Hunched, trembling |
| Tired | Droopy | Slow, heavy |

**MOOLLM:** Emotional description:

```yaml
# In narrative:
emotional_tells:
  happy: "Palm's tail swung in wide arcs"
  focused: "Ears flattened, eyes intent on the page"
  excited: "Bouncing slightly, words tumbling out"
  tired: "Movements slow, eyes half-lidded"
```

---

## Carrying Animations

**Sims:** Objects affected how Sims moved:

```
Carrying modes:
- One hand (book, phone)
- Two hands (baby, pizza box)
- Over shoulder (guitar)
- Pushing (cart)
```

Walking animations adjusted for carried items.

**MOOLLM:** Inventory affects description:

```yaml
# characters/palm/inventory.yml
carrying:
  - fountain_pen: in hand
  - notebook: under arm
  
# This affects narrative:
# "Palm approached, pen still in hand, notebook 
# tucked against his side."
```

---

## Image Prompts

**Sims:** No image generation — 3D rendering.

**MOOLLM:** Explicit image prompts:

```yaml
# characters/palm/IMAGE-PROMPTS.yml
portrait:
  style: digital painting, warm lighting
  subject: golden-furred spider monkey
  pose: thoughtful, pen in hand
  setting: cozy study with typewriters
  mood: contemplative, gentle
  
action:
  style: dynamic illustration
  subject: Palm writing at desk
  details: scattered papers, banana peel
  lighting: desk lamp, amber glow
```

Ready for image generation tools.

---

## The Visual-to-Verbal Translation

The Sims communicated through visuals. MOOLLM communicates through prose. The translation:

| Sims Visual | MOOLLM Verbal |
|-------------|---------------|
| Walk animation | "Palm crossed the room" |
| Thought balloon | `current_thoughts:` in YAML |
| Facial expression | "His expression softened" |
| Censor blur | "The door closed behind them" |
| Draw groups | Natural description order |
| Animation mixing | Rich, compound sentences |
| Costume changes | Appearance layer updates |

Same information, different medium.

---

## See Also

- [characters/palm/APPEARANCE.yml](../examples/adventure-4/characters/palm/APPEARANCE.yml) — Appearance definition
- [characters/palm/IMAGE-PROMPTS.yml](../examples/adventure-4/characters/palm/IMAGE-PROMPTS.yml) — Image generation
- [skills/mind-mirror/](../skills/mind-mirror/) — Internal state display
- [skills/representation-ethics/](../skills/representation-ethics/) — Appropriate depiction
- [sims-personality-motives.md](./sims-personality-motives.md) — The inner states being displayed

---

*"Character Animation Suits Heads Hands Bodies Accessories... Censorship Invisibility"*

What the Sims showed, MOOLLM describes.
