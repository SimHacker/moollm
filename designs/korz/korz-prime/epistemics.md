# Epistemics — names, K-lines, isKnown, and the end of null

*Part of the [Korz cauldron](../README.md). The
[design](README.md) gives Korz′ two dispatchers — a strict VM and an
LLM. This document works out what that does to *reference*: what a
name means, what an address can point at, what replaces null, and how
latent knowledge gets measured, cached, and reviewed.*

## Names are inheritance

Dimensions and coordinates are ordinary words — `mood`, `weather`,
`era`, `trust` — and in the soft tier a word is a **K-line** (Minsky's
term: a name that reactivates everything attached to it): `mood:
gezellig` imports everything the training data knows about the Dutch
concept of gezelligheid, no definition required. The strict tier
treats the same word as an opaque symbol. One name, prepaid latent
semantics above, free interning below.

## Any slot can hold a K-line pointer

Not only `parents:`.
[LATENT-SPACE-INHERITANCE](https://github.com/SimHacker/moollm/blob/main/designs/object-system/LATENT-SPACE-INHERITANCE.md)
(a MOOLLM design: parent lists may name concepts that exist only in
training data) established the move for the parent list; the sea
generalizes it to every slot body. `template:
gothic-victorian-newspaper` with no such file on disk isn't a broken
link — it's an address into training data, dereferenced by the soft
tier at send time. `voice: carnival-barker`, `layout: ransom-note`,
`physics: looney-tunes` — each resolves to more than any file you'd
bother writing.

Every slot value is an address, and addresses come in two kinds:

- **Filesystem paths** — resolved by `open`, versioned by git, honored
  by the strict tier.
- **K-lines** — resolved by inference, versioned by the model
  generation, soft tier only.

The strict compiler treats an unresolvable pointer the way it treats a
prose body — refuses it, which marks it: every latent pointer is a
standing candidate for crystallization into a real file once its
improvised referent stabilizes. Dangling pointers become deopt
triggers instead of segfaults.

## isNull becomes isKnown

With path pointers the presence test is boolean — the file exists or
it doesn't. With K-line pointers the question generalizes: not *is it
null* but **how known is it** — `isNull: bool ⇒ isKnown: float`.
`mood: gezellig` activates deep, dense, consistent training knowledge;
`layout: zorbleflax` activates nothing; `theme: bridge-gothic` sits in
between — composable from parts, but no canonical referent.

Measurable, too: ask the model to describe the referent several times
and score the agreement (consistency probing), or read the logprobs
directly — cheap conversational version and instrumented version of
the same test.

What it buys:

- **Guards can threshold on knownness** — `template: {kline:
  gothic-victorian-newspaper, min_known: 0.6}` matches only when the
  referent is solid enough to trust. The
  [korz-notes](../korz-notes.md) null question ("no null coordinate —
  missing feature or dodged bullet?") gets a third answer: neither
  null nor absence, but *graded presence*.
- **Crystallization gets its policy signal.** High isKnown → safe to
  leave latent (the training data is the file). Low isKnown → spell it
  once, in a real file — which is the
  [no-ai-humansplaining](https://github.com/SimHacker/moollm/tree/main/skills/no-ai-humansplaining)
  test ("is the pointee in latent space?") turned from a heuristic
  into a compiler policy with a threshold.
- **Improvisation scales its own caution.** The soft tier can lower
  its temperature as isKnown drops — confident riffing on gezellig,
  careful literalism near zorbleflax — instead of hallucinating with
  uniform confidence. State the confidence as a number, then act on
  it: calibrated dereferencing.
- **Advertisement scores get an epistemic term.** In The Sims'
  dispatch economy, objects advertise scored actions and each Sim
  re-weights the scores through its own needs
  ([worked example](examples/sims-advertisements.md)). Let the score
  also multiply in the isKnown of the ad's own referents — `score: 80
  * isKnown(template) * isKnown(voice)` — and a slot whose pointers
  are shaky **bids low in its own auction**. Confident slots outbid
  vague ones; a half-remembered behavior gracefully loses to a
  well-grounded one instead of winning on a hardcoded number; and the
  hallucination damper is built into the market instead of bolted onto
  the model.

## Do we want nulls at all? (The zillion-dollar question)

Hoare called null references his billion-dollar mistake — a zillion
with inflation — and his regret was specific: null silently inhabits
*every* reference type, so every dereference is a hidden conditional.

Korz already dodged that bullet structurally, and it's worth saying
how: **absence is not a value.** A dimension is either bound or
unmentioned; there is no `location: null` poisoning the coordinate
space, no token you can accidentally dereference — an unbound
dimension just means only more-generic slots match.

The deeper sin of null is that one token conflated at least three
meanings — *no binding*, *unknown*, and *nothing* — and Korz′ gives
each its own honest mechanism:

| Null conflated | Korz′ separates |
|---|---|
| No binding | Unmentioned dimension — structural absence, matched by generic slots |
| Unknown | `isKnown: float` — measured, thresholded, acted on |
| Nothing | A real sentinel coordinate you name and guard on — `inventory: empty`, `location: nowhere` — a value, never a hole |
| Failure | Deopt to the soft tier — improvise, don't segfault |

So: keep Korz's refusal of the null coordinate (dodged bullet,
confirmed), replace null's epistemic duty with isKnown (the boolean
shadow gets its continuum), and when a domain genuinely needs
"nothing," model it as a named coordinate that dispatch can see —
E-Prime discipline applied to reference: ban the degenerate universal
token, and every absence has to say *which kind of absent it is*.

A July 2024 [HN comment of Don's](https://news.ycombinator.com/item?id=41043950)
staked out this ground: JavaScript's null *and* undefined, plus
TypeScript's `unknown`, stack up what Anders Hejlsberg calls the
Two-Billion-Dollar Mistake — and, as one reply put it, that assumes
"these mistakes are additive and not multiplicative." Korz′'s answer
to the multiplication is to hold a zero factor: no null tokens at all,
so the product of the mistakes is zero. The same comment cites the
Rumsfeld Matrix, and it maps onto isKnown mechanically:

| Rumsfeld | isKnown |
|---|---|
| Known knowns | High isKnown — dense latent activation, or a resident page a reviewer signed |
| Known unknowns | Low isKnown, *measured* — the page-fault queue; the strict compiler's crystallization to-do list |
| Unknown unknowns | K-lines never minted, dereferences never attempted — no score exists; deopt is the detector that turns one into a known unknown |

And one more loop closes: Microsoft COM's root interface is IUnknown —
the whole object world already rests on the Unknown, and MOOLLM reads
directories as IUnknown facets
([hosting-moollm.md](hosting-moollm.md)). Korz′ upgrades the root
interface by one letter and one type: **IUnknown → isKnown**, boolean
interface to measured float.

## Paging latent space: K-line virtual memory

isKnown is the page fault detector; here is the fault handler. When an
important K-line dereferences below threshold, don't just improvise
cautiously — **page it in**: system call out to a web search or
vector-store lookup, distill what comes back, and cache it as a repo
file under the same K-line name
(`klines/gothic-victorian-newspaper.yml`, big-endian, greppable). Next
dereference hits the file instead of faulting.

The mapping is exact:

| Virtual memory | K-line paging |
|---|---|
| Virtual address | The K-line name |
| Backing store | Latent space and the web |
| RAM | The repo |
| Resident page | The cached file |
| Page fault | A dereference below the isKnown threshold |
| Fault handler | Search → distill → commit |

**The cache is editable and learnable.** Pages are YAML with
provenance comments — search date, sources, who distilled. Humans and
LLMs correct them in place; git versions every refinement. A wrong
page gets *fixed*, not just evicted.

**PR review is the memory integrity checker.** Paging in is a commit,
so every page-in can go through a pull request. The review agent reads
the new page's provenance, checks its claims against the cited
sources, and catches a bad page *before it becomes resident* — ECC for
the K-line cache, except the parity check is a literate review and the
correction is a diff. Hallucinations that survive distillation still
have to survive review. And unlike DRAM, a page that passes review is
*better* than its backing store: a reviewer signed it.

**Cache policy falls out of the two signals already on hand.**

- Page in when isKnown is low and usage is high.
- Leave latent when isKnown is high — the training data is the file.
- A paged K-line serves both tiers at once: the strict tier reads the
  file; the soft tier reads the file *plus* the activation.

**The repo already runs this by hand.** Every `sources/` directory in
this repository — papers fetched, hashed, and preserved so they
survive even if the site goes away — is a paged-in K-line. The
proposal just makes the librarian automatic and lets the dispatch
statistics decide what's worth shelving.

---

*Next: [sparse-shadow-trees.md](sparse-shadow-trees.md) — the one null
that was never a mistake: absence as delegation.*
