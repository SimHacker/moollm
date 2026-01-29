# 🛒 GROCERIES

> "Tea. Earl Grey. Hot. And add milk to the replicator queue."

Dutch supermarket integration with smart shopping automation.
Sister scripts for Albert Heijn API, meal planning, and list management.

## Quick Start

```bash
# Anonymous (no login needed)
python scripts/ah.py search "hagelslag"
python scripts/ah.py bonus --week current
python scripts/ah.py stores --near "Amsterdam"

# Authenticated (requires 1Password setup)
python scripts/ah.py login
python scripts/ah.py receipts --limit 10
python scripts/ah.py orders
python scripts/ah.py list add "melk" "brood" "kaas"
```

## Architecture

```
skills/groceries/           # SHAREABLE (this repo)
├── CARD.yml                # Quick reference
├── SKILL.md                # This file
├── scripts/
│   ├── ah.py               # Albert Heijn API client
│   └── meal_plan.py        # Meal planning helper
├── templates/              # Config templates (copy to personal)
│   ├── config.yml.tmpl
│   ├── stores.yml.tmpl
│   └── pantry.yml.tmpl
└── examples/               # Trekified examples (safe to share)
    ├── enterprise-galley.yml
    ├── ds9-replimat.yml
    └── voyager-neelix.yml

~/.moollm/skills/groceries/ # PERSONAL (gitignored)
├── config.yml              # Your credentials, preferences
├── stores.yml              # Your preferred stores
├── pantry.yml              # Your inventory
├── lists/                  # Your shopping lists
└── history/                # Your order history

# OR in your own MOOLLM repo:
YourHome/household/shopping/  # PERSONAL (your repo)
├── INDEX.yml
├── current-list.yml
├── grocery/
│   ├── albert-heijn.yml
│   ├── meal-planning.yml
│   └── delivery-apps.yml
└── zooplus.yml
```

## Credentials — 1Password Integration

Store your supermarket credentials in 1Password, retrieve via `op`:

```bash
# Setup (one time)
op signin

# The script uses:
op read "op://Personal/Albert Heijn/email"
op read "op://Personal/Albert Heijn/password"
```

### Config Template

Copy `templates/config.yml.tmpl` to `~/.moollm/skills/groceries/config.yml`:

```yaml
# ~/.moollm/skills/groceries/config.yml
# GITIGNORED — contains personal data

credentials:
  method: "1password"  # or "env" or "direct"
  
  # 1Password paths
  op:
    ah:
      email: "op://Personal/Albert Heijn/email"
      password: "op://Personal/Albert Heijn/password"
    jumbo:
      email: "op://Personal/Jumbo/email"
      password: "op://Personal/Jumbo/password"
      
  # Or environment variables
  # env:
  #   ah_email: "AH_EMAIL"
  #   ah_password: "AH_PASSWORD"

preferences:
  default_store: "ah"
  delivery_address: "Your address here"
  
  # Dietary preferences for suggestions
  diet:
    vegetarian: false
    vegan: false
    gluten_free: false
    lactose_free: false
    
  # Favorite brands (for SUGGEST)
  brands:
    coffee: ["Douwe Egberts", "Lavazza"]
    cheese: ["Old Amsterdam", "Beemster"]
```

## Albert Heijn API

### Endpoints

| Endpoint | Auth | Description |
|----------|------|-------------|
| `/mobile-auth/v1/auth/token/anonymous` | No | Get anonymous token |
| `/mobile-auth/v1/auth/token` | Login | Get user token |
| `/mobile-services/product/search/v2` | Anon | Search products |
| `/mobile-services/v1/receipts` | User | Get receipts |
| `/mobile-services/v2/receipts/{id}` | User | Get receipt details |
| `/mobile-services/shoppinglist/v2/items` | User | Manage shopping list |
| `/gql` | Varies | GraphQL (bonus, categories) |

### Headers Required

```
User-Agent: Appie/8.22.3
Content-Type: application/json
Authorization: Bearer {access_token}  # for authenticated requests
```

### Authentication Flow

