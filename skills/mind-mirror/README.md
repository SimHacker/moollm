# Mind Mirror

> *"Mirrors should reflect a little before throwing back images."*
> — Jean Cocteau

---

## What Is It?

**Mind Mirror** is MOOLLM's personality modeling system, inspired by Timothy Leary's groundbreaking 1985 software of the same name. It provides a structured framework for:

- **Self-reflection** — Map your current self vs. your ideal self
- **Character modeling** — Create rich, dimensional NPCs and personas
- **Empathy exploration** — Role-play through others' perspectives
- **Comparison** — Compare any two personalities on multiple dimensions

Mind Mirror uses **four Thought Planes**, each with **eight dimensions** arranged in a circle — like a psychological pie menu.

---

## The Lineage

| Source | Contribution |
|--------|--------------|
| **Timothy Leary** | Mind Mirror (1985), Interpersonal Circumplex, PhD dissertation on personality |
| **Electronic Arts** | Original publisher (when EA made weird, beautiful things) |
| **Peter Van den Beemt & Bob Dietz** | Original programmers |
| **Leary's PhD** | "The Social Dimensions of Personality" — the foundation |

### The Jail Break Story

Before LSD, Leary designed the **Interpersonal Behavior Circle** personality assessment. In the 1970s, when imprisoned, he was given a psychological assessment to gauge escape risk — *a test he had designed*. Understanding the criteria, he answered to appear low-risk, was assigned minimum security, and escaped.

**Your own self-knowledge is your most powerful tool.**

---

## The Four Thought Planes

Mind Mirror organizes personality into four planes, each a circle of eight dimensions:

### 1. BIO-ENERGY (Life Force)

Mood, vitality, temperament, energy level.

```
                    Energetic
                        │
          Restless ─────┼───── Enthusiastic
              │         │         │
        Serious ────────┼──────── Cheerful
              │         │         │
          Cautious ─────┼───── Easy-Going
                        │
                      Calm
```

| Inner (Moderate) | Outer (Extreme) |
|------------------|-----------------|
| Energetic | Wired |
| Enthusiastic | Vivacious |
| Cheerful | Silly |
| Easy-Going | Lazy |
| Calm | Lethargic |
| Cautious | Worried |
| Serious | Gloomy |
| Restless | Driven |

### 2. EMOTIONAL INSIGHT (Interpersonal Style)

How you approach others, emotional expression, relational angle.

```
                    Forceful
                        │
            Proud ──────┼───── Confident
              │         │         │
        Irritable ──────┼──────── Friendly
              │         │         │
           Touchy ──────┼───── Docile
                        │
                      Timid
```

| Inner (Moderate) | Outer (Extreme) |
|------------------|-----------------|
| Forceful | Dominating |
| Confident | Charismatic |
| Friendly | Over-Friendly |
| Docile | Dependent |
| Timid | Submissive |
| Touchy | Resentful |
| Irritable | Angry |
| Proud | Arrogant |

### 3. MENTAL ABILITIES (Cognitive Style)

Knowledge, creativity, information grasp, imagination.

```
                  Well-Informed
                        │
         Practical ─────┼───── Innovative
              │         │         │
      Conventional ─────┼──────── Creative
              │         │         │
         Sensible ──────┼───── Impractical
                        │
                   Uneducated
```

| Inner (Moderate) | Outer (Extreme) |
|------------------|-----------------|
| Well-Informed | Know-It-All |
| Innovative | Visionary |
| Creative | Dreamy |
| Impractical | Unrealistic |
| Uneducated | Illiterate |
| Sensible | Imitative |
| Conventional | Unimaginative |
| Practical | Pedantic |

### 4. SOCIAL INTERACTION (Class & Convention)

Status, tolerance, sophistication, moral conventionality.

```
                   Influential
                        │
        Respectable ────┼───── Worldly
              │         │         │
        Moralistic ─────┼──────── Uninhibited
              │         │         │
     Unsophisticated ───┼───── Uncultured
                        │
                   Lower-Class
```

| Inner (Moderate) | Outer (Extreme) |
|------------------|-----------------|
| Influential | Snobbish |
| Worldly | Ultra-Sophisticated |
| Uninhibited | Non-Conformist |
| Uncultured | Wild |
| Lower-Class | Unknown |
| Unsophisticated | Naive |
| Moralistic | Puritanical |
| Respectable | Upright |

---

## How It Works in MOOLLM

### Creating a Mind Mirror Profile

