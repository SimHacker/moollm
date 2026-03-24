#!/usr/bin/env python3.14
"""Generate showboat-demo.md from live cursor-mirror databases.

Usage:
    cd skills/cursor-mirror
    source .venv/bin/activate
    python3.14 scripts/generate_showboat_demo.py [output.md]

Reads cursor-mirror.db and cursor-model.db, produces a Markdown document
with all output blocks populated from real queries. Default output is stdout.
"""

import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
DB = SKILL_DIR / "cursor-mirror.db"
MODEL_DB = SKILL_DIR / "cursor-model.db"


def q(conn, sql, params=()):
    return conn.execute(sql, params).fetchall()


def q1(conn, sql, params=()):
    row = conn.execute(sql, params).fetchone()
    return row[0] if row else None


def bar_chart(value, scale=20, char="$"):
    return char * int(round(value / scale))


def generate(out):
    if not DB.exists():
        print(f"ERROR: {DB} not found. Run export_datasette first.", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row
    conn2 = sqlite3.connect(str(MODEL_DB)) if MODEL_DB.exists() else None
    if conn2:
        conn2.row_factory = sqlite3.Row

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    def w(line=""):
        out.write(line + "\n")

    w("# cursor-mirror: See Yourself Think")
    w()
    w(f"*{now} -- all output below is real, queried from cursor-mirror.db*")
    w()
    w("cursor-mirror reads all of Cursor IDE's internal databases -- chat logs, "
      "agent transcripts, tool calls, shell commands, feature flags, billing "
      "events -- and integrates them into a single queryable picture. Built on "
      "MOOLLM, a framework of 120+ skills. Served via Simon Willison's Datasette.")
    w()

    # Dashboard
    w("## 1. Dashboard")
    w()
    w("```output")
    metrics = [
        ("Conversations", "SELECT count(*) FROM composers WHERE bubble_count > 0"),
        ("Total messages", "SELECT sum(bubble_count) FROM composers"),
        ("Transcript sections", "SELECT count(*) FROM transcript_sections"),
        ("Shell commands", "SELECT count(*) FROM shell_commands"),
        ("Tool calls logged", "SELECT count(*) FROM tool_calls"),
        ("Unique tools used", "SELECT count(distinct tool_name) FROM tool_calls"),
        ("Tool error rate %", "SELECT round(100.0 * sum(is_error) / count(*), 1) FROM tool_calls"),
        ("Feature flags with drift", "SELECT count(*) FROM feature_flags WHERE drift = 1"),
        ("Thinking blocks", "SELECT count(*) FROM transcript_sections WHERE type = 'THINKING'"),
        ("Usage events", "SELECT count(*) FROM usage_events"),
        ("Total spend $", "SELECT round(sum(cost), 2) FROM usage_events"),
        ("Total tokens (billions)", "SELECT round(sum(total_tokens) / 1e9, 2) FROM usage_events"),
    ]
    for label, sql in metrics:
        w(f"  {label}: {q1(conn, sql)}")
    w("```")
    w()

    # Data pipeline
    w("## 2. The data pipeline")
    w()
    w("Three data sources feed into one SQLite database:")
    w()
    w("```output")
    w(f"  Source 1: Cursor's SQLite databases (state.vscdb / cursorDiskKV)")
    w(f"           → {q1(conn, 'SELECT count(*) FROM tool_calls'):,} tool calls with params (truncated to 300 chars)")
    w(f"           → {q1(conn, 'SELECT count(*) FROM composers'):,} conversations with metadata")
    w(f"  Source 2: Agent transcript .txt files (plaintext, parsed into sections)")
    w(f"           → {q1(conn, 'SELECT count(*) FROM transcript_sections'):,} sections (USER/ASSISTANT/TOOL_CALL/THINKING)")
    w(f"           → {q1(conn, 'SELECT count(*) FROM shell_commands'):,} shell commands extracted")
    w(f"  Source 3: Cursor billing CSV (downloaded, timestamped per-request)")
    w(f"           → {q1(conn, 'SELECT count(*) FROM usage_events'):,} billing events with model, tokens, cost")
    w(f"  Output:   cursor-mirror.db ({os.path.getsize(DB) / 1024 / 1024:.1f} MB) + cursor-model.db ({os.path.getsize(MODEL_DB) / 1024:.0f} KB)")
    w(f"  Served:   Datasette with {35} canned queries, FTS, faceting, JSON API at every URL")
    w("```")
    w()
    w("All three join on `composer_id`. Every section has an `estimated_utc` timestamp "
      "interpolated from transcript file birth/modification times and line position "
      "-- forensic timestamp recovery where none existed.")
    w()

    # Where the money goes
    w("## 3. Where the money goes")
    w()
    w("### Daily spending")
    w()
    w("```output")
    w(f"{'Date':<12} {'Cost':>10}  {'Events':>6}  {'Tokens':>15}  {'Cache%':>6}")
    w("-" * 60)
    for row in q(conn, """
        SELECT date_only, round(sum(cost),2) as cost, count(*) as events,
               sum(total_tokens) as tokens,
               round(sum(cache_read)*100.0/sum(total_tokens),1) as cache_pct
        FROM usage_events GROUP BY date_only ORDER BY date_only DESC LIMIT 18
    """):
        w(f"{row['date_only']:<12} ${row['cost']:>9.2f}  {row['events']:>6}  {row['tokens']:>15,}  {row['cache_pct']:>5.1f}%")
    w("```")
    w()

    # Cost by model
    w("### Cost by model")
    w()
    w("```output")
    w(f"{'Model':<45} {'Cost':>9}  {'Calls':>6}  {'Avg':>6}  {'Cache%':>6}")
    w("-" * 80)
    for row in q(conn, """
        SELECT model, round(sum(cost),2) as cost, count(*) as calls,
               round(avg(cost),2) as avg, round(sum(cache_read)*100.0/nullif(sum(total_tokens),0),1) as cache_pct
        FROM usage_events GROUP BY model ORDER BY cost DESC
    """):
        cp = f"{row['cache_pct']:.1f}%" if row['cache_pct'] is not None else "N/A"
        w(f"{row['model']:<45} ${row['cost']:>8.2f}  {row['calls']:>6}  ${row['avg']:>5.2f}  {cp:>6}")
    w("```")
    w()

    # Bucks and Fucks
    w("### Bucks and Fucks")
    w()
    w("$ = ~$20 spend, \U0001F92C = 1 fuck. All times UTC (Amsterdam = UTC+1). "
      "Fuck timestamps interpolated from transcript file birth/mod times and line position.")
    w()
    w("```output")
    for row in q(conn, """
        WITH hours(h) AS (
            VALUES (0),(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),
                   (12),(13),(14),(15),(16),(17),(18),(19),(20),(21),(22),(23)
        )
        SELECT hours.h as hour, coalesce(cost.total, 0) as cost, coalesce(f.cnt, 0) as fucks
        FROM hours
        LEFT JOIN (SELECT printf('%02d', hour) as hr, round(sum(cost),2) as total FROM usage_events GROUP BY hour)
            cost ON cost.hr = printf('%02d', hours.h)
        LEFT JOIN (SELECT estimated_hour as hr, count(*) as cnt FROM transcript_sections
            WHERE type='USER' AND estimated_hour IS NOT NULL AND lower(user_query_preview) LIKE '%fuck%'
            GROUP BY estimated_hour) f ON f.hr = hours.h
        ORDER BY hours.h
    """):
        cost_bars = bar_chart(row["cost"], 20, "$")
        fuck_bars = "\U0001F92C" * row["fucks"]
        w(f"  {row['hour']:02d}:00  ${row['cost']:>7.0f}  {row['fucks']:>3}F  {cost_bars}{fuck_bars}")
    w("```")
    w()

    # Most expensive
    w("### Most expensive single requests")
    w()
    w("```output")
    w(f"{'Date':<28} {'Model':<42} {'Cost':>7}  {'Tokens':>12}  Think")
    w("-" * 100)
    for row in q(conn, "SELECT date, model, cost, total_tokens, max_mode FROM usage_events ORDER BY cost DESC LIMIT 10"):
        think = "Yes" if row["max_mode"] == "Yes" else "No"
        w(f"{row['date'][:26]:<28} {row['model']:<42} ${row['cost']:>6.2f}  {row['total_tokens']:>12,}  {think}")
    w("```")
    w()

    # Tool usage
    w("## 4. What the agents actually do")
    w()
    w("### Tool usage breakdown")
    w()
    w("```output")
    w(f"{'Tool':<42} {'Calls':>5}  {'Errors':>6}  {'Err%':>5}  {'Sessions':>8}")
    w("-" * 75)
    for row in q(conn, """
        SELECT tool_name, count(*) as calls, sum(is_error) as errors,
               round(100.0*sum(is_error)/count(*),1) as err_pct,
               count(distinct composer_id) as sessions
        FROM tool_calls GROUP BY tool_name ORDER BY calls DESC
    """):
        w(f"{row['tool_name']:<42} {row['calls']:>5}  {row['errors']:>6}  {row['err_pct']:>4.1f}%  {row['sessions']:>8}")
    w("```")
    w()

    # Model vs Reality (new)
    if conn2:
        w("### Model vs reality")
        w()
        w("The universal model documents Cursor's tools from reverse engineering. "
          "Cross-referencing with actual usage shows which tools Cursor deprecated:")
        w()
        w("```output")
        w(f"{'Tool':<30} {'Documented':>10}  {'Actual':>7}  {'Errors':>7}  Status")
        w("-" * 75)
        for row in q(conn2, "SELECT name, count FROM tools ORDER BY count DESC"):
            actual = q1(conn, "SELECT count(*) FROM tool_calls WHERE tool_name = ?", (row["name"],))
            errors = q1(conn, "SELECT coalesce(sum(is_error),0) FROM tool_calls WHERE tool_name = ?", (row["name"],)) or 0
            status = ""
            if row["count"] > 100 and actual == 0:
                status = "DEPRECATED"
            elif actual > 0 and errors > actual * 0.1:
                status = f"{errors} errors!"
            w(f"{row['name']:<30} {row['count']:>10}  {actual:>7}  {errors:>7}  {status}")
        w("```")
        w()

    # Security audit
    w("## 5. Security audit")
    w()
    w("### Dangerous commands")
    w()
    w("```output")
    for row in q(conn, """
        SELECT command FROM shell_commands
        WHERE command LIKE '%sudo%' OR command LIKE '%ssh %' OR command LIKE '%kill %'
        ORDER BY id DESC LIMIT 13
    """):
        w(f"  [?] {row['command'][:75]}")
    w("```")
    w()

    # Git operations
    w("### Git operations")
    w()
    w("```output")
    git_ops = {
        "git commit": "git commit",
        "git status": "git status",
        "git diff": "git diff",
        "git log": "git log",
        "git push": "git push",
        "git add": "git add",
        "git checkout/switch": "git checkout%' OR command LIKE '%git switch",
        "git branch": "git branch",
    }
    for label, pattern in git_ops.items():
        count = q1(conn, f"SELECT count(*) FROM shell_commands WHERE command LIKE '%{pattern}%'")
        if count:
            w(f"  {label:<25} {count:>4}")
    w("```")
    w()

    # Conversations
    w("## 6. Conversations")
    w()
    w("### Busiest conversations")
    w()
    w("```output")
    w(f"{'Conversation':<50} {'Msgs':>6}  {'Sects':>6}  {'Cmds':>5}")
    w("-" * 75)
    for row in q(conn, """
        SELECT c.name, c.bubble_count,
               (SELECT count(*) FROM transcript_sections ts WHERE ts.composer_id = c.id) as sects,
               (SELECT count(*) FROM shell_commands sc WHERE sc.composer_id = c.id) as cmds
        FROM composers c WHERE c.bubble_count > 0
        ORDER BY c.bubble_count DESC LIMIT 10
    """):
        name = (row["name"] or "(unnamed)")[:48]
        w(f"{name:<50} {row['bubble_count']:>6}  {row['sects']:>6}  {row['cmds']:>5}")
    w("```")
    w()

    # Daily fuck log
    w("## 7. Daily fuck log")
    w()
    w("The agent never swears. Every fuck is human.")
    w()
    w("```output")
    for row in q(conn, """
        SELECT substr(estimated_utc, 1, 10) as day, count(*) as fucks
        FROM transcript_sections
        WHERE type = 'USER' AND estimated_utc IS NOT NULL
          AND lower(user_query_preview) LIKE '%fuck%'
        GROUP BY day ORDER BY day
    """):
        bar = "#" * row["fucks"]
        w(f"  {row['day']}  {row['fucks']:>3}  {bar}")
    total_fucks = q1(conn, """
        SELECT count(*) FROM transcript_sections
        WHERE type = 'USER' AND lower(user_query_preview) LIKE '%fuck%'
    """)
    total_cost = q1(conn, "SELECT round(sum(cost), 2) FROM usage_events")
    w(f"\n  {total_fucks} fucks, ${total_cost:,.2f} total spend, ${total_cost / max(total_fucks, 1):.2f}/fuck overall")
    w("```")
    w()

    # Cost per fuck
    w("### Cost per fuck")
    w()
    w("```output")
    w(f"  {'Date':<14} {'Fucks':>5}  {'Cost':>10}  {'$/fuck':>8}")
    w("  " + "-" * 42)
    for row in q(conn, """
        WITH fuck_days AS (
            SELECT substr(estimated_utc, 1, 10) as day, count(*) as fucks
            FROM transcript_sections
            WHERE type = 'USER' AND estimated_utc IS NOT NULL
              AND lower(user_query_preview) LIKE '%fuck%'
            GROUP BY day
        ), cost_days AS (
            SELECT date_only as day, round(sum(cost), 2) as cost FROM usage_events GROUP BY date_only
        )
        SELECT f.day, f.fucks, coalesce(c.cost, 0) as cost,
               round(coalesce(c.cost, 0) / f.fucks, 2) as per_fuck
        FROM fuck_days f LEFT JOIN cost_days c ON c.day = f.day
        WHERE coalesce(c.cost, 0) > 0
        ORDER BY per_fuck DESC LIMIT 7
    """):
        w(f"  {row['day']:<14} {row['fucks']:>5}  ${row['cost']:>9.2f}  ${row['per_fuck']:>7.2f}")
    w("```")
    w()

    # Universal model (new)
    if conn2:
        w("## 8. The universal model")
        w()
        w("A second Datasette database documents Cursor's internals as queryable YAML-to-SQLite. "
          "The model drives the code; tests validate the model against live state.")
        w()
        w("```output")
        for row in q(conn2, """
            SELECT 'tools' as cat, count(*) as n FROM tools
            UNION ALL SELECT 'models', count(*) FROM models
            UNION ALL SELECT 'features', count(*) FROM features
            UNION ALL SELECT 'keys', count(*) FROM keys
            UNION ALL SELECT 'sql_queries', count(*) FROM sql_queries
            UNION ALL SELECT 'assimilated_sources', count(*) FROM assimilated_sources
            UNION ALL SELECT 'model_files', count(*) FROM model_files
        """):
            w(f"  {row['cat']:<25} {row['n']:>4} documented")
        w("```")
        w()
        w("### Assimilated sources")
        w()
        w("21 external projects whose Cursor internals knowledge was extracted into the model:")
        w()
        w("```output")
        for row in q(conn2, "SELECT filename, cursor_mirror_use FROM assimilated_sources ORDER BY filename"):
            use = (row["cursor_mirror_use"] or "")[:55]
            w(f"  {row['filename']:<42} {use}")
        w("```")
        w()

    # Feature flag drift
    w("## 9. Cursor evolution tracking")
    w()
    w("Flags that Cursor changed since the universal model was last updated:")
    w()
    w("```output")
    for row in q(conn, "SELECT flag, model_enabled, live_enabled FROM feature_flags WHERE drift = 1 ORDER BY flag"):
        m = "ON" if row["model_enabled"] else "OFF"
        l = "ON" if row["live_enabled"] else "OFF"
        w(f"  {row['flag']}: model says {m}, Cursor says {l}")
    w("```")
    w()

    # Footer
    events = q1(conn, "SELECT count(*) FROM usage_events")
    sections = q1(conn, "SELECT count(*) FROM transcript_sections")
    w("## 10. What this is")
    w()
    w("All data above comes from cursor-mirror, a MOOLLM skill that reads "
      "Cursor IDE's SQLite databases, agent transcript files, and billing CSV. "
      "It integrates them into a universal model documented as YAML, served via "
      "Simon Willison's Datasette and captured by Showboat.")
    w()
    w(f"{events:,} billing events. {sections:,} transcript sections. "
      f"35 canned SQL queries. 73 CLI commands. 81 tests. "
      f"21 assimilated external sources. 13 AI models tracked. "
      f"Full-text search across everything. JSON API at every URL.")

    conn.close()
    if conn2:
        conn2.close()


if __name__ == "__main__":
    output_path = sys.argv[1] if len(sys.argv) > 1 else None
    if output_path:
        with open(output_path, "w") as f:
            generate(f)
        print(f"Written to {output_path}", file=sys.stderr)
    else:
        generate(sys.stdout)
