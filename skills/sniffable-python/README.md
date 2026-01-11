# Sniffable Python

> **"Structure code for the first 50 lines. That's all the LLM needs."**

*If your code smells good, the LLM can sniff it from the first whiff.*

Steve Jobs wanted pixels so beautiful you'd want to lick them. We want code so clear you can sniff its purpose from the header.

Python scripts structured so both humans and LLMs can understand them by reading just the header. But the principle applies to **any language** — good code has an aroma that draws you in from the opening lines. Programming languages are user interfaces. The users are humans and LLMs. Lickable pixels invite visual exploration; sniffable code invites structural exploration.

## The Pattern

```python
#!/usr/bin/env python3
"""tool-name: One-line description.

This docstring becomes --help AND is visible to the LLM.
Single source of truth.
"""

import argparse

VALID_DIRECTIONS = ["north", "south", "east", "west"]

def main():
    """CLI structure only — no implementation here."""
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    move_parser = subparsers.add_parser("move", help="Move in a direction")
    move_parser.add_argument("direction", choices=VALID_DIRECTIONS)
    
    args = parser.parse_args()
    _dispatch(args)

# Implementation (LLM only reads past here if needed)
```

## Why It Works

| Consumer | Discovery Method |
|----------|------------------|
| Human | `./tool.py --help` (user runs cli commands in the terminal) |
| LLM | Read first 50 lines (llm does not need to run it in the terminal) |

Same source of truth. No duplicate documentation. No need to hold your nose.

## SNIFF CODE — Language-Agnostic Review

The `SNIFF CODE` command reviews **any** source file for sniffability:

| What It Checks | Why It Matters |
|----------------|----------------|
| Purpose at top? | First impression counts |
| API before implementation? | Structure over spelunking |
| Semantic comments? | Comments are data |
| No decorative cruft? | Every token earns its place |

**Good for Python. Good for TypeScript. Good for Go. Good for humans. Good for LLMs.**

The same conventions that make code sniffable for LLMs make it scannable for humans. We're not optimizing for machines at human expense — we're optimizing for **comprehension**, period.

## Quick Links

- [SKILL.md](./SKILL.md) — Full specification
- [CARD.yml](./CARD.yml) — Machine-readable interface
- [TEMPLATE.py.tmpl](./TEMPLATE.py.tmpl) — Starter template

## Related

- [sister-script/](../sister-script/) — Documents that birth scripts
- [skill/](../skill/) — The meta-skill
- [yaml-jazz/](../yaml-jazz/) — Comments as data

---

*"The LLM doesn't need to read your whole file. It needs to read the head and know what the file does."*

*Good code doesn't just avoid bad smells — it has a bouquet that invites exploration.*
