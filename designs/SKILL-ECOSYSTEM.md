# 🌐 The MOOLLM Skill Ecosystem

> **Skills are programs. The ecosystem is the package registry.**

---

## The Vision

npm for skills. Docker Hub for skill bundles. Snyk for skill security.

```
┌────────────────────────────────────────────────────────────────┐
│                    SKILL ECOSYSTEM                              │
├─────────────────┬──────────────────┬──────────────────────────┤
│  PUBLICATION    │   DISCOVERY      │   TRUST & CURATION       │
├─────────────────┼──────────────────┼──────────────────────────┤
│  • Git repos    │  • Registry      │  • skill-snitch          │
│  • Skill Forge  │  • INDEX files   │  • Verified publishers   │
│  • Bundle dist  │  • Search/tags   │  • Community review      │
│  • Versioning   │  • MOO-Maps      │  • Trust tiers           │
└─────────────────┴──────────────────┴──────────────────────────┤
                                                                 │
     ┌───────────────────────────────────────────────────────────┘
     │
     ▼
┌────────────────────────────────────────────────────────────────┐
│                    SKILL LIFECYCLE                              │
├─────────────────┬──────────────────┬──────────────────────────┤
│     PLAY        │      LEARN       │       LIFT               │
├─────────────────┼──────────────────┼──────────────────────────┤
│  • Install      │  • Observe       │  • Contribute            │
│  • Experiment   │  • Document      │  • Publish               │
│  • Fork         │  • Pattern match │  • Curate                │
│  • Customize    │  • Audit         │  • Maintain              │
└─────────────────┴──────────────────┴──────────────────────────┘
```

---

## Trust Tiers

Not all skills are equal. The ecosystem needs graduated trust:

### Core Skills (🟢 GREEN)
```yaml
status: Bundled with MOOLLM, audited
location: skills/
examples:
  - moollm       # Self-explanation
  - bootstrap    # Session warmup
  - skill        # Skill creation
  - k-lines      # Activation theory
trust: Implicit — shipped with MOOLLM
```

### Verified Skills (🔵 BLUE)
```yaml
status: Community skills, snitch-verified
location: Published repos with verification
examples:
  - cursor-mirror   # Introspection
  - adventure       # Room-based simulation
  - adversarial-committee
trust: Publisher verified, scan passed
```

### Community Skills (🟡 YELLOW)
```yaml
status: Published, not audited
location: Any git repo
trust: Scan on install, user discretion
warning: "This skill hasn't been verified. Run skill-snitch SCAN before use."
```

### Local Skills (🟠 ORANGE)
```yaml
status: Your personal skills
location: .moollm/skills/
trust: Only you — not shared
use_case: Personal customization, experiments
```

### Ephemeral Skills (⚪ WHITE)
```yaml
status: Generated during session
location: In-context only
persist: false
trust: Dies with session
use_case: One-off compositions, experiments
```

---

## Skill Snitch: The Curator

**skill-snitch** is essential infrastructure for a healthy ecosystem:

### Static Analysis (Before Installation)
```bash
"Scan https://github.com/unknown/cool-skill for security issues"
```

- Pattern grep for secrets, exfiltration, dangerous ops
- Consistency checks (CARD.yml ↔ SKILL.md ↔ code)
- License and provenance verification

### Runtime Surveillance (During Use)
```bash
"Snitch on what cool-skill did in this session"
```

- Compare declared tools vs actual tools used
- Detect undeclared network calls
- Watch for file access outside declared scope

### Trust Assessment (Combined Score)
```yaml
trust_score:
  static: 0.8   # Passed pattern scans
  runtime: 0.6  # Some undeclared file reads
  combined: 0.7 # YELLOW tier
  notes:
    - "Reads ~/.ssh/config (not declared)"
    - "No network exfiltration detected"
```

---

## Skill Compositions

Skills compose. That's the power. The ecosystem enables composition patterns:

### Suites (Related Constraints)

```yaml
# The No-AI-* Suite — constraint skills
no-ai-suite:
  members:
    - no-ai-slop
    - no-ai-bias
    - no-ai-joking
    - no-ai-sycophancy
    - no-ai-hedging
    - no-ai-gloss
    - no-ai-moralizing
    - no-ai-ideology
    - no-ai-customer-service
    - no-ai-overlord
    - no-ai-soul
  effect: "Stark, useful, honest output"
  install: "Load all 11 skills for full effect"
```

### Ensembles (Cooperative Capabilities)

```yaml
# Introspection Ensemble
introspection-ensemble:
  members:
    - cursor-mirror     # Watch yourself think
    - skill-snitch      # Audit skill behavior
    - thoughtful-commit # Link commits to reasoning
  composition: "snitch uses mirror, commit uses mirror"
  effect: "Complete metacognitive loop"
```

### Stacks (Layered Functionality)

