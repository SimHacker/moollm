# Named SQL query runner. Loads queries from model/sql/INDEX.yml,
# resolves parameters, executes against the right database.
# Composable: chain queries by feeding output params into the next.

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .db import open_db, decode_blob
from .debug_util import debug
from .paths import GLOBAL_DB, WORKSPACES_ROOT
from .resolve import resolve_workspace

_MODEL_SQL_DIR = Path(__file__).resolve().parent.parent / "reference" / "universal" / "model" / "sql"


@dataclass
class QueryDef:
    """A named query definition from INDEX.yml."""
    id: str
    file: str
    db: str
    table: str
    description: str
    params: dict[str, dict[str, Any]] = field(default_factory=dict)
    returns: str = ""
    multi_statement: bool = False
    chain_hint: str = ""

    @property
    def sql(self) -> str:
        path = _MODEL_SQL_DIR / self.file
        return path.read_text().strip() if path.exists() else ""

    @property
    def required_params(self) -> list[str]:
        return [k for k, v in self.params.items() if v.get("required", False)]

    @property
    def param_defaults(self) -> dict[str, Any]:
        return {k: v["default"] for k, v in self.params.items() if "default" in v}

    def summary(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "db": self.db,
            "description": self.description,
            "params": {k: v.get("description", "") for k, v in self.params.items()},
            "chain_hint": self.chain_hint,
        }


def load_query_index() -> dict[str, QueryDef]:
    """Load all named queries from INDEX.yml."""
    index_path = _MODEL_SQL_DIR / "INDEX.yml"
    if not index_path.exists():
        return {}
    data = yaml.safe_load(index_path.read_text()) or {}
    queries = {}
    for qid, qdef in data.get("queries", {}).items():
        queries[qid] = QueryDef(
            id=qid,
            file=qdef.get("file", ""),
            db=qdef.get("db", "global"),
            table=qdef.get("table", ""),
            description=qdef.get("description", ""),
            params=qdef.get("params", {}),
            returns=qdef.get("returns", ""),
            multi_statement=qdef.get("multi_statement", False),
            chain_hint=qdef.get("chain_hint", ""),
        )
    return queries


def resolve_db_path(db_target: str, workspace_ref: str | None = None) -> Path:
    """Resolve 'global', 'workspace', or 'either' to an actual DB path."""
    if db_target == "global":
        return GLOBAL_DB
    if db_target == "workspace" and workspace_ref:
        ws = resolve_workspace(workspace_ref)
        if ws:
            return ws / "state.vscdb"
    if db_target == "either" and workspace_ref:
        ws = resolve_workspace(workspace_ref)
        if ws:
            return ws / "state.vscdb"
    return GLOBAL_DB


@dataclass
class QueryResult:
    """Result from executing a named query."""
    query_id: str
    columns: list[str]
    rows: list[dict[str, Any]]
    row_count: int
    sql_executed: str
    params_used: dict[str, Any]

    def first(self) -> dict[str, Any] | None:
        return self.rows[0] if self.rows else None

    def values(self, column: str) -> list[Any]:
        """Extract a single column as a flat list -- useful for chaining."""
        return [row[column] for row in self.rows if column in row]


def run_query(
    query_id: str,
    workspace: str | None = None,
    **params: Any,
) -> QueryResult:
    """Execute a named query by ID with parameter binding.

    Usage:
        result = run_query("full_session", composer_id="3856dad8-...")
        result = run_query("search_keys_prefix", prefix="bubbleId:3856dad8:%", limit=10)
        result = run_query("list_sessions_workspace", workspace="moollm")

    Chain:
        composers = run_query("list_composers_global")
        for row in composers.rows:
            cid = row["key"].replace("composerData:", "")
            session = run_query("full_session", composer_id=cid)
    """
    index = load_query_index()
    if query_id not in index:
        raise KeyError(f"Unknown query: {query_id}. Available: {', '.join(sorted(index.keys()))}")

    qdef = index[query_id]

    # Check required params
    for p in qdef.required_params:
        if p not in params:
            raise ValueError(f"Query '{query_id}' requires parameter '{p}' ({qdef.params[p].get('description', '')})")

    # Apply defaults
    bound = dict(qdef.param_defaults)
    bound.update(params)

    # Resolve database
    db_path = resolve_db_path(qdef.db, workspace)
    debug("run_query: %s on %s with %s", query_id, db_path.name, bound)

    conn = open_db(db_path)
    conn.row_factory = sqlite3.Row

    # Get SQL text (strip comment lines for execution, keep for reference)
    raw_sql = qdef.sql
    executable_lines = [line for line in raw_sql.split("\n") if not line.strip().startswith("--")]
    sql_text = "\n".join(executable_lines).strip()

    # Handle multi-statement: execute first non-empty SELECT only
    if qdef.multi_statement:
        statements = [s.strip() for s in sql_text.split(";") if s.strip()]
        sql_text = statements[0] if statements else sql_text

    rows_raw = conn.execute(sql_text, bound).fetchall()
    columns = [desc[0] for desc in conn.execute(sql_text, bound).description] if rows_raw else []
    conn.close()

    rows = []
    for row in rows_raw:
        d = dict(row)
        # Auto-decode blob values
        for k, v in d.items():
            if isinstance(v, (bytes, bytearray)):
                d[k] = decode_blob(v)
        rows.append(d)

    return QueryResult(
        query_id=query_id,
        columns=columns,
        rows=rows,
        row_count=len(rows),
        sql_executed=sql_text,
        params_used=bound,
    )


def list_queries() -> list[dict[str, Any]]:
    """List all available named queries with summaries."""
    return [q.summary() for q in load_query_index().values()]
