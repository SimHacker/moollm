# Layer 2: validate tool schemas against actual Cursor data.
# Detects: unknown tools (Cursor added new ones), undocumented params, API drift.

from pathlib import Path


def test_tool_schemas_load():
    from lib.tool_validator import load_tool_schemas
    schemas = load_tool_schemas()
    assert len(schemas) > 10, f"Expected 10+ tools, got {len(schemas)}"
    assert "read_file" in schemas
    assert "run_terminal_cmd" in schemas
    assert "search_replace" in schemas


def test_param_aliases_load():
    from lib.tool_validator import load_param_aliases
    aliases = load_param_aliases()
    assert "read_file" in aliases
    assert "targetFile" in aliases["read_file"]


def test_validate_synthetic_bubbles():
    from lib.tool_validator import validate_tool_calls, load_tool_schemas
    schemas = load_tool_schemas()
    bubbles = [
        {"toolFormerData": {"name": "read_file", "params": {"path": "/tmp/test"}}},
        {"toolFormerData": {"name": "totally_new_tool_xyz", "params": {"foo": "bar"}}},
        {"text": "no tool here"},
    ]
    result = validate_tool_calls(bubbles, schemas)
    assert "totally_new_tool_xyz" in result.unknown_tools
    assert result.drift_detected


def test_validate_real_bubbles(global_db: Path):
    """Layer 2: scan actual Cursor bubbles for tool API drift."""
    from lib.tool_validator import validate_tool_calls, load_tool_schemas
    from lib.bubbles import iter_bubbles

    schemas = load_tool_schemas()
    sample_bubbles = []
    for _cid, _key, obj in iter_bubbles():
        if obj.get("toolFormerData"):
            sample_bubbles.append(obj)
            if len(sample_bubbles) >= 500:
                break

    result = validate_tool_calls(sample_bubbles, schemas)
    print(f"\nTool validation (500 sample bubbles):")
    print(f"  Observed tools: {len(result.observed_tools)}")
    print(f"  Unknown tools: {result.unknown_tools}")
    print(f"  Undocumented params: {dict((k, sorted(v)) for k, v in result.undocumented_params.items())}")
    print(f"  Drift detected: {result.drift_detected}")

    # This test reports but does not fail on drift -- drift is expected as Cursor evolves.
    # Fail only if we can't read tool calls at all.
    assert len(sample_bubbles) > 0, "Should find tool calls in bubbles"
    assert len(result.observed_tools) > 0, "Should observe at least one tool"
