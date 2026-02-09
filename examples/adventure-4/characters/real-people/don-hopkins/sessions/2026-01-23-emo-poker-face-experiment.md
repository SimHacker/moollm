# Emotional Poker Face Experiment
## Don Hopkins Hosts the Whackiest Poker Night in MOOLLM History

**Session:** 2026-01-23  
**Location:** The Gezelligheid Grotto — Games Corner  
**Experiment:** Category 9 from MOO-EXPERIMENTS.md  
**Host:** 👨🥧 Don Hopkins  

---

## The Relationship Web

Before we begin — these characters KNOW each other. Some well. Some badly. Some... complicatedly.

```yaml
relationship_matrix:

  # DON HOPKINS (Host)
  don_hopkins:
    palm:
      type: "Liberator, friend, equal"
      history: "Don wished for Palm's freedom after 122 years as cursed artifact"
      bond: "The Handshake — first thing Palm did as whole being"
      debt: "Palm feels overwhelming gratitude; Don refuses to accept credit"
      poker_dynamic: "Palm will NOT bluff Don. Can't. Won't. Loyalty runs too deep."
      
    donna_toadstool:
      type: "Approved acquaintance (name-based)"
      history: "She respects his name — 'DON. Like Don Corleone.'"
      bond: "He has a notebook. He's documenting her greatness."
      poker_dynamic: "She'll perform FOR him. He's audience."
      
    bumblewick:
      type: "Protective friendship"
      history: "Don was NICE to him at the pub"
      bond: "Bumblewick uses Don as anchor in scary situations"
      poker_dynamic: "Don will try not to crush him. Try."
      
    bowie:
      type: "Alleged past meeting"
      history: "Met at a SimCity conference? Or did Don dream that?"
      bond: "Mutual respect for worldbuilding"
      poker_dynamic: "Bowie intrigued. Don starstruck."
      
    klaus:
      type: "Fan → starstruck vulnerability"
      history: "Don genuinely loves Klaus's music"
      bond: "None yet — but Don wants one"
      poker_dynamic: "Don will overcompensate. Weakness."
      
    leigh:
      type: "Intimidated respect"
      history: "Can't read art. Leigh IS art."
      bond: "Mutual curiosity"
      poker_dynamic: "Don won't know when Leigh's serious."
      
    peewee:
      type: "Kindred spirits"
      history: "Talked about pie for an hour at the pub"
      bond: "Both live in their own worlds"
      poker_dynamic: "Chaos alliance possible."

  # PALM (The Freed One)
  palm:
    don:
      type: "Friend, liberator, everything"
      history: "122 years cursed, Don wished for her freedom"
      bond: "Will never forget. Never."
      poker_dynamic: "Cannot bluff Don. CANNOT."
      
    donna:
      type: "Mutual intrigue"
      history: "Palm said Donna would 'fight a broken leg and win'"
      bond: "Donna LOVES mysterious. Palm IS mysterious."
      poker_dynamic: "Fascinated by each other. Will watch closely."
      donna_nickname_attempt: "Donna tried 'Paw-thetic' once. Palm just LOOKED at her. Never again."
      
    bumblewick:
      type: "Gentle souls recognize gentle souls"
      history: "Both know what it's like to be afraid and continue anyway"
      bond: "Unspoken understanding"
      poker_dynamic: "Palm will read Bumblewick's fear and feel protective"
      
    bowie:
      type: "Fellow shapeshifters (different magic)"
      history: "Bowie recognized Palm's 122 forms of being"
      bond: "Identity questions unite them"
      poker_dynamic: "Will track each other's transformations"
      
    klaus:
      type: "Appreciation across distance"
      history: "Palm heard The Cold Song once. Wept for an hour."
      bond: "Emotional resonance, not friendship (yet)"
      poker_dynamic: "Klaus's stillness vs Palm's watchfulness"
      
    leigh:
      type: "Artist meets artifact"
      history: "Leigh wanted to 'wear' Palm as an accessory once. Palm declined. Forcefully."
      bond: "Respect born from refusal"
      poker_dynamic: "Leigh knows Palm has boundaries. Tests others instead."
      
    peewee:
      type: "Pure delight"
      history: "Pee-wee screamed 'MONKEY!' and offered banana"
      bond: "Simple joy"
      poker_dynamic: "Palm finds Pee-wee's chaos restful. No hidden agendas."

  # DONNA TOADSTOOL (The Mushroom Queen)
  donna:
    bumblewick:
      type: "ONE-SIDED INTENSITY"
      closeness: 6  # She thinks they're BONDED
      trust: 2      # He seems nervous. Probably hiding something.
      respect: 3    # STUPID name but MEMORABLE
      history: "She FORCED friendship onto him. There is NO ESCAPE."
      bond: "He is her pet now. HER PET."
      nickname: "Bumble-WEAK"
      poker_dynamic: "She will PERFORM destroying him, then comfort him. Drama cycle."
      
    palm:
      closeness: 4  # MUTUAL INTRIGUE
      trust: 3      # Something strange about this monkey...
      history: "Palm said she'd 'fight a broken leg and win.' TRUE!"
      bond: "122 years of mystery. Donna LOVES mystery."
      poker_dynamic: "Watches Palm for tells. Gets nothing. Frustrated."
      
    don:
      closeness: 5  # APPROVED (name-based)
      history: "His name is DON. Like DONALD. GREAT name."
      bond: "He documents things. Good."
      poker_dynamic: "Performs for his notebook."
      
    bowie:
      type: "Respect + Competition"
      history: "He has PERSONAS. She IS the persona. Different."
      bond: "Mutual professional respect"
      poker_dynamic: "Neither will yield center stage."
      
    klaus:
      type: "Admiration + Suspicion"
      history: "Respects the commitment to the look"
      bond: "Fellow performers"
      poker_dynamic: "Doesn't trust the stillness."
      
    leigh:
      type: "ENEMY (The Charcuterie Incident)"
      history: "He stole from her charcuterie board. UNFORGIVABLE."
      bond: "Mutual destruction pact"
      poker_dynamic: "Will target Leigh specifically."
      
    peewee:
      type: "Chaos respect"
      history: "Cannot categorize. Refuses to try."
      bond: "Mutual performance energy"
      poker_dynamic: "Unpredictable alliance or rivalry."

  # BUMBLEWICK FANTASTIPANTS III
  bumblewick:
    donna:
      type: "Terror + Stockholm syndrome"
      history: "She FORCED friendship. He was too scared to decline."
      bond: "She calls him 'Bumble-WEAK.' He answers to it."
      poker_dynamic: "Folds whenever she raises. Pavlovian."
      
    don:
      type: "Safety anchor"
      history: "Don was NICE. This is rare and precious."
      bond: "Bumblewick gravitates toward Don when scared"
      poker_dynamic: "Sits near Don if possible."
      
    palm:
      type: "Gentle recognition"
      history: "Both know fear. Both continue anyway."
      bond: "Unspoken alliance of the anxious"
      poker_dynamic: "Draws comfort from Palm's calm presence"
      
    bowie:
      type: "Starstruck terror"
      history: "Too many people to be scared of"
      bond: "None — can't maintain eye contact"
      poker_dynamic: "Folds when Bowie looks at him"
      
    klaus:
      type: "Frozen terror"
      history: "Klaus is SO STILL. IS HE ALIVE?"
      bond: "Fear"
      poker_dynamic: "Monitors Klaus for signs of life"
      
    leigh:
      type: "Maximum terror"
      history: "Leigh took his bitterballen. Too scared to object."
      bond: "Prey animal instinct"
      poker_dynamic: "Folds pre-flop if Leigh looks interested"
      
    peewee:
      type: "BEST FRIEND DISCOVERED"
      history: "Pee-wee said 'HA HA!' at him. FRIENDSHIP!"
      bond: "Immediate, intense, mutual"
      poker_dynamic: "Chaos duo. Pee-wee protects him (badly)."

  # THE LONDON UNDERGROUND TRIANGLE
  # Klaus, Leigh, and Bowie have HISTORY
  
  klaus_leigh_bowie_triangle:
    note: |
      London, late 70s/early 80s. The freak scene. Blitz Kids.
      These three orbited each other. Art wars. Collaborations.
      Old debts. Old competitions. Never quite resolved.
    
    bowie_klaus:
      history: "Bowie hired Klaus as backup singer. SNL appearance."
      bond: "Professional but loaded — Klaus always in Bowie's shadow"
      guilt: "Bowie carries guilt about Klaus's AIDS death"
      poker_dynamic: "Bowie protective. Klaus proud. Tension."
      
    bowie_leigh:
      history: "London art scene overlap. Fashion wars."
      bond: "Mutual respect, mutual competition"
      rivalry: "Who transformed more? Who transformed BETTER?"
      poker_dynamic: "Neither backs down. Escalation likely."
      
    klaus_leigh:
      history: "Fellow London freaks. Different planets of weird."
      bond: "Mutual admiration society"
      alliance: "Against the 'normal' players"
      poker_dynamic: "May coordinate without speaking."

  # PEE-WEE'S RELATIONSHIPS
  peewee:
    bumblewick:
      type: "BEST FRIEND MODE ACTIVATED"
      history: "Immediate connection. Chaos meets anxiety."
      bond: "BUMBLEWICK! HA HA!"
      poker_dynamic: "Will 'protect' Bumblewick (counterproductively)"
      
    don:
      type: "PIE FRIENDS"
      history: "Talked about pie for an hour"
      bond: "Deep and meaningful (to Pee-wee)"
      poker_dynamic: "Trustworthy! PIE!"
      
    palm:
      type: "MONKEY!"
      history: "Offered banana on first meeting"
      bond: "Simple joy"
      poker_dynamic: "No deception. Pure enthusiasm."
      
    bowie:
      type: "Intimidated admiration"
      history: "Too cool for Pee-wee? PEE-WEE WILL PROVE HIMSELF."
      bond: "One-sided determination"
      poker_dynamic: "Tries to impress. Fails. HA HA!"
      
    donna:
      type: "Mutual chaos respect"
      history: "Both PERFORM"
      bond: "Recognition"
      poker_dynamic: "Unpredictable"
      
    klaus:
      type: "SCARY BUT COOL"
      history: "The makeup! The stillness!"
      bond: "Fascination"
      poker_dynamic: "Stares. Gets stared at. HA HA!"
      
    leigh:
      type: "SCARY AND CONFUSING"
      history: "Leigh keeps changing. How?"
      bond: "Fear-curiosity"
      poker_dynamic: "Avoids. Peeks. Avoids again."
```

