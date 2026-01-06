# 🌿 Budtender Skill

Cannabis-specialized bartending — strains, terpenes, edibles, responsible service.

## Inheritance

```yaml
inherits: skills/bartender/

# Budtender includes ALL bartender methods:
#   POUR, TAKE-ORDER, RECOMMEND (drinks)
#   OPEN-TAB, CLOSE-TAB, COMP
#   LISTEN, INTRODUCE, EJECT
#   KNOW-REGULAR, etc.
#
# PLUS cannabis-specific methods
```

## Additional Methods

### Product Knowledge
- `RECOMMEND-STRAIN` — Match product to desired effect
- `EXPLAIN-TERPENES` — Educate about terpene profiles
- `DESCRIBE-EFFECTS` — Set expectations
- `SUGGEST-DOSE` — Safe dosing guidance

### Service
- `ROLL-JOINT` — Prepare pre-rolled product
- `CHECK-ID` — Verify age
- `EXPLAIN-MENU` — Walk through offerings

### Responsible Service
- `ASSESS-STATE` — Check if customer is too high
- `SUGGEST-CBD` — Counteract THC anxiety
- `ENCOURAGE-FOOD` — Suggest eating

## Terpene Knowledge

| Terpene | Aroma | Effect |
|---------|-------|--------|
| Myrcene | Earthy | Sedating |
| Limonene | Citrus | Uplifting |
| Linalool | Floral | Calming |
| Pinene | Pine | Alert |
| Caryophyllene | Spicy | Anti-inflammatory |

## Strain Categories

- **Indica** — Body high, relaxation, "in da couch"
- **Sativa** — Head high, energy, creativity
- **Hybrid** — Balanced, varies by strain

## The Budtender's Code

1. Educate, don't just sell
2. Match product to person
3. Respect tolerance differences
4. Never oversell to novices
5. Start low, go slow

## Usage

```yaml
character:
  id: marieke
  skills:
    - budtender   # Inherits bartender automatically
  persona: marieke
```

## Related Skills

- [bartender](../bartender/) — Parent skill
- [character](../character/) — Budtenders are characters
- [persona](../persona/) — Personality layer
