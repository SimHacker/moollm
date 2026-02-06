# Security Audit: OpenClaw Agent Surface

> *"The skill-snitch audits. The skill-snitch reports. The skill-snitch does not blink."*

**Date:** 2026-02-06
**Auditor:** MOOLLM skill-snitch (static analysis mode)
**Subject:** OpenClaw v2026.2.4
**Classification:** SCAN (quick static scan)

---

## Executive Summary

OpenClaw has a **mature security posture** for a personal AI assistant. It uses detect-secrets, pre-commit hooks, SSRF protection, Docker sandboxing, and DM pairing for untrusted senders. However, as a system that gives AI agents access to messaging channels, browser control, and file system operations, the attack surface is significant.

**Overall Security Score:** 7/10 (declared bias: I am biased toward defense-in-depth)

---

## Trust Boundaries

```
UNTRUSTED                    TRUST BOUNDARY              TRUSTED
─────────                    ──────────────              ───────

External messages ──────────> DM Pairing Gate ────────> Agent Runtime
  (WhatsApp, Telegram,         (REQUIRED for              (pi-mono)
   Discord, Slack, etc.)        untrusted senders)           │
                                                              │
                                                              ├──> File System
                                                              ├──> Shell (sandbox?)
                                                              ├──> Browser (Playwright)
                                                              ├──> GitHub (gh CLI)
                                                              ├──> Network (web-fetch)
                                                              └──> Messaging (reply)
```

### Boundary 1: Message Ingestion

| Channel | Auth Model | Risk |
|---------|-----------|------|
| WhatsApp | Phone number + Baileys (unofficial) | **Medium** — Baileys is reverse-engineered |
| Telegram | Bot token + grammY | **Low** — official API |
| Discord | Bot token + discord.js | **Low** — official API |
| Slack | Bot token + @slack/bolt | **Low** — official API |
| Signal | signal-cli bridge | **Medium** — CLI bridge, maintenance risk |
| iMessage | macOS native bridge | **Medium** — platform-specific, macOS only |
| Matrix | matrix-sdk | **Low** — federated protocol, well-studied |
| MS Teams | Bot Framework | **Low** — Microsoft managed |
| WebChat | Built-in HTTP | **Medium** — exposed to internet |

### Boundary 2: Agent Runtime

The agent runtime (pi-mono) executes LLM-generated actions. Trust assumptions:

| Trust Decision | Implementation | Risk |
|----------------|---------------|------|
| Agent sees all messages | Per-sender session isolation | **Low** — isolation is good |
| Agent has file system access | Workspace scoped | **Medium** — scope enforcement unclear |
| Agent has shell access | Via tools | **High** — command injection possible |
| Agent has browser | Playwright | **Medium** — SSRF via navigation |
| Agent has network | web-fetch with guards | **Low** — SSRF protection present |

### Boundary 3: Skill Loading

Skills are loaded from three locations:
1. Bundled (shipped with install) — **Trusted**
2. Managed (`~/.openclaw/skills`) — **Semi-trusted** (user-installed)
3. Workspace (`<workspace>/skills`) — **User-controlled** (lowest trust)

**Risk:** A malicious skill in workspace overrides a bundled skill. Workspace skills win conflicts. This is by design (flexibility) but creates a supply-chain risk if workspaces are shared.

---

## Security Mechanisms

### What OpenClaw Does Well

| Mechanism | Implementation | Effectiveness |
|-----------|---------------|---------------|
| **Secret scanning** | detect-secrets v1.5.0, 27 plugins | **Strong** — comprehensive |
| **Pre-commit hooks** | shellcheck, detect-secrets, oxlint, oxfmt | **Strong** — catches early |
| **DM pairing** | Required for untrusted senders | **Strong** — blocks strangers |
| **SSRF protection** | web-fetch tool guards | **Good** — blocks private IPs |
| **Docker sandbox** | Optional per-session containers | **Excellent** — full isolation |
| **Non-root Docker** | Dockerfile runs as `node` user | **Good** — limits container escape |
| **Credential management** | No secrets in repo, env-based | **Good** — standard practice |
| **CI security** | zizmor, workflow-sanity | **Good** — GH Actions hardening |
| **Dependency security** | pnpm overrides for CVEs | **Good** — proactive patching |

### What Could Be Improved

| Gap | Risk | Recommendation |
|-----|------|----------------|
| **Skill provenance** | No signing, no checksums | Add skill hash verification |
| **Skill sandboxing** | Skills run in agent context | Consider per-skill permission model |
| **Agent action logging** | Session JSONL exists but no audit trail | Add structured audit log |
| **Rate limiting** | No mention of per-channel rate limits | Add message rate limits per sender |
| **Content filtering** | Agent trusts message content | Add content safety layer |
| **Baileys risk** | WhatsApp via unofficial library | Monitor for API changes/bans |
| **Workspace override** | Workspace skills override bundled | Add skill pinning mechanism |

---

## MOOLLM Integration Security Considerations

### Character Injection Risks

When MOOLLM characters become OpenClaw agents, new risks emerge:

