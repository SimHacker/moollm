# Namespacing Skills

## The Problem

Flat `skills/` directory doesn't scale:
- 100+ skills = chaos
- No logical grouping
- No ambient behavior for categories
- Can't scope permissions or effects by domain

## The Solution

Break `skills/` into category subdirectories with optional ROOM.yml files.

```
skills/
  meta/
    ROOM.yml            # Meta-skills ambient behavior
    moollm/
    bootstrap/
    k-lines/
    
  writing/
    ROOM.yml            # Writing room ambiance
    no-ai-slop/
    no-ai-gloss/
    no-ai-hedging/
    sister-script/
    
  character/
    ROOM.yml            # Character creation context
    incarnation/
    voice/
    personality/
    
  game/
    ROOM.yml            # Game mechanics zone
    adventure/
    room/
    buff/
    mount/
    
  deliberation/
    ROOM.yml            # Serious thinking mode
    adversarial-committee/
    debate/
    evaluator/
    
  security/
    ROOM.yml            # High-trust zone
    skill-snitch/
    deep-snitch/
    audit/
    
  satire/
    ROOM.yml            # Satirical mode engaged
    no-ai-overlord/
    no-ai-customer-service/
    no-ai-soul/
    acme/
```

## Category as Room

Each category can have a `ROOM.yml` that defines:

```yaml
# skills/writing/ROOM.yml
name: Writing Workshop
description: "Skills for quality writing and editing"

mount:
  skill: writing-discipline
  params:
    clarity: high
    verbosity: low
    
ambiance:
  - "Focus on craft"
  - "Every word earns its place"
  - "Cut the fluff"
  
entering_message: |
  You enter the Writing Workshop.
  The air smells of red ink and determination.
  A sign reads: "NO SLOP ZONE"
  
permissions:
  can_edit: true
  can_create: true
  requires_review: false
  
exports:
  # Skills available for mounting elsewhere
  - no-ai-slop
  - no-ai-gloss
  - sister-script
```

## Ethical Scoping

Categories can enforce ethical boundaries:

```yaml
# skills/security/ROOM.yml
name: Security Sanctum
description: "High-trust security skills"

mount:
  skill: security-mindset
  
permissions:
  requires_trust_level: high
  audit_all_actions: true
  no_external_calls: true
  
entering_message: |
  ⚠️ SECURITY ZONE
  All actions logged. Think carefully.
  
forbidden:
  - external network access
  - credential exposure
  - unaudited file writes
```

```yaml
# skills/satire/ROOM.yml
name: Satire Factory
description: "Where irony is manufactured"

mount:
  skill: satirical-lens
  
warnings:
  - "Content here is SATIRICAL"
  - "Not for production use without labeling"
  - "May cause confusion if taken literally"
  
entering_message: |
  🎭 SATIRE ZONE
  Everything here is a joke. Even this warning.
  Especially this warning.
```

## Namespace Resolution

Skill references can be:

```yaml
# Fully qualified
skill: game/adventure

# Category-relative (when inside category)
skill: ./adventure

# Search path (finds first match)
skill: adventure

# Multiple matches = error, must qualify
skill: meta/bootstrap    # not game/bootstrap
```

## Search Path

Configure search order in `.moollm/config.yml`:

```yaml
skill_search_path:
  - .moollm/skills/       # Local overrides first
  - skills/meta/          # Meta always available
  - skills/writing/       # Frequently used
  - skills/game/
  - skills/               # Fallback to root scan
```

## Inheritance

Categories can inherit from parent categories:

```yaml
# skills/writing/editing/ROOM.yml
name: Editing Suite
inherits: ../ROOM.yml    # Inherits Writing Workshop mounts

mount:
  - skill: red-pen-mode
  - skill: track-changes
```

## Character-Style Organization

Just like characters have skill subdirs, categories ARE skill subdirs:

```
characters/minsky/skills/     → Minsky's personal skills
skills/deliberation/          → Deliberation category skills

# Same structure, same rules
# Categories are just skills without a character
```

## Room Effects When Browsing

When you `cd skills/satire/`:

```
> cd skills/satire/

🎭 Entering: Satire Factory
Mount activated: satirical-lens

Available skills:
  - no-ai-overlord      (SIMULATE AI OVERLORD)
  - no-ai-customer-service  (AGGRESSIVE HELPFULNESS)
  - no-ai-soul          (CORPORATE SOULLESSNESS)
  - acme               (EVERYTHING FAILS IRONICALLY)
  
Warning: Content here is SATIRICAL
```

## INDEX.yml Updates

Each category needs an INDEX.yml:

```yaml
# skills/writing/INDEX.yml
category: writing
description: "Quality writing skills"

skills:
  no-ai-slop:
    purpose: "Eliminate filler"
    maturity: stable
    
  no-ai-gloss:
    purpose: "Remove vague abstractions"
    maturity: stable
    
  sister-script:
    purpose: "Doc-first automation"
    maturity: experimental
```

## Migration Path

1. Create category directories
2. Add ROOM.yml to each
3. Move skills to categories
4. Update INDEX.yml files
5. Add symlinks for backwards compat (optional)
6. Update skill references in examples

## Benefits

| Before | After |
|--------|-------|
| Flat list of 100+ skills | Organized categories |
| No ambient context | Categories have mood/rules |
| No ethical scoping | Permissions per category |
| Hard to discover | Browse like rooms |
| No inheritance | Category → subcategory inheritance |

## Relationship to MOOFS

MOOFS layers apply per-category:

```
LOCAL: .moollm/skills/writing/no-ai-slop/  (my override)
CATEGORY: skills/writing/no-ai-slop/       (category version)
BASE: skills/no-ai-slop/                   (original flat location)
```

Top wins. Local overrides category overrides base.

## Open Questions

1. **Symlinks for migration?** Keep `skills/no-ai-slop` → `skills/writing/no-ai-slop`?
2. **Multi-category skills?** Can a skill live in multiple categories?
3. **Dynamic categories?** Create categories on the fly?
4. **Category permissions?** Who can add skills to `security/`?

---

*"Categories are rooms. Skills live in rooms. Rooms have rules."*
