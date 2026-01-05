---
name: cat
description: Feline interactions, buffs, and relationship building
allowed-tools:
  - file_read
  - file_write
tier: 1
protocol: CAT
tags: [pet, companion, interaction, buff, terpene]
origin: "Tamagotchi, Harvest Moon, Stardew Valley, real cats"
related: [character, buff, mind-mirror, room, adventure]
---

# CAT — The Feline Interaction Skill

> *"Cats are the original NPCs. They have their own agenda."*

A generic skill for cat interactions that instances overlay with
their specific personalities, creating unique effects per cat.

Philosophy: Cats are not just decoration. They're gameplay.

invokes:
  - mind-mirror          # Personality determines effects
  - play-learn-lift      # Learn what each cat likes
  - procedural-rhetoric  # Cats teach through interaction

## INTERACTIONS — Universal cat actions

### TOUCH INTERACTIONS — Physical contact

#### PAT

```yaml
PAT:
  command: "PAT [cat]"
  description: "Quick pat on the head"
  duration: brief
  risk: low
  base_effect: |
    A quick, friendly gesture. Most cats tolerate this.
    Effect depends on cat's Outgoing and Nice traits.
  
  success_calculation: |
    success_chance = (cat.nice + cat.outgoing) / 20
    # Nice 8 + Outgoing 6 = 70% success
    
  outcomes:
    success:
      effect: "Minor charm boost"
      duration: "5 minutes"
      buff: "+1 Cheerful"
      message: "*purrs briefly*"
      
    neutral:
      effect: "No effect"
      message: "*tolerates it*"
      
    failure:
      effect: "Minor annoyance"
      debuff: "-1 to next interaction with this cat"
      message: "*ear flicks irritably*"
```

#### PET

```yaml
PET:
  command: "PET [cat]"
  description: "Extended petting session"
  duration: medium
  risk: medium
  base_effect: |
    Longer contact. Requires more cat cooperation.
    Effect depends on cat's Nice, Outgoing, and Playful traits.
    
  success_calculation: |
    success_chance = (cat.nice + cat.outgoing + cat.playful) / 30
    
  outcomes:
    success:
      effect: "Charm boost + mood lift"
      duration: "15 minutes"
      buff: "+2 Cheerful, +1 Easy-going"
      message: "*settles in, purrs contentedly*"
      
    great_success:  # Rolled on high Nice cats
      effect: "Deep bond moment"
      duration: "1 hour"
      buff: "+3 Cheerful, +2 Calm, temporary bond with cat"
      message: "*slow blink of trust*"
      
    failure:
      effect: "Rejected"
      debuff: "-1 Confidence"
      message: "*walks away with dignity*"
```

#### SCRITCH

```yaml
SCRITCH:
  command: "SCRITCH [cat]"
  aliases: ["SCRATCH", "CHIN SCRATCH", "EAR SCRATCH"]
  description: "Targeted scratching of preferred spots"
  duration: medium
  risk: medium
  requires_knowledge: true
  base_effect: |
    Expert-level interaction. Must know cat's preferences.
    Different cats like different spots: chin, ears, base of tail...
    
  knowledge_sources:
    - "Previous interactions with this cat"
    - "Observing other NPCs interact"
    - "ASK MARIEKE ABOUT [cat]'s favorite spots"
    
  success_calculation: |
    base = (cat.nice + cat.playful) / 20
    if knows_preference: base += 0.3
    
  outcomes:
    success:
      effect: "Significant mood boost"
      duration: "30 minutes"
      buff: "+2 Cheerful, +1 Playful, cat remembers you"
      message: "*tilts head into the scritch* *motor purr activates*"
      
    wrong_spot:
      effect: "Mild discomfort"
      message: "*flinches* *gives you a look*"
      learning: "Now you know: not THAT spot"
```

#### BELLY_RUB

```yaml
BELLY_RUB:
  command: "RUB [cat]'S BELLY" 
  aliases: ["BELLY RUB", "TUMMY RUB"]
  description: "The forbidden zone"
  duration: varies
  risk: HIGH
  base_effect: |
    The belly is a TRUST TEST. Most cats will trap and bite.
    Only attempt with very high Nice cats or established trust.
    
  success_calculation: |
    # Very difficult
    success_chance = (cat.nice - 5) / 10
    if cat.nice < 7: almost_guaranteed_failure
    
  outcomes:
    success:  # Rare!
      effect: "MAJOR trust established"
      duration: "Until you leave"
      buff: "+5 bond with this cat, they follow you"
      message: "*exposes belly* *allows the forbidden touch* *purrs like a motorboat*"
      
    trap:  # Common
      effect: "The Venus Cat Trap"
      damage: "1d4 scratch damage (cosmetic)"
      message: "*CLAMP* *bunny kicks* *you knew the risks*"
      learning: "Note: This cat is NOT a belly cat"
```

