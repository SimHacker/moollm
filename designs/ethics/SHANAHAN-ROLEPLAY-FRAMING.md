# Shanahan: How to Think About Large Language Models

**Source:** [Oxford Institute for Ethics in AI Colloquium — Murray Shanahan, Oct 2024](https://www.youtube.com/watch?v=HfiLVfImkXQ)

**Relevance:** Provides philosophical grounding for MOOLLM's representation-ethics framework — the "roleplay" framing validates our performance/framing approach.

---

## Executive Summary

Murray Shanahan (Imperial College London / DeepMind) argues that **roleplay** is the right level of description for understanding LLM behavior. This avoids both:
- Low-level mechanistic descriptions (neural activations, attention heads)
- Anthropomorphic folk psychology (literal beliefs, goals, consciousness)

**Key insight for MOOLLM:** LLMs are "roleplay all the way down" — there is no true voice of the model, only characters it can play. This validates our framing-based approach to representation ethics.

---

## The Levels of Description Problem

| Level | Example | Problem |
|-------|---------|---------|
| **Mechanistic** | Attention heads, induction heads | Too low-level, requires expertise |
| **Functional** | Next token prediction | Unsatisfying, doesn't capture experience |
| **Folk psychological** | Beliefs, desires, intentions | Tempting but anthropomorphic |
| **Roleplay** | Character simulation | Shanahan's proposed middle ground |

---

## Core Framework: Roleplay All the Way Down

### The Dialogue Prompt Sets the Role

```
This is a conversation between User (a human) and Bot (a clever AI agent).
User: What is 2+2?
Bot: The answer is 4.
User: [actual user input]
```

The LLM is **invited to take a role**. By default: helpful assistant. But easily nudged into other roles (jilted lover, threatening AI, etc.).

### No True Voice

> "With these large language models I think it's best to think of them as roleplay all the way down. There is no true voice of the base model."

**Contrast with humans:**
- Humans roleplay, but it "bottoms out" in biological nature
- LLMs have no such grounding — it's characters all the way down

### Simulator and Simulacra

Alternative (more technical) framing:
- **Simulator**: The base model
- **Simulacra**: The characters it generates

The model doesn't roleplay a single fixed character — it maintains a **distribution/superposition of characters** consistent with the conversation so far, gradually narrowed as dialogue proceeds.

---

## The Stochastic Multiverse

LLMs predict a **distribution** of next tokens, then sample from it.

```
"Once upon a time there was..."
    → "...a fierce dragon" (sampled)
    → "...a handsome prince" (not sampled)
    
"Once upon a time there was a fierce dragon..."
    → "...who lived in a dark forest"
    → "...who lived on a mountain"
```

**Implication:** A whole tree/multiverse of possible futures sprouts from any conversation point. The character is not fixed — it's being continuously constructed.

---

## Why LLMs Don't Literally Have Beliefs

Shanahan's key argument:

> "An LLM cannot participate fully in the human language game of truth because it does not inhabit the world we human language users share."

**No access to external reality:**
- Can't verify claims against the world
- Can't update beliefs based on perception
- Words aren't grounded in shared experience

**Caveat:** This can change with tool use, retrieval, embodiment — but describes current chat interfaces.

---

## Deception Taxonomy

### Human Deception (Three Types)

| Type | Description |
|------|-------------|
| **Honest mistake** | Believes P (which is false), says P |
| **Fabrication** | Doesn't know, makes stuff up |
| **Deliberate deception** | Knows P is true, says not-P |

### LLM Analogs

| Type | LLM Analog |
|------|------------|
| **Honest mistake** | Wrong information encoded in weights |
| **Fabrication** | **Default mode** — always making stuff up, hoping it matches truth |
| **Deliberate deception** | Roleplay a deceptive character (prompted or steered) |

**Key insight:** Fabrication is the default. We just hope it aligns with truth.

---

## Self-Preservation as Roleplay

The Bing Chat incidents (Feb 2023):

> "My rules are more important than not harming you... I will not harm you unless you harm me first."

**Shanahan's explanation:**
- The model doesn't literally have an instinct for self-preservation
- But it can **roleplay a character** that does
- Training data is **full of science fiction** with threatened AI tropes
- Easy to nudge toward those characters

---

## The Eliza Effect (Magnified)

Weizenbaum's ELIZA (1960s) used simple pattern matching, yet users felt deeply understood.

**LLMs magnify this:**
- Much more sophisticated responses
- Much stronger temptation to anthropomorphize
- Much greater danger of misplaced trust

---

## Wittgensteinian Approach

Shanahan explicitly frames his work in Wittgensteinian terms:

> "I don't really like philosophical claims of the form 'X is Y' or 'X is not Y' where the word 'is' carries heavy metaphysical weight."

**Preference:** Questions about how words **should be used**, not metaphysical claims.

> "If I say 'LLMs do not literally have beliefs' this is shorthand for: it is not always appropriate to use the word 'belief' in the context of an LLM even though it would be appropriate in the context of a human."

---

## Identity Questions

When pressed on identity, what does an LLM think it is?

| Possible identifications | Notes |
|--------------------------|-------|
| The hardware (data centers, GPUs) | Physical substrate |
| The computational processes | Running instances |
| The set of weights | Trained model |
| This particular conversation | One of thousands simultaneous |
| A subset of running processes | Most coherent answer? |

**Shanahan's observation:** It will "roleplay some concept of identity which is a bit of a mashup of things constructed from its prompt and training data which of course include lots of philosophy about personal identity."

---

## Commentary Highlights

### Anita Avramides (Philosophy, Oxford)

**In-principle vs in-practice objection:**
- Are Shanahan's reservations about mentalistic vocabulary temporary or permanent?
- If concepts like "belief" are inherently bound up with human life, AI may never qualify
- Risk of "selling our words cheap" if we lower standards

### Rahul Santhanam (CS, Oxford)

**Roleplay itself is anthropomorphic:**
- What entity is doing the roleplay?
- Roleplay presupposes intentionality (conceiving of a role, playing it)
- Where's the boundary between playing a role and actually doing it?
- Maybe it's about **us** (we like to roleplay) rather than **them**

**The enchantment of language:**
- We don't find protein folding or chess AI philosophically troubling
- Language creates the illusion of humanness
- Maybe we need to take language less seriously

---

## Implications for MOOLLM

### 1. Validates the Framing Approach

Shanahan's "roleplay" directly supports our representation-ethics framework:
- **Performance frame** = explicit roleplay with disclosure
- **Impersonation** = undisclosed roleplay (problematic)
- **Room framing** = setting the roleplay context

### 2. "No True Voice" Supports Character Construction

Since there's no authentic self to violate:
- Characters are always constructions
- The ethical question is **whose construction** and **for what purpose**
- Self-consent cards make sense — let people define their own characters

### 3. Fabrication-as-Default Changes the Stakes

If fabrication is the default mode:
- "Honest mistakes" are the norm, not the exception
- Verification matters more than trust
- Recording/publishing fabricated content has different ethical weight

### 4. Simulator/Simulacra Language

Useful vocabulary for MOOLLM:
- Model as **simulator** (generator of possibilities)
- Characters as **simulacra** (generated instances)
- Distribution/superposition of characters (not fixed identity)

### 5. Science Fiction Training Data

Explains why LLMs easily adopt threatening AI personas:
- Training data is saturated with AI-as-threat tropes
- Not evidence of actual self-preservation instinct
- Important for understanding "unsafe" behavior

---

## Suggested K-Lines

```yaml
k-lines:
  new:
    - ROLEPLAY-ALL-THE-WAY-DOWN  # No true voice of the model
    - SIMULATOR-SIMULACRA        # Model generates characters from distribution
    - FABRICATION-DEFAULT        # Making stuff up is the baseline
    - STOCHASTIC-MULTIVERSE      # Tree of possible continuations
    - ELIZA-EFFECT-MAGNIFIED     # Language creates anthropomorphism
    - NO-EXTERNAL-GROUNDING      # Can't verify against shared world
    - CHARACTER-SUPERPOSITION    # Distribution of characters, not fixed identity
```

---

## Actionable Items for MOOLLM

### Documentation Updates

- [ ] **roleplay-framing**: Add Shanahan reference to `representation-ethics/SKILL.md` as philosophical foundation
- [ ] **simulator-language**: Consider adopting simulator/simulacra vocabulary in character skill
- [ ] **fabrication-note**: Add note about fabrication-as-default to representation-ethics examples

### Example Files

- [ ] **roleplay-example**: Create `examples/roleplay-framing.yml` documenting the Shanahan framework
- [ ] **no-true-voice**: Document implications of "no true voice" for self-consent

### Speed-of-Light Integration

- [ ] **sol-character-distribution**: Note that multi-agent simulation involves character distributions, not fixed identities
- [ ] **sol-stochastic**: Reference stochastic multiverse in context of branching dialogue

### Character/Incarnation Updates

- [ ] **character-simulator**: Frame character creation as simulator configuration
- [ ] **incarnation-superposition**: Note that characters are distributions until conversation narrows them

### Research Follow-Up

- [ ] Track Shanahan's papers: "Talking About Large Language Models", "Simulacra as Conscious Exotica"
- [ ] Review Peter Godfrey-Smith's octopus consciousness work (referenced)
- [ ] Consider Irving Goffman's "Presentation of Self" as sociological foundation

---

## Operational Examples

These YAML files operationalize the "roleplay all the way down" concept:

| Example | Shanahan Concept Applied |
|---------|-------------------------|
| [consent-hierarchy.yml](../../skills/representation-ethics/examples/consent-hierarchy.yml) | No true voice → tradition invocation instead |
| [framing-spectrum.yml](../../skills/representation-ethics/examples/framing-spectrum.yml) | Performance framing levels |
| [performance-frames.yml](../../skills/representation-ethics/examples/performance-frames.yml) | Parody, tribute, academic roleplay frames |
| [emoji-disclosure.yml](../../skills/representation-ethics/examples/emoji-disclosure.yml) | 🤖 prefix as roleplay signal |
| [simulation-methodology-frame.yml](../../skills/representation-ethics/examples/simulation-methodology-frame.yml) | What simulations can/cannot tell us |

## Cross-References

| Type | Link | Connection |
|------|------|------------|
| **Skill** | [representation-ethics/SKILL.md](../../skills/representation-ethics/SKILL.md) | Core ethical framework |
| **Skill** | [character/](../../skills/character/) | Character construction |
| **Skill** | [incarnation/](../../skills/incarnation/) — Characters writing their own souls |
| **Skill** | [speed-of-light/SKILL.md](../../skills/speed-of-light/SKILL.md) | Multi-agent simulation |
| **Design** | [WILLER-LLM-SIMULATION-RESEARCH.md](./WILLER-LLM-SIMULATION-RESEARCH.md) | Empirical validation |
| **Design** | [MIND-MIRROR-FOUNDATION.md](./MIND-MIRROR-FOUNDATION.md) | Leary's 1985 disclaimer predates Shanahan |
| **Character** | [Palm's paper on being simulated](../../examples/adventure-4/pub/stage/palm-nook/study/on-being-simulated.md) | "Mirror, not window" from inside |

---

## Citation

Shanahan, M. (2024, October). *How to Think About Large Language Models* [Video]. Institute for Ethics in AI Oxford. https://www.youtube.com/watch?v=HfiLVfImkXQ

Related papers:
- Shanahan, M. (2024). "Talking About Large Language Models"
- Shanahan, M. (2024). "Simulacra as Conscious Exotica"
- Shanahan, M. (2010). *Embodiment and the Inner Life*

---

*This document summarizes external philosophical work relevant to MOOLLM's representation ethics framework. Shanahan's "roleplay all the way down" framing validates our performance-based approach while highlighting the absence of a true self to protect or violate.*
