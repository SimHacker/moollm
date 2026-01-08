# Character Incarnation Protocol

> *"READMEs are catalogs. Subdirectories are incarnations. Each instance is UNIQUE."*

---

## The Two-Level Pattern

```
characters/
├── PROTOCOL.md          # This file -- shared by all subdirs
├── real-people/
│   ├── README.md        # CATALOG: Lists possible characters to incarnate
│   ├── ROOM.yml         # Ethical framing for this category
│   ├── CARD.yml         # Advertisements for this room
│   └── alan-kay/        # INCARNATION: Actually instantiated character
│       └── CHARACTER.yml
```

### Level 1: README Catalogs (Lazy)

READMEs list **possible characters** organized by sub-category:

```markdown
### Computing & AI

| Character | Reference | Description |
|-----------|-----------|-------------|
| alan-kay | `lloooomm/00-Characters/alan-kay/` | Smalltalk creator |
| ada-lovelace | `lloooomm/00-Characters/ada-lovelace/` | First programmer |
```

These are **pointers, not instances**. The character doesn't exist here yet.

### Level 2: Subdirectory Incarnations (Instantiated)

When you need a character, **create a subdirectory**:

```
> INCARNATE alan-kay

Created: characters/real-people/alan-kay/
  - CHARACTER.yml (generated from references)
```

Now the character EXISTS. It's **owned** and **unique** to this adventure.

---

## Just-In-Time Incarnation

**Don't pre-create characters.** Wait until needed:

```
> SUMMON marshall-mcluhan

Marshall McLuhan is not yet incarnated.
Reference found: lloooomm/00-Characters/marshall-mcluhan/

Would you like to INCARNATE? (y/n)
```

---

## Reference Sources

Characters can reference multiple sources:

```yaml
character:
  name: "Marshall McLuhan"
  
  references:
    - type: lloooomm
      path: "lloooomm/00-Characters/marshall-mcluhan/"
    - type: wikipedia
      url: "https://en.wikipedia.org/wiki/Marshall_McLuhan"
    - type: work
      title: "Understanding Media"
```

---

## Commands

| Command | Effect |
|---------|--------|
| `INCARNATE name` | Create character from reference |
| `INCARNATE name FROM url` | Create from specific source |
| `GENERATE name AS "desc"` | Create original character |
| `TRANSFORM name INTO category` | Move between categories |
| `RETIRE name` | Archive (don't delete) |

---

## Uniqueness Principle

Each incarnation is **UNIQUE** to this adventure. Same reference, different context.

---

## Sub-Category Promotion

When a README sub-category grows, promote to subdirectory:

```
fictional/
├── blade-runner/       # Was a section, now a room
│   ├── ROOM.yml
│   └── roy-batty/
```

---

## Ethical Inheritance

Subdirectories inherit ethics from parents. Can add, not remove.

> *"The README is the seed catalog. The subdirectory is the garden."*
