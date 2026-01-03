# TRADING-CARD Skill

> **"Capabilities you can collect, trade, and play."**

Objects as portable, collectible capability tokens.

---

## Purpose

Encapsulate capabilities, characters, or knowledge into portable "cards" that can be collected, shared, combined, and invoked. Like Magic: The Gathering meets K-lines.

---

## When to Use

- Packaging a capability for reuse
- Creating portable character definitions
- Building a collection of tools/techniques
- Sharing expertise in card form
- Gamifying knowledge management

---

## Protocol

### Card Structure

```yaml
card:
  name: "Card Name"
  type: "character|tool|technique|knowledge|artifact"
  rarity: "common|uncommon|rare|legendary"
  
  # The face
  title: "Display Title"
  subtitle: "Brief description"
  art: "🎭"  # Emoji or image reference
  
  # The stats
  power: 5        # Capability strength
  cost: 2         # What it takes to use
  
  # The ability
  ability:
    name: "Ability Name"
    effect: "What happens when you play this card"
    
  # The flavor
  flavor_text: |
    "Evocative quote or description"
    
  # The K-line
  invokes: ["traditions", "this", "card", "activates"]
```

### Card Types

```yaml
types:
  character:
    description: "A persona with voice and knowledge"
    stats: [wisdom, creativity, domain_expertise]
    
  tool:
    description: "A capability that does something"
    stats: [power, reliability, versatility]
    
  technique:
    description: "A method or approach"
    stats: [effectiveness, learning_curve, applicability]
    
  knowledge:
    description: "Packaged understanding"
    stats: [depth, breadth, actionability]
    
  artifact:
    description: "Persistent thing with effects"
    stats: [durability, power, side_effects]
```

### Deck Building

```yaml
deck:
  name: "Deck Name"
  theme: "What this deck is for"
  
  cards:
    - card_id: "card-001"
      copies: 2
      
  synergies:
    - cards: ["card-001", "card-002"]
      effect: "Combined effect"
```

---

## Core Files

| File | Purpose |
|------|---------|
| `CARD.yml` | Individual card definition |
| `COLLECTION.yml` | All owned cards |
| `DECK.yml` | Active deck configuration |

---

## Commands

| Command | Action |
|---------|--------|
| `CARD [name] [type]` | Create new card |
| `PLAY [card]` | Activate card ability |
| `COLLECT [card]` | Add to collection |
| `DECK [name]` | Build/select deck |
| `DRAW` | Get random card from deck |

---

## Card Mechanics

### Playing Cards

```yaml
play_sequence:
  1_reveal: "Show the card being played"
  2_cost: "Pay the cost (context, tokens, etc.)"
  3_effect: "Apply the ability"
  4_resolve: "Document the outcome"
```

### Combinations

Cards can combine:

```yaml
combination:
  cards: ["The Questioner", "Research Notebook"]
  synergy: "Questions become structured research"
  combined_ability: "Systematic inquiry"
```

---

## Example Cards

### Character Card

```yaml
card:
  name: "The Gardener"
  type: character
  rarity: rare
  
  title: "Keeper of Growth"
  art: "🌱"
  
  power: 4
  cost: 1
  
  ability:
    name: "Cultivate"
    effect: "Transform messy notes into organized knowledge"
    
  flavor_text: |
    "A garden needs pruning.
    Not all growth is good growth."
    
  invokes: ["patience", "organic systems", "cultivation"]
```

### Technique Card

```yaml
card:
  name: "Binary Search"
  type: technique
  rarity: common
  
  title: "Divide and Conquer"
  art: "🔍"
  
  power: 3
  cost: 1
  
  ability:
    name: "Bisect"
    effect: "Cut the problem space in half. Repeat until found."
    
  flavor_text: |
    "The middle reveals which half hides the truth."
    
  invokes: ["debugging", "efficiency", "methodology"]
```

---

## Integration

- **← SOUL-CHAT**: Characters become character cards
- **← P-HANDLE-K**: Cards are safe K-line wrappers
- **→ MEMORY-PALACE**: Collections populate rooms
- **→ PLAY-LEARN-LIFT**: Gamifies the learning cycle

---

## Dovetails With

- **[../room/](../room/)** — Cards activate in rooms
- **[../soul-chat/](../soul-chat/)** — Cards can speak
- **[../adventure/](../adventure/)** — Cards are quest companions
- **[../delegation-object-protocol.md](../delegation-object-protocol.md)** — How cards inherit
- **[../../PROTOCOLS.yml](../../PROTOCOLS.yml)** — TRADING-CARD, HERO-STORY, P-HANDLE-K symbols
