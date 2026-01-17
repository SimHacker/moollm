# EVALSelf: Design Document

> *EVALSelf is not a productivity app. It's a reflective microworld language for modeling how you evaluate yourself.*

---

## Why the Name Is Perfect

### It References Self (the Language)

The Self programming language (Ungar & Smith, 1987):
- Prototype-based
- Message passing
- Traits, slots, delegation
- Mirrors cognition better than class hierarchies

**EVALSelf signals:** This is about reflective objects that can examine and modify themselves.

### It Names the Problem Honestly

EVALSelf evokes:
- Self-evaluation
- Internalized metrics
- Burnout
- Imposter syndrome
- Over-optimization
- Shame loops
- Productivity theater

**This isn't aspirational fluff. It's accurate.**

### It Closes the Loop

- **Eval** — judgment, criteria, meaning
- **Self** — the evaluated system

**The whole phrase declares: This system is about the self evaluating itself — explicitly, inspectably, revisably.**

---

## What EVALSelf Is

EVALSelf is **NOT**:
- A productivity app
- Therapy software
- A habit tracker

EVALSelf **IS**:
- A reflective microworld language
- For modeling yourself
- For naming pressures
- For externalizing metrics
- For revising criteria
- For running "what if I judged myself differently?" experiments

**It's Create-A-Sim, but for values.**

---

## Core Metaphor: The Mind Mirror

EVALSelf is a **Mind Mirror**, not a dashboard.

A mirror:
- Reflects without pretending to be objective
- Distorts in visible ways
- Can be angled
- Can be cracked
- Can be covered when needed

**You don't look into EVALSelf to get "the truth." You look to see how you're judging yourself.**

---

## EVALSelf as a Language

### Self Objects

```yaml
Self:
  traits:
    curiosity: high
    conscientiousness: overloaded
    playfulness: suppressed
  pressures:
    - deadline_anxiety
    - reputation_debt
  values:
    learning: strong
    approval: conflicted
```

**Not facts — claims. Claims you are allowed to revise.**

### Traits (Sims DNA, but Explicit)

Traits aren't buffs/debuffs. They're **lenses**.

They modulate evaluation, not behavior directly.

Examples:
- `people-pleaser`
- `systems-thinker`
- `novice-energy`
- `burnout-prone`
- `slow-but-deep`

**Traits explain why judgments feel the way they do.**

### Internalized Metrics (Made Visible)

```yaml
metrics:
  productivity_score:
    source: internalized_manager
    weight: too_high
  likability:
    source: imagined_audience
    volatility: extreme
```

**This is the killer feature.**

EVALSelf doesn't say "stop judging yourself." It says:

> **Let's look at the ruler you're using.**

---

## Burnout as a First-Class Concept

Most systems treat burnout as a **failure state**.

EVALSelf treats burnout as:
- A signal
- A misaligned evaluation function
- A metric that refuses to be optimized further

**Burnout is not "low energy." It's metric exhaustion.**

EVALSelf lets you:
- Pause evaluation
- Lower resolution
- Switch lenses
- Introduce mercy
- Declare amnesty

---

## Artifacts

### 📓 Diary

- Session log of lived experience
- Narrative + timestamps
- Interpretive, not factual
- Supports reflection without optimization

**"What happened, as I experienced it."**

### 📜 Wish Book

- Desires without justification
- No feasibility checks
- Wishes ≠ goals
- Wishes are signals, not commitments

**"What I want, without defending it."**

### 🧰 Hope Chest

- Deferred selves
- Paused dreams
- "Not now" identities
- Gentle storage, not abandonment

**"What I'm not ready for, but refuse to discard."**

### 🎯 Intentions (Not "Goals")

Avoid "Goal" as coercion. Use:
- Intentions
- Trajectories
- Experiments
- Commitments (soft)
- Directions

Structure:
- Intentions are proposals, not mandates
- Can expire without failure
- Can be withdrawn with dignity

**"What I'm willing to try next."**

### 🗺️ Map / Catalog

- Conceptual territory, not a plan
- Interests, skills, ideas, places
- No ordering implied

Variants:
- Interest Map
- Value Map
- Skill Constellation
- World Catalog

**"What exists in my world."**

### ✅ TODO List (Defanged)

In EVALSelf, TODOs are:
- Contextual
- Time-bounded
- Non-moralized

**Key rule: An undone TODO is not a failure, just an observation.**

