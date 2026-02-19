# Export cursor-mirror data to a consolidated SQLite database for Datasette.
# Produces a single .db file with sections, shell_commands, tool_calls,
# composers, feature_flags -- all queryable via Datasette's web UI and JSON API.
#
# Usage: from lib.datasette_export import export_datasette
#        export_datasette(Path("cursor-mirror.db"))
# Then:  datasette cursor-mirror.db

from __future__ import annotations

import csv
import json
import sqlite3
from pathlib import Path
from typing import Any

import yaml

from .composers import get_all_composers, get_bubble_counts
from .bubbles import iter_bubbles
from .feature_monitor import diff_features, get_live_feature_flags, load_model_features
from .transcript import find_all_transcripts, parse_transcript, extract_shell_commands
from .transcript_index import update_index, index_path_for

_SCHEMA = """
CREATE TABLE IF NOT EXISTS composers (
    id TEXT PRIMARY KEY,
    name TEXT,
    workspace TEXT,
    workspace_folder TEXT,
    bubble_count INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS transcript_sections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    composer_id TEXT,
    workspace TEXT,
    transcript_file TEXT,
    type TEXT,
    start_line INTEGER,
    end_line INTEGER,
    line_count INTEGER,
    tool_name TEXT,
    user_query_preview TEXT,
    text_preview TEXT
);

CREATE TABLE IF NOT EXISTS shell_commands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    composer_id TEXT,
    workspace TEXT,
    command TEXT,
    line INTEGER,
    tool_name TEXT
);

CREATE TABLE IF NOT EXISTS tool_calls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    composer_id TEXT,
    tool_name TEXT,
    params_preview TEXT,
    is_error BOOLEAN,
    bubble_type INTEGER,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS feature_flags (
    flag TEXT PRIMARY KEY,
    model_enabled BOOLEAN,
    live_enabled BOOLEAN,
    drift BOOLEAN
);

CREATE INDEX IF NOT EXISTS idx_sections_composer ON transcript_sections(composer_id);
CREATE INDEX IF NOT EXISTS idx_sections_type ON transcript_sections(type);
CREATE INDEX IF NOT EXISTS idx_shell_composer ON shell_commands(composer_id);
CREATE TABLE IF NOT EXISTS usage_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    kind TEXT,
    model TEXT,
    max_mode TEXT,
    input_with_cache INTEGER,
    input_without_cache INTEGER,
    cache_read INTEGER,
    output_tokens INTEGER,
    total_tokens INTEGER,
    cost REAL,
    date_only TEXT,
    hour TEXT
);

CREATE INDEX IF NOT EXISTS idx_tool_calls_name ON tool_calls(tool_name);
CREATE INDEX IF NOT EXISTS idx_tool_calls_composer ON tool_calls(composer_id);
CREATE INDEX IF NOT EXISTS idx_usage_date ON usage_events(date);
CREATE INDEX IF NOT EXISTS idx_usage_model ON usage_events(model);
CREATE INDEX IF NOT EXISTS idx_usage_cost ON usage_events(cost);
"""

_USAGE_CSV_DIR = Path(__file__).resolve().parent.parent.parent.parent / ".moollm" / "usage"


