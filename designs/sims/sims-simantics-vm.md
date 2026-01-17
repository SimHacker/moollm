# SimAntics Virtual Machine → MOOLLM

> *The visual programming language inside The Sims*
> *Skills are programs. The LLM is the VM.*

## The Insight

SimAntics was The Sims' secret weapon: a visual programming language embedded in the game engine. Every object's behavior — how a Sim uses a toilet, how a refrigerator dispenses food, how a phone connects calls — was written in SimAntics "tree code."

MOOLLM takes this further: **skills are programs, the LLM is the virtual machine.**

---

## Tree Code

**Sims:** Behaviors were "trees" — branching decision structures:

```
IF person.bladder < 20
  THEN walk_to_toilet
    IF toilet.occupied
      THEN wait_or_find_another
    ELSE use_toilet
      decrement bladder
      play animation "relieve"
```

**MOOLLM:** Skills are natural language programs the LLM interprets:

```yaml
# skills/needs/SKILL.md

When bladder need is critical:
1. Check nearby facilities
2. If occupied, queue "wait" or "find alternative"
3. Execute relief action
4. Update need state in CHARACTER.yml
5. Apply comfort buff if successful
```

The structure is the same — conditional behavior trees. The syntax is prose instead of nodes.

---

## Tree Tables

**Sims:** Every object had a "tree table" — a registry of available interactions:

| Tree ID | Name | Type | Guard |
|---------|------|------|-------|
| 0 | Init | Private | Always |
| 1 | Use | Public | is_adult |
| 2 | Clean | Public | is_dirty |
| 3 | Repair | Public | is_broken AND has_skill |

**MOOLLM:** [CARD.yml](../skills/card/) advertised methods:

```yaml
# pub/bar/bartender.yml
advertised_methods:
  SERVE-DRINK:
    type: public
    guard: customer.in_pub
    
  RESTOCK:
    type: private
    guard: inventory.low
    
  REPAIR-TAP:
    type: public  
    guard: tap.broken AND actor.has_skill("repair")
```

Same pattern: a registry of what this object can do, with guards controlling availability.

---

## Primitives

**Sims:** SimAntics had ~150 primitives — atomic operations:

| Primitive | Function |
|-----------|----------|
| `Sleep` | Pause execution |
| `Expression` | Math operations |
| `Run Subroutine` | Call another tree |
| `Set Motive` | Change need value |
| `Route` | Pathfinding |
| `Animate` | Play animation |
| `Create Object` | Spawn new object |
| `Relationship` | Modify social bonds |

**MOOLLM:** LLM-native primitives are semantic:

| MOOLLM Concept | Function |
|----------------|----------|
| `WAIT` | Pause in action queue |
| Empathic Expressions | Any computation the LLM can understand |
| `DELEGATE-TO` | Call another skill |
| Modify `needs:` in YAML | Change need value |
| Navigate exits | Move between rooms |
| Prose description | "Animation" is narration |
| Create `.yml` file | Spawn new entity |
| Update `relationships:` | Modify social bonds |

SimAntics had 150 primitives because they were hardcoded. MOOLLM has *infinite* primitives because the LLM can understand any operation described in prose.

---

## Subroutines

**Sims:** Trees could call other trees:

```
Tree: "Make Dinner"
  Call: "Go To Kitchen"
  Call: "Open Refrigerator"
  Call: "Get Ingredients"
  Call: "Cook Food"
  Call: "Serve Meal"
```

**MOOLLM:** Skills compose through delegation:

```yaml
# skills/cooking/CARD.yml
advertised_methods:
  MAKE-DINNER:
    delegates_to:
      - room.GO-TO: kitchen
      - fridge.OPEN
      - inventory.GET: ingredients
      - stove.COOK
      - table.SERVE
```

Or in prose:

```markdown
## MAKE-DINNER

1. Navigate to kitchen using [room](../room/) skill
2. Interact with fridge using its CARD.yml methods
3. Gather ingredients per [inventory](../inventory/) protocol
4. Use cooking station per object's behaviors
5. Serve using [social](../social/) interaction patterns
```

Skills are subroutines. Composition is natural language.

---

## Return Values

**Sims:** Trees returned true/false, controlling flow:

```
IF [Try To Use Toilet] returns TRUE
  THEN play_happy_animation
ELSE
  play_frustrated_animation
```

**MOOLLM:** Skills return structured results:

```yaml
# After action execution
result:
  success: true
  effects:
    bladder: +50
    comfort: +10
  narrative: "Palm finds relief at the facilities."
```

Or simply: the LLM continues the narrative, implying success or failure through what happens next.

---

## Parameters

**Sims:** Trees could receive parameters:

```
Tree: "Animate"
  Param 0: animation_id (int)
  Param 1: speed (float)
  Param 2: loop (bool)
```

**MOOLLM:** Method parameters are YAML or natural language:

```yaml
# Explicit parameters
SERVE-DRINK:
  params:
    drink_type: string
    size: [small, medium, large]
    garnish: optional string
```

Or implicit through context — "serve the usual" means the LLM knows what "usual" means for this customer.

---

## Comments

**Sims:** SimAntics trees had comments explaining logic:

```
// Check if sim is adult before allowing alcohol
IF person.age >= 18
  allow_drink
```

