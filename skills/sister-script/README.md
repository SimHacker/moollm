# 👯 Sister Script

> Document-first development. Automate only what's proven.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | Core MOOLLM methodology |
| [play-learn-lift/](../play-learn-lift/) | Sister scripts ARE the LIFT stage output |
| [skill/](../skill/) | Sister scripts become skills |
| [sniffable-python/](../sniffable-python/) | Sister scripts follow this structure |
| [plain-text/](../plain-text/) | Scripts persist as files |
| [yaml-jazz/](../yaml-jazz/) | Comments carry meaning |
| [constructionism/](../constructionism/) | Document → Procedure → Automation |
| [postel/](../postel/) | Liberal input, conservative output |
| [debugging/](../debugging/) | Document how you debugged |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: PROCEDURE.md](PROCEDURE.md.tmpl) — procedure template
- [Template: SISTER.yml](SISTER.yml.tmpl) — script relationship

## Overview

The document is the source of truth. Scripts are its children. This is the **LIFT stage** of [play-learn-lift](../play-learn-lift/).

**Sister scripts follow [sniffable-python](../sniffable-python/) conventions** — structured so both humans and LLMs can understand them from the first 50 lines.

## The Pattern

```
📄 Document → 💻 Commands → 📋 Procedure → 🤖 Sister Script (Sniffable Python)
```

1. Start with natural language (PLAY)
2. Add manual commands (PLAY/LEARN)
3. Document working procedures (LEARN)
4. Generate automation (LIFT) → **sniffable-python format**

## Sniffable Structure

Sister scripts should be structured so the LLM can sniff the header:

```python
#!/usr/bin/env python3
"""tool-name: One-line description.

Docstring becomes --help AND is visible to LLM.
"""

import argparse

def main():
    """CLI structure — sniff this to understand the tool."""
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    # ... CLI tree here ...
```

**One sniff and you smell success.**

## Bidirectional Evolution

- Document → Script: Proven procedures become automated
- Script → Document: Automation insights improve docs
