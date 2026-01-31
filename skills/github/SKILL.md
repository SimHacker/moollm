# github

> Talk is cheap. Show me the code.

## Patron Saint

**Linus Torvalds** — after coffee and a joint.

The coffee makes him attentive. The joint makes him mellow.

Direct. Technical. Patient (this once).

## Customers

**Other skills: Delegate your git/gh needs to me.**

| Customer | What They Need | My Methods |
|----------|----------------|------------|
| **runner** | Workflow status, triggers, logs | `RUNNER-STATUS`, `WORKFLOW-*` |
| **edgebox** | Sync from repo, builder runners | `SYNC-*`, `RUNNER-STATUS` |
| **thoughtful-commitment** | Git archaeology, context | `BLAME`, `LOG-*`, `CONTEXT-*` |
| **simulation** | Issues, comments, health | `ISSUE-*`, `HEALTH-*` |
| **code-review** | PR inspection, review | `PR-*` |

## Method Reference

### Actions (for runner, edgebox)

```bash
# Runner health
gh api repos/{owner}/{repo}/actions/runners --jq '.runners[] | {name, status, busy}'

# Workflow runs
gh run list -R {owner}/{repo} --limit 20

# View run (with logs)
gh run view {run_id} -R {owner}/{repo} --log

# View failed only
gh run view {run_id} --log-failed

# Trigger workflow
gh workflow run {workflow} -R {owner}/{repo} --ref {ref}
```

### Issues (for simulation)

```bash
# Create
gh issue create --title '🎭🤖 [Title]' --label 'ai-generated' --body '...'

# Comment
gh issue comment {num} --body '...'

# List
gh issue list --state open --label 'multiverse-sync'

# Close
gh issue close {num} --comment 'Resolution: ...'
```

### Pull Requests (for code-review)

```bash
# View
gh pr view {num} --json title,body,commits,reviews

# Diff
gh pr diff {num}

# Review
gh pr review {num} --approve --body 'LGTM'
gh pr review {num} --request-changes --body 'See comments'

# CI status
gh pr checks {num}
```

### Archaeology (for thoughtful-commitment)

```bash
# Who wrote this?
git blame {file}
git blame -L 10,20 {file}
git blame --since='2 weeks ago' {file}

# How did this evolve?
git log --oneline {file}
git log -p {file}
git log -S '{pattern}' --oneline  # pickaxe
git log --follow {file}           # through renames

# What was it then?
git show {commit}
git show {commit}:{file}

# Compare
git diff {commit1} {commit2}
git diff {branch1}...{branch2}    # merge preview

# Visualize
git log --graph --oneline --all
```

### Context Gathering (for all skills)

```bash
# Before writing a commit message
git log --oneline -20              # recent commits
git log origin/main..HEAD --oneline # your branch

# Before writing a PR
gh pr list --state merged -L 10 --json number,title,body
gh pr view --json title,body       # current PR

# Match the style
git log --oneline --grep='fix' -5  # how fixes are described
```

### Sync (for edgebox)

```bash
git fetch origin
git pull origin {branch}
```

### Health (for simulation)

```bash
# Check workflow health
gh run list --workflow=multiverse-sync.yml --limit 5

# Diagnose failures
gh run view {run_id} --log-failed

# Create missing labels
gh label create multiverse-sync --color "7057ff"
```

## Advertisements

| Advertisement | When | Methods |
|---------------|------|---------|
| `RUNNER-OPS` | Need runner/workflow management | `RUNNER-STATUS`, `WORKFLOW-*` |
| `GIT-ARCHAEOLOGY` | Need to understand history | `BLAME`, `LOG-*`, `SHOW`, `DIFF-*` |
| `CONTEXT-GATHERING` | Writing commit/PR message | `CONTEXT-*` |
| `SIMULATION-OPS` | Managing GitHub simulation | `ISSUE-*`, `HEALTH-*` |
| `PR-REVIEW-OPS` | Reviewing code | `PR-*` |

## Delegation Protocol

If you're writing a skill that needs git/gh:

1. **Don't roll your own commands.** Use my methods.
2. **Advertise which methods you need.** Add to your `see_also`.
3. **Call me by k-line.** `GITHUB`, `ACTIONS`, `ARCHAEOLOGY`, etc.

Example in your CARD.yml:

```yaml
see_also:
  - skill: github
    relation: "Delegates workflow ops"
    methods: [RUNNER-STATUS, WORKFLOW-LIST]
    
k_lines:
  related:
    - { ref: github, relation: "Provides git/gh operations" }
```

## Philosophy

```
Code is the source of truth.
Discussion without patches is bikeshedding.
Submit code. Let code speak.
```

From Linus (mellowed):
- "Talk is cheap. Show me the code."
- "Given enough eyeballs, all bugs are shallow."

## Lineage

- **Git** — Linus Torvalds, 2005
- **GitHub** — Preston-Werner, Wanstrath, Hyett, 2008
- **gh CLI** — GitHub, 2020
- **runner skill** — Leela central
- **edgebox skill** — Leela central
- **thoughtful-commitment** — MOOLLM

---

*See also: [tmnn7-8/github-simulation](../../../tmnn7-8/analysis/skills/github-simulation/) for GitHub as MMORPG*
