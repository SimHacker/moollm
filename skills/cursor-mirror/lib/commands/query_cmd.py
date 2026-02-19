# CLI commands for the canned query runner.
# query-list, query-info, query-run
# Reads queries from reference/universal/datasette-metadata.yml (single source of truth).

from __future__ import annotations

import json
import sys
from typing import Any

from ..query_runner import run_query, list_queries, load_canned_queries
from ..format_util import get_output_format, output_data


def cmd_query_list(args: Any) -> None:
    """List all canned queries with descriptions and parameters."""
    fmt = get_output_format(args)
    queries = list_queries()

    if fmt in ("json", "yaml"):
        output_data(queries, fmt, command="query-list", supported=["text", "json", "yaml"])
        return

    print(f"{'ID':<30s} {'DB':<16s} {'PARAMS':<20s} TITLE")
    print("-" * 100)
    for q in queries:
        params = ", ".join(q["params"]) if q["params"] else "-"
        print(f"{q['id']:<30s} {q['database']:<16s} {params:<20s} {q['title'][:40]}")
    print(f"\n{len(queries)} queries. Run: cursor-mirror query-run <id> [--param key=value]")


def cmd_query_info(args: Any) -> None:
    """Show detailed info about a canned query: SQL, parameters."""
    all_queries = load_canned_queries()
    qid = args.query_id

    if qid not in all_queries:
        print(f"Unknown query: {qid}", file=sys.stderr)
        print(f"Available: {', '.join(sorted(all_queries.keys()))}", file=sys.stderr)
        sys.exit(1)

    qdef = all_queries[qid]
    fmt = get_output_format(args)

    info = {
        "id": qdef.id,
        "title": qdef.title,
        "description": qdef.description,
        "database": qdef.database,
        "params": qdef.params,
        "sql": qdef.sql,
    }

    if fmt in ("json", "yaml"):
        output_data(info, fmt, command="query-info", supported=["text", "json", "yaml"])
        return

    print(f"Query: {qdef.id}")
    print(f"Title: {qdef.title}")
    print(f"Description: {qdef.description}")
    print(f"Database: {qdef.database}")

    if qdef.params:
        print(f"Parameters: {', '.join(':' + p for p in qdef.params)}")
    else:
        print(f"Parameters: (none)")

    print(f"\nSQL:")
    print(qdef.sql)
    print(f"\nDatasette URL: /cursor-mirror/{qdef.id}" if qdef.database == "cursor-mirror"
          else f"\nDatasette URL: /cursor-model/{qdef.id}")


def cmd_query_run(args: Any) -> None:
    """Execute a canned query with parameters and display results."""
    qid = args.query_id
    fmt = get_output_format(args, default="text")

    params: dict[str, Any] = {}
    if args.param:
        for p in args.param:
            if "=" not in p:
                print(f"Invalid param format: {p} (expected key=value)", file=sys.stderr)
                sys.exit(1)
            k, v = p.split("=", 1)
            try:
                v = int(v)
            except ValueError:
                pass
            params[k] = v

    try:
        result = run_query(qid, **params)
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if fmt in ("json", "yaml"):
        output_data(result.rows, fmt, command="query-run",
                    supported=["text", "json", "yaml", "csv", "jsonl"])
        return

    if fmt == "csv":
        output_data(result.rows, "csv", command="query-run", supported=["text", "json", "yaml", "csv"])
        return

    if fmt == "jsonl":
        for row in result.rows:
            print(json.dumps(row, default=str, ensure_ascii=False))
        return

    if not result.rows:
        print(f"(no results)")
        return

    cols = result.columns
    widths = [max(len(str(c)), max((len(str(row.get(c, ""))[:60]) for row in result.rows), default=0)) for c in cols]
    widths = [min(w, 60) for w in widths]

    header = "  ".join(str(c).ljust(w) for c, w in zip(cols, widths))
    print(header)
    print("  ".join("-" * w for w in widths))
    for row in result.rows:
        line = "  ".join(str(row.get(c, ""))[:60].ljust(w) for c, w in zip(cols, widths))
        print(line)

    print(f"\n{result.row_count} row(s)")
