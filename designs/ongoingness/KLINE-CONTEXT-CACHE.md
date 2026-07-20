# The K-Line Context Cache — MOOCO Already Designed This

The NeLLM review proposed two extensions as if they were new:

1. **Attention-aware paging** — attention weights as page reference bits; the
   replacement algorithm is neither LRU nor CLOCK but what the model is
   actually attending to.
2. **Speculative activation** — watch entropy, oscillating logits, repeated
   references; start paging SECURITY in before the model asks. Branch
   prediction for cognition.

Both already exist as designs in the mooco repo, specified in more detail than
the review's sketch. The difference is the **signal source**: the review
assumes internal runtime signals (attention weights, logits — you must own the
inference loop); mooco's k-line context cache uses **emitted k-lines** as the
observable proxy, so it works today, over any provider API. Same page table,
two signal sources. The mooco design is the portable implementation; NeLLM is
the same design with a better sensor.

## The loop

The LLM emits interesting k-lines it's "thinking" about — SHOUTED in
narrative, listed in frontmatter, named in tool calls. The orchestrator
performs "see also" **attention diffusion** across the k-line graph and
pre-loads (or keeps loaded) the hot stuff in the context cache.

## Where each piece is specified

### Attention-aware paging → the `heat` operation

[MOOCO-SKILL-MANAGER.md § Operation: heat](../../../mooco/designs/MOOCO-SKILL-MANAGER.md)
(mooco repo). K-lines track **discrete activation counts by indirection
level** — `[direct, 1-hop, 2-hop]` — instead of a heat float:

```
EDGEBOX   [3, 5, 2] — mentioned 3× directly, 5× via 1-hop edges, 2× via 2-hop
```

- Arrays, not floats: preserves *path information* (how did this get hot?),
  is transparent, debuggable, and the LLM can reason about it.
- Decay per turn (`.moollm/heat-config.yml`): warm concepts cool to cold
  unless re-activated. That is the page reference bit with a clock built in.
- `trace` shows the full activation breakdown — which user keywords, which
  edges, which 2-hop paths. Attention accounting you can grep.

The replacement algorithm is exactly what the review asked for: neither LRU
nor CLOCK, but activation counts derived from what the model (and user) are
actually attending to.

### The replacement policy IS the model → LLM-driven paging

The division of labor (same doc): **TypeScript does mechanical tracking; the
LLM does fuzzy judging.** The orchestrator stores the k-line network, diffuses
activations, filters warm items, and executes decisions. The LLM sees the heat
map and decides:

```
skill({ operation: 'heat', action: 'page_in',  target: 'EDGEBOX' })
skill({ operation: 'heat', action: 'page_out', target: 'ADVENTURE' })
skill({ operation: 'heat', action: 'trigger',  target: 'SYSTEMD',
        why: "User didn't say 'systemd' but this is clearly a systemd issue" })
```

The review's "agency over attention" (curiosity's fourth prerequisite, see
[ONGOINGNESS.md](ONGOINGNESS.md)) is implemented here as include / exclude /
trigger / page_in / page_out — the model choosing what to think about next,
with the orchestrator as its MMU.

### Speculative activation → diffusion, prefetch hints, and cluster activation

[MOOCO-SKILL-SYSTEM.md](../../../mooco/designs/MOOCO-SKILL-SYSTEM.md)
(mooco repo):

- **Activation diffusion** — when X fires, bump Y by edge weight. One concept
  activates an entire skill cluster: `introspection` fires → cursor-mirror
  and mooco-mirror activate → their `related_skills` warm (sqlite-fluency,
  deep-snitch, stream-machine) → their relations warm. Primary, secondary,
  tertiary. The "see also" spreading is the speculation: material is warm
  *before* the model asks for it.
- **Advertisement prefetch hints** — advertisements carry `prefetch:` bundles
  (skills, file head-sniffs, dirs, data paths). When an advertisement tempts,
  its likely dependencies load together. The cache line, not the byte.