```
1. Visit: https://login.ah.nl/secure/oauth/authorize?client_id=appie&redirect_uri=appie://login-exit&response_type=code
2. Login with credentials
3. Get redirected to: appie://login-exit?code=CODE
4. Exchange code for token:
   POST https://api.ah.nl/mobile-auth/v1/auth/token
   {"clientId": "appie", "code": "CODE"}
5. Receive: {"access_token": "...", "refresh_token": "...", "expires_in": 7199}
```

## Sister Script: ah.py

### Structure (follows sister-script pattern)

```python
#!/usr/bin/env python3
"""Albert Heijn API client — groceries skill sister script."""

import argparse
import json
import subprocess
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
import requests

# --- CONFIGURATION ---
CONFIG_PATH = Path.home() / ".moollm/skills/groceries/config.yml"
TOKEN_CACHE = Path.home() / ".moollm/skills/groceries/.tokens.json"
API_BASE = "https://api.ah.nl"
USER_AGENT = "Appie/8.22.3"

# --- STATE ---
@dataclass
class AuthState:
    access_token: str | None = None
    refresh_token: str | None = None
    expires_at: float = 0

# --- CLI DEFINITION ---
def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Albert Heijn API client",
        epilog="See 'ah.py COMMAND --help' for details."
    )
    sub = parser.add_subparsers(dest="command")
    
    # SEARCH — Find products
    search = sub.add_parser("search", help="Search for products")
    search.add_argument("query", help="Search term")
    search.add_argument("--limit", type=int, default=10)
    search.add_argument("--bonus", action="store_true", help="Only bonus items")
    
    # BONUS — Get current deals
    bonus = sub.add_parser("bonus", help="Get bonus/sale items")
    bonus.add_argument("--week", default="current")
    bonus.add_argument("--category", help="Filter by category")
    
    # STORES — Find stores
    stores = sub.add_parser("stores", help="Find stores")
    stores.add_argument("--near", help="Location (city or coordinates)")
    stores.add_argument("--limit", type=int, default=5)
    
    # LOGIN — Authenticate
    sub.add_parser("login", help="Login to AH account")
    
    # RECEIPTS — Get purchase history
    receipts = sub.add_parser("receipts", help="Get receipts")
    receipts.add_argument("--limit", type=int, default=20)
    receipts.add_argument("--detail", help="Get specific receipt ID")
    
    # ORDERS — Get online orders
    orders = sub.add_parser("orders", help="Get online order history")
    orders.add_argument("--limit", type=int, default=10)
    
    # LIST — Manage shopping list
    list_cmd = sub.add_parser("list", help="Manage shopping list")
    list_sub = list_cmd.add_subparsers(dest="list_action")
    list_sub.add_parser("show", help="Show current list")
    list_add = list_sub.add_parser("add", help="Add items")
    list_add.add_argument("items", nargs="+", help="Items to add")
    list_clear = list_sub.add_parser("clear", help="Clear list")
    
    return parser

# --- IMPLEMENTATION ---
# (See full script in scripts/ah.py)
```

## Methods

### SEARCH — Find Products

```yaml
invoke: python scripts/ah.py search "kaas" --limit 5

example_output:
  - title: "AH Jong belegen kaas plakken"
    price: 2.49
    unit: "200g"
    bonus: true
    bonus_price: 1.99
```

### BONUS — Current Deals

```yaml
invoke: python scripts/ah.py bonus --week current

# Or via GraphQL for full details:
query: |
  query bonusCategories($input: PromotionSearchInput) {
    bonusCategories(filterSet: WEB_CATEGORIES, input: $input) {
      id
      title
      promotions {
        title
        price { now { amount } was { amount } }
      }
    }
  }
```

### LIST-SYNC — Sync to AH App

```yaml
invoke: python scripts/ah.py list add "melk" "brood" "eieren"

# Adds to AH shopping list via API:
# PATCH /mobile-services/shoppinglist/v2/items
# {"items": [{"productId": 123, "quantity": 1, "type": "SHOPPABLE"}]}
```

### RECEIPTS — Purchase History

```yaml
invoke: python scripts/ah.py receipts --limit 5

example_output:
  - transaction_id: "ABC123"
    date: "2026-01-28"
    store: "AH Amsterdam Centrum"
    total: 45.67
    items: 23
```

