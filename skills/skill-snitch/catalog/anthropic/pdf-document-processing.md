# pdf — Deep Probe + MOOLLM Integration Notes

> IMPORT as new MOOLLM-native skill. No document processing skill exists.

**Trust**: GREEN | **Scripts**: 8 Python | **License**: Proprietary (source-available)

## What It Does

Full PDF toolkit: read/extract text and tables, merge, split, rotate, watermark, create new PDFs, fill forms (fillable and annotation-based), encrypt/decrypt, extract images, OCR scanned documents. Uses pypdf, pdfplumber, reportlab.

## Code Review

| Script | Lines | Issues |
|--------|-------|--------|
| check_bounding_boxes.py | 55 | No docstring. sys.argv. Type hints on dataclass only. |
| check_fillable_fields.py | 10 | **No `if __name__` guard — runs on import.** No docstring. |
| convert_pdf_to_images.py | 28 | No docstring. sys.argv. No type hints. |
| create_validation_image.py | 33 | No docstring. sys.argv. No type hints. |
| extract_form_field_info.py | 108 | No docstring. sys.argv. Partial type hints. |
| extract_form_structure.py | 97 | Has docstring with usage. sys.argv. No type hints. |
| fill_fillable_fields.py | 90 | **CWD-dependent relative import** (`from extract_form_field_info import`). Monkeypatches pypdf. |
| fill_pdf_form_with_annotations.py | 95 | No docstring. sys.argv. No type hints. |

**Systemic issues**:
- 7/8 scripts use raw sys.argv instead of argparse
- 7/8 lack module docstrings
- 6/8 lack type hints
- 1 runs on import (check_fillable_fields.py)
- 1 has CWD-dependent relative import (fill_fillable_fields.py)
- 0/8 output JSON (all print prose)
- The monkeypatch in fill_fillable_fields.py is fragile (pypdf version-dependent)

**What's good**: All use pypdf/pdfplumber (well-maintained libraries). No eval/exec. No subprocess (except CLI tools referenced in SKILL.md). `extract_form_structure.py` has a proper docstring.

## MOOLLM-Native Version

**New skill**: `skills/pdf/`

**Upgrades**:
1. All scripts get **argparse** with `--help` and `--json` output
2. All scripts get **module docstrings** (sniffable in 5 lines)
3. `check_fillable_fields.py` gets `if __name__` guard
4. `fill_fillable_fields.py` relative import → absolute or package import
5. **empathic-expressions**: "fill in the name field" → identifies correct field_id
6. **room**: each page is a room, navigate PDF as space
7. **image-mining**: Three Eyes on each page
8. **sister-script**: all scripts follow the pattern (script IS documentation)
9. **advertisement**: PDF-OPS activates when PDF files are in context

**License note**: Anthropic's PDF skill is proprietary (source-available, not Apache 2.0). The MOOLLM version would be a clean reimplementation using the same libraries (pypdf, pdfplumber, reportlab are all open source), not a fork of their code. The SKILL.md approach and method design can be inspired by theirs.
