# EXPORTS Protocol

> *Skills that know how to package themselves.*

## Purpose

The EXPORTS protocol enables skills to declare how they can be extracted from the MOOLLM ecosystem and bundled for standalone distribution. This supports:

1. **Alpha releases** — Share specific skills on Hacker News, forums, etc.
2. **Minimal bundles** — Include only what's needed, not the whole ecosystem
3. **Dependency awareness** — Skills know what they need to function
4. **Graceful degradation** — Document what works/breaks outside MOOLLM

## EXPORTS.yml Schema

Every exportable skill can include an `EXPORTS.yml` file:

```yaml
# EXPORTS.yml — How to package this skill for standalone distribution

export:
  name: "skill-name"
  version: "1.0.0"
  tagline: "One-line description"
  
  # Where to get it
  source:
    repo: "leela-ai/moollm"
    path: "skills/skill-name"
    branch: "main"
    
  # What this export produces
  bundle:
    name: "skill-name-bundle"
    format: "tar.gz"
    includes:
      - "skills/skill-name/**"
      - "skills/dependency-1/**"
      - "skills/dependency-2/**"

# Dependency tiers (high to low priority)
dependencies:
  required:
    # MUST include — skill won't work without these
    - skill: "dependency-name"
      reason: "Why it's required"
      
  recommended:
    # SHOULD include — significantly better experience
    - skill: "dependency-name"
      reason: "What it enables"
      
  optional:
    # MAY include — nice-to-have features
    - skill: "dependency-name"
      reason: "What extra features"
      
  ecosystem:
    # NOT included — but work better with full MOOLLM
    - skill: "moollm-feature"
      reason: "What's missing without it"

# Standalone capability assessment
standalone:
  works: true/partial/false
  degradation:
    - feature: "Feature name"
      status: "works | degraded | unavailable"
      reason: "Explanation"
      
  requirements:
    - "Python 3.8+"
    - "Cursor IDE"
    - "macOS/Linux/Windows"

# Export commands
commands:
  bundle: |
    # Shell commands to create the bundle
    tar -czf $BUNDLE_NAME.tar.gz \
      --transform 's|^skills/|cursor-mirror-bundle/skills/|' \
      skills/cursor-mirror \
      skills/skill-snitch \
      ...
      
  install: |
    # How users install after download
    tar -xzf cursor-mirror-bundle.tar.gz
    cd cursor-mirror-bundle
    # Follow README.md

# What to include in the bundle
files:
  readme: "README-EXPORT.md → README.md"  # Renamed at bundle root
  license: "LICENSE"
  skills: [list of skill directories]
```

## Dependency Tiers

### Required (MUST include)
Skills that are absolutely necessary. The primary skill won't function without them.

**Example:** `cursor-mirror` requires no other skills to run its Python script, but `skill-snitch` requires `cursor-mirror` for the `deep-snitch` command.

### Recommended (SHOULD include)
Skills that significantly enhance the experience. The primary skill works without them, but key workflows are missing.

**Example:** `thoughtful-commitment` is recommended for cursor-mirror because it creates the commit workflow that traces back to thinking blocks.

### Optional (MAY include)
Nice-to-have skills that add extra features but aren't core to the primary skill's mission.

**Example:** `trekify` adds privacy masking before sharing transcripts publicly.

### Ecosystem (NOT included, but documented)
Skills that only work within full MOOLLM. Including them wouldn't help standalone users, but they should know what they're missing.

**Example:** `adventure`, `character`, `room` — these are game/narrative skills that use cursor-mirror for introspection but aren't relevant to standalone usage.

## Bundle Structure

```
cursor-mirror-bundle/
├── README.md            # Copied from README-EXPORT.md
├── LICENSE              # MIT
├── MANIFEST.yml         # What's included, versions
├── skills/
│   ├── cursor-mirror/   # Primary skill
│   ├── skill-snitch/    # Required dependency
│   ├── thoughtful-commitment/  # Recommended
│   ├── trekify/         # Optional
│   └── [methodology skills...]
└── docs/
    └── ECOSYSTEM.md     # What you're missing, invitation to full MOOLLM
```

## Usage

### Creating a Bundle

```bash
# From moollm repo root
cd skills/cursor-mirror
cat EXPORTS.yml  # Read the bundle command

# Run the bundle command
tar -czf cursor-mirror-bundle-v1.0.0.tar.gz \
  --transform 's|^|cursor-mirror-bundle/|' \
  -C .. \
  cursor-mirror \
  skill-snitch \
  thoughtful-commitment \
  trekify \
  session-log \
  sister-script \
  sniffable-python \
  play-learn-lift \
  k-lines
```

### Distributing

1. Create GitHub release with the tarball
2. Post link to Hacker News, Cursor forums, etc.
3. Point to the bundle's README.md for instructions

### Installing

```bash
# Download and extract
curl -LO https://github.com/leela-ai/moollm/releases/download/v1.0.0/cursor-mirror-bundle.tar.gz
tar -xzf cursor-mirror-bundle.tar.gz
cd cursor-mirror-bundle

# Read the README
cat README.md

# Use cursor-mirror
python3 skills/cursor-mirror/cursor_mirror.py status
```

## Protocol Symbol

```
EXPORTS
```

Invoke when: Packaging a skill for standalone distribution, creating release bundles.

## See Also

- [skill/SKILL.md](./SKILL.md) — How skills work
- [play-learn-lift/](../play-learn-lift/) — The LIFT stage produces shareable skills
- [sister-script/](../sister-script/) — Scripts that work standalone
