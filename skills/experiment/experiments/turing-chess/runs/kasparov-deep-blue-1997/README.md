# Kasparov vs Deep Blue — Game 6, May 11, 1997

The day everything changed.

## Overview

This run simulates the historic final game of the 1997 rematch between World Chess Champion Garry Kasparov and IBM's Deep Blue. Deep Blue won, becoming the first computer to defeat a reigning world champion in a match.

## The Simulation

Unlike a simple game replay, this is **full-theater simulation**:

- **Dual Commentary**: Howard Cosell (sports drama) and James Burke (historical connections)
- **Curated Audience**: Hand-picked from history and fiction for maximum dramatic impact
- **Spy Mic Coverage**: Captures individual conversations and reactions
- **Kiss Cam Moments**: Meaningful glances between human and robot attendees
- **Grafana Dashboard**: Deep Blue's internal state visualized in real-time
- **Mythic Framing**: John Henry inheritance — man vs machine through the ages

## The Audience

### Human Section
- **Chess Legends**: Bobby Fischer, Anatoly Karpov, Judit Polgár
- **Computing Pioneers**: Claude Shannon, Marvin Minsky, John McCarthy
- **Philosophers**: John Searle, Daniel Dennett, Douglas Hofstadter
- **Spirit Seats**: Alan Turing (photograph), Sun Tzu (scroll), Mikhail Tal (empty chair)
- **Family**: Klara Kasparova, Regina Fischer (mothers of prodigies)

### Robot Section
- **Household**: Roomba, AIBO
- **Industrial**: FANUC welding arm, KUKA assembly robot
- **Fictional**: C-3PO, R2-D2, Tin Man, Data, HAL 9000, WALL-E, Terminator
- **Research**: Shakey (first AI robot), Kismet (emotional robot)
- **Space**: Voyager Golden Record, Mars Pathfinder Sojourner

## File Structure

```
kasparov-deep-blue-1997/
├── README.md           # This file
├── RUN-000.yml         # Complete run configuration
└── templates/
    └── RUN-000.yml.tmpl  # Template for creating new runs
```

## Creating New Runs

1. Copy the template: `cp templates/RUN-000.yml.tmpl ../new-match/RUN-000.yml`
2. Fill in the `{{placeholders}}`
3. Customize audience for your specific dramatic needs

## Key Moments

| Move | Event |
|------|-------|
| 8 | Nxe6! — Deep Blue sacrifices a knight. Audience gasps. |
| 9 | Bg6+ — King exposed. Kasparov in serious trouble. |
| 19 | Nd4! — Kasparov stares at the board. Resigns. |

## The Coda

> "John Henry beat the steam hammer. And then he died.
> Kasparov lost to Deep Blue. And he will live.
> Perhaps that's the difference. Perhaps that's progress.
> Or perhaps... the story isn't over. It never is."
> 
> — James Burke

## Links

- [Turing Chess Experiment](../../EXPERIMENT.md)
- [John Henry Broadcast Layer](../../EXPERIMENT.md#layer-6-the-broadcast--live-tv-coverage)
- [Revolutionary Chess Plugin](../../plugins/revolutionary-chess/PLUGIN.yml)
