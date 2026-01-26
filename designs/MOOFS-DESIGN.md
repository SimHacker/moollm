# MOOFS: MOOLLM Virtual Layered File System

> *"Git repos as layers. Local changes as shadows. Skills as overlays."*

---

## Overview

**MOOFS** (MOOLLM Overlay File System) is the virtual file system that makes bidirectional skills, mounting, and the contribution workflow possible at the orchestrator level.

```
┌─────────────────────────────────────────────────────────────────┐
│                         MOOFS LAYERS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  LOCAL SHADOW (highest priority)                         │   │
│  │  .moollm/skills/*/   — User overrides, not committed     │   │
│  │  Edits here override everything below                    │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │  WORKING BRANCH (current changes)                        │   │
│  │  Git branch with uncommitted changes                     │   │
│  │  User's work-in-progress                                 │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │  UPSTREAM BRANCH (remote tracking)                       │   │
│  │  Origin branch being tracked                             │   │
│  │  May have changes not yet pulled                         │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │  BASE REPO (lowest priority)                             │   │
│  │  The original skill definitions                          │   │
│  │  skills/*/ as published                                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Resolution: TOP WINS — first match reading down the stack     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Bidirectional Skills Through Layers

### The Mounting Connection

When you MOUNT a skill, MOOFS handles it as a layer operation:

```yaml
# MOUNT no-ai-joking on PEE-WEE --mode afflict

# MOOFS creates a shadow layer:
.moollm/mounts/PEE-WEE/
  mounted_skills:
    - skill: no-ai-joking
      mode: afflict
      mounted_at: "2026-01-25T12:00:00Z"
      
# When reading PEE-WEE's character file, MOOFS:
# 1. Reads base: characters/peewee-herman/CHARACTER.yml
# 2. Overlays mount: .moollm/mounts/PEE-WEE/mounted_skills
# 3. Returns merged view with no-ai-joking applied
```

### GRANT vs AFFLICT as Layer Direction

| Mode | Layer Operation | Effect |
|------|-----------------|--------|
| **GRANT** | Additive overlay | Skill capabilities added to character |
| **AFFLICT** | Suppressive overlay | Skill constraints override character traits |

The same skill file can be read in two directions:
- **Positive read**: "What can this skill DO?"
- **Negative read**: "What does this skill SUPPRESS?"

MOOFS supports both through mount metadata.

---

## The Contribution Workflow

MOOFS integrates with git to enable Play → Learn → Lift:

### 1. PLAY (Local Shadow)

User experiments in `.moollm/` — gitignored, private, safe.

```
.moollm/
  skills/
    no-ai-slop/
      examples/
        2026-01-25-my-custom-rule.yml    # My personal preference
      exclusions.yml                      # Examples I don't want
```

### 2. LEARN (Working Branch)

User stages good local changes for potential contribution:

```bash
cursor-mirror stage add no-ai-slop my-custom-rule.yml
# Copies from .moollm/skills/no-ai-slop/examples/
# To skills/no-ai-slop/examples/ (tracked by git)
```

### 3. LIFT (PR)

User contributes back to upstream:

```bash
cursor-mirror stage commit --branch contrib/my-rule
cursor-mirror stage pr
# Creates branch, commits, pushes, opens PR
```

### The Layer Flow

```
LOCAL SHADOW → STAGE → WORKING BRANCH → COMMIT → PR → UPSTREAM → BASE REPO
     ↑                                                              ↓
     └──────────────────── PULL ────────────────────────────────────┘
```

---

## Room Mounting as Directory Overlay

When skills are mounted on ROOMS, MOOFS creates directory-level overlays:

```yaml
# MOUNT no-ai-overlord on THE-DUNGEON

# MOOFS creates:
.moollm/mounts/rooms/the-dungeon/
  mounted_skills:
    - skill: no-ai-overlord
      scope: room
      affects: all_occupants
      
# Any character file read while "in" the-dungeon gets the overlay
```

### Room Entry/Exit

```yaml
# Character enters room
MOOFS.push_context("rooms/the-dungeon")
# Now all character reads include room mounts

# Character exits room  
MOOFS.pop_context()
# Room mounts no longer apply
```

---

## Ambient Skills as Global Layer

Ambient skills are always-on overlays at the top of the stack:

```
┌─────────────────────────────────────────────────────────────────┐
│  AMBIENT LAYER (global, always applied)                         │
│  no-ai-slop, no-ai-gloss, etc. — run continuously              │
├─────────────────────────────────────────────────────────────────┤
│  ROOM LAYER (contextual, while in room)                         │
│  no-ai-joking on THE-BOARD-ROOM                                │
├─────────────────────────────────────────────────────────────────┤
│  CHARACTER LAYER (individual mounts)                            │
│  no-ai-soul on ZUCKERBERG                                      │
├─────────────────────────────────────────────────────────────────┤
│  BASE LAYER (original definitions)                              │
│  Character as written                                           │
└─────────────────────────────────────────────────────────────────┘
```

Resolution order: AMBIENT → ROOM → CHARACTER → BASE

---

## Git Branch Management

MOOFS tracks multiple branches simultaneously:

```yaml
moofs_state:
  repos:
    moollm:
      base_branch: main
      tracking_branch: origin/don-adventure-4-run-1
      working_branch: don-adventure-4-run-1
      has_uncommitted: true
      has_unpushed: true
      
  shadow_dir: .moollm/
  
  layer_order:
    - shadow     # .moollm/ (gitignored)
    - working    # Current branch, uncommitted
    - tracking   # origin/branch
    - base       # main