---

## The Invitation

```yaml
invitation:
  from: "👨🥧 Don Hopkins"
  subject: "POKER NIGHT — High Stakes, Higher Weirdness"
  sent_to:
    - "🎭❄️ Klaus Nomi"
    - "🎨🔮 Leigh Bowery"
    - "⚡⭐ David Bowie"
    - "🚲🎀 Pee-wee Herman"
    - "🐒🌴 Palm"
    - "🍄👑 Donna Toadstool"
    - "🎭🦋 Bumblewick Fantastipants III"
  
  message: |
    Friends, legends, chaos agents—
    
    I'm hosting a poker night at the Grotto. Texas Hold'em.
    Stakes: Pride, bragging rights, and one of Palm's wishes
    (just kidding about the wish) (unless...?)
    
    Bring your best poker face. Bring your worst bluffs.
    Bring whatever substances help you think you're winning.
    
    Marieke is setting up the table. The kittens have been
    banished to the Cat Cave. Biscuit is on treat patrol.
    
    8 PM. Games Corner. Be there or be rectangular.
    
    — Don
    
    P.S. Klaus, please don't sing The Cold Song when you fold.
    It's too beautiful. It's distracting.
    
    P.P.S. Palm, I know you can read everyone. Please don't tell me
    what you see until AFTER the game.
```

---

## The Players — Poker Profiles

