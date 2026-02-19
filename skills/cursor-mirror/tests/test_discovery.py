# Layer 1: workspace discovery works on this machine.

from pathlib import Path


def test_iter_workspace_paths(workspaces_root: Path):
    from lib.discovery import iter_workspace_paths
    paths = list(iter_workspace_paths())
    assert len(paths) > 0, "Should find at least one workspace"
    for p in paths:
        assert p.is_dir()


def test_get_workspace_folder(any_workspace: Path):
    from lib.discovery import get_workspace_folder
    folder = get_workspace_folder(any_workspace)
    # folder can be None for some workspaces, but the function should not crash
    if folder is not None:
        assert isinstance(folder, str)


def test_folder_uri_to_path():
    from lib.discovery import folder_uri_to_path
    assert folder_uri_to_path("file:///Users/me/project") == "/Users/me/project"
    assert folder_uri_to_path("file:///path/with%20spaces") == "/path/with spaces"
    assert folder_uri_to_path("/already/a/path") == "/already/a/path"


def test_project_name_from_uri():
    from lib.discovery import project_name_from_uri
    assert project_name_from_uri("file:///Users/me/project") == "project"
    assert project_name_from_uri("file:///Users/me/my%20project") == "my project"
    assert project_name_from_uri("/Users/me/foo/") == "foo"