```yaml
# Adventure Stack
adventure-stack:
  layers:
    base:
      - room        # Directory as space
      - character   # Entity patterns
      - persona     # Character voice
    simulation:
      - adventure   # Game mechanics
      - soul-chat   # Multi-character dialogue
      - speed-of-light  # Many turns, one call
    meta:
      - play-learn-lift # Methodology
      - game-theory     # Analysis
```

---

## Publication Patterns

### GitHub as Registry

```
github.com/SimHacker/moollm/           # Core skills
github.com/SimHacker/moollm-adventures/ # Adventure skills
github.com/YourName/your-skills/       # Your skills
```

### Skill Bundles

Like Docker images, but for skill sets:

```yaml
# bundle.yml
id: research-assistant
version: 1.0.0
includes:
  - moollm-core          # Base
  - research-notebook    # Notes
  - citation-manager     # References
  - adversarial-committee # Debate
  - sniffable-python     # Code review
config:
  hot.yml: "Research mode defaults"
```

### Versioning

```
skill-name@1.0.0     # Exact version
skill-name@^1.0.0    # Compatible updates
skill-name@main      # Latest development
skill-name@stable    # Production release
```

---

## Discovery: MOO-Maps

The multi-resolution index enables discovery:

### Global INDEX.md

```markdown
# Skill Index (117 skills)

## Foundational
- **moollm** — Self-explanation, navigation
- **bootstrap** — Session warmup
- **k-lines** — Minsky activation patterns

## Methodology  
- **play-learn-lift** — Explore → patterns → share
- **sister-script** — Doc-first automation
- **speed-of-light** — Many turns in one call
...
```

### Per-Skill GLANCE.yml

```yaml
# 5-70 lines, injectable into every prompt
id: cursor-mirror
tagline: "Watch yourself think"
tier: 2
methods: [STATUS, TREE, TOOLS, THINKING]
invoke_when: ["Review past chats", "Debug agent behavior"]
```

### Tags and Search

```yaml
# Registry metadata
tags:
  - introspection
  - security
  - meta
  
search_terms:
  - "watch yourself think"
  - "cursor internals"
  - "sqlite database"
```

---

## Contribution Flow

### Stage Local → Contribute Upstream

```
Your .moollm/skills/my-skill/    (LOCAL)
        │
        ▼ [cursor-mirror STAGE-ADD]
        
skills/my-skill/                 (REPO, staged)
        │
        ▼ [cursor-mirror STAGE-COMMIT]
        
git commit with thoughtful-commit
        │
        ▼ [cursor-mirror STAGE-PR]
        
Pull Request → Community Review → Merge
```

### Curation Loop

```
Community Skill → skill-snitch SCAN → YELLOW tier
        │
        ▼ [Maintainer reviews]
        
skill-snitch AUDIT (deep) + OBSERVE (runtime)
        │
        ▼ [Passes all checks]
        
Promoted to BLUE tier (Verified)
        │
        ▼ [Bundled with MOOLLM release]
        
Promoted to GREEN tier (Core)
```

---

## The Zizek Angle

> *"The structure of the toilet reflects how a culture examines itself."*

German toilets: shelf for inspection before flushing.
French toilets: immediate disposal.
American toilets: ambivalent middle.

**skill-snitch is the German toilet of the skill ecosystem.**

Before you install a skill, you can examine it:
- What does it claim to do? (CARD.yml)
- What tools does it use? (methods)
- What files does it touch? (patterns)
- What has it actually done? (runtime observation)

Most software registries are French toilets — npm install, code runs, hope for the best. skill-snitch enables **hermeneutic inspection**: understanding what you're about to trust.

---

## Roadmap

### Phase 1: Current
- [x] Core skills in `skills/`
- [x] skill-snitch static analysis
- [x] cursor-mirror introspection
- [x] Local `.moollm/skills/` customization

### Phase 2: Registry
- [ ] Central skill registry (like registry.npmjs.org)
- [ ] Versioned skill packages
- [ ] Automated snitch scans on publish
- [ ] Publisher verification

### Phase 3: Ecosystem
- [ ] Skill bundles (like Docker Compose)
- [ ] Skill forge (CI/CD for skills)
- [ ] Community curation
- [ ] Trust chain verification

---

## See Also

- [Speed of Light vs Carrier Pigeon](SPEED-OF-LIGHT-VS-CARRIER-PIGEON.md) — Why skills beat MCP
- [MOOLLM for Hackers](MOOLLM-FOR-HACKERS.md) — Quick tour
- [skill-snitch](../skills/skill-snitch/) — Security auditing
- [cursor-mirror](../skills/cursor-mirror/) — Introspection
- [play-learn-lift](../skills/play-learn-lift/) — Methodology

---

*Skills are programs. The LLM is eval(). Trust is earned.*
