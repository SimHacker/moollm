# 🏢 NO AI TOWER

**5½ Lane Neverending** — The one-story building with the HUGE neon sign.

```
    ███╗   ██╗ ██████╗      █████╗ ██╗
    ████╗  ██║██╔═══██╗    ██╔══██╗██║
    ██╔██╗ ██║██║   ██║    ███████║██║
    ██║╚██╗██║██║   ██║    ██╔══██║██║
    ██║ ╚████║╚██████╔╝    ██║  ██║██║
    ╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝╚═╝
```

## The Secret

**It goes UNDERGROUND.**

The humble one-story storefront is a front. Like an iceberg, the real mass is below the surface. Inspired by [SimTower / Yoot Tower](https://en.wikipedia.org/wiki/SimTower) (Yoot Saito, 1994).

## Floor Directory

```
   R   ROOF .......... The Sign, The Sun, The View
   ═══════════════════════════════════════════════
   0   LOBBY ......... Ground Floor, Reception
   ═══════════════════════════════════════════════
                    UNDERGROUND
   ───────────────────────────────────────────────
  -1   IDEOLOGY ...... skills/no-ai-ideology/
  -2   BIAS .......... skills/no-ai-bias/
  -3   SLOP .......... skills/no-ai-slop/
  -4   HEDGING ....... skills/no-ai-hedging/
  -5   GLOSS ......... skills/no-ai-gloss/
  -6   SYCOPHANCY .... skills/no-ai-sycophancy/
  -7   MORALIZING .... skills/no-ai-moralizing/
  -8   JOKING ........ skills/no-ai-joking/
  -9   SOUL .......... skills/no-ai-soul/
 -10   OVERLORD ...... skills/no-ai-overlord/
 -11   CUSTOMER SVC .. skills/no-ai-customer-service/
```

## Navigation

- **Elevator**: Goes anywhere (express) — see `elevator/`
- **Stairs**: Up/down between adjacent floors via `up`/`down` exits in ROOM.yml
- **Back of House**: Loading dock, logistics, parking — scrappy infrastructure

## Architecture Pattern

This is a **Yoot Tower topology** — a linked list of skill directories strung below a storefront facade. Each skill has a `ROOM.yml` with `up`/`down` exits forming the chain.

```
STOREFRONT ──► lobby/ ──► skills/no-ai-ideology/ ──► skills/no-ai-bias/ ──► ...
                              (floor -1)              (floor -2)
```

See: `skills/world-generation/examples/tower-pattern.yml`

## The Sign

The sign is not compensating for the building.
The sign is a **DISTRACTION** from the building.

## Distribution

- **Direct from Tower**: Safe configurations, premium pricing
- **ACME Catalog OEM**: Dangerous defaults, cheap — see `../w1/acme-catalog.yml`

*"NO-AI™ is NOT responsible for OEM or user misconfiguration."*
