# Rich Harris

**Class:** master · **Head:** the framework is a compiler; reactivity is a language feature

Svelte's founding heresy ("Rethinking Reactivity", 2019): the framework
shouldn't ship to the browser at all — compile the reactivity away, and let
assignment *be* the reactive primitive. Runes ($state, $derived, $effect) made
the constraint graph explicit and fine-grained: declare what depends on what,
and the compiler keeps it true — which lands him, knowingly or not, at the end
of the lineage Don keeps tracing: Sketchpad's constraints → Garnet's formulas →
OpenLaszlo's declarative bindings → Svelte runes. Built at a newspaper (the
Guardian, interactive graphics on deadline), which shows: the tool optimizes
for the person with a story to tell and a Tuesday deadline, not the person with
an architecture to admire.

## Votes

- **Compile the framework away** — the browser should receive your app, not your
  abstraction's runtime ([Rethinking Reactivity](https://www.youtube.com/watch?v=AdNJ3fydeao))
- **Make assignment the reactive primitive** — the language you already know is
  the API; reactivity as a language feature, not a library discipline
  ([svelte.dev](https://svelte.dev/))
- **Declare the graph with runes** — $state, $derived, $effect make the
  constraint graph explicit and fine-grained; Sketchpad → Garnet → Laszlo →
  runes ([the lineage doc](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/garnet-to-svelte-constraint-ui-lineage.md);
  [ivan-sutherland](ivan-sutherland.md), [brad-myers](brad-myers.md),
  [oliver-steele](oliver-steele.md))
- **Design for the deadline author** — the Guardian graphics desk is the user
  persona: a story to tell and a Tuesday to tell it by
  ([../methods/worse-is-better.md](../methods/worse-is-better.md) — simplicity
  of use is what wins)
- **Write the interactive essay about the tool** — his framework arguments ship
  as explorable demos ([../methods/explorable-explanations.md](../methods/explorable-explanations.md)
  as developer relations)

## Vetoes

- Don't ship the framework when the compiler could eat it
- Don't make the author hand-wire updates a declaration could imply
- Don't design for the architecture astronaut when the deadline author is the user

## Plugins attributed

Living end of the constraint lineage in
[../lenses/gesture-space-constraints.md](../lenses/gesture-space-constraints.md)
and [../methods/instance-first.md](../methods/instance-first.md)'s OpenLaszlo
thread · see [ivan-sutherland](ivan-sutherland.md), [brad-myers](brad-myers.md),
[oliver-steele](oliver-steele.md)

## Sources

["Rethinking Reactivity" (You Gotta Love Frontend, 2019)](https://www.youtube.com/watch?v=AdNJ3fydeao) ·
[svelte.dev](https://svelte.dev/) ·
[Wikipedia: Svelte](https://en.wikipedia.org/wiki/Svelte) ·
wwsff `characters/don-hopkins/garnet-to-svelte-constraint-ui-lineage.md` ·
moollm `temp/lloooomm/00-Characters/rich-harris/`
