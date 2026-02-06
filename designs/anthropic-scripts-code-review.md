# Anthropic Skills Scripts — Code Review & MOOLLM Convention Suggestions

> 30 scripts reviewed line-by-line. What they do well, what could be better, and how MOOLLM conventions (sniffable-python, sister-script, CWD-independence) would improve them.

## Overall Assessment

Anthropic's scripts are clean, security-conscious (zero eval/exec across all 30 files, defusedxml everywhere), and demonstrate a clear division of labor between deterministic scripts and LLM orchestration. But they're inconsistent in structure — some follow best practices, others cut corners.

## Scorecard

| Convention | Best Example | Count Following | Count Violating |
|-----------|-------------|-----------------|----------------|
| Module docstring | `soffice.py`, `comment.py` | 12/30 | 18/30 |
| argparse CLI | `thumbnail.py`, `evaluation.py` | 6/30 | 24/30 |
| `if __name__ == '__main__'` | Most scripts | 22/30 | 8/30 (libraries OK, but `check_fillable_fields.py` runs on import) |
| Type hints | `connections.py`, `gif_builder.py` | 16/30 | 14/30 |
| CWD-independent | `soffice.py`, easing/gif modules | 10/30 | 20/30 |
| JSON output for LLM consumption | `recalc.py` | 1/30 | 29/30 |
| No dead imports | Most | 29/30 | 1/30 (`quick_validate.py` imports `os` but never uses it) |

## Specific Issues & MOOLLM Recommendations

### 1. Most scripts use raw sys.argv instead of argparse

**Problem**: 24/30 scripts parse `sys.argv` manually with positional arguments. No `--help`, no argument validation, no named flags. The LLM has to read the source or the SKILL.md to know the argument order.

**Examples**:
```python
# Current (recalc.py)
filename = sys.argv[1]
timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 30

# Current (init_skill.py)
if len(sys.argv) < 4 or sys.argv[2] != '--path':
    print("Usage: init_skill.py --path ")
```

**MOOLLM sister-script convention**: Every script should have argparse with `--help`. The `--help` output IS part of the API surface. An LLM can run `python script.py --help` to learn the interface without reading source.

```python
# MOOLLM convention
parser = argparse.ArgumentParser(description="Recalculate Excel formulas via LibreOffice")
parser.add_argument("filename", help="Excel file to recalculate")
parser.add_argument("--timeout", type=int, default=30, help="Timeout in seconds")
parser.add_argument("--json", action="store_true", help="Output as JSON")
```

**Best existing example**: `thumbnail.py` and `evaluation.py` — both use argparse properly with argument groups and epilog examples.

### 2. CWD dependency is rampant

**Problem**: 20/30 scripts resolve file paths relative to CWD. If the LLM runs the script from a different directory, paths break. Worse: `fill_fillable_fields.py` does `from extract_form_field_info import get_field_info` — a relative Python import that only works if CWD is the `scripts/` directory.

**MOOLLM convention**: Scripts should work from any directory. Use `Path(__file__).parent` for script-relative resources. Accept absolute or relative paths via CLI args. Never assume CWD.

```python
# CWD-independent resource loading
SCRIPT_DIR = Path(__file__).parent
TEMPLATE_DIR = SCRIPT_DIR / "templates"

# Accept paths that work from anywhere
parser.add_argument("input", type=Path, help="Input file (absolute or relative)")
```

**Best existing example**: `soffice.py` — uses absolute paths for everything (`/tmp/`, `Path(filename).absolute()`). Also `comment.py` uses `Path(__file__).parent / "templates"`.

### 3. Only 1 script outputs structured JSON

**Problem**: `recalc.py` is the ONLY script that outputs structured JSON. Every other script outputs human-readable text. The LLM has to parse prose to understand results.

**MOOLLM convention**: Every script should support `--json` flag for structured output. The default can be human-readable, but `--json` gives the LLM clean data.

```python
# MOOLLM convention: dual output
if args.json:
    print(json.dumps({"status": "success", "files_removed": removed, "count": len(removed)}))
else:
    print(f"Removed {len(removed)} unreferenced files")
```

**Why this matters for LLM orchestration**: When the LLM runs `clean.py --json`, it gets `{"removed": ["ppt/slides/slide3.xml", ...], "count": 3}` instead of parsing `"Removed 3 unreferenced files:\n  ppt/slides/slide3.xml"`.

### 4. Sniffable-python: API in the first 50 lines

**Problem**: Some scripts bury their API deep. `fill_fillable_fields.py` starts with imports and helper functions — you have to scroll to `fill_pdf_fields()` to understand what it does. Others (`check_fillable_fields.py`) are 10 lines with no structure at all.

**MOOLLM sniffable-python convention**: The API should be visible by reading the first 50 lines. Module docstring → imports → main function signature → `if __name__`.

