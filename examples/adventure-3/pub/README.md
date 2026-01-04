# 🍺 The Rusty Lantern

> *"A warm, inviting tavern that somehow exists just south of where your adventure begins."*

A proper adventure needs a proper pub.

---

## 🎨 THEME SYSTEM

The pub can transform into **any environment you imagine**:

| Command | Result |
|---------|--------|
| `THEME DEFAULT` | Classic fantasy tavern |
| `THEME space cantina` | Sci-fi watering hole |
| `THEME cyberpunk bar` | Neon-lit undercity dive |
| `THEME victorian parlor` | Steampunk gentleman's club |
| `THEME pirate tavern` | Portside sea dog haunt |
| `THEME wild west saloon` | Frontier drinking establishment |
| `THEME [your description]` | **Anything you can imagine!** |

When you theme the pub:
- 🏠 The decor transforms
- 🧑‍🍳 The bartender changes identity (but keeps their mysterious knowledge)
- 👥 New patrons appear
- 📜 Menu updates (with theme-appropriate currency!)
- 🎲 Activities adapt

---

## 🍽️ Activities

| Activity | Command | Notes |
|----------|---------|-------|
| 🍺 **Drink** | `ORDER [item]` | Spend gold, hear rumors |
| 🍖 **Eat** | `EAT [item]` | Restorative, less dramatic than kitchen food |
| 🎯 **Darts** | `PLAY DARTS` | Challenge patrons, win bets/info |
| ♟️ **Chess** | `PLAY CHESS` | Reveals character, bartender is VERY good |
| 🃏 **Cards** | `PLAY CARDS` | Poker, blackjack, local games |
| 💬 **Socialize** | `TALK TO [patron]` | Quest hooks, rumors, alliances |
| 👂 **Eavesdrop** | `EAVESDROP` | Catch snippets, risk detection |
| 🎭 **Perform** | `PERFORM [act]` | Earn tips or thrown drinks |
| 🛏️ **Sleep** | `RENT ROOM` | Rest, dreams, time passes |

---

## 🧑‍🍳 The Bartender

**Grim** (default theme) — weathered, knowing, always polishing that glass.

The bartender:
- 🧠 **Knows everything** (but charges for specifics)
- 👁️ **Remembers everyone** (including Mother)
- 🔑 **Guards the back room** (earn access)
- 🎭 **Transforms with theme** (but stays mysterious)

### Key Topics

| Topic | Cost | Reveals |
|-------|------|---------|
| The maze | Free | General warnings |
| The grue | 10 gold | Patrol patterns |
| Mother | 30 gold | "She came through here..." |
| The skeleton | 10 gold | Full backstory |
| The back room | Prove yourself | ??? |

---

## 📢 Rumor Mill

The pub is an **information hub**:

| Source | Reliability | Cost |
|--------|-------------|------|
| Patrons | Variable | Free (buy them a drink) |
| Bartender | High | Gold |
| Notice board | Mixed | Free |
| Eavesdropping | Fragments | Risk |

### Sample Rumors

- ✅ "There's gold in the cold room of the maze"
- ⚠️ "A grue can be killed with cheese" (it was BLUE cheese!)
- ❌ "The bartender is actually the grue in disguise"
- 📌 "Someone's been asking about YOUR family..."

---

## 🚪 The Back Room

A mysterious door leads to... **whatever the story needs**.

Possibilities:
- Underground fighting ring
- Secret guild meeting
- Portal to another theme dimension
- Mother's favorite booth from her adventuring days
- Shortcut to the maze (or trap?)

**Access:** Prove yourself to the bartender.

---

## 🎲 Objects

| Object | Purpose |
|--------|---------|
| 🧑‍🍳 [bartender.yml](./bartender.yml) | The mysterious keeper |
| 🎯 [dart-board.yml](./dart-board.yml) | Games of skill |
| ♟️ [chess-table.yml](./chess-table.yml) | Games of strategy |
| 🃏 [card-deck.yml](./card-deck.yml) | Games of chance |
| 🔥 [fireplace.yml](./fireplace.yml) | Warmth, hearthstone secret |
| 📋 [notice-board.yml](./notice-board.yml) | Jobs, quests, warnings |
| 👻 [pacman-cabinet.yml](./pacman-cabinet.yml) | Wakka wakka wakka |
| 🏓 [pong-cabinet.yml](./pong-cabinet.yml) | The game that started it all |
| 🍒 [fruit-machine.yml](./fruit-machine.yml) | One-armed bandit |

---

## 🌟 Special Events

| Event | Trigger | Effect |
|-------|---------|--------|
| **Last Call** | Late adventure | "Time to go home, adventurer" |
| **Mother's Tab** | Low on gold | One-time credit from her account |
| **The Regulars** | Third visit | Patrons recognize you |
| **Bartender's Favor** | Help another patron | Free drink, significant gesture |

---

## 🧭 Navigation

| Exit | Destination |
|------|-------------|
| 🚪 NORTH | [../start/](../start/) — Chamber of Commencement |
| ⬆️ UP | Inn rooms (requires payment) |
| 🚪 BACK | ??? (earn access) |

---

## 📚 Lineage

The pub is a tribute to:
- **Bar Karma** (Will Wright & Don Hopkins) — First crowdsourced TV series. A bar at the edge of the universe where lost souls face karmic crossroads. StoryMaker tool for collaborative script writing and community voting.
- Every mysterious D&D tavern
- The cantina in Star Wars
- Rick's Café in Casablanca
- The Prancing Pony (LotR)
- Cheers (everybody knows your name)

*This is where quests begin and end. And the community shapes the story.*
