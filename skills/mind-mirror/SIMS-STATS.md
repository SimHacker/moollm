# The Sims 1 Character Data — A Complete Field Guide

> The complete field guide to what makes a Sim tick.

## The PersonData Array

Every Sim is a flat array of 80 signed 16-bit integers. This is the entire runtime representation of a character's state. Everything — personality, skills, job, age, gender, zodiac sign, routing state, head-seeking behavior — lives in one contiguous block of 160 bytes.

The simplicity is the genius. Will Wright's team could have built a complex object hierarchy. Instead: 80 slots, each a number. Any SimAntics behavior tree can read or write any slot. The personality system, the skill system, the career system, and the animation system all share the same flat namespace.

## Personality: Five Sliders, Twenty-Five Points

Character creation gives you 25 personality points to distribute across 5 traits:

| Trait | Index | Low (0) | High (10) | What It Does |
|-------|-------|---------|-----------|-------------|
| **Neat** | 7 | Sloppy | Neat | Cleaning autonomy, mess tolerance, hygiene decay |
| **Outgoing** | 6 | Shy | Outgoing | Social initiation, party comfort, conversation skill |
| **Active** | 3 | Lazy | Active | Movement speed, exercise preference, energy sensitivity |
| **Playful** | 5 | Serious | Playful | Entertainment choice, boredom rate, humor |
| **Nice** | 2 | Grouchy | Nice | Relationship success, conflict tendency, helping behavior |

There's also a sixth trait — **Generous** (index 4, selfish ↔ generous) — that exists in the PersonData array but isn't exposed in the Sims 1 UI. It sits between Nice and Playful in memory. The Sims Online uses it. The original game stores it but never shows it to the player.

Internally, traits are 0-1000. The UI shows 0-10. Conversion: `display = internal / 100`.

### How Traits Drive Behavior

The trait values don't just color dialogue — they directly affect the autonomous behavior engine. When a Sim is idle, the game evaluates "advertisements" from nearby objects. Each object advertises how well it satisfies needs, and the Sim's personality modifies the scores:

- A **Neat 9** Sim sees dirty dishes and gets a cleaning urge that a **Neat 2** Sim ignores
- An **Outgoing 8** Sim gravitates toward the phone; an **Outgoing 2** Sim gravitates toward the bookcase
- A **Playful 9** Sim picks the computer game over the newspaper; a **Playful 1** Sim picks the newspaper

This is the advertisement system — objects broadcast what they offer, and personality shapes which offers appeal most. It's the same system MOOLLM uses for character decision-making.

## Skills: Seven Learnable Abilities

Skills are learned by interacting with skill-building objects. Unlike traits, skills start at 0 and only go up.

| Skill | Index | Learned From | What It Unlocks |
|-------|-------|-------------|----------------|
| **Cooking** | 10 | Bookcase, stove | Better meals, fewer fires |
| **Mechanical** | 12 | Bookcase, broken objects | Repairs without electrocution |
| **Charisma** | 11 | Mirror, conversation | Better social interactions |
| **Logic** | 18 | Chess, telescope | Win at chess, career advancement |
| **Body** | 17 | Exercise equipment, pool | Win fights, career advancement |
| **Creativity** | 15 | Easel, piano | Valuable paintings, music skill |
| **Cleaning** | 9 | Practice cleaning | Faster, more thorough cleaning |

Cleaning skill (index 9) is hidden — it exists in the data and affects cleaning speed, but doesn't appear in the skill panel. It increases through the act of cleaning.

Skills matter for careers. Each career level requires minimum skill levels. A Sim can't become a detective (Law Enforcement level 5) without sufficient Logic and Body. The career system checks these at promotion time.

## The Eight Needs

The need system is the heartbeat of The Sims. Eight meters that constantly decay and drive all autonomous behavior:

