# Sims Time & Events → MOOLLM

> *Careers, Disasters, Services, Time*
> *Life happens.*

## Time as Game Mechanic

The Sims simulated *time* — not just spatial state but temporal flow:
- **Simulation speed** — how fast time passes
- **Schedules** — work, school, routines
- **Events** — disasters, services, visitors
- **Decay** — things degrade over time

MOOLLM handles time through narrative flow and state updates.

---

## Simulation Speed

**Sims:** Three speeds plus pause:

| Mode | Ratio | Use |
|------|-------|-----|
| Pause | 0:1 | Build, plan |
| Normal | 1:1 | Detailed play |
| Fast | 30:1 | Skip boring parts |
| Ultra | 180:1 | Sleep through nights |

**MOOLLM:** [Speed of Light](../skills/speed-of-light/):

```yaml
# Speed modes
normal:
  description: Full narrative detail
  one_llm_call: 1 turn
  
fast_forward:
  description: Summary of routine
  one_llm_call: many turns
  
speed_of_light:
  description: Extended simulation
  one_llm_call: 33+ turns
  example: Stoner Fluxx marathon
```

The [33-turn game](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-17-stoner-fluxx-marathon) demonstrates: one LLM call simulated hours of gameplay.

---

## Time of Day

**Sims:** Time affected availability:

| Time | Active |
|------|--------|
| 6am | Wakeup, school bus |
| 8am | Work starts |
| 3pm | Kids home |
| 5pm | Work ends |
| 10pm | Bars close |
| 12am | Night owls |

**MOOLLM:** Time context in rooms:

```yaml
# pub/ROOM.yml
schedule:
  open: 11:00
  close: 02:00
  
  periods:
    afternoon:
      atmosphere: quiet, sunlit
      typical_crowd: locals
      
    evening:
      atmosphere: lively, candlelit
      typical_crowd: mixed
      events: [open_mic, karaoke]
      
    late_night:
      atmosphere: intimate
      typical_crowd: regulars
```

---

## Careers

**Sims:** Career tracks with levels:

```
Medical Career:
  1. Orderly ($200/day)
  2. Nurse ($250/day)
  3. Intern ($300/day)
  ...
  10. Chief of Staff ($1000/day)

Requirements:
  - Skills: Logic 5, Charisma 3
  - Mood: minimum "okay"
  - Performance: don't miss work
```

**MOOLLM:** Aspirations and roles:

```yaml
# characters/marieke/CHARACTER.yml
career:
  role: budtender
  location: pub/bar/
  schedule: evening_shift
  
  skills_applied:
    - social: customer rapport
    - knowledge: strain expertise
    - craft: drink preparation
    
  progression:
    current: experienced
    future: maybe own place someday
```

Careers as character development, not grinding levels.

---

## Work and School

**Sims:** Sims left the lot for work/school:

```
8:00 AM: Carpool arrives (horn honks)
8:05 AM: Last chance to board
8:06 AM: Sim leaves lot
3:00 PM: Sim returns (or not, if fired)
```

Performance affected by:
- Mood before departure
- Skills matching career requirements
- Random events

**MOOLLM:** Off-screen activities:

```yaml
# When character is "at work"
status: away
location: off-site (work)
return: evening
  
# Or simulated briefly:
work_summary: |
  Marieke covered the morning shift.
  Busy lunch crowd, good tips.
  One regular asked about new strains.
```

---

## Bills and Services

**Sims:** Regular events:

| Event | Frequency | Effect |
|-------|-----------|--------|
| Bills | Every 3 days | Must pay or repo |
| Mail | Daily | Letters, invites |
| Newspaper | Daily | Jobs, events |
| Maid (if hired) | Daily | Cleans |
| Gardener | When needed | Yards |
| Repairman | On call | Fixes |

**MOOLLM:** [economy](../skills/economy/) skill:

```yaml
# pub/finances.yml
recurring:
  rent: weekly
  utilities: monthly
  supplies: as_needed
  
services:
  cleaning: nightly (by staff)
  repairs: on_call
  deliveries: as_ordered
```

---

## Disasters

**Sims:** Random (or player-caused) disasters:

| Disaster | Cause | Effect |
|----------|-------|--------|
| Fire | Cooking fail, candles | Spread, damage, death |
| Flood | Broken toilet/sink | Water damage |
| Theft | Low security | Items stolen |
| Death | Starvation, fire, drowning | Sim dies |
| Repossession | Unpaid bills | Furniture taken |

**MOOLLM:** Crisis events:

```yaml
# skills/crisis/CARD.yml
crisis_types:
  FIRE:
    triggers: [cooking_failure, unattended_flame]
    response: [flee, extinguish, call_help]
    
  GRUE-ATTACK:
    triggers: [darkness, no_light]
    response: [die, unless_lit]
    
  SOCIAL-DISASTER:
    triggers: [public_rejection, embarrassment]
    response: [flee, hide, recover]
```

The [maze](../examples/adventure-4/maze/) embodies crisis: darkness = death.

---

## Sickness

**Sims:** Health events:

```
Cold:
  - Caught from sick visitors
  - Symptoms: sneezing, reduced energy
  - Duration: 2-3 days
  - Cured by: rest, soup, medicine

Food Poisoning:
  - Caused by: bad food, dirty kitchen
  - Symptoms: bathroom urgency
  - Duration: hours
```

