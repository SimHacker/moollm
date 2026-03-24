# Timeline: 2 minutes before and after most expensive request

**Center (UTC):** 2026-02-12T13:04:23.860Z  
**Window:** 13:02:24 – 13:06:24 UTC (2 minutes either side)  
**Timezone:** All times are UTC (Z = Zulu = GMT/UTC). The cursor-mirror DB stores billing and event timestamps in UTC.

---

| Time (UTC) | Type | Summary | Source |
|------------|------|---------|--------|
| 2026-02-12T13:02:58.502Z | usage | $9.56 claude-4.6-opus-high-thinking | usage_events (id 225) |
| 2026-02-12T13:03:43.514Z | usage | $1.33 claude-4.6-opus-high-thinking | usage_events (id 224) |
| **2026-02-12T13:04:23.860Z** | **usage** | **$27.97 claude-4.6-opus-high-thinking** | usage_events (id 223) |

No chat (transcript_sections) or tool_calls in this 4-minute window in the DB; only billing events. The $27.97 request is the most expensive in the window and matches the “Most Expensive Requests” row.

---

*Generated from cursor-mirror.db with the timeline query (window_minutes=2).*
