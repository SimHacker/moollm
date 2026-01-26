# Dialog Layers — Universal Transformation System

Dialog layers are NOT just "personalization for a player character."  
They're a **general transformation system** — like translation layers.

The same architecture that compiles "dialog for Don Hopkins" can compile:
- Dialog in French
- Dialog for Don Hopkins *in French*
- Dialog for children (simplified)
- Dialog in Pirate English (Arr!)
- Dialog for blind users (extra spatial descriptions)
- Dialog for speedrunners (terse)

## Key Structure

```
{character}:{language}:{style}:{accessibility}
```

| Key | Example |
|-----|---------|
| `don-hopkins:en:default:standard` | Don, English, normal |
| `don-hopkins:fr:default:standard` | Don, French |
| `generic:en:pirate:standard` | Arr matey! |
| `generic:en:noir:standard` | Hard-boiled detective |
| `generic:en:default:blind` | Extra spatial descriptions |

## Four Dimensions

| Dimension | Purpose | Examples |
|-----------|---------|----------|
| **character** | WHO is playing? NPCs react to soul | don-hopkins, dr-no, generic |
| **language** | Human language | en, fr, ja, pirate, shakespeare |
| **style** | Tone and verbosity | default, dramatic, terse, noir |
| **accessibility** | Adaptations for needs | standard, blind, deaf, cognitive |

## Compilation

Layers compile at **export time**, not runtime:

1. Start with base dialog from prototypes
2. Apply character-specific overrides
3. Apply language translation
4. Apply style transformation
5. Apply accessibility adaptations
6. Result: fully baked dialog tree

**Benefits:** No runtime overhead, human-editable, works offline.

## Example Transform

**Base:**
> OVERLORD: "Welcome to NO AI TOWER."

**don-hopkins:en:pirate:**
> OVERLORD: "Arrr, Don Hopkins! The scallywag what invented them circular treasure maps! Welcome aboard, ye old seadog."

**generic:en:noir:**
> The door creaked open. "Welcome to NO AI TOWER," it rasped. It was gonna be that kind of night.

## Fan Fiction

Layers can be **generated**, not just translated:
- **Transform**: Restyle existing layers
- **Generate**: New characters, crossovers, AUs
- **Share**: Community marketplace, remix chains