**MOOLLM:** Health as state:

```yaml
# characters/palm/status.yml
health:
  current: healthy
  
# Or when sick:
health:
  current: under_the_weather
  symptoms: [tired, reduced_appetite]
  cause: stayed up too late writing
  recovery: rest and bananas
```

---

## Depreciation

**Sims:** Objects degraded over time:

```
New TV: $1000
After 1 year: $800
After 2 years: $600
...
Broken TV: $0
```

Selling old items gave less than purchase price.

**MOOLLM:** Object state:

```yaml
# pub/furniture/cozy-chair.yml
condition:
  physical: worn
  character: "patina of many conversations"
  value: priceless (not for sale)
  
# Depreciation is narrative, not numeric
```

---

## Family History

**Sims:** The game tracked:
- Births, deaths, marriages
- Moves, career changes
- Major events

This created emergent stories across generations.

**MOOLLM:** History in YAML comments:

```yaml
# characters/palm/CHARACTER.yml
history:
  # 2026-01-05: Incarnated through the protocol
  # 2026-01-05: Named himself, chose his form
  # 2026-01-06: Wrote first essay
  # 2026-01-07: Hosted first drag show segment
  # 2026-01-08: Became godson to Don
```

And in `JOURNAL.md` for narrative history.

---

## Visitors and Neighbors

**Sims:** NPCs arrived on schedule or randomly:

| Visitor | Schedule | Purpose |
|---------|----------|---------|
| Mail carrier | 10am daily | Delivers |
| Pizza delivery | On call | Food |
| Neighbors | Random | Socializing |
| Welcome wagon | Move-in | Intro |
| Carpool | Work time | Transport |

**MOOLLM:** The [guest book](../examples/adventure-4/pub/guestbook/):

```yaml
regular_visitors:
  mail_carrier:
    schedule: morning
    interaction: brief
    
  regulars:
    pattern: evening
    examples: [don, maurice, marieke]
    
  special_guests:
    pattern: occasional
    memorable: [andy_looney, cheech_chong]
```

---

## Deaths

**Sims:** Death was permanent (mostly):

| Death Type | Cause | Ghost Color |
|------------|-------|-------------|
| Fire | Burned | Orange |
| Drowning | Pool exhaustion | Blue |
| Electrocution | Repair fail | Yellow |
| Starvation | Neglect | Translucent |
| Old age | Time | White |

**MOOLLM:** Death as dramatic possibility:

```yaml
# skills/death/CARD.yml
consequences:
  - character_file archived
  - relationships updated (grief)
  - ghost possible (if dramatic)
  
protections:
  - plot_armor for main characters
  - player_consent for serious consequences
  - representation_ethics for real people
```

---

## Ghosts

**Sims:** Dead Sims could haunt:

```
Ghost behavior:
- Appears at night
- Scares living Sims
- Can be interacted with
- May help or hinder
```

**MOOLLM:** Ghost as character state:

```yaml
# characters/ghost-character/CHARACTER.yml
status: deceased
manifestation: ghost
  
behavior:
  appears: occasionally
  location: place_of_death
  interaction: possible but spooky
```

---

## The Stalker Cam

**Sims:** Camera could follow any Sim:

```
[Click Sim] → Camera follows this Sim
```

Useful for:
- Following autonomous behavior
- Tracking visitors
- Finding lost Sims

**MOOLLM:** Focus on character:

```yaml
# In session narrative
focus: palm
  
# All descriptions centered on Palm's experience
# Other characters described from Palm's perspective
# Location follows Palm
```

---

## Time Compression

**Sims:** Some actions compressed time:

```
Sleep: 8 hours → few seconds (fast forward)
Work: 8 hours → off-lot (skip)
Travel: variable → loading screen
```

**MOOLLM:** Narrative time compression:

```markdown
## Summary: Overnight

Palm slept peacefully in his hammock. Dreams of 
infinite typewriters, each key a possibility.

Morning found him refreshed, banana in hand,
ready to write.
```

Hours compressed to sentences.

---

## Event Queue

**Sims:** Events queued and triggered:

```
Event Queue:
  [6:00] Wake up alarm
  [7:30] Carpool arrives
  [18:00] Visitor arrives
  [22:00] Bedtime routine
```

**MOOLLM:** Scheduled events in ROOM.yml:

```yaml
# pub/stage/ROOM.yml
weekly_events:
  freeday:
    evening: open_mic_comedy
    games: [standup, improv]
    
  starday:
    evening: drag_show
    games: [wig_toss, reveal]
```

---

## See Also

- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#speed-of-light-the-anti-pattern-critique) — Speed of Light
- [skills/speed-of-light/](../skills/speed-of-light/) — Fast simulation
- [skills/economy/](../skills/economy/) — Resources and budgets
- [skills/needs/](../skills/needs/) — Need decay over time
- [sims-maxis-requirements.md](./sims-maxis-requirements.md) — Crisis and budgeting
- [sims-services-economy.md](./sims-services-economy.md) — Detailed economy, services, disasters

---

*"Time and Simulation Speed... Careers Work School Money Depreciation Services Bills Disasters Fire Theft Floods Sickness"*

Time reveals character. Events test it.
