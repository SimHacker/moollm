# skill-creator — Deep Probe + MOOLLM Integration Notes

> NOT importing as a new skill. MOOLLM's `skill` skill already does this, better. But there's protein to extract.

**Trust**: GREEN | **Scripts**: 3 (init_skill.py, package_skill.py, quick_validate.py) | **Total**: ~386 lines

## What It Does

Meta-skill that guides skill creation: understand → plan → initialize → edit → package → iterate. Three scripts handle scaffolding, packaging (.skill zip), and validation.

## Code Review

| Script | Lines | Convention Issues |
|--------|-------|-------------------|
| init_skill.py | 215+ | No argparse (raw sys.argv with `--path` hack). No type hints. Large template strings inline. Uses `Path(path).resolve()` (CWD-independent). |
| package_skill.py | 92 | No argparse. Default output is `Path.cwd()` (CWD-dependent). No `--json` output. |
| quick_validate.py | 79 | No argparse. Dead import (`os` never used). Uses `yaml.safe_load`. Frontmatter-only validation (shallow). |

## What To Steal for MOOLLM `skill` Skill

### 1. Degrees-of-Freedom Framework

```yaml
# Worth adding to CARD.yml schema for all skills
freedom:
  high: "Text instructions — LLM interprets intent"
  medium: "Pseudocode — LLM follows pattern" 
  low: "Specific script — LLM runs deterministic code"
```

Each method in a CARD.yml could declare its freedom level. This tells the LLM how much creative latitude it has. Low-freedom methods get scripts. High-freedom methods get empathic-templates.

### 2. Three-Resource-Type Convention

```
scripts/     — executable code (run, don't read)
references/  — context docs (read, don't run)
assets/      — output files (use in output, never load into context)
```

Some MOOLLM skills already follow this (groceries: scripts/ah.py, templates/, examples/). Formalizing it in `skill` SKILL.md as a recommended convention would standardize directory layout.

### 3. Anti-Patterns List

Anthropic's skill-creator explicitly says "What NOT to include: no README.md, no INSTALLATION_GUIDE.md, no CHANGELOG.md." We agree about INSTALLATION_GUIDE and CHANGELOG — those don't belong in skill dirs. But we respectfully disagree about README.md. In MOOLLM, README.md is the deepest level of the Semantic Image Pyramid (GLANCE → CARD → SKILL → README) — it's the "why was it built?" context for developers and curious readers. It's optional, loaded only when needed, but valuable when present. MOOLLM's skill skill should document anti-patterns for what NOT to put in a skill directory — but README isn't one of them.

### 4. quick_validate.py Structural Pre-Check

Could complement skill-snitch with a fast structural check: frontmatter exists, name is valid hyphen-case, description present, no unexpected keys. Skill-snitch does deep security analysis; this does quick lint.

## What NOT to Steal

- `init_skill.py` scaffolding — MOOLLM's `CREATE` method with empathic-templates is more powerful
- `.skill` packaging format — MOOLLM distributes via git, not zip files
- The template TODOs — MOOLLM uses `{{describe_purpose}}` empathic-templates instead of `[TODO]` markers