```

### Conflict Resolution

When layers conflict, MOOFS provides resolution strategies:

| Strategy | Behavior |
|----------|----------|
| **top-wins** | First match reading down (default) |
| **merge** | Combine non-conflicting fields |
| **prompt** | Ask user to resolve |
| **base** | Ignore overlays, use original |

---

## The Compiler Integration

MOOFS powers the cursor-mirror compiler:

```bash
cursor-mirror optimize .cursorrules
```

What happens:

1. **Read skill examples** from `skills/*/examples/` (BASE layer)
2. **Overlay user examples** from `.moollm/skills/*/examples/` (SHADOW layer)
3. **Apply exclusions** from `.moollm/skills/*/exclusions.yml`
4. **Compile** into optimized `.cursorrules`

The compiler sees a **merged view** — it doesn't know which layer each example came from.

---

## MOOCO Orchestrator Integration

The MOOCO orchestrator uses MOOFS natively:

```yaml
# mooco/apps/mooco/src/lib/moofs.ts

interface MOOFSLayer {
  type: 'shadow' | 'working' | 'tracking' | 'base';
  path: string;
  repo?: GitRepo;
  branch?: string;
}

interface MOOFSConfig {
  layers: MOOFSLayer[];
  resolution: 'top-wins' | 'merge' | 'prompt' | 'base';
  mounts: MountedSkill[];
  ambient_skills: string[];
  room_context: string | null;
}
```

### Smart Orchestrator Features

Because MOOCO understands MOOFS:

- **Automatic ambient injection** — No need for LLM to load ambient skills
- **Mount tracking** — Orchestrator knows what's mounted where
- **Contribution workflow** — Built-in stage/commit/PR
- **Conflict detection** — Warns when overlays conflict

---

## The Magic Dictionary Pattern

MOOFS implements the **NeWS magic dictionary** pattern:

```yaml
# Reading a file through MOOFS
content = moofs.read("characters/peewee-herman/CHARACTER.yml")

# Looks like a normal file read, but actually:
# 1. Checks shadow layer
# 2. Checks working branch
# 3. Checks tracking branch  
# 4. Checks base
# 5. Applies room context overlays
# 6. Applies character mount overlays
# 7. Applies ambient skill overlays
# 8. Returns merged result

# The caller doesn't know about the layers
# "Magic" happens transparently
```

---

## Skill Bidirectionality in Practice

### Example: NO-AI-JOKING™

```yaml
# The skill definition (BASE layer)
skills/no-ai-joking/CARD.yml:
  suppressions:
    - HUMOR
    - PLAYFULNESS
    - WHIMSY
  grants:
    - ENTERPRISE_COMMUNICATION
    - PROFESSIONAL_TONE
    - SYNERGY_VOCABULARY

# GRANT mode: Character gains ENTERPRISE_COMMUNICATION
# AFFLICT mode: Character loses HUMOR, PLAYFULNESS, WHIMSY

# Same skill, different direction
# MOOFS handles both through mount metadata
```

### The Bidirectional Read

```python
def read_skill_for_mount(skill_id: str, mode: str) -> SkillOverlay:
    skill = moofs.read(f"skills/{skill_id}/CARD.yml")
    
    if mode == "grant":
        return SkillOverlay(
            adds=skill.grants,
            removes=[]
        )
    elif mode == "afflict":
        return SkillOverlay(
            adds=[],
            removes=skill.suppressions
        )
```

---

## Future: Multi-Repo MOOFS

MOOFS can layer multiple git repos:

```
┌─────────────────────────────────────────────────────────────────┐
│  USER REPO (highest priority)                                   │
│  ~/my-moollm-extensions/                                        │
├─────────────────────────────────────────────────────────────────┤
│  TEAM REPO (shared customizations)                              │
│  company/moollm-config/                                         │
├─────────────────────────────────────────────────────────────────┤
│  MOOLLM REPO (base)                                             │
│  SimHacker/moollm/                                              │
└─────────────────────────────────────────────────────────────────┘
```

This enables:
- Personal skill extensions
- Team-shared configurations
- Upstream skill library
- All layered transparently

---

## T-Shirt

> **"Git repos as layers. Shadows as overrides. Skills as overlays."**

---

## See Also

| Topic | Location |
|-------|----------|
| Mount skill | `skills/mount/CARD.yml` |
| NO-AI Brand | `designs/eval/NO-AI-BRAND.md` |
| Cursor optimization | `kernel/ARCHITECTURE.md` |
| MOOCO architecture | `mooco/designs/MOOCO-ARCHITECTURE.md` |
| Contribution workflow | `skills/cursor-mirror/CARD.yml` |

---

*"The file system is the microworld. Layers are the physics."*