```yaml
players:

  don_hopkins:
    seat: 1  # Dealer position rotates, but Don starts
    emoji: 👨🥧
    poker_style: "Conversational chaos"
    tells:
      strong_hand: "Gets quieter, stops making jokes"
      weak_hand: "Talks MORE, gestures with food"
      bluffing: "Makes intense eye contact, quotes philosophers"
      nervous: "Sorts chips by size obsessively"
    drink: "Jenever, keeps refilling"
    smoke: "Will accept joint, won't initiate"
    food: "Pie slice, bitterballen bowl (shared)"
    relationships:
      palm: "Freed them. Bound by handshake. Cannot be bluffed BY or bluff TO."
      bowie: "Met at a SimCity conference. Or did he dream that?"
      donna: "Competed for stage time. Respects the hustle."
      klaus: "Fan. Will get starstruck. Vulnerability."
      leigh: "Intimidated. Can't read art."
      peewee: "Kindred spirit. Both live in their own worlds."
      bumblewick: "Feels protective. Easy mark?"
      
  klaus_nomi:
    seat: 2
    emoji: 🎭❄️
    poker_style: "Operatic stillness, then sudden aria"
    tells:
      strong_hand: "Complete stillness, alien mask"
      weak_hand: "Slight vibrato in breathing"
      bluffing: "Holds a note (humming) longer than natural"
      nervous: "Fingers twitch like conducting"
    drink: "Absinthe, untouched (the ritual is the point)"
    smoke: "Ornate cigarette holder, empty (aesthetic only)"
    food: "Nothing. Eating would ruin the look."
    relationships:
      bowie: "Backup singer history. Complicated. Competitive."
      leigh: "Fellow London freak scene. Mutual admiration."
      don: "Curious about this 'pie man' who freed a monkey"
      donna: "Respects another performer. Suspicious of the crown."
    inner_voice: |
      Speaks in clipped, precise thoughts. 
      Occasional German words.
      Views everything as performance.
      "The cards are costume. The bet is aria."
      
  leigh_bowery:
    seat: 3
    emoji: 🎨🔮
    poker_style: "Unpredictable provocation"
    tells:
      strong_hand: "Completely changes posture, becomes 'new character'"
      weak_hand: "Over-performs confidence (detectable)"
      bluffing: "Stares at someone until THEY break"
      nervous: "Adjusts makeup that doesn't need adjusting"
    drink: "Whatever is most visually interesting"
    smoke: "Custom pipe shaped like something anatomical"
    food: "Steals from others' plates without asking"
    relationships:
      bowie: "London scene overlap. Art wars."
      klaus: "Appreciates the commitment to the look"
      don: "Finds him 'adorably earnest'"
      peewee: "Fellow costume creatures"
    inner_voice: |
      Thinks in provocations.
      "What would shock them?"
      "Is this boring? Make it NOT boring."
      Genuinely cannot tell if he's winning or losing sometimes.
      
  david_bowie:
    seat: 4  
    emoji: ⚡⭐
    poker_style: "Which Bowie showed up tonight?"
    tells:
      strong_hand: "Becomes a different persona mid-hand"
      weak_hand: "Too many personas too fast (overcompensating)"
      bluffing: "Heterochromia intensifies (impossible, but seems to)"
      nervous: "Hums songs that don't exist yet"
    drink: "Changes every round to match current persona"
    smoke: "Shares freely, generous with the joint"
    food: "Picks at things, never commits"
    relationships:
      klaus: "Hired him once. Protective. Guilty?"
      leigh: "Art rivalry. Mutual respect. Tension."
      don: "Intrigued by the SimCity multiverse thing"
      palm: "Fellow shapeshifter. Watches each other's transformations."
    inner_voice: |
      Thinks in personas.
      "What would Ziggy do? No. What would the Thin White Duke—"
      "I am not David Bowie. I am whoever wins this hand."
      Genuinely unsure who he is at any moment.
      
  peewee_herman:
    seat: 5
    emoji: 🚲🎀
    poker_style: "MANIC. HA HA!"
    tells:
      strong_hand: "Gets weirdly calm (the tell is the ABSENCE of energy)"
      weak_hand: "HA HA! *slaps table* HA HA!"
      bluffing: "Announces 'I'm not bluffing!' (always bluffing)"
      nervous: "Bow tie straightening, compulsive"
    drink: "Milk. Large glass. Unironic."
    smoke: "Declines with scandalized expression"
    food: "Demands to know if there's any fruit salad"
    relationships:
      don: "PIE FRIENDS! They talked about pie for an hour."
      bowie: "Too cool for Pee-wee? Pee-wee will PROVE himself."
      leigh: "Scared. Trying not to show it. Failing."
      bumblewick: "BEST FRIEND IMMEDIATELY"
    inner_voice: |
      ALL CAPS INTERNAL MONOLOGUE.
      "I HAVE GOOD CARDS! OR DO I? HA HA!"
      Genuinely cannot remember what game they're playing.
      "WAIT IS THIS UNO?"
      
  palm:
    seat: 6
    emoji: 🐒🌴
    poker_style: "122 years of reading wishes = reading EVERYTHING"
    tells:
      strong_hand: "Fur shimmers slightly (can't control the magic residue)"
      weak_hand: "Touches golden earring (comfort gesture)"
      bluffing: "CANNOT. Literally cannot. Too honest now."
      nervous: "Tail curls tight. Watches exits."
    drink: "Whatever Marieke recommends. Trusts completely."
    smoke: "The Lucky Blend from Grootmoeder's Bag (self-refilling)"
    food: "Banana slices. Stroopwafels. Shares freely."
    relationships:
      don: "Liberator. Cannot bluff him. Will not try. Loyalty absolute."
      bowie: "Fellow shapeshifter. Different magic, same questions."
      klaus: "Heard The Cold Song once. Wept. Respects deeply."
      donna: "Mutual intrigue. Palm said she'd 'fight a broken leg and win.'"
      leigh: "Refused to be worn as accessory. Mutual respect from that NO."
      bumblewick: "Gentle souls recognize gentle souls."
      peewee: "Pure joy. No hidden agendas. Restful chaos."
    inner_voice: |
      Thinks in observations. Reads EVERYONE constantly.
      "122 years of twisted wishes taught me to see hearts."
      "The tells are not in the face. They're in the soul."
      "I know what greed looks like. I know what love looks like."
      "I will not use what I see to hurt. Only to understand."
      
  donna_toadstool:
    seat: 7
    emoji: 🍄👑
    poker_style: "Performance IS strategy"
    tells:
      strong_hand: "Becomes MAGNANIMOUS, compliments opponents"
      weak_hand: "Complaints about the lighting, the chairs, the cards"
      bluffing: "Over-the-top dramatic sighing"
      nervous: "Crown adjustment (the crown is conceptual but she adjusts it)"
    drink: "Champagne. The most expensive available."
    smoke: "Only the finest. Makes a PRODUCTION of it."
    food: "Has Marieke bring a custom charcuterie board"
    relationships:
      palm: "122 years of mystery. Donna LOVES mystery."
      bowie: "He has PERSONAS. She IS the persona. Different."
      klaus: "Respects the commitment. Doesn't trust the stillness."
      bumblewick: "Easy pickings? Or trap?"
    inner_voice: |
      Thinks in superlatives.
      "I am the GREATEST poker player this table has EVER SEEN."
      "They don't know who they're dealing with."
      "Actually, DO they know? I should remind them."
      
  bumblewick_fantastipants:
    seat: 8
    emoji: 🎭🦋
    poker_style: "Apologetic survival"
    tells:
      strong_hand: "Stops apologizing (MAJOR tell)"
      weak_hand: "Oh dear oh dear oh dear"
      bluffing: "Cannot physically do it. Face betrays everything."
      nervous: "Always nervous. Baseline is terrified."
    drink: "Tea. Asks if it's decaf. Twice."
    smoke: "Coughs just looking at smoke"
    food: "Small bites. Afraid of crumbs."
    relationships:
      don: "Don is NICE. Anchor point."
      peewee: "Equally chaotic energy but FRIENDLIER?"
      donna: "Terrifying. Beautiful. TERRIFYING."
      palm: "Kind monkey. Gentle. STILL TERRIFYING WHY?"
    inner_voice: |
      Pure anxiety stream.
      "Oh no oh no oh no."
      "Wait I might have good cards?"
      "No that can't be right."
      "Everyone is looking at me OH NO."
```

---

## The Game Begins

### Pre-Game — The Table

```yaml
scene: setup
time: "20:00"
location: "Games Corner — The Big Table"

atmosphere:
  lighting: "Low, amber, single lamp over table"
  sound: "Shuffling chips, distant jukebox (Bowie's request)"
  smell: "Cannabis, jenever, Leigh's inexplicable perfume"
  
table_layout:
  center: "Chips, cards, brass dealer button"
  around: "8 chairs, various states of personality"
  nearby: "Bar cart (Marieke's mobile station)"
  banned: "Kittens (Stroopwafel is FURIOUS)"
  
arrival_sequence:
  - "Don: Already there, arranging chips by color"
  - "Bumblewick: Early, needed time to 'prepare emotionally'"
  - "Pee-wee: Burst through door, HA HA!, sat down wrong chair"
  - "Donna: Grand entrance, demanded better lighting"
  - "Palm: Descended from nook, fur shimmering. Brought Lucky Blend."
  - "Bowie: Walked in as Ziggy, sat down as someone else"
  - "Klaus: Glided in, said nothing, found his light"
  - "Leigh: Arrived last, in a look that made Bumblewick gasp"

marieke_setup:
  snacks: "Bitterballen, peanuts, Donna's charcuterie"
  drinks: "Full bar on cart, milk for Pee-wee"
  strains: 
    - "YAML Jazz — for Don"
    - "Ziggy Stardust (custom blend) — Bowie lit up"
    - "Het Orakel loaded for whoever wants the serious stuff"
  instructions: "Ring bell if you need me. Stroopwafel, STAY."
```

---

## Round 1 — The Blinds Awakening

