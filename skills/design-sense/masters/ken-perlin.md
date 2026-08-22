# Ken Perlin

**Class:** master · **Head:** controlled randomness; the sketch that computes

Perlin noise (1983, for *Tron*; the only Academy Award ever given for a
procedural texture function): structured pseudo-randomness — smooth, band-limited,
infinitely detailed — the primitive underneath every procedural cloud, marble
slab, terrain, and flame since. The insight wasn't randomness, it was *tunable
coherence*: nature looks random at every scale but correlated between scales,
and one function can fake that. Improv: procedural animation where characters
have persistent personality noise instead of canned clips. Chalktalk: drawings
that come alive — sketch a shape, and it becomes a working simulation you can
wire to other sketches, Bret Victor's dynamic media with a blackboard accent.

## Votes

- **Correlate the randomness across scales** — nature is random at every zoom but
  coherent between zooms; one octave-summed function fakes the universe
  ([Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise);
  [his reference implementation](https://mrl.cs.nyu.edu/~perlin/noise/) fits on
  a page)
- **Give characters personality noise** — Improv's actors wobble with persistent
  procedural character instead of replaying clips
  ([craig-reynolds](craig-reynolds.md)' steering, aimed at expression;
  [../methods/emergence-nuance-slider.md](../methods/emergence-nuance-slider.md))
- **Make the sketch compute** — Chalktalk: draw a pendulum, get a pendulum; the
  blackboard is a runtime ([Chalktalk on GitHub](https://github.com/kenperlin/chalktalk);
  [../methods/explorable-explanations.md](../methods/explorable-explanations.md))
- **Put the demo where the paper is** — his homepage is applets all the way
  down; the argument runs in the browser
  ([everything-is-concrete](../methods/everything-is-concrete.md) for research)
- **Optimize until it's a primitive** — noise won an Oscar because it was fast
  enough to be *everywhere*; performance is what turns a technique into a
  material

## Vetoes

- Don't use uniform randomness where nature is correlated across scales
- Don't can the animation a function could keep alive
- Don't let the sketch stay dead — a drawing is a program that hasn't run yet

## Plugins attributed

Texture-level engine of [../methods/tuned-emergence.md](../methods/tuned-emergence.md) ·
Chalktalk is kin to [../methods/explorable-explanations.md](../methods/explorable-explanations.md)
and [../methods/reverse-diagrams.md](../methods/reverse-diagrams.md) gone live

## Sources

"An Image Synthesizer" (SIGGRAPH 1985) ·
[Wikipedia: Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise) ·
[Wikipedia: Ken Perlin](https://en.wikipedia.org/wiki/Ken_Perlin) ·
[Chalktalk (GitHub)](https://github.com/kenperlin/chalktalk) ·
[mrl.cs.nyu.edu/perlin](https://mrl.cs.nyu.edu/perlin/) — including his noise-in-one-page reference code
