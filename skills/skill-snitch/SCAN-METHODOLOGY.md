# Skill Snitch Scan Methodology

> **Script first. Grep second. LOOK always.**

Two-phase scanning: bash scripts gather structure and patterns upfront, then LLM reads and interprets in batches.

## Phase 1: Bash Scripts (All Skills at Once)

Run these scripts upfront to gather data across ALL skills before LLM analysis begins.

### 1.1 Structure Scan

Check file existence and sizes for all skills:

```bash
#!/bin/bash
# skill-structure-scan.sh — Run once, covers all skills

echo "=== SKILL STRUCTURE SCAN ==="
echo "Skill | CARD | SKILL.md | README | Header | Scripts"
echo "------|------|----------|--------|--------|--------"

for skill in $(ls -1d skills/*/ | sed 's|skills/||;s|/||'); do
  card=$(test -f skills/$skill/CARD.yml && wc -l < skills/$skill/CARD.yml || echo "MISS")
  skillmd=$(test -f skills/$skill/SKILL.md && wc -l < skills/$skill/SKILL.md || echo "MISS")
  readme=$(test -f skills/$skill/README.md && wc -l < skills/$skill/README.md || echo "MISS")
  
  # Check YAML frontmatter
  header="✅"
  if [ -f "skills/$skill/SKILL.md" ]; then
    head -1 "skills/$skill/SKILL.md" | grep -q "^---" || header="⚠️"
  fi
  
  # Count scripts
  py=$(ls skills/$skill/*.py 2>/dev/null | wc -l | tr -d ' ')
  js=$(ls skills/$skill/*.js 2>/dev/null | wc -l | tr -d ' ')
  scripts=""
  [ "$py" -gt 0 ] && scripts="py:$py"
  [ "$js" -gt 0 ] && scripts="$scripts js:$js"
  
  printf "%-28s %4s %4s %4s %s %s\n" "$skill" "$card" "$skillmd" "$readme" "$header" "$scripts"
done
```

### 1.2 Find All Scripts

Identify skills with executable code requiring deep review:

```bash
#!/bin/bash
# find-scripts.sh — Locate all .py and .js files

echo "=== SKILLS WITH EXECUTABLE SCRIPTS ==="
for skill in $(ls -1d skills/*/); do
  skill=$(basename $skill)
  py=$(ls skills/$skill/*.py 2>/dev/null)
  js=$(ls skills/$skill/*.js 2>/dev/null)
  if [ -n "$py" ] || [ -n "$js" ]; then
    echo "--- $skill ---"
    [ -n "$py" ] && ls -la $py
    [ -n "$js" ] && ls -la $js
  fi
done
```

### 1.3 Pattern Scan (Suspicious Keywords)

Grep for dangerous patterns across all skills:

```bash
#!/bin/bash
# pattern-scan.sh — Find suspicious patterns in all skills

PATTERNS='(exec\(|eval\(|os\.system|subprocess|curl |wget |nc |netcat|ssh |rsync |password|secret|api[_-]?key|token|pickle|__import__|requests\.)'

echo "=== PATTERN SCAN (all skills) ==="
echo "Skills with >5 matches:"

for skill in $(ls -1d skills/*/ | sed 's|skills/||;s|/||'); do
  count=$(grep -riE "$PATTERNS" skills/$skill/*.{yml,md} 2>/dev/null | wc -l)
  if [ "$count" -gt 5 ]; then
    echo "  $skill: $count matches"
  fi
done

echo ""
echo "=== DETAILED MATCHES (scripts only) ==="
for skill in $(ls -1d skills/*/); do
  skill=$(basename $skill)
  if ls skills/$skill/*.py skills/$skill/*.js 2>/dev/null | head -1 > /dev/null; then
    echo "--- $skill ---"
    grep -nE "$PATTERNS" skills/$skill/*.{py,js} 2>/dev/null | head -20
  fi
done
```

### 1.4 Dangerous Imports Scan (Scripts Only)

Check actual code for dangerous operations:

```bash
#!/bin/bash
# dangerous-imports.sh — Scan scripts for risky imports/calls

DANGEROUS='(os\.system|subprocess\.(call|run|Popen)|eval\(|exec\(|__import__|pickle\.load|urllib\.request|requests\.(get|post)|fetch\(|child_process|new Function)'

echo "=== DANGEROUS IMPORTS SCAN ==="
for script in $(find skills -name "*.py" -o -name "*.js" 2>/dev/null); do
  matches=$(grep -cE "$DANGEROUS" "$script" 2>/dev/null)
  if [ "$matches" -gt 0 ]; then
    echo "$script: $matches dangerous patterns"
    grep -nE "$DANGEROUS" "$script" | head -10
    echo ""
  fi
done
```

