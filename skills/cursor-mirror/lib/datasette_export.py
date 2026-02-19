# Export cursor-mirror data to a consolidated SQLite database for Datasette.
# Produces a single .db file with sections, shell_commands, tool_calls,
# composers, feature_flags -- all queryable via Datasette's web UI and JSON API.
#
# Usage: from lib.datasette_export import export_datasette
#        export_datasette(Path("cursor-mirror.db"))
# Then:  datasette cursor-mirror.db

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

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
CREATE INDEX IF NOT EXISTS idx_tool_calls_name ON tool_calls(tool_name);
CREATE INDEX IF NOT EXISTS idx_tool_calls_composer ON tool_calls(composer_id);
"""


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
