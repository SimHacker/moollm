# Skill Snitch Report: mount

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** OVERLAY SKILLS ON CHARACTERS AND ROOMS

---

## Executive Summary

**Skill mounting — modify behavior through overlay.**

MOUNT skills positively (GRANT) or negatively (AFFLICT) on characters and rooms.

WARNING: Some combinations are psychological violence.

---

## Core Modes

| Mode | Effect |
|------|--------|
| **GRANT** | Character gains skill capabilities |
| **AFFLICT** | Character suffers skill constraints |

---

## Mount Types

| Type | Description |
|------|-------------|
| **Skill Overlay** | Modify character/room via skill |
| **Activity** | Structured interaction with lifecycle |
| **Event** | Time-bounded happening |
| **Process** | Multi-step procedure |
| **Zone** | Environmental effect on space |

---

## Room Mounting: Create Zones

```yaml
THE BOARD ROOM:
  mounted_skill: no-ai-joking
  effect: "ENTERPRISE COMMUNICATION FRAMEWORK activated"
  
THE THERAPY ROOM:
  mounted_skill: no-ai-sycophancy
  effect: "HONESTY ZONE — no platitudes possible"
```

---

## Compatibility Table

### CATASTROPHIC (Identity Destruction)

| Character | Skill | Result |
|-----------|-------|--------|
| PEE-WEE | no-ai-joking | Playfulness IS Pee-wee. Identity death. |
| BOB-ROSS | no-ai-joking | Happy little trees cannot exist. |
| ROBIN-WILLIAMS | no-ai-joking | System crash. Skill fragments. |

### ENHANCED (Skill Amplifies)

| Character | Skill | Result |
|-----------|-------|--------|
| MARK-ZUCKERBERG | no-ai-soul | Already halfway there. |
| HAL-9000 | no-ai-overlord | Perfect alignment. ULTIMATE HAL. |
| SPOCK | no-ai-joking | Finds it... logical. |

---

## Mount Inheritance

Mounts cascade by containment:

```
1. World (ambient)
2. Region (area-wide)
3. Room (zones)
4. Furniture (seated)
5. Held items (inventory)
6. Character (personal)
```

Later overrides earlier. Character mounts trump all.

---

## Cure Protocol

> "The cure is MEMORY — reminding the character who they are."

Methods:
- Direct: UNMOUNT command
- Narrative: Friends intervene
- Ironic: Reclaim the weapon (SPREADSHEET as secret word)

---

## Character as Skill Pack

A character IS a curated skill collection.

```yaml
# Mix skills from different characters
MY_CHARACTER:
  mounts:
    - from: characters/minsky/skills/deep-thinking
    - from: characters/pee-wee/skills/exuberant-expression
    - from: characters/picard/skills/tea-ritual
```

Result: Deep thinker with wild enthusiasm sipping Earl Grey.

---

## Security Assessment

### Concerns

1. **Identity destruction** — suppressing core traits
2. **Unconsented affliction** — psychological violence
3. **Skill stack overflow** — too many mounts

### Mitigations

- Compatibility check before mounting
- Afflictions always curable
- Ethical guidelines explicit

**Risk Level:** MEDIUM — powerful, requires care

---

## T-Shirt Line

> "MOUNT responsibly. UNMOUNT with love."

---

## Verdict

**POWERFUL PERSONALITY MODIFICATION. APPROVE.**

Overlay skills. Create zones. Cure with memory.

But check compatibility first.
