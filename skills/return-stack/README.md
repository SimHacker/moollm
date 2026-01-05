# 🔙 Return Stack

> Where you've been is where you can go back to

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Navigation history as a first-class **continuation** — a stack of saved positions you can manipulate like browser history or a call stack.

## The Metaphor

| Programming | Browser | MOOLLM |
|-------------|---------|--------|
| Call stack | History | Return stack |
| Return address | Back button | Previous room |
| Stack frame | Tab | Room context |
| Push | Navigate | ENTER |
| Pop | Back | BACK |

## Commands

| Command | Effect |
|---------|--------|
| `ENTER room` | Push current, enter new |
| `BACK` | Pop, return to previous |
| `FORWARD` | Redo after BACK |
| `HISTORY` | Show the stack |
| `BOOKMARK` | Save position |
| `GOTO bookmark` | Jump to saved |
| `FORK` | Create parallel stack |

## Related Skills

- [room](../room/) — rooms are stack frames
- [adventure](../adventure/) — navigation through rooms