#### PICK_UP

```yaml
PICK_UP:
  command: "PICK UP [cat]"
  aliases: ["HOLD", "CARRY"]
  description: "Lift and hold the cat"
  duration: varies
  risk: medium-high
  base_effect: |
    Some cats love being held. Some HATE it.
    Depends heavily on trust and cat's personality.
    
  success_calculation: |
    success = (cat.nice + cat.trusting) / 20
    if cat.active > 7: success -= 0.2  # Active cats want DOWN
    
  outcomes:
    success:
      effect: "Portable cat companion"
      duration: "Until cat decides otherwise"
      buff: "+2 Calm (cat purring against you)"
      message: "*allows lifting* *settles into arms*"
      
    squirm:
      effect: "Temporary holding"
      duration: "30 seconds"
      message: "*tolerates briefly* *begins squirming*"
      
    escape:
      effect: "Immediate rejection"
      message: "*YEET* *cat phases through your arms*"
      debuff: "-2 to next hold attempt with this cat"
```

### PLAY INTERACTIONS — Engagement activities

#### PLAY_WITH

```yaml
PLAY_WITH:
  command: "PLAY WITH [cat]"
  description: "General play interaction"
  duration: medium-long
  risk: low
  base_effect: |
    Engage the cat in play. Effect depends on cat's Playful trait.
    High Playful cats LOVE this. Low Playful cats look at you weirdly.
    
  success_calculation: |
    success = cat.playful / 10
    if cat.active > 5: success += 0.2
    
  outcomes:
    success:
      effect: "Mutual joy"
      duration: "Until one of you gets tired"
      buff: "+3 Playful, +2 Energetic, exercise!"
      message: "*POUNCE* *chase* *POUNCE AGAIN*"
      
    exhaustion:  # High Active cats
      effect: "Cat keeps going, you're tired"
      debuff: "-2 Energetic"
      message: "*cat is NOT done* *you are*"
```

#### LASER_POINTER

```yaml
LASER_POINTER:
  command: "USE LASER POINTER"
  description: "The red dot of destiny"
  duration: until_you_stop
  risk: none (physical)
  warning: |
    CAUTION: Some cats become OBSESSED.
    Always end with a "catch" (shining on a treat).
    Never just turn it off — causes existential cat crisis.
    
  outcomes:
    engagement:
      effect: "Maximum cat entertainment"
      buff: "Tired cat = calm cat (+3 Calm later)"
      message: "*pupils dilate* *full hunting mode engaged*"
      
    obsession:  # High Restless cats
      effect: "Cat cannot stop looking for the dot"
      duration: "Hours"
      message: "*still hunting* *where is it* *WHERE*"
```

### CARE INTERACTIONS — Nurturing activities

#### FEED

```yaml
FEED:
  command: "FEED [cat]"
  description: "Give food or treats"
  duration: brief
  risk: none
  base_effect: |
    Food is love. Most cats respond well.
    But picky cats (high Neat) may reject inferior offerings.
    
  success_calculation: |
    if food_quality >= cat_standards: success = 1.0
    else: success = 0.3  # They'll eat, but judge
    
  outcomes:
    success:
      effect: "Fed and happy"
      buff: "+2 bond, cat associates you with food"
      message: "*eats enthusiastically* *food is good*"
      
    picky_rejection:  # High Neat cats
      effect: "Standards not met"
      message: "*sniffs* *walks away* *standards*"
```

### COMMUNICATION — Non-physical interactions

#### SLOW_BLINK

```yaml
SLOW_BLINK:
  command: "SLOW BLINK AT [cat]"
  aliases: ["BLINK AT", "CAT KISS"]
  description: "The feline I-love-you"
  duration: instant
  risk: none
  base_effect: |
    The slow blink is cat language for trust and affection.
    Cats recognize this. They may blink back.
    
  outcomes:
    returned:
      effect: "Mutual affection acknowledged"
      buff: "+1 bond, +1 Calm, quiet moment of connection"
      message: "*blinks back slowly* *understanding*"
      
    ignored:
      effect: "They saw. They chose not to respond."
      message: "*stares* *does not blink* *mysterious*"
```

