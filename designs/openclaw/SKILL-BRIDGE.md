# Skill Bridge: MOOLLM ↔ OpenClaw Interoperability

> *"A SKILL.md is a SKILL.md. The LLM doesn't care who wrote it."*

**Date:** 2026-02-06
**Status:** Design Document

---

## The Happy Coincidence

MOOLLM and OpenClaw both use `SKILL.md` with YAML frontmatter as their skill format. This is not a coincidence — it's convergent evolution toward the same pattern that Anthropic popularized. The bridge is already half-built.

---

## Format Comparison

### OpenClaw Skill Format

```yaml
---
name: github
description: Interact with GitHub using the gh CLI
emoji: "🐙"
always: false
openclaw:
  skillKey: github
  primaryEnv: GH_TOKEN
  homepage: https://cli.github.com
  requires:
    bins: ["gh"]
    env: ["GH_TOKEN"]
  install:
    - platform: macos
      command: "brew install gh"
    - platform: linux
      command: "curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | ..."
---

# GitHub Skill

Use the `gh` CLI to interact with GitHub.
[... body ...]
```

### MOOLLM Skill Format

```yaml
# skills/github/CARD.yml
name: github
tier: utility

tools:
  required: [shell, read_file]
  optional: [write, search_replace]

methods:
  - name: CREATE-ISSUE
    description: Create a GitHub issue
    parameters:
      - name: title
        type: string
        required: true

advertisements:
  CREATE-ISSUE:
    visibility: public
    trigger: "when user wants to file a bug or feature request"
  CHECK-PR:
    visibility: public
    trigger: "when user asks about pull request status"

dovetails:
  - adventure: "Issues as quests, PRs as diplomatic incidents"
  - character: "Characters can interact with GitHub in their voice"
```

### The Differences

| Aspect | OpenClaw | MOOLLM |
|--------|----------|--------|
| **Metadata** | YAML frontmatter in SKILL.md | Separate CARD.yml |
| **Install info** | `openclaw.install` array | Not applicable (filesystem-based) |
| **Dependencies** | `requires.bins`, `requires.env` | `tools.required` |
| **Discovery** | Flat key match, `always` flag | K-line semantic activation |
| **Advertisements** | Not present | The Sims-style action broadcasting |
| **Dovetails** | Not present | Inter-skill connection map |
| **Ethics** | Not present | Inherited from directory scope |
| **Three files** | SKILL.md only | CARD.yml + SKILL.md + README.md |

---

## The Bridge

### Direction 1: MOOLLM Skill → OpenClaw

A MOOLLM skill becomes an OpenClaw skill by:

1. **Flattening CARD.yml into frontmatter:**

```yaml
# Original MOOLLM CARD.yml
name: church-of-emacs
tier: gameplay
methods:
  - name: BLESS
  - name: CURSE
  - name: RETROGNUIFY
advertisements:
  BLESS: {visibility: public, trigger: "when code is offered for blessing"}

# Becomes OpenClaw SKILL.md frontmatter
---
name: church-of-emacs
description: Blessings and curses from the Church of Emacs
emoji: "🦬"
always: false
---
```

2. **Merging SKILL.md body** — MOOLLM SKILL.md protocol section becomes OpenClaw SKILL.md body verbatim. The LLM reads both formats equally well.

3. **Dropping what OpenClaw can't use** — Advertisements, dovetails, K-line references. These enhance MOOLLM but don't break OpenClaw — they become informative comments.

### Direction 2: OpenClaw Skill → MOOLLM

An OpenClaw skill becomes a MOOLLM skill by:

1. **Extracting CARD.yml from frontmatter:**

```yaml
# OpenClaw frontmatter
---
name: weather
description: Get weather forecasts
emoji: "🌤"
openclaw:
  requires:
    bins: ["curl"]
---

# Becomes MOOLLM CARD.yml
name: weather
tier: utility
tools:
  required: [shell]
methods:
  - name: GET-FORECAST
    description: Get weather for a location
advertisements:
  GET-FORECAST:
    visibility: public
    trigger: "when someone asks about weather"
dovetails:
  - adventure: "Weather affects room descriptions and character comfort"
  - needs: "Weather influences outdoor comfort need"
```

2. **Adding README.md** — OpenClaw skills don't always have separate READMEs. MOOLLM expects one.

3. **Adding dovetails and K-lines** — The MOOLLM-specific connections that make skills compose with the world model.

### The Compiler

A `skill-bridge.py` script that automates conversion:

