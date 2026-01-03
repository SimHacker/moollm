# DEBUGGING Skill

> **"Hypothesize, test, learn, repeat."**

Systematic bug investigation with hypothesis tracking.

---

## Purpose

Debug problems methodically. Track hypotheses, document tests, record what you learn, and converge on root causes.

---

## When to Use

- Something isn't working as expected
- Mysterious behavior needs explanation
- Performance problems need diagnosis
- "Works on my machine" situations

---

## Protocol

### Debugging Loop

```
OBSERVE → HYPOTHESIZE → TEST → LEARN → (repeat or) → FIX
```

### Observation Phase

Before guessing, gather facts:

```yaml
observation:
  symptom: "What's the observable problem?"
  context: "When does it happen?"
  expected: "What should happen instead?"
  
  evidence:
    - "Error message (exact text)"
    - "Logs showing the issue"
    - "Steps to reproduce"
    
  constraints:
    - "What we know for sure"
    - "What we've already ruled out"
```

### Hypothesis Tracking

```yaml
hypothesis:
  id: "hyp-001"
  claim: "The bug is caused by X"
  confidence: "high|medium|low"
  
  if_true:
    - "We would expect to see..."
    - "Changing X should fix it"
    
  test:
    action: "What to try"
    expected: "What we expect if hypothesis is correct"
    
  result:
    status: "confirmed|refuted|inconclusive"
    observation: "What actually happened"
    learned: "What this tells us"
```

### Test Documentation

```yaml
test:
  id: "test-001"
  hypothesis: "hyp-001"
  action: "What we did"
  
  before:
    state: "System state before test"
    
  after:
    state: "System state after test"
    
  result: "confirmed|refuted|inconclusive"
  learned: "What we now know"
```

---

## Core Files

| File | Purpose |
|------|---------|
| `DEBUG.yml` | Current debugging session |
| `HYPOTHESES.md` | All hypotheses and their status |
| `TESTS.md` | Test log |
| `ROOT_CAUSE.md` | Final analysis |

---

## Commands

| Command | Action |
|---------|--------|
| `DEBUG [symptom]` | Start debugging session |
| `OBSERVE [fact]` | Record observation |
| `HYPOTHESIZE [claim]` | Propose hypothesis |
| `TEST [action]` | Document test |
| `LEARN [insight]` | Record what you learned |
| `ROOT-CAUSE [explanation]` | Document root cause |

---

## The Scientific Method for Bugs

1. **Observe**: What exactly is happening?
2. **Question**: Why might this be happening?
3. **Hypothesize**: Form testable explanation
4. **Predict**: What would we see if hypothesis is true?
5. **Test**: Try to confirm or refute
6. **Analyze**: What did we learn?
7. **Iterate**: New hypothesis or fix

---

## Common Patterns

### Binary Search Debugging

```yaml
technique: "binary_search"
description: "Narrow down where the bug lives"
steps:
  - "Find a known good state"
  - "Find a known bad state"
  - "Check the middle"
  - "Repeat until found"
```

### Rubber Duck Debugging

```yaml
technique: "rubber_duck"
description: "Explain the problem out loud"
implementation: "Write detailed observation in DEBUG.yml"
why_it_works: "Forces you to articulate assumptions"
```

---

## Integration

- **← PLAY-LEARN-LIFT**: Debugging IS learning
- **→ SESSION-LOG**: Log all debugging activities
- **→ RESEARCH-NOTEBOOK**: Complex bugs need research
- **→ HONEST-FORGET**: Compress debugging wisdom

---

## Dovetails With

- **[../adventure/](../adventure/)** — Debugging IS adventure + hypothesis tracking
- **[../play-learn-lift/](../play-learn-lift/)** — Debugging IS PLAY stage
- **[../session-log/](../session-log/)** — Track all debug steps
- **[../research-notebook/](../research-notebook/)** — Investigation notes
- **[../room/](../room/)** — Debug sessions are rooms
- **[../trading-card/](../trading-card/)** — Git Goblin 🧌, Index Owl 🦉 companions