### ANALYZE — Pattern Analysis

```yaml
# After fetching receipts, analyze patterns:

patterns:
  most_bought:
    - "AH Halfvolle melk": 47 times
    - "AH Volkoren brood": 43 times
    - "Avocado": 38 times
    
  weekly_spend:
    average: "€127.50"
    min: "€45.00"
    max: "€210.00"
    
  shopping_days:
    saturday: 45%
    sunday: 30%
    wednesday: 15%
    
  bonus_usage:
    percent_bonus_items: "34%"
    estimated_savings: "€45/month"
```

## Trekified Examples

All examples use Star Trek terminology for safe public sharing:

### Enterprise Galley (examples/enterprise-galley.yml)

```yaml
# USS Enterprise NCC-1701-D — Deck 10 Forward Galley
# Trekified grocery data for safe sharing

ship: "🖖USS Enterprise NCC-1701-D"
location: "🖖Deck 10, Forward Section"
galley_chief: "🖖Lieutenant Commander Data (acting)"

replicator_queue:
  protein:
    - item: "🖖Replicated protein base (bovine)"
      english: "Ground beef"
      qty: "750g"
      
  produce:
    - item: "🖖Vulcan root vegetable"
      english: "Onion"
      qty: 2
    - item: "🖖Risan bell fruit"
      english: "Bell pepper"  
      qty: 3
      
  dairy:
    - item: "🖖Dairy matrix Type-7"
      english: "Sour cream"
      qty: 2
      priority: CRITICAL
      note: "🖖Captain's standing order"

commissary:
  preferred: "🖖Starbase 375 Commissary"
  backup: "🖖Deep Space 9 Promenade"
  
  account:
    officer: "🖖Captain Picard"
    contact: "🖖picard@starfleet.fed"
```

### DS9 Replimat (examples/ds9-replimat.yml)

```yaml
# Deep Space Nine — Promenade Replimat
# Quark's complaint: "The replicators are inferior to real food!"

station: "🖖Deep Space Nine"
establishment: "🖖Replimat (Promenade, Level 1)"
manager: "🖖Ensign Recurring Background Character"

inventory_issues:
  always_out_of:
    - "🖖Altarian mineral water (lime)"  # Jarritos
    - "🖖Bajoran spring wine"
    - "🖖Cardassian yamok sauce"
    
  overstocked:
    - "🖖Replicated tube grubs"
    - "🖖Synthesized gagh (dead)"

regular_orders:
  major_kira:
    usual: "🖖Raktajino, extra strong"
    frequency: "3x daily"
    
  odo:
    usual: "Nothing (doesn't eat)"
    frequency: "Judges others"
    
  quark:
    usual: "Real food, not replicated garbage"
    source: "🖖Personal suppliers (don't ask)"
```

## Integration with Your Repo

The groceries skill works with your personal MOOLLM repo:

```yaml
# In your repo: household/shopping/grocery/INDEX.yml

meta:
  skill: groceries
  integration:
    config: "~/.moollm/skills/groceries/config.yml"
    scripts: "moollm/skills/groceries/scripts/"
    
# Your real data stays in your repo
# Skill provides the automation
```

## Resources

### Libraries

| Language | Package | Status |
|----------|---------|--------|
| Go | `github.com/gwillem/appie-go` | Active (Jan 2026) |
| Node.js | `albert-heijn-wrapper` | Active |
| Python | `skills/groceries/scripts/ah.py` | This skill |

### Documentation

- **API Gist**: `gist.github.com/jabbink/8bfa44bdfc535d696b340c46d228fdd1`
- **GraphQL Schema**: `github.com/gwillem/appie-go/doc/graphql-schema-20260118.md`
- **OpenAPI Spec**: `github.com/NickBouwhuis/Albert-Heijn-OpenAPI`

### Community

- **Price Comparison**: `lijssie.nl` (AH, Jumbo, Dirk, Coop, etc.)
- **Gist Comments**: Active discussion on jabbink's gist

## See Also

- `skills/sister-script` — Script structure pattern
- `skills/trekify` — Privacy through technobabble
- `skills/inventory` — General inventory tracking
