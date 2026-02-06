# Trail of Bits — Security Skills (Non-Blockchain)

> Professional security toolbox. 20 non-blockchain skills. The sharp-edges cognitive framework and audit-context-building anti-hallucination rules are gold.

**Author**: Trail of Bits | **License**: Various | **Relevant skills**: 20 (3 blockchain skipped)

## Priority Skills for skill-snitch / MOOLLM

### P0 — Directly Applicable

| Skill | What | Key Value |
|-------|------|-----------|
| **static-analysis** | CodeQL + Semgrep + SARIF integration | Multi-tool security scanning in one package |
| **semgrep-rule-creator** | Test-driven Semgrep rule authoring | Custom pattern detection — parallel to skill-snitch patterns/*.yml |
| **insecure-defaults** | Detect fail-open configs, hardcoded secrets, weak crypto | Directly applicable to skill scanning |
| **sharp-edges** | Three-adversary model for API misuse detection | Cognitive framework for skill-snitch pattern design |

### P1 — High Value

| Skill | What | Key Value |
|-------|------|-----------|
| **constant-time-analysis** | Compiler-induced timing side-channel detection | Real CVE-class finds. Standalone Python tool with pyproject.toml |
| **audit-context-building** | Ultra-granular pre-audit context with anti-hallucination rules | Methodology for deep code review — anti-hallucination is critical for LLM-based analysis |
| **variant-analysis** | Find similar bugs after initial discovery | Progressive generalization (exact → abstract → generic) |
| **differential-review** | Git-based security review with blast radius estimation | 7-phase workflow, modular docs for token efficiency |
| **yara-authoring** | Behavior-driven YARA-X detection rule authoring | Malware detection — directly complements skill-snitch IOC patterns |

### P2 — Useful Reference

| Skill | What |
|-------|------|
| **firebase-apk-scanner** | Active scanning (50KB bash script probes Firebase endpoints) |
| **testing-handbook-skills** | Meta-generator for 16 appsec sub-skills from Trail of Bits handbook |
| **semgrep-rule-variant-creator** | Cross-language rule porting |
| **fix-review** | Verify fix commits address audit findings |
| **property-based-testing** | Hypothesis/fast-check/proptest across 7 languages |
| **burpsuite-project-parser** | Search Burp Suite project files |
| **dwarf-expert** | DWARF debug info format expertise |
| **modern-python** | uv + ruff + ty + pytest best practices |

### Skipped (Blockchain)

ask-questions-if-underspecified, culture-index, claude-in-chrome-troubleshooting — utility, not security.
building-secure-contracts, entry-point-analyzer, spec-to-code-compliance — blockchain.

## Key Frameworks Worth Adopting

### The Three-Adversary Model (sharp-edges)

| Adversary | What They Do | skill-snitch Application |
|-----------|-------------|-------------------------|
| **The Scoundrel** | Deliberately exploits APIs and configs | Malware authors, prompt injectors |
| **The Lazy Developer** | Takes shortcuts, copies examples blindly | Skills with copy-paste lineage, minimal customization |
| **The Confused Developer** | Misunderstands APIs, makes honest mistakes | Skills with coherence issues, wrong framework versions |

This maps directly to skill-snitch's trust tiers: Scoundrel → malware, Lazy → caution, Confused → reviewed.

### Anti-Hallucination Rules (audit-context-building)

The audit-context-building skill explicitly tells the LLM: "You are NOT identifying vulnerabilities. You are building context. Do NOT propose fixes. Do NOT rate severity." This is exactly the separation skill-snitch needs between Phase 1 (observation) and Phase 2 (assessment).
