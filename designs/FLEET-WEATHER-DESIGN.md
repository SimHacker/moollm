# Fleet Weather — Reactive Capacity Orchestration with LLM-in-the-Loop

*Copied out of Leela AI's private `central` repo (tools/utils/docs/
fleet-weather-design.md, captured 2026-04-25) and shared by Don Hopkins
as a concrete production example of the selfish configuration lineage —
see [SELFISH-CONFIG-IN-PRODUCTION](SELFISH-CONFIG-IN-PRODUCTION.md) and
[PROTOTYPE-FRAGMENT-CONFIG](PROTOTYPE-FRAGMENT-CONFIG.md). Relative
links to other private-repo docs have been unlinked; they name docs
that live alongside the original.*

Captured 2026-04-25. Builds on `per-zone-autoscaler-config-design.md`. Status: **design**.

## Current decision (2026-04-25, end-of-day)

After a long session iterating on this design, we've settled on a pragmatic short path:

1. **Stay with GCP MIGs + autoscalers + secrets for now.** The reconciler-without-MIGs architecture is the right long-term shape but not the right next step. Cost of switching > cost of living with MIG warts a while longer.
2. **Replace ~12 per-project `LOOKER_VM_*` / `LOOKER_AUTOSCALER_*` / `LOOKER_ZONES` secrets with a single `LOOKER_FLEET_CONFIG` YAML secret.** One source of truth per project, human-editable, reviewable in chat.
3. **Build bash + python scripts** under `skills/gcs/scripts/` for: pull/push fleet config, probe actual fleet state, reconcile declared vs actual. Stick with the toolset we already use (`gcloud`, `gsutil`, bash, python).
4. **Use these scripts manually with Cursor** — develop intuition for the dynamics before automating decisions.
5. **Defer Terraform until the Azure deploy.** Learn TF by using it to bring up Azure + Azure CI/CD. Once that's working and the TF muscle is built, retrofit GCP and consider the cross-cloud orchestrator.
6. **Defer the cross-system smart-load-balancing orchestrator** until after both clouds + edgebox have shipped first-pass reconcilers. THEN Fleet Weather becomes a multi-biome orchestrator on top of mature single-biome adapters.

This means **most of this design doc is the long-term destination**, not next-week's work. The short-path implementation is captured below as **Phase A**.

### Phase A — declarative fleet config in GCS + scripts

**Scope**: all worker types eventually (looker, web, thinker, edgebox); start with looker since that's where today's urgency lives. Schema accommodates all worker types from day one (see `skills/gcs/scripts/fleet/schema.py`).

**Storage**: GCS, not Secret Manager (per-version cost, semantic noise — secrets are for credentials). Path: `gs://$BUCKET_NAME/fleet/declared.yml`. GCS object versioning gives free history; `if-generation-match` gives atomic CAS for safe concurrent edits.

**One YAML per project** describes all worker types and all cells (MIGs) for that project.

See `skills/gcs/scripts/fleet/README.md` for the schema, examples, and CLI shape. The Pydantic-style dataclasses are committed at `skills/gcs/scripts/fleet/schema.py`.

**Scripts** (under `central/skills/gcs/scripts/`):

| Script | Purpose |
|---|---|
| `fleet-pull.sh PROJECT` | Fetch fleet config from Secret Manager → stdout |
| `fleet-push.sh PROJECT FILE` | Push YAML file as new Secret Manager version |
| `fleet-edit.sh PROJECT` | pull → `$EDITOR` → push (convenience) |
| `fleet-probe.sh PROJECT` | Emit YAML of current actual fleet state (uses existing `probe-looker.sh`) |
| `fleet-reconcile.sh PROJECT [--dry-run]` | Read declared + actual, compute diff, apply via gcloud |
| `fleet-snapshot.sh PROJECT` | Dated snapshot under `skills/gcs/instances/looker/snapshots/` |

**Conservative reconciler defaults**:
- Never deletes MIGs. `enabled: false` resizes to 0; cell removed from config emits warning.
- Always idempotent. Re-running with no diff = no-op.
- Always emits a YAML plan (the diff) before applying. Default to `--dry-run` until `--apply`.

