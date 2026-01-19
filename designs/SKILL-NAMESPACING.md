# Skill Namespacing & External Import Protocol

> *"NAT for skills. Private addresses inside, public addresses outside."*

## The Problem

**Current state: Symbolic land grab with inevitable collisions.**

When you import an external skill, what happens if it has the same name as yours?

```yaml
# Your repo has:
skills/
  visualizer/       # Your image generation skill

# External repo has:
skills/
  visualizer/       # Their data visualization skill
```

Both skills claim `visualizer`. Both have k-lines that reference it. Both assume they're the only one.

**MCP's solution is crude:**
```
ServerName:tool_name
# "GitHub:create_issue" vs "GitLab:create_issue"
```

This is path prefixing, not namespacing. It doesn't solve:
- How external skill references *each other*
- How to combine skills that reference the same third skill
- How to override/extend without modifying imports

---

## The NAT Analogy

Network Address Translation maps private → public addresses:

```
┌─────────────────────────────────────────────────────────────────┐
│                        YOUR NETWORK                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │ 192.168.1.1 │    │ 192.168.1.2 │    │ 192.168.1.3 │         │
│  │   Device A  │    │   Device B  │    │   Device C  │         │
│  └─────────────┘    └─────────────┘    └─────────────┘         │
│         │                 │                  │                  │
│         └────────────────┬┴──────────────────┘                  │
│                          │                                      │
│                    ┌─────▼─────┐                                │
│                    │ NAT/Router│                                │
│                    │ 24.1.2.3  │  ← Public IP                   │
│                    └─────┬─────┘                                │
│                          │                                      │
└──────────────────────────┼──────────────────────────────────────┘
                           │
                    ┌──────▼──────┐
                    │  INTERNET   │
                    └─────────────┘
```

**Apply to skills:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR MOOLLM REPO                             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ IMPORTED: external-skills/                               │   │
│  │                                                          │   │
│  │  visualizer/        → PRIVATE: still "visualizer"        │   │
│  │  data-mining/       → PRIVATE: still "data-mining"       │   │
│  │                                                          │   │
│  │  (Their internal refs work — they reference each other)  │   │
│  └─────────────────────────────────────────────────────────┘   │
│         │                                                       │
│         │ NAT WRAPPER                                           │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ YOUR NAMESPACE                                           │   │
│  │                                                          │   │
│  │  ext-visualizer     → maps to → external/visualizer      │   │
│  │  ext-data-mining    → maps to → external/data-mining     │   │
│  │                                                          │   │
│  │  visualizer         → YOUR local visualizer (unchanged)  │   │
│  │  data-mining        → YOUR local data-mining (unchanged) │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key insight:** The external skills don't change. They still reference each other by their original names. The NAT wrapper translates at the boundary.

---

## Implementation: Import Cards

Create a **wrapper card** that:
1. Encapsulates the external skill
2. Provides namespace mapping
3. Rewires k-lines explicitly
4. Never modifies the import

### Import Card Structure

```yaml
# skills/imports/ext-visualizer/CARD.yml
#
# Import wrapper for external visualization skill.
# NAT mapping: "ext-visualizer" → external-skills/visualizer

card:
  id: ext-visualizer
  name: "External Visualizer (Data)"
  type: [import, wrapper]
  
  # IMPORT DECLARATION
  imports:
    source: "external-skills/visualizer"
    version: "1.2.0"           # Pin to specific version
    checksum: "sha256:abc..."  # Optional integrity check
    
  # NAMESPACE MAPPING (NAT TABLE)
  namespace:
    # Public name (ours) → Private name (theirs)
    mappings:
      ext-visualizer: visualizer
      ext-data-charts: data-charts
      
    # How to handle their references to other skills
    rewrites:
      # Their "image-mining" → our "ext-image-mining"
      image-mining: ext-image-mining
      # Their "chart-lib" stays internal (not exposed)
      chart-lib: external-skills/chart-lib
      
  # K-LINE BRIDGE
  # Explicitly wire their k-lines to our namespace
  k-lines:
    # They activate → we activate
    forwards:
      DATA-VISUALIZATION: EXT-DATA-VISUALIZATION
      CHART-RENDER: EXT-CHART-RENDER
      
    # We expose these (public interface)
    exports:
      - EXT-DATA-VISUALIZATION
      - EXT-CHART-RENDER
      - EXT-DASHBOARD
      
    # We DO NOT expose these (internal only)
    private:
      - INTERNAL-CACHE
      - DEBUG-MODE
      
  # CONFLICT RESOLUTION
  conflicts:
    # If their skill tries to use OUR "visualizer"
    on_collision: error  # error | warn | shadow | merge
    
  # DELEGATION
  # Route method calls through the wrapper
  methods:
    VISUALIZE:
      delegates_to: external-skills/visualizer#VISUALIZE
      # Optionally transform parameters
      param_map:
        our_param: their_param
```

