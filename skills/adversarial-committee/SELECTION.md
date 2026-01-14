# 🎯 Committee Selection Guide

> *"Diversity is essential. Balance enables consensus."*

This guide explains how `FORM-SMART` selects diverse committee members from a character pool.

---

## Selection Principles

### 1. Diversity is Essential

A good committee needs **opposing propensities** that create productive tension:

| Dimension | Why It Matters |
|-----------|----------------|
| **Propensity Type** | Different core perspectives (paranoid vs. idealist, operational vs. systems) |
| **Risk Tolerance** | Low/medium/high creates conflict over trade-offs |
| **Epistemology** | Different truth-finding methods prevent premature consensus |
| **Debate Role** | Different functions ensure comprehensive coverage |

### 2. Balance for Consensus

Too much diversity = endless debate. Too little = premature consensus.

**Ideal Committee Size:** 5-7 members
- **Minimum:** 3 members (too small, lacks diversity)
- **Maximum:** 9 members (too large, hard to reach consensus)

**Composition Guidelines:**
- **2-3 "pushers"** (low risk tolerance, devil's advocate) — prevent rushing
- **1-2 "optimists"** (high risk tolerance, opportunity scout) — surface opportunities
- **1-2 "analysts"** (evidence-based, systems thinking) — provide grounding
- **1 "synthesizer"** (medium risk, can bridge perspectives) — help reach consensus

### 3. Avoid Redundancy

Don't include multiple characters with:
- Same propensity type
- Same epistemology
- Same debate role

**Exception:** If you need multiple perspectives on the same dimension, ensure they differ on other dimensions.

---

## Selection Strategies

### Core Strategy (Default)

Mike Gallaher's canonical 5-member pattern:

```yaml
committee:
  members:
    - propensity: paranoid_realism     # Low risk, assume_bad_faith
    - propensity: idealism             # High risk, assume_good_faith
    - propensity: continuity_guardian  # Medium risk, trust_precedent
    - propensity: evidence_prosecutor  # Medium risk, prove_it
    - propensity: systems_thinking     # Varies risk, trace_feedback_loops
```

**Why This Works:**
- Maximum diversity: 5 propensities, 5 epistemologies, 5 roles
- Balanced risk: low, high, medium×2, varies
- Covers all bases: paranoia, idealism, precedent, evidence, systems

**Use When:** Need comprehensive exploration of a complex decision.

---

### Balanced Strategy

Extended committee for deeper exploration (6-7 members):

```yaml
committee:
  members:
    - # Core 5 members
    - propensity: operational_realism  # Adds operational focus
    - propensity: evidence_guardian    # Adds evaluation focus (optional)
```

**Why This Works:**
- Adds operational and evaluation perspectives
- Still maintains diversity
- Multiple evidence-focused roles but different functions

**Use When:** Need deeper operational and evaluation perspectives.

---

### Consensus Strategy

Optimized for reaching decisions without endless debate (5 members):

```yaml
committee:
  members:
    - propensity: paranoid_realism     # Pusher (prevents rushing)
    - propensity: idealism             # Optimist (surfaces opportunities)
    - propensity: continuity_guardian  # Synthesizer (bridges perspectives)
    - propensity: systems_thinking     # Analyst/Synthesizer
    - propensity: evidence_guardian    # Analyst (grounds discussion)
```

**Why This Works:**
- Fewer "prove_it" epistemologies (less evidence paralysis)
- Includes synthesizers who can bridge perspectives
- Still has tension (pusher vs. optimist) but balanced

**Use When:** Need to reach decisions efficiently while maintaining quality.

---

### Evidence Strategy

For decisions requiring rigorous proof (6 members):

```yaml
committee:
  members:
    - propensity: paranoid_realism     # Reality check
    - propensity: evidence_prosecutor  # Demands proof
    - propensity: evidence_guardian    # Guards evidence quality
    - propensity: evidence_architect   # Designs evaluation
    - propensity: systems_thinking     # Maps consequences
    - propensity: continuity_guardian  # Historical context
```

**Why This Works:**
- Multiple evidence-focused roles (prosecutor, guardian, architect)
- Still includes paranoia and systems thinking
- Precedent provides historical context

**Use When:** Decisions require extensive evidence gathering and validation.

---

### Innovation Strategy

For exploring new opportunities (6 members):

```yaml
committee:
  members:
    - propensity: idealism             # Optimist
    - propensity: opportunity_optimist # Optimist
    - propensity: cross_industry_innovator # Innovation focus
    - propensity: paranoid_realism     # Reality check
    - propensity: systems_thinking     # Consequences
    - propensity: evidence_prosecutor  # Evidence check
```

**Why This Works:**
- Multiple optimists explore opportunities
- Reality checks prevent reckless decisions
- Systems thinking maps consequences

**Use When:** Exploring new opportunities, products, or markets.

---

## Diversity Analysis

### Character Pool Requirements

Characters must have explicit propensities:

```yaml
character:
  propensity:
    type: paranoid_realism           # Required
    risk_tolerance: low              # Required
    epistemology: assume_bad_faith   # Required
    debate_role: devil's_advocate    # Required
    surfaces: [...]                  # What they reveal
    voice: "..."                     # Signature phrase
```

### Diversity Score

`FORM-SMART` calculates a diversity score:

```yaml
diversity_score:
  propensity_diversity: 5/5    # Unique propensity types
  risk_diversity: 3/4          # Unique risk tolerances (low, medium, high, varies)
  epistemology_diversity: 4/5  # Unique epistemologies
  role_diversity: 5/5          # Unique debate roles
  
  total: 17/19 (89%)
```

**Target:** 75%+ diversity score for effective committees.

---

## Selection Algorithm

### Step 1: Analyze Pool

- `propensity.type`
- `propensity.risk_tolerance`
- `propensity.epistemology`
- `propensity.debate_role`

**Inference Rule:** If `propensity` block is missing, INFER it from `mind_mirror`, `sims_traits`, and `description`.
- *Example:* High `innovative` + Low `conventional` + High `active` => `idealism` / `high risk`.
- *Example:* High `cautious` + High `sentimental` => `continuity_guardian` / `low risk`.

### Step 2: Apply Strategy

Based on selected strategy, identify required slots:

```yaml
# Core strategy slots
slots:
  - { propensity: paranoid_realism, role: devil's_advocate }
  - { propensity: idealism, role: opportunity_scout }
  - { propensity: continuity_guardian, role: historian }
  - { propensity: evidence_prosecutor, role: evidence_checker }
  - { propensity: systems_thinking, role: systems_analyst }
```

### Step 3: Match Characters

For each slot, find best-matching character:
1. Exact propensity match preferred
2. Similar propensity acceptable (e.g., `evidence_guardian` for `evidence_prosecutor`)
3. Ensure no duplicate characters

### Step 4: Verify Diversity

Check diversity dimensions:
- At least 4 unique propensities
- At least 3 unique epistemologies
- Mix of risk tolerances
- No duplicate debate roles

### Step 5: Generate Rationale

Output selection rationale:

```yaml
selection:
  strategy: core
  members:
    - maya-tilted-hat: "paranoid_realism, low risk, assume_bad_faith, devil's_advocate"
    - frankie-kerouac: "idealism, high risk, assume_good_faith, opportunity_scout"
    - joe-gusher: "continuity_guardian, medium risk, trust_precedent, historian"
    - vic-eyebrow: "evidence_prosecutor, medium risk, prove_it, evidence_checker"
    - tammy-silent: "systems_thinking, varies risk, trace_feedback_loops, systems_analyst"
    
  diversity:
    propensities: 5/5 unique
    epistemologies: 5/5 unique
    risk_tolerances: 4/4 (low, medium, high, varies)
    debate_roles: 5/5 unique
    
  rationale: |
    Selected for maximum diversity using core strategy.
    All 5 canonical propensities represented.
    Full epistemology coverage ensures no blind spots.
    Balanced risk tolerances create productive tension.
```

---

## Using FORM-SMART

### Basic Usage

```
FORM-SMART name="Strategy Review" purpose="Evaluate client engagement" pool="characters/" strategy="core"
```

### With Size Override

```
FORM-SMART name="Deep Dive" purpose="Technical architecture" pool="characters/" strategy="balanced" size=7
```

### With Include/Exclude

```
FORM-SMART name="Budget Review" purpose="Q3 budget allocation" pool="characters/" strategy="consensus" include=[marcus-chen] exclude=[tyler-brooks]
```

### Output

```yaml
# COMMITTEE.yml
committee:
  name: "Strategy Review"
  purpose: "Evaluate client engagement"
  
  members:
    - character: maya-tilted-hat
      role: devil's_advocate
      propensity: paranoid_realism
      risk_tolerance: low
      epistemology: assume_bad_faith
      
    - character: frankie-kerouac
      role: opportunity_scout
      propensity: idealism
      risk_tolerance: high
      epistemology: assume_good_faith
      
    # ... more members
    
  protocol: roberts-rules
  
  selection:
    strategy: core
    diversity_score: 89%
    rationale: "Maximum diversity using core strategy..."
```

---

## Selection Checklist

Before finalizing a committee, verify:

- [ ] **Diversity of propensities:** At least 4-5 different propensity types
- [ ] **Diversity of risk tolerance:** Mix of low, medium, and high
- [ ] **Diversity of epistemology:** At least 3 different epistemologies
- [ ] **Diversity of debate roles:** No duplicate roles (unless intentional)
- [ ] **Balance for consensus:** Include at least 1 synthesizer
- [ ] **Appropriate size:** 5-7 members (3 minimum, 9 maximum)
- [ ] **Topic fit:** Members' backgrounds align with decision topic

---

## When to Use ROBERTS-RULES

ROBERTS-RULES should be used when:

1. **Formal decisions required** (budget approval, strategic direction)
2. **Stakeholders need documented process** (compliance, transparency)
3. **Committee prone to premature consensus** (needs structured exploration)
4. **Multiple motions need consideration** (complex decision space)

Enable by setting `protocol: roberts-rules` in committee configuration.

---

## See Also

- [SKILL.md](SKILL.md) — Full adversarial-committee specification
- [CARD.yml](CARD.yml) — Methods and advertisements
- [../roberts-rules/](../roberts-rules/) — Parliamentary procedure
- [../rubric/](../rubric/) — Scoring criteria
- [../evaluator/](../evaluator/) — Independent assessment