| Need | Range | Decay Rate | Critical Failure |
|------|-------|-----------|-----------------|
| **Hunger** | -100 to 100 | Constant, faster with activity | Death (starvation) |
| **Comfort** | -100 to 100 | When standing/on hard surfaces | Constant complaining |
| **Hygiene** | -100 to 100 | Constant, faster with exercise | Social penalty, Sims recoil |
| **Bladder** | -100 to 100 | Constant, faster after drinks | Wets self (embarrassment) |
| **Energy** | -100 to 100 | Constant while awake | Passes out on floor |
| **Fun** | -100 to 100 | Constant, faster for playful Sims | Depression, slow movement |
| **Social** | -100 to 100 | Constant, slower for shy Sims | Loneliness, talking to self |
| **Room** | -100 to 100 | Based on room quality | Bad mood from ugly rooms |

The **Room** need is unique — it's not replenished by doing something but by *being somewhere nice*. Room score factors in: lighting, decoration value, cleanliness, open space, and the absence of dirty dishes and full trash cans.

### The Decay → Urgency → Behavior Loop

1. Needs decay over time
2. Low needs increase urgency
3. Urgency boosts advertisement scores for relevant objects
4. Sim autonomously seeks the highest-scoring advertisement
5. Interaction replenishes the need
6. Cycle repeats

This is Will Wright's "interesting failure" design philosophy: the game is interesting because things go wrong. Needs decay. Sims make bad choices. Fires start. The toilet breaks. The fun is managing the chaos.

## Career Tracks

Ten career paths, each with 10 levels. Advancement requires skill points, friend count, and job performance:

| Track | Entry Level | Top Level | Key Skills |
|-------|------------|-----------|-----------|
| Culinary | Dishwasher | Celebrity Chef | Cooking, Mechanical |
| Entertainment | Waiter/Waitress | Superstar | Charisma, Creativity |
| Law Enforcement | Security Guard | Captain Hero | Logic, Body |
| Medicine | Orderly | Chief of Hospital Staff | Logic, Mechanical |
| Military | Recruit | General | Body, Mechanical |
| Politics | Campaign Worker | Mayor | Charisma, Logic |
| Pro Athlete | Team Mascot | Hall of Famer | Body, Charisma |
| Science | Test Subject | Mad Scientist | Logic, Mechanical, Creativity |
| Xtreme | Daredevil | Icon | Body, Mechanical, Charisma |

Career data is stored at PersonData index 56 (job type), 57 (level/status), and 63 (performance rating).

## The Zodiac Connection

See `ZODIAC.md` for the full story, but the key insight: zodiac signs are computed from personality traits using Euclidean distance, not assigned independently. Your sign is a READING of who you are, not a box you're put in. Change your personality and your sign changes.

This connects to the Mind Mirror philosophy: personality is measurable, visible, and mutable. The system reflects you; you decide what to do about it.

## For MOOLLM

The `sims:` block in CHARACTER.yml maps 1:1 to the PersonData array:

```yaml
sims:
  traits:    { neat: 9, outgoing: 2, active: 6, playful: 3, nice: 5, generous: 5 }
  skills:    { cooking: 0, mechanical: 2, charisma: 1, logic: 7, body: 1, creativity: 3, cleaning: 8 }
  needs:     { hunger: 40, comfort: 60, hygiene: 70, bladder: 50, energy: 40, fun: 30, social: 20, room: 80 }
  career:    { track: unemployed, level: 0, experience: 0, performance: 50 }
  identity:  { age: adult, gender: null, zodiac: virgo, aspiration: null }
```

Beam down to The Sims: traits × 100 → PersonData slots. Beam up: PersonData slots ÷ 100 → traits. Lossless.

The Mind Mirror layer (`mind_mirror:`) lives alongside this. Sims data is BEHAVIOR (what they do). Mind Mirror is MOTIVATION (why they do it). Together: a complete person.

## References

- The Sims (Maxis/EA, 2000) — Will Wright's original game
- The Sims Wiki — [sims.fandom.com](https://sims.fandom.com)
- SimObliterator Suite — Jeff's binary format parser for Sims 1 save files
- FreeSO — Open source reimplementation of The Sims Online
