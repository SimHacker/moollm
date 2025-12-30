# SUMMARIZE Skill

> **"Compress without losing meaning."**

Context management through intelligent summarization.

---

## Purpose

Compress files and knowledge while preserving essential meaning. Manage context window by creating summaries that can substitute for full content.

---

## When to Use

- Context budget is running low
- File is too large to include in working set
- Need to preserve essence of completed work
- Creating reference material from detailed docs

---

## Protocol

### Summarization Levels

```yaml
levels:
  FULL:
    compression: "1:1"
    use: "Active work, needs all detail"
    
  WORKING:
    compression: "~3:1"
    use: "Recent context, key points preserved"
    
  REFERENCE:
    compression: "~10:1"
    use: "Background knowledge, essence only"
    
  POINTER:
    compression: "~50:1"
    use: "Just enough to know it exists and where"
```

### Summary Structure

Every summary includes:

```yaml
summary_structure:
  header:
    - source_file: "path/to/original.md"
    - summarized_at: "timestamp"
    - compression_level: "WORKING|REFERENCE|POINTER"
    - token_reduction: "from X to Y"
    
  essence:
    - "Core insight or purpose"
    - "Key decisions made"
    - "Important conclusions"
    
  pointers:
    - "Section X: [one-line summary]"
    - "Section Y: [one-line summary]"
    
  retrieval_hints:
    - "Read full file if you need: [specific info]"
```

---

## Core Files

| File | Purpose |
|------|---------|
| `SUMMARIES.yml` | Index of all summaries |
| `summaries/` | Directory of summary files |

---

## Commands

| Command | Action |
|---------|--------|
| `SUMMARIZE [file] [level]` | Create summary at level |
| `COMPRESS [directory]` | Bulk summarize for context |
| `EXPAND [summary]` | Signal need to read full file |
| `GC` | Garbage collect stale summaries |

---

## Summary Types

### ESSENCE Summary
For completed work:
```markdown
# Summary: [original file]
**Essence**: [one paragraph capturing the core]
**Key Points**: [bullet list]
**If you need more**: [what to look for in original]
```

### DECISIONS Summary
For files with choices made:
```markdown
# Decisions: [original file]
**Decided**: [what was decided]
**Alternatives Considered**: [brief list]
**Rationale**: [why this choice]
```

### WISDOM Summary (HONEST-FORGET pattern)
For lessons learned:
```markdown
# Learned: [topic]
**Compressed from**: [source iterations]
**Core lesson**: [the wisdom]
**Pitfalls**: [what to avoid]
```

---

## Integration

- **← PLAY-LEARN-LIFT**: Summarize PLAY_LOG for LEARN phase
- **→ MEMORY-PALACE**: Summaries become room descriptions
- **→ HOT-COLD**: Summaries go to cold.yml, pointers to hot.yml
- **← SESSION-LOG**: Summarize completed sessions

---

## See Also

- `PROTOCOLS.yml#SUMMARIZE`
- `PROTOCOLS.yml#HONEST-FORGET`
- `kernel/memory-management-protocol.md`