def export_datasette(
    output: Path,
    max_transcripts: int = 100,
    max_tool_bubbles: int = 5000,
) -> dict[str, Any]:
    """Export cursor-mirror data to a consolidated Datasette-ready SQLite DB.

    Returns stats dict with counts of exported items.
    """
    if output.exists():
        output.unlink()

    conn = sqlite3.connect(str(output))
    conn.executescript(_SCHEMA)

    stats: dict[str, int] = {}

    # Composers
    all_composers = get_all_composers()
    for cid, meta in all_composers.items():
        conn.execute(
            "INSERT OR IGNORE INTO composers VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                cid,
                meta.get("name"),
                meta.get("_workspace"),
                meta.get("_workspace_folder"),
                meta.get("_bubble_count", 0),
                meta.get("createdAt"),
                meta.get("lastUpdatedAt"),
            ),
        )
    stats["composers"] = len(all_composers)

    # Transcripts -> sections + shell_commands
    transcripts = find_all_transcripts()[:max_transcripts]
    section_count = 0
    cmd_count = 0

    for t_path in transcripts:
        composer_id = t_path.stem
        workspace = t_path.parent.parent.name

        sections, _state = parse_transcript(t_path)
        for s in sections:
            conn.execute(
                "INSERT INTO transcript_sections "
                "(composer_id, workspace, transcript_file, type, start_line, end_line, "
                "line_count, tool_name, user_query_preview, text_preview) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    composer_id, workspace, str(t_path), s.type.name,
                    s.start_line, s.end_line, s.line_count,
                    s.tool_name or None,
                    s.user_query[:200] if s.user_query else None,
                    s.text.strip()[:200] if s.text else None,
                ),
            )
            section_count += 1

        cmds = extract_shell_commands(sections)
        for cmd in cmds:
            conn.execute(
                "INSERT INTO shell_commands (composer_id, workspace, command, line, tool_name) "
                "VALUES (?, ?, ?, ?, ?)",
                (composer_id, workspace, cmd["command"], cmd["line"], cmd["tool_name"]),
            )
            cmd_count += 1

    stats["transcripts"] = len(transcripts)
    stats["sections"] = section_count
    stats["shell_commands"] = cmd_count

    # Tool calls from bubbles
    tool_count = 0
    for cid, _key, obj in iter_bubbles():
        tfd = obj.get("toolFormerData")
        if not tfd:
            continue
        tool_name = tfd.get("name") or tfd.get("toolName") or ""
        if not tool_name:
            continue
        params = tfd.get("params") or tfd.get("rawArgs") or {}
        params_str = json.dumps(params, ensure_ascii=False)[:300] if isinstance(params, dict) else str(params)[:300]
        is_error = False
        ad = tfd.get("additionalData")
        if isinstance(ad, dict) and ad.get("status") == "error":
            is_error = True
        conn.execute(
            "INSERT INTO tool_calls (composer_id, tool_name, params_preview, is_error, bubble_type, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (cid, tool_name, params_str, is_error, obj.get("type"), obj.get("createdAt")),
        )
        tool_count += 1
        if tool_count >= max_tool_bubbles:
            break
    stats["tool_calls"] = tool_count

    # Feature flags
    model = load_model_features()
    model_enabled = set(model.get("feature_flags", {}).get("enabled", []))
    model_disabled = set(model.get("feature_flags", {}).get("disabled", []))
    live_flags = get_live_feature_flags()

    all_flags = model_enabled | model_disabled | set(live_flags.keys())
    for flag in sorted(all_flags):
        m_val = flag in model_enabled
        l_val = live_flags.get(flag, False)
        conn.execute(
            "INSERT OR IGNORE INTO feature_flags VALUES (?, ?, ?, ?)",
            (flag, m_val, l_val, m_val != l_val),
        )
    stats["feature_flags"] = len(all_flags)

    # Usage events from billing CSV
    usage_count = 0
    if _USAGE_CSV_DIR.exists():
        for csv_path in sorted(_USAGE_CSV_DIR.glob("usage-events-*.csv")):
            with open(csv_path, newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    date_str = row.get("Date", "")
                    cost_str = row.get("Cost", "0")
                    try:
                        cost = float(cost_str)
                    except (ValueError, TypeError):
                        cost = 0.0
                    total_tokens_str = row.get("Total Tokens", "0")
                    try:
                        total_tokens = int(total_tokens_str)
                    except (ValueError, TypeError):
                        total_tokens = 0
                    date_only = date_str[:10] if len(date_str) >= 10 else ""
                    hour = date_str[11:13] if len(date_str) >= 13 else ""
                    conn.execute(
                        "INSERT INTO usage_events "
                        "(date, kind, model, max_mode, input_with_cache, input_without_cache, "
                        "cache_read, output_tokens, total_tokens, cost, date_only, hour) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            date_str,
                            row.get("Kind", ""),
                            row.get("Model", ""),
                            row.get("Max Mode", ""),
                            int(row.get("Input (w/ Cache Write)", 0) or 0),
                            int(row.get("Input (w/o Cache Write)", 0) or 0),
                            int(row.get("Cache Read", 0) or 0),
                            int(row.get("Output Tokens", 0) or 0),
                            total_tokens,
                            cost,
                            date_only,
                            hour,
                        ),
                    )
                    usage_count += 1
    stats["usage_events"] = usage_count

    conn.commit()

    # Enable FTS on text previews for Datasette search
    try:
        conn.executescript("""
            CREATE VIRTUAL TABLE IF NOT EXISTS transcript_sections_fts
            USING fts5(user_query_preview, text_preview, content=transcript_sections, content_rowid=id);
            INSERT INTO transcript_sections_fts(transcript_sections_fts) VALUES('rebuild');
        """)
        conn.commit()
    except Exception:
        pass

    conn.close()
    stats["output"] = str(output)
    stats["size_kb"] = int(output.stat().st_size / 1024)
    return stats


