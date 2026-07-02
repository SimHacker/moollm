# 📜 Session Log

> Human-readable markdown session logs that tell stories

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [play-learn-lift/](../play-learn-lift/) | Sessions record PLAY |
| [plain-text/](../plain-text/) | Sessions persist as text |
| [character/](../character/) | Session files live in character directories |
| [adventure/](../adventure/) | Adventure LOG.md follows session patterns |
| [summarize/](../summarize/) | Compress old sessions |
| [honest-forget/](../honest-forget/) | Graceful memory decay |
| [markdown/](../markdown/) | Sessions ARE markdown |
| [examples/adventure-4/characters/real-people/don-hopkins/sessions/](../../examples/adventure-4/characters/real-people/don-hopkins/sessions/) | Gold standard examples |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol with writing guide

---

## Overview

Session logs are **living documents** that capture the narrative of play. Unlike technical event logs, sessions are meant to be **READ** — by users, by future LLMs warming context, by anyone exploring the repo.

> [!NOTE]
> Session logs are **NOT append-only!** They grow and improve over time. Update the index, add links, fix typos — sessions are living documents.

---

## Where Sessions Live

Default: **`SESSION.md`** in the character directory, or named sessions in a `sessions/` subdirectory.

```
characters/real-people/don-hopkins/sessions/marathon-session.md
characters/real-people/don-hopkins/sessions/adventure-uplift.md
characters/fictional/donna-toadstool/SESSION.md
characters/animals/monkey-palm/SESSION.md
```

Name variants: `marathon-session.md`, `adventure-uplift.md`, `SESSION-day1.md`

---

## Key Principles

| Principle | Description |
|-----------|-------------|
| **📖 Narrative first** | Write for humans, not machines |
| **📂 Collapsible sections** | Show narrative, hide data |
| **📊 Index at top** | Always keep updated |
| **🔗 Link generously** | Every file mentioned = link |
| **📈 Tables tell stories** | Stats, rosters, inventories |
| **🔄 Retroactive improvement** | Update as you learn more |

---

## Collapsible Sections

```markdown
<details open>
<summary><h2>🌟 Major Event — Descriptive Subtitle</h2></summary>

Narrative content here (always visible).

<details open>
<summary>📂 <strong>Technical: YAML changes under the hood</strong></summary>

Hidden data — click to expand.

</details>
</details>
```

| Pattern | Use For | Default State |
|---------|---------|---------------|
| `<details open>` | Narrative chapters | **Open** |
| `<details open>` | Technical details | Closed |

---

## 🌟 Gold Standard Examples

Study these for best practices:

| Session | What It Demonstrates |
|---------|---------------------|
| [**Don Hopkins (Marathon)**](../../examples/adventure-4/characters/real-people/don-hopkins/sessions/marathon-session.md) | 7000+ lines, 5 days, extensive linking, speed-of-light simulations |
| [**Donna Toadstool**](../../examples/adventure-4/characters/fictional/donna-toadstool/sessions/2026-01-09-birth.md) | Character creation narrative, file operations, appendices |

---

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [skills/](../) |
| 📖 Full Spec | [SKILL.md](./SKILL.md) |
