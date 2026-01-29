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
      - "GPU temperature climbing — 78°C... 82°C... 87°C..."
      - "Fans spin up from whisper to roar"
      - "Power draw spikes — lights in the venue flicker"
      
  thermal-drama:
    description: "Heat as visible struggle"
    examples:
      - "Chassis vents glow faintly orange"
      - "Wisps of vapor rise from cooling system"
      - "Smoke curls from overtaxed power supply — audience gasps"
      - "Emergency cooling kicks in with a WHOOSH"
      - "Heat shimmer visible above the cabinet"
      - "Technician nervously checks thermal readouts"
      
  grafana-dashboard:
    description: "Live metrics display — the robot's soul laid bare"
    panels:
      evaluation-graph:
        - "Line chart: position evaluation over time"
        - "Spikes when advantage shifts"
        - "Audience watches the line like a stock ticker"
        - "Flatline during obvious moves. Chaos during complications."
        
      confidence-gauge:
        - "Circular gauge: 0-100% confidence in current position"
        - "Needle swings wildly during tactical sequences"
        - "Drops to 34% — audience gasps"
        - "Slowly climbs back — relief in robot section"
        
      positions-counter:
        - "Rolling counter: positions evaluated this move"
        - "12,847,291... 12,847,292... 12,847,293..."
        - "Suddenly accelerates — found something interesting"
        - "Counter freezes. Move selected. Silence."
        
      thermal-panel:
        - "Heat map of GPU clusters"
        - "Red zones spreading like infection"
        - "Alert banner: 'THERMAL THROTTLING IMMINENT'"
        - "Color shift to yellow — crisis averted"
        
      branching-tree:
        - "Live visualization of search tree"
        - "Branches bloom and prune in real-time"
        - "One branch suddenly goes deep — what did it see?"
        - "All other branches collapse. Decision made."
        
      memory-usage:
        - "Bar chart: RAM consumption"
        - "Transposition table filling up"
        - "Garbage collection pause — 0.3 seconds of silence"
        - "Memory freed. Evaluation resumes."
        
    dramatic-moments:
      - "Dashboard goes red during time pressure"
      - "All panels flatline for 0.5 seconds — kernel panic?"
      - "Confidence hits 99.7% — checkmate found"
      - "Evaluation graph inverts suddenly — blunder detected too late"
      - "Dashboard displays: 'POSITION NOT IN OPENING BOOK' — we're off-script"
      - "Technician's face reflected in monitor, sweating"
      
  mechanical-tells:
    description: "Physical movements that reveal state"
    examples:
      - "Arm moves smoothly — confident evaluation"
      - "Slight hesitation at piece pickup — close call"
      - "Camera lens adjusts focus on human's face"
      - "Servo trembles slightly — unprecedented position?"
      - "Arm retracts, pauses, extends again — recalculation"
      - "Piece placement more forceful than usual"
      
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
      - "Old grandmaster shakes head slowly — he's seen this before"
      - "Tech CEO smirks, checking stock price on phone"
      - "Philosophy professor mutters about consciousness"
      
  robot-audience:
    description: "Other machines in attendance, cheering their own"
    examples:
      - "Service robot in back row emits supportive beep sequence"
      - "Roomba near the exit spins in celebration after good move"
      - "Industrial arm from factory delegation raises welding torch salute"
      - "Smartphone in journalist's pocket vibrates congratulations"
      - "ATM in lobby displays 'PROCESSING... HOPE'"
      - "Self-driving car outside honks twice — solidarity"
      - "Smart thermostat lowers venue temperature 0.5° — cooling support"
      
  faction-dynamics:
    description: "Human vs machine allegiances fracture the crowd"
    examples:
      - "Human section erupts in applause — robot section's LEDs dim in disappointment"
      - "Someone shouts 'That's OUR move!' — unclear which side they mean"
      - "Robot sympathizer in human section quietly pumps fist"
      - "Elderly man turns to service robot: 'Your kind will never understand sacrifice'"
      - "Robot's camera pans to elderly man. Stores face. Says nothing."
      
  audience-squabbling:
    description: "Tensions between factions"
    examples:
      - "'Turn off your phone!' 'It's WATCHING, not recording!'"
      - "Human fans shush robot beeping — robots beep louder"
      - "Debate breaks out: 'It's not REALLY thinking' vs 'Neither are you'"
      - "Security removes human for throwing popcorn at service robot"
      - "Two grandmasters argue — one coached the human, one wrote Deep Blue's opening book"
      - "Child befriends Roomba. Parents disapprove. Roomba doesn't care."
      - "Robot section performs synchronized LED wave. Humans try to start 'the wave'. Fails."
      
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