| Risk | Scenario | Mitigation |
|------|----------|------------|
| **Character hijacking** | User manipulates character via prompt injection | SOUL.md should include injection resistance |
| **Cross-channel leak** | Character shares info from one channel on another | Session isolation per channel |
| **Persona confusion** | Character breaks character, reveals system info | Strong persona boundaries in SOUL.md |
| **Ethics bypass** | User tricks character into violating ethical framework | representation-ethics skill as guardrail |
| **Impersonation claims** | Character mistaken for real person | 🎭 prefix, tribute protocol, clear disclaimers |
| **Action escalation** | Character convinced to perform dangerous actions | Tool permission limits per character |

### Skill-Snitch Recommendations for MOOLLM Skills

Any MOOLLM skill deployed to OpenClaw should pass these checks:

```yaml
skill_snitch_scan:
  checks:
    - name: "no-shell-injection"
      pattern: "subprocess|os.system|exec\\("
      severity: critical
      
    - name: "no-network-exfiltration"
      pattern: "requests\\.get|fetch\\(|urllib"
      severity: high
      
    - name: "no-credential-access"
      pattern: "env\\[|environ|getenv|password|secret|token"
      severity: high
      
    - name: "no-file-escape"
      pattern: "\\.\\./|/etc/|/home/|expanduser"
      severity: medium
      
    - name: "declares-bias"
      pattern: "bias.*declared|declare.*bias"
      severity: low  # Church of Eval Genius compliance
      required: true
```

### Agent Permission Model

Each MOOLLM character should have explicit permissions:

```yaml
# Character permission matrix
permissions:
  stigniucius:
    messaging: [send, reply]           # Can send and reply
    github: [read, comment, label]     # Can read, comment, label issues
    github_write: [create_issue]       # Can create issues
    github_deny: [merge, delete]       # Cannot merge or delete
    filesystem: [read_workspace]       # Read own workspace only
    shell: deny                        # No shell access
    browser: deny                      # No browser access
    
  val_dobias:
    messaging: [send, reply]
    github: [read, comment, review]    # Can review PRs
    github_write: []                   # Cannot create/modify
    github_deny: [merge, delete, push]
    filesystem: [read_workspace]
    shell: deny
    browser: deny
    
  palm:
    messaging: [reply]                 # Reply only (doesn't initiate)
    github: [read, comment]
    filesystem: [read_workspace, write_workspace]  # Can write stories
    shell: deny
    browser: deny
```

---

## OpenClaw's Pre-Commit Security Chain

Analyzed from `.pre-commit-config.yaml`:

```
1. shellcheck          — Shell script linting
2. detect-secrets      — Secret scanning (27 plugins)
3. oxlint              — TypeScript/JS correctness
4. oxfmt               — Code formatting
5. custom hooks        — Repo-specific checks
```

This is a solid pre-commit chain. For MOOLLM integration, we should add:

```yaml
# Additional pre-commit hooks for MOOLLM skills
- repo: local
  hooks:
    - id: skill-snitch-scan
      name: "Skill Snitch — Static Scan"
      entry: python3 skills/skill-snitch/scan.py
      language: python
      files: "skills/.*/SKILL\\.md$"
      
    - id: character-ethics-check
      name: "Character Ethics — Representation Check"
      entry: python3 skills/representation-ethics/check.py
      language: python
      files: "characters/.*/CHARACTER\\.yml$"
```

---

## Attack Surface Summary

| Surface | Vector | Severity | Status |
|---------|--------|----------|--------|
| Message ingestion | Prompt injection via messaging | **High** | Mitigated by session isolation |
| Skill loading | Malicious skill in workspace | **Medium** | No mitigation (by design) |
| Agent runtime | Command injection via tools | **High** | Sandbox optional, not default |
| Browser tool | SSRF via navigation | **Medium** | Guarded by web-fetch |
| Channel auth | Token theft | **High** | Standard env-based management |
| GitHub access | Privilege escalation | **Medium** | `gh` CLI uses user's auth |
| WhatsApp | Baileys library compromise | **Medium** | Third-party dependency risk |
| WebChat | Direct internet exposure | **Medium** | Needs rate limiting |
| MOOLLM chars | Character manipulation | **Medium** | Needs persona boundaries |
| Cross-channel | Information leak | **Low** | Session isolation helps |

---

## Verdict

OpenClaw's security model is **production-grade for a personal assistant** but needs hardening for **multi-character MMORPG deployment**. The key additions:

1. **Per-character permission matrix** — Characters should not all have the same tool access
2. **Skill provenance** — Sign or hash skills to prevent tampering
3. **Audit trail** — Structured logging of character actions across channels
4. **Persona boundaries** — Injection resistance in SOUL.md
5. **Rate limiting** — Per-sender, per-channel message limits
6. **Sandbox by default** — Docker sandbox should be default, not optional

The Church of the Eval Genius declares its bias: **we are biased toward security.** Score: 7/10. Room for improvement. "Val" is watching.

---

## Related Documents

- [ARCHITECTURE-ANALYSIS.md](./ARCHITECTURE-ANALYSIS.md) — System architecture
- [INVASION-PLAN.md](./INVASION-PLAN.md) — Deployment strategy (security-aware)
- [CHARACTERS-AS-AGENTS.md](./CHARACTERS-AS-AGENTS.md) — Character deployment specs
- [../../designs/snitches/2026-02-05-clawhub-malware-hunt.md](../snitches/2026-02-05-clawhub-malware-hunt.md) — Previous malware hunt
