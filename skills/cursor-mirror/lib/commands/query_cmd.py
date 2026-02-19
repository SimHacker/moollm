# CLI commands for the named query runner.
# query-list, query-info, query-run

from __future__ import annotations

import json
import sys
from typing import Any

from ..query_runner import run_query, list_queries, load_query_index
from ..format_util import get_output_format, output_data


def cmd_query_list(args: Any) -> None:
    """List all named queries with descriptions and parameters."""
    fmt = get_output_format(args)
    queries = list_queries()

    if fmt in ("json", "yaml"):
        output_data(queries, fmt, command="query-list", supported=["text", "json", "yaml"])
        return

    print(f"{'ID':<30s} {'DB':<10s} {'PARAMS':<30s} DESCRIPTION")
    print("-" * 100)
    for q in queries:
        params = ", ".join(f"{k}" for k in q["params"]) if q["params"] else "-"
        print(f"{q['id']:<30s} {q['db']:<10s} {params:<30s} {q['description'][:50]}")
    print(f"\n{len(queries)} queries. Run: cursor-mirror query-run <id> [--param value]")


def cmd_query_info(args: Any) -> None:
    """Show detailed info about a named query: SQL, parameters, chain hints."""
    index = load_query_index()
    qid = args.query_id

    if qid not in index:
        print(f"Unknown query: {qid}", file=sys.stderr)
        print(f"Available: {', '.join(sorted(index.keys()))}", file=sys.stderr)
        sys.exit(1)

    qdef = index[qid]
    fmt = get_output_format(args)

    info = {
        "id": qdef.id,
        "description": qdef.description,
        "db": qdef.db,
        "table": qdef.table,
        "file": qdef.file,
        "multi_statement": qdef.multi_statement,
        "returns": qdef.returns,
        "chain_hint": qdef.chain_hint,
        "params": {
            k: {
                "type": v.get("type", "str"),
                "required": v.get("required", False),
                "default": v.get("default"),
                "description": v.get("description", ""),
            }
            for k, v in qdef.params.items()
        },
        "sql": qdef.sql,
    }

    if fmt in ("json", "yaml"):
        output_data(info, fmt, command="query-info", supported=["text", "json", "yaml"])
        return

    print(f"Query: {qdef.id}")
    print(f"Description: {qdef.description}")
    print(f"Database: {qdef.db} ({qdef.table})")
    print(f"File: model/sql/{qdef.file}")
    if qdef.returns:
        print(f"Returns: {qdef.returns}")
    if qdef.chain_hint:
        print(f"Chain: {qdef.chain_hint}")

    if qdef.params:
        print(f"\nParameters:")
        for k, v in qdef.params.items():
            req = "REQUIRED" if v.get("required") else f"default={v.get('default', 'none')}"
            print(f"  :{k} ({v.get('type', 'str')}) -- {v.get('description', '')} [{req}]")
    else:
        print(f"\nNo parameters.")

    print(f"\nSQL:")
    print(qdef.sql)


def cmd_query_run(args: Any) -> None:
    """Execute a named query with parameters and display results."""
    qid = args.query_id
    fmt = get_output_format(args, default="text")

    # Parse --param key=value pairs into dict
    params: dict[str, Any] = {}
    if args.param:
        for p in args.param:
            if "=" not in p:
                print(f"Invalid param format: {p} (expected key=value)", file=sys.stderr)
                sys.exit(1)
            k, v = p.split("=", 1)
            # Auto-convert integers
            try:
                v = int(v)
            except ValueError:
                pass
            params[k] = v

    try:
        result = run_query(qid, workspace=args.workspace, **params)
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        # Show query info to help
        index = load_query_index()
        if qid in index:
            qdef = index[qid]
            print(f"\nRequired params for '{qid}':", file=sys.stderr)
            for k, v in qdef.params.items():
                if v.get("required"):
                    print(f"  --param {k}=<{v.get('type', 'str')}>  {v.get('description', '')}", file=sys.stderr)
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

    # Text table output
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
