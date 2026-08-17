# Selfish Config in Production — the same trick, five deployments

Don Hopkins's "ultimate selfish configuration system": small JSON/YAML
objects that declare **parent reference lists** and deep-merge in
order. Clone-override-delegate, applied to configuration. Built first
for Leela AI's devops fleet operations, reimplemented clean-room for
MOOLLM ([PROTOTYPE-FRAGMENT-CONFIG](PROTOTYPE-FRAGMENT-CONFIG.md)), and
used before that in Pantomime. This doc collects the concrete
production evidence, copied out of the private repos with permission.

## The Korz frame: config as a slot space

The Korz paper: *"A body of Korz code is termed a slot space: a
collection of slots organized in a multidimensional space."* A selfish
config system is a slot space where the dimensions are deployment
axes — and dispatch is a compile-time merge instead of a runtime send.
Chess makes the shape obvious: piece **type**, **color**,
**enumeration** (which pawn), **behavior variant** (house rules) are
composable dimensions; one PAWN definition, interpreted per side, plus
[Revolutionary Chess](../skills/experiment/experiments/turing-chess/plugins/revolutionary-chess/)
overlays — never a copy per combination
([GAME-PIECES](GAME-PIECES.md)). Fleet config has the same
combinatorics: platform × app × content set × build flavor × host ×
world. Materializing every combination is exponential; declaring each
dimension once and merging is linear. That is the whole trick.

## Case 1: machine-vision processor config (Leela pyvision, live now)

Verbatim from production (`apps/pyvision/queue_configurations.json`,
trimmed): the config that selects and tunes the GPU inference
processors. Two-deep parent chains, single JSON file, each entry
carrying only its deltas:

```json
{
    "default": {
        "queue_name": "objectdetection",
        "processor": "detectron2",
        "confidence_threshold": 0.1,
        "gpu_enabled": true,
        "num_workers": 1,
        "ack_deadline_seconds_process": 120,
        "max_task_duration_seconds": 3600
    },
    "object":  { "parents": "default", "queue_name": "object",  "model_type": "object" },
    "pose":    { "parents": "default", "queue_name": "pose",    "model_type": "pose" },
    "objectdetection": {
        "parents": "object",
        "config_path": "configs/quick_schedules/mask_rcnn_R_50_FPN_inference_acc_test.yaml",
        "queue_output_suffix": ".obj",
        "contours": true
    },
    "posedetection": {
        "parents": "pose",
        "config_path": "configs/quick_schedules/keypoint_rcnn_R_50_FPN_inference_acc_test.yaml",
        "queue_output_suffix": ".pose",
        "contours": false
    }
}
```

`posedetection → pose → default`: the leaf is four lines because
everything else delegates. Forty-odd tuning knobs live in exactly one
place. Add a new model variant = add a leaf.

## Case 2: edgebox master config (Leela on-prem, live now)

The on-prem vision boxes (GPU inference on customer premises,
optionally air-gapped) are configured by **one YAML document** with a
different selfish move: **prototype-first, presence = enabled**. The
master config starts from a full prototype containing every possible
section with documentation and example values; you copy it and *delete*
what you don't want, along `---- cut here ----` lines. No
`enabled: true` flags — **having a section means "use this"** (the
Korz echo: a slot pertains, or it doesn't; there is no null
coordinate). Setup merges the layers per world:

```
required + storage + web + world (postgres|worker|system) + host + container
    → /data/<world>/*.env   (plain text files; runs offline, no services at runtime)
```

One config document picks which components exist; one script, one
Packer file, one image artifact serve every deployment mode (unified |
split | storage | worker). YAML over JSON *because comments are
semantic* — every puzzling parameter documents where its value comes
from. ([yaml-jazz](../skills/yaml-jazz/), independently confirmed by
industrial ops.) A layer above, the deployments themselves inherit:
**stack** (vision, builder, training) is the class-shaped thing,
**instance** (a named box) carries only its overrides.

## Case 3: fleet operations (Leela cloud, the design that started it)

[FLEET-WEATHER-DESIGN](FLEET-WEATHER-DESIGN.md) — copied out in full.
The GPU worker fleet across ~14 zones × 7 GPU SKUs × spot/on-demand ×
3 worker types is a **decidable multidimensional cell space** (their
words: "each cell is a possible MIG"). Twelve scattered per-project
secrets collapse into one declared YAML per project; probe / decide /
act layers reconcile declared against observed; the LLM reads the YAML
history and *advises* — capacity as weather, the operator as captain.
The committed directory of declared/observed/edits/syncs/thoughts IS
the cache, the audit log, and the LLM context, all at once.

## Case 4: Pantomime (Unity AR/VR, years earlier)

The same grammar configured three different things at once: the JSON
**object and networking system** (plug-in objects as mixins), **app
configuration** (different apps, different content sets), and **build
targets** (platforms × dev/prod flavors) — many composable dimensions,
all selfishly declared as JSON with parent reference lists, one
resolver. The proof that the trick isn't domain-specific.

## Case 5: MOOLLM (the clean-room descendant)

[PROTOTYPE-FRAGMENT-CONFIG](PROTOTYPE-FRAGMENT-CONFIG.md): fragments
declaring `parents: []`, RFC 7386-style deep merge, directory-as-
package with co-located scripts — session profiles and adventure
runtimes as leaf prototypes. Same mechanics, new names, plus the LLM
as resolver-of-last-resort
([LATENT-SPACE-INHERITANCE](object-system/LATENT-SPACE-INHERITANCE.md)).

## What the five cases agree on

1. **Leaves are deltas.** Every entry carries only what differs from
   its parents; the leaf is small because the lineage is real.
2. **Dimensions compose; combinations don't materialize.** Declare each
   axis once; merge on demand. Linear declarations, exponential
   coverage — the same economy Ace bought with `$tradeoff` and Korz
   buys with guards.
3. **Presence is the switch.** A section, slot, or fragment that exists
   is enabled; deletion disables. No parallel boolean bookkeeping.
4. **The merged artifact is boring on purpose.** Flat env files, one
   YAML, one dispatch table — the fancy structure exists at compose
   time, then crystallizes (the tiered-JIT move, at devops speed).
5. **Comments are load-bearing.** YAML jazz in industrial dress: the
   config documents itself, because the person debugging it at 3 AM is
   the reader that matters.

Related: [PROTOTYPE-FRAGMENT-CONFIG](PROTOTYPE-FRAGMENT-CONFIG.md) ·
[FLEET-WEATHER-DESIGN](FLEET-WEATHER-DESIGN.md) ·
[GAME-PIECES](GAME-PIECES.md) ·
[SELF-ISH-INFLUENCES](SELF-ISH-INFLUENCES.md) ·
[object-system/SELF-AND-MOOLLM](object-system/SELF-AND-MOOLLM.md)
