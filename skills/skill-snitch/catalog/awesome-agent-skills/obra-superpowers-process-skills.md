# obra/superpowers — Process-Level Skills Deep Dive

> The closest thing to MOOLLM in the wild. Not domain knowledge — HOW agents work.

**Author**: Jesse Vincent (@obra) | **License**: MIT | **Skills**: 14 | **Architecture**: Claude Code plugin with hooks, agents, commands, lib runtime

## Top 10 Ideas MOOLLM Should Adopt

1. **Two-stage review** (subagent-driven-development): spec compliance THEN code quality. Prevents reviewing quality on something that doesn't meet spec.

2. **TDD for skills** (writing-skills): write pressure scenarios (RED), write skill addressing rationalizations (GREEN), close loopholes (REFACTOR). The most novel idea in the repo.

3. **Rationalization tables**: every discipline skill lists the ways agents dodge it, with rebuttals. Standard skill furniture.

4. **Gate functions**: mental checkpoints before actions. Before mocking: "do I understand this dependency?" Before claiming done: "what's the proof command?"

5. **3-fix circuit breaker** (systematic-debugging): after 3 failed fixes, stop and question the architecture.

6. **CSO — Claude Search Optimization** (writing-skills): descriptions should say WHEN to use, never WHAT it does. Agents use descriptions as shortcuts.

7. **Fresh context per task**: subagents don't inherit stale context. The orchestrator pre-extracts and feeds context directly.

8. **Verification-before-completion**: "No completion claims without fresh verification evidence. Claiming done without evidence is dishonesty."

9. **Spec reviewer distrust**: "The implementer finished suspiciously quickly. Their report may be incomplete, inaccurate, or optimistic. VERIFY INDEPENDENTLY."

10. **Condition-based waiting over timeouts**: poll for actual conditions instead of `sleep(30)`.

## Skills Inventory

| Skill | MOOLLM Equivalent | Novel Contribution |
|-------|-------------------|-------------------|
| dispatching-parallel-agents | speed-of-light | "Group by problem domain" decision tree, anti-pattern list |
| subagent-driven-development | no equivalent (gap) | Two-stage review, prompt templates, fresh-context-per-task |
| test-driven-development | no equivalent (gap) | Rationalization table (12 excuses + rebuttals), nuclear option |
| systematic-debugging | debugging (partial) | 3-fix circuit breaker, defense-in-depth template |
| using-git-worktrees | no equivalent | Isolation for parallel agent work |
| writing-plans | sister-script (partial) | "Junior engineer with poor taste" persona for verification |
| executing-plans | speed-of-light (partial) | Batch-then-checkpoint pattern |
| brainstorming | debate (partial) | One question per message, 200-300 word design sections |
| verification-before-completion | no equivalent (gap) | Gate function: identify proof → run → read → verify → claim |
| finishing-a-development-branch | no equivalent | Exactly 4 options, typed confirmation for destructive ops |
| receiving-code-review | adversarial-committee (partial) | Anti-performative agreement, push-back protocol |
| requesting-code-review | evaluator (partial) | Structured review dispatch template |
| using-superpowers (meta) | bootstrap / .cursorrules | Rationalization table for meta-skill avoidance |
| writing-skills (meta) | skill / yaml-jazz | TDD for documentation, CSO, pressure testing |

## Architectural Comparison

| Dimension | Superpowers | MOOLLM |
|-----------|------------|--------|
| Metaphor | Mandatory workflows | Navigable microworld |
| Bootstrap | Hook injects meta-skill | .cursorrules → kernel → hot.yml |
| Discovery | Flat namespace, description matching | Semantic Image Pyramid, k-line activation |
| Multi-agent | Explicit subagent dispatch | Speed-of-light simulation |
| Quality | Two-stage review | Evaluator + adversarial-committee |
| Testing | Pressure scenarios with subagents | Not formalized (gap) |
| Token mgmt | Word count targets per tier | Semantic Image Pyramid levels |

Superpowers is operationally sharper. MOOLLM is architecturally richer. The combination would be formidable.