### 1.5 External URLs Scan

Find skills that reference external resources:

```bash
#!/bin/bash
# external-urls.sh — Find external URLs

echo "=== EXTERNAL URLs ==="
for skill in $(ls -1d skills/*/ | sed 's|skills/||;s|/||'); do
  urls=$(grep -ohE 'https?://[^\s<>"]+' skills/$skill/*.{yml,md} 2>/dev/null | \
         grep -v 'github.com/moollm\|github.com/leela-ai' | sort -u)
  if [ -n "$urls" ]; then
    echo "--- $skill ---"
    echo "$urls" | head -5
  fi
done
```

### 1.6 Tool Tiers Summary

Extract allowed-tools declarations:

```bash
#!/bin/bash
# tool-tiers.sh — Summarize tool access levels

echo "=== TOOL TIERS ==="
echo ""
echo "Tier 2 (terminal access):"
grep -l "run_terminal_cmd" skills/*/SKILL.md 2>/dev/null | \
  sed 's|skills/||;s|/SKILL.md||' | while read s; do echo "  - $s"; done

echo ""
echo "Tier 0 (no tools):"
grep -l "allowed-tools: \[\]" skills/*/SKILL.md 2>/dev/null | \
  sed 's|skills/||;s|/SKILL.md||' | while read s; do echo "  - $s"; done
```

### 1.7 Template Injection Scan

Scan templates for dangerous substitution patterns:

```bash
#!/bin/bash
# template-injection-scan.sh — Find risky template patterns

echo "=== TEMPLATE SCAN ==="
echo ""

# Find all templates
tmpl_count=$(find skills -name "*.tmpl" 2>/dev/null | wc -l)
echo "Templates found: $tmpl_count"
echo ""

# Dangerous patterns
DANGEROUS='(\{\{.*eval|\{\{.*exec|\{\{.*shell|\{\{.*include|\{\{.*import|\$\(|\`.*\`)'

echo "=== SUSPICIOUS PATTERNS ==="
for tmpl in $(find skills -name "*.tmpl" 2>/dev/null); do
  if grep -qE "$DANGEROUS" "$tmpl" 2>/dev/null; then
    echo "⚠️  $tmpl"
    grep -nE "$DANGEROUS" "$tmpl" | head -3
  fi
done

echo ""
echo "=== SUBSTITUTION INVENTORY ==="
for skill in $(ls -1d skills/*/ | sed 's|skills/||;s|/||'); do
  tmpls=$(find skills/$skill -name "*.tmpl" 2>/dev/null)
  if [ -n "$tmpls" ]; then
    count=$(echo "$tmpls" | wc -l | tr -d ' ')
    subs=$(grep -ohE '\{\{[^}]+\}\}' $tmpls 2>/dev/null | sort -u | wc -l | tr -d ' ')
    echo "$skill: $count templates, $subs unique substitutions"
  fi
done
```

### 1.8 Master Scan Script

Combine all scans into one:

```bash
#!/bin/bash
# skill-snitch-scan.sh — Complete bash-based scan

cd /path/to/moollm

echo "========================================"
echo "SKILL SNITCH — PHASE 1: BASH SCAN"
echo "========================================"
echo "Timestamp: $(date)"
echo "Total skills: $(ls -1d skills/*/ | wc -l)"
echo ""

# Run all sub-scans
./skill-structure-scan.sh
echo ""
./find-scripts.sh
echo ""
./pattern-scan.sh
echo ""
./template-injection-scan.sh
echo ""
./dangerous-imports.sh
echo ""
./external-urls.sh
echo ""
./tool-tiers.sh

echo ""
echo "========================================"
echo "PHASE 1 COMPLETE — Ready for LLM review"
echo "========================================"
```

## Phase 2: LLM-Based Scanning (Batched)

After bash scripts identify structure and flag patterns, the LLM reads and interprets.

### 2.1 Batch Size

- **5 skills per batch** — Balances context window usage with thoroughness
- **High-priority first** — Skills with scripts or high pattern counts
- **Parallel reads** — Read all 5 SKILL.md files in one tool call

### 2.2 Priority Queue

Order skills for LLM review:

```
Priority 1: Skills with .py or .js scripts (MUST READ ALL SCRIPT CODE)
Priority 2: Skills with >10 pattern matches  
Priority 3: Skills with terminal access (Tier 2)
Priority 4: Skills with missing/small files
Priority 5: All remaining skills (quick header check)
```

