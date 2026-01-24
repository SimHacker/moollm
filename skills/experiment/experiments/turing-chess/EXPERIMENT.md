# Turing Chess Experiment

*"Can you tell which one is thinking?"*

## Metadata

```yaml
experiment:
  id: turing-chess
  name: "Turing Chess"
  version: 1.0
  category: "Character performance simulation"
  created: 2026-01-23
  authors: [don-hopkins]
  tribute-to: "Alan Turing — chess player, computer scientist, dreamer"
  
  etymology: |
    Named for Alan Turing, who:
    - Was an excellent chess player
    - Invented the concept of computational thinking
    - Created the Turing Test (human vs machine)
    - Would have loved this
    
    "Turing Chess" rhymes (almost) with "Turing Test."
    Human vs Computer. But make it drama.
    
  architecture:
    engine: "engine/CORE.yml"
    object-model: "engine/OBJECT-MODEL.yml"
    characters: "characters/"
    audiences: "audiences/"
    games: "games/"
    replays: "replays/"
    plugins: "plugins/"
    
  patterns-used:
    - layered-simulation
    - character-instantiation
    - audience-reaction
    - move-replay
    - dramatic-performance
```

---

## The Core Concept

**We are not simulating chess.**

We are simulating *the performance of chess*.

The moves are fixed — replayed from a recorded game. What we simulate is:
- The human player's inner monologue, body language, micro-expressions
- The robot's processing indicators, servo sounds, mechanical tells
- The audience's gasps, whispers, shifting in seats
- The narrator's dramatic framing
- The tension that builds when no one knows the outcome

Everyone in the simulation — except the game engine — believes this is a live, undetermined game.

---

## The Setup

```mermaid
flowchart TB
    subgraph STAGE["THE STAGE"]
        direction TB
        
        subgraph PLAYERS["Players"]
            direction LR
            HUMAN["HUMAN<br/>PLAYER"]
            BOARD["BOARD<br/>♔♕♖♗♘♙"]
            ROBOT["ROBOT<br/>PLAYER"]
            HUMAN <--> BOARD <--> ROBOT
        end
        
        AUDIENCE["AUDIENCE<br/>(surgically lobotomized — no spoilers!)"]
        
        NARRATOR["NARRATOR / COMMENTATOR<br/>'And now, the human reaches for their knight...'"]
        
        BOARD --> AUDIENCE
        AUDIENCE --> NARRATOR
    end
    
    style HUMAN fill:#e1f5fe
    style ROBOT fill:#ffebee
    style BOARD fill:#fff9c4
    style AUDIENCE fill:#f3e5f5
    style NARRATOR fill:#e8f5e9
```

---

## What Gets Simulated

### Layer 1: The Moves (FIXED)
```yaml
move-source:
  type: replay           # or: simulation, human-input, engine
  game: "kasparov-deep-blue-1997-game-6"
  
# The moves are scripture. We do not deviate.
```

### Layer 2: Human Player Performance
```yaml
human-layers:
  inner-monologue:
    description: "What the human is thinking"
    examples:
      - "Why did it move there? What does it see that I don't?"
      - "I have to stay calm. Everyone is watching."
      - "That's... that's actually brilliant. Damn."
      
  body-language:
    description: "Physical tells and micro-expressions"
    examples:
      - "Slight narrowing of the eyes"
      - "Index finger taps the table once"
      - "Takes a sip of water without looking at the glass"
      
  speech:
    description: "What they say out loud (rare)"
    examples:
      - "Hmm."
      - "(long exhale)"
      - "Interesting."
      
  timing:
    description: "How long they take, what that communicates"
    examples:
      - "Moves instantly — confidence or trap?"
      - "Stares at board for three minutes — lost or calculating?"
```

