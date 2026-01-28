# Skill Snitch Report: runtime

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** ALWAYS BOTH. NEVER ONE.

---

## Executive Summary

**Python and JavaScript adventure runtimes.**

The golden rule: ALWAYS generate BOTH `_js` AND `_py` versions.

Never one without the other.

---

## Dual Targets

| Language | Suffix | Class | File | Environment |
|----------|--------|-------|------|-------------|
| JavaScript | `_js` | World | engine.js | Browser |
| Python | `_py` | World | runtime.py | Server/CLI |

---

## World Class Methods

| Category | Methods |
|----------|---------|
| **Inventory** | has, give, take |
| **Tags** | has_tag, find_by_tag |
| **Flags** | flag, set_flag |
| **Narrative** | emit, narrate |
| **Navigation** | go, can_go |
| **Buffs** | has_buff, add_buff, remove_buff |
| **State** | get, set |
| **Effective Values** | reset_effective, get_effective, modify_effective |
| **Subjective** | i_have, i_say, i_am, i_get, i_set... |

---

## Simulation Loop

```
increment_turn
    ↓
reset_effective (foo_effective = foo)
    ↓
apply_buffs (modify _effective values)
    ↓
simulate_objects
    ↓
deliver_mail (deterministic!)
    ↓
process_events
    ↓
process_navigation
    ↓
display_update (uses _effective)
```

---

## Mail Delivery

**Deterministic — no LLM needed!**

- Queue: `world.skills.postal.outgoing`
- Routing: `skills/postal/ROUTING.md`
- Attachment transfer: true
- Triggers events: true

---

## Security Assessment

### Concerns

1. **Sync drift** — JS and Python diverge
2. **Method mismatch** — different signatures

### Mitigations

- Always generate both
- Methods listed canonically

**Risk Level:** LOW — parallel implementations

---

## Verdict

**DUAL RUNTIME FOREVER. APPROVE.**

Always both. Never one.

JS for browser. Python for server.
