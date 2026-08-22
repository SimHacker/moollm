# Craig Reynolds

**Class:** master · **Head:** behavior is cheaper than choreography

Boids (1987): three local steering rules — separation, alignment, cohesion — and
a flock appears, with no flock anywhere in the code. The demonstration that
lifelike group behavior is an emergent property of individual perception, not a
global script: nobody choreographs the murmuration. "Steering Behaviors for
Autonomous Characters" (GDC 1999) turned the insight into an engineering toolbox
— seek, flee, pursue, wander, arrive — that every game AI crib sheet since has
copied. The design method: give each agent a tiny sensorium and a tiny will,
then tune weights until the crowd looks alive. Choreography scales linearly;
behavior scales for free.

## Votes

- **Steer the bird, get the flock free** — three local rules, no global
  choreography, and the murmuration emerges
  ([boids](https://www.red3d.com/cwr/boids/);
  [../methods/tuned-emergence.md](../methods/tuned-emergence.md))
- **Give each agent a tiny sensorium and a tiny will** — local perception plus
  weighted desires; The Sims' needs-driven agents are boids with furniture
  ([../methods/find-best-n-dither.md](../methods/find-best-n-dither.md))
- **Ship the toolbox, not just the demo** — seek, flee, pursue, arrive, wander:
  [Steering Behaviors](https://www.red3d.com/cwr/steer/) named the primitives and
  every game AI since composes them
- **Prefer behavior to animation** — a steering rule survives level changes,
  obstacles, and player chaos that canned paths can't
  ([ken-perlin](ken-perlin.md)'s Improv casts the same vote for character motion)
- **Weight and blend, don't arbitrate** — conflicting desires resolve by mixing
  forces, not by if-else; the blend is where the lifelike lives

## Vetoes

- Don't script the flock — steer the bird
- Don't give the agent more perception than the behavior needs
- Don't animate what a rule would keep alive under change

## Plugins attributed

The agent-level mechanics of [../methods/tuned-emergence.md](../methods/tuned-emergence.md)
and [../methods/find-best-n-dither.md](../methods/find-best-n-dither.md) — The
Sims' motive-driven agents are boids with furniture · see
[will-wright](will-wright.md), [john-conway](john-conway.md)

## Sources

"Flocks, Herds, and Schools: A Distributed Behavioral Model" (SIGGRAPH 1987) ·
["Steering Behaviors for Autonomous Characters" (GDC 1999)](https://www.red3d.com/cwr/steer/) ·
[red3d.com/cwr/boids](https://www.red3d.com/cwr/boids/) — his own boids page ·
[Wikipedia: Boids](https://en.wikipedia.org/wiki/Boids)
