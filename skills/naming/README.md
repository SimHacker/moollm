# 📛 Naming

> Big-endian file naming as semantic binding.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Uses naming for organization |
| [character/](../character/) | Character naming patterns |
| [yaml-jazz/](../yaml-jazz/) | Names carry meaning |
| [kernel/NAMING.yml](../../kernel/NAMING.yml) | Definitive reference |
| [k-lines/](../k-lines/) | Names ARE K-lines |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Files are named big-endian: `TYPE-VARIANT.ext`, e.g. `cat-terpie.yml`. The filesystem becomes a semantic network. Sorting reveals hierarchy.

## The Pattern

```
TYPE-VARIANT.ext
│    │
│    └── Specific instance
└────── Category/role

cat-terpie.yml      # A cat named Terpie
cat-stroopwafel.yml # Another cat
staff-marieke.yml   # Staff member
ROOM.yml            # Room definition (type only, no variant)
```

## Why Big-Endian?

- `ls` sorts by category first
- Easy to find "all cats" → `cat-*.yml`
- Clear inheritance hierarchy
- Inspired by Minsky's K-lines