def export_model_to_sqlite(output: Path) -> dict[str, Any]:
    """Export the universal model YAML + assimilated sources to a Datasette-ready SQLite DB.

    Produces tables: model_files, keys, tools, models, features, sql_queries,
    services, assimilated_sources. Full-text search on model file content.
    """
    model_dir = Path(__file__).resolve().parent.parent / "reference" / "universal" / "model"
    assim_dir = Path(__file__).resolve().parent.parent / "reference" / "assimilated"

    if output.exists():
        output.unlink()

    conn = sqlite3.connect(str(output))

    conn.executescript("""
    CREATE TABLE model_files (
        path TEXT PRIMARY KEY, name TEXT, category TEXT,
        content_yaml TEXT, content_json TEXT, line_count INTEGER);
    CREATE TABLE keys (
        name TEXT PRIMARY KEY, table_name TEXT, location TEXT,
        description TEXT, source_file TEXT);
    CREATE TABLE tools (
        name TEXT PRIMARY KEY, category TEXT, count INTEGER,
        params TEXT, has_explanation BOOLEAN, note TEXT);
    CREATE TABLE models (
        name TEXT PRIMARY KEY, provider TEXT, tier TEXT,
        usage TEXT, deprecated BOOLEAN, migrated_to TEXT);
    CREATE TABLE features (
        name TEXT PRIMARY KEY, section TEXT, value TEXT, type TEXT);
    CREATE TABLE sql_queries (
        name TEXT PRIMARY KEY, filename TEXT, sql_text TEXT, line_count INTEGER);
    CREATE TABLE services (
        name TEXT PRIMARY KEY, category TEXT, purpose TEXT);
    CREATE TABLE assimilated_sources (
        filename TEXT PRIMARY KEY, source_url TEXT,
        assimilated_date TEXT, cursor_mirror_use TEXT);
    """)

    stats: dict[str, int] = {}

    # model_files
    count = 0
    for yml in sorted(model_dir.rglob("*.yml")):
        rel = str(yml.relative_to(model_dir))
        text = yml.read_text()
        data = yaml.safe_load(text)
        cat = yml.parent.name if yml.parent != model_dir else "root"
        conn.execute("INSERT INTO model_files VALUES (?,?,?,?,?,?)",
            (rel, yml.stem, cat, text, json.dumps(data, default=str, ensure_ascii=False), text.count('\n')))
        count += 1
    stats["model_files"] = count

    # keys
    count = 0
    for key_file in sorted((model_dir / "keys").glob("*.yml")):
        data = yaml.safe_load(key_file.read_text()) or {}
        if "session_list_priority" in data:
            for k in data["session_list_priority"].get("keys", []):
                conn.execute("INSERT OR IGNORE INTO keys VALUES (?,?,?,?,?)",
                    (k, "ItemTable", "workspace", "Session list key", key_file.name))
                count += 1
        if "entries" in data:
            for name, info in data["entries"].items():
                pattern = info.get("pattern", "") if isinstance(info, dict) else ""
                conn.execute("INSERT OR IGNORE INTO keys VALUES (?,?,?,?,?)",
                    (name, "cursorDiskKV", "global", pattern, key_file.name))
                count += 1
    stats["keys"] = count

    # tools
    count = 0
    tools_data = yaml.safe_load((model_dir / "tools.yml").read_text()) or {}
    for cat in ["file_operations", "search", "execution", "validation", "meta"]:
        for name, info in tools_data.get(cat, {}).items():
            if not isinstance(info, dict):
                continue
            conn.execute("INSERT OR IGNORE INTO tools VALUES (?,?,?,?,?,?)",
                (name, cat, info.get("count", 0),
                 json.dumps(info.get("params", [])), info.get("has_explanation", False),
                 info.get("note", "")))
            count += 1
    stats["tools"] = count

    # models
    count = 0
    models_data = yaml.safe_load((model_dir / "models.yml").read_text()) or {}
    for provider in ["claude", "gpt", "grok", "auto"]:
        for name, info in models_data.get(provider, {}).items():
            if not isinstance(info, dict):
                continue
            conn.execute("INSERT OR IGNORE INTO models VALUES (?,?,?,?,?,?)",
                (name, provider, info.get("tier", ""), info.get("usage", ""),
                 info.get("deprecated", False), info.get("migrated_to", "")))
            count += 1
    stats["models"] = count

    # features
    count = 0
    feat_data = yaml.safe_load((model_dir / "features.yml").read_text()) or {}
    for section_name in ["feature_config", "feature_flags", "server_config"]:
        section = feat_data.get(section_name, {})
        for k, v in section.items():
            if k == "location":
                continue
            if isinstance(v, dict):
                for k2, v2 in v.items():
                    conn.execute("INSERT OR IGNORE INTO features VALUES (?,?,?,?)",
                        (k2, f"{section_name}.{k}", str(v2), type(v2).__name__))
                    count += 1
            elif isinstance(v, list):
                for item in v:
                    conn.execute("INSERT OR IGNORE INTO features VALUES (?,?,?,?)",
                        (str(item), section_name, "listed", "flag"))
                    count += 1
    stats["features"] = count

    # sql_queries
    count = 0
    sql_dir = model_dir / "sql"
    if sql_dir.exists():
        for sql_file in sorted(sql_dir.glob("*.sql")):
            text = sql_file.read_text()
            conn.execute("INSERT INTO sql_queries VALUES (?,?,?,?)",
                (sql_file.stem, sql_file.name, text, text.count('\n')))
            count += 1
    stats["sql_queries"] = count

    # services
    count = 0
    svc_data = yaml.safe_load((model_dir / "services.yml").read_text()) or {}
    for cat, info in svc_data.items():
        if isinstance(info, dict):
            for name, detail in info.items():
                conn.execute("INSERT OR IGNORE INTO services VALUES (?,?,?)",
                    (str(name), cat, str(detail) if not isinstance(detail, dict) else json.dumps(detail)))
                count += 1
        elif isinstance(info, str):
            conn.execute("INSERT OR IGNORE INTO services VALUES (?,?,?)", (info, cat, ""))
            count += 1
    stats["services"] = count

    # assimilated_sources
    count = 0
    if assim_dir.exists():
        for yml in sorted(assim_dir.glob("*.yml")):
            data = yaml.safe_load(yml.read_text()) or {}
            meta = data.get("meta", {})
            conn.execute("INSERT OR IGNORE INTO assimilated_sources VALUES (?,?,?,?)",
                (yml.name, meta.get("source", ""), meta.get("assimilated", ""), meta.get("cursor_mirror_use", "")))
            count += 1
    stats["assimilated_sources"] = count

    # FTS
    try:
        conn.executescript("""
        CREATE VIRTUAL TABLE IF NOT EXISTS model_files_fts
        USING fts5(path, name, content_yaml, content=model_files, content_rowid=rowid);
        INSERT INTO model_files_fts(model_files_fts) VALUES('rebuild');
        """)
    except Exception:
        pass

    conn.commit()
    conn.close()
    stats["output"] = str(output)
    stats["size_kb"] = int(output.stat().st_size / 1024)
    return stats