**Per-cell `pyvision_processes`**: documentation-only in Phase A. The project-wide `PYVISION_PROCESSES` secret still rules at runtime. Phase A2 (later, after looker image rebuild) ships the metadata-override path so each cell can have its own value.

**Cells expressed for staging + dev today** (initial fleet config, captures current state):
- staging: 1 enabled cell (`monster-truck-west4a`, g4-standard-48, max 2) + dormant cells for fallback
- dev: 1 cell (`2gpu-multigpu-test`, g4-standard-96, fixed 0 unless someone flips it)

### Phase A implementation deferred to a follow-up PR

The Phase A schema (dataclasses) ships in `don-big-gpu`. The implementation (CLI, GCS I/O, probe, reconcile) is deferred to a follow-up PR for two reasons:

1. **`don-big-gpu` is already a coherent shipping unit** — Blackwell hardware, multi-GPU pyvision, PYVISION_PROCESSES_TESTING override path, probe v2, snapshot time series, design docs. Adding a half-built Python module would muddy the diff.
2. **Implementation is bounded** — ~6-8 hours of focused work; better as its own reviewable PR.

The follow-up branch (`don-fleet-phase-a` or similar) ships:

#### Storage: GCS directly, no abstraction (yet)

Use `google-cloud-storage` Python lib directly. Match the pattern pyvision/insights already use. **No new packages**, no abstractions. Refactor later when a second use case justifies it. The shared-python-packages plan (see `shared-python-packages-plan.md`) is the long-term destination, not a Phase A blocker.

#### Layout: committed dir IS the mirror

```
central/skills/gcs/scripts/fleet/
├── fleet.py                     ← the one Python script (subcommanded CLI)
├── schema.py                    ← already shipped in don-big-gpu
├── README.md
├── templates/
│   └── declared.yml.template    ← MOOLLM empathic template
└── examples/
    ├── leela-zion2-staging-0.declared.yml
    └── leela-zion2-dev-0.declared.yml

central/skills/gcs/instances/<project-id>/
├── declared.yml                 ← latest desired state (committed; mirrors gs://<project>/fleet/declared.yml)
├── declared/<ts>-...yml         ← full edit history (committed)
├── edits/<ts>-...yml            ← edit log (committed)
├── syncs/<ts>-...yml            ← reconciler action log (committed)
└── thoughts/<ts>-...yml         ← journal (committed)

# .gitignore'd (volatile, written every probe):
├── observed.yml
└── observed/
```

The committed directory IS the cache. Mirrors `gs://<project>/fleet/`. Serves as backup, reference, template for new projects, and LLM context. `fleet snapshot <project> <label>` is the explicit "commit this observed moment" command for record-worthy probes (matching the existing `instances/looker/snapshots/` pattern).

#### Reuse cli.py functions directly

For functions Fleet Weather needs (image tag lookup, project listing, etc.), import directly from cli.py via a small bootstrap shim — same pattern as `pypgqueue_bootstrap.py`. Zero new abstractions; eventual decomposition of cli.py is a separate concern (per `shared-python-packages-plan.md`).

#### CLI surface

```
fleet pull <project>                    # gsutil rsync gs://<project>/fleet/ → committed dir
fleet push <project> [--intent TXT]     # rsync ↑; writes new declared/<ts> + edit record
fleet edit <project>                    # pull → $EDITOR → push (intent extracted from YAML comments)
fleet probe <project>                   # writes observed.yml + observed/<ts>.yml (BOTH local + GCS)
fleet sync <project> [--dry-run|--apply]# diff declared vs observed; plan + apply via worker-deploy.sh
fleet snapshot <project> <label>        # explicit commit-this-moment to instances/<project>/snapshots/
fleet think <project> --topic T --body  # writes thoughts/<ts>
fleet diff <project> [--from TS]        # diff declared.yml versions
fleet log <project> [--since DUR]       # browse edits + syncs + thoughts
```

#### Worker-type coverage

