# Korz′ proof of concept — cauldron

> Status: **draft** — Phase 1 (melting). Do not execute anything from this file
> directly; wait for LADLE to produce playbooks.
>
> Started: 2026-08-21. Skill: moollm `skills/cauldron` (MELT).
> Design source: [design.md](README.md). This monolith plans the
> **runnable, unoptimized proof of concept**: YAML jazz schemas defined by
> example, a deterministic interpreter over a git repo substrate, and the
> LLM ping-pong loop for everything the strict tier refuses.

---

## 1. Current state: what is wrong

The design (design.md, né korz-prime.md) is ~1200 lines of design with zero running code. Every claim
about the strict tier — guards match decidably, ambiguity errors, dispatch
traces as plain text, doesNotUnderstand promoted to peer dispatcher — is
currently prose. The Self prototype needed an image and an IDE; Korz′ claims
it needs neither, only files, git, and a model. That claim is testable and
untested.

The honest framing of the bootstrap: **IDE-less is aspirational; the actual
IDE is Cursor.** The LLM half of the two-dispatcher semantics arrives for
free as the agent in the editor. That is not cheating — it is the design:
the strict engine is a program, the soft dispatcher is whoever is reading
the events, and today that reader lives in the Cursor chat pane.

Precedent for the loop already exists in this ecosystem: the MOOLLM
adventure compiler ping-pongs between deterministic traversal/validation
(emit warnings and errors as text) and LLM passes that translate prose into
code the JS/Py engine can run, iterating until the model validates. The
Korz′ PoC is the same loop with dispatch instead of adventure traversal.

## 2. Target model

Two processes, one repo, ping-pong via files:

1. **The strict engine** (deterministic, boring, proud of it — working
   name **Kelvin**, see B.2) scans the soup — YAML jazz slot files in a
   directory tree — executes sends, writes traces, and on any failure of
   decidability emits an **event file**: `doesNotUnderstand`,
   `ambiguous`, `malformed`, `unknownDimension`. It never guesses. It
   exits 0 having reported honestly.

   And it is a **faithful courier**: every event carries as much
   contextual comment material as practical — the jazz on and around
   the failed send, the nearest-miss slots, the relevant dimension
   declarations — quoted verbatim with provenance paths. The engine
   cannot read these letters; it delivers them anyway, because the
   event's addressee can. Comments are semantic data, and the machine's
   job at the boundary is to forward the channel that isn't for it.
2. **The LLM** (in Cursor) reads open events, does what the strict tier
   cannot — writes the missing slot, resolves the ambiguity by adding a
   guard, translates a prose slot into code, edits the world, sends
   messages back to the engine — commits, and re-runs. Repeat until the
   events directory is quiet.
3. **The user** is the third dispatcher. Events the LLM can't resolve —
   ambiguous intent, decisions that are genuinely the author's to make —
   get escalated with the **same event shape** (`status: escalated`,
   audience: human). This is where the cool user interface eventually
   comes in; for the PoC the human's inbox is Cursor chat, and the LLM
   presents escalated events there as questions.

The engine is also the **round-trip custodian**: it may rewrite values but
must preserve comments and, as far as practical, formatting. Comments are
semantic (YAML jazz); losing one is data loss.

git supplies the rest: history is the time dimension, commits are the write
barrier, PR review is the human-and-agent-in-the-middle integrity check.

## 3. Preliminary schemas, by example

Schemas are defined **by example plus comments**, not by JSON Schema — the
examples in this section are normative until M1 hardens them. All engine
I/O must round-trip these files comment-intact.

### 3.1 DIMENSIONS.yml — the dimension registry

```yaml
# DIMENSIONS.yml — names the dimensions this soup dispatches on.
# The engine treats unknown dimensions in guards as an `unknownDimension` event.
dimensions:
  character:          # who acts — the Zork/Sims "me"
    kind: tree        # values form a hierarchy; enables character-parent fall-through (M4)
    root: characters/
  place:
    kind: tree
    root: rooms/
  mood:
    kind: enum
    values: [grumpy, sunny]   # open enum — a novel value is doesNotUnderstand fuel, not an error
  time:
    kind: ordered     # spine is git history; PoC treats it as opaque labels until M4
```