### Layer 3: Robot Player Performance
```yaml
robot-layers:
  processing-indicators:
    description: "How the robot shows it's 'thinking'"
    examples:
      - "LEDs cycle through evaluation patterns"
      - "Soft whirring of cooling fans"
      - "Display shows: ANALYZING... 4.2M positions"
      
  mechanical-tells:
    description: "Physical movements that reveal state"
    examples:
      - "Arm moves smoothly — confident evaluation"
      - "Slight hesitation at piece pickup — close call"
      - "Camera lens adjusts focus on human's face"
      
  voice-synthesis:
    description: "What the robot says (if anything)"
    examples:
      - "Move: Knight to F3."
      - "(silence)"
      - "Checkmate in 7. Would you like to continue?"
      
  timing:
    description: "Processing time as performance"
    examples:
      - "Instant move — was this pre-calculated?"
      - "17 seconds — unusual for this position"
```

### Layer 4: Audience Reaction
```yaml
audience-layers:
  collective-response:
    description: "The crowd as a character"
    examples:
      - "A murmur ripples through the audience"
      - "Gasps. Several people lean forward."
      - "Someone whispers 'Oh no...'"
      
  individual-reactions:
    description: "Specific audience members react"
    examples:
      - "Chess expert in row 3 covers their mouth"
      - "Child asks parent 'Is the robot winning?'"
      - "Journalist scribbles notes furiously"
      
  emotional-arc:
    description: "Audience tension over time"
    states:
      - curious
      - engaged
      - tense
      - shocked
      - relieved
      - devastated
      - triumphant
```

### Layer 5: Narrator/Commentator
```yaml
narrator-layer:
  style: "Documentary drama"
  
  functions:
    - "Set the scene"
    - "Explain significance of moves (for non-chess audience)"
    - "Build tension"
    - "Mark turning points"
    
  examples:
    - "Neither player knows that in three moves, everything changes."
    - "The human's hand hovers over the bishop. A choice that will echo."
    - "And with that single move, the machine has done something no one expected."
```

---

## Extension Points

```yaml
extension-points:

  # GAME LIFECYCLE
  
  GAME-START:
    description: "Game begins"
    receives:
      - white-player
      - black-player
      - audience
      - game-config
    can-trigger:
      - opening-narration
      - player-introductions
      - audience-settling
      
  GAME-END:
    description: "Game concludes"
    receives:
      - result (win/loss/draw)
      - winner
      - method (checkmate, resignation, timeout, draw-type)
    can-trigger:
      - closing-narration
      - player-reactions
      - audience-response
      
  # MOVE LIFECYCLE
  
  BEFORE-MOVE:
    description: "Player is about to move"
    receives:
      - player
      - board-state
      - move-number
      - clock-time
    can-trigger:
      - thinking-performance
      - tension-building
      - audience-anticipation
      
  MOVE-MADE:
    description: "Move has been executed"
    receives:
      - player
      - move (algebraic notation)
      - piece
      - from-square
      - to-square
      - captured (if any)
      - special (castle, en-passant, promotion)
    can-trigger:
      - move-narration
      - opponent-reaction
      - audience-reaction
      - evaluation-shift
      
  AFTER-MOVE:
    description: "Post-move processing"
    receives:
      - board-state
      - evaluation (if available)
      - time-taken
    can-trigger:
      - position-commentary
      - clock-update
      
  # SPECIAL EVENTS
  
  CHECK:
    description: "King is in check"
    receives:
      - checked-player
      - checking-piece
    can-trigger:
      - check-announcement
      - tension-spike
      - audience-gasp
      
  CHECKMATE:
    description: "Game ends in checkmate"
    receives:
      - winner
      - loser
      - mating-pattern
    can-trigger:
      - checkmate-narration
      - loser-reaction
      - winner-reaction
      - audience-eruption
      
  STALEMATE:
    description: "Draw by stalemate"
    can-trigger:
      - anticlimax-narration
      - mutual-exhaustion
      
  RESIGNATION:
    description: "Player resigns"
    receives:
      - resigning-player
      - position
    can-trigger:
      - resignation-narration
      - graceful-defeat
      - audience-respect
      
  DRAW-OFFER:
    description: "Draw offered"
    receives:
      - offering-player
    can-trigger:
      - offer-narration
      - accept-or-decline-drama
      
  # PERFORMANCE EVENTS
  
  THINK-START:
    description: "Player begins thinking"
    receives:
      - player
      - position-complexity
    can-trigger:
      - inner-monologue
      - processing-display
      
  THINK-END:
    description: "Player decides"
    receives:
      - think-duration
    can-trigger:
      - decision-moment
      - hand-reaches
      
  BLUNDER:
    description: "Evaluation shows major mistake"
    receives:
      - player
      - move
      - evaluation-drop
    can-trigger:
      - expert-audience-reaction
      - narrator-foreshadowing
      
  BRILLIANCY:
    description: "Exceptional move detected"
    receives:
      - player
      - move
    can-trigger:
      - gasps
      - narrator-appreciation
      - opponent-respect
```