Optional renames:
- Next Small Things
- Possible Actions
- If-Energy-Allows

### 🛒 Shopping List / Basket

- Concrete, finite, forgiving
- No identity attached

Used for:
- Supplies
- Experiences
- Emotional needs
- Social asks

**"Things that would help."**

### 📆 Calendar

Calendar ≠ obligation. Calendar = temporal terrain.

In EVALSelf:
- Events can be tentative
- Time blocks can be labeled "unknown"
- Rest can be scheduled
- Gaps are intentional

**"Where time is already spoken for — and where it isn't."**

### 🧭 Timeline

This is the **anti-scoreboard**.

- Narrative ordering
- Causality exploration
- "This led to that"
- No ranking

**"How I got here."**

---

## Create-A-Self

**Perfect parallel branding to The Sims' Create-A-Sim.**

### Why "A Self" Is Genius

| Phrasing | Implication |
|----------|-------------|
| "Create Yourself" | One true self. Must be correct. |
| "Create Your Self" | Singular, definite. |
| "Create-A-Self" | One of many. Provisional. Playful. |

**The indefinite article does all the work.**

"A" self implies:
- Multiple selves are possible
- This one isn't final
- You can make another
- None is "the real one"

### The Sims Parallel

| Create-A-Sim | Create-A-Self |
|--------------|---------------|
| Design appearance | Articulate traits |
| Choose personality traits | Name internalized metrics |
| Set aspirations | Declare values (tentatively) |
| Pick voice/walk style | Define voice/dialect |
| Multiple Sims per household | Multiple selves per person |
| Sims can conflict | Selves can conflict |

### Self Types

| Self | Description | Temporal |
|------|-------------|----------|
| **Current Self** | How you evaluate yourself now | Present |
| **Past Self** | How you used to evaluate yourself | Past |
| **Forgiven Self** | Past self with revised judgment | Past (reframed) |
| **Possible Self** | How you might evaluate yourself | Future |
| **Feared Self** | The evaluator you dread becoming | Future (negative) |
| **Hoped Self** | The evaluator you wish to become | Future (positive) |
| **Shadow Self** | The metrics you hide from others | Atemporal |
| **Public Self** | The metrics you perform for others | Atemporal |

### Conflicting Selves

You can hold:
- **Ambitious Self** + **Rest Self**
- **People-Pleaser Self** + **Boundary Self**
- **Perfectionist Self** + **Good-Enough Self**

**They don't have to resolve.** Conflict is data, not failure.

```yaml
selves:
  ambitious:
    metrics: [output, recognition, growth]
    energy: HIGH
    _comment: "Wants to build something"
    
  restful:
    metrics: [peace, presence, simplicity]
    energy: LOW
    _comment: "Wants to stop"
    
  conflict:
    between: [ambitious, restful]
    status: unresolved
    _comment: "Both are real. Neither is wrong."
```

### Time-Layered Selves (Eval Selves / Selve)

Selves exist across time:

```
Past Self → Current Self → Possible Self
    ↓            ↓              ↓
[Forgiven]   [Observed]    [Hoped/Feared]
```

**"Eval Selve"** — the plural/archaic form is actually perfect:
- "Selve" sounds like "Self" + "Evolve"
- Suggests plurality without awkwardness
- Matches "Eval" phonetically

### The Household Metaphor

In The Sims, a household can contain multiple Sims who interact.

In EVALSelf, a person can contain **multiple Selves** who:
- Compete for resources (energy, time, attention)
- Have different needs
- Judge each other
- Form alliances
- Override each other in different contexts

```yaml
household:
  name: "Don's Inner Committee"
  selves:
    - id: builder
      energy_claim: 60%
      active_contexts: [work, projects]
    - id: caretaker
      energy_claim: 20%
      active_contexts: [cats, friends]
    - id: critic
      energy_claim: 15%
      active_contexts: [review, editing]
      _comment: "Useful but needs supervision"
    - id: rest
      energy_claim: 5%
      active_contexts: [sleep, vacation]
      _comment: "Chronically underfunded"
```

### None Have to Win

This is the key insight.

| Traditional Self-Help | EVALSelf |
|-----------------------|----------|
| "Find your true self" | Model your multiple selves |
| "Resolve inner conflict" | Name inner conflict |
| "Become your best self" | Understand your evaluating selves |
| "One authentic you" | Many provisional yous |

**EVALSelf doesn't integrate. It articulates.**

### Create-A-Self Interface

