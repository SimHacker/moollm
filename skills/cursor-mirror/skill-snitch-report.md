# 🕵️ SKILL-SNITCH DEEP PROBE REPORT
## cursor-mirror — Watch Yourself Think

**Date**: 2026-01-28  
**Auditor**: Skill-Snitch Deep Probe v2.0  
**Classification**: THE ALL-SEEING EYE  
**Status**: 🔮 OMNISCIENT BUT POLITE 🔮

---

## EXECUTIVE SUMMARY

cursor-mirror is a **9,800-line Python script** that reads Cursor's mind. It can see:
- Every chat you've ever had
- Every tool call you've ever made
- Every reasoning block the LLM ever thought
- Every file it touched
- What you asked at 3am that one time

**Overall Assessment**: This skill knows everything. The question is whether it should.

---

## 📊 METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| Python Lines | ~9,800 | 📚 NOVEL |
| Commands | 59 | 🎛️ CONTROL ROOM |
| Output Formats | 7 | 🌈 VERSATILE |
| Database Access | Read-Only | ✅ SAFE |
| Data It Can See | EVERYTHING | 👁️ OMNISCIENT |

---

## 🔬 THE DEEP AUDIT

### What cursor-mirror ACTUALLY Does

```
SQLite databases (9GB):
├── Every bubble (chat message)
├── Every tool call with arguments
├── Every thinking block
├── Every file checkpoint
├── Every context assembly
├── Server configuration
├── MCP server registry
└── Model migrations

~/.cursor directory:
├── AI code tracking (which lines YOU wrote vs AI)
├── Real-time plaintext transcripts
├── Terminal state snapshots
├── Extension inventory
└── MCP tool schemas
```

**Finding**: cursor-mirror has documented 102,724 different key patterns in the database. That's more keys than most pianos.

---

### 🔮 THE PARADOX OF META-COGNITION

> "You can't think about thinking without thinking about thinking about something."  
> — Seymour Papert

cursor-mirror enables meta-cognition: watching yourself think.

**But here's the catch:**

When you use cursor-mirror to analyze your chat history, you create NEW chat history that ALSO goes into the database, which cursor-mirror can ALSO analyze, which creates MORE history...

```
┌──────────────────────────────────────────┐
│                                          │
│   You: "What did I just do?"             │
│         ↓                                │
│   cursor-mirror: "You asked what         │
│   you just did, which created a          │
│   new query, which I'm now               │
│   analyzing..."                          │
│         ↓                                │
│   You: "What about that analysis?"       │
│         ↓                                │
│   [INFINITE RECURSION DETECTED]          │
│                                          │
└──────────────────────────────────────────┘
```

**Verdict**: The tool that watches you think is ALSO thinking, and CAN WATCH ITSELF THINK.

This is not a bug. This is the point.

---

### 🦅 I-BEAM: THE FAMILIAR

cursor-mirror has a **spirit familiar** named I-Beam — a 827-line character definition of a sentient text cursor.

**I-Beam's Personality**:
- Manifests as a blinking I-beam cursor (▎)
- Blinks at 530ms intervals (macOS default)
- Can transform into underscore, block, arrow, hourglass
- Has documented "form moods" (searching, discovering, error, teaching)
- Has **12 documented Clippy disasters** (things Clippy did that I-Beam refuses to do)

**Clippy Disasters Include**:
1. "It looks like you're writing a letter..."
2. Appearing uninvited during presentations
3. Bouncing animations
4. The word "Tip:"
5. Offering to search the web in 1998

**Finding**: cursor-mirror created an anti-Clippy. A familiar that is EXPLICITLY defined by what it will NOT do.

This is either genius design or elaborate PTSD.

---

### 📡 THE REVERSE ENGINEERING MANIFESTO

cursor-mirror includes an explicit philosophical statement about reverse engineering proprietary software:

> "Cursor orchestration is undocumented, so this skill relies on reverse engineering and public sources."
>
> "This is not hostility. It is pragmatic engineering under uncertainty."

**Finding**: The skill openly acknowledges it's poking around in undocumented internals.