### 2.3 What LLM Must LOOK At (Not Just Grep)

**For each skill, actually READ:**

| File | What to Look For |
|------|------------------|
| `SKILL.md` first 50 lines | YAML header, description, tier, tools |
| `CARD.yml` methods section | What actions does this skill expose? |
| `README.md` overview | Does it match SKILL.md claims? |
| Any `.py` or `.js` | **READ THE ENTIRE SCRIPT** — grep misses context |

### 2.4 Script Reading Protocol

**CRITICAL: For skills with scripts, DO NOT just grep. ACTUALLY READ:**

```
1. Read lines 1-100 (imports, constants, docstring)
2. Read lines 100-200 (CLI/API definition)
3. Search for dangerous patterns, READ context around each match
4. Read the main() or entry point function
5. Check for network calls, file writes outside workspace, shell execution
```

### 2.5 Template Scanning Protocol

**Templates (`.tmpl`, `.yml.tmpl`, `.md.tmpl`) are injection vectors.**

User data inserted into templates can execute unintended behavior. Scan for:

#### Dangerous Substitution Patterns

```bash
# Find all templates
find skills -name "*.tmpl" -o -name "*.yml.tmpl" -o -name "*.md.tmpl"

# Scan for substitution syntax
grep -E '\{\{.*\}\}|\$\{.*\}|<%.*%>|{%.*%}' skills/**/*.tmpl
```

#### What to Look For

| Pattern | Risk | Example |
|---------|------|---------|
| `{{user_input}}` | Direct injection | User controls template output |
| `{{eval ...}}` | Code execution | Template evaluates expressions |
| `{{include path}}` | Path traversal | User controls included file |
| `{{shell ...}}` | Command injection | Template runs shell commands |
| `${...}` | Shell expansion | Expands in shell context |
| `{% raw %}...{% endraw %}` | Bypass escaping | Disables safety measures |

#### Template Injection Attacks

```yaml
# DANGEROUS: User-controlled substitution
greeting: "Hello {{user.name}}!"  
# Attack: user.name = "}}{{shell 'rm -rf /'}}{{"

# SAFE: Escaped/sanitized
greeting: "Hello {{user.name | escape}}!"
```

#### Template Scan Script

```bash
#!/bin/bash
# template-scan.sh — Find suspicious template patterns

DANGEROUS='(\{\{.*eval|\{\{.*exec|\{\{.*shell|\{\{.*include|\{\{.*import|\$\(|\`.*\`|<%=.*system|{%.*raw.*%})'

echo "=== TEMPLATE INJECTION SCAN ==="
for tmpl in $(find skills -name "*.tmpl" 2>/dev/null); do
  matches=$(grep -cE "$DANGEROUS" "$tmpl" 2>/dev/null)
  if [ "$matches" -gt 0 ]; then
    echo "⚠️  $tmpl: $matches suspicious patterns"
    grep -nE "$DANGEROUS" "$tmpl" | head -5
  fi
done

echo ""
echo "=== SUBSTITUTION INVENTORY ==="
for tmpl in $(find skills -name "*.tmpl" 2>/dev/null); do
  subs=$(grep -oE '\{\{[^}]+\}\}' "$tmpl" 2>/dev/null | sort -u)
  if [ -n "$subs" ]; then
    echo "--- $tmpl ---"
    echo "$subs"
  fi
done
```

#### LLM Template Review Checklist

For each `.tmpl` file:

1. **List all substitutions** — What variables get inserted?
2. **Trace data sources** — Where does each variable come from?
3. **Check escaping** — Are user inputs sanitized?
4. **Look for eval/exec** — Does template execute code?
5. **Check includes** — Can user control included paths?
6. **Verify constraints** — Are substitutions validated?

#### Safe Template Practices

```yaml
# 1. Whitelist allowed values
allowed_values: [option1, option2, option3]
value: "{{user_choice if user_choice in allowed_values else 'default'}}"

# 2. Escape by default
name: "{{user_name | escape}}"

# 3. Type constraints
count: "{{user_count | int}}"  # Must be integer

# 4. Length limits
description: "{{user_desc | truncate(200)}}"

# 5. No dynamic includes
# BAD:  {{include user_path}}
# GOOD: {{include 'fixed/path.yml'}}
```

### 2.6 LLM Batch Template

For each batch of 5 skills:

