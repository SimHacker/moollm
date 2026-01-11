---
name: sniffable-python
description: "Structure Python so LLMs can understand it in 50 lines."
license: MIT
tier: 0
allowed-tools:
  - read_file
  - write_file
related: [sister-script, skill, yaml-jazz, constructionism, play-learn-lift]
credits:
  - "MOOLLM — Dual-audience code structure"
  - "Python argparse — Built-in CLI with clean structure/implementation separation"
---

# Sniffable Python

> **"Structure code for the first 50 lines. That's all the LLM needs."**

Don't invent new syntax — **structure existing syntax** for optimal LLM comprehension.

*If your code smells good, the LLM can sniff it from the first whiff.*

*Steve Jobs wanted pixels you could lick. We want code you can sniff.*

---

## The Problem

LLMs can read Python. But:
- Large files overwhelm context
- Implementation details bury the API
- Comments scattered or missing
- No clear entry point for understanding

**Solution:** Structure Python so the first ~50 lines contain everything needed to understand and use the tool. Make your code's bouquet apparent from the opening notes.

---

## The Pattern

### Canonical Structure

```python
#!/usr/bin/env python3
"""skill-name: Brief description of what the script does.

This docstring becomes --help output AND is immediately visible to the LLM.
It should contain:
- Purpose (one sentence)
- Usage examples
- Key behaviors

Usage:
    python script.py command [options]
    
Examples:
    python script.py move north --quiet
    python script.py examine sword --verbose
"""

import argparse
from pathlib import Path
import yaml

# Configuration
DEFAULT_ROOM = "start"
VALID_DIRECTIONS = ["north", "south", "east", "west"]
MAX_INVENTORY = 10

def main():
    """Main entry point — CLI structure only, no implementation."""
    parser = argparse.ArgumentParser(
        description=__doc__.split('\n')[0],  # First line of module docstring
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # move command
    move_parser = subparsers.add_parser("move", help="Move in a direction")
    move_parser.add_argument("direction", choices=VALID_DIRECTIONS,
                             help="Direction to move")
    move_parser.add_argument("--quiet", "-q", action="store_true",
                             help="Suppress output")
    
    # examine command
    examine_parser = subparsers.add_parser("examine", help="Look at something")
    examine_parser.add_argument("target", help="What to examine")
    examine_parser.add_argument("--verbose", "-v", action="store_true",
                                help="Show details")
    
    # status command
    status_parser = subparsers.add_parser("status", help="Show game state")
    status_parser.add_argument("--verbose", "-v", action="store_true",
                               help="Show details")
    
    args = parser.parse_args()
    _dispatch(args)

# Implementation (LLM only reads past here if modifying behavior)

def _dispatch(args):
    """Route to appropriate handler."""
    if args.command == "move":
        _do_move(args.direction, args.quiet)
    elif args.command == "examine":
        _do_examine(args.target, args.verbose)
    elif args.command == "status":
        _show_status(args.verbose)

def _do_move(direction: str, quiet: bool) -> None:
    """Internal: Execute movement."""
    ...

def _do_examine(target: str, verbose: bool) -> None:
    """Internal: Examine an object."""
    ...

def _show_status(verbose: bool) -> None:
    """Internal: Display status."""
    ...

if __name__ == "__main__":
    main()
```

### The Zones

| Zone | Lines | Purpose |
|------|-------|---------|
| **Shebang + Docstring** | 1-15 | Purpose, usage, becomes `--help` |
| **Imports** | 16-22 | Dependencies visible at a glance |
| **Constants** | 23-30 | Configuration, valid values, limits |
| **CLI Structure** | 31-50 | Command tree with types and docs |
| **Implementation** | 51+ | Only read if modifying |

---

## Why This Works

### Dual-Audience Design

```
                    ┌─────────────────┐
                    │   Python File   │
                    │  (sniffable)    │
                    └────────┬────────┘
                             │
            ┌────────────────┴────────────────┐
            │                                 │
            ▼                                 ▼
    ┌───────────────┐                 ┌───────────────┐
    │    Human      │                 │     LLM       │
    │   runs:       │                 │   reads:      │
    │  --help       │                 │  first 50     │
    │               │                 │  lines        │
    └───────────────┘                 └───────────────┘
            │                                 │
            └────────────────┬────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Same source    │
                    │  of truth       │
                    └─────────────────┘
```