### Directory Structure

```
skills/
  visualizer/                    # YOUR visualizer
    CARD.yml
    SKILL.md
    
  imports/                       # Import wrappers
    ext-visualizer/              # Wrapper for external
      CARD.yml                   # NAT mapping card
      README.md                  # Why we imported, how to use
      
  external/                      # Actual imported content
    external-skills/             # Git submodule or copy
      visualizer/                # Unmodified external skill
        CARD.yml                 # Their card (untouched)
        SKILL.md                 # Their docs
```

---

## K-Line Resolution Protocol

When a k-line is activated, resolution follows this order:

```yaml
resolution_order:
  1_local:
    description: "Check local skills first"
    path: "skills/{name}/"
    
  2_imports:
    description: "Check import wrappers"
    path: "skills/imports/{name}/"
    note: "Wrapper card handles delegation"
    
  3_external:
    description: "Check external directly (if no wrapper)"
    path: "skills/external/{source}/{name}/"
    warning: "Bypasses namespace protection"
    
  4_global:
    description: "Check global/community skills"
    path: "$GLOBAL_SKILLS/{name}/"
    future: true
```

### Qualified References

When you need to be explicit:

```yaml
# Unqualified — uses resolution order
k-lines:
  related:
    - visualizer              # Resolves to YOUR visualizer

# Qualified — explicit namespace
k-lines:
  related:
    - ext-visualizer          # Resolves to imported wrapper
    - external-skills/visualizer  # Direct reference (bypass NAT)
```

---

## Standalone Operation

**How can MOOLLM skills work outside MOOLLM?**

The key is the **CARD.yml is the interface contract**:

```yaml
# Minimum viable standalone skill
skills/
  my-skill/
    CARD.yml      # Interface: methods, k-lines, dependencies
    SKILL.md      # Protocol: how to use it
    README.md     # Human docs
```

**For standalone operation:**

1. **CARD.yml declares dependencies explicitly**
   ```yaml
   dependencies:
     required:
       - yaml-jazz: ">=1.0"     # Semantic versioning
       - postel: "any"          # Any version
     optional:
       - adventure: ">=4.0"     # Only for game integration
   ```

2. **Missing dependencies get stub behavior**
   ```yaml
   fallbacks:
     yaml-jazz:
       description: "If yaml-jazz unavailable"
       behavior: "Treat comments as comments, not semantic data"
     adventure:
       description: "If adventure unavailable"
       behavior: "Skip game integration, pure skill mode"
   ```

3. **SKILL.md works as prose documentation**
   - Even without MOOLLM runtime, humans can read SKILL.md
   - The protocol is documented, not hidden in code

---

## Import Protocol

### Step 1: Acquire External Skill

```bash
# Option A: Git submodule
git submodule add https://github.com/them/their-skills.git skills/external/their-skills

# Option B: Copy (for modification)
cp -r /path/to/their-skills skills/external/their-skills

# Option C: Symlink (for development)
ln -s /path/to/their-skills skills/external/their-skills
```

### Step 2: Create Import Wrapper

```bash
mkdir -p skills/imports/ext-their-visualizer
```

Create `CARD.yml`:

```yaml
card:
  id: ext-their-visualizer
  type: [import]
  
  imports:
    source: external/their-skills/visualizer
    
  namespace:
    mappings:
      ext-their-visualizer: visualizer
      
  k-lines:
    exports:
      - EXT-THEIR-VISUALIZE
```

### Step 3: Register in INDEX.yml

```yaml
skills:
  # ... your skills ...
  
  - name: ext-their-visualizer
    path: skills/imports/ext-their-visualizer
    description: "Their visualization skill (imported)"
    import_source: external/their-skills/visualizer
    tier: 2
```

### Step 4: Use via Public Name

```yaml
# In your skills, reference via public (mapped) name
k-lines:
  related:
    - { ref: ext-their-visualizer, meaning: "External viz for data" }
```

---

## Collision Handling

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| `error` | Fail on collision | Default, safest |
| `warn` | Log but continue | Development |
| `shadow` | Local wins, external hidden | Override external |
| `merge` | Combine k-lines from both | Dangerous but powerful |