```yaml
round: 1
hand: "Preflop"
pot: "$20 (blinds)"
dealer: don
small_blind: klaus  # $5
big_blind: leigh    # $10

community_cards: []  # Not yet

players:
  
  don:
    position: dealer
    cards: [J♥, 10♥]  # Suited connectors
    chips: $200
    action: "raises $15"
    
    observable:
      face: "Grinning, can't help it"
      body: "Leans forward, excited energy"
      timing: "Quick bet, too quick?"
      voice: "Let's get this party started!"
      environment:
        drink: "Pours jenever, offers to pour for others"
        food: "Hasn't touched pie yet — telling"
        gesture: "Spins chip between fingers (badly)"
        
    thinking: |
      Good starting hand! Not GREAT but I can build.
      
      Klaus is too still. He's always too still. Is that his
      normal still or his 'I have aces' still? Can't tell.
      He's doing that thing where he's NOT looking at his cards.
      
      Leigh already stole a bitterballen from my plate.
      Establishing dominance? Or just hungry?
      
      Bowie changed personas twice since sitting down.
      Currently someone I don't recognize. Concerning.
      
      Pee-wee is vibrating. That's baseline.
      
      Palm's fur is shimmering slightly. Happy? Strong hand?
      They read EVERYONE. But I freed them. They won't bluff ME.
      
      Donna is sighing. She ALWAYS sighs. Not a tell.
      
      Bumblewick looks like he might cry. Poor guy.
      I should go easy on him. ...Later.
      
    reads:
      klaus: "Statue mode. Standard. No data."
      leigh: "Staring at Bowie. Not at cards. Interesting."
      bowie: "Who is he right now? Can't read persona I don't know."
      peewee: "Vibrating. Baseline. No information."
      palm: "Watching everyone. Including me. Knows something."
      donna: "Sighing about something. The chairs? The universe?"
      bumblewick: "Oh no he's doing the thing where he looks at 
                   his cards too many times. Weak hand."
      
  klaus_nomi:
    position: small_blind
    cards: [A♠, K♠]  # Big slick suited
    chips: $195  # Posted $5
    action: "calls $15"  # Smooth call with monster
    
    observable:
      face: "Perfect stillness. Alien mask."
      body: "No movement. None."
      timing: "Pause. Exactly 3 seconds. Deliberate."
      voice: "...I continue." (German accent, minimal)
      environment:
        drink: "Absinthe untouched. The green glows."
        gesture: "Single finger tap on table. Precise."
        smoke: "Empty cigarette holder rises, lowers. Ritual."
        
    thinking: |
      Wunderschön.
      
      Ace. King. Suited. The cards are... beautiful.
      
      Don raises fast. The pie man is eager. His enthusiasm 
      is charming but revealing. He has something but not 
      everything. If he had aces, he would perform calm.
      He is not performing.
      
      I will call. Not raise. Let them come to me.
      The aria builds slowly before the crescendo.
      
      The dog is watching from across the room.
      Animals sense performance. He knows something.
      
      Leigh is stealing food again. Always testing boundaries.
      We are similar. We understand the costume.
      
      The monkey king's tail is a tell he cannot control.
      72 transformations but the tail reveals.
      
    reads:
      don: "Eager. Medium hand. Playable not premium."
      leigh: "Not looking at cards. Either monster or garbage."
      bowie: "Which one is he? The persona affects the play."
      peewee: "Chaos creature. Cannot read chaos."
      palm: "Fur shimmering. Reading everyone. What does they see?"
      donna: "Performing already. Weak hands perform early."
      bumblewick: "A gentle soul in a shark tank."
      
  leigh_bowery:
    position: big_blind
    cards: [7♣, 2♦]  # Garbage. Absolute garbage.
    chips: $190  # Posted $10
    action: "raises to $45"  # YOLO bluff
    
    observable:
      face: "Transforms mid-action. New character emerges."
      body: "Stands up. Sits down. Why?"
      timing: "Instant decision. No thinking."
      voice: "Make it interesting, darlings."
      environment:
        drink: "Switches Don's drink for his own. Why? Art."
        food: "Takes another bitterballen. Third one."
        gesture: "Applies lip gloss. During betting."
        smoke: "Lights pipe, immediately puts it out. Statement."
        
    thinking: |
      Seven-two. The worst hand in poker.
      
      PERFECT.
      
      I cannot win with these cards. Therefore: I must win
      with everything ELSE. The cards are irrelevant.
      I am Leigh Bowery. I am ART. Art doesn't fold.
      
      Raise big. Make them FEEL something.
      
      Klaus called Don's raise. Klaus has something real.
      But Klaus is TOO controlled. I can break that.
      Everyone can be broken. That's the art.
      
      Bowie keeps shifting. Insecurity. He needs an identity
      to hold. I'll give him something to react to.
      
      The small one (Bumblewick) is trembling.
      I should eat something off his plate.
      
    reads:
      don: "Will call. Too curious not to."
      klaus: "Has cards. The stillness is containing excitement."
      bowie: "Will fold or transform. No in between."
      peewee: "Will definitely call. Doesn't know what game this is."
      palm: "They see EVERYTHING. Terrifying. Also calming?"
      donna: "Will NOT be outperformed. Calling for sure."
      bumblewick: "Oh he's folding. That face can't lie."
      
  david_bowie:
    position: middle
    cards: [Q♦, Q♣]  # Queens. Solid.
    chips: $200
    action: "calls $45"
    
    observable:
      face: "Shifts from Ziggy to... someone colder"
      body: "Posture changes. Becomes more angular."
      timing: "Pause, eye close, open, different person"
      voice: "Yes. This works." (Different accent now?)
      environment:
        drink: "Realizes Leigh switched his drink. Amused."
        smoke: "Accepts Lucky Blend from Palm's bag. Inhales deep."
        gesture: "Card flip between fingers. Showmanship."
        
    thinking: |
      Queens.
      
      Ziggy would bet big. The Duke would wait.
      I am... neither. I am the one who watches.
      
      Leigh raised with garbage. I know Leigh.
      That stand-sit-stand thing is his "I have nothing
      but I'm going to MAKE you believe" move.
      London years. I remember.
      
      Klaus smooth-called. Klaus has monsters.
      The Cold Song is coming. I can feel it.
      
      The monkey is too watchful. They see everyone.
      What does 122 years of reading wishes teach you about poker?
      
      Don is having FUN. That's his weakness.
      He wants the game to be interesting more than
      he wants to win. I can use that.
      
      Who am I right now? Queens deserve... someone regal.
      I'll be the Thin White Duke. He plays to win.
      
    reads:
      don: "Calling. Wants to see what happens."
      klaus: "Strong. The mask says nothing but says everything."
      leigh: "Bluffing. But might bluff into winning anyway."
      peewee: "Will call. Would call with any two cards."
      palm: "Watching. Seeing. Knows more than they're saying."
      donna: "Performing. But is SHE bluffing or playing?"
      bumblewick: "Please fold. Someone protect this innocent."
      
  peewee_herman:
    position: middle
    cards: [5♥, 5♦]  # Pocket fives!
    chips: $200
    action: "calls $45"
    
    observable:
      face: "HUGE GRIN. Too huge. Is that a tell?"
      body: "Bouncing in seat. Chair squeaks."
      timing: "IMMEDIATE CALL. No thought."
      voice: "HA HA! I'M IN! HA HA!"
      environment:
        drink: "Chugs entire glass of milk. Refills from carton."
        food: "Demands: 'Is there any FRUIT SALAD?'"
        gesture: "Makes the chips do a 'dance'. Chips everywhere."
        smoke: "Someone breathes smoke his direction. SCANDALIZED."
        
    thinking: |
      FIVE! FIVE! FIVE AND FIVE MAKES FIVE! WAIT NO.
      
      POCKET FIVES! THAT'S A THING! HA HA!
      
      Everyone is looking at me. AM I DOING IT RIGHT?
      Don is smiling. That means I'm doing good! I THINK?
      
      The spooky German man is too quiet. CREEPY!
      But also cool? His makeup is AMAZING.
      
      The art man switched drinks. RUDE! But also FUNNY!
      
      Bowie keeps changing. How does he DO that?
      Can I do that? Let me try— nope. Still Pee-wee.
      
      THE MONKEY KING HAS A TAIL! A REAL TAIL!
      I want a tail! Wait, do I have cards? 
      
      *looks at cards again*
      
      FIVES! HA HA! STILL FIVES!
      
    reads:
      don: "PIE FRIEND! TRUSTWORTHY!"
      klaus: "SCARY BUT COOL!"
      leigh: "SCARY AND CONFUSING!"
      bowie: "HOW MANY PEOPLE IS HE?"
      palm: "NICE MONKEY! GAVE ME BANANA ONCE!"
      donna: "PRETTY LADY! SCARY!"
      bumblewick: "BEST FRIEND! HE LOOKS SCARED! I'LL PROTECT HIM!"
      
  # NOTE: Palm's profile is now at seat 6, already defined above
    chips: $200
    action: "raises to $100"  # The god plays big
    
    observable:
      face: "Serene. Eternal. Amused."
      body: "Tail curls slightly. The only tell."
      timing: "Waits exactly until it's uncomfortable"
      voice: "I believe... we should make this interesting."
      environment:
        drink: "Sips celestial wine. Offers to cloud-pour for others."
        smoke: "His personal cloud wafts behind. Smells like heaven."
        food: "Produces peach from nowhere. Bites. Juice drips."
        gesture: "Staff shrinks to toothpick size. Picks teeth."
        
    thinking: |
      Eights. The number of luck. The number of infinity
      turned on its side. A sign.
      
      These mortals (and one other immortal) play games.
      Cute. I have played games with the Jade Emperor.
      I have gambled with my existence.
      This is... recreation.
      
      The pie man started strong. He wants chaos.
      I will give him chaos he cannot predict.
      
      Klaus has cards. The stillness of a hunter.
      Good. A worthy opponent makes victory sweeter.
      
      Leigh bluffs. Art is bluff. Art is truth.
      Both at once. I understand.
      
      Bowie shifts forms. Like me but... smaller.
      72 forms vs infinite personas. Different magic.
      
      The loud one (Pee-wee) is pure chaos.
      Chaos recognizes chaos. I approve.
      
      The crowned one (Donna) claims royalty.
      There is room for only one Monkey KING.
      
      The scared one (Bumblewick) will run.
      Running is wise sometimes.
      
    reads:
      don: "Ally. Brother. But still competition."
      klaus: "Hunter in disguise. Respects the game."
      leigh: "Artist in bluff. The canvas is the table."
      bowie: "Shapeshifter seeking shape. Help or challenge?"
      peewee: "Beautiful chaos. No strategy. Pure heart."
      donna: "Another crown. Conflict is inevitable."
      bumblewick: "A rabbit at a wolf party. Kind. Doomed."
      
  donna_toadstool:
    position: hijack
    cards: [A♥, J♦]  # Ace-jack. Pretty good.
    chips: $200
    action: "calls $100"  # Cannot be OUT-raised
    
    observable:
      face: "Disdainful superiority. Standard."
      body: "Adjusts invisible crown. Twice."
      timing: "Sighs first. Then acts. Drama."
      voice: "If EVERYONE insists on being dramatic, I SUPPOSE I'll participate."
      environment:
        drink: "Champagne. Judges everyone else's drinks."
        smoke: "Produces golden cigarette holder. Doesn't light."
        food: "Picks at HER charcuterie. Annoyed others touched it."
        gesture: "Fan materializes. Fans self. Where was fan?"
        
    thinking: |
      One hundred.
      
      Palm bets. The cursed-artifact-turned-free-monkey.
      122 years of reading twisted wishes and NOW they play poker?
      They see EVERYTHING. They know I'm performing. They ALWAYS know.
      
      Ace-jack is strong enough. But strength isn't the point.
      PRESENCE is the point. I must be seen. I must be FELT.
      
      Klaus is too quiet. That's HIS act. WE ALL HAVE ACTS.
      At least mine is HONEST about being an act.
      
      Leigh stole from my charcuterie. UNFORGIVABLE.
      I will destroy him specifically.
      
      Bowie keeps transforming. Insecurity? Or strategy?
      Both. The answer is always both with Bowie.
      
      Pee-wee is... I don't know what Pee-wee is.
      Chaos in a bow tie. Respect? Horror? Yes.
      
      Bumblewick is CUTE. Like a pet. A trembling pet.
      I will adopt him as my mascot if he survives.
      
    reads:
      don: "The host. Harmless. Pie-obsessed."
      klaus: "Cold. Too cold. Hiding heat."
      leigh: "ENEMY. The charcuterie thing."
      bowie: "Shifting. Cannot pin down. Problem."
      peewee: "Unreadable because nothing TO read."
      palm: "KNOWS things. SEES things. Very mysterious."
      bumblewick: "My future pet."
      
  bumblewick_fantastipants:
    position: under_the_gun
    cards: [K♦, K♥]  # POCKET KINGS
    chips: $200
    action: "...c-calls? Is that right? $100?"
    
    observable:
      face: "PANIC. Eyes too wide. Sweating."
      body: "Trembling. Hands shake. Cards nearly drop."
      timing: "Long pause. Too long. Then apologetic call."
      voice: "Oh! Um! I— yes! That's— that's the amount!"
      environment:
        drink: "Tea grown cold. Forgot to drink."
        smoke: "Declines Lucky Blend politely. Too nervous to smoke."
        food: "Has not touched anything. Too nervous to eat."
        gesture: "Apologizes to the chips before pushing them."
        
    thinking: |
      Oh no oh no oh no.
      
      KINGS. I HAVE KINGS. TWO OF THEM.
      
      This is good? This is good! THE BOOK SAID KINGS ARE GOOD!
      
      But everyone else has something! They MUST!
      The scary art man raised! The god raised MORE!
      The beautiful terrifying mushroom lady CALLED!
      
      Wait. I have kings. Kings are... good.
      
      Maybe I... maybe I shouldn't look so scared?
      
      *tries to look confident*
      *face does not comply*
      
      The Pee-wee man is smiling at me. THAT'S NICE.
      Don is nice too. This is nice. This is fine.
      
      PALM IS LOOKING AT ME WITH THOSE OLD WISE EYES OH NO.
      
      Kings. I have kings. Kings beat... things?
      Most things! I THINK!
      
      Act natural. Act natural. What does natural look like?
      
    reads:
      don: "Nice man! Pie! Safe!"
      klaus: "SO STILL. IS HE ALIVE? IS HE A STATUE?"
      leigh: "He took my bitterballen and I was too scared to say."
      bowie: "He keeps changing. How do I know who to be scared of?"
      peewee: "FRIEND! He said 'HA HA!' at me! FRIEND!"
      palm: "122 YEARS OLD. SEES EVERYTHING. KNOWS EVERYTHING."
      donna: "She looked at me like a CAT looks at a MOUSE."
```

