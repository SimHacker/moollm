# 👃🐍 Sniffable Python

> Structure Python scripts so the first 50-100 lines describe the entire API.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [sister-script/](../sister-script/) | Sniffable Python IS the sister-script format |
| [play-learn-lift/](../play-learn-lift/) | LIFT produces sniffable automation |
| [yaml-jazz/](../yaml-jazz/) | Comments carry meaning (applied to Python) |
| [plain-text/](../plain-text/) | Scripts are first-class objects |
| [skill/](../skill/) | Meta-skill that explains how skills work |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Interface Card](CARD.yml) — machine-readable methods
- [Starter Template](TEMPLATE.py.tmpl) — copy and modify

---

## The Idea

An LLM reads the head of a Python file to understand the entire script. Like a human running `script.py --help`, except it reads the source instead of executing it.

The LLM already knows Python from billions of lines of training data. Zero tokens to teach it the language. Novel syntax requires stuffing the manual into every prompt. Python requires nothing.

The optimization isn't fewer tokens through unfamiliar syntax. It's familiar syntax, structured for fast comprehension.

---

## The Rules

1. **Docstring at top of file**: all commands, arguments, gotchas, reference syntax
2. **Use `argparse` with `add_subparsers`**: the entire CLI lives in `main()` as one contiguous block. Not `click`/`typer`/`fire` which scatter argument definitions across decorated functions. An LLM can't sniff a `click` app without reading every decorated function in the file.
3. **Constants and path definitions** immediately after imports
4. **`main()` defines the CLI**, `set_defaults(func=cmd_xxx)` routes to handlers
5. **Everything below `main()` is implementation** — underground, only dig when the head tells you where to look

Same principle as the Semantic Image Pyramid applied within a single file. GLANCE→CARD→SKILL→README is progressive disclosure across files. Sniffable-python is progressive disclosure within a file. The head sticks above ground. The body is below.

---

## The Pattern

```python
#!/usr/bin/env python3
"""adventure-lint: Validate adventure world consistency.

Scans adventure directories for ROOM.yml, objects, and characters.
Reports errors, warnings, and suggestions.

Usage:
    python adventure-lint.py lint examples/adventure-4/
    python adventure-lint.py check pub/ROOM.yml
"""

import argparse
from pathlib import Path
import yaml

REQUIRED_FIELDS = ["name", "description", "exits"]  # rooms need these
MAX_EXIT_DEPTH = 10  # prevent infinite loops

def main():
    """CLI structure — sniff this to understand the tool."""
    parser = argparse.ArgumentParser(
        description=__doc__.split('\n')[0],
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # lint command
    lint_parser = subparsers.add_parser("lint", help="Lint entire adventure")
    lint_parser.add_argument("adventure_path", type=Path)
    lint_parser.add_argument("--output", "-o", type=Path, default="LINTER.yml")
    lint_parser.add_argument("--fix", action="store_true", help="Auto-fix issues")
    
    # check command
    check_parser = subparsers.add_parser("check", help="Check single file")
    check_parser.add_argument("file", type=Path)
    
    args = parser.parse_args()
    _dispatch(args)

# Implementation below — the LLM doesn't need to read past here
```

The LLM reads `main()` and knows everything: two commands (`lint` and `check`), `lint` takes a path and can auto-fix, `check` validates a single file. One read. Full comprehension. No spelunking through 500 lines of implementation.

---

## Canonical Example

`cursor-mirror/scripts/cursor_mirror.py` — 9,800 lines, 59 commands.

| Section | Lines | What's There |
|---------|-------|-------------|
| Docstring | 1-160 | All 59 commands, reference syntax, gotchas, data locations |
| Imports + constants | 160-178 | Path constants, database schema comments |
| `main()` with argparse | 183-260 | Every command defined in one block |
| Handler implementations | 260+ | Underground — 9,500 lines of implementation |

An LLM reads lines 1-260 and knows the complete interface without reading the other 9,500 lines.

---

## Inline Comments as Data

YAML Jazz applies to Python too. Inline comments next to constants are data for the LLM:

```python
TIMEOUT = 30  # generous — API flaky on Mondays
MAX_BATCH = 5  # more than 5 overflows context window
```

These aren't just documentation for humans. They're context the model reads and acts on.

---

## The Feedback Loop

Sniffable scripts enable a generate-validate-fix cycle:

1. LLM sniffs the script header, understands the CLI
2. LLM invokes the tool
3. Tool outputs structured results (YAML, JSON)
4. LLM reads output, fixes issues
5. Repeat

This is how adventure-4 grew 36 rooms and 37 objects — the LLM generated content, ran the linter, read the output, fixed errors, and iterated.

---

## See Also

- [SKILL.md](./SKILL.md) — Full specification
- [CARD.yml](./CARD.yml) — Machine-readable interface
- [TEMPLATE.py.tmpl](./TEMPLATE.py.tmpl) — Starter template
- [sister-script/](../sister-script/) — Document-first development
- [cursor-mirror/scripts/cursor_mirror.py](../cursor-mirror/scripts/cursor_mirror.py) — Canonical example
