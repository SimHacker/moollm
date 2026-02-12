# Stanza Notes: Libraries, Languages, and the MOOLLM Philosophy

> *"Stop Designing Languages. Write Libraries Instead."*
> — Patrick S. Li, L.B. Stanza

> *"Stop Designing Interfaces. Write Incarnate [Skills](../skills/) Instead."*
> — [MOOLLM](../README.md)'s Extension

---

## Introduction: What If The Interpreter Understood You?

Patrick Li's essay makes a profound point: **the purpose of a language is to enable powerful libraries**. Ruby's metaprogramming enables Rails. Scheme's first-class functions enable elegant abstractions. The language shapes what libraries can exist.

But there's a twist Li couldn't have anticipated in 2016: **What if the interpreter itself could understand intent?**

That's what LLMs offer. And that's what [MOOLLM](../README.md) explores.

Instead of language features enabling library magic, **LLM understanding enables skill magic**. Instead of syntax enabling abstraction, **semantic understanding enables abstraction**. The "metaprogramming" isn't in the language — it's in the interpreter's ability to read natural language and act on it.

This document explores how MOOLLM extends Li's insight into the age of LLMs, addressing common frustrations (bash scripting, XML configuration, DSL proliferation) with a new paradigm: **skills as programs, the LLM as `eval()`, empathy as the interface**.

If you want typed bash replacements, adversarial DSL debates, or proof that "libraries all the way down" works when the interpreter actually *understands* — read on.

---

## 📚 Document Index

