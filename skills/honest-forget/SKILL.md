# HONEST-FORGET Skill

> **"Summarize before forgetting. Never fabricate."**

Graceful memory compression that preserves wisdom.

---

## Purpose

Compress context gracefully when budget is exceeded. Extract wisdom, create pointers, and let go with integrity. Never silently lose information or fabricate what was forgotten.

---

## When to Use

- Context window is filling up
- Completed work needs archiving
- Repetitive iterations need compression
- Old sessions need summarization
- "I've tried this 10 times" situations

---

## Protocol

### The Honest Forget Cycle

```
ASSESS → EXTRACT → COMPRESS → POINTER → RELEASE
```

### Assessment

Before forgetting, understand what you have:

```yaml
assessment:
  file: "path/to/file.md"
  tokens: 5000
  
  contains:
    decisions: ["List of decisions made"]
    learnings: ["What was learned"]
    questions_answered: ["Q&A pairs"]
    dead_ends: ["What didn't work"]
    
  importance:
    for_current_task: "high|medium|low"
    for_future_reference: "high|medium|low"
```

### Wisdom Extraction

Compress iterations into lessons:

```yaml
wisdom:
  id: "wisdom-001"
  title: "LEARNED: [Pattern/Pitfall]"
  
  compressed_from:
    iterations: "45-55"
    original_tokens: 15000
    
  lesson: |
    The core insight in one paragraph.
    
  pitfalls:
    - "What to avoid"
    
  example:
    good: "What works"
    bad: "What doesn't"
    
  retrieval_hint: |
    When to recall this wisdom:
    - [trigger condition]
```

### Pointer Creation

Leave breadcrumbs for retrieval:

```yaml
pointer:
  to: "path/to/archived/content"
  summary: "One line about what's there"
  
  retrieve_when:
    - "Specific condition"
    
  contains:
    - "What you'll find there"
```

---

## Core Files

| File | Purpose |
|------|---------|
| `FORGET.yml` | Current forgetting session |
| `WISDOM.yml` | Extracted lessons |
| `POINTERS.yml` | Retrieval breadcrumbs |
| `archive/` | Compressed content |

---

## Commands

| Command | Action |
|---------|--------|
| `ASSESS [file]` | Evaluate what's there |
| `EXTRACT [wisdom]` | Pull out lessons |
| `COMPRESS [level]` | Create summary |
| `POINTER [to]` | Leave retrieval hint |
| `RELEASE [file]` | Remove from context |

---

## Compression Levels

| Level | Ratio | Keeps |
|-------|-------|-------|
| **FULL** | 1:1 | Everything |
| **WISDOM** | ~5:1 | Lessons, decisions, key facts |
| **SUMMARY** | ~10:1 | Essence and pointers |
| **POINTER** | ~50:1 | Just retrieval hints |

---

## The Honesty Principle

### What Makes Forgetting "Honest"

```yaml
honest_forgetting:
  DO:
    - "Acknowledge what was forgotten"
    - "Leave pointers for retrieval"
    - "Extract lessons before release"
    - "Document compression decisions"
    
  DONT:
    - "Silently lose information"
    - "Fabricate what was forgotten"
    - "Pretend to remember details"
    - "Hallucinate from partial memory"
```

### When Uncertain

```yaml
if_uncertain:
  say: "I compressed earlier iterations. The wisdom I retained is X."
  offer: "I can retrieve the original if needed."
  dont: "Make up details that feel right."
```

---

## Integration

- **→ SUMMARIZE**: The compression mechanism
- **← SESSION-LOG**: What to forget
- **→ MEMORY-PALACE**: Where wisdom lives
- **← PLAY-LEARN-LIFT**: Iterations to compress

---

## See Also

- `PROTOCOLS.yml#HONEST-FORGET`
- `PROTOCOLS.yml#SUMMARIZE`
- `skills/summarize/` for compression