```python
#!/usr/bin/env python3
"""Convert between MOOLLM and OpenClaw skill formats."""

def moollm_to_openclaw(skill_dir: str) -> str:
    """Read CARD.yml + SKILL.md, emit OpenClaw SKILL.md with frontmatter."""
    card = load_yaml(f"{skill_dir}/CARD.yml")
    skill_body = read_file(f"{skill_dir}/SKILL.md")
    
    frontmatter = {
        "name": card["name"],
        "description": card.get("methods", [{}])[0].get("description", ""),
        "emoji": infer_emoji(card),
        "always": "AMBIENT" in card.get("advertisements", {}),
    }
    
    # OpenClaw-specific metadata
    if card.get("tools", {}).get("required"):
        frontmatter["openclaw"] = {
            "requires": {"bins": card["tools"]["required"]}
        }
    
    return format_skill_md(frontmatter, skill_body)


def openclaw_to_moollm(skill_md_path: str) -> tuple[str, str, str]:
    """Read OpenClaw SKILL.md, emit CARD.yml + SKILL.md + README.md."""
    frontmatter, body = parse_frontmatter(skill_md_path)
    
    card = {
        "name": frontmatter["name"],
        "tier": "utility",  # default, can be overridden
        "tools": {"required": extract_tools(frontmatter)},
        "methods": extract_methods(body),
        "advertisements": infer_advertisements(body),
    }
    
    readme = generate_readme(frontmatter, body)
    skill_md = body  # body passes through as-is
    
    return (dump_yaml(card), skill_md, readme)
```

---

## Skill Ecosystem Comparison

### OpenClaw's 50+ Skills

| Category | Skills | MOOLLM Equivalents |
|----------|--------|--------------------|
| Communication | imsg, discord, slack, telegram, whatsapp | postal, soul-chat |
| Productivity | notion, obsidian, bear-notes, apple-notes | memory-palace, scratchpad |
| Development | github, coding-agent | github, debugging, code-review |
| Media | spotify-player, video-frames, openai-image-gen | visualizer, image-mining |
| System | tmux, peekaboo, 1password | — (no direct equivalent) |
| Location | weather, local-places, goplaces | — (no direct equivalent) |
| Automation | cron (built-in), canvas | action-queue, simulation |

### MOOLLM's 121 Skills That OpenClaw Lacks

| Category | Skills | Why OpenClaw Would Want Them |
|----------|--------|-------------------------------|
| Character | character, persona, incarnation, mind-mirror | Make agents into characters with personality |
| World | adventure, room, object, exit | Spatial navigation for agent memory |
| Ethics | representation-ethics, ontology, hero-story | Safe simulation of real people |
| Sims | advertisement, action-queue, needs, economy | Need-driven autonomous behavior |
| Quality | no-ai-slop, no-ai-gloss, no-ai-sycophancy | Output quality hygiene |
| Deliberation | adversarial-committee, debate, evaluator | Multi-perspective reasoning |
| Memory | memory-palace, honest-forget, summarize | Structured long-term memory |
| Communication | postal (universal addressing) | Address anything: files, YAML keys, line numbers |
| Meta | speed-of-light, empathic-expressions | Performance and expressiveness |

### Skills That Should Be Shared

| Skill | Origin | Shared Because |
|-------|--------|----------------|
| `github` | Both | Both need GitHub interaction |
| `coding-agent` / `code-review` | Both | Both review and write code |
| `weather` | OpenClaw | MOOLLM characters could use weather |
| `spotify-player` | OpenClaw | Characters could control music |
| `no-ai-slop` | MOOLLM | OpenClaw agents need quality control too |
| `adversarial-committee` | MOOLLM | Multi-perspective PR review |
| `postal` | MOOLLM | Universal addressing for OpenClaw tools |

---

## Implementation Priority

| Priority | Skill | Direction | Effort |
|----------|-------|-----------|--------|
| 1 | `church-of-emacs` | MOOLLM → OpenClaw | Low (new skill) |
| 2 | `eval-genius` | MOOLLM → OpenClaw | Low (new skill) |
| 3 | `github-mmorpg` | MOOLLM → OpenClaw | Medium (needs gh integration) |
| 4 | `no-ai-slop` | MOOLLM → OpenClaw | Low (ambient skill) |
| 5 | `weather` | OpenClaw → MOOLLM | Low (add CARD.yml) |
| 6 | `adversarial-committee` | MOOLLM → OpenClaw | Medium (multi-agent) |
| 7 | `skill-bridge.py` | Bridge tool | Medium |
| 8 | Full extension | Both directions | High |

---

## Related Documents

- [ARCHITECTURE-ANALYSIS.md](./ARCHITECTURE-ANALYSIS.md) — OpenClaw architecture
- [INVASION-PLAN.md](./INVASION-PLAN.md) — Strategic deployment plan
- [CHARACTERS-AS-AGENTS.md](./CHARACTERS-AS-AGENTS.md) — Character deployment specs