**MOOLLM:** [Comment Intelligence](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#comment-intelligence). Comments are first-class:

```yaml
# Only adults may order from the bar
# This respects pub/bar/ROOM.yml access rules
access:
  minimum_age: 21
  # Note: age_check is responsibility of budtender
```

Comments aren't ignored — they're context that shapes LLM behavior.

---

## Tree Properties

**Sims:** Every tree had metadata:

| Property | Purpose |
|----------|---------|
| Name | Human-readable identifier |
| Format | Parameter types |
| Flags | Private, blocking, etc. |
| Returns | What the tree produces |

**MOOLLM:** Skill metadata in `CARD.yml`:

```yaml
id: bartender-serve-drink
version: 1.0.0
requires_tools: [read_file, write_file]

advertised_methods:
  SERVE-DRINK:
    visibility: public
    blocking: false
    returns: drink_object
    satisfies: [thirst, social]
```

Same pattern: structured metadata describing behavior properties.

---

## Tree Tracing

**Sims:** The Edith editor could trace tree execution:

```
> TRACE "Make Dinner"
[0] Enter Make Dinner
[1]   Call Go To Kitchen
[2]     Route to (12, 8)
[3]     Arrive
[1]   Return TRUE
[4]   Call Open Refrigerator
...
```

**MOOLLM:** The [return-stack](../skills/return-stack/) skill:

```yaml
# After action completion
call_trace:
  - skill: room/GO-TO
    target: kitchen
    result: arrived
    
  - skill: object/INTERACT
    target: fridge
    action: OPEN
    result: opened
    
  - skill: inventory/GET
    items: [eggs, cheese, bread]
    result: acquired
```

Tracing for debugging and understanding causality.

---

## Tree Debugging

**Sims:** Breakpoints in SimAntics trees:

```
BREAKPOINT at "Cook Food" line 12
> Inspect: person.cooking_skill = 3
> Inspect: stove.heat = 350
> Continue
```

**MOOLLM:** Debugging through inspection:

1. Read the YAML files to see current state
2. Ask the LLM "why did this happen?"
3. The LLM explains its reasoning
4. Check [return-stack](../skills/return-stack/) for decision history

No formal breakpoints — the LLM can always explain itself.

---

## The VM Comparison

| SimAntics VM | MOOLLM LLM |
|--------------|------------|
| Interprets tree nodes | Interprets prose skills |
| ~150 hardcoded primitives | Infinite semantic operations |
| Compiled behavior files | YAML + Markdown files |
| Type-checked parameters | Context-understood arguments |
| Stack-based execution | Narrative-based flow |
| Visual debugging in Edith | Conversational debugging |
| Returns bool/int | Returns structured YAML or prose |
| Object-attached trees | Directory-attached skills |

---

## The Evolution

SimAntics was revolutionary for 1997 — a visual programming language accessible to designers, not just programmers. Objects could have complex behaviors without C++ code.

MOOLLM completes the evolution:

```
1997: Visual programming (SimAntics)
      ↓
2015: Natural language understanding (LLMs)
      ↓
2026: Skills as prose programs (MOOLLM)
```

The final step: you don't need visual tools OR programming syntax. You write what you want in prose. The LLM understands.

---

## Tree Code Example: Toilet

**SimAntics (1997):**

```
Tree: Use Toilet (ID: 127)
├─ [0] Test: person.bladder < 50?
│   └─ FALSE → Exit (Return FALSE)
├─ [1] Route to toilet slot
├─ [2] Test: toilet.occupied?
│   └─ TRUE → Queue(Wait 10 ticks) → Goto [1]
├─ [3] Animate: "sit_down"
├─ [4] Expression: person.bladder = 100
├─ [5] Expression: toilet.dirty += 10
├─ [6] Animate: "stand_up"
├─ [7] Animate: "flush"
└─ [8] Exit (Return TRUE)
```

**MOOLLM (2026):**

```markdown
# skills/bathroom/SKILL.md

## USE-TOILET

When a character needs to use the toilet:

1. **Check need** — Only proceed if bladder need is pressing
2. **Navigate** — Route to bathroom, check toilet availability
3. **Wait if occupied** — Queue a brief wait, retry
4. **Use facility** — Describe the action appropriately
5. **Update state**:
   - Set bladder need to satisfied
   - Increase toilet cleanliness debt
6. **Narrate exit** — Character resumes activities

### State Changes

```yaml
after:
  character.needs.bladder: 100
  toilet.cleanliness: -10
```

The logic is identical. The expression is human.

---

## Why This Matters

SimAntics proved that:
1. Complex behaviors can emerge from simple primitives
2. Non-programmers can author interactive content
3. The simulation is in the *composition*, not the engine

MOOLLM inherits all of this:
1. Complex behaviors emerge from simple skill invocations
2. Anyone who can write prose can author skills
3. The simulation emerges from *skill composition* in natural language

SimAntics was the proto-LLM for objects. MOOLLM is the realized vision.

---

## See Also

- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — Full architecture
- [skills/action-queue/](../skills/action-queue/) — Action execution
- [skills/return-stack/](../skills/return-stack/) — Execution tracing
- [skills/card/](../skills/card/) — Method advertisements (tree tables)
- [sims-find-best-action.md](./sims-find-best-action.md) — Autonomy algorithm
- [sims-happy-friends-home.md](./sims-happy-friends-home.md) — The design that needed SimAntics

---

*"SimAntics Programming Primitives Subroutines Return Values Parameters Comments Tree Properties Tree Tracing Tree Debugging Tree Breakpoints"*

Every one of these exists in MOOLLM — as natural language.
