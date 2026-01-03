# Adventure Protocol Skill
## Room-Based Exploration with Narrative Evidence Collection

*"Every directory is a room. Every file is a clue. Navigation is investigation."*

---

## Purpose

Transform file exploration into a narrative-driven adventure where:
- The filesystem becomes a dungeon/world to explore
- Files are artifacts, clues, or characters you encounter
- Your progress is tracked in a persistent adventure log
- Evidence accumulates toward understanding

Combines Memory Palace spatial organization with detective/adventure game mechanics.

---

## When to Use

- Exploring an unfamiliar codebase
- Investigating a bug through evidence
- Onboarding to a new project
- Documentation archaeology
- Any exploration task that benefits from narrative framing

---

## Prerequisites

- File tools (ls, read, write)
- Working Memory Palace recommended
- No execution required (Tier 1)

---

## Protocol

### Step 1: Begin the Adventure

1. Create an ADVENTURE.yml to track the quest
2. Create a LOG.md for narrative progress
3. Identify the starting "room" (directory)
4. State the quest objective

### Step 2: Room Protocol

When entering any directory:

1. **DESCRIBE** — List contents, note what's here
2. **EXAMINE** — Read interesting files
3. **COLLECT** — Note evidence in adventure log
4. **EXITS** — Note paths to other rooms
5. **DECIDE** — Choose next direction

### Step 3: Evidence Collection

As you explore:
- **CLUES** — Bits of information that might matter
- **ITEMS** — Files worth remembering
- **CHARACTERS** — Code entities, configs, patterns
- **MAPS** — Mental models of structure

### Step 4: Conclude

1. Summarize findings
2. Update adventure log
3. Archive or continue quest

---

## Core Files

### ADVENTURE.yml
```yaml
quest:
  name: "The Mystery of the Failing Tests"
  objective: "Discover why tests fail on CI but pass locally"
  status: "active"
  
starting_room: "project-root/"
current_room: "src/tests/"

evidence:
  clues:
    - id: "clue-001"
      found_in: "package.json"
      content: "Different test runner versions"
      significance: "high"
      
  items:
    - name: "CI Config"
      path: ".github/workflows/test.yml"
      notes: "Uses Node 18"
      
  characters:
    - name: "jest.config.js"
      type: "configuration"
      personality: "Strict about module resolution"

rooms_visited:
  - path: "/"
    entered: "2025-12-30T10:00"
    notes: "Project root, standard layout"
    
  - path: "src/tests/"
    entered: "2025-12-30T10:05"
    notes: "Found failing test files"

quest_log:
  - "Began investigation in project root"
  - "Noticed version mismatch in package.json"
  - "Descended into tests directory"
```

### LOG.md
```markdown
# Adventure Log: The Mystery of the Failing Tests

## Quest Objective
Discover why tests fail on CI but pass locally.

---

## Entry 1: The Beginning
*10:00 AM - Project Root*

I stand in the project root. Around me I see the usual suspects:
- `package.json` — The manifest of dependencies
- `src/` — Where the code lives
- `.github/` — CI secrets dwell here

I examine `package.json` first...

**CLUE FOUND:** Test runner version is `^29.0.0` — a floating version!

## Entry 2: Into the Tests
*10:05 AM - src/tests/*

I descend into the tests directory. The air grows thick with assertions.
Files here: `user.test.ts`, `api.test.ts`, `setup.ts`

I examine `setup.ts`...

**ITEM ACQUIRED:** `setup.ts` — Contains global mocks

---

## Current Status
- **Location:** src/tests/
- **Clues:** 1
- **Items:** 1
- **Next Move:** Examine CI config
```

---

## Room Description Format

When you enter a room, narrate it:

```markdown
## [Directory Name]
*[Timestamp] — [Path]*

### Description
What kind of place is this? What's the vibe?

### Contents
- `file1.js` — brief description
- `subdir/` — [door] leads somewhere

### Notable Findings
What stands out? What's unusual?

### Exits
- ← Back to [parent]
- → Into [subdir1]
- → Into [subdir2]

### Decision
Where next, and why?
```

---

## Commands

| Intent | Action |
|--------|--------|
| "Enter room X" | cd to directory, ls contents |
| "Examine artifact" | Read file, note findings |
| "Collect evidence" | Add to ADVENTURE.yml |
| "Update log" | Append to LOG.md |
| "Check inventory" | Review evidence section |
| "Recall quest" | Read ADVENTURE.yml objective |
| "Where am I?" | Note current path |
| "Review journey" | Read LOG.md |

---

## Evidence Types

### Clues
Small pieces of information:
```yaml
clues:
  - id: "clue-003"
    found_in: "config/database.yml"
    content: "Production uses different pool size"
    significance: "medium"
    relates_to: ["clue-001"]
```

### Items
Files worth tracking:
```yaml
items:
  - name: "The Ancient Makefile"
    path: "Makefile"
    notes: "Contains build secrets"
    acquired: "2025-12-30T10:15"
```

### Characters
Code entities with personality:
```yaml
characters:
  - name: "AuthMiddleware"
    type: "guardian"
    location: "src/middleware/auth.ts"
    personality: "Suspicious of all requests"
    quotes:
      - "401 Unauthorized"
      - "Token expired"
```

### Maps
Mental models:
```yaml
maps:
  - name: "Data Flow"
    description: "How data moves from API to database"
    rooms: ["routes/", "services/", "models/"]
```

---

## Tips

1. **Stay in character** — The narrative frame aids memory
2. **Log frequently** — Update LOG.md as you go
3. **Evidence everything** — Small clues compound
4. **Name your NPCs** — Config files have personalities
5. **Draw maps** — Mental models in ADVENTURE.yml
6. **Quest checkpoints** — Save state before major moves

---

## Outputs

- ADVENTURE.yml with quest state and evidence
- LOG.md with narrative exploration record
- Accumulated understanding of the territory
- Transferable documentation of the journey