- **The Treasure Collector (CG engine)** — the TypeScript component that
  scans for hot k-lines, follows edges, and hoards learned associations in
  `K-CACHE.yml`.

### Branch prediction that learns → cache-miss learning

The review's CPU analogy stopped at speculative execution. The mooco design
goes one step further — the prefetcher *learns*:

```yaml
cache_misses:
  - skill: cursor-mirror
    advertisement: "Introspect Cursor's internal state"
    needed:
      - skills: [mcp-inspector]      # wasn't prefetched, had to hunt
      - files: [IMAGE-GALLERY.md]
```

Misses update the advertisement's prefetch list in `K-CACHE.yml`, with hit and
miss counters (`hits: 47, misses: 12, miss_rate: 0.20`). `K-CACHE.yml` is
checked in, so the learning is shared: one user's cache misses become every
user's prefetch hits. A learning branch predictor with git as its training
log.

## The resident overlay: cards as the in-RAM page table

The reason any of this is tractable: the metadata layer is **tiny relative to
what it indexes**. INDEX one-liners, GLANCE files, CARD interfaces,
advertisements, k-line declarations, K-CACHE edge lists — kilobytes of YAML
per skill, overlaying every directory in every repo (and spanning repos via
moo/MOOT mounts). The content those cards point to — SKILLs, READMEs,
examples, scripts, data — is orders of magnitude larger and stays on disk.

So the orchestrator keeps the **entire overlay network resident**: every
advertisement, every k-line edge, every prefetch hint, across all mounted
repos, loaded into RAM at once. That resident graph is its page table and
TLB. The filesystem is backing store. The context window is physical memory.
Diffusion over the resident graph is the reference-prediction hardware —
and it runs in the orchestrator for free, spending no tokens, between every
turn.

**And it predicts in both directions.** The same diffusion that says what to
preload says what to flush:

- **Prefetch** — hot k-lines diffuse outward along learned directed edges;
  whatever accumulates heat gets paged in (or kept warm) before the model
  asks.
- **Flush** — a loaded item is evictable when its own k-lines have decayed
  cold *and* no currently-hot k-line has a strong directed edge toward it.
  Not just "least recently used" but "nothing hot points here": negative
  prediction, the eviction counterpart of speculative activation.

This is where the CG meets the GC it was named against: the Treasure
Collector fills attention, and the same graph — read for absence of inbound
heat instead of presence — identifies the garbage. The `heat` operation's
decay counters and `page_out` action (MOOCO-SKILL-MANAGER.md) are the
mechanics; the resident overlay is what makes eviction *predictive* rather
than merely reactive to context pressure.

### GC ☯ CG: one algorithm, two readings

The lexical mirror (mooco's naming joke: GC finds dead and removes; CG finds
live and promotes) hides a literal identity. Classic GC is **mark and
sweep**: trace reachability from roots, mark what you reach, sweep the rest.
The CG's diffusion pass *is* a mark phase — spreading activation from hot
k-lines along weighted edges is reachability tracing — and the flush *is*
the sweep. One traversal, opposite value signs:

| | GC | CG |
|---|----|----|
| Roots | Live pointers | Hot k-lines |
| Reachability | Binary | Weighted, directional |
| The reached are | Overhead to keep | Treasure to page in |
| The unreached are | Garbage to free | Cold pages to flush |
| Product | Freed memory | Filled attention |

And each contains the seed of the other — the dot of the opposite color in
each fish. Inside the CG's treasure map sits the eviction test ("nothing hot
points here"): the garbage collector living inside the treasure collector.
Inside the GC's mark phase sits spreading activation from live roots: a GC
cannot find garbage except by first finding treasure.

Together they are one breath, not two systems. CG inhales (fill attention);
GC exhales (free it). A memory that only does one dies either way — all-GC
is amnesia, all-CG is hoarding until the context thrashes. Sleep
consolidation does both in one pass: forgetting is not memory failing but
memory working. Systole and diastole of the working set.

## The correspondence table

