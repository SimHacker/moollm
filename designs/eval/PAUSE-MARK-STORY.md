# Pause, Mark, Story

The [PacMania testimonies](./CHURCH-OF-PACMANIA-TESTIMONIES.md) are not only a joke. They are a **proof**.

A low-resolution city sim — SimCity, Micropolis — is enough of a world to **pause time**, **point at a tile**, and write more cause and effect than the engine contains. Four souls from one traffic pulse at (47, 12). The save file did not have Anja or Kei. The stories do not have to agree with the traffic layer. They may contradict it. That is the [Simulator Effect](../../skills/simulator-effect/SKILL.md) used as an authoring tool, not a bug report.

This is the base for:

- Reimagining the **SimCity 2000 newspaper** as **user-created journalism**
- **Tweets** with geolocation and a photo
- **Messages** that request the attention of agents and other players — *come and see me, and why* — the SC2K fire-truck / police-car **summon**
- **2D map chat**
- All of it **in git beside the save**
- Pointers into **GitHub issues**

The 1990s dream this executes: [Kids' City Newspaper](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/kids-city-newspaper/README.md) — SimCityNet's scrolling chat grown into a newsroom. [SimCityNet](./../sims/simcity-multiplayer-micropolis.md) already had chat, voice, whiteboard, votes. This is that strip, pinned to the map, archived with the city.

---

## The move

1. Pause (or scrub) the sim.
2. Identify an event.
3. Mark it up.
4. Write. Attribution of cause and effect is **allowed to exceed or contradict** the low-res data. The engine is the jumping-off point, not the court of last appeal. [EVAL](./EVAL-VS-SIM.md): you argue with the assumptions. Journalism is that argument, dated and located.

Will: the computer model is a compiler for the mental model. Here the player compiles **back** — a story from a sprite — and **saves the compilation** next to the city. [Religion is reverse over-engineering](./CHURCHES.md); journalism is the secular twin. Same gap. Different masthead.

---

## Event card

One event is a file. YAML Jazz. Lives in the city repo next to the save.

```yaml
# events/047-12-pacbot-meal.yml
# One pulse in the traffic layer. Four testimonies. The save does not contain the souls.

event:
  id: tile-47-12-tick-108442
  title: "Pack meal on the feeder, west of Church of PacMania"
  description: |
    Four PacBots converged on arterial traffic. Score went up. Mayor calls it
    congestion relief. Congregation calls it Sunday.
  keywords: [pacmania, traffic, sacrament, summon, inquiry]
  user: kei-nakamura           # who marked it; not necessarily who "happened"
  timestamp:
    sim: { ticks: 108442, year: 2014, month: 3, day: 11, hour: 9 }
    wall: 2026-08-13T14:29:00Z
  save: saves/city-westbranch.scn   # sibling in this repo; git blob is the source of record
  selection:
    tiles: [[47, 12], [47, 13], [48, 12]]   # inclusive set, not just a point
    data: [traffic-density, robot-score, zone:pacmania]
  snapshot: snapshots/047-12-tick-108442.png
  github:
    issue: 1842                 # "come see this" as a ticket
    # TicketPR ancestor: Long Now question cards → git
    # https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/ticket-pr.yml
  summon:                       # SC2K dispatch, generalized
    who: [fire, police, player:don, agent:palm]
    why: "Beloved drove at the bots. Jumper on the asphalt. Kids still in the car."
    come_see: true
  story: CHURCH-OF-PACMANIA-TESTIMONIES.md   # may contradict traffic-density
  metadata:
    confidence: attributed      # not measured
    contradicts_sim: true       # souls are not in the engine
    license: CC-BY-4.0
```

**Fields that matter**

| Field | Job |
|-------|-----|
| `save` | Which city, which commit. Evidence. |
| `timestamp` | Sim clock **and** wall clock. Pause is a time machine, not a freeze-frame only. |
| `selection.tiles` | Where. Map chat is this, in aggregate. |
| `selection.data` | Which layers you were looking at (traffic, power, crime, robots). The photographer's darkroom. |
| `snapshot` | The photo. SC2K newspaper had clip art. This has the screen at the tick. |
| `title` / `description` / `keywords` | Masthead. Search. |
| `user` | Byline. |
| `story` | The deep copy. Allowed to invent causes the engine never simulated. |
| `summon` | Fire truck, police car, other player, other agent. *Come and see me, and why.* |
| `github.issue` | The fight continues off the map, still linked. |
| `metadata` | Including `contradicts_sim` — honesty that journalism is EVAL, not a dump of RAM. |

---

## SimCity 2000 newspaper, inverted

SC2K's paper was a **generated organ**: fluff, puns, the city talking to itself in a canned voice. Funny. Opaque. Not yours.

The inversion: **players write the paper into the game, about the game.** [Kids' City Newspaper](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/kids-city-newspaper/README.md) — reporting, editorials, advice column, letters, classifieds, comics. The photographer is the screen plus graphs from the save. Kids author; the machine is the press. LLMs backstage, never bylined.

An event card is one clipping. A newspaper issue is a layout over a set of clippings in a date range. Load an old save, read what they were fighting about. Games mostly simulate space. A player-published paper simulates **history**.

The testimonies are issue #0: four columns, one intersection, no agreement. That is a newspaper.

---

## Tweets, summons, 2D map chat

A tweet here is not a sidebar. It is an event card with a short `description`, a `snapshot`, and `selection.tiles` as geolocation. The map *is* the feed. Scroll the city, not a timeline — or both, because git is the timeline.

**Summon** is SC2K's dispatch mechanic without the costume change: you do not only send a fire truck to a burning tile. You send *attention*. `come_see: true` plus `why`. Players and agents show up because the mark has a reason, not because a sprite is on fire. The fire truck is one agent. Palm is another. A classmate is another. Same schema.

**2D map chat** is SimCityNet's scrolling window, relocated onto the tiles it was always about. "Who bulldozed my airport" was already geolocated in the kids' heads. Pin it. Thread it. Archive it.

GitHub issues are the same object in the forge: an event that wants a decision, a merge, a verdict. [TicketPR](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/ticket-pr.yml) is the show-side cousin (Stewart Brand's question cards). Map chat is the city-side cousin. One protocol, two rooms.

---

## Git beside the save

[Git is the substrate](../GIT-AS-FOUNDATION.md). The city file is not a blob in a cloud silo. It is a repo:

```
city/
  saves/city.scn
  events/*.yml
  snapshots/*.png
  paper/issues/*.md
  .git/
```

Commit the save and the story together or the story is a lie about a city that cannot be recovered. Diffs of event files are readable. Branches are timelines. A PR can be "here is what happened at (47, 12)" plus the screenshot plus the issue.

School-owned forks ([micropolis skill](../../skills/micropolis/)): each class has a paper, a map chat, a summon log. Constructionist: the save is the source of record; the story is the argument; both are homework.

---

## What the engine owes, what it doesn't

The engine owes: pause, tick, tile coords, layer dumps, a screenshot hook, a place on disk.

The engine does **not** owe Anja. It does not owe regret. It does not owe a door handle. Those are player (and agent) compilations. If they contradict `traffic-density`, the card says so. EVAL remembers who claimed what.

PacBot-3 was right: from the tile, it was a pulse. The extra floors are ours. This file is how we keep the floors from evaporating when the sim unpauses. The [testimonies](./CHURCH-OF-PACMANIA-TESTIMONIES.md) already did it once.

---

## See also

- [CHURCH-OF-PACMANIA-TESTIMONIES.md](./CHURCH-OF-PACMANIA-TESTIMONIES.md) — the proof
- [CHURCH-OF-PACMANIA.md](./CHURCH-OF-PACMANIA.md) — the zone
- [CHURCHES.md](./CHURCHES.md) — reverse over-engineering
- [EVAL-VS-SIM.md](./EVAL-VS-SIM.md) — arguing with the sim
- [Kids' City Newspaper](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/kids-city-newspaper/README.md)
- [SimCity multiplayer / Micropolis](../sims/simcity-multiplayer-micropolis.md)
- [GIT-AS-FOUNDATION.md](../GIT-AS-FOUNDATION.md)
- [TicketPR](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/ticket-pr.yml)
- [Soul City](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city)