```yaml
# characters/captain-ashford.mirror.yml
mind_mirror:
  subject: "Captain Ashford"
  context: "After slaying the grue"
  
  bio_energy:
    energetic: 6      # 0-7 scale
    enthusiastic: 7
    cheerful: 5
    easy_going: 3
    calm: 2
    cautious: 4
    serious: 5
    restless: 6
    
  emotional_insight:
    forceful: 6
    confident: 7
    friendly: 5
    docile: 1
    timid: 0
    touchy: 2
    irritable: 3
    proud: 6
    
  mental_abilities:
    well_informed: 5
    innovative: 6
    creative: 7
    impractical: 4
    uneducated: 1
    sensible: 4
    conventional: 2
    practical: 5
    
  social_interaction:
    influential: 5
    worldly: 6
    uninhibited: 7
    uncultured: 3
    lower_class: 2
    unsophisticated: 1
    moralistic: 2
    respectable: 4
```

### Comparing Two Profiles

```
> MIND-MIRROR COMPARE captain-ashford WITH mother

BIO-ENERGY:
  Captain more Energetic (6 vs 4)
  Mother more Calm (6 vs 2)
  Captain more Restless (6 vs 2)
  
EMOTIONAL INSIGHT:
  Captain more Forceful (6 vs 3)
  Mother more Friendly (7 vs 5)
  Captain more Proud (6 vs 2)
  
...
```

### Self-Reflection Mode

```
> MIND-MIRROR SELF

Let's scope your current self.
Rate yourself on each dimension (0-7):

BIO-ENERGY:
  How PEPPY are you right now? (0=Never, 7=Always) _
  How LAID-BACK are you? _
  ...
```

---

## Integration with MOOLLM

### As Character DNA

Every character in MOOLLM can have a Mind Mirror profile:

```yaml
# In any character file
character:
  name: "The Bartender"
  
  mind_mirror:
    # Abbreviated form — just the extremes
    bio_energy: "calm, serious"
    emotional: "confident, proud"
    mental: "well-informed, sensible"
    social: "worldly, uninhibited"
```

### In Soul-Chat

Mind Mirror profiles influence how characters speak:

```yaml
# SOUL-CHAT uses Mind Mirror to calibrate voice
character_voice:
  bartender:
    mind_mirror_influence:
      - calm → speaks slowly, pauses
      - confident → never apologizes unnecessarily
      - well-informed → drops historical references
      - uninhibited → occasionally vulgar
```

### In Adventures

NPCs can have Mind Mirror profiles that affect:
- How they respond to the player
- What advertisements they generate
- Their decision-making in simulations

---

## The Plain Talk / Shrink-Rap Toggle

Leary provided two vocabulary modes:

| Plain Talk | Shrink-Rap (Psychological) |
|------------|---------------------------|
| Peppy | Hyper-Manic |
| Laid-Back | Low-Energy |
| Intense | Agitated |
| Low-Key | Tranquil |
| Sad | Melancholic |
| Happy | Euphoric |
| Hesitant | Listless |
| Gung-Ho | Wholehearted |
| Bossy | Dictatorial |
| Shy | Passive |
| Cocky | Haughty |
| Cute | Eager-to-Please |
| Grumpy | Hostile |
| Sweet | Congenial |
| Whining | Complaining |
| Encouraging | Nurturant |
| Knowledgeable | Intelligent |
| Dumb | Ignorant |
| Organized | Efficient |
| Flaky | Disorganized |
| Closed-Minded | Literal-Minded |
| Imaginative | Original |
| By-the-Book | Narrow-Minded |
| Ingenious | Inventive |
| V.I.P. | Aristocratic |
| Social-Nobody | Insignificant |
| Proper | Pillar-of-the-Community |
| Rowdy | Rebellious |
| Straight-Arrow | Inhibited |
| Free-Living | Social-Maverick |
| Square | Small-Townish |
| Sophisticated | Cosmopolitan |

---

## Exercises from the Original

### Exercise 1: SELF PORTRAIT

Compare your self as you are right now with your ideal self.

```
> MIND-MIRROR EXERCISE self-portrait

First, scope YOUR SELF as you are today.
Then, scope YOUR IDEAL SELF — who you want to become.

[After completion]

Your Self is more Restless than your Ideal.
Your Ideal is more Calm than your Self.
Consider: What would help you move toward your Ideal?
```

### Exercise 2: SELF-RANGE

Compare your best and worst selves.

```
> MIND-MIRROR EXERCISE self-range

Scope YOUR BEST SELF — you at your peak.
Then, scope YOUR WORST SELF — you at your lowest.

[After completion]

The gap between your Best and Worst on EMOTIONAL INSIGHT
is larger than average. You experience significant swings
in confidence and friendliness.
```

### Exercise 3: ROLE-PLAY ODYSSEY (Life Simulation)

