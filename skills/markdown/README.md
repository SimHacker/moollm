# Markdown Skill

> *"Plain text formatting that's readable raw AND rendered"*

## Quick Reference

### Headers
```markdown
# H1
## H2
### H3
```

### Emphasis
```markdown
*italic* or _italic_
**bold** or __bold__
***bold italic***
```

### Lists
```markdown
- Unordered item
- Another item

1. Ordered item
2. Another item

- [ ] Task (unchecked)
- [x] Task (checked)
```

### Links & Images
```markdown
[Link text](url)
![Alt text](image-url)
```

### Code
```markdown
`inline code`

​```python
def code_block():
    pass
​```
```

### Tables (GFM)
```markdown
| Column 1 | Column 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

### Collapsible (GFM) — CRITICAL!
```html
<details>
<summary><strong>📋 Section Title — Key points visible here</strong></summary>

Hidden content. Reader can skip if summary tells them enough!

</details>
```

**Pro tip:** Put descriptive text in `<summary>` so readers can scan without opening!

### Mermaid Diagrams (GFM)
```markdown
​```mermaid
flowchart LR
    A[YAML] --> B[Python] --> C[JSON] --> D[Browser]
​```
```

Types: `flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`, `classDiagram`, `gantt`

### Blockquotes
```markdown
> Quote text
> — Attribution
```

---

## Key Principle

**The source IS the destination.** Markdown is readable before AND after rendering.

---

See: [SKILL.md](SKILL.md) for full documentation.
