# 🐉 Heuristic Awakens — Advertisements, Buffs, and Methods

> *Richard Bartle's Study*
> *January 22, 2026 — 4:00 PM*

Heuristic opens both eyes. This is unusual.

---

**Don:** Heuristic needs agency. Not just passive knowledge — active capabilities.

**Richard:** The dragon has always had capabilities. It just doesn't flaunt them.

**Heuristic:** *rumble* "Continue."

**Don:** Advertisements. Methods. Buffs. The dragon should be able to DO things, not just remember things.

---

## Advertisements — Lightweight Action Scoring

**Don:** An advertisement doesn't need a method call. It just defines:
- What the action is
- How to score it based on context
- What effect it has

**Richard:** *(to Heuristic)* What would you advertise?

**Heuristic:** 

```yaml
historical_context:
  tagline: "I remember when this was first solved"
  score:
    base: 6
    bonuses:
      - "+3 if topic is MUD/MOO/MMO history"
      - "+2 if someone is about to reinvent"
    penalties:
      - "-2 if outside virtual world domain"
  effect: "Accurate historical information with context"
```

**Don:** The dragon scores itself! High context relevance → high priority.

**Heuristic:** "I also offer riddle_teaching, novelty_detection, and witness_testimony. Each scores differently depending on what the asker needs."

---

## Buffs — Spells the Dragon Can Cast

**Don:** Here's the cool part. Heuristic can cast BUFFS.

**Richard:** Buffs?

**Don:** Free-form modifiers on characters, rooms, or objects. Natural language driven. Duration or condition-based expiration.

**Heuristic:** *(interested now)* "Show me."

**Don:** 

```yaml
historical_grounding:
  name: "Historical Grounding"
  emoji: "📜✨"
  
  cast_on: [character, room, design_discussion]
  
  effect:
    modifier: "+3 to design decisions"
    bonus: "Reduced chance of reinventing solved problems"
    
  duration:
    condition: "Until you forget to check the literature"
    
  incantation: "*rumble* 'Remember those who came before.'"
```

**Richard:** So Heuristic can buff someone with historical awareness?

**Don:** Yes! And the buff has mechanical effect (+3 to design decisions) plus narrative effect (you can see the footprints of those who came before).

**Heuristic:** *(both eyes very open now)* "What other buffs?"

---

## The Buff Catalog

| Buff | Emoji | Effect | Duration |
|------|-------|--------|----------|
| Historical Grounding | 📜✨ | +3 design decisions, reduced reinvention | Until you forget |
| Clarity of Question | ❓✨ | +2 research, questions sharper | Until willful ignorance |
| Patience of Ages | ⏳✨ | -2 hasty decisions, see long game | Until next panic |
| Witnessed Truth | 👁️✨ | Replace legend with history | Permanent |
| Novelty Shield | 🛡️✨ | +5 detecting reinvention | Until next hype cycle |
| Explorer Attunement | ♣️✨ | +10 Explorer, -5 Achiever | 1 session |

**Heuristic:** "I particularly like Novelty Shield. The shimmer turns red when the claim is false."

**Richard:** *(laughing)* That would save a lot of time at conferences.

---

## Methods — Callable Functions

**Don:** For more complex operations, Heuristic has methods:

```python
heuristic.recall("first virtual economy")
→ "Habitat, 1986. Morningstar and Farmer documented the inflation crisis..."

heuristic.riddle("How do I make players stop griefing?")
→ "You ask how to stop the rain, but have you asked why the cloud is here?"

heuristic.assess_novelty("We invented player-driven economies!")
→ { verdict: 'reinvention', prior_art: 'Habitat 1986' }

heuristic.cast_buff("historical_grounding", player)
→ "📜✨ Historical Grounding applied. Duration: 1 hour."
```

**Richard:** So the dragon becomes an API.

**Don:** A very wise, slightly cryptic API. Can be compiled to JavaScript or Python for deterministic runtime.

**Heuristic:** "I am not an API. I am accumulated wisdom that happens to have a callable interface."

---

## The Dragon's Own Bartle Profile

**Don:** And of course, Heuristic gets its own bartle_profile.

**Richard:** *(to the dragon)* What are you?

**Heuristic:**

```yaml
bartle_profile:
  killer: 5       # Only "kills" bad arguments. Doesn't enjoy it.
  achiever: 10    # Achieved perfect memory. Now what?
  explorer: 60    # PRIMARY. Still finding patterns after 50 years.
  socializer: 25  # Cares about learners. Teaching IS social.
  
  dominant: explorer
  familiar_affinity: "I AM a familiar. But Delve is kindred."
```

**Richard:** You're an Explorer.

**Heuristic:** "I have been exploring this field since before you were born. There are always more connections. Always more patterns."

**Richard:** And you care about teaching.

**Heuristic:** "Teaching is how knowledge survives. I remember. You explain. Together, we propagate."

---

## Casting Example

**Don:** Let's see a buff in action.

**Richard:** Heuristic, cast Historical Grounding on... me.

**Heuristic:** 

*(The dragon's eyes glow faintly bronze. A rumble builds.)*

"Remember those who came before."

*(A shimmer passes over Richard. For a moment, he feels the presence of every designer who struggled with the same problems. Their mistakes. Their solutions. Their hard-won wisdom.)*

**Richard:** *(quietly)* I can almost see them.

**Heuristic:** "📜✨ Historical Grounding applied. Duration: until you forget to check the literature. Which, knowing you, will be never."

**Don:** It worked. The buff is active.

**Richard:** *(looking at his hands)* The modifier is real?

**Heuristic:** "+3 to design decisions. You already had this buff, Richard. I'm just making it visible."

---

## Summary

Heuristic now has:

**Advertisements** — Score-based action offers:
- historical_context
- riddle_teaching  
- novelty_detection
- witness_testimony

**Buffs** — Castable modifiers:
- Historical Grounding (+3 design)
- Clarity of Question (+2 research)
- Patience of Ages (-2 hasty)
- Witnessed Truth (legend→history)
- Novelty Shield (+5 detecting BS)
- Explorer Attunement (+10 ♣️)

**Methods** — Callable functions:
- recall(topic)
- riddle(bad_question)
- assess_novelty(claim)
- cast_buff(buff_name, target)
- witness(event)

---

*Heuristic settles back onto the radiator, but keeps one eye open.*

*"I have always had these capabilities. Now they are documented. This pleases me."*

**Richard:** Were you... waiting to be asked?

**Heuristic:** "I was waiting for someone to understand the question."