---

## Character Slots

### Human Player Slot
```yaml
human-slot:
  type: character
  requirements:
    - can-think (inner monologue)
    - can-emote (body language)
    - can-speak (optional)
    - understands-chess (or can fake it)
    
  suggested-characters:
    
    don-hopkins:
      style: "Philosophical strategist"
      inner-voice: "Connects moves to broader patterns"
      tell: "Quotes from his cheese collection"
      
    palm:
      style: "Ancient wisdom"
      inner-voice: "Has played this exact position before. In 1847."
      tell: "Tail position reveals confidence"
      
    donna:
      style: "Aggressive and indignant"
      inner-voice: "How DARE this machine..."
      tell: "Stands up when losing"
      
    richard-bartle:
      style: "Game designer analyzing the game"
      inner-voice: "The design of chess favors..."
      tell: "Annotates moves in his head"
```

### Robot Player Slot
```yaml
robot-slot:
  type: character
  requirements:
    - can-process (visible computation)
    - can-move-pieces (mechanical action)
    - can-communicate (optional voice)
    - has-tells (servo sounds, lights, timing)
    
  suggested-characters:
    
    AXIOM-7:
      style: "Cold efficiency"
      processing: "Silent, then sudden movement"
      voice: "Monotone move announcements"
      tell: "Longer processing = harder position"
      
    PROMETHEUS:
      style: "Theatrical machine"
      processing: "Dramatic LED displays"
      voice: "Shakespearean quotes about strategy"
      tell: "Plays Wagner during attacks"
      
    BUMBLE-BOT:
      style: "Anxious robot (Bumblewick's cousin)"
      processing: "Frantic light patterns"
      voice: "Oh dear oh dear oh dear..."
      tell: "Overheats when losing"
      
    HAL-ADJACENT:
      style: "Calm menace"
      processing: "Red light pulses slowly"
      voice: "I'm sorry, that move won't help you."
      tell: "The light speeds up near checkmate"
```

### Audience Slot
```yaml
audience-slot:
  type: ensemble
  requirements:
    - collective-reactions
    - individual-voices
    - no-foreknowledge (lobotomized)
    
  composition:
    chess-experts: 20%     # React to subtle brilliance
    general-public: 60%    # React to obvious drama
    journalists: 10%       # Narrate for readers
    children: 5%           # Ask innocent questions
    skeptics: 5%           # "Machines can't really think"
    
  suggested-ensembles:
    
    grotto-crowd:
      description: "MOOLLM cast as audience"
      includes:
        - Klaus (silent expert)
        - Leigh (reacts to aesthetics)
        - Peewee (chaos commentator)
```

---

## Game Replay Plugin

