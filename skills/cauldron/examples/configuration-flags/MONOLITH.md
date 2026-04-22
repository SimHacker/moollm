# 🖖 Configuration Unification Plan (trekified excerpt)

**Status:** teaching excerpt — condensed from a Phase-1 kitchen-sink document (~1,900 lines, ~30 turns). Full text and line-level evidence live in the Fleet Monorepo (`docs/CONFIGURATION-FLAGS-PLAN.md`).

**Scope (trekified):** 🖖 Forward Sensor Inference Suite, 🖖 Positronic Action Processor, worker chassis, Forward Sensor Outpost tooling, Validation Grid (cross-repo).

**Goal:** Replace a tangle of overlapping env vars and CLI flags with **orthogonal, positively named drivers** that behave identically on 🖖 Sector 001 (cloud) and Forward Sensor Outposts.

---

## §1 Current state — what was wrong

### 1.1 Flags in the wild (summary)

| Concern | Legacy shape | Problem class |
|---------|--------------|---------------|
| Message queue | `QUEUE_DRIVER` + aliases | Overloaded: also implied storage, logging, schema defaults |
| Bulk storage | `DISABLE_GCS`, `--enable-gcp` | Double negative; misaligned names |
| Structured data | Implicit from queue | Could not express "local events + cloud archive" cleanly |
| Logging | Multiple env + CLI names | Three parallel logger implementations; silent SQL mismatch |
| Identity | `PROJECT_ID` × 3 | Name proliferation |

### 1.2 Anti-patterns (representative)

1. **Import-time env reads** decide whether cloud filesystem adapters load. Validation Grid often omits the queue var → adapters never load → reads fail **silently**.
2. **One flag, many meanings** — queue driver, storage, logging, and schema defaults collapsed together.
3. **Deep `os.getenv` in libraries** — effective config depends on call order.
4. **Container reality is env-first** — CLI argparse drifted from what production actually set.

### 1.3 Shape of the error

Four independent axes were **conflated**:

- How work is queued (🖖 Subspace Broadcast vs Memory Core Alpha vs none)
- Where bulk objects live (🖖 Long-Range Object Vault vs local)
- Where structured rows go (🖖 Astrometrics Archive vs Memory Core Alpha vs none)
- Where logs go (stdout, cloud, Memory Core Alpha, file)

---

## §2 Target model — orthogonal drivers

### 2.1 Five knobs (any combination valid)

| Knob | Values | Meaning (trek read in prose) |
|------|--------|------------------------------|
| `EVENTS_DRIVER` | `pubsub` \| `postgres` \| `none` | 🖖 Subspace Broadcast vs 🖖 Memory Core notify vs one-shot CLI |
| `DATA_DRIVER` | `bigquery` \| `postgres` \| `none` | 🖖 Astrometrics Archive vs 🖖 Memory Core vs offline |
| `STORAGE_BACKEND` | `gcs` \| `local` | 🖖 Long-Range Object Vault vs outpost disk |
| `LOG_SINKS` | comma subset of `stdout`, `google`, `postgres`, `file` | Multiple sinks, independent |
| `MQTT_ENABLED` | `true` \| `false` | No `DISABLE_*` proxy |

Implementers: these spellings are the **canonical** ones from the Fleet Monorepo plan; trekify substitutes apply to narrative text, not to enum tokens in code or env files.

### 2.2 Rules

1. **Env name ↔ CLI flag mechanically** — no drift.
2. **Parse once** at entry — libraries receive narrow frozen slices, not raw env.
3. **CLI > env > file > default.**
4. **Booleans positive** — no `DISABLE_*`.
5. **Unknown enum → fail fast** — no silent fallback.
6. **Safe local defaults** — one-shot scoring works with no network.

### 2.3 Legacy flag retirement

- `QUEUE_DRIVER` → `EVENTS_DRIVER` with **narrowed** semantics.
- `DISABLE_GCS` deleted → `STORAGE_BACKEND=local` (or equivalent explicit choice).

---

## §3 Affected surfaces (high level)

Trekked names only; the real doc lists every file path and grep anchor.

- 🖖 Positronic Action Processor: path helpers, lazy vault imports, MQTT gating.
- 🖖 Forward Sensor Inference Suite: `gcp.py` diet, ChainMap layering, server entrypoint.
- Forward Sensor Outpost: systemd env files, identity vars for fleet compute metadata.
- Validation Grid: per-operator env YAML, onboarding doc rewrites, Python harness flags.

---

## §4 Shared packages (intent)

Land small modules: **one app config parser**, **one logging facade**, **retry**, **MQTT client**, **identity helpers**, **fakes for tests**—each with a narrow API. **No** giant shared object-storage package; storage stays tactical per app with clear import vs ingest layer boundaries.

---

## Appendix B — Open questions (sample shape)

```yaml
# Illustrative only — full tracker lives in source 10-open-questions.md
questions:
  - id: Q1
    summary: "Canonical name for local buckets root"
    status: resolved_in_source
    lesson: "Evidence beat ideology; fleet kept an existing name where churn cost > win."
```

---

## Transition to Phase 2

When the user said **"now break it up,"** the monolith was split into:

- `README.md` — skimmer index
- `01-overview.md` … `10-open-questions.md` — topical shards
- `design-wisdom.md` — Appendix A principles
- `playbooks/PB-NN-*.md` — one PR per file
- `META-PLAN.md` — **how this document was made** (reusable)

That META-PLAN is the meta-skill export: **same process, different topic, new cauldron.**

---

*End of excerpt. For execution graphs, Harper's Index numbers, and playbook sidecars, see `sharded/README.md` and the Fleet Monorepo.*
