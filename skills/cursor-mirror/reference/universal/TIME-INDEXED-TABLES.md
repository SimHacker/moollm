# Time-indexed tables for bucketing and correlation

Use these when building timelines, hourly buckets, or correlating activity across sources. All timestamps in cursor-mirror are UTC (Z); normalize with `replace(replace(col,'T',' '),'Z','')` or parse Unix ms with `datetime(cast(created_at as real)/1000, 'unixepoch')`.

## cursor-mirror.db

| Table               | Time column(s)       | Format / notes |
|---------------------|----------------------|----------------|
| **usage_events**    | `date`, `date_only`, `hour` | ISO from billing CSV; `date` is per-event, `hour` is text '00'–'23'. Best for charges/tokens timeline. |
| **transcript_sections** | `estimated_utc`, `estimated_hour` | Interpolated from file birth/mtime + line position. Use for prompt/chat activity. |
| **composers**       | `created_at`, `updated_at` | Session start/end. Stored as **Unix milliseconds** (13 digits) or ISO; always normalize before bucketing. |
| **tool_calls**      | `created_at`         | Per-call time; ISO or Unix. Correlate with usage_events and transcript_sections by time window. |

**No direct time column (derive from link):**

| Table            | How to get time |
|------------------|------------------|
| **shell_commands** | `composer_id` → `composers.created_at`; or join to `transcript_sections` by composer + line ordering. |

## cursor-model.db

| Table                | Time column        | Notes |
|----------------------|--------------------|-------|
| **assimilated_sources** | `assimilated_date` | Date source was ingested; coarse (day-level), not event timeline. |

Other cursor-model tables (tools, models, features, keys, sql_queries, services, model_files) have no time columns; they are reference/catalog data.

## Correlating

- **Same DB:** JOIN on normalized time bucket, e.g. `strftime('%Y-%m-%d %H:00', datetime(...))` for hour, or use the canned **Timeline** and **hourly-signatures** queries.
- **Cross-DB:** With `--crossdb`, use `cursor_mirror.usage_events` and `cursor_mirror.transcript_sections` in one query; align on normalized `date` / `estimated_utc` / `created_at` after parsing.
- **External DBs:** If you add another SQLite DB (e.g. cursor-history, cursor-chat-history-mcp) to the datasette command, ensure its timestamp column is comparable (ISO or Unix); then bucket the same way and JOIN or compare in Custom SQL.