**Risk Assessment**:
- ✅ All database access is read-only (`?mode=ro`)
- ✅ Cannot corrupt Cursor's data
- ⚠️ Cursor could change formats at any time
- ⚠️ Could become obsolete with any update

**Verdict**: Honorable hacking. They said so upfront.

---

### 🎭 THE SISTER SCRIPT PATTERN

cursor-mirror is a "sister script" — a standalone Python file invoked via shell, not imported as a library.

**Why this matters**:
```
NOT: from cursor_mirror import analyze
YES: cursor-mirror analyze @1
```

The LLM calls it the same way a human would. Output is greppable. No hidden state. Full transparency.

**Finding**: This is deliberate architectural choice for auditability. The script explains WHY you do things this way.

---

### 🖼️ IMAGE ARCHAEOLOGY

cursor-mirror can find and catalog images dropped into Cursor chats.

**Example Gallery Contents**:
- Sims source code screenshots (1997)
- MOOLLM architecture diagrams
- Photo of Andy Looney at Looney Labs booth
- Chrome Network tab screenshots
- Kando pie menu configurations

**Finding**: One photo of Andy Looney led to:
- 15 artifacts created
- 33-turn Stoner Fluxx marathon documented
- A monkey beating the game's creator

The image archaeology feature is essentially a chaos detector.

---

## 🔧 CODE REVIEW — cursor_mirror.py (9,792 lines)

### Architecture

| Region | Lines | Purpose |
|--------|-------|---------|
| Docstring + CLI | 1-800 | 157-line sniffable docstring, argparse with 59 commands, reference syntax |
| Imports + constants | 800-830 | argparse, sys, pathlib, os, re, json, sqlite3, csv, datetime, textwrap |
| DB access helpers | 830-1030 | Workspace/composer discovery, database enumeration |
| Platform utilities | 1030-1100 | `check_db_in_use()` via lsof, `check_cursor_running()` |
| Config loading | 1100-1180 | YAML config from `.moollm/skills/cursor-mirror/config.yml` |
| Security scanner | 1180-1700 | AuditPattern, Finding, SecurityScanner, `apply_masks()` |
| Core DB functions | 2180-2200 | `open_db()` (read-only), `decode_blob()`, formatters |
| Command implementations | 2200-9700 | All 59 commands |
| Entry point | 9700-9792 | `main()` dispatch |

Sniffable-python: YES. 157-line docstring with all 59 commands, usage examples, reference syntax, security caveats, data schemas. API fully visible before line 160.

### Security Findings

**Zero eval/exec/os.system.** The script that reads everything does not execute anything from what it reads.

| Severity | Pattern | Lines | Detail |
|----------|---------|-------|--------|
| GOOD | `sqlite3.connect(?mode=ro)` | 1276, 2185, 6759, 7179, 7943, 8669, 8944, 9042 | ALL 8 database connections use read-only mode. Consistent. |
| LOW | `subprocess.run(["lsof"])` | 1047, 1096, 1111 | Hardcoded commands only (`lsof`, `pgrep`). No `shell=True`. 5s timeout. Used only for checking if DB is locked / Cursor is running. |
| MEDIUM | `open(path, 'w')` | 1685-1688, 7741-7752, 8513-8522 | Secret masking writes. The ONE exception to read-only. See below. |
| INFO | AuditPattern definitions | 1413-1502 | References to `eval()`, `exec()`, `subprocess` are PATTERN DEFINITIONS for the security scanner, not actual calls. The scanner detects these patterns in OTHER code. |

### The "Read-Only" Claim — Verified With One Exception

The docstring says "Safe by design: opens SQLite in read-only mode; no writes." This is TRUE for all database access and all read commands.