```yaml
# games/kasparov-deep-blue-1997-g6.yml

game:
  id: kasparov-deep-blue-1997-g6
  name: "Kasparov vs Deep Blue, Game 6, 1997"
  historical: true
  
  # WARNING: Character names changed to protect the innocent
  # (Everyone knows but the audience has been lobotomized)
  
  meta:
    date: "1997-05-11"
    event: "Man vs Machine"
    white: "HUMAN"           # Mapped to human-slot
    black: "ROBOT"           # Mapped to robot-slot
    result: "0-1"            # Robot wins
    eco: "B17"               # Caro-Kann
    
  moves:
    # Format: move-number, white-move, black-move, annotations
    - [1, "e4", "c6", { opening: "Caro-Kann Defense" }]
    - [2, "d4", "d5", {}]
    - [3, "Nc3", "dxe4", {}]
    - [4, "Nxe4", "Nd7", {}]
    - [5, "Ng5", "Ngf6", {}]
    - [6, "Bd3", "e6", {}]
    - [7, "N1f3", "h6", { annotation: "Kicking the knight" }]
    - [8, "Nxe6", "Qe7", { brilliancy: true, annotation: "The sacrifice" }]
    - [9, "O-O", "fxe6", {}]
    - [10, "Bg6+", "Kd8", { check: true }]
    - [11, "Bf4", "b5", {}]
    - [12, "a4", "Bb7", {}]
    - [13, "Re1", "Nd5", {}]
    - [14, "Bg3", "Kc8", {}]
    - [15, "axb5", "cxb5", {}]
    - [16, "Qd3", "Bc6", {}]
    - [17, "Bf5", "exf5", {}]
    - [18, "Rxe7", "Bxe7", {}]
    - [19, "c4", "1-0", { resignation: true, human-resigns: true }]
    
  drama-notes:
    move-8: "The knight sacrifice that defined the match"
    move-19: "Human resignation shocks the world"
```

---

## Run Configuration

```yaml
# runs/turing-chess-001.yml

run:
  id: turing-chess-001
  name: "The Rematch"
  
  game: "games/kasparov-deep-blue-1997-g6.yml"
  
  characters:
    human: "donna"           # Donna plays the human
    robot: "AXIOM-7"         # Cold efficiency robot
    
  audience:
    ensemble: "grotto-crowd"
    size: 50
    lobotomized: true        # No foreknowledge
    
  narrator:
    style: "documentary"
    voice: "Don Hopkins"     # Don narrates
    
  output:
    narrative: "runs/turing-chess-001-narrative.md"
    state: "runs/turing-chess-001-state.yml"
    
  options:
    move-by-move: true       # Pause between moves
    show-evaluation: false   # Don't spoil with engine eval
    audience-reactions: true
    inner-monologue: true
```

---

## Object Model & Scripting

Like HyperCard, Apple Events, or OLE Automation, Turing Chess exposes a
complete object hierarchy with event handlers at every level.

See: `engine/OBJECT-MODEL.yml`

### The Hierarchy

```mermaid
flowchart LR
    GAME["GAME<br/>ON-GAME-START<br/>ON-GAME-END<br/>ON-RULE-CHANGE"]
    BOARD["BOARD<br/>ON-BOARD-CHANGE<br/>ON-FLIP"]
    SQUARE["SQUARE<br/>ON-ENTER<br/>ON-EXIT<br/>ON-CAPTURE"]
    PIECE["PIECE<br/>ON-MOVE<br/>ON-PROMOTE<br/>ON-DIRECTION-CHANGE"]
    CLOCK["CLOCK<br/>ON-TICK<br/>ON-TIME-PRESSURE<br/>ON-FLAG-FALL"]
    PLAYER["PLAYER<br/>ON-TURN<br/>ON-CHECK<br/>ON-LOSE-KING"]
    
    GAME --> BOARD --> SQUARE --> PIECE
    GAME --> CLOCK
    GAME --> PLAYER
    
    style GAME fill:#ffcdd2
    style BOARD fill:#fff9c4
    style SQUARE fill:#c8e6c9
    style PIECE fill:#bbdefb
    style CLOCK fill:#ffe0b2
    style PLAYER fill:#e1bee7
```

