# I1: Tool param validation.
# Compare actual tool calls in bubbles against documented schemas in tools.yml.
# Detects: unknown tools, undocumented params, missing tools, Cursor API drift.
# Driven by reference/universal/model/tools.yml and entities/tool-param-aliases.yml

from pathlib import Path
from typing import Any
from dataclasses import dataclass, field

import yaml

from .debug_util import debug

_MODEL_DIR = Path(__file__).resolve().parent.parent / "reference" / "universal" / "model"


def _load_yaml(name: str) -> dict[str, Any]:
    path = _MODEL_DIR / name
    if path.exists():
        return yaml.safe_load(path.read_text()) or {}
    return {}


@dataclass
class ToolSchema:
    """Documented tool from the universal model."""
    name: str
    params: list[str] = field(default_factory=list)
    count: int = 0
    category: str = ""
    has_explanation: bool = False
    note: str = ""


@dataclass
class ValidationResult:
    """Result of validating observed tool calls against documented schemas."""
    documented_tools: dict[str, ToolSchema] = field(default_factory=dict)
    observed_tools: dict[str, int] = field(default_factory=dict)
    unknown_tools: dict[str, int] = field(default_factory=dict)
    undocumented_params: dict[str, set[str]] = field(default_factory=dict)
    missing_tools: list[str] = field(default_factory=list)

    @property
    def drift_detected(self) -> bool:
        return bool(self.unknown_tools) or bool(self.undocumented_params)

    def summary(self) -> dict[str, Any]:
        return {
            "documented_tools": len(self.documented_tools),
            "observed_tools": len(self.observed_tools),
            "unknown_tools": dict(self.unknown_tools),
            "undocumented_params": {k: sorted(v) for k, v in self.undocumented_params.items()},
            "missing_tools": self.missing_tools,
            "drift_detected": self.drift_detected,
        }


def load_tool_schemas() -> dict[str, ToolSchema]:
    """Load documented tool schemas from tools.yml."""
    raw = _load_yaml("tools.yml")
    schemas: dict[str, ToolSchema] = {}

    for category in ["file_operations", "search", "execution", "validation", "meta"]:
        cat_data = raw.get(category, {})
        for name, info in cat_data.items():
            if not isinstance(info, dict):
                continue
            schemas[name] = ToolSchema(
                name=name,
                params=info.get("params", []),
                count=info.get("count", 0),
                category=category,
                has_explanation=info.get("has_explanation", False),
                note=info.get("note", ""),
            )

    mcp = raw.get("mcp", {})
    for server, info in mcp.items():
        if isinstance(info, dict):
            for tool_name in info.get("tools", []):
                full_name = f"{server}.{tool_name}"
                schemas[full_name] = ToolSchema(name=full_name, category="mcp")

    return schemas


def load_param_aliases() -> dict[str, list[str]]:
    """Load tool param aliases from entities/tool-param-aliases.yml."""
    return _load_yaml("entities/tool-param-aliases.yml")


def validate_tool_calls(
    bubbles: list[dict[str, Any]],
    schemas: dict[str, ToolSchema] | None = None,
) -> ValidationResult:
    """Validate observed tool calls against documented schemas.

    Args:
        bubbles: list of bubble dicts (from load_bubbles or iter_bubbles)
        schemas: optional pre-loaded schemas (loads from model if None)

    Returns:
        ValidationResult with unknown tools, undocumented params, drift flag
    """
    if schemas is None:
        schemas = load_tool_schemas()

    aliases = load_param_aliases()
    result = ValidationResult(documented_tools=schemas)

    all_known_names = set(schemas.keys())
    # Also accept base names without v2 suffix and vice versa
    for name in list(all_known_names):
        if name.endswith("_v2"):
            all_known_names.add(name[:-3])
        else:
            all_known_names.add(f"{name}_v2")

    for bubble in bubbles:
        tfd = bubble.get("toolFormerData")
        if not tfd or not isinstance(tfd, dict):
            continue

        tool_name = tfd.get("name") or tfd.get("toolName") or ""
        if not tool_name:
            continue

        result.observed_tools[tool_name] = result.observed_tools.get(tool_name, 0) + 1

        if tool_name not in all_known_names:
            result.unknown_tools[tool_name] = result.unknown_tools.get(tool_name, 0) + 1
            debug("unknown tool: %s", tool_name)

        # Check params against documented schema
        schema = schemas.get(tool_name)
        if schema and schema.params:
            known_params = set(schema.params)
            # Add aliases
            for alias_list in aliases.values():
                if any(p in known_params for p in alias_list):
                    known_params.update(alias_list)

            observed_params: set[str] = set()
            for key in ["params", "rawArgs"]:
                raw = tfd.get(key)
                if isinstance(raw, dict):
                    observed_params.update(raw.keys())
                elif isinstance(raw, str):
                    try:
                        import json
                        parsed = json.loads(raw)
                        if isinstance(parsed, dict):
                            observed_params.update(parsed.keys())
                    except (json.JSONDecodeError, TypeError):
                        pass

            novel = observed_params - known_params - {"explanation"}
            if novel:
                if tool_name not in result.undocumented_params:
                    result.undocumented_params[tool_name] = set()
                result.undocumented_params[tool_name].update(novel)

    # Check for documented tools never observed
    result.missing_tools = [
        name for name, schema in schemas.items()
        if schema.count > 0 and name not in result.observed_tools
    ]

    return result