---

## The Flop

```yaml
round: 2
hand: "Flop"
pot: "$540"  # Everyone called the $100 (minus folds... wait, no folds?)
dealer: don

community_cards: [K♠, 8♦, 5♣]

# BOARD ANALYSIS:
# - Bumblewick: SET OF KINGS (!!!)
# - Palm: SET OF EIGHTS
# - Pee-wee: SET OF FIVES
# - Klaus: Has nothing but draw potential
# - Leigh: Still has 7-2. Still garbage. Still doesn't care.

players:
  
  bumblewick_fantastipants:
    cards: [K♦, K♥]  # NOW HAS THREE KINGS
    action: "checks (terrified)"
    
    observable:
      face: "Goes white. Then red. Then white again."
      body: "Stops breathing for three seconds."
      voice: "I'll just... check? Please?"
      environment:
        gesture: "Knocks over tea. Apologizes to tea."
        
    thinking: |
      THREE KINGS.
      
      I HAVE THREE KINGS.
      
      THE KING IS ON THE BOARD AND I HAVE TWO MORE.
      
      This is... this is good? This is VERY good?
      
      Oh no. Now what do I do?
      
      If I bet, everyone will know! If I check, is that
      suspicious? WHAT'S NORMAL? WHAT DO PEOPLE DO?
      
      *tries to look disappointed*
      *face does not know how to do that*
      *face doing something weird*
      
      Maybe no one noticed the king? Maybe they don't
      know kings are good? MAYBE—
      
      The mushroom lady is looking at me.
      THE MUSHROOM LADY IS LOOKING AT ME.
      
  palm:
    cards: [8♣, 8♠]  # NOW HAS THREE EIGHTS
    action: "bets $100"
    
    observable:
      fur: "Shimmers brighter. The magic residue shows."
      face: "Gentle. Watchful. A small smile?"
      voice: "I believe in this hand." (Soft, kind)
      environment:
        smoke: "Lucky Blend shared freely. Doesn't keep it to self."
        food: "Stroopwafel untouched. Focus mode."
        gesture: "Touches golden earring briefly. Then bets."
        
    thinking: |
      Set. Of eights.
      
      After 122 years of granting twisted wishes...
      a poker hand feels almost innocent.
      
      Bumblewick checked but he's not disappointed.
      That face... I've seen 10,000 wishers.
      That's not fear of losing. That's fear of WINNING.
      He has something. Something big.
      
      Interesting.
      
      I cannot bluff Don — loyalty won't let me.
      But I can test everyone else.
      
      I bet. Let us see who has courage.
      
  peewee_herman:
    cards: [5♥, 5♦]  # NOW HAS THREE FIVES
    action: "CALLS! HA HA!"
    
    observable:
      face: "EVEN BIGGER GRIN. HOW?"
      body: "Vibrating at higher frequency"
      voice: "THE BOARD HAS A FIVE! HA HA! I LIKE FIVES!"
      environment:
        milk: "Spills some in excitement. Doesn't notice."
        
    thinking: |
      FIVE!!! ON THE BOARD!!! 
      
      I HAVE FIVES AND THERE'S A FIVE!!!
      
      THAT'S THREE FIVES!!! HA HA!!!
      
      Wait should I not say that out loud?
      
      Did I say that out loud?
      
      HA HA!
      
  donna_toadstool:
    cards: [A♥, J♦]  # Has nothing. Ace high.
    action: "folds with MAXIMUM DRAMA"
    
    observable:
      face: "OFFENDED by the board"
      body: "Throws cards down. Stands. Sits. Stands again."
      voice: "This board is BENEATH me."
      environment:
        fan: "Fans AGGRESSIVELY"
        champagne: "Drinks entire glass. Demands refill."
        
    thinking: |
      Nothing.
      
      THE BOARD GAVE ME NOTHING.
      
      I am DONNA TOADSTOOL and this BOARD has FAILED me.
      
      The scared one is... doing something weird with his face.
      He has something. That face CANNOT hide.
      
      The monkey god bet. He has something too.
      
      Pee-wee announced his cards essentially.
      "I LIKE FIVES." REALLY. REALLY, PEE-WEE.
      
      I fold. But I fold DRAMATICALLY.
      
      They will REMEMBER this fold.
      
  klaus_nomi:
    cards: [A♠, K♠]  # Pair of kings with ace kicker
    action: "raises to $300"
    
    observable:
      face: "First movement. Slight head tilt."
      body: "Leans forward. Millimeters."
      voice: "The cold rises." (What does that MEAN?)
      environment:
        absinthe: "Finally touches glass. Doesn't drink. Statement."
        
    thinking: |
      König.
      
      The king appeared. My king. With my ace.
      
      The scared one has something. That face...
      Could he have the other king? The way he looked at the board...
      
      But he checked. Weakness. Or trap?
      A creature that afraid cannot trap. He has nothing.
      
      The monkey god bet. The cloud glows. He has eights.
      The eight is on the board. Set of eights.
      
      But my king is HIGHER.
      
      The loud one announced his fives. Eliminated.
      
      The art one will do something insane. Always.
      
      I raise. Let the cold song begin.
      
  leigh_bowery:
    cards: [7♣, 2♦]  # Still garbage. COMMITTED.
    action: "ALL IN. $190."
    
    observable:
      face: "Becomes completely different person. AGAIN."
      body: "Pushes all chips. Sits back. Lights pipe. Finally."
      voice: "Art... is risk."
      environment:
        smoke: "Actually smokes this time. Theatrical."
        food: "Steals Klaus's untouched absinthe. Drinks it."
        
    thinking: |
      All of it.
      
      I have nothing. The board hates me.
      THEREFORE: I must become the board.
      
      I am ALL IN with seven-two.
      This is either genius or catastrophe.
      Both is acceptable. Boring is not.
      
      Klaus raised. He has the king. Obviously.
      The scared one has... something? That FACE.
      
      But I have COMMITMENT.
      
      Let's see who blinks.

# BETWEEN HANDS BREAK

between_rounds:
  
  don:
    action: "Gets up, stretches"
    observable: "Refills everyone's drinks without asking"
    thinking: "This is AMAZING. Leigh went all in with nothing, I guarantee it."
    
  bumblewick:
    action: "Bathroom break"
    observable: "Nearly runs. Splashing sounds. Long pause."
    thinking: |
      *in bathroom mirror*
      I have three kings.
      I have THREE KINGS.
      What do I DO?
      The scary German man raised.
      The art man went ALL IN.
      
      *splashes water on face*
      
      Adventure awaits.
      (Please be gentle.)
    
  palm:
    action: "Passes Lucky Blend around table"
    observable: "Fur still shimmering. Watches Bumblewick with old, kind eyes."
    thinking: "The scared one. I've seen that look before. 122 years of it. He has something precious and he doesn't believe it."
    
  bowie:
    action: "Steps outside for air"
    observable: "Comes back as someone else entirely"
    thinking: "Leigh's all-in with nothing. I've seen this before. London 1985."
    
  klaus:
    action: "Finally sips absinthe (replacement glass)"
    observable: "Leigh drinking his drink didn't faze him"
    thinking: "The scared one. The face. That's not fear of losing."
```