### 3.2 Slot files — the sea

Surface form: **the selector is the key**; each slot is its own YAML
document (`---` separators), so the same selector can recur freely.
Postel note: the parser accepts repeated keys within one document too
(eemeli's yaml parses them with `uniqueKeys: false`) but the custodian
emits the canonical multi-document form.

```yaml
# sea/troll/greet.yml — three slots, one selector
greet:
  guards: {rcvr: troll*, world: zork}     # troll* — glob over the rcvr dimension
  do: The troll brandishes his axe and blocks the passage.
---
greet:
  guards: {rcvr: troll*, world: adventure}
  do: The troll demands payment before you may cross the bridge.
---
greet:
  guards:
    rcvr: troll*
    mood:              # bare name — presence guard: bind whatever mood is present
  do: |                # prose body: soft tier only, for now
    Greet in a way that fits {mood}; lead with menace if provoked,
    grudging respect if the visitor has beaten you before.
  # He's privately embarrassed about the axe incident — never mentions
  # it first. This comment is load-bearing: the strict tier transports
  # it, the soft tier plays it.
---
greet:
  guards: {rcvr: troll*, world: zork, mood: sunny}
  do: "Fine day for a toll, eh?"          # 3 guards > 2: wins when mood matches
---
toll:
  guards: {rcvr: troll*}
  method:                                 # code slot: the strict tier executes this
    lang: js
    params: [traveler]
    body: return traveler.gold >= 5 ? "pass, friend" : "SPLASH";
---
menace:
  guards: {rcvr: troll*}
  constraint:                             # Laszlo-style: value tracks its dependencies
    lang: js
    # Menace rises with strength and collapses without the axe.
    # Reads ctx.strength and ctx.axe — the engine re-evaluates when
    # either changes; readers always see a current value.
    body: return ctx.strength * (ctx.axe ? 2 : 0.5);
```

Body kinds: `do:` with a plain string is a data slot (strict tier returns
it, interpolating bound guards like `{mood}`); `do:` with prose that needs
judgment is a soft slot (strict tier emits `needsCrystallization` or routes
the send to the LLM); `method:` is a code slot; `constraint:` is a
**Laszlo-style constraint** — an expression whose value is kept current
against the slots and dimensions it reads, OpenLaszlo's `$` expressions
reborn in YAML. The strict tier decides which kind it holds by what it can
decide, not by being told.

Constraints are a natural LLM output format: the model generates them
directly as **commented code** — the comment carrying the design intent,
the expression carrying the law — or crystallizes them from user prompts
and design sketches ("menace should track strength but crater when he's
disarmed" becomes the constraint above, intent preserved as jazz).

### 3.3 Manifest guard tree expressions

Flat `guards:` maps are sugar. When sugar runs out, guards are **manifest
trees** — expression trees written as data, inspectable, diffable,
round-trippable, never code:

```yaml
guard-trees:
  guards:
    rcvr: troll*         # glob leaf — sugar for {glob: "troll*"}
    mood:                # presence leaf — dimension bound, any value
    all:                 # tree combinators: all / any / not, nesting freely
      - any:
          - {world: zork}
          - {world: adventure}
      - not: {mood: sunny}
      - strength: {gte: 2}          # comparison leaves: gte/lte/eq/in/range
      - place: {within: rooms/underground/}   # tree-dimension leaf: ancestor test (M4)
```

The strict tier evaluates any tree whose leaves are all decidable; one
prose leaf (`vibe: "seems trustworthy"`) makes the whole guard soft and
routes it to the LLM. Specificity generalizes from "count of guard
dimensions" to "count of distinct dimensions constrained anywhere in the
tree" — default until M4 forces better (see B.2).

### 3.4 Pointers — one way to point at anything

Events, traces, and jazz harvests all need to report context. One
convention: a **purposed dict of pointers** — the key says what kind of
context it is, the value is a path that can drill *into* objects. Paths
are repo-relative by default, `./`-relative to the reporting file, or
global (`scheme://`) for cross-repo; the fragment drills down.

```yaml
pointers:
  failed_send: sends/0013-serenade.send.yml
  nearest_slot: sea/troll/greet.yml#/2/greet        # doc 2, key greet
  dimension_decl: DIMENSIONS.yml#/dimensions/mood
  guard_leaf: sea/troll/greet.yml#/2/greet/guards/mood
  world_room: ../rooms/bridge/                      # relative: drill into the world
  prior_art: moollm://examples/all-alike-maze/MAZE.yml#/rooms/like13
```

An array is legal where purpose is obvious (the `jazz:` harvest list), but
the purposed dict is the default: readers should never have to guess why a
pointer was included.

### 3.5 Sends and traces

```yaml
# sends/0007-greet.send.yml — a send is a file; drop it in, run the engine
send: greet
context:
  rcvr: troll
  world: zork
  mood: grumpy
```

```yaml
# sends/0007-greet.trace.yml — written by the engine; append-only sibling
send: greet
matched: {slot: "sea/troll/greet.yml#/0/greet", specificity: 2}
considered: 5
result: "The troll brandishes his axe and blocks the passage."
```

### 3.6 Events — the flare the strict tier fires

```yaml
# events/0012-doesNotUnderstand.yml
event: doesNotUnderstand
send: serenade
context: {rcvr: troll, world: zork}
pointers:                      # purposed dict (§3.4): why each pointer is here
  failed_send: sends/0013-serenade.send.yml
  nearest_slot: sea/troll/greet.yml#/2/greet   # message differs, guard matches
  dimension_decl: DIMENSIONS.yml#/dimensions/mood
jazz:                          # comments harvested near the failure, verbatim —
  - from: sea/troll/greet.yml#/2/greet         # the engine can't read these;
    comment: "# He's privately embarrassed about the axe incident — never mentions it first."
  - from: DIMENSIONS.yml#/dimensions/mood      # its reader can
    comment: "# open enum — a novel value is doesNotUnderstand fuel, not an error"
ask: |
  No slot answers `serenade` under this context. Write one, alias
  serenade -> greet, or mark it out of scope.
status: open                   # LLM flips to `resolved`, adds `commit: <sha>`
```

`ambiguous` events carry the tied slots; `needsCrystallization` carries the
prose slot; every event has `status: open|resolved|declined|escalated` so
the events directory doubles as the work queue and the audit log —
`escalated` means the LLM has forwarded it up the chain to the human, and
the event waits on an answer only the author can give.

## 4. Language decision

**TypeScript, with [`yaml`](https://eemeli.org/yaml/) (eemeli's) as the
parser.** Confidence: 85%.

- Comment round-trip is the binding constraint, and eemeli's `yaml` is the
  best *programmatic* comment API of the candidates: the Document/AST keeps
  `commentBefore`/`comment` on every node, is designed for parse-edit-
  stringify workflows, and exposes a CST layer when byte-exactness matters.
- One language spans the whole arc: node CLI engine now, browser demo later,
  and the WebGPU crystallization target the design already names — camera
  in the loop, no port required.
- Dynamic enough for soup semantics, typed enough to encode the schemas.

**Embedded language: JS in the YAML, TS around it (2026-08-21).** The
precedent is OpenLaszlo — JavaScript embedded in XML, with the platform
itself written in another language. This is JavaScript embedded in YAML,
with the engine written in TypeScript. Slot bodies are **JS, not TS**:

- `new Function` evals JS directly — zero toolchain in the hot path,
  identical in node and browser. TS in slots means transpile-before-eval
  everywhere, forever.
- Type *stripping* is cheap and portable (esbuild-wasm, sucrase, and
  node's own strip-types can all run in or near the browser), but
  stripping without *checking* buys only decoration — and checking means
  shipping tsc, which is heavy in a browser tab.
- The guards already carry the types. `guards: {rcvr: troll*, strength:
  {gte: 2}}` is the parameter declaration; TS annotations inside the body
  would restate the guard in a second notation that can drift from it.
- Slot bodies are tiny and LLM-authored; JS is maximally in-distribution.
- Want types anyway? Use **JSDoc — types as comments, comments as jazz.**
  The strict tier transports them, tooling that cares can check them, and
  the round-trip custodian preserves them for free. The type channel is
  the comment channel.

`lang: ts` stays legal later as a *source* format: crystallization
transpiles it once (esbuild) and the cache stores JS — TS melts, JS
freezes. But the PoC defines `lang: js` and nothing else.

**Execution model (ratified 2026-08-21).** The Korz′ compiler compiles
slots into JavaScript: a decidable guard tree becomes a predicate
function, a method body becomes a callable, and the engine executes them
by eval — `new Function` (or `node:vm` when isolation matters, per B.2) —
**caching the compiled functions** keyed by content hash, so editing a
slot invalidates exactly that slot's cache entry, then calling them with
the context as argument. This makes the JIT metaphor literal twice over:
crystallization emits JS, and V8's JIT then compiles *that* — the strict
tier rides the platform's optimizer rather than fighting it, which is
Vanessa's SqueakJS bet run one level down. The cache is also the deopt
site: a cache miss on a stale hash is just recompilation, and a guard the
compiler can't make decidable never enters the cache at all — it stays
soft and routes to the LLM.

Runners-up, honestly assessed:

- **Python + ruamel.yaml** — ruamel's default round-trip fidelity is
  excellent (best-in-class at *preserving*), but its comment-*editing* API
  is awkward and under-documented (`ca` attribute surgery). Python stays in
  the picture as the PyTorch crystallization head; the engine may grow a
  twin, and the troll has two heads for exactly this reason.
- **Go + yaml.v3** — has Head/Line/FootComment on nodes but round-trip
  formatting fidelity is patchy, and Go is stiff clay for dispatch
  experiments. Declined.
- **PDP-7 assembly** — declined; resubmit as a Code Bakelite acquisition
  around 2045.

## 5. Comment round-trip discipline

- **M0 gate, before any dispatch code:** load → save with no edits must be
  byte-identical (or a documented, minimal set of canonicalization diffs)
  across a corpus of jazz-heavy files harvested from moollm and this repo.
- The engine's writes are **surgical**: touch the value node, leave every
  comment node alone. New machine-written keys (trace fields, `status`
  flips) get their own comments explaining themselves.
- If the high-level API proves lossy, drop to the CST. If that proves
  lossy, the persistence layer diffs at the text level and refuses to save
  a file whose comments shrank — robust-first: degrade to read-only and
  emit an event rather than eat a comment.

## 6. Milestones

| # | Deliverable | Proves |
|---|---|---|
| M0 | Round-trip harness + corpus test | comments survive the custodian |
| M1 | Data-slot dispatch: specificity = guard dimension count, ties → `ambiguous` event | strict tier exists |
| M2 | Event loop demo in Cursor: send `serenade`, engine flares, LLM writes the slot, engine answers | the ping-pong |
| M3 | Method slots (js bodies via `node:vm`), `needsCrystallization` prose → code | two tiers, one soup |
| M4 | Tree-dimension fall-through: guard matches value or ancestor (sparse shadow delegation) | dimension-parents |
| M5 | Troll-bridge adventure on the Zork five dimensions | it plays |
| M6 | Crystallization spike: compile a rule-table subset to a lookup table or WGSL | design.md §crystallization, live |

Repo: start as `korz-poc/` inside a sandbox, graduate to its own GitHub
repo at M2 when the ping-pong is demonstrable.

## 7. Instance first: Korzork

Feed M5/M5.5 from real corpora instead of invented examples —
reverse-engineer interesting, modular, reusable parts into Korz slots.

| Corpus | What it gives | Where |
|---|---|---|
| Knuth's `advent.w` (CWEB Adventure, *Selected Papers on Fun and Games*) | Literate commentary = crystallization notes already written; clean data structures (travel table, object properties, dwarf/pirate daemons, lamp fuse) | Knuth's Stanford CWEB samples |
| MIT Zork MDL source (late '70s "muddle", Dynamic Modeling Group tape) | The five-dimension dispatch in the wild: PRSA/PRSO/PRSI, WINNER rebinding, HERE cascade, daemons and fuses via the clock | [MITDDC/zork](https://github.com/MITDDC/zork) |
| Infocom ZIL sources (secondary) | The commercialized, refactored descendant for comparison | [historicalsource](https://github.com/historicalsource) |

Extraction discipline: one artifact at a time (the troll first — he's
already this document's mascot), each becoming (a) a set of Korz slots,
(b) a round-trip test file, and (c) a diff against the original's
behavior, with forty-five years of players as the oracle. Modularity is
the acceptance test: a part counts as extracted only if it runs in a
soup that doesn't contain the rest of its game.

Corpus measurements (2026-08-21): `advent.w` is 4,439 lines including
all literate prose and TeX, one file, 201 sections, 131 `make_loc`,
393 `make_inst`, ~500 decision points (`if`/`case`/loops). Zork MDL is
20,703 lines across 19 files, 196 rooms, 211 objects, 675 `DEFINE`s,
1,519 `COND`s with ~2,170 clauses. Adventure is 4-5x smaller on every
axis and pre-annotated. **First imports shipped:** the all-alike maze
(26 rooms, pure travel table, zero code) as
[moollm examples/all-alike-maze](https://github.com/SimHacker/moollm/tree/main/examples/all-alike-maze)
— one inherited description, exits-only rooms, a sparse shadow tree
that shipped in 1977 — and its structural opposite, the
[all-different maze](https://github.com/SimHacker/moollm/tree/main/examples/all-different-maze):
an 11×11 Latin square where every room answers all ten motions (total
dispatch, doesNotUnderstand impossible by construction) and the eleven
"different" descriptions are permutations of one word bag. The pirate
cross-links the pair: chest at `dead2` (alike), taunting message at
`pony` (different). The transcription practice has a name —
**Jazzork**: lifting the historic comments out of the code and into
the YAML jazz data, Knuth's `@q..@>` numbers and asides preserved
beside the facts they annotate.

---

## Appendix A. Design wisdom and conventions (cross-cutting)

- **The engine never guesses.** Every failure of decidability is an event,
  every event is a file, every file is the LLM's inbox. (Adventure
  compiler discipline.)
- **Comments are data.** A serializer that loses a comment has corrupted
  the database.
- **The file boundary is chrome.** Slot identity is `path#/slots/N`, not
  the file; reorganizing files must not change dispatch.
- **Traces beside sends.** Debugging symmetric dispatch means reading the
  trace file, not stepping a debugger — hosting-moollm.md's IDE-audit table, made
  real.

## Appendix B. Questions still awaiting a decision

### B.1 Already resolved (kept here for audit)

- **Language:** TypeScript + eemeli `yaml` (§4), ratified by Don
  2026-08-21, with the compile-to-JS / eval / function-cache execution
  model. Python twin deferred to the PyTorch crystallization milestone.
- **Embedded language:** slot bodies are JS, not TS (§4) — the
  OpenLaszlo arrangement: script in the delivery language, platform in
  the typed one. JSDoc comments are the sanctioned type channel;
  `lang: ts` deferred as a crystallization source format.
- **Constraint evaluation: push**, ratified by Don 2026-08-21 — Laszlo's
  actual model: dependency graphs with eager propagation. Within an
  engine run, a write propagates through the dirty subgraph in
  topological order and constraint outputs are materialized into the
  world, so files always hold current values and diffs show consequences
  beside causes. Dependency capture at first eval builds the graph; the
  content-hash cache doubles as the dirty detector on cold start. In the
  browser demo the same graph drives live listeners. (Pull-on-read
  survives only as the cold-start recovery path.)
- **Schema style:** by example + comments, normative examples in §3, no
  JSON Schema until the examples stabilize.

### B.2 Still open — not blocking

- **Specificity metric.** Default: count of guard dimensions; more is more
  specific; equal counts with different dimensions = tie = `ambiguous`.
  Alternative: per-dimension precedence order (Self-style parent
  priorities). Default stands until M4 forces the issue.
- **Slot granularity.** Default: file-per-message with a `slots:` list;
  also accept one-slot-per-file for big method slots. Engine must treat
  both identically (file boundary is chrome).
- **Where does context come from in M5?** Default: the send file carries
  the full context explicitly; ambient context assembly (cwd-as-place,
  git-author-as-character) is a later parlor trick.
- **Sandboxing method slots.** Default: `node:vm` with no require, PoC
  honor system. Real isolation is out of scope until someone besides us
  runs a soup.
- **Event numbering.** Default: zero-padded sequence per directory; git
  history disambiguates collisions.
- **Which Korzork corpus first?** Default: Knuth's `advent.w` first (the
  literate comments are ready-made jazz; translation is transcription),
  Zork MDL second (the dispatch structure is the prize but muddle
  requires more archaeology).
- **Pointer fragment syntax.** Default: JSON-Pointer-ish over the
  multi-doc stream — `path#/docIndex/key/...` — with repo-relative paths
  default, `./` for file-relative, `scheme://` for cross-repo (e.g.
  `moollm://`). Alternative: XPath-ish selectors matching guards instead
  of positions; revisit when doc order churns under edits.
- **Guard-tree leaf vocabulary.** Default set: glob, presence (bare
  name), `eq/gte/lte/in/range`, `within:` for tree dimensions,
  combinators `all/any/not`. Anything else is a prose leaf and soft.
- **The engine's name.** Default: **Kelvin** — the strict tier runs at
  absolute zero (the design's own metaphor: crystallize, melt, the warm
  end of the scale), and Lord Kelvin's "when you cannot measure it...
  your knowledge is of a meagre and unsatisfactory kind" is the strict
  tier's constitution, with the soft tier as the meagre-but-necessary
  kind. Alternates: **Zorkmid** (the hard currency of the realm),
  **Frobozz** (the magic company). Awaiting Don's ratification.

### B.3 New questions raised by later deep-dives

- **Adventure compiler as a client (2026-08-21).** the design now
  proposes the reverse arrow: the adventure compiler targets the Korz
  engine as its runtime — compilation becomes translation into the
  soup, host capabilities (I/O, persistence, dice, timers, media)
  arrive as plug-in objects registered under their own dimension.
  Default: M5's troll bridge is hand-authored slots first; an M5.5
  re-emits the same game through the adventure compiler and diffs the
  soups. New sub-question with default: plug-in object API = a
  `host` dimension whose values are engine-registered objects,
  callable from method slots; no other FFI in the PoC.

### B.4 Questions confirmed or declined during drafting

- **Declined:** inventing a comment-preserving YAML dialect of our own.
  Two mature libraries exist; the PoC's job is dispatch, not parsing.
- **Confirmed (2026-08-21):** selector-as-key surface form (`greet:` with
  `guards:` and `do:` inside), canonical multi-document stream so a
  selector can recur; duplicate keys within one document accepted on read
  (Postel), re-emitted as multi-doc by the custodian.
- **Confirmed (2026-08-21):** context reporting via purposed pointer
  dicts — the key names the purpose, the value drills into the object
  (§3.4); bare arrays only where purpose is self-evident.

### B.5 Convention for tracking questions going forward

Every substantive question gets logged here with a default. Resolutions
move from B.2/B.3 to B.1; nothing is deleted. Drafting-phase confirmations
move to B.4.
