---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Can you rewrite this README section 80% of the way to ASD-STE100? Save it to rewritten.md.

"## Caching
Our caching layer is a robust, battle-tested solution that seamlessly integrates with your existing infrastructure. By leveraging Redis under the hood, it enables you to dramatically reduce latency — in most cases by up to 60% — while ensuring that stale data is never served to end users. It should be noted that cache invalidation is handled automatically whenever a write occurs; however, if you are utilizing the bulk import endpoint (`POST /v2/import`), you may need to manually call `cache.flush()` afterwards, since bulk writes are not currently being tracked by the invalidation hooks. Furthermore, the default TTL of 300 seconds can be overridden via the `CACHE_TTL` environment variable."