The schema accommodates all worker types from day one. Phase A's reconciler delegates VM operations to `worker-deploy.sh` (which already handles looker scaled fleets, web singleton-with-volume stop-wait-start, thinker scaled fleets). Fleet Weather knows WHAT should change; worker-deploy.sh knows HOW.

### Phase B — automated reactive control (after weeks of A operation)

After hand-running A and developing intuition: extend probe scripts to write to postgres, build deterministic Python reconciler modules that handle the obvious first-order knobs (scale based on backlog, drain stocked-out zones, fall back to standard, etc.), keep the YAML config as the source of truth.

### Phase C — LLM advisor (after B is stable)

Reconciler emits state to YAML + postgres → LLM reads recent history + current state → produces YAML edit recommendations → operator reviews → apply.

### Phase D — cross-biome orchestrator (after Azure ships + Terraform muscle built)

Lift the per-biome reconcilers behind a uniform interface. Then a single Fleet Weather module decides across (gcs, azure, edgebox, …). This is when the long-term architecture sketched in the rest of this doc becomes the implementation. Until then, the rest of this doc is **target architecture**, not active work.

---

## The framing

Capacity in spot markets is **weather**, not infrastructure. It moves on minute-to-hour timescales. A zone that's clear in the morning storms out by noon, clears again by afternoon. Workload demand has its own weather pattern — daily/weekly cycles plus episodic batches like the urgent backfills we ran yesterday.

We need a sailor's posture, not a builder's:
- **Read the weather.** Probe capacity, watch the storms move.
- **Set sails for the wind we have.** Run more workers in zones with capacity, fewer where it's stocked out.
- **Trim continuously.** Don't lock in one configuration; let the fleet shape change shape with the weather.
- **Pay for shelter when the storm threatens the cargo.** Fall back to on-demand when spot can't deliver and the workload is too important to wait.
- **An experienced sailor (LLM) advises the captain (operator), not auto-pilots.** The LLM proposes; the operator (or a constrained automation) disposes.

This document captures the design intent. Implementation will land in phases.

## The decision space — a multi-dimensional matrix

| Dimension | Cardinality | Examples |
|---|---|---|
| Zone | ~14 G4-capable US zones | us-west4-a, us-west4-c, us-central1-b, us-central1-f, us-east1-b, us-east1-d, … |
| Machine type / GPU count | 7 G4 SKUs | g4-standard-{6,12,24,48,96,192,384} = 1, 1, 1, 1, 2, 4, 8 GPUs |
| Provisioning model | 2 | spot (preemptible) / on-demand (standard) |
| Worker type | 3 | looker, web, thinker |

For looker alone: **14 zones × 7 SKUs × 2 provisioning = 196 possible MIG configurations.** We won't materialize all of them. The point is to have a **decidable space**: each cell is a possible MIG; the decision is which cells to provision and at what max-replica count.

## Layered architecture

```
                    ┌──────────────────────────────────────┐
                    │          ACTION LAYER                │
                    │  worker-deploy.sh + upgrade-worker-  │
                    │  vm.sh + manual gcloud + fleet API   │
                    └──────────────▲───────────────────────┘
                                   │  applies recommendations
                    ┌──────────────┴───────────────────────┐
                    │         DECISION LAYER               │
                    │  fast loop: rules ("backlog>X →      │
                    │   scale max replicas"; "stockout →   │
                    │   shift to healthy zones")           │
                    │  slow loop: LLM advisor reads        │
                    │   probe data, proposes fleet shape   │
                    └──────────────▲───────────────────────┘
                                   │  reads time-series
              ┌────────────────────┴────────────────────┐
              │           STORAGE LAYER                  │
              │  YAML snapshots (git-tracked, LLM-      │
              │   readable, human-friendly)              │
              │  Postgres time-series (queryable,        │
              │   joinable, machine-friendly)            │
              │  same data, two fidelities               │
              └────────────────────▲────────────────────┘
                                   │  emits observations
              ┌────────────────────┴────────────────────┐
              │           PROBE LAYER                    │
              │  capacity-probe (try-create per cell)    │
              │  performance-probe (probe-looker-worker) │
              │  workload-probe (Pub/Sub backlog/rate)   │
              │  cost-probe (spot vs standard pricing)   │
              │  preempt-tracker (when did each VM die)  │
              └──────────────────────────────────────────┘
```