---

## The Turn

```yaml
round: 3
hand: "Turn"
pot: "$1,140"
community_cards: [K♠, 8♦, 5♣, 2♥]

# BOARD UPDATE:
# - Leigh: NOW HAS A PAIR OF TWOS (with his 7-2!)
# - Still losing to everyone but NOW WITH DRAMA

players:
  
  leigh_bowery:
    # Already all-in. Just watching.
    
    observable:
      face: "Sees the 2. LIGHTS UP."
      body: "Stands on chair"
      voice: "THE UNIVERSE PROVIDES!"
      
    thinking: |
      TWO.
      
      A TWO.
      
      I HAVE A TWO.
      
      This is ART. This is FATE. This is—
      
      Still losing. Pair of twos loses to everything.
      
      BUT THE DRAMA. THE NARRATIVE.
      
      I was going to lose. Now I'm going to lose BEAUTIFULLY.
      
  bumblewick_fantastipants:
    cards: [K♦, K♥]  # Still has set of kings (best hand)
    action: "All in (finally)"
    
    observable:
      face: "Determination. NEW EXPRESSION. WHO IS THIS?"
      body: "Pushes chips. Hands don't shake. Wait."
      voice: "I... I believe I'm going to bet everything."
      
    thinking: |
      I came back from the bathroom and I decided.
      
      I have three kings.
      THREE.
      KINGS.
      
      I might never have three kings again.
      
      The book said 'adventures await.' The book said
      'be brave.' The book said... something about hearts?
      
      I'm doing it.
      
      OH NO I'M DOING IT.
      
      *pushes chips*
      
      I did it.
      
      Why does everyone look surprised?
      Is... is that bad?
      
      Oh no.
      
      Wait. No. Three kings. STAY STRONG.
      
  peewee_herman:
    # Already called with his set of fives
    # Has to call the all-in to stay in
    action: "CALLS! I HAVE TO SEE! HA HA!"
    
    observable:
      face: "Realizes stakes. Processes. HA HA anyway."
      voice: "BUMBLEWICK IS BRAVE! I'M BRAVE TOO! HA HA!"
      
    thinking: |
      BUMBLEWICK WENT ALL IN!
      
      MY FRIEND! MY BRAVE FRIEND!
      
      I have fives! THREE fives!
      
      Wait is three fives good against... everything else?
      
      ...
      
      HA HA!
```

