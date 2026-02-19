# Layer 1: all command modules import without error and export callable cmd_* functions.

import importlib

MODULES = [
    'workspaces', 'composers_cmd', 'messages', 'search', 'tools_cmd',
    'context_cmd', 'files_todos', 'images', 'export', 'status_cmd',
    'db_cmd', 'audit_cmd', 'dotcursor_cmd',
]


def test_all_command_modules_import():
    for mod_name in MODULES:
        mod = importlib.import_module(f'lib.commands.{mod_name}')
        assert mod is not None, f"Failed to import {mod_name}"


def test_all_commands_are_callable():
    import lib.commands
    all_cmds = [name for name in dir(lib.commands) if name.startswith('cmd_')]
    assert len(all_cmds) >= 70, f"Expected >= 70 commands, got {len(all_cmds)}"
    for name in all_cmds:
        func = getattr(lib.commands, name)
        assert callable(func), f"{name} is not callable"


def test_key_commands_exist():
    from lib.commands import (
        cmd_list_workspaces, cmd_show_workspace, cmd_tree,
        cmd_list_composers, cmd_show_composer,
        cmd_tail, cmd_stream, cmd_transcript,
        cmd_grep, cmd_analyze,
        cmd_tools, cmd_tool_result, cmd_thinking,
        cmd_status, cmd_status_config,
        cmd_sql, cmd_find,
        cmd_secrets, cmd_full_audit,
        cmd_dotcursor_status, cmd_events,
    )
    for func in [cmd_list_workspaces, cmd_tail, cmd_grep, cmd_status, cmd_sql]:
        assert callable(func)