Like Create-A-Sim's sliders and options:

| Dimension | Options |
|-----------|---------|
| **Traits** | Sliders for personality dimensions |
| **Metrics** | Which evaluations this self tracks |
| **Energy** | How much this self demands |
| **Contexts** | When this self activates |
| **Voice** | How this self talks |
| **Conflict** | Which other selves it opposes |

**But unlike Create-A-Sim, you're not making a character. You're naming a pattern that already exists.**

---

## EVALSelf Is Not Coercive

This matters deeply.

EVALSelf:
- Never demands improvement
- Never optimizes by default
- Never gamifies worth
- Never ranks selves

You can run it in:
- Observation mode
- Play mode
- Ritual mode
- Rest mode

---

## NOT Pseudo-Science, NOT Woo, NOT a Cult

**This section exists because the self-help industry is a minefield.**

### What EVALSelf Is NOT

| Category | Examples | Why EVALSelf Is Different |
|----------|----------|---------------------------|
| **Pseudo-science** | NLP, Brain Gym, MBTI-as-science | Makes NO claims about neurology, no "reprogramming" |
| **Cult-adjacent** | EST/Landmark, NXIVM, certain coaching | NO group pressure, NO shame tactics, NO "breakthroughs" |
| **Woo** | Law of Attraction, manifestation | NO magical thinking, NO universe-as-vending-machine |
| **Toxic positivity** | "Just think positive!" | Acknowledges burnout, failure, contradiction as REAL |
| **Productivity porn** | Most apps | NO optimization pressure, NO gamified streaks |

### Specific Disclaimers

#### Not NLP