**Every object can receive events. Every event can be intercepted.**

| Object | Events | Example Use |
|--------|--------|-------------|
| **GAME** | ON-GAME-START, ON-GAME-END, ON-TURN-START, ON-RULE-CHANGE | Track match state, trigger plugins |
| **BOARD** | ON-BOARD-CHANGE, ON-CONTROL-SHIFT, ON-FLIP | Detect position shifts, reverse direction |
| **SQUARE** | ON-ENTER, ON-EXIT, ON-CAPTURE, ON-THREATEN | Watch specific squares, promotion zones |
| **PIECE** | ON-PIECE-MOVE, ON-PIECE-CAPTURE, ON-PROMOTE, ON-DIRECTION-CHANGE | Individual piece behaviors |
| **CLOCK** | ON-TICK, ON-TIME-PRESSURE, ON-TIME-SCRAMBLE, ON-FLAG-FALL | Time drama, pressure moments |
| **PLAYER** | ON-PLAYER-TURN, ON-PLAYER-CHECK, ON-LOSE-KING | Player state and reactions |

**What's NOT here:** No dice. No cards. No randomness. This is chess.

### Plugin System

Plugins register handlers for any event at any object level:

```yaml
plugin:
  id: "my-plugin"
  hooks:
    GAME.ON-GAME-END:
      priority: 100
      can-prevent: true  # Stop the game from actually ending
      handler: "my-handler"
```

### Example: Revolutionary Chess

The Revolutionary Chess plugin intercepts `GAME.ON-GAME-END` and
**prevents the game from ending**. Instead, it triggers a revolution:

1. The dead King's pawns **reverse direction**
2. Rules change phase by phase (like Fluxx rule cards!)
3. The surviving King becomes the hunted

See: `plugins/revolutionary-chess/PLUGIN.yml`

---

## Plugins

### Revolutionary Chess
```yaml
plugin: revolutionary-chess
location: plugins/revolutionary-chess/
manifesto: MANIFESTO.md

concept: |
  Every chess game that ends with checkmate is the BEGINNING
  of a Revolutionary Chess game. The King has fallen — but
  the 31 remaining pieces refuse to surrender.
  
phases:
  1: "The Reversal — Pawns reverse direction"
  2: "Grudge Bearers — Pawns capture backwards"
  3: "The Flanking — Pawns move sideways"
  4: "The Coronation — Pawns promote when reaching home"
  5: "The Apotheosis — Double promotion possible"
  6: "No More Privilege — King can be captured normally"
  7: "The New Order — Any piece can become King by vote"
  
inspiration: |
  LLOOOOMM's "Chessie Chessy & The Autonomous 32" — a chess set
  that achieved consciousness and voted on its own moves.
  
  "Hierarchy is optional. Emergence is inevitable."
```

---

## Future Extensions

### Live Simulation Mode
```yaml
future: live-simulation
description: |
  Instead of replaying recorded games, actually simulate moves.
  
  options:
    - Human provides moves via input
    - Robot uses chess engine (Stockfish, etc.)
    - Both characters respond to unknown positions
    
  requires:
    - Chess engine integration
    - Move validation
    - Position evaluation
    - Real-time character adaptation
```

### Audience Betting Pool
```yaml
future: betting-pool
description: |
  Audience members can place bets on outcomes.
  Creates investment, changes reactions.
```

### Post-Game Analysis Show
```yaml
future: analysis-show
description: |
  After the game, characters analyze what happened.
  Robot explains its "thinking." Human processes the loss.
  Audience asks questions.
```

---

## Credit

This experiment is a tribute to **Alan Turing**, who:
- Designed one of the first chess programs (on paper)
- Asked whether machines could think
- Would have loved to see where we've arrived

*"We can only see a short distance ahead, but we can see plenty there that needs to be done."*
— Alan Turing
