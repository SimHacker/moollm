"""Read a YAML file's body whether it is flat or wrapped in an envelope key.

Older files wrap their slots (`object: {...}`, `character: {...}`); flat files put them at the
top. The same keys also appear in flat files as references (`prototype: skills/object`,
`prototype: {source, id}`, or a map of clonable prototypes), so an envelope is taken only
when the file has no top-level `name` and the value is a mapping that is not a reference.
"""

from __future__ import annotations

from typing import Any

REFERENCE_KEYS = {"source", "id", "ref", "path", "why"}


def body(data: Any, *envelopes: str) -> dict:
    """The first envelope whose value is a mapping of slots, else the file itself."""
    if not isinstance(data, dict):
        return {}
    if "name" in data:
        return data
    for key in envelopes:
        value = data.get(key)
        if isinstance(value, dict) and not set(value) <= REFERENCE_KEYS:
            return value
    return data
