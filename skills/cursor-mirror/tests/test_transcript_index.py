# Transcript SQLite index tests.

from pathlib import Path

from lib.transcript_index import (
    update_index, query_index, query_shell_commands,
    index_path_for, open_index,
)

SYNTHETIC = """\
user:
<user_query>
Deploy the thing.
</user_query>

A:
Running deploy.
[Tool call] Shell
  command: npm run deploy --production
  description: Deploy to prod

[Tool result] Shell

A:
Deployed. Now checking.
[Tool call] Shell
  command: curl https://example.com/health

[Tool result] Shell

[Thinking] Looks good, health check passed.
A:
All done.
"""


def test_create_index():
    tmp = Path("/tmp/test_idx_transcript.txt")
    tmp.write_text(SYNTHETIC)
    stats = update_index(tmp)
    db = index_path_for(tmp)
    assert db.exists()
    assert stats["is_fresh"]
    assert stats["total_sections"] > 0
    assert stats["shell_commands"] == 2
    db.unlink()
    tmp.unlink()


def test_incremental_update():
    tmp = Path("/tmp/test_idx_incr.txt")
    part1 = "user:\n<user_query>\nHi\n</user_query>\n\nA:\nHello.\n"
    part2 = "[Tool call] Shell\n  command: ls\n\n[Tool result] Shell\n\nA:\nDone.\n"

    tmp.write_text(part1)
    stats1 = update_index(tmp)
    assert stats1["is_fresh"]
    count1 = stats1["total_sections"]

    tmp.write_text(part1 + part2)
    stats2 = update_index(tmp)
    assert not stats2["is_fresh"]
    assert stats2["total_sections"] > count1
    assert stats2["shell_commands"] >= 1

    index_path_for(tmp).unlink()
    tmp.unlink()


def test_query_by_type():
    tmp = Path("/tmp/test_idx_query.txt")
    tmp.write_text(SYNTHETIC)
    update_index(tmp)
    db = index_path_for(tmp)

    tool_calls = query_index(db, section_type="TOOL_CALL")
    assert len(tool_calls) == 2
    assert all(r["type"] == "TOOL_CALL" for r in tool_calls)

    users = query_index(db, section_type="USER")
    assert len(users) == 1

    db.unlink()
    tmp.unlink()


def test_query_shell_commands():
    tmp = Path("/tmp/test_idx_shell.txt")
    tmp.write_text(SYNTHETIC)
    update_index(tmp)
    db = index_path_for(tmp)

    cmds = query_shell_commands(db)
    assert len(cmds) == 2
    assert "npm run deploy" in cmds[0]["command"]
    assert "curl" in cmds[1]["command"]

    db.unlink()
    tmp.unlink()


def test_real_transcript_index():
    """Index a real transcript on this machine."""
    from lib.transcript import find_all_transcripts
    transcripts = find_all_transcripts()
    if not transcripts:
        return

    smallest = min(transcripts, key=lambda t: t.stat().st_size)
    stats = update_index(smallest)
    db = index_path_for(smallest)

    print(f"\nIndexed {smallest.name}:")
    print(f"  Sections: {stats['total_sections']}")
    print(f"  Shell commands: {stats['shell_commands']}")
    print(f"  DB size: {db.stat().st_size} bytes")

    cmds = query_shell_commands(db)
    if cmds:
        print(f"  First command: {cmds[0]['command'][:80]}")

    db.unlink()
