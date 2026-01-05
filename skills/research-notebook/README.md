# 📔 Research Notebook

> Structured research with sources, findings, and decisions

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: NOTEBOOK.yml](NOTEBOOK.yml.tmpl) — notebook template
- [Template: SOURCES.yml](SOURCES.yml.tmpl) — sources template

## Overview

Track investigations and capture knowledge. This is the **LEARN stage** of [play-learn-lift](../play-learn-lift/) — where patterns emerge from exploration.

## Structure

| Section | Purpose |
|---------|---------|
| **Questions** | What you're trying to learn |
| **Sources** | Where you looked |
| **Findings** | What you discovered |
| **Decisions** | What you concluded |

## Example

```yaml
research:
  topic: "LLM context management"
  
  questions:
    - "How do other systems handle token budgets?"
    
  sources:
    - url: "paper-on-context.pdf"
      relevance: "Direct answer to Q1"
```

## Related Skills

- [play-learn-lift](../play-learn-lift/) — research-notebook IS LEARN
- [debugging](../debugging/) — investigation structure
- [scratchpad](../scratchpad/) — unstructured notes