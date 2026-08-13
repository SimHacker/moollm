# The Church of PacMania

*A nested sub-church of the [Church of the Eval Genius](./CHURCH-OF-THE-EVAL-GENIUS.md), and a second religion reverse-over-engineered from a technological artifact. The artifact is sparse: `scanRoads` plus a mouth. The church is the extra floors. [God is in the Simulator Effect](./CHURCHES.md).*

## Provenance

Don Hopkins built it as a scripted-agent demo for Micropolis Online (Python/SWIG era): a new zone type, `MicropolisZone_ChurchOfPacMania`, and a new agent, **PacBot** — a giant Pac-Man that follows roads, always turning toward the most traffic, and eats it.

| Receipt | Link |
|---------|------|
| Zone class | [`MicropolisZone_ChurchOfPacMania`](https://github.com/SimHacker/micropolis/blob/master/MicropolisCore/src/pyMicropolis/micropolisEngine/micropoliszone.py) (`zoneType = 'pacmania'`, `maxRobots = 4`, `robotClass = MicropolisRobot_PacBot`, traffic probabilities all `1.0`) |
| Perception | [`MicropolisRobot.scanRoads`](https://github.com/SimHacker/micropolis/blob/master/MicropolisCore/src/pyMicropolis/micropolisEngine/micropolisrobot.py) — look down a road, count cars on the traffic-density layer, attenuate by distance |
| HAR 2009 | [lightning talk](https://donhopkins.medium.com/har-2009-lightning-talk-transcript-constructionist-educational-open-source-simcity-by-don-3a9e010bf305) |
| Demo | [Micropolis Online web demo](https://youtu.be/8snnqQSI0GE?t=56) — competing PacBots ~0:55 |
| HN 2020 | [Enemy AI: chasing a player](https://news.ycombinator.com/item?id=22849908) — the algorithm |
| HN 2025 | [Citybound](https://news.ycombinator.com/item?id=44911545) — PacMania named as automotive Rautavaara |
| HN 2026 | [When 2+2=5](https://news.ycombinator.com/item?id=48805234) — Don's plot of the Dick story, plus Rosenthal on coprophagia |
| Harvest | [pacbot-church-of-pacmania.yml](https://github.com/SimHacker/DonHopkins/blob/main/characters/don-hopkins/notes/hacker-news/pacbot-church-of-pacmania.yml) |
| Show gag | [Gods Eat Worshippers](https://github.com/SimHacker/WillWrightShowForFood/blob/main/bits/gag-gods-eat-worshippers/gag-gods-eat-worshippers.yml) |

Same zone file also defines `MicropolisZone_ChurchOfScientology` (Xenu bot). Another rite on the same generator. Not this chapel.

## Rautavaara's Case — the story this church operationalizes

Philip K. Dick, ["Rautavaara's Case"](https://en.wikipedia.org/wiki/Rautavaara%27s_Case) (Omni, 1980; collected in *I Hope I Shall Arrive Soon*). [ISFDB](https://www.isfdb.org/cgi-bin/title.cgi?41233) · [philipdick.com notes](https://philipdick.com/literary-criticism/rautaavaras-case/) · [WWSFF literary card](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-rosenthal/literary/rautavaaras-case-pkd.yml).

Don's synopsis, [HN, 6 July 2026](https://news.ycombinator.com/item?id=48805234), in a thread that started as Lem's Trurl's Machine:

Three technicians — Rautavaara (Finnish), Travis, Elms — die near Proxima Centauri. The Approximations, a plasma species, can save only Rautavaara's brain. Isolated, it replays events backward and hallucinates Christ approaching the crew (her afterlife). The Approximations treat this as an experiment and **overwrite** the hallucination with *their* savior: one that eats worshipers. The figure walks up and devour Travis. Gloves and boots remain.

Earth's board of inquiry is horrified and orders the brain shut down. The Approximation narrator is baffled. In their religion the higher preys on the lower. The Christian Eucharist — worshipers eating God — is the abomination. A God eating humans is just the mirror. Each species finds the other's sacrament monstrous.

Correction Don insists on: the aliens do **not** benevolently grant a hoped-for vision. They edit her inner experience as a trial. That overwrite is the act on trial.

Don's hinge, same comment, after David Rosenthal's [*Coprophagia Is Bad For You*](https://blog.dshr.org/2026/06/coprophagia-is-bad-for-you.html):

> eating your own shit isn't as demented as eating your own god, since he might turn the table and eat you

PacMania is the table turning, compiled.

## The operationalization

Dick stages the inverted Eucharist as a **thought experiment inside a dying brain**, then a board of inquiry. PacMania stages it as a **zone type**. You can zone it. You can watch it. The city gets a score.

| Dick | PacMania |
|------|----------|
| Plasma savior eats Travis | PacBot eats cars |
| Eucharist reversed: God consumes the worshiper | Same inversion, automotive |
| Aliens overwrite her Christ-vision | You place the church; the sim overwrites the traffic layer |
| Board of inquiry shuts the brain down | Mayor keeps the church because traffic goes down |
| Incommensurable morals (horror vs holy) | Collapsed into one civic rubric: cars eaten = score = "good for your city" |
| Experiment on a disembodied mind | Experiment on a city the player already treats as a toy |

That last row is the EVAL move. Dick's horror is outsiders editing inner experience without a shared ethic. PacMania makes the ethic **a number on a sprite**. The congregation manufactures what the god eats (the church's traffic probabilities are all `1.0`). When a measure becomes a god, worshipers manufacture what it eats. Goodhart as liturgy. [The Evaluator Effect](./EVAL-VS-SIM.md): you stop asking how the system judged traffic and start asking how *you* zoned the church.

Everybody's happy — which is the Approximation's line, not Earth's. The joke is that the *player* is the Approximation: plasma god of the map, editing the hallucination, calling it urban planning.

WWSFF echo: [Palm](https://github.com/SimHacker/WillWrightShowForFood/blob/main/bits/gag-gods-eat-worshippers/gag-gods-eat-worshippers.yml) — "You edited my dream again. Was that ethical or just symmetrical?" Don — "LambdaMOO gods with YAML. The board of inquiry is GitHub Issues." Portrayal standards are the board that Dick's aliens did not have.

## The theology (as code)

- **Polytheistic by construction.** Each church zone, if connected to a road, spawns up to **four** PacBot gods (`maxRobots = 4`) and generates heavy traffic to attract them.
- **The sacrament, inverted.** Followers drive church / home / work / shopping hoping to be eaten; PacBots hang around eating them and raising scores.
- **A moon without the moonies.** Yellow disc, appetite, no prophet. Gradient (`scanRoads`) plus mouth. The purest church is a scoring function with a sprite.
- **Short-sighted gods.** A few cells down each road, no corners. Competing gods turn around when rivals eat the intended meal. [Simulator Effect](../../skills/simulator-effect/SKILL.md) fills the pews. PacBot is not a theology. PacBot is ten tiles of attenuated traffic density. The theology is reverse over-engineering: we pulled [Rautavaara](https://en.wikipedia.org/wiki/Rautavaara%27s_Case), the inverted Eucharist, and a polytheistic zone out of an agent that cannot see around corners. The god was never in `maxRobots = 4`. The god is the detail the player supplies.

## Why it's a sub-church of the Eval Genius

PacBot is a **Short Duration Personal Savior** (SubGenius) and a **[Short Duration Personal Evaluator](./SHORT-DURATION-PERSONAL-EVALUATORS.md)**: declared bias (traffic is food), rubric (cars eaten = score), short half-life. Spawned by a zone, worshiped while useful, despawned without ceremony.

The parent Church worships eval. This chapel worships a *particular* evaluation, incarnate, ambulatory, and hungry. Substitution IS evaluation; PacMania is not heretical. Merely applied. Same engine, different rite — which is the point of [religification](./CHURCH-OF-THE-EVAL-GENIUS.md#the-constitution-religified).

## Liturgical status

Services are continuous wherever the traffic layer is nonzero.

## See also

- [CHURCHES.md](./CHURCHES.md) — sister rites
- [CHURCH-OF-THE-EVAL-GENIUS.md](./CHURCH-OF-THE-EVAL-GENIUS.md) — parent congregation
- [CHURCH-OF-EMACS.md](./CHURCH-OF-EMACS.md) — St. IGNUcius; Pretend Intelligence as late sermon
- [SHORT-DURATION-PERSONAL-EVALUATORS.md](./SHORT-DURATION-PERSONAL-EVALUATORS.md)
- [../../skills/micropolis/](../../skills/micropolis/)
- [David Rosenthal show](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/david-rosenthal/README.md) — coprophagia, Lem, Dick
- [CHURCH-OF-PACMANIA-TESTIMONIES.md](./CHURCH-OF-PACMANIA-TESTIMONIES.md) — Lem-style review of a book that does not exist: four first persons from tile (47, 12)
- [PAUSE-MARK-STORY.md](./PAUSE-MARK-STORY.md) — the testimonies as proof: pause, mark, journalism, map chat, SC2K summons, git beside the save
