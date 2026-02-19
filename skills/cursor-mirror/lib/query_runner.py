# Named SQL query runner. Two layers:
#   1. Low-level: model/sql/*.sql queries against Cursor's raw state.vscdb
#      (loaded by lib/sql.py, used internally by lib modules)
#   2. High-level: datasette-metadata.yml canned queries against exported .db files
#      (used by CLI query-list/query-info/query-run and by Datasette web UI)
#
# This module handles layer 2. Layer 1 stays in lib/sql.py.

from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .db import open_db, decode_blob
from .debug_util import debug

_METADATA_PATH = Path(__file__).resolve().parent.parent / "reference" / "universal" / "datasette-metadata.yml"


@dataclass
class CannedQuery:
    """A canned query from datasette-metadata.yml."""
    id: str
    database: str
    title: str
    description: str
    sql: str
    params: list[str] = field(default_factory=list)

    def summary(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "database": self.database,
            "title": self.title,
            "description": self.description,
            "params": self.params,
        }


def _extract_params(sql: str) -> list[str]:
    """Extract :named_params from SQL text."""
    return sorted(set(re.findall(r':(\w+)', sql)))


def load_canned_queries() -> dict[str, CannedQuery]:
    """Load all canned queries from datasette-metadata.yml."""
    if not _METADATA_PATH.exists():
        return {}
    data = yaml.safe_load(_METADATA_PATH.read_text()) or {}
    queries: dict[str, CannedQuery] = {}
    for db_name, db_config in data.get("databases", {}).items():
        for qid, qdef in db_config.get("queries", {}).items():
            sql = qdef.get("sql", "")
            queries[qid] = CannedQuery(
                id=qid,
                database=db_name,
                title=qdef.get("title", qid),
                description=qdef.get("description", ""),
                sql=sql.strip(),
                params=_extract_params(sql),
            )
    return queries


@dataclass
class QueryResult:
    """Result from executing a canned query."""
    query_id: str
    columns: list[str]
    rows: list[dict[str, Any]]
    row_count: int
    sql_executed: str
    params_used: dict[str, Any]

    def first(self) -> dict[str, Any] | None:
        return self.rows[0] if self.rows else None

    def values(self, column: str) -> list[Any]:
        """Extract a single column as a flat list."""
        return [row[column] for row in self.rows if column in row]


def run_query(
    query_id: str,
    db_path: Path | None = None,
    **params: Any,
) -> QueryResult:
    """Execute a canned query by ID with parameter binding.

    If db_path is not given, looks for {database}.db in the cursor-mirror skill dir.

    Usage:
        result = run_query("tool-usage")
        result = run_query("shell-commands-search", pattern="docker", limit=10)
        result = run_query("thinking-search", search="security")
    """
    all_queries = load_canned_queries()
    if query_id not in all_queries:
        raise KeyError(f"Unknown query: {query_id}. Available: {', '.join(sorted(all_queries.keys()))}")

    qdef = all_queries[query_id]

    # Check required params
    for p in qdef.params:
        if p not in params:
            raise ValueError(
                f"Query '{query_id}' requires parameter ':{p}'. "
                f"Pass --param {p}=<value>"
            )

    # Resolve database path
    if db_path is None:
        skill_dir = Path(__file__).resolve().parent.parent
        db_path = skill_dir / f"{qdef.database}.db"
        if not db_path.exists():
            raise FileNotFoundError(
                f"Database not found: {db_path}\n"
                f"Run the export first: from lib.datasette_export import export_datasette"
            )

    debug("run_query: %s on %s with %s", query_id, db_path.name, params)

    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    rows_raw = conn.execute(qdef.sql, params).fetchall()
    columns = list(rows_raw[0].keys()) if rows_raw else []
    conn.close()

    rows = [dict(row) for row in rows_raw]

    return QueryResult(
        query_id=query_id,
        columns=columns,
        rows=rows,
        row_count=len(rows),
        sql_executed=qdef.sql,
        params_used=params,
    )


def list_queries() -> list[dict[str, Any]]:
    """List all available canned queries with summaries."""
    return [q.summary() for q in load_canned_queries().values()]