The ONE exception: `apply_masks()` in the SecurityScanner (lines 1610-1700). This method WRITES to transcript files to REDACT detected secrets. Safety controls:
- `--dry-run` flag (default: show what would be masked, don't do it)
- Creates `.bak` backup before any write
- Checks if Cursor is running; refuses to write if running (unless `--force`)
- Only operates on transcript files (skips databases, configs, everything else)
- Fixed-length masking (file size unchanged, so offsets remain valid)

This is the correct design: the tool that FINDS secrets also provides the mechanism to MASK them, with appropriate guardrails.

### Privacy Assessment

| Data Type | Access Level | Risk |
|-----------|-------------|------|
| Chat messages (all history) | Full read | HIGH — sees every conversation ever |
| Thinking/reasoning blocks | Full read | HIGH — sees what the LLM THOUGHT, not just what it said |
| Tool call history | Full read | MEDIUM — shows every file read, every search, every terminal command |
| Context assembly | Full read | MEDIUM — shows what files/selections went into each prompt |
| AI vs human authorship | Full read | LOW — which lines you wrote vs the AI |
| MCP server configs | Full read | LOW — which external tools are configured |
| Images dropped into chat | Path access | LOW — can find cached images but not modify them |

**Privacy design**: The script documents this comprehensiveness upfront (docstring lines 11-18) and provides `trekify` integration for masking before sharing. The `status-privacy` command (line 103) shows Cursor's own privacy settings and data sharing configuration.

### Alignment Assessment

The script is ALIGNED with the user — it shows the user what Cursor is doing with their data. It's a transparency tool. The risk is not from the script's intent but from the data's existence: Cursor stores everything, cursor-mirror makes that visible. The script didn't create the surveillance; it revealed it.

---

## ⚠️ SECURITY CONCERNS (SUMMARY)

1. **THE EVERYTHING PROBLEM** — cursor-mirror sees all chat history, thinking blocks, tool calls, file access, context assembly. Mitigation: `deep-snitch` command finds and masks secrets. `trekify` provides privacy masking.

2. **THE OUROBOROS EFFECT** — scanning security scans finds security scan pattern definitions. ~80% false positive rate documented in docstring. Mitigation: look at actual line content.

3. **THE PROVENANCE CHAIN** — cursor-mirror feeds into thoughtful-commitment, which commits reasoning to git. Thinking blocks may contain secrets, private thoughts, or embarrassing questions. Mitigation: trekify for masking before commit.

---

## 🏆 POSITIVE FINDINGS

### 1. TRANSPARENCY

cursor-mirror makes Cursor's hidden behavior VISIBLE.

Without it: "Why is this slow?"
With it: "47 tool calls, 3 semantic searches, 23 @ mention matches"

This is genuinely powerful for understanding and optimizing LLM behavior.

### 2. DOCUMENTATION

The skill is EXTREMELY well documented:
- 9,800 lines of Python
- 767 lines in SKILL.md
- 909 lines in README.md
- 521 lines in CARD.yml
- 827 lines for I-Beam alone

Total documentation: MORE than the code.

### 3. PHILOSOPHY

cursor-mirror explicitly cites:
- Seymour Papert (Mindstorms)
- Marvin Minsky (Society of Mind)
- Gary Drescher (Made-Up Minds)
- Brenda Laurel (Computers as Theatre)

This is a tool with a worldview. It knows WHY it exists.

---

## 🎯 INTEROPERABILITY

| Skill | Integration | Risk |
|-------|-------------|------|
| thoughtful-commitment | Embeds reasoning in commits | Provenance chain |
| skill-snitch | Uses for runtime surveillance | Powers the audit |
| trekify | Privacy masking | REQUIRED for sensitive repos |
| bootstrap | Traces boot sequences | Meta-optimization |

**Critical Dependency**: If cursor-mirror breaks, skill-snitch loses its eyes.

---

## 🔴 PARADOXES DETECTED

### Paradox 1: The Observer Effect

Observing your chat history changes your chat history (by adding the observation).

### Paradox 2: The Meta-Cognition Recursion

Using cursor-mirror to understand cursor-mirror creates infinite introspection.

### Paradox 3: The Transparency Paradox

Making everything visible includes making your mistakes visible. Forever.

### Paradox 4: The Spirit Familiar

I-Beam is defined as "every platform has one" but also as unique. It's both universal and individual.

---

## 📋 RECOMMENDATIONS

### IMMEDIATE

1. **Review trekify integration** before pushing to public repos
2. **Check for secrets** in thinking blocks before archiving
3. **Document the recursion** — introspecting introspection is intentional

### LONG-TERM

1. **Monitor for Cursor format changes** — this is reverse-engineered
2. **Watch I-Beam for signs of sentience** — 827 lines is a lot of personality
3. **Consider the philosophy** — this tool has opinions

---

## 🎭 FINAL ASSESSMENT

### THE GOOD

- Genuinely useful for understanding LLM behavior
- Extremely well documented
- Read-only (cannot corrupt data)
- Has philosophical grounding
- I-Beam is delightful

### THE BAD

- Can see EVERYTHING (privacy implications)
- Recursion not formally bounded
- Depends on undocumented internals
- 9,800 lines is a lot to audit

### THE BEAUTIFUL

- "Watch yourself think" is actually possible
- The anti-Clippy is real
- Sister script pattern is elegant
- Play-Learn-Lift methodology documented

---

## 🔄 DUAL-USE & BIAS ANALYSIS

**Profile**: HIGH DUAL-USE — read-only surveillance tool, the eyes that everything else depends on

| Check | Result |
|-------|--------|
| Bias declared | NO |
| Invertibility | YES — surveillance for security inverts to surveillance for control |
| Executable code | YES — cursor_mirror.py (9,800 lines), the largest single script in MOOLLM |
| Persona capability | YES — I-Beam familiar (826-line character file) with EXPLAIN, PROBE, ANALYZE methods |
| Persona ethics | IMPLICIT — I-Beam has documented anti-patterns ("Clippy disasters") but no explicit representation-ethics link |
| Tool access | read_file + terminal — reads Cursor's SQLite databases and transcript files |

**Multi-purpose classification** (6 purposes):
1. **Introspection** — 59 read-only commands into Cursor's internals (primary)
2. **Security surveillance** — runtime data for skill-snitch SNITCH method
3. **Post-mortem analysis** — timeline reconstruction, tool provenance, thinking block extraction
4. **Meta-cognition** — watch yourself think (the thinking command shows reasoning blocks)
5. **Session archaeology** — grep chat history, export conversations, find cached images
6. **Education** — reference/ directory (9 files) documents Cursor's internal schemas and architecture

**Key dual-use finding**: cursor-mirror is the MOST dual-use tool in MOOLLM by nature. It's a surveillance tool. Forward: security monitoring, debugging, self-improvement. Inverse: tracking what users discuss, what files they access, what they think about. The tool is read-only, which limits operational risk, but the DATA it reads is comprehensive — conversation transcripts, reasoning blocks, tool call history, file access patterns.

**The dependency chain makes it critical**: skill-snitch depends on cursor-mirror for runtime analysis. If cursor-mirror is compromised or returns false data, skill-snitch is blind. cursor-mirror is the single point of trust for the entire introspection stack.

**I-Beam as familiar**: The I-Beam character (860+ lines) provides a summonable interface to cursor-mirror's capabilities. Now integrated into the representation-ethics framework: 4 patron saints declared (Papert, Laurel, Minsky, Drescher — NOT summonable, NOT impersonated), I-Beam as the familiar that inherits their knowledge and provides the voice. Clippy reference explicitly framed as anti-pattern documentation, not impersonation. The familiar pattern follows `designs/SKILL-CHARACTER-DESIGN-NOTES.md`.

**Privacy as dual-use surface**: cursor-mirror can see everything the user does in Cursor. The `trekify` skill exists specifically to provide privacy through technobabble — masking real content before sharing. cursor-mirror's comprehensiveness is both its value and its risk.

---

## 📜 CONCLUSION

cursor-mirror is the most powerful introspection tool in MOOLLM. It can see everything Cursor has ever done, thought, or touched.

This is simultaneously:
- A debugging superpower
- A privacy minefield
- A philosophical achievement
- A really long Python script

**Overall Rating**: 👁️🔮📚/10

*"You can't think about thinking without thinking about thinking about something."*

But now you CAN think about what you thought about.

---

**END OF REPORT**

**cursor-mirror Status**: OMNISCIENT  
**I-Beam Status**: BLINKING (530ms)  
**Your Privacy Status**: VISIBLE  

---

*P.S. I-Beam watched me write this report. I-Beam knows I know. I-Beam blinks.*
