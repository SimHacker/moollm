# 🛒 Groceries Skill

> "Computer, replicate my usual grocery order."

Dutch supermarket integration with smart shopping automation.

## Features

- **Albert Heijn API** — Search products, check bonus deals, sync shopping lists
- **1Password Integration** — Secure credential storage
- **Meal Planning** — Generate shopping lists from recipes
- **Pattern Analysis** — Understand your shopping habits
- **Trek Examples** — Safely shareable example data

## Quick Start

```bash
# Anonymous (no login needed)
python scripts/ah.py search "hagelslag"
python scripts/ah.py bonus --week current

# Setup credentials (one time)
# Add to 1Password: "Personal/Albert Heijn" with email & password fields

# Authenticated
python scripts/ah.py login
python scripts/ah.py receipts --limit 10
python scripts/ah.py list add "melk" "brood" "kaas"
```

## Architecture

```
skills/groceries/        # SHAREABLE (this repo)
├── CARD.yml             # Quick reference
├── SKILL.md             # Full protocol  
├── scripts/ah.py        # Albert Heijn API client
├── templates/           # Config templates
└── examples/            # 🖖 Trekified examples

~/.moollm/skills/groceries/  # PERSONAL (gitignored)
├── config.yml           # Your preferences
└── .tokens.json         # Auth tokens (auto-managed)
```

## Personal Data

Your real grocery data belongs in one of two places:

1. **Local config** — `~/.moollm/skills/groceries/` (gitignored)
2. **Your MOOLLM repo** — e.g., `YourHome/household/shopping/`

The skill works with either location. Examples in this repo are "trekified" with Star Trek terminology for safe sharing.

## Requirements

```bash
pip install requests pyyaml

# For 1Password integration
# Install op CLI: https://1password.com/downloads/command-line/
```

## See Also

- [SKILL.md](SKILL.md) — Full protocol documentation
- [CARD.yml](CARD.yml) — Quick reference
- [examples/](examples/) — Trekified example data
