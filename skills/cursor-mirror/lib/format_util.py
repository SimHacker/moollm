# Output formatting utilities.
# format_ts, get_output_format, output_data, format_not_supported

import json
import sys
from datetime import datetime
from typing import Any


def format_ts(ts: int | float | str | None) -> str:
    """Format timestamp for display."""
    match ts:
        case str():
            return ts[:19].replace("T", " ")
        case int() | float():
            return datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S")
        case _:
            return str(ts) if ts is not None else ""


def get_output_format(args: Any, default: str = "text") -> str:
    """Get the output format from args, with legacy --json/--yaml fallback."""
    if getattr(args, "output_format", None):
        return args.output_format.lower()
    if getattr(args, "json", False):
        return "json"
    if getattr(args, "yaml", False):
        return "yaml"
    return default


def format_not_supported(fmt: str, command: str, supported: list[str]) -> None:
    """Print error and exit for unsupported format."""
    print(f"Error: Format '{fmt}' not supported by '{command}'.", file=sys.stderr)
    print(f"Supported formats: {', '.join(supported)}", file=sys.stderr)
    sys.exit(1)


def output_data(
    data: Any,
    fmt: str,
    command: str = "command",
    supported: list[str] | None = None,
    pretty: bool = False,
) -> None:
    """Output data in the requested format (text, json, jsonl, yaml, csv, md)."""
    if supported is None:
        supported = ["text", "json", "yaml"]

    fmt = fmt.lower()
    if fmt not in supported:
        format_not_supported(fmt, command, supported)
        return

    match fmt:
        case "text":
            if isinstance(data, str):
                print(data)
            elif data is not None:
                _print_text_data(data)

        case "json":
            indent = 2 if pretty else None
            print(json.dumps(data, indent=indent, default=str, ensure_ascii=False))

        case "jsonl":
            if isinstance(data, list):
                for item in data:
                    print(json.dumps(item, default=str, ensure_ascii=False))
            else:
                print(json.dumps(data, default=str, ensure_ascii=False))

        case "yaml":
            import yaml
            print(yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))

        case "csv":
            _print_csv(data)

        case "md":
            _print_markdown(data)

        case _:
            format_not_supported(fmt, command, supported)


def _print_text_data(data: Any, indent: int = 0) -> None:
    prefix = "  " * indent
    match data:
        case dict():
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    print(f"{prefix}{k}:")
                    _print_text_data(v, indent + 1)
                else:
                    print(f"{prefix}{k}: {v}")
        case list():
            for item in data:
                if isinstance(item, dict):
                    print(f"{prefix}- ")
                    _print_text_data(item, indent + 1)
                else:
                    print(f"{prefix}- {item}")
        case _:
            print(f"{prefix}{data}")


def _print_csv(data: Any) -> None:
    import csv
    import io

    if not isinstance(data, list) or not data:
        print("Error: CSV format requires a non-empty list of records.", file=sys.stderr)
        sys.exit(1)

    output = io.StringIO()
    if isinstance(data[0], dict):
        all_keys: list[str] = []
        seen: set[str] = set()
        for row in data:
            for key in row:
                if key not in seen:
                    all_keys.append(key)
                    seen.add(key)

        def flatten(v: Any) -> str:
            if v is None:
                return ""
            if isinstance(v, (dict, list)):
                return json.dumps(v, ensure_ascii=False)
            return str(v)

        writer = csv.DictWriter(output, fieldnames=all_keys, extrasaction="ignore")
        writer.writeheader()
        for row in data:
            writer.writerow({k: flatten(row.get(k, "")) for k in all_keys})
    else:
        writer = csv.writer(output)
        writer.writerows(data)
    print(output.getvalue(), end="")


def _print_markdown(data: Any, depth: int = 0) -> None:
    """Smart markdown output -- tables for flat dicts, nested outlines for deep structures."""
    match data:
        case None:
            print("*null*")
        case str() if "\n" in data and len(data) > 100:
            print("```")
            print(data)
            print("```")
        case str():
            print(data)
        case int() | float() | bool():
            print(f"`{data}`")
        case list() if not data:
            print("*(empty list)*")
        case list() if all(isinstance(item, dict) for item in data):
            _print_markdown_table(data)
        case list():
            indent = "  " * depth
            for item in data:
                if isinstance(item, (dict, list)):
                    print(f"{indent}-")
                    _print_markdown(item, depth + 1)
                else:
                    s = str(item)
                    print(f"{indent}- {s[:77] + '...' if len(s) > 80 else s}")
        case dict() if not data:
            print("*(empty)*")
        case dict():
            indent = "  " * depth
            for key, value in data.items():
                match value:
                    case dict():
                        if depth == 0:
                            print(f"\n## {key}")
                        else:
                            print(f"{indent}**{key}:**")
                        _print_markdown(value, depth + 1)
                    case list():
                        print(f"{indent}**{key}:** ({len(value)} items)")
                        _print_markdown(value, depth + 1)
                    case _:
                        s = str(value) if value is not None else "*null*"
                        print(f"{indent}- **{key}:** {s[:57] + '...' if len(s) > 60 else s}")


def _print_markdown_table(data: list[dict[str, Any]]) -> None:
    if not data:
        return
    headers: list[str] = []
    seen: set[str] = set()
    for row in data:
        for key in row:
            if key not in seen:
                headers.append(key)
                seen.add(key)

    def cell(v: Any) -> str:
        if v is None:
            return ""
        if isinstance(v, (dict, list)):
            s = json.dumps(v, ensure_ascii=False)
            return s[:47] + "..." if len(s) > 50 else s
        s = str(v).replace("|", "\\|").replace("\n", " ")
        return s[:47] + "..." if len(s) > 50 else s

    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join("---" for _ in headers) + " |")
    for row in data:
        print("| " + " | ".join(cell(row.get(h, "")) for h in headers) + " |")