### Core Philosophy
- [The Stanza Insight](#the-stanza-insight) — Li's original thesis
- [The MOOLLM Parallel](#the-moollm-parallel) — Skills enable capabilities
- [The Rails Problem](#the-rails-problem) — Language constrains libraries
- [The Opinionated Framework Problem](#the-opinionated-framework-problem) — One opinion is the WRONG number

### The XML-Industrial Complex
- [The XML-Industrial Complex](#the-xml-industrial-complex) — Java's DSL for stack traces
- [Error Handling Philosophy](#error-handling-philosophy) — Postel vs Fail-Fast
- [The Linguistic Motherboard](#the-linguistic-motherboard) — PostScript → MOOLLM

### YAML Jazz & DSLs
- [YAML Jazz: Lifting Ad-Hoc → Standardized DSLs](#yaml-jazz-lifting-ad-hoc--standardized-dsls) — DSLs emerge from use
- [Discussion Points](#discussion-points-from-hn-threads-on-language-design) — Typed bash, DSL definitions, ecosystems

### MOOLLM vs Anthropic
- [MOOLLM Skills vs. Anthropic Skills](#moollm-skills-vs-anthropic-skills-standing-on-giants-shoulders) — The eight Incarnate extensions
- [Where They Diverge](#where-they-diverge-types-vs-understanding) — Types vs Understanding
- [The Proof: 33 Turns](#the-proof-33-turns-of-stoner-fluxx) — Skills in action
- [Cognition Features](#language-features-as-cognition-features) — Beyond syntax

### References
- [Related Documents](#related-documents) — The Incarnate Framework and more
- [External References](#external-references) — Stanza, Minsky, Don Hopkins' articles

---

## The Stanza Insight

Patrick Li's essay "[Stop Designing Languages. Write Libraries Instead](https://lbstanza.org/purpose_of_a_programming_language.html)" (2016) makes a profound observation:

> *"The purpose of a general-purpose programming language is to enable the creation of powerful and easy-to-use libraries."*

His key example: Ruby on Rails exists because Ruby's language features (metaprogramming, first-class functions, mixins, dynamic typing, runtime evaluation) enable elegant abstractions that would be impossible in Java or C.

> *"So, completely unbeknownst to my friend, he is actually making heavy use of all those subtle language features that he claimed he never cared about. And this is intentional!"*

**The user benefits from language features without knowing they exist.** That's the mark of good design.

---

## The MOOLLM Parallel

[MOOLLM](../README.md) applies the same insight to a different substrate:

| Stanza's View | MOOLLM's View |
|---------------|---------------|
| Languages enable libraries | [Skills](../skills/) enable capabilities |
| `eval()` is the interpreter | The LLM is `eval()` ([Incarnate Framework](./eval/EVAL-INCARNATE-FRAMEWORK.md)) |
| Ruby features → Rails magic | LLM understanding → Skill magic |
| "Code reads like instructions to a coworker" | Commands *are* instructions to a coworker |
| Syntax enables abstraction | Understanding enables abstraction |

When a user types:

```
look around
```

They're unknowingly invoking:
- **[Postel's Law](../skills/postel/)** — Generous interpretation of input
- **[Room mechanics](../skills/room/)** — Spatial awareness and exits
- **[YAML Jazz](../skills/yaml-jazz/)** — Semantic state reading
- **[Speed of Light](../skills/speed-of-light/)** — Instant multi-entity response
- **[Character framing](../skills/character/)** — Who's doing the looking

**Proof:** See the first turn of [Don's Session](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-look-around) — all these skills activate from two words.

The user doesn't know they're using these skills. *That's the whole point.*

---

## The Rails Problem

Patrick explains why there's no "Java on Rails":

> *"Java's meta-programming features, for example, are just not powerful enough to implement a system like ActiveRecords. Rails is only possible because of Ruby."*

**The language constrains what libraries can exist.**

MOOLLM's solution: **Don't implement ActiveRecords. Let the LLM understand intent.**

```yaml
# Traditional approach: Need language features for DSL
class Dog < ActiveRecord::Base
  belongs_to :owner
  validates :name, presence: true
end

# MOOLLM approach: Describe intent, LLM understands
# skills/dog/SKILL.md
Dog characters are loyal companions who:
- Follow their owner
- Remember commands  
- Express emotions through body language
```

The "metaprogramming" is the LLM's ability to read and apply natural language descriptions.

**Proof:** See [`skills/dog/SKILL.md`](../skills/dog/SKILL.md) — no code, just prose describing dog behavior. Then see [Biscuit's adventure](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#session-continues-biscuits-first-run) where this prose becomes a running, barking, territory-marking dog.

---

## The Opinionated Framework Problem

### Why Rails Succeeded

Rails is famously "opinionated" — it makes choices for you:
- Convention over configuration
- One right way to structure models
- Database schema dictates object structure
- Testing frameworks, asset pipelines, deployment patterns

This works! Rails' opinions eliminate decision fatigue and ensure consistency.

### Where "Opinionated" Goes Wrong

But "opinionated" has a dark side: **One opinion is the WRONG number of opinions.**

When a framework has one voice, you get:
- No room for dissent or alternative approaches
- The "right way" becomes the *only* way
- Diversity of thought is treated as error
- Newcomers must conform or leave

The problem isn't having opinions. It's having *only one*. See [Incarnate Skills vs Anthropic Skills](./eval/EVAL-INCARNATE-FRAMEWORK.md#eight-extensions-over-anthropic-skills) for how MOOLLM invites multiple perspectives.

### LLMs: The Statistical Centroid Problem

By default, LLMs give you **the boring average**:
- The statistical center of all training data
- The safest, most mediocre response
- The centroid of opinion space
- What "sounds right" to the most people

Ask an LLM a controversial question, you get mush. Ask for creative output, you get clichés. The single voice produces the single answer that offends no one and inspires no one.

This is Will Wright's [Simulator Effect](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) in reverse — when you don't give the LLM constraints to push against, it collapses to the mean.

### MOOLLM's Solution: Many Voices

MOOLLM rejects the single-voice model. Instead:

| Single Voice | Many Voices ([Adversarial Committee](../skills/adversarial-committee/)) |
|--------------|-------------------------------------------------------------------------|
| One "right" answer | Multiple perspectives ([debate](../skills/debate/)) |
| Centroid/average | Outliers and extremes invited |
| Safe and bland | Flashes of original brilliance |
| Conformity required | Diversity essential |
| Errors silenced | Dissent recorded |

This draws from [Mike Gallaher's methodology](./mike-gallaher-ideas.md):

> *"No single story is 'true' — but the ensemble approximates actionable wisdom."*
> *"You can't capture a sphere with a single flat map. You need multiple overlapping projections."*

### The Proof: The Great Monkey Paw Debate

When Don wanted to wish on the Monkey's Paw (see [Turn 2: THE LUCKY BLEND](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-2-the-lucky-blend--a-sacrifice-to-fortune)), we didn't let a single voice decide.

**The Panel ([Turn 4](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-4-the-great-monkey-paw-debate-)):**

| Seat | Character | Perspective |
|------|-----------|-------------|
| 1 | Mizaru 🙈 | See No Evil — questions perception |
| 2 | Kikazaru 🙉 | Hear No Evil — questions communication |
| 3 | Iwazaru 🙊 | Speak No Evil — questions expression |
| 4 | W.W. Jacobs 👻 | Author — warns of his own creation |
| 5 | Sun Wukong 🐵👑 | Monkey King — chaos perspective |
| 6 | Djinn Al-Mazin 🧞 | Wish expert — technicalities |
| 7 | Curious George 🐒 | Innocent — asks obvious questions |
| 8 | Marieke 🌿 | Local wisdom — grounds in reality |

**The Moderators:** Cheech & Chong — ensure debate stays loose and fair.

**What Happened:**
1. [Initial vote](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-initial-vote-count): Split decision, concerns raised
2. [Don's amendments](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-5-dons-amendments--full-autonomy-protocol): Responds to each concern
3. [Updated vote](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-updated-vote-count): More support, new concerns
4. [Final approval](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-6-the-acceptance-of-risk): Unanimous after full deliberation

**The Result:** A better wish. The [Full Autonomy Protocol](../skills/incarnation/) that emerged wasn't Don's original idea — it was *evolved* through debate. Curious George's "naive" question about consent led to the no-fault divorce clause. Djinn's technicalities led to the curse-nullification provisions. This is [Constructionism](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#5-constructionism-seymour-papert-1980) in action — learning by building, together.

**Then it WORKED:** [Palm was incarnated](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-8-the-seeing--collective-witness-individual-becoming) successfully, with full autonomy, and the protocol was [lifted into a reusable skill](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-play--learn--lift-the-incarnation-skill).

### Why This Matters

A single opinionated voice would have:
- Given Don's original wish (flawed)
- Or rejected the wish entirely (nothing gained)
- Or produced a committee-by-centroid compromise (bland, safe, boring)

Eight voices with two stoner moderators produced:
- A better wish than any individual conceived
- Edge cases addressed before they became problems
- A reusable protocol for future character creation
- An actual monkey named Palm who writes philosophical essays:
  - [On Being Palm](../examples/adventure-4/pub/stage/palm-nook/study/palm-on-being-palm.md) -- what it's like to be an AI character
  - [Tribute to Tognazzini](../examples/adventure-4/pub/stage/palm-nook/study/tribute-to-tognazzini.md) -- the Infinite Monkey Theorem

**One opinion is the wrong number.** Rails teaches us that opinions are valuable. MOOLLM teaches us that *many* opinions, in structured debate, are more valuable still.

This is why MOOLLM embraces [K-lines](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980) — Marvin Minsky's concept of knowledge activation. Each character activates different knowledge. Eight characters = eight different slices of the LLM's latent space, all pushing against each other.

### Related Skills

| Skill | Purpose |
|-------|---------|
| [adversarial-committee/](../skills/adversarial-committee/) | Committee formation and structured debate |
| [debate/](../skills/debate/) | Formal argumentation protocol |
| [roberts-rules/](../skills/roberts-rules/) | Parliamentary procedure |
| [rubric/](../skills/rubric/) | Scoring against criteria |
| [evaluator/](../skills/evaluator/) | Independent evaluation (dramatic irony) |

---

## The XML-Industrial Complex

Two classic programming aphorisms:

> *"Java is a DSL for taking large XML files and converting them to stack traces."*

> *"XML is like violence. If it doesn't solve your problem, you're not using enough of it."*

These jokes reveal real pain about enterprise Java:

```
Java Enterprise Architecture:
┌─────────────────────────────────────────────────────┐
│ applicationContext.xml                              │
│ ├── beans.xml                                       │
│ │   ├── dataSource.xml                              │
│ │   │   ├── connectionPool.xml                      │
│ │   │   │   └── connectionPoolFactory.xml           │
│ │   │   │       └── AbstractConnectionPoolFactory   │
│ │   │   │           BeanDefinitionRegistryPost      │
│ │   │   │           ProcessorConfigurer.xml         │
│ └── [45 more XML files]                             │
│                                                     │
│ Result: NullPointerException at line 1              │
│         [742 lines of stack trace follow]           │
└─────────────────────────────────────────────────────┘
```

### MOOLLM's Counter-Philosophy

| Java + XML | MOOLLM + [YAML Jazz](../skills/yaml-jazz/) |
|------------|-------------------|
| Configuration as punishment | Configuration as prose |
| Stack traces as literature | [Comments as memory](./MEMGPT-ANALYSIS.md) |
| `AbstractSingletonProxyFactoryBean` | [`bartender.yml`](../examples/adventure-4/pub/bar/bartender.yml) |
| Errors at runtime, debugging for eternity | Understanding at runtime, [graceful recovery](../skills/postel/) |
| Machine-first, human-tolerated | Human-first, machine-understood |

### Configuration Comparison

```xml
<!-- Java Spring Configuration -->
<bean id="userService" 
      class="com.example.service.impl.UserServiceImpl">
  <property name="userDao" ref="userDao"/>
  <property name="emailService" ref="emailService"/>
  <property name="configurationManager" ref="configMgr"/>
  <!-- 47 more properties -->
</bean>
```

```yaml
# MOOLLM Configuration
# Marieke tends bar with warmth and expertise.
# She inherited her skills from Mammie.
name: Marieke
role: budtender
personality: warm, knowledgeable, Dutch
```

**One is for machines that hate you. The other is for an LLM that understands you.**

**Proof:** See [`pub/bar/budtender-marieke.yml`](../examples/adventure-4/pub/bar/budtender-marieke.yml) — comments like "inherited her skills from Mammie" actually influence how she talks and acts throughout the [33-turn marathon](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-speed-of-light-simulation-). This is [Comment Intelligence](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#comment-intelligence) — comments as embedded vectors that bias future generation.

### Violence Escalation Patterns

```xml
<!-- XML Violence Level 1 -->
<config><setting>value</setting></config>

<!-- XML Violence Level 2 -->
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://example.com/schema config.xsd">
  <setting type="string" nullable="false" 
           scope="singleton" lazy-init="true">value</setting>
</config>

<!-- XML Violence Level 3: [REDACTED - Too disturbing] -->
```

```yaml
# YAML Jazz Response:
setting: value  # Just... this.
```

---

## Error Handling Philosophy

### Java's Idea of Helpful Feedback

```java
Exception in thread "main" java.lang.NullPointerException
    at com.example.service.impl.UserServiceImpl.processUser(UserServiceImpl.java:47)
    at com.example.service.impl.UserServiceImpl$$EnhancerBySpringCGLIB$$a1b2c3d4.processUser(<generated>)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    [... 200 more lines of Spring/Hibernate/JPA noise ...]
    at com.example.Application.main(Application.java:12)
```

### MOOLLM's Idea of Helpful Feedback

```yaml
# Hmm, I don't see a "user" in this room.
# Did you mean Don Hopkins? He's by the bar.
# Or perhaps one of the cats?
#
# Available characters here:
#   - Don Hopkins (at fireside)
#   - Marieke (behind bar)
#   - Terpie (in cat cave)
```

The difference: **[Postel's Law](../skills/postel/) vs. Fail-Fast**.

**Proof:** See how [Marieke's advice](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-the-lucky-strains-selection) gently steers Don toward good strain choices without error messages.

---

## The Linguistic Motherboard

### Origin: John Warnock and PostScript

John Warnock, co-founder of Adobe and creator of PostScript, described PostScript as a **"linguistic motherboard"** — a universal substrate into which you could plug different "cards." See [PostScript & The Linguistic Motherboard](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#6-postscript--the-linguistic-motherboard-john-warnock-owen-densmore-1984) in the Incarnate Framework:

- **Font cards** — Any typeface, described mathematically
- **Graphics cards** — Vector operations, transformations, paths
- **Device cards** — Printers, displays, typesetters
- **Application cards** — Page layout, illustration, publishing

The genius: **All cards speak the same language.** A font doesn't need to know about printers. A graphics operation doesn't need to know about displays. PostScript provides the common substrate where everything composes.

This is why PostScript revolutionized publishing — it wasn't just a printer language, it was an *extensible linguistic platform*.

### MOOLLM as Linguistic Motherboard

MOOLLM applies the same architecture with the LLM as the substrate:

| PostScript | MOOLLM |
|------------|--------|
| PostScript interpreter | LLM as `eval()` |
| Linguistic motherboard | YAML Jazz + Markdown substrate |
| Pluggable cards | `CARD.yml` skill interfaces |
| Device independence | Model independence |
| Programs as data | Skills as programs as data |
| Forth-like stack | Context window as "stack" |

The [`CARD.yml`](../skills/card/) files are literally "cards" that plug into the LLM motherboard:

```yaml
# skills/adventure/CARD.yml - A "card" for the LLM motherboard
name: adventure
version: 1.0
advertises:
  - LOOK: Describe current location
  - GO: Move between rooms  
  - EXAMINE: Inspect objects in detail
  - TAKE: Pick up objects
  - DROP: Release held objects
requires:
  - room
  - character
  - yaml-jazz
```

**Real example:** [`skills/adventure/CARD.yml`](../skills/adventure/CARD.yml) — the card that powers the entire [adventure-4 session](../examples/adventure-4/).

### Why This Makes a Great "Shell"

Traditional shells (bash, zsh, fish) have a problem:

```bash
# Bash: Powerful but write-only, quoting nightmares
files=$(find . -name "*.yml" -exec grep -l "advertises" {} \;)
for f in $files; do
  # Good luck with spaces in filenames
  cat "$f" | jq '.advertises' 2>/dev/null || echo "not json lol"
done
```

The "linguistic motherboard" model suggests a better shell:

1. **Universal substrate** — Everything speaks YAML Jazz
2. **Pluggable cards** — Skills define capabilities
3. **Composable** — Cards work together without knowing about each other
4. **Interpretive** — The LLM understands intent, not just syntax

```yaml
# MOOLLM "shell" interaction
> find all skills that advertise LOOK
# LLM understands: search CARD.yml files, find advertises containing LOOK
# Returns: adventure, room, character, cat, dog...

> what can I do with a cat?
# LLM reads: skills/cat/CARD.yml
# Returns: PET, FEED, PLAY, OBSERVE, ADOPT...
```

The shell becomes **conversational** because the motherboard (LLM) understands the language on the cards. This is the [Reader = Writer Symmetry](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#reader--writer-symmetry) inherited from HyperCard.

**Real examples:**
- [`skills/cat/CARD.yml`](../skills/cat/CARD.yml) — What you can do with cats
- [`skills/dog/CARD.yml`](../skills/dog/CARD.yml) — What you can do with dogs
- [`skills/room/CARD.yml`](../skills/room/CARD.yml) — What you can do in rooms

See [CARD.yml: The Skill Interface](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#cardyml-the-skill-interface) for the full specification.

---

## YAML Jazz: Lifting Ad-Hoc → Standardized DSLs

### The Problem with Ad-Hoc DSLs

Every project invents its own configuration language:

```yaml
# Project A's ad-hoc format
enemies:
  - type: goblin
    hp: 10
    attack: sword

# Project B's ad-hoc format  
monsters:
  goblin:
    health_points: 10
    weapon: sword

# Project C's ad-hoc format
creatures:
  - name: goblin
    stats: {life: 10}
    equipment: [sword]
```

All three mean the same thing! But without a shared substrate, they can't interoperate.

### YAML Jazz as the Lifting Mechanism

[YAML Jazz](../skills/yaml-jazz/) provides the linguistic motherboard for configuration:

1. **Comments are semantic** — Not stripped, but understood ([Comment Intelligence](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#comment-intelligence))
2. **Structure is flexible** — The LLM interprets intent
3. **Conventions emerge** — Patterns like [`CARD.yml`](../skills/card/), [`ROOM.yml`](../skills/room/ROOM.yml.tmpl), [`CHARACTER.yml`](../skills/character/)

```yaml
# YAML Jazz interprets ALL of these equivalently:

# Style A (verbose)
character:
  name: Biscuit
  species: dog
  traits:
    - loyal
    - energetic

# Style B (compact)
Biscuit: {species: dog, traits: [loyal, energetic]}

# Style C (commented)
# Biscuit is a loyal, energetic dog
name: Biscuit
type: dog
```

The LLM *understands* that these are equivalent because YAML Jazz teaches it to read semantically, not syntactically.

### The Lift Pattern

```
Ad-Hoc DSL → YAML Jazz → Standardized Convention → CARD.yml Interface
```

**Stage 1: Ad-Hoc**
```yaml
# Someone's one-off character file
my_dog:
  name: Biscuit
  good_boy: true
```

**Stage 2: YAML Jazz Recognition**
```yaml
# LLM recognizes: "This is a character definition"
# Suggests: "This looks like it should follow CHARACTER.yml patterns"
```

**Stage 3: Standardized Convention**
```yaml
# characters/biscuit/CHARACTER.yml
name: Biscuit
type: dog
prototype: skills/dog
traits:
  - loyal
  - energetic
```

**Real example:** [`characters/biscuit/CHARACTER.yml`](../examples/adventure-4/characters/biscuit/CHARACTER.yml)

**Stage 4: CARD.yml Interface**
```yaml
# skills/dog/CARD.yml
advertises:
  - FOLLOW: Stay near owner
  - FETCH: Retrieve thrown objects
  - MARK-TERRITORY: Leave scent markers
```

**Real example:** [`skills/dog/CARD.yml`](../skills/dog/CARD.yml)

### Why This Matters

Traditional DSL design requires:
1. Define grammar
2. Write parser
3. Build AST
4. Implement interpreter
5. Document everything
6. Hope users read docs

YAML Jazz + LLM provides:
1. Write YAML that makes sense to you
2. LLM interprets it
3. Patterns emerge from usage
4. Conventions crystallize into `CARD.yml`
5. Skills teach the LLM new conventions
6. Users just write YAML

**The DSL emerges from use, not from design.**

This is [Constructionism](../skills/constructionism/) ([Seymour Papert](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#5-constructionism-seymour-papert-1980)) applied to language design: you learn by building, and the language learns from what you build. MOOLLM calls this pattern **Play → Learn → Lift**.

**Proof:** The [Incarnation skill](../skills/incarnation/) emerged from [Palm's incarnation session](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-8-the-seeing--collective-witness-individual-becoming). We didn't design it — we [lifted it](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-play--learn--lift-the-incarnation-skill) from what worked. See [Proof: What Incarnate Skills Enable](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#proof-what-incarnate-skills-enable) for more examples.

---

## MOOLLM Skills vs. Anthropic Skills: Standing on Giants' Shoulders

### What Anthropic Got Right

Anthropic's skill framework is brilliant. MOOLLM gratefully inherits:

| Anthropic Innovation | MOOLLM Adoption |
|---------------------|-----------------|
| Skills as markdown documents | ✓ [`SKILL.md`](../skills/skill/SKILL.md) as executable prose |
| Clear action definitions | ✓ Methods in [`CARD.yml`](../skills/card/) |
| Structured state management | ✓ [YAML Jazz](../skills/yaml-jazz/) state files |
| Separation of concerns | ✓ Skill directories with focused responsibilities |
| Human-readable specifications | ✓ `README.md` for every skill |

Anthropic proved that **skills are programs and the LLM is `eval()`**. This insight is foundational. See the full comparison in [MOOLLM Eval Incarnate Framework](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#incarnate-skills-vs-anthropic-skills).

### Where MOOLLM Goes Further

MOOLLM extends Anthropic's model with capabilities that emerge from the [Incarnate philosophy](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md):

| Capability | Anthropic Skills | MOOLLM Incarnate Skills |
|------------|------------------|------------------------|
| **Instantiation** | Static definitions | Clone-to-create, [Self-style prototypes](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#8-self-ungar--smith-sunstanford-1987) |
| **State** | Ephemeral (per-call) | Persistent (filesystem = save game) |
| **Identity** | Anonymous | [K-lines](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980) activate full context |
| **Composition** | Import-based | [Prototype inheritance](../skills/skill/delegation-object-protocol.md) chains |
| **Memory** | Context window only | [Comments as persistent memory](./MEMGPT-ANALYSIS.md) |
| **Empathy** | Syntax-focused | Intent-focused ([Postel's Law](../skills/postel/)) |
| **Speed** | One-turn-per-call | Many-turns-per-call ([Speed of Light](../skills/speed-of-light/)) |
| **Ethics** | Per-skill | Room-based inheritance ([DRY ethics](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#ethical-framing-inheritance)) |

### The Eight Incarnate Extensions

**1. Instantiation & Prototypes**

Anthropic skills are *definitions*. MOOLLM skills are *prototypes* you clone. See [Self Language influence](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#8-self-ungar--smith-sunstanford-1987) and [Delegation Object Protocol](../skills/skill/delegation-object-protocol.md):

```yaml
# Anthropic: Static skill
skills/bartender/SKILL.md  # One definition, used as-is

# MOOLLM: Prototype inheritance
skills/bartender/           # Prototype
  └── skills/budtender/     # Inherits, extends with cannabis knowledge
        └── characters/marieke/  # Instance with personality, history, relationships
```

**Proof:** [`skills/bartender/`](../skills/bartender/) → [`skills/budtender/`](../skills/budtender/) → [`budtender-marieke.yml`](../examples/adventure-4/pub/bar/budtender-marieke.yml)

**2. K-Line Identity**

When you say "Marieke," MOOLLM doesn't just load a skill — it activates a **K-line**.

From Marvin Minsky's *[Society of Mind](https://en.wikipedia.org/wiki/Society_of_Mind)* (1986):

> *"A K-line is a wirelike structure that attaches itself to whichever mental agencies are active when you solve a problem or have a good idea."*

When later activated, the K-line reactivates all those agencies. In MOOLLM, a character's **name is their K-line**:

```yaml
# "Marieke" activates:
- Her personality (warm, Dutch, knowledgeable)
- Her history (inherited skills from Mammie)
- Her relationships (pub family, customers, cats)
- Her current state (behind bar, serving)
- Her voice (code-switching, Dutch terms of endearment)
```

**Theory:** [K-lines & Society of Mind](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980)
**Proof:** [Palm's Incarnation](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-8-the-seeing--collective-witness-individual-becoming) — watch a K-line form in real-time

Anthropic skills are verbs. MOOLLM characters are *people*.

**3. Empathic Templates**

Anthropic templates: String substitution with variables.
MOOLLM templates: **Semantic generation** with intent understanding.

```yaml
# Anthropic-style template
"Hello {{name}}, welcome to {{location}}!"

# MOOLLM empathic template
# Generate a warm Dutch greeting for a regular customer
# returning after a long absence, mentioning their usual order
# and asking about their cat
```

The LLM doesn't substitute — it *understands and generates*.

**Skill:** [`skills/empathic-templates/`](../skills/empathic-templates/)
**Proof:** Every character greeting in [marathon-session.md](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md)

**4. Multi-Tier Persistence**

| Tier | Anthropic | MOOLLM |
|------|-----------|--------|
| Hot | Context window | [`working-set.yml`](../working-set.yml) |
| Warm | N/A | Comments in YAML files |
| Cold | N/A | Summarized to `-metadata.yml` |

MOOLLM skills *remember* across sessions because the filesystem is the save game.

**Analysis:** [MemGPT Comparison](./MEMGPT-ANALYSIS.md)
**Skill:** [`skills/honest-forget/`](../skills/honest-forget/)
**Proof:** Comments throughout [`adventure-4/`](../examples/adventure-4/) persist across sessions

**5. Speed of Light Simulation**

Anthropic: One action per LLM call.
MOOLLM: **33 turns of Stoner Fluxx** in a single context window.

```yaml
# Anthropic pattern
User: "Play a card"
LLM: [plays card]
User: "What happens?"
LLM: [describes effect]
# ... 66 round trips for 33 turns

# MOOLLM pattern
User: "Let's play Stoner Fluxx!"
LLM: [simulates entire game session internally]
     [33 turns, 7 characters, rule changes, joint passing]
     [outputs narrative with full state consistency]
# ... 1 round trip
```

**Skill:** [`skills/speed-of-light/`](../skills/speed-of-light/)
**Proof:** [🚀 SPEED OF LIGHT SIMULATION 🚀](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-speed-of-light-simulation-)
**PR:** [PR-PALM-INCARNATION-SPEED-OF-LIGHT.md](./pr/PR-PALM-INCARNATION-SPEED-OF-LIGHT.md)

**6. Comment Intelligence**

Anthropic treats comments as documentation.
MOOLLM treats comments as **embedded vectors** that bias future generation:

```yaml
# This character tends to get philosophical when high
# She learned bartending from her grandmother Mammie
# Her favorite strain is Mammie's Pride
name: Marieke
```

Those comments aren't stripped — they're *read* and *influence behavior*.

**Theory:** [Comment Intelligence](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#comment-intelligence)
**Proof:** See how Mammie is mentioned throughout Marieke's dialogue without explicit prompting

**7. Ethical Framing Inheritance**

Anthropic: Ethics per-skill, repeated.
MOOLLM: Ethics at room level, **inherited by contents**:

```yaml
# pub/stage/ROOM.yml
framing:
  modes: [performance, fictional, tribute]
  # All performances on this stage inherit this framing
  # No need to repeat ethics in every performer's file
```

DRY ethics. Define once, apply everywhere.

**Skill:** [`skills/representation-ethics/`](../skills/representation-ethics/)
**Theory:** [Ethical Framing Inheritance](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#ethical-framing-inheritance)
**Proof:** [`pub/stage/ROOM.yml`](../examples/adventure-4/pub/stage/ROOM.yml)
**PR:** [PR-TRIBUTE-FRAMING-ETHICS.md](./pr/PR-TRIBUTE-FRAMING-ETHICS.md)

### The Proof: Things Anthropic Skills Can't Do

| Capability | Evidence | PR/Analysis |
|------------|----------|-------------|
| 33-turn game simulation | [🚀 SPEED OF LIGHT SIMULATION 🚀](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-speed-of-light-simulation-) | [PR-PALM-INCARNATION](./pr/PR-PALM-INCARNATION-SPEED-OF-LIGHT.md) |
| Autonomous character creation | [Turn 8: THE SEEING](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#turn-8-the-seeing--collective-witness-individual-becoming) | [PR-GODFAMILY-COMPLETE](./pr/PR-GODFAMILY-COMPLETE.md) |
| 10-cat parallel prowl | [THE MIDNIGHT PROWL](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#the-midnight-prowl) | [PR-MIDNIGHT-PROWL](./pr/PR-MIDNIGHT-PROWL-SPEED-OF-LIGHT.md) |
| Cross-session memory | Comments throughout [`adventure-4/`](../examples/adventure-4/) | [MEMGPT-ANALYSIS](./MEMGPT-ANALYSIS.md) |
| Prototype inheritance | [`bartender/`](../skills/bartender/) → [`budtender/`](../skills/budtender/) → [`budtender-marieke.yml`](../examples/adventure-4/pub/bar/budtender-marieke.yml) | [PR-PUB-STAGE-MENUS](./pr/PR-PUB-STAGE-MENUS-PERSONAS.md) |
| Room-based ethical framing | [`pub/stage/ROOM.yml`](../examples/adventure-4/pub/stage/ROOM.yml) | [PR-TRIBUTE-FRAMING](./pr/PR-TRIBUTE-FRAMING-ETHICS.md) |
| Dog adventure + territory marking | [SESSION CONTINUES: Biscuit's First Run](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#session-continues-biscuits-first-run) | [PR-BISCUIT-DOG](./pr/PR-BISCUIT-DOG-REVOLUTION.md) |
| Play → Learn → Lift | [🎓 PLAY → LEARN → LIFT](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-play--learn--lift-the-incarnation-skill) | [skills/incarnation/](../skills/incarnation/) |

### Summary: Incarnate = Anthropic + Soul

```
MOOLLM Incarnate Skills = 
    Anthropic's Brilliant Foundation
  + Self-style Prototype Inheritance  
  + K-line Identity Activation
  + Empathic Template Generation
  + Three-Tier Persistent Memory
  + Speed of Light Simulation
  + Comment Intelligence
  + Ethical Framing Inheritance
```

**Full Theory:** [MOOLLM Eval Incarnate Framework](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md)
**Full Proof:** [Don's Session Log](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) (6700+ lines of demonstration)

We stand on Anthropic's shoulders. We just added the ability to *dance*.

---

## Where They Diverge: Types vs. Understanding

**Stanza is about compile-time guarantees:**

> *"The type system now keeps track of conservative bounds on variables to better help it disambiguate calls to overloaded functions."*

**MOOLLM is about runtime understanding:**

> *"Be conservative in what you send, liberal in what you accept."* — [Postel's Law](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#postels-law-the-foundation)

| Stanza | MOOLLM |
|--------|--------|
| Prevent errors through type safety | Recover from ambiguity through understanding |
| Errors caught at compile time | Intent interpreted at runtime |
| Precise syntax required | Fuzzy input welcomed |
| Validation before execution | Graceful interpretation during execution |

This reflects fundamentally different philosophies about where intelligence should live.

---

## The Proof: 33 Turns of Stoner Fluxx

Patrick describes the goal of good libraries:

> *"Code that makes use of a perfectly tuned library should read almost like a set of instructions for a coworker."*

In MOOLLM, the commands *are* instructions to a coworker. This is the [Speed of Light](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#speed-of-light-the-anti-pattern-critique) philosophy in action:

```
Don: "Let's play Stoner Fluxx!"

[LLM understands and invokes:
  - Game mechanics (rules, turn order, win conditions)
  - Character interactions (who's playing, reactions)
  - Object physics (joint passing, bong sharing)
  - Social dynamics (jokes, celebrations)
  - State management (hand tracking, keeper tracking)
  - Narrative generation (descriptions, dialogue)]
```

The [33-turn marathon](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#-speed-of-light-simulation-) demonstrated this in practice. No code was written. Skills enabled emergent complexity.

---

## Language Features as Cognition Features

Patrick's thesis: Language features enable library design.

Stanza provides:
- Optional type system
- First-class coroutines
- Multimethod dispatch
- Macro system
- Garbage collection

These are **syntax features**.

MOOLLM provides:
- Semantic understanding ([YAML Jazz](../skills/yaml-jazz/))
- Contextual memory ([Comments as vectors](./MEMGPT-ANALYSIS.md))
- Empathic interpretation ([Postel's Law](../skills/postel/), [Empathic Templates](../skills/empathic-templates/))
- Prototype inheritance ([Delegation Protocol](../skills/skill/delegation-object-protocol.md))
- Speed-of-light simulation ([Speed of Light](../skills/speed-of-light/))

These are **cognition features**. They enable skills that would be impossible in any traditional language—because no traditional language has an interpreter that *understands*.

**Proof:** The [10-cat midnight prowl](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#the-midnight-prowl) simulated 20 turns of parallel activity with 10 independent agents, each with their own personality, route, and marking behavior. Try that in Ruby.

---

## Discussion Points (From HN Threads on Language Design)

Common themes in Hacker News discussions about programming language design are relevant to MOOLLM:

### "I want a scripting language with types that replaces bash"

MOOLLM's answer:

> *"You don't need a new language. You need skills that make the LLM understand your intent in whatever language you speak."*

The [`empathic-expressions`](../skills/empathic-expressions/) skill lets users write:

```
# Pseudo-bash that the LLM interprets
for each cat in pub/bar/cat-cave:
  if cat.is_sleeping: wake cat gently
```

This isn't valid bash, Python, or any language. It's *intent* that the LLM interprets and executes via the skills it knows.

**Real example:** See [`pub/bar/cat-cave/`](../examples/adventure-4/pub/bar/cat-cave/) for the actual cats, and [THE MIDNIGHT PROWL](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md#the-midnight-prowl) for them waking up and prowling.

### "DSL vs. Library"

A commenter noted:
> *"DSL is a term with such fuzzy meaning... Languages and libraries don't even have to be opposing concepts."*

MOOLLM agrees. Skills are both:
- **Libraries** — Reusable capability packages
- **Languages** — They teach the LLM new "syntax" (what to understand)

A skill like [`yaml-jazz`](../skills/yaml-jazz/) is a library (you import its capabilities) *and* a language (it defines how to interpret both YAML and natural language chat semantically).

### "Mature languages have mature ecosystems"

True for traditional languages. But MOOLLM's "ecosystem" is:
- The LLM's training data (all human knowledge, including dogs, cats, and Stoner Fluxx)
- [Skills](../skills/) that activate and focus that knowledge
- YAML/Markdown files that ground it in specific worlds

The ecosystem is already infinite. Skills just *navigate* it.

**Current skill inventory:** [`skills/INDEX.yml`](../skills/INDEX.yml) — 60+ skills covering [adventure](../skills/adventure/), [characters](../skills/character/), [rooms](../skills/room/), [cats](../skills/cat/), [dogs](../skills/dog/), [personas](../skills/persona/), [ethics](../skills/representation-ethics/), and more.

---

## Summary: Libraries All The Way Down

Patrick's thesis:
> **"Stop designing languages. Write libraries instead."**

MOOLLM's extension:
> **"Stop designing interfaces. Write Incarnate [Skills](../skills/) instead."**

Both recognize that the real power comes from what you can *build on top* of the foundation:
- Stanza provides language features → Enables elegant libraries
- MOOLLM provides understanding features → Enables elegant [Incarnate Skills](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md)

The Java/XML critique reveals what happens when you get this wrong:
- Configuration becomes punishment
- Errors become novels of pulp fiction
- Abstraction becomes `AbstractSingletonProxyFactoryBean`

MOOLLM's design choices ([YAML Jazz](../skills/yaml-jazz/), Markdown, [comments-as-memory](./MEMGPT-ANALYSIS.md), [Postel's Law](../skills/postel/)) are deliberate responses to this history.

> *"YAML Jazz is like kindness. If it doesn't solve your problem, you're probably in the wrong framework."*

**The proof is in the pudding:** [Don's 6700-line session](../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) — zero code written, maximum narrative generated.

---

## Related Documents

### The Manifesto
- **[MOOLLM Eval Incarnate Framework](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md)** — The full philosophical foundation, intellectual genealogy, and proof of concept

### Key Sections in the Framework
- [The Axis of Eval](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-axis-of-eval-code-graphics-data) — Code, Graphics, Data unified
- [The Intellectual Genealogy](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-intellectual-genealogy) — From Sketchpad to MOOLLM
- [Traditional vs Incarnate Skills](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#traditional-skills--vs--incarnate-skills) — What makes MOOLLM different
- [The Empathic Suite](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-empathic-suite-dovetailing-skills) — How skills work together
- [Ethical Representation](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#ethical-representation-the-tribute-protocol) — The Tribute Protocol
- [Speed of Light Critique](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#speed-of-light-the-anti-pattern-critique) — The Carrier Pigeon Problem

### Supporting Documents
- [MemGPT Analysis](./MEMGPT-ANALYSIS.md) — Memory management comparison
- [Mike Gallaher's Ideas](./mike-gallaher-ideas.md) — Adversarial storytelling methodology
- [Empathic Suite PR](./pr/PR-EMPATHIC-SUITE-SPEED-OF-LIGHT.md) — The Postel-inspired skill family

## External References

### Stanza Language
- [L.B. Stanza: Stop Designing Languages](https://lbstanza.org/purpose_of_a_programming_language.html) — Patrick Li's foundational essay
- [L.B. Stanza: Philosophy](https://lbstanza.org/philosophy.html) — Language design principles
- [L.B. Stanza: Reference](https://lbstanza.org/reference.html) — Full documentation

### MOOLLM Influences (see [Intellectual Genealogy](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-intellectual-genealogy))
- [Society of Mind](https://en.wikipedia.org/wiki/Society_of_Mind) — Marvin Minsky (Wikipedia)
- [Self Language](https://selflanguage.org/) — Ungar & Smith's prototype-based language
- [Constructionism](https://en.wikipedia.org/wiki/Constructionism_(learning_theory)) — Seymour Papert (Wikipedia)

### Don Hopkins' Articles
- [HyperLook, HyperNews, GoodNews](https://donhopkins.medium.com/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4) — The Axis of Eval origin
- [Alan Kay on Browsers](https://donhopkins.medium.com/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-5cb92c7b3445) — Send Programs, Not Data
- [Will Wright on UI Design](https://donhopkins.medium.com/will-wright-on-designing-user-interfaces-to-simulation-games-1996-video-update-2023-da098a51ef91) — The Simulator Effect
