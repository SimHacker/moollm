# Layer 1: composer access works against real Cursor DBs.

from pathlib import Path


def test_get_workspace_composers(any_workspace: Path):
    from lib.composers import get_workspace_composers
    composers = get_workspace_composers(any_workspace)
    assert isinstance(composers, list)
    # At least one workspace should have composers; but this specific one might not
    for c in composers:
        assert isinstance(c, dict)
        assert "composerId" in c


def test_get_bubble_counts(global_db: Path):
    from lib.composers import get_bubble_counts
    counts = get_bubble_counts()
    assert isinstance(counts, dict)
    assert len(counts) > 0, "Should have at least one composer with bubbles"
    for cid, count in counts.items():
        assert isinstance(cid, str)
        assert isinstance(count, int)
        assert count > 0


def test_get_all_composers(global_db: Path):
    from lib.composers import get_all_composers
    all_c = get_all_composers()
    assert isinstance(all_c, dict)
    assert len(all_c) > 0
    for cid, meta in all_c.items():
        assert isinstance(cid, str)
        assert "_bubble_count" in meta


def test_cache_works(global_db: Path):
    from lib.composers import get_bubble_counts, clear_caches
    clear_caches()
    counts1 = get_bubble_counts()
    counts2 = get_bubble_counts()
    assert counts1 is counts2, "Second call should return cached object"
