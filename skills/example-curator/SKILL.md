# Example Curator Protocol

## Invocation

```
CURATE <path> [--mode interactive|autonomous|advisory]
```

## Worker Loop

```
WHILE examples_exist:
    timestamped = SCAN for YYYY-MM-DD-*.yml
    canonical = SCAN for *.yml without timestamp
    
    clusters = CLUSTER(timestamped, by=semantic_similarity)
    
    FOR cluster IN clusters:
        IF cluster.matches(canonical):
            ARCHIVE timestamped (already represented)
        ELSE IF cluster.size >= 3:
            PROMOTE best_exemplar OR MERGE into new canonical
        ELSE:
            QUEUE for future analysis
    
    novel = DETECT patterns in timestamped not in canonical
    FOR pattern IN novel:
        PROPOSE new canonical
    
    AWAIT human approval OR auto-approve if configured
```

## Cluster Analysis

AI excels at:
- Semantic similarity across examples
- Abstracting concrete instances to general patterns  
- Detecting subtle variations of same anti-pattern
- Spotting gaps in canonical coverage

## Output Formats

### Promotion PR

```yaml
# Promoted from: 2026-01-18-alice-furthermore-abuse.yml
# Contributor: @alice
# Cluster: 12 similar examples analyzed
# Pattern: Unnecessary transition word abuse

name: transition-spam
violation:
  pattern: "Excessive 'Furthermore', 'Additionally', 'Moreover'"
  # ... rest of canonical format
```

### Merge Summary

```yaml
merged_from:
  - 2026-01-15-transition-spam.yml
  - 2026-01-18-alice-furthermore-abuse.yml
  - 2026-01-20-connecting-word-salad.yml
contributors:
  - @alice
  - anonymous (2)
pattern_synthesis: |
  Combined 12 examples into unified transition-spam canonical.
  Preserved best sub-examples from each contribution.
```

## Credit Attribution

Contributors can:
- Include handle in filename: `2026-01-24-alice-my-catch.yml`
- Include in metadata: `contributor: alice`
- Omit for anonymity

Curator MUST preserve attribution when promoting/merging.

## Self-Application

This skill can curate its own examples:

```
CURATE skills/example-curator/examples/
```

Recursion is intentional. The curator learns to curate better.