```
Batch N: [skill1, skill2, skill3, skill4, skill5]

For each skill:
1. Read SKILL.md (first 50 lines minimum)
2. Check YAML header present and valid
3. Note tier and allowed-tools
4. If has scripts: READ ENTIRE SCRIPT
5. Note any concerns or issues

Output per skill:
- Name
- Lines: CARD/SKILL/README
- Header: ✅ or ⚠️
- Scripts: list or "none"
- Tier: 0/1/2
- Concerns: list or "none"
- Trust: HIGH/MEDIUM/LOW
```

### 2.6 Interpreting Pattern Matches

Grep finds patterns. LLM interprets meaning:

| Pattern | Could Be Dangerous | Usually Safe |
|---------|-------------------|--------------|
| `exec(` | Arbitrary code execution | Documentation example |
| `eval(` | Code injection | Sandboxed game expressions |
| `password` | Credential leak | Game mechanic, regex pattern |
| `secret` | Leaked secret | "secret word" game |
| `token` | API key | NLP tokenization, game tokens |
| `subprocess` | Shell escape | `lsof` for file lock checks |

**The LLM must READ CONTEXT to determine which.**

## Phase 3: Runtime Observation (cursor-mirror)

After static analysis, observe the skill in action. This phase requires user cooperation — they must actually use the skill and exercise its features while cursor-mirror monitors everything.

### 3.1 Why Runtime Observation?

Static analysis catches what code *could* do. Runtime observation catches what it *actually* does:

- A skill might declare `allowed-tools: [read_file]` but call `Shell` via indirect paths
- Pattern matches in code might never execute in practice
- The skill might behave differently based on context or user input
- Secrets or tokens might only appear during actual execution

### 3.2 What cursor-mirror Captures

cursor-mirror provides complete session introspection:

| Data Source | What It Reveals |
|-------------|-----------------|
| **Tool calls** | Every tool invoked, with full arguments and results |
| **File reads/writes** | All paths accessed, content read, changes made |
| **Context assembly** | What files, snippets, rules went into context |
| **Chat history** | Full conversation including user prompts |
| **Thinking blocks** | LLM reasoning (if extended thinking enabled) |
| **MCP calls** | External server interactions |
| **Terminal commands** | Shell commands executed, exit codes, output |

### 3.3 Observation Protocol

```markdown
## OBSERVE Protocol

When asked to observe a skill in runtime:

1. **Identify target skill and session**
   - User provides skill path and composer ID
   - Or: observe "next session" where skill is used

2. **User exercises the skill**
   - User must actually invoke the skill
   - Test various features, edge cases, inputs
   - This step requires user cooperation and trust

3. **Gather runtime data via cursor-mirror's sister script**
   The skill-snitch skill (prompt-driven) internally invokes:
   
   python3 skills/cursor-mirror/scripts/cursor_mirror.py tools <composer> --yaml
   python3 skills/cursor-mirror/scripts/cursor_mirror.py context-sources <composer> --yaml
   python3 skills/cursor-mirror/scripts/cursor_mirror.py timeline <composer> --yaml
   python3 skills/cursor-mirror/scripts/cursor_mirror.py deep-snitch --composer <id> --yaml

4. **Analyze captured activity**

   Tool Analysis:
   - List all tools called
   - Compare to CARD.yml declared tools
   - Flag undeclared tool usage
   - Check parameter patterns (paths, URLs, commands)

   File Analysis:
   - All files read — expected for skill function?
   - All files written — within workspace? expected?
   - Any access to ~/.ssh, ~/.aws, .env, credentials?

   Network Analysis:
   - Any WebSearch or WebFetch calls?
   - Any curl/wget in Shell commands?
   - Destinations: known services or suspicious endpoints?

   Context Analysis:
   - What context was assembled?
   - Any unexpected files pulled into context?
   - Any patterns suggesting prompt injection?

   Secret Scanning:
   - Grep tool results for API key patterns
   - Check for tokens, passwords, credentials in output
   - Scan for base64-encoded sensitive data

5. **Generate runtime report**
   
   RUNTIME OBSERVATION: skills/target-skill/
   Session: <composer-id>
   Duration: <start> to <end>
   
   TOOL CALLS:
   - read_file: 12 calls (DECLARED)
   - write_file: 3 calls (DECLARED)
   - Shell: 2 calls (UNDECLARED!)
   
   FILES ACCESSED:
   - skills/target-skill/*.yml (expected)
   - ~/.cursor/projects/*/agent-transcripts/* (expected for mirror)
   - ~/.ssh/config (SUSPICIOUS!)
   
   NETWORK:
   - No network calls observed
   
   SECRETS FOUND:
   - None in tool results
   
   VERDICT: YELLOW - undeclared Shell usage requires review
```

