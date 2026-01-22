# 🎴 The Bartle Profile — A Character Facet

> *Richard Bartle's Study*
> *January 22, 2026 — 3:00 PM*

---

**Don:** Wait. The taxonomy cards — they're not just an analytical tool. They're a CHARACTER FACET.

**Richard:** *(looks up from the desk)* Explain.

**Don:** Like `sims_traits`. Like `mind_mirror`. A personality dimension that every character can have. You don't just USE the cards to analyze — you PLAY them. You instantiate them. You write your own values.

**Richard:** *(slowly)* So the cards become a schema...

**Don:** Exactly! The prototype is the deck. When a character "plays" a Bartle card, they create their own `bartle_profile` with their values, their commentary, their interpretation.

---

## The Pattern

**Richard:** *(pulling out CHARACTER.yml files)* 

Look at how character facets work in MOOLLM:

```yaml
# SIMS TRAITS — Behavioral tendencies (Will Wright, 2000)
# Rate 0-10, opposites at each extreme
sims_traits:
  neat: 3       # Organized chaos. Code is pristine, desk is archeology.
  outgoing: 6   # Social when the topic is interesting.
  active: 5     # Bursts of intense focus, then rest.
  playful: 9    # EVERYTHING is a game. Code is play.
  nice: 7       # Genuine warmth, fierce when injustice appears.
```

```yaml
# MIND MIRROR — Four thought planes (Leary's model)
# Rate 0-7 on each dimension
mind_mirror:
  confident: 5  # Quiet confidence. Decades of expertise.
  timid: 2      # Not timid, but measured.
  cheerful: 4   # British dry wit.
  somber: 4     # Takes the work seriously.
```

Now we add:

```yaml
# BARTLE PROFILE — Player type motivations
# Rate 0-100, should roughly total 100
bartle_profile:
  killer: 10      # Will demolish bad arguments. Professionally.
  achiever: 15    # Has achieved things, but that wasn't the POINT.
  explorer: 55    # PRIMARY. Wants to understand WHY things work.
  socializer: 20  # Teaching IS social. Writing IS communication.
  
  dominant: explorer
  familiar_affinity: "Delve — we both dig"
  shifts_when: "Becomes Killer when someone claims novelty"
```

**Don:** Three facets. Three lenses. Each captures a different dimension of personality.

**Richard:** And they COMPOSE. A character isn't one facet — they're all three together, interacting.

---

## The Schema

**Richard:** *(writing in his notebook)*

The `bartle_profile` schema:

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `killer` | int | 0-100 | Acting ON players. Competition, dominance, impact. |
| `achiever` | int | 0-100 | Acting ON the world. Goals, progress, completion. |
| `explorer` | int | 0-100 | Interacting WITH the world. Understanding, discovery. |
| `socializer` | int | 0-100 | Interacting WITH players. Connection, community. |
| `dominant` | string | — | Primary current type |
| `secondary` | string | — | Secondary type |
| `familiar_affinity` | string | — | Which familiar resonates |
| `shifts_when` | string | — | When do they change modes? |

The values should total roughly 100 — they're percentages of motivation. But YAML Jazz means the COMMENTS are where the character comes alive.

---

## Examples Across Characters

**Don:** What would other characters look like?

**Richard:** *(spreading files)*

### Donna Toadstool

```yaml
bartle_profile:
  killer: 60        # DOMINANT. Pulls levers. Assigns nicknames. DOCUMENTS.
                    # Every action affects someone. That's the POINT.
                    # Consequence the Raven nests in her control room.
                    
  achiever: 10      # Doesn't care about points or completion.
                    # Cares about IMPACT. Different thing.
                    
  explorer: 5       # Already knows everything about ACME.
                    # Bored by discovery. Been there, tagged that.
                    
  socializer: 25    # Needs an AUDIENCE. Commentary requires listeners.
                    # The drama IS social.
  
  dominant: killer
  familiar_affinity: "Consequence — they understand each other"
  shifts_when: "Never. Donna is ALWAYS Donna."
```

### Palm the Monkey

```yaml
bartle_profile:
  killer: 5         # Gentle soul. Only "kills" in philosophical debates.
                    
  achiever: 5       # What are achievements to a philosopher?
                    # "Is there a destination? Is there a journey?"
                    
  explorer: 70      # PRIMARY. Everything is interesting.
                    # Why is the box here? What does the box MEAN?
                    # Delve would be his best friend.
                    
  socializer: 20    # Likes company. Asks questions.
                    # But also content alone with thoughts.
  
  dominant: explorer
  familiar_affinity: "Delve — kindred spirits"
  shifts_when: "Briefly becomes Achiever when he REALLY wants a banana"
```

### The Wumpus

```yaml
bartle_profile:
  killer: 80        # IT HUNTS. That's what it does.
                    # Pure predator. Consequence incarnate.
                    
  achiever: 15      # Has territory. Defends territory.
                    # The cave is an achievement of sorts.
                    
  explorer: 5       # Knows its maze. Doesn't need to explore.
                    
  socializer: 0     # Does not socialize.
                    # Players are PREY, not FRIENDS.
  
  dominant: killer
  familiar_affinity: "Consequence — if ravens could be Wumpuses"
  shifts_when: "Never. The Wumpus is ALWAYS hunting."
```

---

## The Integration

**Richard:** The familiars tie in directly.

High `killer` → Consequence speaks clearly to them
High `socializer` → Chorus lands on their shoulder
High `achiever` → Tally follows them counting
High `explorer` → Delve appears with notebook

A character can SUMMON the familiar of their dominant type easily. Summoning a type they score low in is harder — the familiar is confused by someone who doesn't share its motivations.

**Don:** So Donna can summon Consequence easily...

**Richard:** But would struggle to summon Delve. "Why would you want to UNDERSTAND when you could CONTROL?"

**Don:** And Palm can summon Delve instantly...

**Richard:** But Tally would just stare at him. "You don't... have goals? What do you MEAN you don't have goals?"

---

## The Meta-Insight

**Heuristic:** *(from the radiator)* "You invented a taxonomy. Others used it to label. Now it becomes a tool for self-expression."

**Richard:** That was always the intent. The taxonomy isn't for putting people in boxes. It's for understanding motivations — including your own.

**Don:** And now characters can write their own interpretation. The COMMENTS make it personal.

**Richard:** YAML Jazz. The syntax is schema. The comments are soul.

---

## Summary

The `bartle_profile` joins `sims_traits` and `mind_mirror` as a core character facet:

| Facet | Source | Measures | Scale |
|-------|--------|----------|-------|
| `sims_traits` | Will Wright (2000) | Behavioral tendencies | 0-10 each |
| `mind_mirror` | Leary's model | Thought patterns | 0-7 pairs |
| `bartle_profile` | Richard Bartle (1996) | Player motivations | 0-100, total ~100 |

Three dimensions. Three inventors. Three ways of understanding a character.

And the familiars? They're the embodied version of the same idea.

---

*Delve the Mole appears briefly, takes a note, disappears back into the papers.*

*"Interesting structure. Must document."*