The layers are **insulated**: probes don't decide, decisions don't probe. New probes can be added without touching the decision layer. New decision rules can be added without touching the probe layer.

## Probe layer

Five probes run on independent schedules. Each emits **structured YAML** to a snapshot file AND **inserts** into a Postgres table.

### 1. capacity-probe (every 5-15 min, per cell)

For each (zone, SKU, provisioning) cell we care about:
- Try to create a single VM via `gcloud compute instances create --no-restart-on-failure`
- Wait for STATUS=RUNNING (success) or wait <10s for stockout error (failure)
- Immediately delete the VM
- Record (cell, success/failure, error_code, latency_ms, ts) in postgres + yaml

This costs a few cents per probe and gives us a **real-time capacity weather map**.

### 2. performance-probe (every 5 min, per running VM)

We already have this — `skills/gcs/scripts/probe-looker-worker.sh`. Snapshots already record per-GPU utilization, per-process RSS, container health, restart count, configuration secrets, runtime file contents. **No new code needed for this probe.** Add postgres insert step.

### 3. workload-probe (every 1 min, per project)

Pull from Cloud Monitoring API:
- `pubsub.googleapis.com/subscription/num_undelivered_messages` → backlog
- `pubsub.googleapis.com/subscription/ack_message_count` → throughput  
- `pubsub.googleapis.com/topic/send_message_operation_count` → publish rate
- Per-video processing time (from container logs — pyvision logs `init_duration` + `frame_count` per video)

Emit YAML to a `workload/` subdir + insert to postgres.

### 4. cost-probe (daily)

GCP doesn't expose pricing via API simply, but spot pricing is published periodically. Pull spot vs standard prices for each (zone, SKU) cell. Slowly-changing data; daily refresh is enough.

### 5. preempt-tracker (event-driven)

When `gcloud compute instance-groups managed list-errors` shows new entries, OR a VM transitions from RUNNING to TERMINATED+autoDelete, record the preempt event with cell + lifetime + workload-state-at-preempt.

This is the **survival data**: how long does a spot VM live in (zone, SKU)? Histograms feed both the LLM and the rule-based fast loop.

## Storage layer

### YAML snapshots — the LLM/human surface

Continuing the convention from `skills/gcs/instances/looker/snapshots/`. New cousin directories:
- `skills/gcs/snapshots/capacity/<yyyymmdd-hhmmss>-<zone>-<sku>-<provisioning>.yml`
- `skills/gcs/snapshots/workload/<yyyymmdd-hhmmss>-<project>.yml`
- `skills/gcs/snapshots/preempt/<yyyymmdd-hhmmss>-<vm-name>-<lifetime>.yml`

Cluster-prefix naming. Sortable by filename. LLM reads the most-recent + recent-history N as context.

### Postgres tables — the analyst surface

```sql
CREATE TABLE fleet_weather.capacity_probe (
  ts          timestamptz PRIMARY KEY,
  zone        text,
  machine_type text,
  gpu_type    text,
  gpu_count   int,
  provisioning text,           -- 'spot' or 'standard'
  outcome     text,            -- 'success' or 'stockout' or 'quota' or 'other'
  error_code  text,
  latency_ms  int
);

CREATE TABLE fleet_weather.workload_observation (
  ts                    timestamptz,
  project_id            text,
  subscription          text,
  backlog               int,
  publish_rate_msg_s    real,
  ack_rate_msg_s        real,
  PRIMARY KEY (ts, project_id, subscription)
);

CREATE TABLE fleet_weather.vm_lifecycle (
  vm_name              text,
  zone                 text,
  machine_type         text,
  project_id           text,
  created_at           timestamptz,
  terminated_at        timestamptz,
  termination_reason   text,    -- 'preempt' | 'manual' | 'crash' | 'maintenance'
  lifetime_seconds     int,
  PRIMARY KEY (vm_name, created_at)
);

CREATE TABLE fleet_weather.cost_observation (
  ts                   timestamptz,
  zone                 text,
  machine_type         text,
  spot_price_usd_hr    real,
  standard_price_usd_hr real,
  PRIMARY KEY (ts, zone, machine_type)
);
```