Mind Mirror's "Life Simulation" mode let you role-play through situations as different personalities. This maps directly to MOOLLM adventures!

```
> MIND-MIRROR SIMULATE "job interview" AS captain-ashford

You are Captain Ashford, approaching a job interview.
Your Mind Mirror profile suggests you'll be:
- Forceful and Confident (might come across as arrogant)
- Creative and Innovative (good for brainstorming questions)
- Uninhibited (might say something unexpected)

The interviewer asks: "What's your greatest weakness?"

How do you respond?
```

---

## Connection to K-Lines

Mind Mirror dimensions ARE K-lines:

```
Type "CONFIDENT" → activates the cluster:
  - Charismatic at extreme
  - Opposite of Timid
  - Part of EMOTIONAL INSIGHT plane
  - Associated behaviors and speech patterns
```

When you invoke a Mind Mirror dimension, you're invoking a tradition of personality psychology going back to Leary's PhD work in the 1950s.

---

## Connection to Representation Ethics

Mind Mirror provides a **structured, non-impersonating** way to model real people:

```yaml
# Instead of "pretending to be Einstein"
# we create a Mind Mirror profile based on documented traits

einstein_profile:
  bio_energy: "restless, serious, driven"
  emotional: "confident, proud, irritable" 
  mental: "innovative, visionary, impractical"
  social: "influential, non-conformist, unsophisticated"
  
  sources:
    - "Documented personality traits from biographies"
    - "Public statements and behavior patterns"
    - "Colleague descriptions"
```

This is **tradition invocation**, not impersonation. The profile activates documented traits without claiming to *be* the person.

---

## Protocol Symbols

```
MIND-MIRROR       — The whole personality modeling system
THOUGHT-PLANE     — One of the four circular dimensions
BIO-ENERGY        — Life force, mood, vitality plane
EMOTIONAL-INSIGHT — Interpersonal style plane
MENTAL-ABILITIES  — Cognitive style plane
SOCIAL-INTERACTION — Class and convention plane
SELF-PORTRAIT     — Compare self with ideal self
SELF-RANGE        — Compare best and worst selves
ROLE-PLAY-ODYSSEY — Life simulation through different profiles
PLAIN-TALK        — Everyday vocabulary mode
SHRINK-RAP        — Psychological vocabulary mode
```

---

## Dovetails With

| Skill | Relationship |
|-------|--------------|
| [representation-ethics/](../representation-ethics/) | Mind Mirror is an ethical way to model personalities |
| [hero-story/](../hero-story/) | Hero-Story cards can include Mind Mirror profiles |
| [card/](../card/) | Character cards can embed Mind Mirror data |
| [soul-chat/](../soul-chat/) | Mind Mirror influences character voice |
| [adventure/](../adventure/) | NPCs have Mind Mirror profiles |
| [coatroom/](../../examples/adventure-3/coatroom/) | Costumes can modify Mind Mirror dimensions |

---

## The Deeper Philosophy

Leary's Mind Mirror was part of his larger project: **using technology for consciousness exploration**. The original software said:

> "MIND TOOLS: Enhance Insight, Mental Fitness, Learning Skills and Performance."
> "MIND PLAY: Sophisticated Head Games."

This maps perfectly to MOOLLM's PLAY-LEARN-LIFT:

- **PLAY** with personality dimensions, try on different profiles
- **LEARN** patterns about yourself and others
- **LIFT** insights into structured understanding

Mind Mirror is **constructionist psychology** — you construct your understanding of self through active exploration.

---

## The Disclaimer (from the original)

> "In this program you will find references and statements attributed to several hundred public figures and historical personages. All such statements attributed to living persons are fictional; they are intended as gentle satire and provocative humor. In no case is there any implication that the statements reflect the true sentiments of the 'alleged' speaker."

This disclaimer from 1985 anticipated the exact concerns we address in [representation-ethics/](../representation-ethics/). Mind Mirror profiles are **models**, not **claims**.

---

## Further Reading

- [Timothy Leary's Mind Mirror — USC Archive](https://scalar.usc.edu/works/timothy-leary-software/index)
- [Interpersonal Circumplex — Wikipedia](https://en.wikipedia.org/wiki/Interpersonal_circumplex)
- [Leary's PhD Dissertation](https://archive.org/details/leary/leary.300dpi/mode/2up)
- [Don Hopkins' Mind Mirror Text Extraction](https://donhopkins.com/home/mind-mirror.txt)
- [Mind Mirror Scales as JSON](https://donhopkins.com/home/mind-mirror.json)

---

*"In a magic mirror we see reflected not only our lives, but the lives of all men that have been. When I think on this majestic theme, my eyes dazzle."*
— Oliver Wendell Holmes
