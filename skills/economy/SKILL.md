---
name: economy
description: Currency and trade — gold flows where stories lead
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
  - search_replace
related: [character, scoring, room, advertisement]
tags: [moollm, currency, trade, gold, commerce]
inputs:
  item:
    type: string
    required: false
    description: Item to buy, sell, or trade
  seller:
    type: string
    required: false
    description: NPC or entity selling
  buyer:
    type: string
    required: false
    description: NPC or entity buying
outputs:
  - character inventory update
  - transaction log
---

# 💰 Economy Skill

> **"Gold flows where stories lead."**

Economic systems for currency, trade, and value exchange. Money is earned, spent, hidden, and traded.

## Key Concepts

- **Currency** — Usually gold, can be custom
- **Earning** — Find, quest, sell, trade, work
- **Spending** — Buy items, services, information
- **Hidden value** — Not all gold is visible

## Currency

### Default Currency

Gold is the standard, but alternatives include:
- Reputation (social currency)
- Favors (barter)
- Skill tokens
- Custom per-adventure

## Earning

| Method | Examples |
|--------|----------|
| Exploration | Find treasure (hidden, maze, rewards) |
| Quests | Complete tasks (notice board, requests) |
| Trade | Sell items |
| Skills | Trade or teach skills |
| Games | Win at arcade, pub games, gambling |
| Work | Complete NPC jobs and requests |

## Spending

| Category | Typical Prices |
|----------|----------------|
| Food/Drink | 1-5 gold per item |
| Catalog Items | 3-50 gold per item |
| Lodging | 5 gold per night |
| Information | 5-20 gold (secrets, tips) |
| Services | Variable |

## Price Examples

### Cheap (1-2 gold)
- Stroopwafel: 1
- Coffee: 1
- Espresso: 2

### Moderate (3-5 gold)
- Snack: 3
- Tosti: 4

### Expensive (10-50 gold)
- Cannabis strain: 15
- Catalog gadgets: 25-50

### Catalog Items
- Mystery Box: 3
- Monkey's Paw: 5

## Hidden Value

Not all gold is visible. Exploration reveals hidden wealth:
- Kitchen drawer: 25 gold
- Mattress stash: 10 gold
- Secret compartment: variable

## Trade

### Barter

Items can be traded directly without currency. Value is negotiated between parties.

### Skill Trade

Skills themselves can be:
- Traded for items
- Taught for payment
- Auctioned to highest bidder
- Bequeathed to future characters

## Commands

| Command | Syntax | Checks |
|---------|--------|--------|
| `INVENTORY` | `INVENTORY` | Shows current gold amount |
| `BUY` | `BUY [item] FROM [seller]` | Gold available, item in stock |
| `SELL` | `SELL [item] TO [buyer]` | Fair value or negotiated price |
| `TRADE` | `TRADE [item/skill] FOR [item/skill]` | Relative value, relationship modifiers |

## Integration

| Skill | Relationship |
|-------|--------------|
| [character](../character/) | Gold stored in character inventory |
| [room](../room/) | Shops and merchants in rooms |
| [buff](../buff/) | Some buffs affect prices |
| [scoring](../scoring/) | Skills have economic value |