```python
"""Fill PDF form fields from JSON data.

Usage: python fill_fillable_fields.py input.pdf fields.json output.pdf

The fields.json should contain: [{"field_id": "name", "page": 1, "value": "Claude"}]
"""

# ... imports ...

def fill_pdf_fields(input_pdf: str, fields_json: str, output_pdf: str) -> dict:
    """Fill form fields and return status."""
    ...

if __name__ == "__main__":
    ...
```

**Best existing examples**: `soffice.py` (docstring with two usage patterns), `comment.py` (docstring with examples AND XML instructions), `evaluation.py` (rich argparse with examples in epilog).

### 5. check_fillable_fields.py runs on import

**Problem**: This 10-line script has no `if __name__` guard. It runs PdfReader on import, meaning you can't import it as a module.

```python
# Current — executes on import!
reader = PdfReader(sys.argv[1])
if (reader.get_fields()):
    print("This PDF has fillable form fields")
```

**MOOLLM convention**: Always guard with `if __name__`. Even tiny scripts. Even one-liners.

### 6. Division of labor is excellent but undocumented

**Problem**: The division between deterministic scripts and LLM reasoning is consistently good across all scripts — but it's implicit. The SKILL.md describes it but the scripts themselves don't declare their boundary.

**MOOLLM convention**: Each script should declare its automation boundary in the docstring.

```python
"""Accept all tracked changes in a DOCX file.

DETERMINISTIC: This script handles LibreOffice macro setup, file copying,
and change acceptance. No LLM reasoning occurs at runtime.

LLM ROLE: Decide when to call this script and provide input/output paths.
The LLM does not need to understand OOXML internals.
"""
```

### 7. Error handling via string matching

**Problem**: Multiple scripts return `(None, message)` tuples and check for errors via `if "Error" in message`. This is fragile.

```python
# Current
_, message = accept_changes(args.input_file, args.output_file)
if "Error" in message:
    raise SystemExit(1)
```

**MOOLLM convention**: Use exceptions or return structured results.

```python
# Better: structured result
result = accept_changes(args.input_file, args.output_file)
if result["status"] == "error":
    print(json.dumps(result))
    sys.exit(1)
```

### 8. validate.py uses assert for argument validation

**Problem**: `validate.py` uses `assert` statements for input validation. Asserts can be disabled with `python -O`, silently skipping all checks.

```python
# Current
assert path.exists(), f"Error: {path} does not exist"
```

**MOOLLM convention**: Never use assert for input validation. Use `if not ... raise` or argparse constraints.

## What They Do Well (keep these patterns)

### 1. Zero eval/exec across all 30 files
Not a single eval or exec anywhere. Security-conscious throughout.

### 2. defusedxml everywhere
Every script that parses XML uses `defusedxml.minidom`, not `xml.dom.minidom`. Prevents XXE attacks.

### 3. Clean library modules (slack-gif-creator)
`gif_builder.py`, `validators.py`, `easing.py`, `frame_composer.py` — all pure libraries with no `__main__`, excellent docstrings, thorough type hints, zero CWD dependencies, zero I/O side effects. This is the gold standard.

### 4. soffice.py: remarkable engineering
A Python module that detects AF_UNIX socket restrictions, compiles a C shared library at runtime via GCC, and LD_PRELOADs it to intercept socket/listen/accept/close syscalls. This is the kind of deep systems programming you rarely see in skill scripts.

### 5. evaluation.py: Claude as test subject
The only script that uses an LLM at runtime — but as the test subject, not the orchestrator. The script provides deterministic infrastructure (connect, parse XML test cases, run agent loop, score exact-match, generate markdown report). Claude's role is to use MCP tools to answer questions. Clean separation.

### 6. comment.py: hybrid output
Prints the deterministic result AND the XML instructions for the LLM to follow next. The script handles the hard part (XML manipulation), then tells the LLM exactly what to do with the result. This is excellent division of labor.

## Summary: What MOOLLM Conventions Would Add

| Convention | Scripts Affected | Upgrade |
|-----------|-----------------|---------|
| argparse everywhere | 24 scripts | `--help` becomes part of the API |
| `--json` output flag | 29 scripts | LLM reads structured data, not prose |
| CWD-independent paths | 20 scripts | Scripts work from any directory |
| Module docstrings | 18 scripts | API visible in first 5 lines |
| Sniffable first 50 lines | ~10 scripts | Main function signature visible immediately |
| `if __name__` guard | 8 scripts | All scripts importable as modules |
| Structured error returns | ~8 scripts | Replace string matching with JSON status |
| Automation boundary docs | All scripts | Declare what's deterministic vs what needs LLM |

The scripts are clean and functional. These conventions would make them better citizens of an LLM-orchestrated ecosystem where the LLM needs to discover, invoke, and parse script interfaces programmatically.

---

*Reviewed 2026-02-06. 30 scripts, ~4,500 lines of code. Pattern: Play-Learn-Lift.*
