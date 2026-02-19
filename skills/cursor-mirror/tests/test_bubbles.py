# Layer 1: bubble access and text extraction against real Cursor data.

from pathlib import Path


def test_iter_bubbles_all(global_db: Path):
    from lib.bubbles import iter_bubbles
    count = 0
    for cid, key, obj in iter_bubbles():
        assert isinstance(cid, str)
        assert key.startswith("bubbleId:")
        assert isinstance(obj, dict)
        count += 1
        if count >= 100:
            break
    assert count > 0, "Should find at least some bubbles"


def test_load_bubbles_for_largest(global_db: Path):
    from lib.composers import get_bubble_counts
    from lib.bubbles import load_bubbles
    counts = get_bubble_counts()
    largest_cid = max(counts, key=counts.get)
    bubbles = load_bubbles(largest_cid)
    assert len(bubbles) > 0
    assert len(bubbles) == counts[largest_cid]


def test_get_bubble_text():
    from lib.bubbles import get_bubble_text
    assert get_bubble_text({"text": "hello"}) == "hello"
    assert get_bubble_text({"content": "world"}) == "world"
    assert get_bubble_text({}) == ""


def test_has_content():
    from lib.bubbles import has_content
    assert has_content({"text": "hello"})
    assert has_content({"toolCalls": [{}]})
    assert has_content({"thinking": {"text": "..."}})
    assert not has_content({})


def test_extract_bubble_text_user():
    from lib.bubbles import extract_bubble_text, USER
    obj = {"type": USER, "text": "What is this?", "codeBlocks": []}
    assert "What is this?" in extract_bubble_text(obj)


def test_extract_bubble_text_assistant():
    from lib.bubbles import extract_bubble_text, ASSISTANT
    obj = {"type": ASSISTANT, "text": "Here is the answer.", "codeBlocks": []}
    assert "Here is the answer." in extract_bubble_text(obj)


def test_extract_bubble_text_with_code_blocks():
    from lib.bubbles import extract_bubble_text, ASSISTANT
    obj = {
        "type": ASSISTANT,
        "text": "Check this:",
        "codeBlocks": [{"content": "print('hello')"}],
    }
    result = extract_bubble_text(obj)
    assert "Check this:" in result
    assert "print('hello')" in result


def test_is_error():
    from lib.bubbles import is_error
    assert is_error({"toolFormerData": {"additionalData": {"status": "error"}}})
    assert not is_error({"toolFormerData": {"additionalData": {"status": "success"}}})
    assert not is_error({})
    assert not is_error({"toolFormerData": {}})