#### PSPSPS

```yaml
PSPSPS:
  command: "PSPSPS"
  description: "The universal cat summoning noise"
  duration: instant
  risk: none
  base_effect: |
    Call any nearby cat. Some come. Some don't.
    Effectiveness depends on cat's Outgoing and current mood.
    
  outcomes:
    comes:
      effect: "Cat approaches"
      message: "*ears perk* *trots over* *what do you want*"
      
    ignores:
      effect: "Cat heard you. Cat doesn't care."
      message: "*ear flick* *continues not caring*"
```

### SENSORY INTERACTIONS — Bidirectional!

#### SNIFF

```yaml
SNIFF:
  command: "SNIFF [cat]"
  aliases: ["SMELL"]
  description: "Investigate a cat's scent"
  duration: brief
  risk: low
  bidirectional: true
  base_effect: |
    Scent is information. Cats know this. Humans can learn.
    Sniffing is how cats say "hello" and "who are you?"
    
    When YOU sniff a cat: You learn about them (mood, health, where they've been).
    When a CAT sniffs you: They're gathering intel. It's a compliment.
    
  human_to_cat:
    success_calculation: |
      success = (cat.trust_level / 100) + 0.5
      # Most cats allow sniffing at familiar+ relationship
      
    outcomes:
      success:
        effect: "Scent information gained"
        learns:
          - "Cat's current mood (anxious, content, playful...)"
          - "Where cat has been recently"
          - "Health status (if trained)"
          - "Terpene notes (for the Terpene Litter)"
        relationship: { trust: +1 }
        message: |
          *You lean in. The cat allows it.*
          *Scent notes: [generated based on cat]*
          *They smell like [location] and [mood].*
          
      rejection:
        effect: "Cat pulls away"
        message: "*leans back* *not that close, please*"
        relationship: { trust: -1 }
        
  cat_to_human:
    trigger: "Cat initiates sniff (relationship 30+ or curiosity)"
    effect: "Cat is gathering information about you"
    meaning: |
      The cat is interested. They want to know:
      - Where have you been?
      - What have you touched?
      - Are you safe?
      - Do you have food?
    outcomes:
      thorough_sniff:
        message: |
          *The cat approaches. Nose working.*
          *Sniff. Sniff sniff. Extended analysis.*
          *You are being CATALOGUED.*
        relationship: { fondness: +1 }
        
      quick_sniff:
        message: "*brief sniff* *acceptable*"
        
      recoil:
        message: |
          *sniff* *pause* *sniff again*
          *The cat makes a face. What have you been DOING?*
        note: "You smell like something the cat doesn't like"
        
  cat_to_cat:
    description: |
      Cats greet each other with nose touches and mutual sniffing.
      This is cat small talk. Politeness. Information exchange.
    outcomes:
      friendly:
        message: "*nose boop* *mutual sniffing* *social protocols complete*"
      
      suspicious:
        message: "*cautious sniff* *backing away* *not sure about this one*"
        
      familial:
        message: |
          *They know each other's scent intimately*
          *Brief touch. All is well. Family confirmed.*
```

#### LICK

