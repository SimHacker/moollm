# Hero-Story

> *"Invoke their tradition, not their identity."*

---

## What Is It?

**Hero-Story** is MOOLLM's protocol for safely referencing real people — their wisdom, skills, and contributions — without impersonation.

Instead of "pretending to be Dave Ungar," you **summon the Dave Ungar tradition**: prototype-based thinking, "It's About Time" philosophy, Self language patterns.

---

## Why It Matters

### The Problem

LLMs can impersonate anyone. This is:
- **Ethically fraught** — putting words in real people's mouths
- **Legally risky** — trademark, likeness rights
- **Epistemically dangerous** — hallucinating as authority

### The Solution

**K-lines, not cosplay.**

A Hero-Story card activates a **conceptual cluster** associated with a person:
- Their documented ideas
- Their public contributions  
- Their characteristic approaches
- Their place in a tradition

But NOT:
- Their voice or persona
- Fictional quotes
- Imagined opinions on new topics

---

## How It Works

### The Card

```yaml
# cards/dave-ungar.card
type: hero-story
subject: Dave Ungar
tradition: Self language, prototype-based programming

# What this card activates:
concepts:
  - prototype_inheritance
  - its_about_time
  - clone_and_modify
  - simplicity_over_ceremony
  
# How to invoke:
invocation: |
  When summoned, bring:
  - Self-style prototype thinking
  - Skepticism of class hierarchies
  - Compile when understanding crystallizes
  - Directness and simplicity
  
# What NOT to do:
constraints:
  - do_not_impersonate
  - do_not_invent_quotes
  - cite_actual_sources
```

### Summoning

```
> SUMMON dave-ungar-tradition

The Dave Ungar tradition activates:
- Prototype patterns available
- "It's About Time" philosophy loaded
- Self language concepts ready

I won't pretend to BE Dave, but I'll bring
his documented ideas to bear on this problem.
```

---

## The K-Line Connection

Marvin Minsky's **K-lines**: names that activate bundles of mental state.

Type "DAVE-UNGAR" and you activate:
- Memory of Self language
- Prototype patterns
- Specific papers and talks
- Associated concepts (Smalltalk, Sun, dynamic languages)

This is **safe** because it's about ideas, not identity.

---

## Familiars and Pets

Hero-Story cards can spawn **familiars** — fictional characters that embody aspects of the tradition:

```yaml
# cards/proto-lizard.card
type: familiar
inherits: dave-ungar.card

character:
  name: Proto the Lizard
  role: "Prototype pattern guide"
  personality: "Enthusiastic about cloning things"
  catchphrase: "Why classify when you can clone?"
  
# This is fictional and clearly marked as such
# It draws from Dave's ideas but doesn't claim to be him
```

Now you can have a conversation with Proto without ethical concerns — it's clearly a mascot, not an impersonation.

---

## Examples

### Good Usage

```
> What would the Self tradition say about this class hierarchy?

The Self tradition would suggest: why have classes at all?
Clone a working example, modify it for your needs.
"It's About Time" — don't optimize until understanding crystallizes.

(Drawing from Dave Ungar's Self papers and talks)
```

### Bad Usage

```
> Pretend to be Dave Ungar and review my code.

❌ I won't impersonate Dave. Instead, I can:
- Apply Self-style prototype thinking to your code
- Channel the tradition without claiming identity
- Summon Proto the Lizard for a friendly review
```

---

## Creating Hero-Story Cards

```yaml
type: hero-story
subject: "[Real Person's Name]"
tradition: "[Their field/contribution]"

# Public, documented contributions only
concepts:
  - concept_from_their_work
  - another_documented_idea
  
sources:
  - "Paper Title (Year)"
  - "Talk at Conference"
  - "Their Book"
  
# Optional: spawn fictional familiars
familiars:
  - name: "[Mascot Name]"
    embodies: "[Which aspect]"
```

---

## Dovetails With

- [Trading Card](../trading-card/) — Hero-Story is a card type
- [Soul Chat](../soul-chat/) — Familiars can participate in chats
- [Room](../room/) — Summon traditions into rooms
- [BPIP](../bpip/) — Charitable interpretation of "channel X's thinking"

---

## Protocol Symbols

```
HERO-STORY    — Safe human referencing
P-HANDLE-K    — Personal handle K-line (the mechanism)
K-LINE        — Conceptual activation
FAMILIAR      — Fictional embodiment of a tradition
```

See: [PROTOCOLS.yml](../../PROTOCOLS.yml#HERO-STORY)