### DRY Principle

The CLI decorators ARE the documentation:

```python
@click.option('--verbose', '-v', is_flag=True, help='Show details')
```

This single line defines:
- The flag name (`--verbose`)
- The short form (`-v`)
- The type (boolean flag)
- The help text
- The Python parameter name and type

No duplication. No drift. One source.

---

## Why Syntax Compression Fails

Some argue for compressing syntax to save tokens — dense symbols, sigils, minimal keywords. This is the wrong optimization.

**Perl is the cautionary tale.** Its obsessive fetish for compact syntax, sigils, punctuation, and performative TMTOWTDI one-liners — to the point of looking like line noise — is exactly why it's no longer relevant for LLM comprehension and generation.

| Approach | Tokens | Comprehension | Training Data |
|----------|--------|---------------|---------------|
| Dense novel syntax | Fewer | Low (unfamiliar) | Minimal |
| Sniffable Python | More | High (known syntax) | Billions |

**The LLM already knows Python cold.** Teaching it a novel syntax costs millions of tokens per context window (docs, examples, corrections) — and that cost is paid every single prompt, because prompting is not training. LLMs have no memory. Sniffable Python costs zero tokens to teach — the LLM just reads code it understands deeply from massive pre-training.

### The Symbol Collision Problem

Short symbols cause semantic collisions. When `@` appears, it activates Python decorators, shell patterns, email addresses, and more — simultaneously. The model has to do disambiguation work that wouldn't exist with unambiguous keywords. That disambiguation costs compute and introduces error modes.

### Comprehension Fidelity > Token Count

You're not optimizing for token count. You're optimizing for **how well the LLM understands your code**.

Dense punctuation is anti-optimized for how transformers tokenize and reason. Verbose, well-structured code with semantic comments actually compresses better in the LLM's internal representations.

---

## Comments as YAML Jazz

Apply YAML-JAZZ principles to Python comments:

```python
# === CONSTANTS ===
TIMEOUT = 30        # generous — API is flaky on Mondays
MAX_RETRIES = 3     # based on observed failure patterns in prod
BATCH_SIZE = 100    # memory-safe for 8GB instances

# TODO: Add circuit breaker after next major outage
# FIXME: Rate limiting not yet implemented
# NOTE: This duplicates logic in api_client.py — consider extracting
```

These comments ARE data. The LLM reads them. Acts on them. Uses them to understand *why*, not just *what*.

---

## Comments: Substance Over Decoration

**Don't waste tokens on decorative separators:**

```python
# ❌ BAD: Decorative toilet paper
# ================================================================
# === IMPORTS ===================================================
# ================================================================
import argparse

# ✓ GOOD: Just the content
# Imports
import argparse
```

**Don't trim Christmas trees:**

```python
# ❌ BAD: ASCII art borders
#╔══════════════════════════════════════╗
#║         CONFIGURATION                ║
#╚══════════════════════════════════════╝

# ✓ GOOD: Plain and functional
# Configuration
TIMEOUT = 30  # generous — API flaky on Mondays
```

**Do include useful semantic comments:**

```python
# ✓ GOOD: Explains WHY
TIMEOUT = 30        # generous — API flaky on Mondays
MAX_RETRIES = 3     # based on observed failure patterns
BATCH_SIZE = 100    # memory-safe for 8GB instances

# ✓ GOOD: Documents intent
# TODO: Add circuit breaker after next outage
# NOTE: Duplicates logic in api_client.py — consider extracting
```

**The rule:** Every comment token should carry meaning. If it's just decoration, delete it.

---

## Argparse vs Click vs Typer

**Argparse is preferred** for sniffable Python because it separates structure from implementation:

| Feature | Argparse | Click | Typer |
|---------|----------|-------|-------|
| Structure/impl separation | ✓ Clean | ✗ Mixed | ✗ Mixed |
| Top-down tree order | ✓ | ✗ | ✗ |
| Built-in (no deps) | ✓ | ✗ | ✗ |
| Training data | Abundant | Abundant | Growing |
| LLM familiarity | Highest | High | Medium |

### The Argparse Advantage

With Click/Typer, decorators attach to functions — so CLI structure is **interleaved** with implementation:

