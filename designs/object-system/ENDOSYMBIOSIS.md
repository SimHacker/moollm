# Endosymbiosis: Composition the Margulis Way

Lynn Margulis argued in 1967 (*On the Origin of Mitosing Cells*) that
mitochondria and chloroplasts were once free-living bacteria. A larger
cell engulfed them and, instead of digesting them, kept them. They
retained their own DNA, kept dividing on their own schedule, and traded
services — ATP, photosynthesis — for room and board. The theory was
ridiculed for a decade and then confirmed by genetics: mitochondria
really do carry their own genome, closer to bacterial DNA than to their
host's.

The eukaryotic cell was not *designed* with an energy subsystem. It
**swallowed one that already worked.** That is the composition model
MOOLLM uses, and it is different from the metaphors software usually
reaches for:

| Metaphor | The component is | Co-evolution |
|---|---|---|
| Library | Dead code you link | None — you upgrade versions |
| Service / API | Remote, behind a contract | Independent, negotiated |
| Framework | The host; *you're* the organelle | You conform to it |
| **Organelle** | **Alive, local, self-describing, running its own genome** | **Continuous, both directions** |

## The mapping

- **Engulfment without digestion.** A whole working system is taken in
  as a live component — not rewritten, not ported, not wrapped until
  unrecognizable. It keeps its shape and its habits.
- **Retained genome.** The organelle carries its own source code, in its
  own original language, still readable, still executable. This is the
  load-bearing part: because the genome is retained, the organelle can
  still replicate (`cp -r`), still be studied, still be lifted.
- **Metabolic trade.** The organelle advertises services to its host —
  Sims-style [advertisements](../GAME-PIECES.md), CARD.yml interfaces —
  and the host supplies context, activation, and a place to live.
- **Gene transfer to the nucleus.** Over evolutionary time, organelle
  genes migrate into the host's nuclear genome. Software version: rulings
  and behaviors proven inside the organelle get lifted into the host's
  own slot space — the adventure compiler crystallizing LLM improvisations
  into deterministic guards, house rules appending organelles to the
  commons. The organelle keeps working while the host absorbs what it
  learned.
- **Vertical inheritance.** Clone the host and the organelles come along,
  genomes intact.
- **Latent-space endosymbiosis.** Inheriting by name from training data
  ([LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md)) is engulfing
  an organism that lives in latent space — and the host can filter,
  modulate, and rename what it takes in ("inherit Self's clone semantics,
  but rename `clone` to `incarnate` and add consent"), which is exactly a
  host cell regulating organelle gene expression.

## The specimens

Live examples, in [adventure-4](../../examples/adventure-4/) and beyond:

- **The Cross-Platform Troll**
  ([characters/fictional/troll/](../../examples/adventure-4/characters/fictional/troll/))
  — one character who swallowed two game worlds. His zork-mind and
  adventure-mind are organelles with their own
  [realms](../../examples/adventure-4/characters/fictional/troll/realms/):
  navigable microworld vignettes running *inside* him, each with its own
  ecology and physics.
- **Wumpus-Snorax's built-in game cartridge**
  ([characters/fictional/wumpus-snorax/](../../examples/adventure-4/characters/fictional/wumpus-snorax/))
  — a character whose mitochondria are literally his genome: his own
  source code in four editions
  ([sources/](../../examples/adventure-4/characters/fictional/wumpus-snorax/sources/):
  two 1970s BASICs, V7 C, BSD C, each with a code-review sidecar),
  plug-in cave topologies, and templated hazard pieces that instantiate
  into any cave. You can read him, run him, and replicate him.
- **The coatroom grue**
  ([coatroom/](../../examples/adventure-4/coatroom/)) — an organism from
  Zork's ecology living in another world's closet, its dark-detection
  trigger wired to the *host* world's light levels. A transplanted
  organelle metabolizing local conditions.
- **Cross-game playing pieces** —
  [turing-chess](../../skills/experiment/experiments/turing-chess/) and
  its [revolutionary-chess](../../skills/experiment/experiments/turing-chess/plugins/revolutionary-chess/)
  plugin: pieces and characters from different games interoperating in
  one space, house rules arriving as new organelles the game absorbs
  mid-play.
- **Ebike safari** — a geographic platform
  ([design cauldron](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/ebike-safari/design))
  whose host cell is the city map itself: games, utilities, guides,
  storytelling, and tools ride it as organelles sharing one
  place-and-time substrate.
- **Real and imaginary maps, linked** — MOOLLM characters play on maps
  of real and imagined spaces and create doors between them: walk in the
  front door at a real street address and you're transported into a
  MOOLLM map of the home
  ([HOME-AUTOMATION-MEMORY-PALACE](../HOME-AUTOMATION-MEMORY-PALACE.md)),
  where household, pet, and home-automation organelles live. The same
  host organizes its keeper: Don uses MOOLLM to run his home, himself,
  [Will Wright Show For Food](https://github.com/SimHacker/WillWrightShowForFood),
  the repo shows, and Micropolis / Soul City development
  ([LIVE-OBJECTS-EXAMPLES](LIVE-OBJECTS-EXAMPLES.md)).

## Why the biology matters

Margulis's point was that major evolutionary novelty comes from
**symbiotic merger, not gradual mutation** — new kinds of organism arise
when previously independent living systems combine and stay alive inside
each other. The Korz paper's conclusion makes the software version of
the claim: a particular combination of concepts, each well-known from
the past, can be "more powerful than the sum of its parts." MOOLLM's bet
is the same bet — selfish prototypes, leaning into the training, YAML
jazz, empathic templates, K-lines — each an already-living organism,
swallowed whole with its genome intact, chosen because they reinforce
each other harmonically rather than merely coexist.

Related: [SELF-AND-MOOLLM](SELF-AND-MOOLLM.md) ·
[LATENT-SPACE-INHERITANCE](LATENT-SPACE-INHERITANCE.md) ·
[GAME-PIECES](../GAME-PIECES.md) ·
[LIVE-OBJECTS-EXAMPLES](LIVE-OBJECTS-EXAMPLES.md) ·
[LEGACY-MIGRATION](../LEGACY-MIGRATION.md) — engulfment applied to a
legacy app: containerize it with its genome intact, then absorb what it knows