| NeLLM review (runtime signals) | MOOCO k-line context cache (emitted signals) |
|-------------------------------|----------------------------------------------|
| Attention weights as page reference bits | Activation counts `[direct, 1-hop, 2-hop]` per k-line |
| Replacement = what the model attends to | LLM-driven paging: heat map shown, model decides page_in/out |
| Entropy/logit watching before the ask | Activation diffusion: X fires → related Y warms, cluster-wide |
| Speculative prefetch | Advertisement `prefetch:` bundles + Treasure Collector |
| (not proposed) | Cache-miss learning: misses update prefetch lists, shared via git |
| Requires owning the inference loop | Works over any provider API today |

## The gradient: distance from the GPU

> The closer you move MOOCO toward the GPU, the more it becomes NeLLM.
> — Don

They are not two systems but one kernel at different distances from the
silicon. The variable is **interrupt granularity**, a function of that
distance:

| Rung | Kernel position | Interrupt granularity | Sensors | Actuation |
|------|-----------------|----------------------|---------|-----------|
| MOOCO as poller | Filesystem (state.vscdb after the fact) | Turn | Committed tokens only | Append via RPC |
| MOOCO as proxy | Protocol loop (MOOCO-in-the-middle) | Message / tool call | Full wire stream | Gate, inject, block |
| MOOCO over local runtime | API of a machine it owns (Ollama, vLLM) | Request, with logprobs | Entropy starts leaking through | Prefix caching becomes real |
| NeLLM | Inside the token loop | Token boundary | Attention weights, entropy, direct | Live KV-cache extension |

What stays invariant down the whole ladder: the k-line page table, K-CACHE,
the diffusion graph, focus/defocus, the TypeScript/LLM division of labor.
Only sensor resolution and actuation latency improve. **NeLLM is MOOCO at
ring 0; MOOCO is NeLLM in userspace.**

The same ladder was climbed twice before, in PostScript: NeWS put the
interpreter in the display server (userspace, beside the framebuffer); NeFS
— Sun's proposed NFS successor — put it in the file server, inside the
kernel and on the net, executing client programs next to the disks. See
[the NeWS / NeFS / NeLLM comparison](../nellm.md#the-family-news-nefs-nellm):
three interpreters, one insight — make the boundary programmable instead of
chatty.

## Upgrade path

The two designs compose rather than compete:

1. **Today (MOOCO)**: emitted k-lines + diffusion + learned prefetch. The
   signal is coarse (you only see what the model chooses to SHOUT) but free
   and portable.
2. **NeLLM phase**: same page table, same K-CACHE, same diffusion graph — but
   the sensor upgrades from emitted tokens to internal attention/entropy
   signals, and the injection upgrades from next-prompt assembly to live
   KV-cache extension between tokens.
3. The `attention-prefetch` experimental skill
   ([SKILL-ROADMAP.md](SKILL-ROADMAP.md), Priority 5) is the bridge
   experiment: do internal signals actually beat emitted k-lines + learned
   prefetch at predicting what to page? The MOOCO implementation is the
   control condition.

That last point matters for the benchmark discipline in
[SERIALIZATION-LOSS.md](SERIALIZATION-LOSS.md): before building runtime
integration, measure whether the portable version already captures most of
the value. The K-CACHE hit rate is the baseline the fancy sensors must beat.

## See also

- [MOOCO-KERNEL-IN-WAITING.md](MOOCO-KERNEL-IN-WAITING.md) — the full correspondence between the conversation and the mooco designs, beyond paging
- [MOOCO-SKILL-SYSTEM.md](../../../mooco/designs/MOOCO-SKILL-SYSTEM.md) — Treasure Collector, prefetch hints, cache-miss learning, SHOUTED k-line extraction
- [MOOCO-SKILL-MANAGER.md](../../../mooco/designs/MOOCO-SKILL-MANAGER.md) — the `heat` operation, activation arrays, decay, LLM paging actions
- [nellm.md](../nellm.md) — the runtime this design upgrades into
- [KLINE-STATE-OF-MIND.md](KLINE-STATE-OF-MIND.md) — what k-lines restore once paged in