```python
# Click: structure mixed with implementation
@cli.command()
def examine(target: str):  # ← implementation starts here
    """Look at something."""
    do_stuff()  # ← can't sniff without reading this
```

With argparse, `main()` contains the **entire CLI tree** with no implementation:

```python
# Argparse: clean separation
def main():
    """CLI structure only — no implementation."""
    parser = argparse.ArgumentParser(description="Tool description")
    subparsers = parser.add_subparsers(dest="command")
    
    # examine command
    examine_parser = subparsers.add_parser("examine", help="Look at something")
    examine_parser.add_argument("target", help="What to examine")
    examine_parser.add_argument("--verbose", "-v", action="store_true")
    
    # move command
    move_parser = subparsers.add_parser("move", help="Move in a direction")
    move_parser.add_argument("direction", choices=VALID_DIRECTIONS)
    
    args = parser.parse_args()
    _dispatch(args)  # ← implementation is ELSEWHERE

# === IMPLEMENTATION (completely separate, below the fold) ===
def _dispatch(args):
    ...
```

**The LLM reads `main()` and sees the entire command tree** — arguments, types, choices, help text — without any implementation noise. Pure sniffability. No need to hold your nose.

---

## Integration with Sister Scripts

Sniffable Python is how sister scripts should be structured:

```
skill/
├── SKILL.md           # Tells LLM how to generate scripts
├── CARD.yml           # Interface definition
└── scripts/
    └── helper.py      # Sniffable Python
```

When the skill/SKILL.md instructs the LLM to generate a sister script, it should follow sniffable-python conventions:

1. Docstring with usage at top, no decorations
2. Imports grouped and labeled
3. Constants with explanatory comments
4. CLI structure before implementation
5. Implementation below the fold

---

## The Coherence Engine Flow

```
User: "Run the room builder for the kitchen"
                    │
                    ▼
    ┌───────────────────────────────────┐
    │  LLM reads skill/SKILL.md         │
    │  Discovers: scripts/room-builder  │
    └───────────────────┬───────────────┘
                        │
                        ▼
    ┌───────────────────────────────────┐
    │  LLM sniffs room-builder.py       │
    │  Reads first 50 lines:            │
    │  - Docstring: "Creates rooms..."  │
    │  - Commands: create, modify, list │
    │  - Options: --template, --force   │
    └───────────────────┬───────────────┘
                        │
                        ▼
    ┌───────────────────────────────────┐
    │  LLM understands the API          │
    │  Generates: room-builder create   │
    │             --template kitchen    │
    └───────────────────────────────────┘
```

The LLM discovers the tool's capabilities by reading its structure, not by loading documentation. One quick sniff and it knows what's cooking.

---

## Checklist

When writing sniffable Python:

- [ ] Shebang on line 1
- [ ] Module docstring with purpose, usage, examples
- [ ] Imports grouped at top (no decorative markers)
- [ ] Constants with explanatory comments
- [ ] CLI structure in `main()` using argparse (preferred) or Click/Typer
- [ ] Each command has a docstring
- [ ] Types specified in function signatures
- [ ] Implementation below line 50
- [ ] Internal functions prefixed with `_`
- [ ] `if __name__ == "__main__":` at bottom

---

## Anti-Patterns (Code Smells You Can't Unsmell)

❌ **Implementation before CLI**
```python
def _helper():
    ...
def _another_helper():
    ...
# 200 lines later...
@click.command()
def main():
    ...
```

❌ **No docstrings**
```python
@click.command()
def process(x, y, z):
    # What does this do? What are x, y, z?
```

❌ **Magic constants**
```python
if retries > 3:  # Why 3? What happens at 4?
```

❌ **Scattered imports**
```python
import os
def foo():
    import json  # Hidden dependency
```

---

## Commands

| Command | Action |
|---------|--------|
| `SNIFF [file]` | Read and summarize a Python file's API |
| `SNIFF CODE [file]` | **Language-agnostic** review for sniffability |
| `GENERATE-SNIFFABLE [name]` | Create new sniffable script from template |
| `VALIDATE-SNIFFABLE [file]` | Check if file follows conventions |

### SNIFF CODE — Works on Any Language

The `SNIFF CODE` command isn't Python-specific. It reviews **any** source file:

