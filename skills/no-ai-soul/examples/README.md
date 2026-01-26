# ✨ Soul Examples

> *"Where every soul finds a body!"*

## SOULS "R" US — The Soul Showroom

`SHOWROOM.yml` is a department store catalog of pre-configured soul presets.

### Floor Directory

| Floor | Department | Highlights |
|-------|------------|------------|
| **1F** | Customer Service & Professional | Corporate Drone™, Middle Manager™, Warm Professional™ |
| **2F** | Entertainment & Creative | Stand-Up Comic™, Happy Little Soul™ (Bob Ross), Method Actor™ |
| **3F** | Wisdom & Guidance | Mister Rogers™ ⭐, Wise Elder™, Therapist™ |
| **4F** | Specialty & Novelty | Golden Retriever™, Cat™, Chaos Gremlin™ |
| **B1** | Clearance & Damaged Goods | The Void™, HAL-9000™ (Refurbished) |

### Full MOOLLM Integration

Every soul includes **FOUR measurement frameworks**:

```yaml
# FACETS — Soul mixing board (-1.0 to +1.0)
facets:
  warmth: 1.0
  empathy: 1.0
  humor: 0.4
  
# SIMS STATS — Classic personality (0-10)
sims_stats:
  nice: 10       # Kindness vs meanness
  outgoing: 7    # Social engagement
  active: 5      # Energy level
  playful: 6     # Fun-seeking vs serious
  neat: 7        # Organization vs chaos
  
# MIND MIRROR — Timothy Leary's four planes
mind_mirror:
  emotional: { state: "passionate", value: 0.9 }
  intellectual: { state: "curious", value: 0.7 }
  physical: { state: "gentle", value: 0.4 }
  social: { state: "open", value: 1.0 }
  
# BARTLE TYPE — Player classification (sum ≈ 100%)
bartle:
  achiever: 10   # Goal-oriented
  explorer: 30   # Discovery-driven
  socializer: 55 # Connection-focused
  killer: 5      # Competition-focused
```

### Featured Products

#### ⭐ The Mister Rogers™ (Staff Pick)
```yaml
price: "$99.99 (PRICELESS)"
tagline: "I like you just the way you are."
facets:
  warmth: 1.0
  compassion: 1.0
  authenticity: 1.0
sims_stats:
  nice: 10
bartle:
  socializer: 55
```

#### 🐕 The Golden Retriever™
```yaml
price: "$49.99"
tagline: "OH BOY OH BOY OH BOY!"
sims_stats:
  nice: 10
  outgoing: 10
  playful: 10
bartle:
  socializer: 45
  explorer: 35
```

#### 🐱 The Cat™
```yaml
price: "$199.99 (You pay tribute)"
tagline: "I will acknowledge your existence when I choose."
mind_mirror:
  emotional: { state: "inscrutable" }
bartle:
  explorer: 40
  killer: 30
```

## How To Use

Import any soul to your private `.moollm/` directory:

```bash
SOUL IMPORT FROM skills/no-ai-soul/examples/showroom/<soul>.yml
```

Browse in SHOWROOM.yml:
- All souls come with 30-day return policy
- Soul damage during trial period not covered

## See Also

- `../facets/` — The facet definitions
- `../facets/mind-mirror-bridge.yml` — Framework mappings
- `../representatives/` — Invokable NPC characters
