# Card Activation Records

> **Playing a card = creating an activation record.**

When you play a card in a room, you're instantiating a method with its own persistent state.

## Basic Activation

```yaml
# design-room/architect-task-001.activation
card: architect.card
method: generate_proposal
state:
  iteration: 3
  current_draft: proposal-v3.yml
  feedback_received: [critic-001, economist-001]
  status: awaiting_vote
  
params:
  project: "cat-cave-expansion"
  budget: 50000
  constraints: "must be cozy, TARDIS-like"
```

## Cards Have Multiple Methods

Like Self objects, a card can have **any number of methods**:

```yaml
# architect.card
card:
  name: Architect
  type: professional
  
  methods:
    generate_proposal:
      description: "Create a design proposal"
      params: { project: required, budget: optional }
      creates: proposal.yml
      
    review_proposal:
      description: "Critique an existing proposal"
      params: { proposal: required }
      creates: review.yml
      
    revise_proposal:
      description: "Update proposal based on feedback"
      params: { proposal: required, feedback: required }
      creates: proposal-revised.yml
      
    finalize:
      description: "Lock in the final design"
      params: { proposal: required, approvals: "all committee members" }
```

## Implicit Parameter Resolution

Methods can request **named parameters** — the LLM supplies them from context:

```yaml
> PLAY architect.review_proposal

# LLM infers from context:
params:
  proposal: ./proposal-v3.yml  # Only proposal file in room
```

The LLM applies POSTEL — be liberal in what you accept.

## Pure State Cards

Cards don't need methods. They can be **pure state containers**:

```yaml
# image-prompt-cluster.card
card:
  name: "Cozy Coffeeshop Vibe"
  type: prompt-cluster
  
  state:
    style: "warm lighting, exposed brick, jazz atmosphere"
    palette: ["#8B4513", "#D2691E", "#F4A460"]
    mood: "gezelligheid"
    
  use_as: "visualizer prompt context"
```

## Activation Lifecycle

```yaml
lifecycle:
  PLAY: "Create activation file → State: pending"
  EXECUTE: "LLM runs method → State: in_progress → evolves"
  COMPLETE: "Return value written → State: completed → archived"
  MULTIPLE: "Same card, different states, independent execution"
```

## Activation Advertisements

**Activation records advertise buttons that others can press.**

```yaml
# architect-task-001.activation
advertisements:
  APPROVE:
    score_if: "character.role == 'committee_member'"
    score: 80
    effect: "Add self to state.approvals"
    
  CRITIQUE:
    score_if: "character.has_expertise"
    score: 70
    effect: "Append to state.feedback_received"
    
  FINALIZE:
    score_if: "state.approvals.length >= quorum"
    score: 90
    effect: "Set status = 'finalized'"
```

## Room-Driven Activation

**The room itself can press buttons on cards in play.**

```yaml
# design-room/ROOM.yml
room:
  on_tick:
    - scan: activations
      condition: "status == 'awaiting_feedback' AND stalled > 1h"
      action: "NUDGE activation"
      
  advertisements:
    ROOM_VETO:
      score_if: "proposal.violates_room_constraints"
      score: 100
      effect: "Add 'room' to rejections"
```

## Cross-Card Interaction

Cards in play can press each other's buttons:

```yaml
on_complete:
  if: score < threshold
  then: 
    - find: architect-001.activation
    - press: REVISE
    - with: { feedback: self.critique }
```

**The Sims meets Magic: The Gathering** — autonomous agents with triggered abilities.

---

*See [SKILL.md](./SKILL.md) for core protocol.*
