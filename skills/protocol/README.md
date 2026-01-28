# Protocol — K-lines & Semantic Activation

> **"The name activates the tradition."**

## What It Is

A **protocol** in MOOLLM is a K-line — a name that activates an entire constellation of knowledge and behavior. This is Marvin Minsky's insight from *Society of Mind* (1986).

When you invoke a protocol by name, you're not just referencing documentation — you're **activating** a pattern of understanding.

## Why It Matters

### Massive Compression

A single protocol name can compress ~5000 tokens of context:

```yaml
# Instead of explaining all of this:
- "YAML files should be flexible"
- "Use natural keys instead of cryptic ones"
- "Comments carry semantic meaning"
- "Structure should be improvisational"
- [... 50 more guidelines ...]

# Just say:
> Apply YAML-JAZZ

# The LLM already knows the pattern. The name activates it.
```

### The LLM Already Knows

Most protocols reference patterns the LLM has seen before:
- **POSTEL** → Robustness principle
- **YAML-JAZZ** → Flexible YAML with semantic comments
- **INCARNATION** → Character creation ritual

We're not teaching — we're **activating** pre-existing knowledge.

## K-REF: File Pointers with Metadata

When tools need to point to files, use K-REF format:

```
PATH[:LINE[-END]][#anchor][?search] # TYPE - DESC
```

**Examples:**
```
/path/file.txt:42 # secret 🔴
/path/screenshot.png # image - Cursor can read!
/path/schema.yml#field.name # k-line
```

**Key insight:** Cursor can read image files from absolute paths!

## SISTER-SCRIPT Pattern

Tools emit K-REFs, LLM reads selectively:

1. Tool runs (Python, shell, etc.)
2. Emits list of K-REFs with metadata
3. LLM scans the list
4. Reads only what's needed

This is **scan and point, not dump**.

## Core Protocols

| Protocol | Activates |
|----------|-----------|
| `ADVENTURE` | Text adventure patterns |
| `YAML-JAZZ` | Flexible semantic YAML |
| `BOOTSTRAP` | Session startup sequence |
| `PSIBER` | Data as navigable room |
| `POSTEL` | Liberal/conservative robustness |
| `INCARNATION` | Character creation ritual |
| `SPEED-OF-LIGHT` | Multi-turn in single call |

## Minsky's Insight

> "A K-line is a wirelike structure that attaches itself to whichever mental agents are active when you solve a problem. When activated later, those agents are partially activated, creating a similar mental state."
> — Marvin Minsky, *Society of Mind* (1986)

MOOLLM protocols ARE K-lines. The name IS the activation.

## Commands

| Command | Action |
|---------|--------|
| `INVOKE [name]` | Activate protocol |
| `DEFINE [name]` | Create new protocol |
| `LIST PROTOCOLS` | Show available |
| `K-REF [path]` | Emit file pointer |

## See Also

- [../k-lines/](../k-lines/) — Naming conventions
- [../naming/](../naming/) — File naming patterns
- [../skill/](../skill/) — Skills are invokable protocols
- [../bootstrap/](../bootstrap/) — Session startup protocol

---

*"Speak the name. Become the pattern."*