### Layer 6: The Broadcast — Live TV Coverage
```yaml
broadcast-layer:
  format: "Prime-time television event"
  network: "Global simulcast"
  
  mythic-inheritance:
    description: "This game carries the weight of every human vs machine battle"
    
    john-henry:
      song: "John Henry was a steel-driving man..."
      story: |
        The legendary railroad worker who raced a steam-powered hammer.
        He won. Then his heart burst from the effort.
        The machine kept working the next day.
        
      echo-in-chess:
        - "Can human intuition beat brute-force calculation?"
        - "What does victory cost?"
        - "If we win, do we still lose?"
        - "The hammer didn't celebrate. Neither will Deep Blue."
        
    lineage:
      - "John Henry vs. the Steam Hammer (1870s)"
      - "Garry Kasparov vs. Deep Blue (1996-1997)"
      - "Lee Sedol vs. AlphaGo (2016)"
      - "This match (now)"
      - "The final battle? Or just another chapter?"
      
    narrator-invocation: |
      "One hundred and fifty years ago, a man named John Henry
      picked up a hammer and faced a machine. He won that race.
      It killed him. Tonight, another human faces another machine.
      The stakes are different. The question is the same:
      What are we willing to sacrifice to prove we matter?"

  dual-commentary:
  
    howard-cosell:
      role: "Sports drama and human stakes"
      style: "Telling it like it is"
      examples:
        - "Ladies and gentlemen, you are looking at the most significant confrontation since Ali faced Frazier in Manila!"
        - "The human is HURT! He's on the ropes! Can he survive this onslaught?"
        - "That move — that MOVE! — is either the work of genius or desperation!"
        - "I have covered boxing, football, baseball. NOTHING compares to this."
        - "The machine feels nothing. The human feels everything. That is the asymmetry."
        - "He's sweating. The machine is not. Draw your own conclusions."
        - "In all my years of broadcasting, I have never seen anything like this."
        
    james-burke:
      role: "Historical connections and scientific context"
      style: "Making unexpected connections across history"
      examples:
        - "And this brings us, curiously, to a textile factory in Lyon, 1801..."
        - "Kasparov's position here mirrors a problem faced by Bletchley Park codebreakers."
        - "The algorithm evaluating this move descends directly from Claude Shannon's 1950 paper."
        - "What the machine is doing now would have seemed like witchcraft to Babbage. Though he predicted it."
        - "This sacrifice connects to a theorem proven by John von Neumann while designing the hydrogen bomb."
        - "The human brain uses 20 watts. That machine uses 20 kilowatts. Efficiency has meanings."
        - "We are watching, in real-time, the question Alan Turing asked in 1950 being answered. Or perhaps, being made obsolete."
        
    banter:
      - "COSELL: 'James, in plain English, what just happened?'"
      - "BURKE: 'The machine found a connection that took humans 400 years to discover. In 0.3 seconds.'"
      - "COSELL: 'Is that good or bad?'"
      - "BURKE: 'Yes.'"
      - "COSELL: 'The human is thinking. The machine is... what? Waiting?'"
      - "BURKE: 'Processing. Though the distinction may be philosophical rather than practical.'"
      - "COSELL: 'I don't like it, James. I don't like it one bit.'"
      - "BURKE: 'Neither did John Henry, Howard. Neither did John Henry.'"

  broadcast-moments:
  
    opening:
      - "Orchestra plays dramatic fanfare"
      - "Montage: Kasparov's face, Deep Blue's cabinet, chess history"
      - "John Henry song plays softly under narration"
      - "COSELL: 'From New York City, the chess capital of the world...'"
      - "BURKE: 'From a lineage stretching back to sixth-century India...'"
      
    commercial-breaks:
      - "We go to break as the human contemplates the impossible position..."
      - "IBM logo. 'Solutions for a small planet.'"
      - "Cutaway: Watching parties in Moscow, Tokyo, San Francisco"
      - "Interview package: 'What this match means for humanity'"
      
    mid-game:
      - "Split screen: human face, Grafana dashboard"
      - "COSELL: 'Look at those numbers climbing, James!'"
      - "BURKE: 'Each one represents a future that will never exist.'"
      - "Crowd noise swells. Someone chanting. In Russian."
      
    climax:
      - "COSELL: 'This is it! This is the moment!'"
      - "BURKE: 'The singularity in miniature.'"
      - "John Henry theme returns, building"
      - "Human's hand trembles over the piece"
      - "Machine's arm extends smoothly"
      - "COSELL: 'The world holds its breath...'"
      
    aftermath:
      - "Silence. Then chaos."
      - "COSELL: 'I... I don't have words.'"
      - "BURKE: 'History rarely announces itself. Tonight it did.'"
      - "Cut to: faces in the crowd, tears or triumph"
      - "Robot section's lights pulse in unison"
      - "John Henry song, final verse: '...and he laid down his hammer and he died.'"
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
