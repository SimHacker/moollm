# One-Step Trap — temporal abstraction in MOOLLM simulations

Rich Sutton ([essay](http://incompleteideas.net/IncIdeas/OneStepTrap.html), Jul 2024) · HN [48883415](https://news.ycombinator.com/item?id=48883415)

**Trap:** treat `f(t+1)` iterated N times as a plan for `f(t+N)`. Errors compound; stochastic futures are trees; cost explodes.

**Fix:** **options** and **GVFs** — temporally abstract models. Plan at the scale you care about; fill micro-detail on demand.

MOOLLM's simulation stack already prefers this architecture. This doc ties Sutton to skills and to the field product [Urban eBike Safari](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/ideas/urban-ebike-safari.yml).

## MOOLLM mapping

| Sutton / HN | MOOLLM skill | How |
|-------------|--------------|-----|
| One-step rollout | **anti-pattern** | Don't plan by simulating every micro-transition |
| Options (semi-MDPs) | [adventure](../adventure/) | `GO`, `LOOK`, `TAKE`, `USE` — verbs on abstract locations |
| Graph edges | [exit](../exit/) | Room-to-room links; guards = option preconditions |
| Discrete game time | [simulation](../simulation/) + [time](../time/) | `TICK` advances **turns**, not physics integration steps |
| Narrative duration | [time](../time/) | LLM judges "until morning" — not iterated wall-clock |
| Spatial memory | [memory-palace](../memory-palace/) | Method of loci; iLoci lineage in WWSFF |
| Seeds not full sim | [simulator-effect](../simulator-effect/) | Implication beats simulation — allied constraint |
| Voice commands | [speech](../speech/) | Parser layer; field STT (SpeechAnalyzer) on bike |
| Hierarchical detail | [adventure](../adventure/) `pickDescription(lod)` | glance → look → examine on demand |
| Data as rooms | [adventure](../adventure/) PSIBER | Enter YAML at `#fragment`; drill down when needed |

## ssivark: tyranny of the specific

Conference trip: flight legs + "15–18 hours," not every turn to the airport. **Hierarchical zoom.**

| Layer | Urban eBike Safari | Text adventure |
|-------|-------------------|----------------|
| Abstract | "Take me to next Invader" | `GO north` to `canal/` |
| Commit | `SET DESTINATION` → Bosch route | Exit traversal |
| Micro | Turn-by-turn (display only) | `LOOK` / `EXAMINE` when stopped |

Voice plans **story legs**. Map fills **traffic lights** only after commit.

## What MOOLLM simulations should do

```yaml
good:
  - Player issues option-level command (verb + target)
  - TICK once per meaningful state change (room entry, not every sentence)
  - LLM narrates outcome; git commits the turn
  - Exits declare reachable abstract states
  - pickDescription(lod) defers detail until requested

avoid:
  - Rolling out N implicit micro-steps to answer "what happens next?"
  - Treating each LLM token as a simulation timestep
  - Building a world-model rollout for navigation planning
  - Turn-by-turn as primary UX while hands are busy (bike, tools)
```

## Field product (WWSFF)

Don Hopkins source room: [sutton-one-step-trap.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/sources/sutton-one-step-trap.md)

- Scene cards at POIs = temporally abstract stops
- Virtual focus hops graph without exposing structure
- StoryMaker / iLoci / DreamScape lineage = options on places, not tile physics

**Ride game (steering + pie + VoyStick):** [urban-safari-steering-voystick-pie-network.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/sources/urban-safari-steering-voystick-pie-network.md) · [examples/urban-safari-ride-game.yml](examples/urban-safari-ride-game.yml)

Continuous AI guess/suggest; pie-menu network navigated by biking; handlebar steering = steering law; VoyStick warble for wedge selection outdoors.

## Related skills (read order)

1. [simulation/GLANCE.yml](GLANCE.yml) → [CARD.yml](CARD.yml) → [SKILL.md](SKILL.md)
2. [adventure/SKILL.md](../adventure/SKILL.md) — reference implementation of options
3. [time/CARD.yml](../time/CARD.yml) — turns ≠ iterations
4. [simulator-effect/CARD.yml](../simulator-effect/CARD.yml) — don't over-simulate
5. [examples/one-step-trap.yml](examples/one-step-trap.yml) — machine-readable cross-links
6. [examples/urban-safari-ride-game.yml](examples/urban-safari-ride-game.yml) — steering pie VoyStick field UX

## References

- Sutton, Precup, Singh (1999) — options framework
- Sutton et al. (2011) — Horde / GVFs
- Sutton et al. (2023) — reward-respecting subtasks
- ssivark [arXiv:2410.05364](https://arxiv.org/abs/2410.05364) — multi-step world models vs temporal abstraction