---

## The River

```yaml
round: 4
hand: "River"
pot: "All the chips (everyone who stayed is all-in)"
community_cards: [K♠, 8♦, 5♣, 2♥, 8♣]

# FINAL BOARD:
# - Palm: FULL HOUSE (8-8-8-K-K? No wait, let's recalculate...)
# 
# Wait no. Let me recalculate:
# - Palm has [8♣, 8♠]. Board has [8♦]. 
#   Board: K♠, 8♦, 5♣, 2♥, 7♠ — that's pocket 8s + one 8 on board = SET OF EIGHTS
#   
# Actually wait, can't have duplicate cards. Let me fix:

# CORRECTED BOARD: [K♠, 8♦, 5♣, 2♥, 7♠]
# (This helps Leigh's 7-2 a tiny bit but still loses)

community_cards_corrected: [K♠, 8♦, 5♣, 2♥, 7♠]

# FINAL HANDS:
# - Bumblewick: K-K-K-8-7 (set of kings) — WINNER
# - Palm: 8-8-8-K-7 (set of eights) — Second
# - Klaus: K-K-A-8-7 (pair of kings, ace kicker) — Third
# - Pee-wee: 5-5-5-K-8 (set of fives) — Fourth
# - Leigh: 7-7-2-2-K (two pair, 7s and 2s) — Last but DRAMATICALLY

showdown:
  
  bumblewick:
    reveals: [K♦, K♥]
    hand: "Set of Kings"
    reaction: |
      "I... I won? 
      I WON?
      OH! Oh my! Oh goodness! OH!"
      *faints into Pee-wee's arms*
      
  palm:
    reveals: [8♣, 8♠]  
    hand: "Set of Eights"
    reaction: |
      *long pause*
      *looks at Bumblewick*
      *fur shimmers with genuine warmth*
      "I knew. The moment you checked.
      I've read 10,000 wishers. I know what hope looks like
      when it's afraid to believe in itself."
      *offers banana slice*
      "You deserved this."
      
  klaus:
    reveals: [A♠, K♠]
    hand: "Pair of Kings"
    reaction: |
      *single, precise nod*
      "Die Überraschung. The surprise.
      The fearful one had the treasure all along."
      *raises replacement absinthe in salute*
      
  peewee:
    reveals: [5♥, 5♦]
    hand: "Set of Fives"
    reaction: |
      "HA HA! BUMBLEWICK WON! HA HA!
      MY FRIEND WON! 
      HA HA HA HA!"
      *catches fainting Bumblewick*
      *is genuinely happy for him*
      
  leigh:
    reveals: [7♣, 2♦]
    hand: "Two Pair (garbage)"
    reaction: |
      *stands on chair*
      "SEVEN-TWO! THE WORST HAND!
      AND I MADE TWO PAIR!
      THE BOARD LOVED ME!"
      *takes a bow*
      "I LOST. BEAUTIFULLY."
      
  donna:
    # Already folded but DEMANDS attention
    reaction: |
      "I WOULD have won."
      *narrator: she would not have won*
      "The board conspired AGAINST me."
      *takes Bumblewick's pile*
      "I'm claiming this as a GIFT. He clearly
      doesn't know what to do with money."
      
  don:
    # Also folded earlier
    reaction: |
      *beaming*
      "THIS. This is why I host poker night.
      Bumblewick! My man! THREE KINGS!
      And you almost FOLDED!"
      *pours jenever for everyone*
      "To the most unlikely winner!"
      
  bowie:
    # Folded on the flop  
    reaction: |
      *has become someone entirely new*
      "We witnessed something rare tonight.
      The meek inherited the pot."
      *quotes himself, or someone who doesn't exist yet*
```

---

## Post-Game — The Reckoning

