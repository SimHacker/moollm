---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Convert this runbook step to strict ASD-STE100 style (full STE, not the softened version). Save it as runbook.md.

"Before running the migration, it is crucial that you have taken a full backup of the production database, since the migration script will be dropping the legacy_orders table and this cannot be undone. Once the backup has been verified, the maintenance window should be announced in #ops, after which you can go ahead and kick off the migration by running `./migrate.sh --env=prod`. The process typically takes 10-15 minutes; if it is still running after 30 minutes, you should abort it with Ctrl+C and roll back using `./rollback.sh 2026.11`."