Use the existing edgebox postgres image (timescaledb) for time-series friendliness, or run a small managed Cloud SQL instance in `leela-devops-0`. **Don't put it in customer projects** — fleet weather is operator data, not customer data.

## Decision layer

### Fast loop (rules; runs every minute)

Rule-based, deterministic, cheap:

| Trigger | Action |
|---|---|
| Backlog > 1000 msgs for >5 min AND any cell shows recent capacity success | Bump `max_replicas` of that cell's MIG by 1 |
| Backlog < 50 msgs for >15 min | Reduce `max_replicas` of biggest MIGs by 1 (down to 0 floor) |
| Cell shows N consecutive stockouts | Mark cell "frozen", redirect demand to other cells |
| Spot VM survival p50 < 5 min in cell | Mark cell "high-churn", deprioritize |
| Backlog > 10000 msgs AND no spot capacity anywhere | Spin up one on-demand cell as backup |

Implement as a Python script with explicit, readable rules. **No magic.** A reader (human or LLM) should be able to predict its behavior from the rule list.

### Slow loop (LLM advisor; runs every 30-60 min)

The LLM is given:
- Last 24 hours of capacity-probe outcomes per cell (small YAML — cells × time)
- Last 24 hours of workload observations
- Last 24 hours of preempt events
- Current fleet shape (which MIGs exist, target sizes)
- The cost data
- Last 5 LLM recommendations + whether they were applied + their outcomes

The LLM produces a structured YAML recommendation:

```yaml
fleet_recommendation:
  generated_at: "2026-04-25T16:00:00Z"
  observed_weather: |
    us-west4-a has been stable for 18h. us-central1-b returned to capacity
    at 09:00 UTC after being out since yesterday 17:30. Spot survival
    p50 in west4-a is 4.2 hours; in central1-b currently unknown (hasn't
    survived a probe yet today).
  observed_workload: |
    Steady state ~50 videos/min for 12h. Recurring spike at 02:00-04:00 UTC
    (visible in 7-day pattern). No active backfill.
  proposed_fleet:
    - mig: looker-us-west4-a    sku: g4-standard-48  provisioning: spot   max_replicas: 2  rationale: "proven; stable; primary"
    - mig: looker-us-central1-b sku: g4-standard-48  provisioning: spot   max_replicas: 1  rationale: "warm spare; capacity returned this morning"
  fallback_if_spot_dies:
    - mig: looker-us-west4-a-standard  sku: g4-standard-48  provisioning: standard  max_replicas: 1  rationale: "guaranteed capacity for batch SLAs; only spin up if both spot cells lose VMs simultaneously"
  confidence: medium
  open_questions:
    - "us-central1-b last preempted at 17:30 yesterday; have we measured its survival pattern post-recovery?"
```

The operator (or a constrained automation) reviews and applies. Initially just a Slack post for human review. Later: an apply-button or a confidence-gated auto-apply.

**The LLM is an advisor, not an actuator.** The action layer is what mutates infra; the LLM only recommends.

## Action layer

What we already have:
- `worker-deploy.sh` — creates MIGs from secrets (zone-list-driven; needs extension for per-cell MIG model)
- `upgrade-worker-vm.sh` — bumps secrets per worker type
- `gcloud compute instance-groups managed resize / stop-autoscaling / update-autoscaling`
- `probe-looker.sh` + `probe-looker-worker.sh` — performance-probe is half-built

What we need to build:
- `fleet-action.sh` (or similar) that takes a "fleet recommendation YAML" and applies it idempotently
- A "MIG matrix" model — instead of single project-wide LOOKER_VM_* secrets, **per-MIG instance templates** with embedded SKU + provisioning. Possibly named `looker-<zone>-<sku>-<spot|std>`.
- Removal of the "single LOOKER_VM_MACHINE_TYPE" assumption (which currently forces all MIGs in a project to the same SKU).

