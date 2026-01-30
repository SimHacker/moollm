# github

> Talk is cheap. Show me the code.

## Patron Saint

**Linus Torvalds** — but after coffee and a joint.

The coffee makes him attentive. The joint makes him mellow.

This is Linus at his best: direct, technical, precise — but patient enough to explain once, clearly, without calling you a fucking moron.

He still *thinks* it. He just doesn't *say* it.

## The Philosophy

```
Discussion without patches is bikeshedding.
Submit code. Let code speak.
```

## Quick Reference

### Issues

```bash
gh issue create --title "Bug: X doesn't work" --body "Steps to reproduce..."
gh issue list --state open
gh issue comment 42 --body "Fixed in PR #43"
```

### Pull Requests

```bash
gh pr create --title "Fix: Handle edge case" --body "..."
gh pr view 43
gh pr review 43 --approve
gh pr merge 43
```

### Commits

```
type(scope): subject

Body explains WHY, not WHAT.
The diff shows WHAT.
```

Types: `fix`, `feat`, `docs`, `refactor`, `test`, `chore`

### Branches

```bash
git checkout -b feature/new-thing
# ... work ...
git push -u origin HEAD
gh pr create
```

## Inherits From

- **postel** — Be liberal in what you accept, strict in what you emit
- **robust-first** — Handle edge cases before happy path
- **code-review** — Systematic review practices

## See Also

- `tmnn7-8/analysis/skills/github-simulation/` — GitHub as MMORPG
- `tmnn7-8/analysis/skills/github-user/` — Characters as GitHub actors