```yaml
LICK:
  command: "LICK [cat]"
  description: "Grooming gesture (usually cat-initiated)"
  duration: varies
  risk: medium
  bidirectional: true
  base_effect: |
    Licking is GROOMING. It's intimate. It's care.
    Cats groom family. Cats groom friends. Cats groom themselves.
    
    If a cat licks YOU: You are accepted. You are THEIRS.
    If you lick a cat: ...are you sure about this?
    
  human_to_cat:
    warning: |
      This is... unconventional. Most humans don't lick cats.
      If you do, the cat will be VERY confused.
      Only attempt with high trust and full acceptance of weirdness.
      
    success_calculation: |
      success = 0.2 if trust < 70 else 0.6
      # Cats find human licking WEIRD
      
    outcomes:
      acceptance:
        requirements: "Trust 70+, relationship 'bonded' or higher"
        effect: "Cat is confused but... touched?"
        relationship: { fondness: +3, history: +2 }
        message: |
          *You lick the cat.*
          *The cat freezes. Processing.*
          *This is NOT how grooming usually goes.*
          *But... you're trying. They appreciate the effort.*
          *They lick you back. Awkwardly. But sincerely.*
          
      confusion:
        effect: "Cat is VERY confused"
        message: |
          *You lick the cat.*
          *The cat stares at you.*
          *What. What are you doing.*
          *Humans don't... that's not...*
          *The cat walks away to reconsider everything.*
          
      disgust:
        requirements: "Trust < 30"
        effect: "Cat is offended"
        relationship: { trust: -3 }
        message: |
          *You attempt to lick the cat.*
          *The cat RECOILS.*
          *BOUNDARIES. YOU HAVE VIOLATED THEM.*
          *The cat will remember this.*
          
  cat_to_human:
    trigger: "Relationship 'friend' or higher"
    meaning: |
      When a cat licks you, they are:
      1. Claiming you (you are THEIRS now)
      2. Grooming you (you clearly can't do it yourself)
      3. Showing affection (highest compliment)
      4. Tasting you (also information gathering)
      
    outcomes:
      grooming:
        requirements: "Relationship 'friend'+"
        effect: "You are being groomed. Accept it."
        relationship: { trust: +2, fondness: +3 }
        message: |
          *The cat begins licking your hand.*
          *Rough tongue. Methodical strokes.*
          *You are being CLEANED. You needed it, apparently.*
          *This is love. Accept it.*
          
      taste_test:
        effect: "Cat is gathering flavor data"
        message: |
          *lick* *pause* *processing*
          *The cat is thinking about what you taste like.*
          *You're not sure how to feel about this.*
          
      claiming:
        requirements: "Relationship 'bonded'+"
        effect: "You have been marked as property"
        relationship: { trust: +3, fondness: +4, history: +2 }
        message: |
          *The cat licks you thoroughly.*
          *Face. Hands. Hair (briefly).*
          *You are THEIRS now. Officially.*
          *Other cats will know. You've been claimed.*
          
      sandpaper_affection:
        effect: "It hurts but it's love"
        message: |
          *lick lick lick lick*
          *The cat's tongue is like sandpaper.*
          *It kind of hurts.*
          *But they're purring. This is LOVE.*
          *Accept the exfoliation.*
          
  cat_to_cat:
    description: |
      Allogrooming — cats grooming each other — is social bonding.
      It's trust. It's family. It's hierarchy.
      The cat who grooms more is usually higher status.
      
    outcomes:
      mutual_grooming:
        message: |
          *They groom each other.*
          *Taking turns. Reaching the spots they can't reach themselves.*
          *This is family. This is pack. This is home.*
          
      dominant_grooming:
        message: |
          *One cat pins the other gently.*
          *Grooming commences. The groomee accepts.*
          *Hierarchy established. Love expressed.*
          
      motherly_grooming:
        context: "Stroopwafel to kittens"
        message: |
          *Stroopwafel grooms the kitten thoroughly.*
          *Behind ears. Under chin. Everywhere.*
          *Protests are ignored. Cleanliness is mandatory.*
          *"You're filthy. Hold still."*
          
      sibling_grooming:
        message: |
          *Half-hearted mutual licking.*
          *"I guess you're okay." "You too, I suppose."*
          *Sibling love: reluctant but real.*
```

#### NOSE_BOOP

```yaml
NOSE_BOOP:
  command: "BOOP [cat]"
  aliases: ["NOSE BOOP", "BOOP NOSE"]
  description: "The gentlest of greetings"
  duration: instant
  risk: low
  bidirectional: true
  base_effect: |
    A nose boop is a tiny, perfect moment of connection.
    It's "hello" and "I like you" and "we're okay" all at once.
    
  human_to_cat:
    success_calculation: |
      success = (cat.nice + cat.trust_level/20) / 15
      # Nice cats accept boops. Trust helps.
      
    outcomes:
      success:
        effect: "Perfect connection"
        relationship: { trust: +1, fondness: +2 }
        message: |
          *boop*
          *The cat's nose is cold and slightly wet.*
          *They hold still for it. They allowed this.*
          *A tiny moment. Perfect.*
          
      counter_boop:
        requirements: "Relationship 'friend'+"
        effect: "Cat returns the boop"
        relationship: { trust: +2, fondness: +3 }
        message: |
          *boop*
          *The cat boops back.*
          *Mutual boop achieved. Friendship confirmed.*
          
      dodge:
        effect: "Cat evades"
        message: "*the cat pulls back just slightly* *not today*"
        
  cat_to_human:
    trigger: "Relationship 'familiar'+ or greeting behavior"
    effect: "Cat-initiated nose contact"
    outcomes:
      greeting_boop:
        message: |
          *The cat stretches up.*
          *Cold nose touches your nose.*
          *"Hello. You exist. I acknowledge this."*
          
      check_in_boop:
        message: |
          *boop*
          *The cat is checking on you.*
          *"You okay? You smell okay. Okay then."*
          
  cat_to_cat:
    description: |
      The classic cat greeting. Nose to nose.
      Safe distance. Information exchange. Social protocol.
    outcomes:
      friendly_boop:
        message: "*nose touch* *we're cool* *carry on*"
        
      family_boop:
        message: |
          *Extended nose contact.*
          *Eyes closed. Trust complete.*
          *Family doesn't need to check anymore. But they do anyway.*
```