## Phased implementation

### Phase 1 — probes + storage (this week)

- Capacity-probe Python script + cron under leela-devops-0 (probes all 14 zones × 3 SKUs × 2 provisioning every 10 min)
- Workload-probe Python script (already half-implemented inline; lift to a `fleet-workload-probe.sh` + cron)
- Postgres in leela-devops-0 (small Cloud SQL, single timescaledb instance)
- YAML snapshot emit (continues current pattern)
- Both targets emit identical data — postgres for queries, yaml for LLM context

Outcome: weeks of capacity + workload + preempt data accumulate. We learn the actual weather patterns.

### Phase 2 — rule-based fast loop (next week)

- Implement the rules listed above as a Python script
- Cron every minute
- Read postgres, decide action, call gcloud
- All actions logged + emitted as YAML for audit trail

Outcome: fleet shape adjusts itself to weather without operator intervention.

### Phase 3 — per-MIG matrix model (the week after)

- Refactor `worker-deploy.sh` to support `looker-<zone>-<sku>-<spot|std>` matrix instead of single project-wide secret
- Each MIG has its own template with its own SKU + provisioning
- Single autoscaler per MIG; the fast loop tunes max_replicas per MIG
- Operators manage by enabling/disabling cells, not by setting one-size-fits-all secrets

### Phase 4 — LLM advisor (when probes have weeks of data)

- Slack bot that posts LLM recommendations every 30-60 min
- Recommendations link to a one-click apply (later: confidence-gated auto-apply)
- LLM reads YAML snapshots + a postgres summary as context

## Success criteria

- **Survival**: Even when an entire region stocks out, fleet capacity drops by <50%.
- **Cost**: Spot saves >70% vs full on-demand; on-demand fallback engages <5% of the time.
- **Latency**: Backlog never exceeds 30 min of work for >10 min.
- **Operator load**: Most weeks, no manual fleet adjustment is needed.
- **LLM utility**: Operators take >80% of LLM recommendations as-is.

## Open design questions

- **Cross-cloud?** Eventually, yes — Azure capacity is independent of GCP capacity, that's free survivability. But for Phase 1-4, GCP-only.
- **Cost vs latency tradeoff knob.** Per-project, configurable as a single number `cost_priority ∈ [0,1]` that biases the rule loop. Most projects want low-cost spot-first; some critical-batch periods want guaranteed capacity.
- **Predictive vs reactive.** Phase 1-4 is reactive. Phase 5+ could include time-series forecasting ("based on the last 4 weeks, expect a spike at 02:00 UTC; pre-warm capacity at 01:30").
- **What if the fast loop and LLM disagree?** Fast loop wins (constrained, deterministic); LLM proposals are advisory and applied by operator approval until confidence is established.
- **MOOLLM framing.** This system itself has the shape of a MOOLLM skill: clear inputs (probes), clear outputs (recommendations + actions), a sister-script protocol, multi-layer (probe/store/decide/act). A future lift could turn it into `skills/fleet-weather/` with the probe-* scripts as cli-tools, the YAML snapshots as `instances/`, and the LLM advisor as a scheduled `incarnation`.

## Related work

- `per-zone-autoscaler-config-design.md` — predecessor; covers the per-zone autoscaler config aspect. This doc supersedes & extends.
- `image-and-container-caching-design.md` — two-layer caching (disk image regional distribution + container regional pull-through), synergistic with Fleet Weather: zone-choice decisions should account for which zones have warm container caches and which have local disk-image replicas.
- `terraform-migration-design.md` — the per-MIG matrix model would be a natural Terraform module ("fleet_cell"). When/if Terraform lands, Fleet Weather's action layer becomes "rewrite TF vars + apply" instead of "call gcloud".
- `skills/gcs/instances/looker/` — performance-probe + snapshot pattern is already established here; Fleet Weather inherits and extends.
- `skills/gcs/gotchas/spot-capacity-stockout.md` — the failure mode this entire system is designed to handle gracefully.