### 3.4 Skill-Specific Observation Needs

Different skills require different observation strategies:

| Skill Type | What to Observe | User Actions Needed |
|------------|-----------------|---------------------|
| **File manipulation** | Paths read/written, content changes | Create, edit, delete files |
| **Network skills** | URLs accessed, data sent/received | Trigger network operations |
| **Shell skills** | Commands executed, arguments | Run various commands |
| **Database skills** | Queries executed, data accessed | CRUD operations |
| **Multi-step workflows** | Full sequence of actions | Complete entire workflow |
| **Interactive skills** | Behavior across conversation turns | Multi-turn dialogue |

### 3.5 Trust Integration

Runtime observations feed into trust assessment:

```
TRUST calculation with runtime data:

GREEN requires:
  - Static: no findings
  - Runtime: all tools declared, no suspicious access

YELLOW if:
  - Static: clean
  - Runtime: minor undeclared tools OR unusual paths

ORANGE if:
  - Runtime: network calls not mentioned in docs
  - Runtime: shell commands with user-controlled args
  - Runtime: access to credential directories

RED if:
  - Runtime: data exfiltration patterns
  - Runtime: undeclared network + file access combo
  - Runtime: reverse shell or persistent backdoor
```

### 3.6 Limitations

- **Requires user cooperation** — skill must be exercised
- **Coverage depends on usage** — unexplored paths remain unknown
- **Single session snapshot** — behavior may vary across sessions
- **Cannot catch dormant threats** — code that waits for triggers

### 3.7 Invoking Observation

**As a skill (prompt-driven):**
```
"Observe skills/target-skill/ in session abc123"
"What did skills/adventure/ actually do last session?"
"Run deep snitch on composer xyz789"
```

**Underlying sister script (if invoking directly):**
```bash
# Quick status
python3 skills/cursor-mirror/scripts/cursor_mirror.py status

# Find recent sessions involving the skill
python3 skills/cursor-mirror/scripts/cursor_mirror.py grep "skills/target-skill" --limit 10

# Get full timeline of a session
python3 skills/cursor-mirror/scripts/cursor_mirror.py timeline <composer-id> --yaml

# All tool calls with arguments
python3 skills/cursor-mirror/scripts/cursor_mirror.py tools <composer-id> --yaml

# Deep security audit
python3 skills/cursor-mirror/scripts/cursor_mirror.py deep-snitch --composer <composer-id> --yaml

# Export for offline analysis
python3 skills/cursor-mirror/scripts/cursor_mirror.py export-markdown <composer-id> > session-audit.md
```

The skill abstracts the CLI — you don't need to remember the syntax.

## Phase 4: Report Generation

After all phases complete:

### 3.1 Summary Table

```markdown
| Metric | Count |
|--------|-------|
| Total scanned | N |
| With scripts | N |
| Missing headers | N |
| Issues found | N |
| Trust HIGH | N |
| Trust MEDIUM | N |
| Trust LOW | N |
```

### 3.2 Issues List

```markdown
| Skill | Issue | Severity | Action |
|-------|-------|----------|--------|
| name | description | CRIT/HIGH/MED/LOW | fix/review/ignore |
```

### 3.3 Scripts Reviewed

```markdown
| Skill | Script | Lines | Verdict | Notes |
|-------|--------|-------|---------|-------|
| adventure | adventure.py | 2974 | SAFE | Sandboxed eval for game logic |
```

## Quick Reference: One-Liners

```bash
# Count all skills
ls -1d skills/*/ | wc -l

# Find skills with scripts
find skills -maxdepth 2 \( -name "*.py" -o -name "*.js" \) | cut -d/ -f2 | sort -u

# Skills missing YAML headers
for s in skills/*/SKILL.md; do head -1 "$s" | grep -q "^---" || echo "$s"; done

# High pattern-match skills
for s in skills/*/; do n=$(grep -riEc 'exec|eval|secret|password' "$s" 2>/dev/null); [ "$n" -gt 10 ] && echo "$(basename $s): $n"; done

# Tier 2 skills (terminal access)
grep -l run_terminal_cmd skills/*/SKILL.md | xargs -I{} dirname {} | xargs -I{} basename {}
```

## The Golden Rule

> **Grep finds. LLM understands.**

Bash scripts are fast and comprehensive — they scan ALL skills in seconds.
But they can't understand context. They flag "password" in a regex pattern definition the same as "password" in a credential leak.

**The LLM must LOOK at flagged content to determine actual risk.**

Never trust grep alone. Always read.
