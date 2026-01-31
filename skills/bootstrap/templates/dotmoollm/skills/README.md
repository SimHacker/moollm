# Skill User Profile Templates

This directory contains **templates** for skill-specific user configuration.

## The Pattern

```
.moollm/skills/<skill-name>/
├── config.yml     # User settings (from template)
├── token.txt      # Cached credentials (gitignored)
├── cache/         # Skill-specific cached data
└── state.yml      # Skill runtime state
```

## Why This Pattern?

1. **Gitignored by default** — credentials never committed
2. **Per-project isolation** — different settings per repo
3. **Override hierarchy** — user preferences > project defaults > skill defaults
4. **Self-documenting** — templates explain what each setting does

## Override Hierarchy

```
Priority (highest wins):

  5. COMMAND LINE       --ha-token "xyz"
     ↑
  4. ENVIRONMENT        export MOOLLM_HA_TOKEN="xyz"
     ↑
  3. USER GLOBAL        ~/.moollm/skills/<skill>/config.yml
     ↑
  2. PROJECT            .moollm/skills/<skill>/config.yml    ← THIS DIR
     ↑
  1. SKILL DEFAULTS     skills/<skill>/defaults.yml
```

## How to Use

### 1. Copy Template

```bash
# From project root:
mkdir -p .moollm/skills/home-assistant
cp /path/to/moollm/skills/bootstrap/templates/dotmoollm/skills/home-assistant/config.yml \
   .moollm/skills/home-assistant/config.yml
```

### 2. Customize

Edit the config.yml, uncommenting sections you need:

```yaml
# Only change what you need — everything else uses defaults

home_assistant:
  url: "http://192.168.1.100:8123"  # Your local IP

auth:
  method: "file"
  token_file: "token.txt"
```

### 3. Add Credentials

```bash
# From 1Password:
op item get "Home Assistant" \
  --field "Long-Lived Access Token" \
  > .moollm/skills/home-assistant/token.txt

# Or just paste directly:
echo "your-token-here" > .moollm/skills/home-assistant/token.txt
```

### 4. Verify Gitignore

Make sure `.moollm/` is in your `.gitignore`:

```gitignore
# MOOLLM user profiles (contain secrets)
.moollm/
```

## Available Templates

| Skill | Template | Purpose |
|-------|----------|---------|
| **TEMPLATE.yml** | Generic | Base template — copy for new skills |
| **home-assistant/** | HA config | Home Assistant API connection |

## Template Structure

Every template should include:

```yaml
# Header explaining location and purpose
# ═══════════════════════════════════════

schema_version: 1

# Override hierarchy documentation
# ─────────────────────────────────────

# Auth section (common pattern)
auth:
  method: "file"
  token_file: "token.txt"
  
# Skill-specific sections
# (documented inline)

# Setup commands
setup:
  cache_token: |
    # Command to populate credentials
    
  test_connection: |
    # Command to verify it works

# Evolution examples
# ═══════════════════════════════════════
# Show how config has grown over time
# Helps users understand migration paths
```

## Adding a New Skill Template

1. Create `templates/dotmoollm/skills/<skill-name>/config.yml`
2. Follow the structure from `TEMPLATE.yml`
3. Document all settings with examples
4. Include setup commands
5. Update this README

## Philosophy

> **The template IS the schema.**
> 
> Instead of a separate JSON Schema, the template file documents itself
> with comments. Users copy it and uncomment what they need. The comments
> ARE the documentation.

This is "YAML Jazz" — comments carry semantic meaning.