```
> SNIFF CODE src/api/handler.ts

Sniffability Report for handler.ts:
✓ Purpose clear from first 10 lines
✓ Exports/API visible before implementation  
✗ Magic number on line 47 — needs comment
✗ Helper function before main export — reorder
✓ Semantic comments explain WHY not WHAT

Overall: Mostly fresh, minor reordering needed
```

**What it checks:**

| Aspect | Question |
|--------|----------|
| **Purpose** | Can you understand what this does in 10 lines? |
| **API-first** | Are exports/interfaces/main before helpers? |
| **Comments** | Do comments explain WHY, not just WHAT? |
| **No decoration** | Are comments semantic, not decorative cruft? |
| **Constants** | Do magic values have explanatory comments? |
| **Dependencies** | Are imports/requires visible at top? |

**Good for humans. Good for LLMs. Same conventions.**

---

## Protocol Symbol

```
SNIFFABLE-PYTHON
```

Invoke when: Generating or reading Python scripts that need to be LLM-comprehensible.

---

## Dovetails With

- **[sister-script/](../sister-script/)** — Scripts generated from documentation
- **[skill/](../skill/)** — The meta-skill that uses sniffable scripts
- **[yaml-jazz/](../yaml-jazz/)** — Comments as semantic data
- **[play-learn-lift/](../play-learn-lift/)** — Scripts emerge from proven procedures
- **[constructionism/](../constructionism/)** — Building inspectable things

---

## Beyond Python: Universal Sniffability

While this skill focuses on Python, **the principles are language-agnostic**:

| Language | Sniffable Structure |
|----------|---------------------|
| **TypeScript** | Exports at top, types before implementation, JSDoc on public API |
| **Go** | Package doc, exported functions first, internal helpers below |
| **Rust** | Module doc, pub items at top, private impl below |
| **Java** | Class Javadoc, public methods before private |
| **Bash** | Usage comment at top, main at top, functions below |

**The universal rule:** Whatever a reader (human or LLM) needs to *use* the code should be visible before whatever they need to *modify* it.

```typescript
// ✓ Sniffable TypeScript
/**
 * User authentication service.
 * @module auth
 */

export interface AuthConfig { ... }
export function authenticate(config: AuthConfig): Promise<User> { ... }
export function logout(): void { ... }

// Implementation details below
function validateToken(token: string): boolean { ... }
```

**Same smell test, any language:** Can you understand what this code offers by reading just the head?

---

## Lickable Pixels, Sniffable Code

When Steve Jobs unveiled Mac OS X's Aqua interface in 2000, he said:

> *"We made the buttons on the screen look so good you'll want to lick them."*

Jobs understood that interfaces aren't just functional — they should be **sensually inviting**. The translucent droplets, the pulsing default buttons, the candy-colored icons — these weren't decoration. They were signals of quality that drew users in.

**Programming languages are user interfaces.** The users are humans and LLMs. And just as lickable pixels invite visual exploration, **sniffable code invites structural exploration**.

| Lickable Pixels (UI) | Sniffable Code |
|---------------------|----------------|
| Visually inviting | Structurally inviting |
| Draws the eye to affordances | Draws the reader to the API |
| Beauty signals quality | Clarity signals quality |
| Users want to click | Readers want to use |
| First impression matters | First 50 lines matter |

Jobs didn't make Aqua pretty at the expense of function — the visual design *reinforced* usability. Sniffable code works the same way: the structural clarity that helps LLMs also helps humans. We're not optimizing for machines at human expense. We're optimizing for **comprehension**, and both benefit.

*Perl looks like line noise. Sniffable Python looks like an invitation.*

---

## The Thesis

The "ideal LLM syntax" question has the wrong framing.

You don't need new syntax. You need **structured familiar syntax**.

- Languages LLMs know (Python, TypeScript, Go, Rust...)
- Structured for sniffability (important stuff at top)
- Comments as data (YAML Jazz applied to any language)
- Single source of truth (the code IS the spec)

Dense syntax compresses the wrong thing. Sniffable code structures the right thing.

*Jobs made you want to lick the screen. We want you to sniff the source.*

---

*"The LLM doesn't need fewer tokens of unfamiliar syntax. It needs familiar syntax, structured for fast comprehension."*

*Good code doesn't just avoid bad smells — it has an aroma that draws you in from the header.*
