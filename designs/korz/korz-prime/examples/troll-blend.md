# The troll blend — ambiguity as a mixture, worn on the neck

*A [Korz example](README.md). Self-contained introduction; the second
half is MOOLLM-integrated. Teaches: the `ambiguity:` policy dimension,
coordinates as distributions, and why a blend is debuggable.*

## The cast, introduced properly

MOOLLM's adventure world keeps a character called **Two-Toll the
Troll**, a.k.a. the Cross-Platform Troll
([his directory](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/fictional/troll)).
The premise: the same troll guarded the Troll Room in *Zork* (1980)
and the chasm bridge in *Colossal Cave Adventure* (1977). Different
games, different payment protocols, same troll — he commuted, and
nobody noticed for fifty years. His character file gives him **one
soul and two minds**: a **zork-mind** whose currency is violence (a
bloody axe, all passages blocked) and an **adventure-mind** whose
currency is wealth (throw me a treasure, one per crossing). At any
moment he decides which mind **fronts** — speaks for the whole troll.
His tagline does the thesis for us: *"All gates are markets. The only
question is the currency."*

He is also — retconned canonical — **literally two-headed**, one head
per mind, more addable. Both games render in text; you never asked how
many heads, and he never volunteered.

## The mechanics: three slots, one selector

In Korz terms the troll is a bundle of slots guarded on a `world`
dimension:

```yaml
# sea/troll/greet.yml — three slots, one selector
- greet:
    guards: {rcvr: troll*, world: zork}
    do: The troll brandishes his axe and blocks the passage.

- greet:
    guards: {rcvr: troll*, world: adventure}
    do: The troll demands payment before you may cross the bridge.

- greet:
    guards:
      rcvr: troll*
      mood: ~                     # bare: any mood, bound into scope
    do: |
      Greet to fit {mood}; menace if provoked,
      grudging respect if they've beaten you.
```

Send `greet` with `{world: zork}` bound and the first slot wins —
unique most-specific match, classical Korz, nothing to discuss. The
interesting case is when *no* unique winner exists.

## Ambiguity as a policy dimension

Korz treats a tie between incomparable most-specific slots as an
**error** — the paper legislates specificity precisely so that
dispatch never has to judge. Korz′ ([design](../README.md)) turns the
response to ambiguity into a context dimension of its own:

| `ambiguity:` | Behavior | Ancestry |
|---|---|---|
| `error` | Refuse; report the tie | Korz |
| `arbitrary` | Pick one, don't care which | Linda tuple spaces |
| `sample` | Pick one at random (optionally weighted) | The Sims' find-best-N ([sibling example](sims-advertisements.md)) |
| `blend` | **Merge the matching bodies** | LLM method combination — no deterministic dispatcher can offer it, because it requires understanding what the bodies *mean* |

`blend` is the new species. A deterministic VM can interleave
bytecode from two methods only as nonsense; an LLM can read "brandish
the axe" and "demand the toll" and produce the troll who *leans on
his axe while quoting a price* — a genuine composition of meanings,
not of instructions.

## Coordinates as distributions

Now let the troll front **both minds at once**. The weights are just
more context bindings:

```yaml
context:
  rcvr: troll*
  world: {zork: 0.7, adventure: 0.3}    # a coordinate, promoted to a distribution
```

A coordinate became a distribution, dispatch became a mixture, and
the sample/blend distinction collapsed into a continuum — **sampling
is blending with all the weight on one slot.** At `{zork: 1.0}` you
have classical dispatch; at 50/50 you have full method combination;
everywhere between, a weighted composition the soft tier interprets.

## Debuggability by physiology

The standing objection to blending: no debugger can see inside a
mixture. The troll answers it anatomically. He has one head per mind,
and **head size displays the live fronting weight** — you know you're
in trouble when the bridge-toll head shrinks and the fighting head
swells. The dispatch mixture is worn as visible anatomy: state that a
classical debugger would need instrumentation to expose is simply
*rendered*, because in a world where the LLM narrates everything, the
cheapest inspector is a description the reader was going to get
anyway.

That generalizes past trolls. The
[hosting story](../hosting-moollm.md) lists "debugging symmetric
dispatch" as an IDE service the bare repo must replace; blend weights
worn as visible state are one of the replacements — put the
dispatcher's internal state *in the fiction*, and every transcript is
a trace.

## Where the canon goes deeper

MOOLLM-integrated trailheads, properly signposted: the troll's
[CHARACTER.yml](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/fictional/troll)
is written in yaml-jazz (comments are data — the LLM reads them);
his two-minds-one-soul shape is the worked instance of Soul City's
soul model (one mind per game, the soul portable between them); and
whether a slot with two time-parents should blend their clocks the
way the troll blends his heads is a live question in
[sparse-shadow-trees.md](../sparse-shadow-trees.md). Whether blending
is a feature or a horror is a per-dimension guard decision — which is
exactly where Korz likes to put such decisions — and whether *David*
buys any of it is on the agenda in [ask-david.md](../../ask-david.md).