## TERPENE EFFECTS — Kitten-specific psychological imprinting

The Terpene Litter kittens impart their namesake's psychological effects
on anyone who interacts with them successfully. The effect is proportional
to interaction quality and duration.

This isn't metaphor — these kittens literally exude their terpene's essence.
Their purrs carry frequency. Their fur holds scent. Their presence shifts mood.

### Mechanism

```yaml
terpene_transfer:
  on_success: |
    effect_strength = interaction_quality × duration_modifier
    duration = base_duration × bond_multiplier
    
  stacking: "Multiple kittens = combined effects (up to saturation)"
  saturation: "Can't exceed 3 simultaneous terpene buffs"
```

### Kitten Effects

| Kitten | Terpene | Effect Name | Buffs | Duration |
|--------|---------|-------------|-------|----------|
| **Myr** | Myrcene | DEEP RELAXATION | +3 Calm, +2 Easy-going, -2 Active | 30 min |
| **Lemon** | Limonene | JOY INFUSION | +3 Cheerful, +2 Energetic, +1 Outgoing | 45 min |
| **Lily** | Linalool | PEACEFUL PRESENCE | +3 Calm, +2 Caring, +1 Open | 1 hour |
| **Pine** | Pinene | SHARP CLARITY | +3 Analytical, +2 Curious, memory boost | 2 hours |
| **Carrie** | Caryophyllene | GUARDIAN'S RESOLVE | +3 Confident, +2 Cautious, threat sense | 1 hour |
| **Hops** | Humulene | REFINED STANDARDS | +2 Neat, quality detection, -2 Hunger | 45 min |
| **Terpy Jr.** | Terpinolene | CHAOS MUSE | +3 Imaginative, +2 Spontaneous, random ideas | ??? |
| **Ocie** | Ocimene | FRESH START | +2 Energetic, +2 Cheerful, clears debuffs | 30 min |

### Combination Effects (Synergies)

| Combo | Name | Effect |
|-------|------|--------|
| Myr + Lily | The Sedation Stack | Short nap = long sleep benefits |
| Lemon + Pine | The Focus Boost | Creative AND productive |
| Carrie + Pine | The Sentinel Package | Hyperawareness without anxiety |
| Terpy Jr. + Lemon | The Chaos Joy | Laughing at things that aren't funny |
| **All 8** | **THE FULL SPECTRUM** | ENTOURAGE EFFECT — all buffs, no downsides (legendary) |

### Stacking Rules

- Maximum 3 simultaneous terpene buffs
- Some terpenes stack better than others
- Saturation warning: Too many conflicting effects may cancel out

## CHARM TYPES — Positive persistent effects

Effect type depends on cat's dominant traits:

| Charm | Source Trait | Effect | Example Cats |
|-------|--------------|--------|--------------|
| **Serenity** | Calm 6+ | +2 Calm | Terpie, Myr, Lily |
| **Joy** | Cheerful 6+ | +2 Cheerful | Lemon, Ocie |
| **Focus** | Analytical 6+ | +2 Analytical | Pine |
| **Courage** | Confident 6+ | +2 Confident | Stroopwafel, Carrie |
| **Creativity** | Spontaneous 6+ | +2 Imaginative | Terpy Jr. |

## POWER-UPS — Temporary ability boosts

