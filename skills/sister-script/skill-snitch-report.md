# Skill Snitch Report: sister-script

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE CODE IS THE DOCUMENTATION

---

## Executive Summary

**Document-first automation — the script IS the documentation.**

Structure Python scripts so the TOP tells you everything. The BOTTOM has implementation.

Single source of truth. Works for humans AND LLMs.

---

## The Canonical Order

| Section | What It Contains | Who Benefits |
|---------|------------------|--------------|
| 1. Imports | Dependencies | LLM knows what's available |
| 2. Globals/Enums | State shape | LLM knows the data model |
| 3. CLI Definition | Full API with help text | Users AND LLMs |
| 4. Implementation | How it works | Read only if needed |

---

## The Key Insight

```python
# CLI DEFINITION — This IS the API documentation

def create_parser():
    parser = argparse.ArgumentParser(
        description="MOOLLM Sister Script CLI"
    )
    
    # LOOK command
    look_parser = subparsers.add_parser(
        "look",
        help="Describe the current room"
    )
```

**The argparse definition IS the documentation.**

Users run: `cli.py --help`
LLMs read: First ~100 lines

---

## Methods

| Method | Purpose |
|--------|---------|
| **DOCUMENT** | Write procedure as documentation |
| **FOLLOW** | Execute documented procedure |
| **EXTRACT** | Convert to Python CLI |
| **SYNC** | Keep doc and script aligned |
| **UNDERSTAND** | LLM reads script top |
| **ENHANCE** | Add new command |

---

## Benefits

### For Humans
- `cli.py --help` shows all commands
- Standard CLI conventions
- Self-documenting

### For LLMs
- Read top of file → know everything
- Imports → dependencies
- Globals → state shape
- CLI definition → full API with types

### For Both
- Single source of truth (no doc drift)
- DRY — help text IS documentation
- Changes auto-update --help

---

## CLI Module Choice

| Module | Pros | Cons | When |
|--------|------|------|------|
| **argparse** | stdlib, no deps | verbose | Simple CLIs |
| **click** | decorator syntax, pretty | dependency | Complex CLIs |
| **typer** | type hints as API | less explicit | Rapid dev |

---

## The Methodology

```
1. Write procedure as PROCEDURE.md
2. LLM follows it (PLAY/LEARN)
3. Refine until stable
4. Extract to Python CLI (LIFT)
5. Script IS the doc
```

---

## Security Assessment

### Concerns

1. **Code execution** — scripts run commands
2. **Sync drift** — doc and script diverge
3. **Over-automation** — premature LIFT

### Mitigations

- Structure prevents hidden behavior
- Single source of truth
- LIFT only when stable

**Risk Level:** LOW — transparent by design

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Don Hopkins** | Documentation-first automation |
| **Donald Knuth** | Literate programming |
| **argparse** | Python stdlib |
| **click** | Pallets Projects |

---

## Verdict

**SINGLE SOURCE OF TRUTH. APPROVE.**

The code IS the documentation. Structure it so the top tells you everything.

No doc drift. No redundancy. Works for humans AND LLMs.
