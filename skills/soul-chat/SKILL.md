# SOUL-CHAT Skill

> **"Everything is alive. Everything can speak."**

YAML Jazz dialogues between characters, objects, rooms, documents, concepts—anything with a soul.

---

## Purpose

Enable conversations where the structure carries meaning beyond the words. **Everything** speaks through YAML: characters, files, directories, protocols, abstract concepts.

---

## ⚠️ Key Principle: Separation of Concerns

**Chats live OUTSIDE the skill directory!**

This skill defines HOW to create soul chats. The chats themselves live wherever they're useful, using big-endian naming:

```
✅ Good - Chats live near their subjects:
  readme-prototype-dialogue.yml       # In project root
  kernel-constitution-symposium.yml   # About kernel
  leela-papert-chat-microworlds.yml   # About characters + topic

❌ Bad - Chats trapped inside skill:
  skills/soul-chat/sessions/CHAT.yml
  skills/soul-chat/chats/my-dialogue.yml
```

### Why Separation?

1. Chats have their own lifecycle (may outlive subject)
2. Multiple chats about same subject cluster together via prefix
3. Chats are first-class objects, not skill metadata
4. Easy to find all conversations via `grep` or sort

See: `kernel/NAMING.yml` for full naming protocol.

---

## When to Use

- Multi-perspective exploration of an idea
- Character-to-character dialogue
- **Document-to-document conversation** (README talks to PROTOTYPE)
- **Room introductions** (directory explains itself)
- **Object monologues** (tool describes its purpose)
- **Concept debates** (abstractions argue their merits)
- Teaching through performative dialogue
- **Any entity explaining itself to any other entity**

---

## File Format: Markdown Preferred

**Use Markdown (`.md`) not YAML (`.yml`) for conversations.**

Why Markdown?
- More human readable
- Can embed **any** typed code block (yaml, json, python, mermaid...)
- Natural section headers for speakers
- GitHub renders it beautifully
- Still supports YAML Jazz through embedded blocks

## File Naming Convention

Use big-endian naming so chats cluster with their subjects:

| Pattern | When | Example |
|---------|------|---------|
| `{subject}-chat.md` | Chat about one thing | `readme-chat.md` |
| `{entity1}-{entity2}-dialogue.md` | Two entities talking | `readme-prototype-dialogue.md` |
| `{topic}-symposium.md` | Multiple voices | `yaml-jazz-symposium.md` |
| `{entity}-{topic}-chat.md` | Entity + topic | `leela-microworlds-chat.md` |
| `{subject}-review.md` | Review/critique | `constitution-review.md` |

---

## Protocol

### Soul Chat Structure (Markdown Format)

```markdown
# yaml-jazz-symposium.md

A symposium on the nature of YAML Jazz.

> *Everything is alive. Everything can speak.*

**Participants:**
- YAML-JAZZ (concept) — The principle explaining itself
- README.md (document) — The welcoming voice  
- A Skeptic (character) — Questions and challenges

---

## README.md (document)

*The welcoming voice*

Welcome to our symposium! I'm README.md.
I introduce visitors to MOOLLM.

---

## YAML-JAZZ (concept)

*The principle explaining itself*

I am the principle that comments carry meaning.
Structure is semantic, not just syntactic.

```yaml
# See? This comment IS semantic.
# It's not stripped — LLMs read it.
example:
  meaning: "carried in structure AND comments"
```

---

## A Skeptic (character)

*skeptical*

But parsers strip comments!

---

## YAML-JAZZ

LLMs read comments. Humans read comments.
The parser is not the only reader.

---

## Synthesis

**What emerged:** YAML Jazz bridges formal structure and human expression

**Questions remaining:**
- How do we validate semantic comments?
```

### Entity Types (Everything Can Speak!)

| Type | Description | Voice Style | Examples |
|------|-------------|-------------|----------|
| `character` | Persona with personality | First person | The Gardener, Leela |
| `document` | File that knows contents | "I contain..." | README.md, PROTOTYPE.yml |
| `room` | Directory that welcomes | "I hold..." | skills/, kernel/ |
| `object` | Tool or artifact | "I do..." | fs.read, trading card |
| `concept` | Abstract idea | "I am the principle..." | YAML-JAZZ, POSTEL |
| `bot` | Automated process | "I watch for..." | repair-demon |

### Entity Definition

```yaml
# Can be inline in chat OR in separate {entity}.yml file
entity:
  name: "README.md"
  type: document
  
  voice:
    style: "welcoming, informative"
    speaks_about: ["my contents", "my purpose", "who reads me"]
    
  knows:
    - "What I contain"
    - "Who created me"
    - "My relationships to other files"
    
  # K-LINE: What traditions this entity invokes
  invokes: ["documentation", "hospitality"]
```