```yaml
# In import card
conflicts:
  on_collision: shadow
  
  # Specific overrides
  overrides:
    - name: VISUALIZE
      local_wins: true
      reason: "We extend their VISUALIZE with our features"
```

---

## The Rewrite Option

Sometimes you WANT to modify imported skills:

```yaml
imports:
  source: external/their-skills/visualizer
  mode: copy              # vs "reference"
  
  # Automated rewrites (safe)
  rewrites:
    # Find/replace in CARD.yml and SKILL.md
    - find: "visualizer"
      replace: "ext-their-visualizer"
    - find: "VISUALIZE"
      replace: "EXT-THEIR-VISUALIZE"
      
  # Manual patches (careful!)
  patches:
    - file: CARD.yml
      diff: |
        @@ -10,1 +10,1 @@
        -  tier: 1
        +  tier: 2
```

**Warning:** This creates a fork. You lose easy updates.

---

## Comparison: NAT vs Rewrite

| Approach | Pros | Cons |
|----------|------|------|
| **NAT (Wrapper)** | Non-invasive, easy updates, clean separation | Indirection, slight complexity |
| **Rewrite (Fork)** | Full control, no wrapper needed | Merge conflicts, maintenance burden |
| **MCP Prefix** | Simple, standard | No internal resolution, crude |

**Recommendation:** NAT wrapper by default. Rewrite only when necessary.

---

## Future: Global Skill Registry

```yaml
# Hypothetical registry
registry:
  url: "https://skills.moollm.org/registry.yml"
  
  search:
    - query: "visualizer"
      results:
        - name: "moollm/visualizer"
          version: "2.1.0"
          description: "AI image generation"
          
        - name: "anthropic/visualizer"
          version: "1.0.0"
          description: "Data visualization"
          
        - name: "openai/visualizer"
          version: "0.9.0"
          description: "Chart rendering"
          
  install:
    command: "moollm install anthropic/visualizer --as ext-visualizer"
    creates:
      - skills/external/anthropic/visualizer/
      - skills/imports/ext-visualizer/CARD.yml
```

---

## K-Lines as the Resolution Mechanism

The key insight: **K-lines ARE the namespace.**

```yaml
# Your skill activates k-lines
k-lines:
  activates:
    - VISUALIZE              # Activates YOUR visualizer's VISUALIZE
    - EXT-VISUALIZE          # Activates imported wrapper's VISUALIZE
    
# Resolution happens at activation time, not declaration time
# The card's k-lines section IS the routing table
```

**Why k-lines work for this:**
1. They're already semantic (meaning, not just name)
2. They're declared explicitly on cards
3. They support synonyms and aliases naturally
4. They're greppable (uppercase, hyphenated)

---

## Example: Importing Claude's Skill

```yaml
# skills/imports/claude-code-review/CARD.yml

card:
  id: claude-code-review
  name: "Claude Code Review (Imported)"
  type: [import, wrapper]
  
  imports:
    source: "https://github.com/anthropic/claude-skills/code-review"
    version: "2025.01"
    
  namespace:
    mappings:
      claude-code-review: code-review
      
    rewrites:
      # Their internal references
      file-reader: claude-file-reader
      diff-parser: claude-diff-parser
      
  k-lines:
    # Their k-lines → our k-lines
    forwards:
      CODE-REVIEW: CLAUDE-CODE-REVIEW
      SUGGEST-FIX: CLAUDE-SUGGEST-FIX
      
    exports:
      - CLAUDE-CODE-REVIEW
      - CLAUDE-SUGGEST-FIX
      
  # If they try to use OUR code-review skill
  conflicts:
    on_collision: shadow  # Theirs is hidden, ours wins
```

---

## Summary

1. **Current state is a land grab** — no formal namespacing, collisions inevitable
2. **NAT wrapper pattern** — import cards translate external → internal names
3. **K-lines are the routing table** — declared on cards, resolved at activation
4. **Never modify imports** — wrapper handles translation
5. **Explicit over implicit** — declare all k-line forwards explicitly
6. **Standalone works** — CARD.yml is self-describing, SKILL.md is prose

The filesystem is the namespace. The card is the router. The k-line is the address.

---

## See Also

- [NAMING.yml](../kernel/NAMING.yml) — Big-endian naming, path variables
- [k-lines/SKILL.md](../skills/k-lines/SKILL.md) — K-line protocol
- [skill/SKILL.md](../skills/skill/SKILL.md) — Skill instantiation
- [PROTOCOLS.yml](../PROTOCOLS.yml) — Protocol symbols

---

*Draft: 2026-01-19*
*Status: Design proposal, not yet implemented*
