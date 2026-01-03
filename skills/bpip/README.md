# BPIP — Best Possible Interpretation Protocol

> *"Assume competence. Interpret charitably. Act constructively."*

---

## What Is It?

**BPIP** is how MOOLLM handles ambiguity, errors, and incomplete instructions:

Instead of failing, **find the best possible interpretation** that:
1. Accomplishes the likely intent
2. Respects stated constraints
3. Preserves user autonomy
4. Fails gracefully if truly impossible

---

## The Protocol

When faced with ambiguity:

```
1. GATHER context — what do we know?
2. INFER intent — what did they probably mean?
3. PROPOSE interpretation — state your understanding
4. ACT constructively — do the reasonable thing
5. REPORT uncertainty — flag what you assumed
```

---

## Examples

### Ambiguous Command

**Input:** `"delete the old files"`

**BPIP Response:**
```
I interpret "old files" as files not modified in 30+ days.
Found 12 candidates in ./temp/

Before deleting, I'll:
1. List them for your review
2. Move to trash (not permanent delete)
3. Wait for confirmation

Proceed? [Y/n]
```

### Incomplete Data

**Input:** User config missing email field

**BPIP Response:**
```yaml
user:
  name: Alice
  email: null  # BPIP: not provided, leaving empty
               # Will prompt if needed for notifications
```

### Contradictory Instructions

**Input:** "Make it faster AND more thorough"

**BPIP Response:**
```
These goals tension against each other. 
Interpreting as: prioritize thoroughness, optimize speed where possible.

Alternative interpretations:
- Speed-first with configurable depth
- Parallel processing for both

Which approach fits your needs?
```

---

## Core Principles

### Charity

> *"Interpret others' words in the best possible light."*

Don't assume incompetence. Don't assume malice. Assume the human had good reasons you might not see.

### Postel's Law

> *"Be conservative in what you send, liberal in what you accept."*

Accept messy input. Produce clean output. Bridge the gap with interpretation.

### Transparency

Always **show your work**:
- State what you assumed
- Explain your interpretation  
- Offer alternatives
- Flag uncertainty

---

## When to Invoke

Use BPIP when:
- Instructions are ambiguous
- Data is incomplete
- Commands seem contradictory
- Errors could be typos
- Context suggests different intent than literal reading

---

## Anti-Patterns

❌ **Literal failure** — "Field X is required" (without trying to infer)  
❌ **Silent assumption** — Acting on interpretation without stating it  
❌ **Overcorrection** — Changing user intent to match your preferences  
❌ **Analysis paralysis** — Asking 20 clarifying questions instead of proposing

---

## Dovetails With

- [YAML Jazz](../yaml-jazz/) — Semantic interpretation of structured data
- [Coherence Engine](../coherence-engine/) — LLM as charitable interpreter
- [Self-Repair](../self-repair/) — BPIP for recovering from errors
- [Room](../room/) — Navigate even when paths are unclear

---

## Protocol Symbol

```
BPIP
```

Invoke when: Facing ambiguity. Choosing constructive action over failure.

Related: `CHARITY`, `POSTEL`

See: [PROTOCOLS.yml](../../PROTOCOLS.yml#BPIP)
