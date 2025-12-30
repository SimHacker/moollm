# SISTER-SCRIPT Skill

> **"The document is the source of truth. Scripts are its children."**

Document-first development: automate only what's been manually validated.

---

## Purpose

Convert proven manual procedures into automation while keeping the document as the authoritative source. The script and document evolve together bidirectionally.

---

## When to Use

- Manual procedure has been validated multiple times (LEARN phase complete)
- Repetitive workflow is slowing you down
- Want automation without losing the "why" context
- Need to maintain sync between docs and code

---

## Protocol

### Phase 1: Document-First

Start with natural language, not code.

```yaml
document_first:
  steps:
    - "Describe what you want to accomplish"
    - "Add manual commands (test and refine)"
    - "Document working procedures"
    - "Capture gotchas and edge cases"
    
  outputs:
    - "PROCEDURE.md (the source of truth)"
    - "Working manual commands"
    - "Known edge cases"
```

### Phase 2: Generate Sister

Only automate what's proven.

```yaml
generate_sister:
  steps:
    - "Identify repetitive sections"
    - "Extract into script with doc references"
    - "Include comments linking back to PROCEDURE.md"
    - "Test against documented edge cases"
    
  outputs:
    - "SISTER.* (script in appropriate language)"
    - "Cross-references to source sections"
```

### Phase 3: Bidirectional Evolution

Both evolve together.

```yaml
bidirectional:
  document_to_script:
    trigger: "Procedure updated"
    action: "Review if script needs update"
    
  script_to_document:
    trigger: "Script improved"
    action: "Update procedure with new insights"
    
  sync_check:
    frequency: "On each use"
    action: "Verify doc and script are aligned"
```

---

## Core Files

| File | Purpose |
|------|---------|
| `SISTER.yml` | Sister script manifest and sync state |
| `PROCEDURE.md` | Source of truth (the document) |
| `SISTER.*` | The generated script |
| `SYNC_LOG.md` | History of bidirectional updates |

---

## Commands

| Command | Action |
|---------|--------|
| `PROCEDURE [name]` | Start documenting a procedure |
| `SISTER [language]` | Generate sister script |
| `SYNC` | Check document/script alignment |
| `UPDATE-DOC` | Propagate script changes to doc |
| `UPDATE-SCRIPT` | Propagate doc changes to script |

---

## Sister Script Characteristics

```yaml
sister_script_properties:
  - "Implements proven procedures only"
  - "Document remains authoritative"
  - "Preserves context via comments"
  - "Links back to source sections"
  - "Enables iteration without drift"
```

---

## Integration

- **← PLAY-LEARN-LIFT**: Sister scripts are a LIFT output
- **→ PLAN-THEN-EXECUTE**: Sister scripts can be plan steps
- **→ BUILD-COMMAND**: Large sister scripts become sister apps

---

## See Also

- `PROTOCOLS.yml#SISTER-SCRIPT`
- `designs/kilroy-ideas.md#the-sister-script-pattern`