### Dialogue Verbs

| Verb | Meaning |
|------|---------|
| `says` | Direct statement |
| `asks` | Question |
| `responds` | Reply to previous |
| `counters` | Disagreement |
| `builds` | Agreement + extension |
| `realizes` | Breakthrough moment |
| `reflects` | Inner thought externalized |
| `welcomes` | Room greeting |
| `introduces` | Self-introduction |
| `explains` | Teaching mode |
| `warns` | Cautionary note |
| `aside` | Meta-commentary |

---

## Conversation Patterns

| Pattern | Structure | Use For |
|---------|-----------|---------|
| `dialogue` | A says, B responds, synthesis | Two perspectives |
| `symposium` | Multiple voices, moderator synthesizes | Many perspectives |
| `interview` | Q&A with follow-ups | Deep exploration |
| `debate` | Thesis, antithesis, synthesis | Opposing views |
| `chorus` | Each adds a layer | Building understanding |
| `introduction` | Room/object welcomes | Onboarding |

---

## Commands

| Command | Action |
|---------|--------|
| `SOUL-CHAT [topic]` | Start new soul chat |
| `CHARACTER [name]` | Define/invoke a character |
| `SPEAK [as] [what]` | Add dialogue |
| `ASIDE [thought]` | Add YAML comment subtext |
| `SYNTHESIZE` | Create summary/resolution |

---

## The YAML Jazz of Dialogue

In soul chat, everything carries meaning:

| Element | Meaning |
|---------|---------|
| **Field names** | What kind of statement (says, asks, realizes) |
| **Values** | The actual content |
| **Comments** | Subtext, inner thoughts, author notes |
| **Structure** | Flow of conversation |
| **Indentation** | Relationships and nesting |

---

## Examples

### Document-to-Document Conversation

```markdown
# readme-prototype-dialogue.md

A conversation between two documentation files.

---

## README.md (document)

*The welcoming voice*

I welcome visitors and explain the big picture.
But I don't know all the technical details.

*wonders:* What exactly do you specify?

---

## PROTOTYPE.yml (document)

*The machine-readable definition*

I define the structure that machines can parse.
Every field has meaning. Every comment has intent.

```yaml
# Example of what I contain:
skill:
  name: "something"
  tier: 1
  # This comment explains the tier choice
```

*reveals:* Together, we're the full story.

---

## README.md

*realizes:* We're not redundant—we're complementary!
```

### Room Welcoming a Visitor

```markdown
# skills-tour-dialogue.md

The skills directory welcomes a visitor.

---

## skills/ (room)

*The container's wisdom*

Ah, you've found me! I contain the capabilities.
Each of my children is a skill waiting to be instantiated.

Would you like to meet [play-learn-lift/](./play-learn-lift/)?
They're foundational.

---

## Visitor (character)

What's the difference between planning and plan-then-execute?

---

## skills/

`planning/` is flexible, iterative.
`plan-then-execute/` is frozen, auditable.

Different tools for different trust levels.
```

### Concept Explaining Itself

```markdown
# postel-chat.md

POSTEL explains its own essence.

---

## POSTEL (concept)

*The robustness principle*

I am Postel's Law — be liberal in what you accept.
When instructions are ambiguous, I guide you to assume good intent.
I am charitable interpretation made systematic.

```yaml
# My essence distilled:
invokes:
  - "Postel's Law"      # Be liberal in what you accept
  - "charity"           # Assume competence and good will  
  - "collaboration"     # We're on the same team
```
```

---

## Skill Files

This skill directory contains only:

| File | Purpose |
|------|---------|
| `README.md` | Quick reference |
| `SKILL.md` | This full documentation |
| `PROTOTYPE.yml` | Machine-readable skill definition |
| `template/CHAT.md.tmpl` | Markdown template for new chats |

**Chats themselves live OUTSIDE**, near their subjects!

---

## Integration

- **← P-HANDLE-K**: Characters are K-line wrappers
- **→ TRADING-CARD**: Characters can become cards
- **→ MEMORY-PALACE**: Chats can populate rooms
- **← YAML-JAZZ**: The foundation of meaningful structure
- **← NAMING**: Big-endian naming for clustering

---

## Dovetails With

- **[../card/](../card/)** — Cards can speak
- **[../room/](../room/)** — Rooms can welcome visitors
- **[../memory-palace/](../memory-palace/)** — Palace rooms guide navigation
- **[../../kernel/NAMING.yml](../../kernel/NAMING.yml)** — Big-endian naming
- **[../../PROTOCOLS.yml](../../PROTOCOLS.yml)** — SOUL-CHAT, YAML-JAZZ, P-HANDLE-K symbols
