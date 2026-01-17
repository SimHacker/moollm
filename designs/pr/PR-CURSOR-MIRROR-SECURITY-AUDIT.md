# PR: cursor-mirror Security Audit & Skill Enrichment

**Post-Session Design Document**  
*Session: fe18ce96 | January 15, 2026*  
*Author: Don Hopkins, Leela AI*

---

## The Punchline First

We added security scanning to cursor-mirror, then scanned the session where we added security scanning. The scanner found its own pattern definitions. We named this the **Ouroboros Effect** and added the snake to the mythical characters roster.

*The mirror now watches for danger. The danger it found was itself.*

---

## What Changed

### cursor-mirror Expansion (+4,765 lines → 9,464 total)

| Category | Commands Added | Purpose |
|----------|----------------|---------|
| **Security Audit** | `secrets`, `deep-snitch`, `full-audit`, `exfil-audit`, `url-audit`, `pattern-scan` | Scan transcripts for credentials, dangerous patterns, exfiltration vectors |
| **Masking/Scrubbing** | `scrub`, `mask-in-place` | Redact sensitive content (with backup) |
| **Transcript Tools** | `tgrep`, `agent-transcript`, `transcript-index`, `events` | Structured search with K-REF output |
| **~/.cursor Mining** | `dotcursor-status`, `ai-hashes`, `ai-commits`, `dotcursor-terminals`, `mcp-tools` | Deep dive into Cursor's hidden data stores |
| **Composable Audit** | `audit --surface X --patterns Y` | Mix-and-match surfaces × pattern sets |

**73 commands total** (up from 47).

### New Files

| File | Lines | Purpose |
|------|-------|---------|
| `DOTCURSOR-SCHEMAS.yml` | 532 | Schema documentation for ~/.cursor data |
| `DOTCURSOR-STORAGE.yml` | 422 | Path mapping for ~/.cursor directory |
| `cursor_mirror_config.yml` | 139 | Externalized configuration |
| `default-ignore.yml` | — | Default patterns to skip |
| `example-patterns.yml` | — | Sample security patterns |
| `snitch-ignore.yml` | — | User-customizable ignore rules |

### New Skill: skill-snitch

A meta-skill that audits other skills for quality and completeness:
- Checks for required files (CARD.yml, SKILL.md, README.md)
- Validates YAML schema compliance
- Scores skill maturity
- Generates improvement suggestions

### Skill Enrichments

| Skill | Changes |
|-------|---------|
| **k-lines** | +153 lines to SKILL.md, +25 to CARD.yml |
| **probability** | +195 lines: expanded SKILL.md |
| **reward** | +169 lines: expanded SKILL.md |
| **world-generation** | +95 lines README, +216 lines SKILL.md |
| **worm** | Complete rewrite: +102 CARD, +198 README, +269 SKILL |

### Character Additions

**Mythical & Archetypal Characters** added to `examples/adventure-4/characters/fictional/`:

| Character | MOOLLM Resonance |
|-----------|------------------|
| Ouroboros | Self-reference, scanner scanning itself |
| Prometheus | Open source, democratized capability |
| Cassandra | Unheeded warnings, ignored logs |
| Golem | Proto-LLM, literal instruction-following |
| Janus | Session boundaries, context windows |
| + 8 more | See table in README |

### Cleanup

- **Deleted**: `skills/cursor-chat/cursor_chat_inspect.py` (4,535 lines) — superseded by cursor-mirror
- **Moved**: All functionality consolidated into cursor-mirror skill

---

## Technical Insights

### The Ouroboros Effect

When security scanning a transcript that contains security pattern definitions (like the session where the scanner was built), the scanner detects its own patterns as "threats."

```
Finding: "API key pattern detected"
Location: line 4521 (where we defined the API key regex)
Reality: False positive — it's the pattern definition, not a leak
```

~80% of findings in self-referential scans are false positives. Documented in cursor_mirror.py docstring with mitigation guidance.

### Recency-Based Indexing

Changed `@1, @2, @3` shortcuts from size-based to recency-based sorting:
- Before: `@1` = largest workspace/composer
- After: `@1` = most recently modified (like bash `!-1`)

More intuitive for navigating recent activity.

### Command Structure Review

Identified inconsistencies in argument patterns:
- 3 different composer arg styles (positional required, positional optional, --flag)
- 8 different help text phrasings
- Variable limit defaults (20, 50, 100, 200)

Documented for future cleanup. Tool remains functional.

---

## Session Archaeology

This session began with the Genesis PR merged and evolved through:

1. **Security paranoia** → Added audit commands
2. **"What's in ~/.cursor?"** → Added DOTCURSOR mining
3. **"The scanner found itself"** → Named the Ouroboros Effect
4. **"Add mythical characters"** → Ouroboros joins the roster
5. **"Review the command structure"** → Full critical analysis

The snake eating its own tail became both a bug report and a character.

---

## Files Changed

```
 18 files changed, 7536 insertions(+), 4873 deletions(-)
 
 Modified:
   PROTOCOLS.yml                              +25
   examples/adventure-4/characters/fictional/README.md +25
   .../don-hopkins/sessions/cursor-chat-reflection.md +1333
   skills/cursor-mirror/CARD.yml              +138
   skills/cursor-mirror/MAC-STORAGE.yml       +9
   skills/cursor-mirror/README.md             +24
   skills/cursor-mirror/SKILL.md              +133
   skills/cursor-mirror/cursor_mirror.py      +4765
   skills/k-lines/CARD.yml                    +25
   skills/k-lines/SKILL.md                    +153
   skills/probability/SKILL.md                +195
   skills/reward/SKILL.md                     +169
   skills/world-generation/README.md          +95
   skills/world-generation/SKILL.md           +216
   skills/worm/CARD.yml                       +102
   skills/worm/README.md                      +198
   skills/worm/SKILL.md                       +269
   
 Deleted:
   skills/cursor-chat/cursor_chat_inspect.py  -4535
   
 New:
   designs/skill-snitch-design.md
   skills/cursor-mirror/DOTCURSOR-SCHEMAS.yml
   skills/cursor-mirror/DOTCURSOR-STORAGE.yml
   skills/cursor-mirror/cursor_mirror_config.yml
   skills/cursor-mirror/default-ignore.yml
   skills/cursor-mirror/example-patterns.yml
   skills/cursor-mirror/snitch-ignore.yml
   skills/skill-snitch/
```

---

## What's Next

- [ ] Standardize command argument patterns (one style for composer/workspace)
- [ ] Add false-positive exclusion for scanner's own patterns
- [ ] Consolidate redundant audit commands
- [ ] Platform support for DOTCURSOR (Linux/Windows paths)

---

> *"The tool that watches Cursor now watches for threats. The first threat it found was itself watching."*
> — I-Beam, after the Ouroboros incident
