# cursor-mirror file classification

All canonical reverse-engineered and reference material lives **inside this skill** (checked in). Nothing canonical is in a private or gitignored dir. Attribution and dates go **inside files**, not in filenames (no timestamp prefixes).

---

## Our original reverse engineering (Don Hopkins / Leela AI)

| Location | Contents |
|----------|----------|
| **reference/reverse-engineered/storage/** | Platform storage maps: MAC-STORAGE.yml, MAC-CURSOR-APP.yml, WINDOWS-STORAGE.yml, LINUX-STORAGE.yml, DOTCURSOR-STORAGE.yml. Paths, tables, keys, provenance notes. |
| **reference/reverse-engineered/DATA-SCHEMAS.yml** | Bubble, composer, prompt, generation, message_request_context, embedded_objects. Reverse-engineered from globalStorage/workspaceStorage state.vscdb. |
| **reference/reverse-engineered/KEY-CATALOG.yml** | cursorDiskKV + ItemTable key inventory (counts, patterns, schemas). Discovered via SQLite introspection. |
| **reference/reverse-engineered/DOUBLE-BUBBLE.md** | Double-bubble behavior and parsing notes. |
| **reference/reverse-engineered/TOOL-ARGS-MISSING.md** | Tool-argument gaps and transcript format. |
| **reference/reverse-engineered/** (catalogs) | ORCHESTRATION.yml, MODELS.yml, NATIVE-MODULES.yml, CURSOR-EXTENSIONS.yml, EXTERNAL-SERVICES.yml, DOTCURSOR-SCHEMAS.yml, TOOLS-CATALOG.yml — our catalogs and schemas from inspection. |

---

## From others (assimilated)

| Location | Contents |
|----------|----------|
| **reference/assimilated/*.yml** | One file per external project: S2THEND-CURSOR-HISTORY, JBDAMASK-CURSOR-DB-MCP, DAV-ELL-BLINK, VLTANSKY, TON-AI-CORE, etc. Harvest in their terms; cursor-mirror integration notes. |
| **reference/assimilated/BORG-COLLECTIVE-COOKBOOK.yml** | Consolidated cookbook from multiple assimilated sources + KEY-CATALOG + DATA-SCHEMAS. |

---

## Synthesized / design

| Location | Contents |
|----------|----------|
| **reference/universal/** | Universal model: CURSOR-SQLITE-MODEL.yml, model/ (chunk dir), DESIGN, PLAN, FORMAT-ENTOURAGE, DATA-LAYOUT, schema. Synthesized from assimilated + reverse-engineered KEY-CATALOG + DATA-SCHEMAS. |
| **designs/** | ASSIMILATION-PROCESS, REVERSE-ENGINEERED-DIR, VALIDATION-DESIGN, INPUT-OUTPUT-PIPELINE, IDEAS-TODO, etc. |
| **reference/** (top-level harvest/index) | SIBLING-REPOS.md, EXTERNAL-SOURCES.md, EXTERNAL-PROJECTS-COMPARISON.md, FORUM-HARVEST.md, PENDING-SOURCES-CLONE-VS-HTTP.md. |

---

## Skill core (not reverse engineering)

| Location | Contents |
|----------|----------|
| **CARD.yml, SKILL.md, README.md, GLANCE.yml** | Skill interface and protocol. |
| **scripts/cursor_mirror.py** | CLI; 59 commands. |
| **templates/**, **examples/**, **characters/** | Config templates, patterns, I-Beam character. |

---

## Path summary

- **Our reverse-engineered artifacts:** all under `reference/reverse-engineered/` (including `storage/` and the YAML/MD catalogs listed above).
- **Canonical only here:** All of this is in the skill repo; nothing canonical in `.moollm` or other private dirs.
- **Naming:** Descriptive filenames only; attribution and dates in `meta` inside each file (see designs/REVERSE-ENGINEERED-DIR.md).
