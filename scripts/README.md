# MOOLLM Scripts

Development scripts for the moollm repository.

## Git Hooks

### Installation

```bash
./scripts/install-hooks.sh
```

This installs:
- **pre-commit** — Validates all staged YAML and JSON files before commit

### What Gets Validated

| Extension | Validator | Checks |
|-----------|-----------|--------|
| `.yml`, `.yaml` | PyYAML | Valid YAML syntax |
| `.json` | Python json | Valid JSON syntax |

### Example Output

```
🔍 Validating YAML files...
  Found 3 YAML file(s) to validate
  ✓ skills/foo/CARD.yml
  ✓ skills/foo/SKILL.md
  Error in skills/bar/CARD.yml:
    while parsing a block mapping
  expected <block end>, but found '<scalar>'

🔍 Validating JSON files...
  ✓ No JSON files staged

✗ Validation failed!
  1 file(s) with errors:
  - skills/bar/CARD.yml
```

### Common Issues

**YAML:**
- Strings with quotes need outer quotes: `'He said "hello"'`
- Strings with colons need quotes: `'key: value here'`
- Strings with special chars need quotes: `'text (with parens)'`

**JSON:**
- Trailing commas are not allowed
- Keys must be double-quoted strings
- No comments allowed in JSON

### Manual Validation

To validate without committing:

```bash
# Single file
python3 -c "import yaml; yaml.safe_load(open('file.yml'))"
python3 -c "import json; json.load(open('file.json'))"

# All YAML files
find . -name '*.yml' -exec python3 -c "import yaml; yaml.safe_load(open('{}'))" \;
```