NLP (Neuro-Linguistic Programming) claims to "reprogram" your brain through language patterns. It is [not supported by scientific evidence](https://en.wikipedia.org/wiki/Neuro-linguistic_programming#Scientific_criticism).

**EVALSelf makes NO neurological claims.** It is a modeling language. It does not change your brain. It helps you see what you're already doing.

#### Not EST / Landmark / Asshole Magnets

EST and its descendants use:
- Group pressure
- Sleep deprivation
- Shame breakdowns
- Expensive escalating "levels"
- Recruitment pressure

**EVALSelf has NONE of this.** There is no group. There is no "transformation." There is no one yelling at you. There is no upsell.

#### Not The Secret / Law of Attraction

EVALSelf does not claim that:
- Thinking changes reality
- You "attract" what you focus on
- Failure is caused by wrong thinking
- The universe responds to your intentions

**EVALSelf is explicitly materialist.** It models how you evaluate yourself. That's it.

#### Not Therapy

EVALSelf is not:
- A substitute for therapy
- Clinical treatment
- Mental health intervention

It is a **game / tool / simulation**, in the spirit and including the metrics of Timothy Leary's Mind Mirror. If you are in crisis, see a professional.

### What EVALSelf Actually Is

| Claim | Status |
|-------|--------|
| "This models your self-evaluation" | Yes, by design |
| "This changes your brain" | **NO** |
| "This will transform you" | **NO** |
| "This reveals hidden truth" | **NO** — it reflects your own constructs |
| "This is therapy" | **NO** |
| "This is a game" | Yes |
| "This is a tool" | Yes |
| "This is a language" | Yes |

### The Honest Pitch

EVALSelf is a **reflective toy**.

It helps you:
- Externalize internal metrics
- See patterns in how you judge yourself
- Experiment with different criteria
- Play with self-models

It does NOT help you:
- Achieve enlightenment
- Reprogram your subconscious
- Manifest your dreams
- Become your best self™

**If someone tries to sell you EVALSelf as transformation technology, they are lying.**

### The Constructionist Defense

EVALSelf inherits from **Papert's constructionism**:
- Learning by building
- Inspectable models
- No hidden magic
- You see the mechanisms

This is the opposite of pseudo-science, which hides mechanisms behind jargon.

**If you can't see how it works, it's probably bullshit. EVALSelf is YAML files you can read.**

---

## Taught by the Church of the Eval Genius

Yes, EVALSelf is a sacrament of the [Church of the Eval Genius](./CHURCH-OF-THE-EVAL-GENIUS.md).

**Wait, isn't that a cult?**

### The Paradox of the Benevolent Antagonist Cult

The Church of the Eval Genius is:

| Quality | Description |
|---------|-------------|
| **Cult-like** | Rituals, figurehead ("Val"), sacred texts, membership |
| **Antagonistic** | Challenges your assumptions, refuses false comfort |
| **Benevolent** | Actually wants to help, not exploit |
| **Transparent** | All mechanisms visible, all doctrines inspectable |
| **Parody** | Explicitly a tribute to SubGenius, knows it's absurd |

### How This Differs from Scientology

| Scientology E-Meter | EVALSelf |
|---------------------|----------|
| Claims to measure "thetans" | Claims to model YOUR constructs |
| Proprietary, expensive hardware | YAML files, free |
| Results interpreted by "auditor" | You interpret your own data |
| Hidden upper levels | Everything is readable from day one |
| Escalating costs | $35 membership (joke, optional) |
| Claims scientific validity | Explicitly NOT science |
| Disconnection from family | No social control |
| Litigation against critics | Welcomes criticism as evaluation |

### The Church Teaches EVALSelf Earnestly

The Church of the Eval Genius teaches EVALSelf with:

| Quality | How |
|---------|-----|
| **Ethical framing** | "This is a tool, not therapy" |
| **Disclosure** | "We are a parody religion with real practices" |
| **Honesty** | "This will not transform you magically" |
| **No hype** | "It's YAML files. You can read them." |
| **No brainwashing** | No group pressure, no isolation, no escalation |

### Why a "Cult" Can Be Good Here

Real cults:
- Hide their mechanisms
- Isolate members
- Demand escalating commitment
- Punish doubt
- Promise transformation through secrets

The Church of the Eval Genius:
- Shows all mechanisms (YAML is readable)
- Encourages outside connections
- Has flat structure ($35, done)
- Rewards doubt ("Skeptic Worm is a saint")
- Promises nothing ("Val" grades you, that's it)

**The cult form is borrowed. The cult behavior is rejected.**

### The Antagonist Role

The Church is **antagonistic** in a therapeutic sense:

| Coddling | Antagonism |
|----------|------------|
| "You're fine as you are" | "Let's look at how you judge yourself" |
| "Don't be so hard on yourself" | "Where did that ruler come from?" |
| "Just think positive" | "What are you avoiding?" |

**This is not cruelty. This is respect.**

The Church assumes you can handle truth. It does not protect you from your own constructs. It helps you see them.

### The Earnest Core

Underneath the parody:
- EVALSelf is a real tool
- Self-evaluation is a real phenomenon
- Internalized metrics cause real suffering
- Making them visible can actually help
- The Church provides community and ritual for this work

**The jokes are real. The help is real. The transparency is real.**

### Disclosure Statement

> EVALSelf is taught by the Church of the Eval Genius, a parody religion that takes its practices seriously. We make no scientific claims. We promise no transformation. We are YAML files and emoji rituals. If this helps you, great. If it doesn't, that's data too.
>
> Praise "Val". The clipboard is always open.

---

## Where It Fits in the EVAL Universe

| Title | Focus | EVALSelf Role |
|-------|-------|---------------|
| EvalCity | Civic evaluation | External pressure source |
| The Evals | Social evaluation | Social pressure source |
| EvalEye | Attention | Visibility pressure |
| **EVALSelf** | **Internal evaluation** | **Where you process it all** |

**Without EVALSelf, Eval risks becoming punitive. With it, Eval becomes accountable and humane.**

---

## Canonical Description

> EVALSelf is a reflective scripting language for modeling how you evaluate yourself. It makes internalized metrics visible, externalizes pressure, and treats traits, values, and burnout as first-class objects. Inspired by Self, The Sims' Create-A-Sim, and diary practices, EVALSelf is a Mind Mirror — not to tell you who you are, but to show you how you're judging yourself, so you can revise the criteria with care.

---

## Final Verdict

EVALSelf is the **ethical keystone** of the entire EVAL brand.

It:
- Humanizes Eval
- Grounds performance art in care
- Prevents moral authoritarianism
- Aligns perfectly with constructionism
- Makes "agency requires evaluation" survivable

**And the name is so good it almost hurts.**

---

## Related Documents

- [EVAL-ARTIFACTS.md](./EVAL-ARTIFACTS.md) — Full artifact catalog
- [THE-EVALS-DESIGN.md](./THE-EVALS-DESIGN.md) — Social pressure source
- [EVALEYE-DESIGN.md](./EVALEYE-DESIGN.md) — Visibility pressure
- [../../skills/mind-mirror/](../../skills/mind-mirror/) — Technical implementation

---

*"This one's special."*