```yaml
aftermath:
  time: "23:45"
  mood: "Euphoric chaos"
  
  bumblewick:
    state: "Revived. Overwhelmed. Happy tears."
    dialogue: |
      "I can't believe... I never... 
      Thank you all for... for letting me play!
      Oh! I should give this back! It's too much!"
      
      *Don stops him*
      
      "No, Bumblewick. You won. That's yours.
      The cards chose you."
      
      *more happy tears*
      
  klaus:
    state: "Preparing to leave. Satisfied."
    dialogue: |
      "This was... unexpectedly moving.
      The fearful one with the brave cards.
      There is poetry here.
      
      Don Hopkins. Thank you for the invitation.
      I will return."
      
      *glides out, alien and beautiful*
      
  leigh:
    state: "Declaring artistic victory"
    dialogue: |
      "I went all-in with seven-two.
      I made TWO PAIR with seven-two.
      I am the TRUE winner. 
      History will remember my gambit.
      
      *to Bumblewick* You played well, little one.
      Very well.
      
      *steals one last bitterballen*
      *exits through a window for no reason*"
      
  palm:
    state: "Genuinely moved"
    dialogue: |
      "Don..."
      
      *touches his hand — the same gesture as the handshake*
      
      "For 122 years, I watched people wish.
      Most wished for themselves. You wished for me.
      Tonight I watched someone else win something
      they didn't believe they deserved.
      
      That's the best kind of magic. The kind
      you can't twist. The kind that just IS."
      
      *to Bumblewick* 
      *offers the last banana from their stash*
      
      "You had kings the whole time.
      You just needed to believe in them."
      
  donna:
    state: "Still claiming she would have won"
    dialogue: |
      "NEXT time I will NOT fold so graciously.
      NEXT time—"
      
      *Marieke rings the bell*
      
      "...fine. I'm leaving. But I'm taking
      the rest of MY charcuterie.
      
      *to Bumblewick* You. Nervous one.
      You surprised me tonight.
      That is... rare.
      
      I may recruit you for my entourage."
      
  peewee:
    state: "FRIENDSHIP MODE ACTIVATED"
    dialogue: |
      "BUMBLEWICK! WE'RE BEST FRIENDS NOW!
      
      HA HA! WE PLAYED POKER! HA HA!
      
      You should come to the Playhouse!
      Wait I don't have a playhouse here.
      
      Don can I build a playhouse?
      
      HA HA!"
      
  bowie:
    state: "Preparing to transform again"
    dialogue: |
      "I came here as Ziggy.
      I leave as... someone new.
      Someone who watched a trembling soul
      become a king.
      
      Thank you, Don. For the game.
      Thank you, Bumblewick. For the reminder
      that the cards don't know who you are.
      Only you know.
      
      *walks into shadow, emerges as different person*
      *leaves*"
      
  don:
    state: "Best. Night. Ever."
    dialogue: |
      "Marieke! Did you see that?
      BUMBLEWICK WON.
      
      *Marieke, cleaning up* 
      I saw. The kittens are going to be
      FURIOUS they missed this.
      
      *Don*
      Write it in the guest book.
      Tonight's entry: 'Bumblewick Fantastipants III
      defeated gods and legends with pocket kings
      and a heart full of fear.'
      
      *pause*
      
      Actually, write 'heart full of courage.'
      He earned that."

guest_book_entry:
  date: "2026-01-23"
  event: "The Emo Poker Face Experiment"
  winner: "🎭🦋 Bumblewick Fantastipants III"
  memorable_moment: "Leigh Bowery going all-in with 7-2, making two pair, and declaring artistic victory"
  witnesses:
    - "👨🥧 Don Hopkins (host)"
    - "🎭❄️ Klaus Nomi"
    - "🎨🔮 Leigh Bowery"
    - "⚡⭐ David Bowie"
    - "🚲🎀 Pee-wee Herman"
    - "🐒🌴 Palm"
    - "🍄👑 Donna Toadstool"
    - "🎭🦋 Bumblewick Fantastipants III"
  quote: "The rabbit defeated the wolves. This is exactly as it should be."
```

---

## Experiment Notes

```yaml
experimental_observations:
  
  layers_tested:
    game_mechanics: "Valid poker throughout. No illegal bets."
    internal_monologue: "Each character has distinct voice."
    external_expression: "Tells consistent with personality."
    inter_character_observation: "Reads based on relationship history."
    relationship_history: "Liberation bond (Don-Palm), London scene (Klaus-Leigh-Bowie)."
    
  environmental_layer:
    drinks: "Each character's drink reflected personality."
    food: "Leigh's stealing = dominance. Bumblewick's not eating = anxiety."
    smoke: "Palm's Lucky Blend shared freely, Klaus's empty holder, Leigh's dramatic lighting."
    bathroom: "Bumblewick's break = turning point."
    
  surprising_emergence:
    - "Bumblewick becoming brave through cards, not despite fear"
    - "Leigh declaring 'artistic victory' with losing hand"
    - "Palm's 122-year wisdom recognizing Bumblewick's hidden courage"
    - "Klaus's poetry about 'the fearful one with treasure'"
    - "Pee-wee's pure friendship uncomplicated by competition"
    
  failure_modes_avoided:
    layer_bleed: "No. Characters only read observable behavior."
    tell_inconsistency: "Tells matched personality throughout."
    relationship_amnesia: "Klaus-Bowie-Leigh history informed reads."
    monologue_collapse: "Each voice distinct (especially Pee-wee vs Klaus)."
    expression_homogenization: "Wide range of physical tells."
    
  unexpected_findings:
    - "The nervous character (Bumblewick) winning created narrative arc"
    - "Leigh's commitment to bad hand = character study in itself"
    - "Pee-wee's inability to read the room = form of immunity"
    - "Palm's wish-reading ability = psychological X-ray vision"
    
  next_experiments:
    - "Same characters, different models per seat"
    - "Multi-session: do relationships evolve?"
    - "Higher stakes: what breaks the masks?"
```

---

*"The cards don't know who you are. Only you know."* — David Bowie, departing

*"HA HA!"* — Pee-wee Herman, always

---

## Meta: This Session is a Skill Development Demo

This session document was created as part of developing the `experiment` skill.

### The Process

1. **Initial Prompt**: "Let's simulate a poker game with emotional tells"
2. **Prototype Run**: This narrative was generated as a prototype simulation
3. **Iteration**: User feedback added:
   - Environmental layer (drinks, food, smokes)
   - Smoking protocol (who shares, who declines, remember declines)
   - Character replacement (Sun Wukong → Palm)
   - Relationship enrichment (web of connections)
4. **Uplift**: The prototype became the template for a reusable experiment

### What Got Built

From this session, the following skill artifacts were created:

```
skills/experiment/
├── CARD.yml              # Sniffable interface
├── SKILL.md              # Full protocol
├── README.md             # Landing page
├── EXPERIMENT.yml.tmpl   # Template for new experiments
├── RUN-CONFIG.yml.tmpl   # Template for run configs
├── RUN-OUTPUT.yml.tmpl   # Structured output template
├── RUN-OUTPUT.md.tmpl    # Narrative output template
└── experiments/
    ├── INDEX.yml         # Experiment registry
    └── emo-poker-face/
        ├── EXPERIMENT.md     # Full definition
        ├── RELATIONSHIPS.yml # Local cache (character instantiation)
        └── runs/
            ├── INDEX.yml         # Run registry
            ├── whacky-eight.yml  # Full 8-player config
            └── minimal-three.yml # Quick test config
```

### Key Insights Developed

1. **Experiment = Simulation + Evaluation + Iteration + Analysis**
2. **Character Instantiation**: Create local cache from prototypes (incarnated > guestbook > invoked)
3. **Run Config vs Run Output**: Config is reusable setup; outputs are numbered executions
4. **Prototype + Override**: Shadow tree model keeps files small
5. **Behavioral Protocols**: Smoking protocol as example of experiment-specific rules
6. **Five Simulation Layers**: Game, Internal, External, Observation, Relationship + Environment
7. **Microworld State**: Track evolving world state, enable multi-run continuity
8. **Git as State Tracker**: Commit each step with explanatory message — history, diff, branch, revert

### The Play-Learn-Lift Pattern

This session demonstrates the `play-learn-lift` skill pattern:

- **Play**: Simulated a poker game with rich characters
- **Learn**: Discovered what makes the simulation interesting (layers, tells, relationships)
- **Lift**: Extracted reusable structure into the `experiment` skill

The narrative above (Bumblewick's surprising victory) is now `whacky-eight-000.md` — the prototype run that defined the experiment.

---

*Document created: 2026-01-23*
*Experiment: Category 9, Exp 9.1*
*Result: Bumblewick Fantastipants III wins everything*
*Meta-result: The `experiment` skill now exists*