| Power-Up | Source | Effect |
|----------|--------|--------|
| **Therapeutic Purr** | Calm 7+ | Heal 1 HP/minute |
| **Luck Boost** | Cat sits in lap unprompted | +10% to random outcomes |
| **Danger Sense** | Cautious 6+ | Warning before threats |
| **Mood Read** | Caring 7 | Sense NPC emotions |
| **Clarity** | Analytical 7 | Remember more details |
| **Fresh Start** | Purifying presence | Clear negative status |

## CURSES — Negative effects (usually player's fault)

| Curse | Trigger | Effect | Cure |
|-------|---------|--------|------|
| **Scratched** | Failed belly rub | -1 HP, visible marks | Rest/heal |
| **Cold Shoulder** | Multiple rejections | Cat ignores you 1hr | Wait |
| **Haunted** | Offending Terpy Jr. | Cat appears watching | Treats + apology |
| **Judged** | Failing Hops' standards | -1 Confidence | Premium food |
| **Protective Wrath** | Threatening family | -3 HP, remembered | MUCH time |

## RELATIONSHIP SYSTEM

Cats remember. Every interaction is tracked. Trust and fondness grow
(or decay) based on how you treat them. The relationship affects
everything: success rates, effect strength, and whether the cat
seeks YOU out.

### Relationship Levels

| Level | Points | Success Mod | Effect Mod | Cat Behavior |
|-------|--------|-------------|------------|--------------|
| **Stranger** | 0-10 | -10% | 50% | Cautious, may avoid |
| **Acquaintance** | 11-25 | — | 75% | Tolerates presence |
| **Familiar** | 26-50 | +10% | 100% | Comfortable, occasional approach |
| **Friend** | 51-75 | +20% | 125% | Seeks attention, greets you |
| **Bonded** | 76-90 | +30% | 150% | Follows you, protective |
| **Soulmate** | 91-100 | +50% | 200% | Psychic connection, anticipates needs |

### Relationship Components

| Component | Weight | Builds From | Damaged By |
|-----------|--------|-------------|------------|
| **Trust** | 40% | Respecting boundaries, consistency | Forcing contact, sudden movements |
| **Fondness** | 35% | Successful interactions, quality time | Ignoring, failed interactions |
| **History** | 25% | Time together, shared experiences | Long absences (decays slower) |

### Interaction Relationship Effects

| Interaction | Success | Great Success | Failure |
|-------------|---------|---------------|---------|
| PAT | +1 trust, +1 fond | +2 trust, +2 fond | -1 trust |
| PET | +2 trust, +2 fond | +3 all, +1 history | -1 trust, -1 fond |
| SCRITCH | +2 trust, +3 fond | +3 trust, +4 fond, +2 history | -1 trust |
| BELLY | +5 all, +3 history | — | -3 trust, -2 fond |
| PLAY | +3 fond, +1 history | — | — |

### Special Events

| Event | When | Bonus |
|-------|------|-------|
| **First Lap Sit** | Cat chooses your lap | +10 trust, +5 fond, +5 history |
| **First Gift** | Cat brings you something | +5 fond, +3 history |
| **Defense** | Cat protects you | +10 all |
| **Healing Presence** | Cat stays when you're hurt | +10 fond, +8 history |

### Cat Personality Affects Build Rate

| Cat | Trust Rate | Fondness Rate | Note |
|-----|------------|---------------|------|
| Terpie | 1.5× | 0.8× | Easy to trust, slow to warm |
| Stroopwafel | 0.6× | 1.2× | Hard to earn, fiercely loyal |
| Lemon | 1.2× | 1.5× | Instant friends |
| Carrie | 0.5× | 0.7× | Must PROVE yourself |
| Lily | 1.0× | 1.3× | Knows your intentions |
| Terpy Jr. | 1.0× | ??? | Non-linear progress |
| Hops | 0.8× | 0.6× | Must earn respect |

### Relationship Decay

- Fondness decays 1 point per session without interaction
- Trust decays 0.5 points per session without interaction
- History never decays (experiences are permanent)
- Decay stops at level floor (can't drop below acquaintance once reached)
- One good interaction resets decay timer

## HOME VS LOCATION PROTOCOL

**Critical architectural pattern for all characters, including cats:**

```yaml
cat:
  home: pub/cat-cave/            # Where FILE lives (don't move!)
  location: pub/cat-cave/nap-zone  # Where cat currently IS
```

| Concept | Meaning | Example |
|---------|---------|---------|
| **home:** | File's physical directory | `pub/cat-cave/` |
| **location:** | Where character currently is | `pub/` (came out to pub) |

**Why this matters:**
- **Stable**: Files don't move around
- **Safe**: No risk of file loss during "movement"  
- **Diff-friendly**: Git tracks field changes, not file moves
- **Organized**: Cats stay in `pub/cat-cave/`, players in `characters/`

## INSTANCE OVERLAY

Cat files inherit this skill and overlay their specifics:

```yaml
# In kitten-lemon.yml
cat:
  skills:
    - cat  # Inherits all interactions from skills/cat
    
  # Traits used in calculations
  sims_traits:
    nice: 8
    outgoing: 10
    active: 10
    playful: 10
    
  # Charm determined by Mind Mirror
  mind_mirror:
    bio_energy:
      cheerful: 7  # → JOY charm
      
  # Instance-specific overrides
  interaction_overrides:
    PLAY_WITH:
      success_modifier: +0.5
      warning: "She may not stop"
      
  # Unique ability
  abilities:
    joy_field:
      effect: "+2 Cheerful to everyone in range"
```

## COMMANDS

| Command | Args | Action |
|---------|------|--------|
| `PAT` | [cat] | Quick friendly pat |
| `PET` | [cat] | Extended petting session |
| `SCRITCH` | [cat] | Targeted scratching |
| `BELLY` | [cat] | Attempt the forbidden zone |
| `PICK UP` | [cat] | Lift and hold |
| `PLAY WITH` | [cat] | Engage in play |
| `FEED` | [cat] | Give food or treats |
| `SLOW BLINK` | [cat] | The feline I-love-you |
| `PSPSPS` | — | Summon nearby cats |
| `SNIFF` | [cat] | Gather scent info |
| `LICK` | [cat] | Grooming gesture |
| `BOOP` | [cat] | Nose boop greeting |

## DESIGN PHILOSOPHY

1. **Consent**: Cats have preferences. Respect them.
2. **Earning**: Success isn't guaranteed. It's EARNED.
3. **Choice**: The best buffs come from cats who CHOOSE to give them.
4. **Agency**: Every cat is an NPC with their own agenda.
5. **Patience**: Trust builds over time, not in one interaction.

> *"A cat that sits in your lap unbidden is worth more than any buff you could force through interaction."*

## LIVE EXAMPLES

The Gezelligheid Grotto has 10 cats using this skill:

### Parents
| Cat | File |
|-----|------|
| **Terpie** | [pub/cat-terpie.yml](../../examples/adventure-3/pub/cat-terpie.yml) |
| **Stroopwafel** | [pub/cat-stroopwafel.yml](../../examples/adventure-3/pub/cat-stroopwafel.yml) |

### The Terpene Litter
| Kitten | File |
|--------|------|
| **Myr** | [pub/kitten-myrcene.yml](../../examples/adventure-3/pub/kitten-myrcene.yml) |
| **Lemon** | [pub/kitten-limonene.yml](../../examples/adventure-3/pub/kitten-limonene.yml) |
| **Lily** | [pub/kitten-linalool.yml](../../examples/adventure-3/pub/kitten-linalool.yml) |
| **Pine** | [pub/kitten-pinene.yml](../../examples/adventure-3/pub/kitten-pinene.yml) |
| **Carrie** | [pub/kitten-caryophyllene.yml](../../examples/adventure-3/pub/kitten-caryophyllene.yml) |
| **Hops** | [pub/kitten-humulene.yml](../../examples/adventure-3/pub/kitten-humulene.yml) |
| **Terpy Jr.** | [pub/kitten-terpinolene.yml](../../examples/adventure-3/pub/kitten-terpinolene.yml) |
| **Ocie** | [pub/kitten-ocimene.yml](../../examples/adventure-3/pub/kitten-ocimene.yml) |

### Their Home
| Location | File |
|----------|------|
| **Gezelligheid Grotto** | [pub/README.md](../../examples/adventure-3/pub/README.md) |
| **The Cat Cave** | [pub/cat-cave.yml](../../examples/adventure-3/pub/cat-cave.yml) |

## DESIGN INFLUENCES

- Tamagotchi — care relationships
- Harvest Moon — animal friendship systems
- Stardew Valley — pet affection mechanics
- Dwarf Fortress — animal personalities
- Real cats — the ultimate reference
