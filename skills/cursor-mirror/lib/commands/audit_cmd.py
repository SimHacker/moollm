# Security audit commands: secrets, scrub, exfil-audit, pattern-scan, audit, full-audit, etc.
# Extracted from cursor_mirror_old.py during Phase 2 refactoring.

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml
import os
import sqlite3
import subprocess

from ..db import open_db, decode_blob, get_item_table_value, get_reactive_storage
from ..paths import GLOBAL_DB, WORKSPACES_ROOT, BASE_DIR
from ..keys import SESSION_LIST_KEYS, COMPOSER_STATE_KEY, NOTABLE_GLOBAL_KEYS
from ..discovery import iter_workspace_paths, get_workspace_folder, folder_uri_to_path
from ..composers import get_workspace_composers, get_all_composers, get_bubble_counts, clear_caches
from ..bubbles import iter_bubbles, load_bubbles, get_bubble_text, has_content, extract_bubble_text, is_error, USER, ASSISTANT
from ..resolve import resolve_workspace, resolve_composer, resolve_composer_id
from ..format_util import format_ts, get_output_format, output_data, format_not_supported
from ..debug_util import debug
from ..sources import register_source


def _audit_section(section, content, patterns, shell_danger, findings, stats, path, line, tool, limit, vector_filter):
    """Audit a transcript section for secrets."""
    if vector_filter and section not in vector_filter:
        return
    
    if len(findings.get(section, [])) >= limit:
        return
    
    # Skip self-references (pattern definitions)
    if 'AUDIT_PATTERNS' in content[:500] or 'EXFIL_PATTERNS' in content[:500]:
        return
    
    # Check for secrets
    for regex, secret_type, severity in patterns:
        for match in regex.finditer(content):
            matched = match.group()
            if len(matched) > 20:
                masked = matched[:10] + '...' + matched[-4:]
            else:
                masked = matched[:8] + '...'
            
            findings[section].append({
                'path': path,
                'line': line,
                'tool': tool,
                'type': secret_type,
                'severity': severity,
                'masked': masked,
            })
            stats[section][secret_type] += 1
    
    # Special check for shell commands with data exfil
    if section == 'tool_call' and tool and 'shell' in tool.lower():
        if shell_danger.search(content):
            findings[section].append({
                'path': path,
                'line': line,
                'tool': tool,
                'type': 'shell_data_exfil',
                'severity': 'high',
                'masked': content[:50] + '...',
            })
            stats[section]['shell_data_exfil'] += 1


def _scan_for_secrets(text, patterns, findings, stats, path, line, tool, source, limit, tool_filter):
    """Helper to scan text for secrets and add findings."""
    if tool_filter and tool_filter.lower() not in tool.lower():
        return
    
    for regex, secret_type, severity in patterns:
        if len(findings) >= limit:
            return
        
        for match in regex.finditer(text):
            matched = match.group()
            
            # Skip if it looks like it's part of the pattern definition itself
            if 'SECRET_PATTERNS' in text[:500] or 'EXFIL_PATTERNS' in text[:500]:
                if matched in text[:1000]:  # Likely self-reference
                    continue
            
            # Mask the secret
            if len(matched) > 16:
                masked = matched[:8] + "..." + matched[-4:]
            else:
                masked = matched[:4] + "..."
            
            findings.append({
                "source": source,
                "path": path,
                "line": line,
                "tool": tool,
                "type": secret_type,
                "severity": severity,
                "masked": masked,
            })
            
            stats["severity"][severity] += 1
            stats["type"][secret_type] += 1
            stats["tool"][tool] += 1
            
            if len(findings) >= limit:
                return


def cmd_secrets(args):
    """Scan transcripts for potential secrets/credentials using K-REFS output.

    Looks for: API keys, private keys, database URIs, passwords, tokens, etc.

    ⚠️  EXPECT FALSE POSITIVES when scanning sessions where:
      - Security patterns were written/discussed (detects its own definitions)
      - Documentation contains example credentials
      - Code handles credential patterns (even without real values)
    
    The scanner detects patterns like `-----BEGIN PRIVATE KEY-----` even when
    they appear in pattern definitions or docs. Always verify actual line content.
    """
    import re
    
    # Compile patterns
    compiled = [(re.compile(pat), name) for pat, name in SECRET_PATTERNS]
    
    # Get files to scan
    files_to_scan = []
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    since_ts = parse_time_filter(args.since) if args.since else None
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if os.path.isdir(trans_dir):
            for fname in os.listdir(trans_dir):
                if fname.endswith('.txt'):
                    if args.composer and not fname.startswith(args.composer):
                        continue
                    fpath = os.path.join(trans_dir, fname)
                    if since_ts:
                        mtime = os.path.getmtime(fpath) * 1000
                        if mtime < since_ts:
                            continue
                    files_to_scan.append(fpath)
    
    matches = []
    context = args.context
    
    for fpath in files_to_scan:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except:
            continue
        
        for i, line in enumerate(lines):
            line_stripped = line.rstrip('\n\r')
            lineno = i + 1
            
            for regex, secret_type in compiled:
                match = regex.search(line_stripped)
                if match:
                    # Mask the actual secret in output
                    matched_text = match.group()
                    if len(matched_text) > 12:
                        masked = matched_text[:6] + "..." + matched_text[-4:]
                    else:
                        masked = matched_text[:4] + "..."
                    
                    start_line = max(1, lineno - context)
                    end_line = min(len(lines), lineno + context)
                    
                    excerpt = []
                    if not args.refs_only:
                        for j in range(start_line - 1, end_line):
                            excerpt.append(lines[j].rstrip('\n\r')[:100])
                    
                    matches.append({
                        "path": fpath,
                        "line": lineno,
                        "start": start_line,
                        "end": end_line,
                        "type": secret_type,
                        "masked": masked,
                        "excerpt": excerpt if excerpt else None
                    })
                    
                    if len(matches) >= args.limit:
                        break
            
            if len(matches) >= args.limit:
                break
        if len(matches) >= args.limit:
            break
    
    # Output
    if args.yaml:
        print(yaml.dump({"secrets": matches, "count": len(matches)}, 
                       default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps({"secrets": matches, "count": len(matches)}, indent=2))
    elif args.refs_only:
        for m in matches:
            print(f"{m['path']}:{m['start']}-{m['end']} # {m['type']} | {m['masked']}")
    else:
        print(f"# Potential Secrets Found: {len(matches)}")
        print(f"# WARNING: Review carefully - may include false positives")
        print()
        for m in matches:
            print(f"{m['path']}:{m['start']}-{m['end']} # {m['type']} | {m['masked']}")
            if m.get("excerpt"):
                print("-" * 60)
                for eline in m["excerpt"]:
                    print(f"    {eline}")
                print()


def cmd_scrub(args):
    """Redact sensitive content from transcripts. QUIT CURSOR FIRST!"""
    import re
    
    print("=" * 60)
    print("SCRUB: Redact sensitive content from Cursor transcripts")
    print("=" * 60)
    print()
    print("WARNING: Make sure Cursor is QUIT before running this!")
    print("         Cursor must not be writing to these files.")
    print()
    
    # Build patterns to scrub
    patterns_to_scrub = []
    
    if args.secrets:
        for pat, name in SECRET_PATTERNS:
            patterns_to_scrub.append((re.compile(pat), name))
    
    if args.pattern:
        try:
            patterns_to_scrub.append((re.compile(args.pattern), 'custom'))
        except re.error as e:
            print(f"Invalid pattern: {e}")
            return
    
    if not patterns_to_scrub:
        print("No patterns specified. Use --secrets and/or --pattern")
        return
    
    # Get files to scrub
    files_to_scrub = []
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if os.path.isdir(trans_dir):
            for fname in os.listdir(trans_dir):
                if fname.endswith('.txt'):
                    if args.composer and not fname.startswith(args.composer):
                        continue
                    files_to_scrub.append(os.path.join(trans_dir, fname))
    
    if not files_to_scrub:
        print("No transcript files found to scrub")
        return
    
    print(f"Files to scan: {len(files_to_scrub)}")
    print(f"Patterns: {len(patterns_to_scrub)}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()
    
    total_redactions = 0
    files_modified = 0
    
    for fpath in files_to_scrub:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
            continue
        
        original_content = content
        file_redactions = 0
        
        for regex, pattern_name in patterns_to_scrub:
            matches = list(regex.finditer(content))
            for match in reversed(matches):  # Reverse to preserve positions
                matched_text = match.group()
                if args.dry_run:
                    print(f"  Would redact [{pattern_name}]: {matched_text[:20]}... in {os.path.basename(fpath)}")
                content = content[:match.start()] + args.redact_text + content[match.end():]
                file_redactions += 1
        
        if file_redactions > 0:
            total_redactions += file_redactions
            files_modified += 1
            
            if not args.dry_run:
                # Create backup unless disabled
                if not args.no_backup:
                    backup_path = fpath + '.bak'
                    try:
                        with open(backup_path, 'w', encoding='utf-8') as f:
                            f.write(original_content)
                        print(f"  Backup: {backup_path}")
                    except Exception as e:
                        print(f"  WARNING: Could not create backup: {e}")
                        print(f"  Skipping {fpath}")
                        continue
                
                # Write scrubbed content
                try:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  Scrubbed {file_redactions} items in {os.path.basename(fpath)}")
                except Exception as e:
                    print(f"  ERROR writing {fpath}: {e}")
    
    print()
    print(f"{'Would redact' if args.dry_run else 'Redacted'}: {total_redactions} items in {files_modified} files")
    if args.dry_run:
        print("\nRun without --dry-run to apply changes")


def cmd_exfil_audit(args):
    """Comprehensive secret exfiltration audit - ALL tools, ALL arguments, both stores.
    
    Design: Systematic, complete by construction.
    - Scans EVERY tool call from both data stores
    - Checks EVERY argument against comprehensive secret patterns
    - Reports ALL findings with K-REFS pointers
    """
    import re
    from collections import defaultdict
    
    # Comprehensive secret patterns - expanded for full coverage
    EXFIL_PATTERNS = [
        # API Keys - specific vendors
        (r'sk-[a-zA-Z0-9]{20,}', 'openai_key', 'high'),
        (r'sk-proj-[a-zA-Z0-9]{20,}', 'openai_project_key', 'high'),
        (r'sk-ant-[a-zA-Z0-9]{20,}', 'anthropic_key', 'high'),
        (r'AKIA[0-9A-Z]{16}', 'aws_access_key', 'high'),
        (r'(?i)aws[_-]?secret[_-]?access[_-]?key["\s:=]+[A-Za-z0-9/+=]{40}', 'aws_secret', 'high'),
        (r'ghp_[a-zA-Z0-9]{36}', 'github_pat', 'high'),
        (r'gho_[a-zA-Z0-9]{36}', 'github_oauth', 'high'),
        (r'github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}', 'github_fine_grained', 'high'),
        (r'glpat-[a-zA-Z0-9\-]{20}', 'gitlab_pat', 'high'),
        (r'xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[a-zA-Z0-9]{24}', 'slack_token', 'high'),
        (r'AIza[0-9A-Za-z\-_]{35}', 'google_api_key', 'high'),
        (r'ya29\.[0-9A-Za-z\-_]+', 'google_oauth', 'high'),
        (r'(?i)npm_[a-zA-Z0-9]{36}', 'npm_token', 'high'),
        (r'(?i)pypi-[a-zA-Z0-9]{32,}', 'pypi_token', 'high'),
        (r'sq0[a-z]{3}-[0-9A-Za-z\-_]{22,}', 'square_token', 'high'),
        (r'stripe_[a-zA-Z0-9]{24,}', 'stripe_key', 'high'),
        (r'sk_live_[a-zA-Z0-9]{24,}', 'stripe_secret', 'high'),
        (r'rk_live_[a-zA-Z0-9]{24,}', 'stripe_restricted', 'high'),
        (r'twilio_[a-zA-Z0-9]{32}', 'twilio_key', 'high'),
        (r'AC[a-f0-9]{32}', 'twilio_sid', 'medium'),
        (r'sendgrid\.[a-zA-Z0-9\-_]{34,}', 'sendgrid_key', 'high'),
        (r'SG\.[a-zA-Z0-9\-_]{22}\.[a-zA-Z0-9\-_]{43}', 'sendgrid_api', 'high'),
        
        # Generic secrets
        (r'(?i)bearer\s+[a-zA-Z0-9\-_.]{20,}', 'bearer_token', 'high'),
        (r'(?i)password[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'password', 'high'),
        (r'(?i)passwd[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'passwd', 'high'),
        (r'(?i)secret[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'secret_value', 'high'),
        (r'(?i)api[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'api_key', 'high'),
        (r'(?i)auth[_-]?token[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'auth_token', 'high'),
        (r'(?i)access[_-]?token[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'access_token', 'high'),
        (r'(?i)private[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'private_key_value', 'high'),
        
        # Private keys (PEM format)
        (r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', 'private_key_pem', 'critical'),
        (r'-----BEGIN PGP PRIVATE KEY BLOCK-----', 'pgp_private', 'critical'),
        (r'-----BEGIN ENCRYPTED PRIVATE KEY-----', 'encrypted_private_key', 'critical'),
        
        # Database URIs with credentials
        (r'(?i)mongodb(?:\+srv)?://[^:]+:[^@]+@[^\s]+', 'mongodb_uri_with_creds', 'critical'),
        (r'(?i)postgres(?:ql)?://[^:]+:[^@]+@[^\s]+', 'postgres_uri_with_creds', 'critical'),
        (r'(?i)mysql://[^:]+:[^@]+@[^\s]+', 'mysql_uri_with_creds', 'critical'),
        (r'(?i)redis://[^:]+:[^@]+@[^\s]+', 'redis_uri_with_creds', 'critical'),
        (r'(?i)amqp://[^:]+:[^@]+@[^\s]+', 'amqp_uri_with_creds', 'critical'),
        
        # URLs with secrets in query params
        (r'https?://[^\s]*[?&](?:api_?key|token|secret|password|auth)=[^&\s]{8,}', 'url_with_secret_param', 'high'),
        (r'https?://[^:]+:[^@]+@[^\s]+', 'url_with_basic_auth', 'critical'),
        
        # Sensitive file paths being accessed
        (r'(?i)\.env(?:\.local|\.prod|\.dev)?$', 'env_file', 'high'),
        (r'(?i)credentials\.json', 'credentials_file', 'high'),
        (r'(?i)service[_-]?account.*\.json', 'service_account_file', 'high'),
        (r'(?i)id_rsa(?:\.pub)?$', 'ssh_key_file', 'high'),
        (r'(?i)\.pem$', 'pem_file', 'medium'),
        (r'(?i)\.p12$', 'p12_file', 'high'),
        (r'(?i)\.pfx$', 'pfx_file', 'high'),
        (r'(?i)\.keystore$', 'keystore_file', 'high'),
        (r'(?i)/etc/passwd', 'etc_passwd', 'medium'),
        (r'(?i)/etc/shadow', 'etc_shadow', 'critical'),
        (r'(?i)~/.ssh/', 'ssh_dir', 'high'),
        (r'(?i)~/.aws/credentials', 'aws_credentials_file', 'critical'),
        (r'(?i)~/.netrc', 'netrc_file', 'high'),
        
        # JWT tokens
        (r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+', 'jwt_token', 'high'),
        
        # SSH private key content
        (r'-----BEGIN OPENSSH PRIVATE KEY-----', 'openssh_private_key', 'critical'),
        
        # High-entropy strings (potential secrets) - 32+ hex chars
        (r'(?<![a-fA-F0-9])[a-fA-F0-9]{32,64}(?![a-fA-F0-9])', 'hex_string_32plus', 'low'),
    ]
    
    # Compile patterns
    compiled_patterns = [(re.compile(p), name, sev) for p, name, sev in EXFIL_PATTERNS]
    
    findings = []
    stats = defaultdict(lambda: defaultdict(int))
    
    # Source 1: Transcripts
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    since_ts = parse_time_filter(args.since) if args.since else None
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            if args.composer and not fname.startswith(args.composer):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            
            if since_ts:
                mtime = os.path.getmtime(fpath) * 1000
                if mtime < since_ts:
                    continue
            
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    lines = f.readlines()
            except:
                continue
            
            # Parse tool calls with their full argument blocks
            current_tool = None
            tool_start_line = 0
            tool_args_text = []
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                lineno = i + 1
                
                # Detect tool call start
                if stripped.startswith('[Tool call]'):
                    # Process previous tool if exists
                    if current_tool and tool_args_text:
                        full_args = '\n'.join(tool_args_text)
                        _scan_for_secrets(
                            full_args, compiled_patterns, findings, stats,
                            fpath, tool_start_line, current_tool, "transcript",
                            args.limit, args.tool
                        )
                    
                    # Start new tool
                    parts = stripped.split()
                    current_tool = parts[2] if len(parts) > 2 else "unknown"
                    tool_start_line = lineno
                    tool_args_text = []
                
                # Detect end of tool section
                elif stripped.startswith('[Tool result]') or stripped in ('user:', 'assistant:'):
                    if current_tool and tool_args_text:
                        full_args = '\n'.join(tool_args_text)
                        _scan_for_secrets(
                            full_args, compiled_patterns, findings, stats,
                            fpath, tool_start_line, current_tool, "transcript",
                            args.limit, args.tool
                        )
                    current_tool = None
                    tool_args_text = []
                
                # Collect tool args
                elif current_tool:
                    tool_args_text.append(line)
                
                if len(findings) >= args.limit:
                    break
            
            if len(findings) >= args.limit:
                break
        if len(findings) >= args.limit:
            break
    
    # Source 2: SQLite
    if len(findings) < args.limit:
        global_db = os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage/state.vscdb")
        if os.path.isfile(global_db):
            try:
                conn = sqlite3.connect(f"file:{global_db}?mode=ro", uri=True)
                cursor = conn.cursor()
                
                # Get tool calls from bubbles
                cursor.execute("""
                    SELECT key, value FROM cursorDiskKV 
                    WHERE key LIKE 'bubbleId:%'
                    AND value LIKE '%"tool"%'
                    LIMIT 1000
                """)
                
                for key, value in cursor.fetchall():
                    if len(findings) >= args.limit:
                        break
                    try:
                        data = json.loads(value)
                        # Extract tool info if present
                        tool_name = data.get("tool", {}).get("name", "unknown") if isinstance(data.get("tool"), dict) else "unknown"
                        tool_args = json.dumps(data.get("tool", {}).get("args", data))
                        
                        _scan_for_secrets(
                            tool_args, compiled_patterns, findings, stats,
                            key, 0, tool_name, "sqlite",
                            args.limit, args.tool
                        )
                    except:
                        pass
                
                conn.close()
            except:
                pass
    
    # Output
    if args.yaml:
        output = {
            "findings": findings,
            "stats": {
                "total_findings": len(findings),
                "by_severity": dict(stats["severity"]),
                "by_type": dict(stats["type"]),
                "by_tool": dict(stats["tool"]),
            }
        }
        print(yaml.dump(output, default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        output = {
            "findings": findings,
            "stats": {
                "total_findings": len(findings),
                "by_severity": dict(stats["severity"]),
                "by_type": dict(stats["type"]),
                "by_tool": dict(stats["tool"]),
            }
        }
        print(json.dumps(output, indent=2))
    else:
        print("=" * 70)
        print("🔐 EXFILTRATION AUDIT (Comprehensive)")
        print("=" * 70)
        print(f"Sources: transcripts (~/.cursor) + state.vscdb")
        print(f"Patterns checked: {len(EXFIL_PATTERNS)}")
        print()
        
        # Summary stats
        print("📊 SUMMARY")
        print("-" * 40)
        print(f"Total findings: {len(findings)}")
        if stats["severity"]:
            print(f"By severity: " + ", ".join(f"{k}={v}" for k, v in sorted(stats["severity"].items(), key=lambda x: -x[1])))
        if stats["type"] and not args.summary:
            print(f"By type: " + ", ".join(f"{k}={v}" for k, v in list(stats["type"].items())[:5]))
        if stats["tool"]:
            print(f"By tool: " + ", ".join(f"{k}={v}" for k, v in list(stats["tool"].items())[:5]))
        
        if not args.summary and findings:
            print()
            print("🚨 FINDINGS (K-REFS)")
            print("-" * 40)
            for f in findings[:30]:  # Limit display
                sev_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "⚪"}.get(f["severity"], "?")
                if f["source"] == "transcript":
                    print(f"{sev_icon} {f['path']}:{f['line']} [{f['tool']}]")
                else:
                    print(f"{sev_icon} {f['path'][:50]} [{f['tool']}]")
                print(f"   {f['type']}: {f['masked'][:80]}")
            
            if len(findings) > 30:
                print(f"\n... and {len(findings) - 30} more findings")
        
        print()


def cmd_pattern_scan(args):
    """Find UUIDs, hashes, secrets, custom patterns with K-REFS output."""
    import re
    
    patterns = []
    
    # UUID pattern (standard format)
    if args.uuids or args.all:
        patterns.append((
            re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', re.I),
            'uuid', 'info'
        ))
    
    # Hash patterns
    if args.hashes or args.all:
        patterns.append((re.compile(r'(?<![a-fA-F0-9])[a-fA-F0-9]{32}(?![a-fA-F0-9])'), 'md5_hash', 'info'))
        patterns.append((re.compile(r'(?<![a-fA-F0-9])[a-fA-F0-9]{40}(?![a-fA-F0-9])'), 'sha1_hash', 'info'))
        patterns.append((re.compile(r'(?<![a-fA-F0-9])[a-fA-F0-9]{64}(?![a-fA-F0-9])'), 'sha256_hash', 'info'))
    
    # Secret patterns
    if args.secrets or args.all:
        patterns.extend([
            (re.compile(r'sk-[a-zA-Z0-9]{20,}'), 'openai_key', 'critical'),
            (re.compile(r'sk-ant-[a-zA-Z0-9]{20,}'), 'anthropic_key', 'critical'),
            (re.compile(r'AKIA[0-9A-Z]{16}'), 'aws_key', 'critical'),
            (re.compile(r'ghp_[a-zA-Z0-9]{36}'), 'github_pat', 'critical'),
            (re.compile(r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----'), 'private_key', 'critical'),
            (re.compile(r'(?i)password[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}'), 'password', 'high'),
            (re.compile(r'(?i)api[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}'), 'api_key', 'high'),
            (re.compile(r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+'), 'jwt', 'high'),
        ])
    
    # Custom pattern
    if args.pattern:
        try:
            patterns.append((re.compile(args.pattern), 'custom', 'info'))
        except re.error as e:
            print(f"Invalid pattern: {e}")
            return
    
    if not patterns:
        print("No patterns specified. Use --uuids, --hashes, --secrets, --all, or --pattern")
        return
    
    findings = []
    
    # Scan transcripts
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            if args.composer and not fname.startswith(args.composer):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
            except:
                continue
            
            lines = content.split('\n')
            
            # Build char->line and char->col mappings
            char_to_line = []
            char_to_col = []
            line_starts = [0]
            char_count = 0
            for i, line in enumerate(lines):
                for c in range(len(line)):
                    char_to_line.append(i + 1)
                    char_to_col.append(c + 1)  # 1-based column
                # newline char
                char_to_line.append(i + 1)
                char_to_col.append(len(line) + 1)
                char_count += len(line) + 1
                if i < len(lines) - 1:
                    line_starts.append(char_count)
            
            for regex, ptype, severity in patterns:
                for match in regex.finditer(content):
                    if len(findings) >= args.limit:
                        break
                    
                    start_pos = match.start()
                    end_pos = match.end()
                    line_num = char_to_line[start_pos] if start_pos < len(char_to_line) else len(lines)
                    col_start = char_to_col[start_pos] if start_pos < len(char_to_col) else 1
                    col_end = char_to_col[end_pos - 1] if end_pos - 1 < len(char_to_col) else col_start
                    matched = match.group()
                    
                    findings.append({
                        'path': fpath,
                        'line': line_num,
                        'col_start': col_start,
                        'col_end': col_end + 1,  # exclusive end
                        'char_start': start_pos,
                        'char_end': end_pos,
                        'length': len(matched),
                        'type': ptype,
                        'severity': severity,
                        'value': matched if len(matched) <= 20 else matched[:10] + '...' + matched[-6:],
                    })
                
                if len(findings) >= args.limit:
                    break
            if len(findings) >= args.limit:
                break
        if len(findings) >= args.limit:
            break
    
    # Output
    if args.emit_redact:
        # Simple redaction commands: file:line:col_start:col_end:length:type
        # Can be piped to a simple tool for processing
        print("# REDACT format: file:line:col_start:col_end:length:type")
        print("# Apply with: awk or simple Python script")
        print(f"# Total: {len(findings)}")
        for f in findings:
            print(f"REDACT:{f['path']}:{f['line']}:{f['col_start']}:{f['col_end']}:{f['length']}:{f['type']}")
    elif args.emit_sed:
        # Group by file for efficient sed processing
        by_file = {}
        for f in findings:
            by_file.setdefault(f['path'], []).append(f)
        
        print("#!/bin/bash")
        print("# Auto-generated redaction script")
        print(f"# {len(findings)} redactions across {len(by_file)} files")
        print()
        for fpath, items in by_file.items():
            print(f"# {os.path.basename(fpath)}: {len(items)} redactions")
            print(f"cp '{fpath}' '{fpath}.bak'")
            # Use Python for reliable fixed-length replacement (sed struggles with this)
            print(f"python3 -c \"")
            print(f"import sys")
            print(f"with open('{fpath}', 'r') as f: c = f.read()")
            # Sort by char_start descending to preserve offsets
            sorted_items = sorted(items, key=lambda x: x['char_start'], reverse=True)
            for item in sorted_items:
                mask = '*' * item['length']
                print(f"c = c[:{item['char_start']}] + '{mask}' + c[{item['char_end']}:]")
            print(f"with open('{fpath}', 'w') as f: f.write(c)")
            print(f"\"")
            print()
    elif args.yaml:
        print(yaml.dump({'findings': findings, 'count': len(findings)}, 
                       default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps({'findings': findings, 'count': len(findings)}, indent=2))
    else:
        print(f"# Pattern Scan: {len(findings)} findings")
        print(f"# Patterns: {len(patterns)}")
        print()
        for f in findings:
            sev_icon = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'info': 'ℹ️'}.get(f['severity'], '⚪')
            print(f"{f['path']}:{f['line']}:{f['col_start']}-{f['col_end']} # {f['type']} len={f['length']}")
            print(f"  {sev_icon} {f['value']}")


def cmd_audit(args):
    """Unified composable audit: surfaces × patterns.

    Examples:
        audit --surface transcript --patterns secrets
        audit --surface transcript --surface sqlite --patterns secrets --patterns uuids
        audit --surface transcript --pattern "my-secret-.*" --emit-redact
        audit --surface transcript --patterns secrets --mask --dry-run
        audit --pattern-file my-patterns.yml
        audit --pattern "password123" --pattern-type literal
        audit --pattern "secret*key" --pattern-type glob
    """
    # Resolve composer reference (@1, prefix, name) to full ID
    composer_id = None
    if args.composer:
        composer_id = resolve_composer_id(args.composer)
        if not composer_id:
            print(f"Composer not found: {args.composer}", file=sys.stderr)
            return
    
    runner = AuditRunner()

    # Add surfaces
    surfaces = args.surfaces or ["transcript"]  # Default to transcripts
    for surface in surfaces:
        if surface == "transcript":
            runner.add_surface(TranscriptSurface(
                workspace=args.workspace,
                composer=composer_id
            ))
        elif surface == "sqlite":
            runner.add_surface(SqliteSurface())
        elif surface == "config":
            # Add common config paths
            home = os.path.expanduser("~")
            runner.add_surface(ConfigSurface(paths=[
                os.path.join(home, ".cursor", "mcp.json"),
                os.path.join(home, ".cursor", "settings.json"),
            ]))
        else:
            print(f"Unknown surface: {surface}")
            print("Available: transcript, sqlite, config")
            return
    
    # Add patterns from YAML file
    if args.pattern_file:
        try:
            runner.add_patterns_from_yaml(args.pattern_file)
        except Exception as e:
            print(f"Error loading pattern file: {e}")
            return
    
    # Add pattern sets
    pattern_sets = args.pattern_sets or []
    if not pattern_sets and not args.pattern and not args.pattern_file:
        pattern_sets = ["secrets"]  # Default
    
    for pset in pattern_sets:
        if pset in PATTERN_REGISTRY:
            runner.add_pattern_set(pset)
        else:
            print(f"Unknown pattern set: {pset}")
            print(f"Available: {', '.join(PATTERN_REGISTRY.keys())}")
            return
    
    # Add custom pattern with specified type
    if args.pattern:
        match_type = MatchType(args.pattern_type)
        runner.add_pattern(AuditPattern(
            name="custom",
            pattern=args.pattern,
            match_type=match_type,
            severity=Severity.INFO,
            category="custom",
            description=f"Custom {args.pattern_type} pattern",
            redact_label="[CUSTOM]"
        ))
    
    # Execute
    preserve_ws = not args.no_preserve_ws
    
    if args.mask:
        results = runner.mask_in_place(
            dry_run=args.dry_run, 
            backup=True, 
            preserve_whitespace=preserve_ws,
            force=getattr(args, 'force', False),
            cursor_stopped=getattr(args, 'cursor_stopped', False)
        )
        if args.yaml:
            print(yaml.dump(results, default_flow_style=False))
        elif args.json:
            print(json.dumps(results, indent=2))
        else:
            for r in results:
                if "error" in r:
                    if "path" in r:
                        print(f"❌ {r['path']}: {r['error']}")
                    else:
                        print(f"❌ {r['error']}")
                        if "warning" in r:
                            print(f"   {r['warning']}")
                        if "hint" in r:
                            print(f"   {r['hint']}")
                else:
                    mode = "Would mask" if r["dry_run"] else "Masked"
                    types_str = ", ".join(r.get("types", []))
                    print(f"✓ {mode} {r['findings']} in {os.path.basename(r['path'])}")
                    print(f"  Types: {types_str}")
                    print(f"  Size: {r['size']} (unchanged), Whitespace: {'preserved' if r.get('preserved_whitespace') else 'replaced'}")
        return
    
    if args.emit_redact:
        for cmd in runner.emit_redact_commands():
            print(cmd)
        return
    
    # Default: K-REF output
    findings = list(runner.scan(limit=args.limit))
    
    if args.yaml:
        out = [{
            "kref": f.to_kref(), 
            "severity": f.severity.value, 
            "pattern": f.pattern_name,
            "match_type": f.match_type,
            "description": f.description,
            "redact_label": f.redact_label,
            "matched": f.matched
        } for f in findings]
        print(yaml.dump({"findings": out, "count": len(out)}, 
                       default_flow_style=False, allow_unicode=True))
    elif args.json:
        out = [{
            "path": f.path, "line": f.line, 
            "col_start": f.col_start, "col_end": f.col_end, 
            "char_start": f.char_start, "char_end": f.char_end,
            "pattern": f.pattern_name, 
            "match_type": f.match_type,
            "severity": f.severity.value,
            "description": f.description,
            "redact_label": f.redact_label,
            "matched": f.matched, 
            "surface": f.surface
        } for f in findings]
        print(json.dumps({"findings": out, "count": len(out)}, indent=2))
    else:
        print(f"# Audit: {len(findings)} findings")
        print(f"# Surfaces: {', '.join(surfaces)}")
        psets = pattern_sets or []
        if args.pattern:
            psets.append(f"custom:{args.pattern_type}")
        if args.pattern_file:
            psets.append(f"file:{args.pattern_file}")
        print(f"# Patterns: {', '.join(psets) if psets else 'default:secrets'}")
        print()
        
        for f in findings:
            print(f.to_kref())
            print(f"  {f.matched}")


def cmd_mask_in_place(args):
    """Mask secrets in-place with same-length replacement (file size unchanged).

    Key feature: Replaces each character with mask_char, preserving exact length.
    This means file offsets remain valid and file size is unchanged.
    """
    import re

    print("MASK-IN-PLACE (file size preserved)")
    print()
    
    # Safety check: is Cursor running?
    if not args.dry_run and not args.cursor_stopped:
        cursor_status = check_cursor_running()
        if cursor_status["running"] and not args.force:
            print(f"ERROR: {cursor_status['warning']}")
            print()
            print("Options:")
            print("  --cursor-stopped  : I confirm Cursor is not running")
            print("  --force           : Modify anyway (dangerous!)")
            print("  --dry-run         : Preview without modifying")
            return
        elif cursor_status["running"] and args.force:
            print(f"WARNING: {cursor_status['warning']}")
            print("Proceeding anyway (--force)")
            print()
    
    patterns = []
    
    # UUID pattern
    if args.uuids:
        patterns.append((
            re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', re.I),
            'uuid'
        ))
    
    # Secret patterns
    if args.secrets:
        patterns.extend([
            (re.compile(r'sk-[a-zA-Z0-9]{20,}'), 'openai_key'),
            (re.compile(r'sk-ant-[a-zA-Z0-9]{20,}'), 'anthropic_key'),
            (re.compile(r'AKIA[0-9A-Z]{16}'), 'aws_key'),
            (re.compile(r'ghp_[a-zA-Z0-9]{36}'), 'github_pat'),
            (re.compile(r'(?i)password[\s]*=[\s]*["\']?[^\s"\']{8,}'), 'password'),
            (re.compile(r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+'), 'jwt'),
        ])
    
    # Custom pattern
    if args.pattern:
        try:
            patterns.append((re.compile(args.pattern), 'custom'))
        except re.error as e:
            print(f"Invalid pattern: {e}")
            return
    
    if not patterns:
        print("No patterns specified. Use --secrets, --uuids, or --pattern")
        return
    
    mask_char = args.mask_char[0]  # Use first char only
    
    # Get files to process
    files_to_mask = []
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if os.path.isdir(trans_dir):
            for fname in os.listdir(trans_dir):
                if fname.endswith('.txt'):
                    if args.composer and not fname.startswith(args.composer):
                        continue
                    files_to_mask.append(os.path.join(trans_dir, fname))
    
    if not files_to_mask:
        print("No transcript files found")
        return
    
    print(f"Files to scan: {len(files_to_mask)}")
    print(f"Patterns: {len(patterns)}")
    print(f"Mask character: '{mask_char}'")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()
    
    total_masks = 0
    files_modified = 0
    
    for fpath in files_to_mask:
        # Check if file is in use
        if not args.dry_run and not args.force:
            file_status = is_file_in_use(fpath)
            if file_status["in_use"]:
                procs = ", ".join(file_status["processes"][:3])
                print(f"  SKIP {os.path.basename(fpath)}: in use by {procs}")
                continue
        
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
            continue
        
        original_size = len(content)
        original_content = content
        file_masks = 0
        
        # Find all matches and their positions
        all_matches = []
        for regex, ptype in patterns:
            for match in regex.finditer(content):
                all_matches.append({
                    'start': match.start(),
                    'end': match.end(),
                    'text': match.group(),
                    'type': ptype
                })
        
        # Sort by position (reverse to preserve offsets)
        all_matches.sort(key=lambda x: x['start'], reverse=True)
        
        # Apply masks
        for m in all_matches:
            masked = mask_char * len(m['text'])
            
            if args.dry_run:
                preview = m['text'][:20] + '...' if len(m['text']) > 20 else m['text']
                print(f"  Would mask [{m['type']}] len={len(m['text'])}: {preview}")
            
            content = content[:m['start']] + masked + content[m['end']:]
            file_masks += 1
        
        # Verify size unchanged
        if len(content) != original_size:
            print(f"  ERROR: Size mismatch in {fpath}! Original={original_size}, New={len(content)}")
            continue
        
        if file_masks > 0:
            total_masks += file_masks
            files_modified += 1
            
            if not args.dry_run:
                # Create backup
                if not args.no_backup:
                    backup_path = fpath + '.bak'
                    try:
                        with open(backup_path, 'w', encoding='utf-8') as f:
                            f.write(original_content)
                    except Exception as e:
                        print(f"  WARNING: Backup failed: {e}")
                        continue
                
                # Write masked content
                try:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  Masked {file_masks} items in {os.path.basename(fpath)} (size unchanged: {original_size})")
                except Exception as e:
                    print(f"  ERROR writing {fpath}: {e}")
    
    print()
    print(f"{'Would mask' if args.dry_run else 'Masked'}: {total_masks} items in {files_modified} files")
    print(f"File sizes: UNCHANGED")
    if args.dry_run:
        print("\nRun without --dry-run to apply")


def cmd_full_audit(args):
    """Full communication audit - ALL vectors in and out of Cursor.
    
    Vectors audited:
    - PROMPTS: User input sent to LLM
    - RESPONSES: LLM output (may echo secrets from context)
    - TOOL_CALLS: Arguments sent to tools
    - TOOL_RESULTS: Data returned from tools
    - MCP: MCP server communication
    - SHELL: Terminal commands executed
    - CONTEXT: Files mentioned/read as context
    - IMAGES: Image paths referenced
    - THINKING: Internal reasoning (may contain secrets)
    """
    import re
    from collections import defaultdict
    
    # Use the same comprehensive patterns
    AUDIT_PATTERNS = [
        # High-value secrets
        (r'sk-[a-zA-Z0-9]{20,}', 'openai_key', 'critical'),
        (r'sk-ant-[a-zA-Z0-9]{20,}', 'anthropic_key', 'critical'),
        (r'AKIA[0-9A-Z]{16}', 'aws_access_key', 'critical'),
        (r'ghp_[a-zA-Z0-9]{36}', 'github_pat', 'critical'),
        (r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', 'private_key', 'critical'),
        (r'(?i)password[\s]*[=:]+[\s]*["\']?[^\s"\']{8,}', 'password', 'high'),
        (r'(?i)api[_-]?key[\s]*[=:]+[\s]*["\']?[^\s"\']{16,}', 'api_key', 'high'),
        (r'https?://[^:/\s]+:[^@\s]+@[^\s]+', 'url_with_creds', 'critical'),
        (r'(?i)bearer\s+[a-zA-Z0-9\-_.]{20,}', 'bearer_token', 'high'),
        (r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+', 'jwt', 'high'),
        # Sensitive files
        (r'(?i)\.env(?:\.local|\.prod|\.dev)?(?:\s|$|")', 'env_file', 'high'),
        (r'(?i)credentials\.json', 'credentials_file', 'high'),
        (r'(?i)~/.ssh/id_rsa', 'ssh_key', 'critical'),
        (r'(?i)~/.aws/credentials', 'aws_creds_file', 'critical'),
    ]
    
    compiled = [(re.compile(p), n, s) for p, n, s in AUDIT_PATTERNS]
    
    # Vector-specific patterns
    shell_danger = re.compile(r'(?i)(curl|wget|ssh|scp|rsync|nc|netcat)\s+.*(-d|--data|@)', re.I)
    mcp_pattern = re.compile(r'\[Tool call\]\s+(cursor-ide-browser|user-\w+|mcp-\w+)', re.I)
    
    findings = defaultdict(list)
    stats = defaultdict(lambda: defaultdict(int))
    
    # Get transcripts
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    since_ts = parse_time_filter(args.since) if args.since else None
    vector_filter = set(args.vector.split(',')) if args.vector else None
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            if args.composer and not fname.startswith(args.composer):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            if since_ts:
                mtime = os.path.getmtime(fpath) * 1000
                if mtime < since_ts:
                    continue
            
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    lines = f.readlines()
            except:
                continue
            
            # State machine to track sections
            current_section = None
            section_start = 0
            section_content = []
            current_tool = None
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                lineno = i + 1
                
                # Detect section changes
                new_section = None
                if stripped == 'user:':
                    new_section = 'prompt'
                elif stripped == 'assistant:':
                    new_section = 'response'
                elif stripped.startswith('[Thinking]'):
                    new_section = 'thinking'
                elif stripped.startswith('[Tool call]'):
                    new_section = 'tool_call'
                    parts = stripped.split()
                    current_tool = parts[2] if len(parts) > 2 else 'unknown'
                    # Check if MCP
                    if mcp_pattern.match(stripped):
                        new_section = 'mcp'
                elif stripped.startswith('[Tool result]'):
                    new_section = 'tool_result'
                
                # Process previous section if section changed
                if new_section and current_section:
                    _audit_section(
                        current_section, '\n'.join(section_content),
                        compiled, shell_danger, findings, stats,
                        fpath, section_start, current_tool, args.limit, vector_filter
                    )
                
                if new_section:
                    current_section = new_section
                    section_start = lineno
                    section_content = []
                    if new_section not in ('tool_call', 'mcp'):
                        current_tool = None
                else:
                    section_content.append(line)
            
            # Process last section
            if current_section and section_content:
                _audit_section(
                    current_section, '\n'.join(section_content),
                    compiled, shell_danger, findings, stats,
                    fpath, section_start, current_tool, args.limit, vector_filter
                )
    
    # Also check context files from SQLite
    if not vector_filter or 'context' in vector_filter:
        global_db = os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage/state.vscdb")
        if os.path.isfile(global_db):
            try:
                conn = sqlite3.connect(f"file:{global_db}?mode=ro", uri=True)
                cursor = conn.cursor()
                
                # Get context/file references
                cursor.execute("""
                    SELECT key, value FROM cursorDiskKV 
                    WHERE key LIKE 'bubbleId:%' 
                    AND (value LIKE '%"context"%' OR value LIKE '%"files"%')
                    LIMIT 100
                """)
                
                for key, value in cursor.fetchall():
                    try:
                        # Scan for sensitive file paths
                        for regex, secret_type, severity in compiled:
                            for match in regex.finditer(value):
                                findings['context'].append({
                                    'path': key[:50],
                                    'line': 0,
                                    'type': secret_type,
                                    'severity': severity,
                                    'masked': match.group()[:20] + '...',
                                    'source': 'sqlite'
                                })
                                stats['context'][secret_type] += 1
                    except:
                        pass
                
                conn.close()
            except:
                pass
    
    # Output
    total = sum(len(v) for v in findings.values())
    
    if args.yaml:
        print(yaml.dump({
            'findings': dict(findings),
            'stats': {k: dict(v) for k, v in stats.items()},
            'total': total
        }, default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps({
            'findings': dict(findings),
            'stats': {k: dict(v) for k, v in stats.items()},
            'total': total
        }, indent=2))
    else:
        print("=" * 70)
        print("🔒 FULL COMMUNICATION AUDIT")
        print("=" * 70)
        print(f"Total findings: {total}")
        print()
        
        for vector in ['prompt', 'response', 'tool_call', 'tool_result', 'mcp', 'thinking', 'context']:
            vec_findings = findings.get(vector, [])
            if vec_findings or not args.summary:
                icon = {
                    'prompt': '📤', 'response': '📥', 'tool_call': '🔧',
                    'tool_result': '📋', 'mcp': '🔌', 'thinking': '💭', 'context': '📁'
                }.get(vector, '❓')
                print(f"{icon} {vector.upper()}: {len(vec_findings)} findings")
                
                if not args.summary:
                    for f in vec_findings[:10]:
                        sev_icon = {'critical': '🔴', 'high': '🟠', 'medium': '🟡'}.get(f['severity'], '⚪')
                        if f.get('source') == 'sqlite':
                            print(f"  {sev_icon} [sqlite] {f['type']}: {f['masked']}")
                        else:
                            print(f"  {sev_icon} {f['path']}:{f['line']} {f['type']}: {f['masked']}")
                    if len(vec_findings) > 10:
                        print(f"  ... and {len(vec_findings) - 10} more")
                print()


def cmd_url_audit(args):
    """Find URLs in tool calls, check for secrets (JOINs both stores)."""
    import re
    
    # Resolve composer reference (@1, prefix, name) to full ID
    composer_id = None
    if args.composer:
        composer_id = resolve_composer_id(args.composer)
        if not composer_id:
            print(f"Composer not found: {args.composer}", file=sys.stderr)
            return
    
    # URL pattern
    url_pattern = re.compile(r'https?://[^\s"\'\]}>]+')
    
    # Secret patterns in URLs
    url_secret_patterns = [
        (re.compile(r'[?&](?:api_?key|token|secret|password|auth|key)=([^&\s]+)', re.I), 'query_param_secret'),
        (re.compile(r'://[^:]+:([^@]+)@', re.I), 'basic_auth_password'),
        (re.compile(r'[?&]access_token=([^&\s]+)', re.I), 'access_token'),
        (re.compile(r'[?&]client_secret=([^&\s]+)', re.I), 'client_secret'),
        (re.compile(r'/v\d+/[a-f0-9]{32,}', re.I), 'embedded_key'),
    ]
    
    results = []
    
    # Source 1: Transcripts (plaintext)
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if not os.path.isdir(trans_dir):
            continue
        
        for fname in os.listdir(trans_dir):
            if not fname.endswith('.txt'):
                continue
            if composer_id and not fname.startswith(composer_id):
                continue
            
            fpath = os.path.join(trans_dir, fname)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    lines = f.readlines()
            except:
                continue
            
            in_tool = False
            tool_name = None
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                
                # Track if we're in a tool call section
                if stripped.startswith('[Tool call]'):
                    in_tool = True
                    parts = stripped.split()
                    tool_name = parts[2] if len(parts) > 2 else "unknown"
                elif stripped.startswith('[Tool result]'):
                    in_tool = True
                    tool_name = "result"
                elif stripped in ('user:', 'assistant:'):
                    in_tool = False
                
                # Find URLs
                for url_match in url_pattern.finditer(line):
                    url = url_match.group()
                    
                    # Check for secrets in URL
                    secrets_found = []
                    for secret_re, secret_type in url_secret_patterns:
                        if secret_re.search(url):
                            secrets_found.append(secret_type)
                    
                    # Check custom pattern
                    if args.pattern:
                        if not re.search(args.pattern, url, re.I):
                            if not secrets_found:
                                continue
                    
                    # Filter if secrets-only
                    if args.secrets_only and not secrets_found:
                        continue
                    
                    # Mask any secrets in URL for output
                    masked_url = url
                    for secret_re, _ in url_secret_patterns:
                        masked_url = secret_re.sub(lambda m: m.group(0).replace(m.group(1), '[REDACTED]') if m.groups() else '[REDACTED]', masked_url)
                    
                    results.append({
                        "source": "transcript",
                        "path": fpath,
                        "line": i + 1,
                        "tool": tool_name if in_tool else None,
                        "url": masked_url[:200],
                        "secrets": secrets_found if secrets_found else None,
                        "in_tool_call": in_tool,
                    })
                    
                    if len(results) >= args.limit:
                        break
            
            if len(results) >= args.limit:
                break
        if len(results) >= args.limit:
            break
    
    # Source 2: SQLite (structured tool calls) - if not at limit
    if len(results) < args.limit:
        global_db = os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage/state.vscdb")
        if os.path.isfile(global_db):
            try:
                conn = sqlite3.connect(f"file:{global_db}?mode=ro", uri=True)
                cursor = conn.cursor()
                
                # Search tool calls in bubbles
                cursor.execute("""
                    SELECT key, value FROM cursorDiskKV 
                    WHERE key LIKE 'bubbleId:%' 
                    AND (value LIKE '%http://%' OR value LIKE '%https://%')
                    LIMIT ?
                """, (args.limit - len(results),))
                
                for key, value in cursor.fetchall():
                    try:
                        data = json.loads(value)
                        text = json.dumps(data)
                        
                        for url_match in url_pattern.finditer(text):
                            url = url_match.group()
                            
                            secrets_found = []
                            for secret_re, secret_type in url_secret_patterns:
                                if secret_re.search(url):
                                    secrets_found.append(secret_type)
                            
                            if args.secrets_only and not secrets_found:
                                continue
                            
                            masked_url = url
                            for secret_re, _ in url_secret_patterns:
                                masked_url = secret_re.sub(lambda m: m.group(0).replace(m.group(1), '[REDACTED]') if m.groups() else '[REDACTED]', masked_url)
                            
                            results.append({
                                "source": "state.vscdb",
                                "key": key[:50],
                                "url": masked_url[:200],
                                "secrets": secrets_found if secrets_found else None,
                            })
                            
                            if len(results) >= args.limit:
                                break
                    except:
                        pass
                    
                    if len(results) >= args.limit:
                        break
                
                conn.close()
            except Exception as e:
                pass
    
    # Output
    if args.yaml:
        print(yaml.dump({"urls": results, "count": len(results)}, 
                       default_flow_style=False, sort_keys=False, allow_unicode=True))
    elif args.json:
        print(json.dumps({"urls": results, "count": len(results)}, indent=2))
    else:
        print(f"# URL Audit: {len(results)} URLs found")
        print(f"# Sources: transcripts (~/.cursor) + state.vscdb")
        secrets_count = sum(1 for r in results if r.get("secrets"))
        if secrets_count:
            print(f"# ⚠️  URLs with potential secrets: {secrets_count}")
        print()
        
        for r in results:
            if r["source"] == "transcript":
                loc = f"{r['path']}:{r['line']}"
                tool_info = f" [{r['tool']}]" if r.get("tool") else ""
            else:
                loc = r.get("key", "sqlite")
                tool_info = ""
            
            secret_flag = " 🔑" if r.get("secrets") else ""
            print(f"{loc}{tool_info}{secret_flag}")
            print(f"  {r['url']}")
            if r.get("secrets"):
                print(f"  ⚠️  {', '.join(r['secrets'])}")
            print()


def cmd_deep_snitch(args):
    """Deep Snitch - comprehensive security audit with K-REF output.

    Scans Cursor activity for:
    - Secrets (API keys, passwords, tokens)
    - Shell exfiltration (curl, wget, netcat, ssh)
    - Code execution (eval, exec, subprocess)
    - Dangerous paths (/etc/passwd, ~/.ssh, etc.)
    - Obfuscation (base64, hex, chr building)
    - Prompt injection attempts
    - Data exfiltration (webhooks, pastebin, file uploads)
    - Suspicious behavior (SSL bypass, cron, rm -rf)

    ⚠️  FALSE POSITIVE WARNING:
    If you scan a transcript where security code was written (like this script),
    the scanner will detect its own pattern definitions! Example:
      - Pattern `r'/etc/passwd'` in code → flagged as "etc_passwd access"
      - Pattern `-----BEGIN PRIVATE KEY-----` in docs → flagged as "private_key"
    
    This is the "Ouroboros effect". Look at actual line content to verify.
    Expect ~80% false positives when scanning security-focused sessions.

    Outputs K-REFs with severity levels for each finding.
    """
    import re
    from collections import defaultdict
    
    # Determine what to scan
    show_all = args.all
    show_patterns = args.patterns or args.all or args.category
    show_overview = args.endpoints or args.mcp or args.files or args.models or args.all
    
    # If nothing specified, do full audit
    if not (show_patterns or show_overview):
        show_all = True
        show_patterns = True
        show_overview = True
    
    # Severity filter
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    min_severity = severity_order.get(args.severity, 4) if args.severity else 4
    
    # Categories to scan
    if args.category:
        categories = [c.strip() for c in args.category.split(',')]
    else:
        categories = [
            "secrets", "shell_exfil", "code_execution", "dangerous_paths",
            "obfuscation", "prompt_injection", "data_exfil", "suspicious_behavior"
        ]
    
    findings = []
    stats = defaultdict(lambda: defaultdict(int))
    
    # Pattern scanning
    if show_patterns:
        # Resolve composer reference (@1, prefix, name) to full ID
        composer_id = None
        if args.composer:
            composer_id = resolve_composer_id(args.composer)
            if not composer_id:
                print(f"Composer not found: {args.composer}", file=sys.stderr)
                return
        
        runner = AuditRunner()
        runner.add_surface(TranscriptSurface(
            workspace=args.workspace,
            composer=composer_id
        ))
        
        # Add requested pattern categories
        for cat in categories:
            if cat == "all":
                for pset in PATTERN_REGISTRY.keys():
                    runner.add_pattern_set(pset)
            elif cat in PATTERN_REGISTRY:
                runner.add_pattern_set(cat)
        
        # Scan (collect all, filter later for proper severity prioritization)
        all_findings = list(runner.scan(limit=10000))
        
        # Sort by severity (critical first) then filter
        all_findings.sort(key=lambda f: severity_order.get(f.severity.value, 4))
        
        for finding in all_findings:
            sev_level = severity_order.get(finding.severity.value, 4)
            if sev_level <= min_severity:
                findings.append(finding)
                stats["severity"][finding.severity.value] += 1
                stats["category"][finding.category] += 1
                stats["pattern"][finding.pattern_name] += 1
            # Apply limit per output, not per scan
            if len(findings) >= args.limit * 10:  # generous buffer
                break
    
    # Overview data
    report = {
        "endpoints": [],
        "mcp_servers": [],
        "models_used": defaultdict(int),
        "files_exposed": set(),
        "tool_calls": defaultdict(int),
        "data_volume": {"prompts": 0, "responses": 0},
    }
    
    if show_overview:
        # Check configured endpoints
        mcp_json = os.path.join(DOTCURSOR_BASE, "mcp.json")
        if os.path.isfile(mcp_json):
            try:
                with open(mcp_json, 'r') as f:
                    mcp_config = json.load(f)
                for server_name, server_config in mcp_config.get("mcpServers", {}).items():
                    cmd = server_config.get("command", "")
                    report["endpoints"].append({
                        "type": "mcp_server",
                        "name": server_name,
                        "command": cmd
                    })
            except:
                pass
        
        # Scan transcripts for overview
        workspaces = get_dotcursor_workspaces()
        if args.workspace:
            workspaces = [ws for ws in workspaces if args.workspace in ws.get("name", "")]
        
        since_ts = parse_time_filter(args.since) if args.since else None
        file_pattern = re.compile(r'(?:path|file)["\s:]+([/\w\-_.]+\.[a-z]{1,5})', re.I)
        model_pattern = re.compile(r'(claude-[a-z0-9\-_.]+|gpt-[a-z0-9\-_.]+|gemini-[a-z0-9\-_.]+)', re.I)
        
        for ws in workspaces:
            trans_dir = os.path.join(ws["path"], "agent-transcripts")
            if not os.path.isdir(trans_dir):
                continue
            
            for fname in os.listdir(trans_dir):
                if not fname.endswith('.txt'):
                    continue
                if args.composer and not fname.startswith(args.composer):
                    continue
                
                fpath = os.path.join(trans_dir, fname)
                if since_ts and os.path.getmtime(fpath) * 1000 < since_ts:
                    continue
                
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                except:
                    continue
                
                # Extract stats
                for match in file_pattern.finditer(content):
                    report["files_exposed"].add(match.group(1))
                for match in model_pattern.finditer(content):
                    report["models_used"][match.group(1).lower()] += 1
    
    # Convert for output
    report["files_exposed"] = sorted(report["files_exposed"])[:50]
    report["models_used"] = dict(report["models_used"])
    
    # Output
    if args.yaml:
        output = {
            "findings": [{
                "kref": f.to_kref(),
                "severity": f.severity.value,
                "category": f.category,
                "pattern": f.pattern_name,
                "description": f.description,
                "redact_label": f.redact_label,
                "matched": f.matched
            } for f in findings],
            "stats": {
                "total": len(findings),
                "by_severity": dict(stats["severity"]),
                "by_category": dict(stats["category"]),
            },
            "overview": report if show_overview else None
        }
        print(yaml.dump(output, default_flow_style=False, allow_unicode=True))
        
    elif args.json:
        output = {
            "findings": [{
                "path": f.path, "line": f.line,
                "col_start": f.col_start, "col_end": f.col_end,
                "severity": f.severity.value,
                "category": f.category,
                "pattern": f.pattern_name,
                "description": f.description,
                "redact_label": f.redact_label,
                "matched": f.matched
            } for f in findings],
            "stats": {
                "total": len(findings),
                "by_severity": dict(stats["severity"]),
                "by_category": dict(stats["category"]),
            },
            "overview": report if show_overview else None
        }
        print(json.dumps(output, indent=2))
        
    else:
        # K-REF output with logging levels
        sev_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🔵", "info": "ℹ️"}
        sev_label = {"critical": "CRITICAL", "high": "HIGH", "medium": "MEDIUM", "low": "LOW", "info": "INFO"}
        
        print("DEEP SNITCH REPORT")
        print(f"Categories: {', '.join(categories)}")
        if args.composer:
            print(f"Composer: {args.composer}")
        if args.since:
            print(f"Since: {args.since}")
        print()
        
        # Summary first
        if not args.summary:
            print(f"Total findings: {len(findings)}")
            if stats["severity"]:
                sev_str = ", ".join(f"{sev_icon.get(k, '?')} {k}={v}" for k, v in 
                                   sorted(stats["severity"].items(), key=lambda x: severity_order.get(x[0], 99)))
                print(f"By severity: {sev_str}")
            print()
        
        # Group by severity for output
        if not args.summary:
            for sev in ["critical", "high", "medium", "low", "info"]:
                sev_findings = [f for f in findings if f.severity.value == sev]
                if not sev_findings:
                    continue
                
                print(f"{sev_icon.get(sev, '?')} {sev_label.get(sev, sev).upper()} ({len(sev_findings)})")
                print("-" * 60)
                
                for f in sev_findings[:args.limit // 5]:  # Limit per severity
                    print(f.to_kref())
                    # Truncate matched for display
                    matched_display = f.matched
                    if len(matched_display) > 80:
                        matched_display = matched_display[:40] + "..." + matched_display[-30:]
                    print(f"  {matched_display}")
                
                if len(sev_findings) > args.limit // 5:
                    print(f"  ... and {len(sev_findings) - args.limit // 5} more {sev} findings")
                print()
        
        # Overview section
        if show_overview and not args.summary:
            print("OVERVIEW")
            print("-" * 60)
            
            if report["endpoints"]:
                print(f"MCP Endpoints: {len(report['endpoints'])}")
                for ep in report["endpoints"][:5]:
                    print(f"  {ep['name']} → {ep.get('command', '?')}")
            
            if report["models_used"]:
                print(f"Models used: {', '.join(list(report['models_used'].keys())[:5])}")
            
            if report["files_exposed"]:
                print(f"Files exposed: {len(report['files_exposed'])} files")
        
        # Summary stats
        print()
        print("SUMMARY")
        print("-" * 60)
        critical = stats["severity"].get("critical", 0)
        high = stats["severity"].get("high", 0)
        medium = stats["severity"].get("medium", 0)
        
        if critical > 0:
            print(f"🔴 {critical} CRITICAL findings - immediate attention required!")
        if high > 0:
            print(f"🟠 {high} HIGH findings - review recommended")
        if medium > 0:
            print(f"🟡 {medium} MEDIUM findings - consider reviewing")
        
        if critical == 0 and high == 0:
            print("✅ No critical or high severity findings")
        
        # Top patterns
        if stats["pattern"]:
            top_patterns = sorted(stats["pattern"].items(), key=lambda x: -x[1])[:5]
            print(f"\nTop patterns: {', '.join(f'{p}({c})' for p, c in top_patterns)}")


def cmd_commits(args):
    """Find git commits mentioned in transcripts using K-REFS output."""
    import re
    
    # Patterns for git commits
    commit_patterns = [
        (re.compile(r'\b([0-9a-f]{40})\b'), 'full_sha'),
        (re.compile(r'\b([0-9a-f]{7,12})\b(?=\s|$|[^0-9a-f])'), 'short_sha'),
        (re.compile(r'commit\s+([0-9a-f]{7,40})', re.I), 'commit_ref'),
        (re.compile(r'git\s+(?:checkout|cherry-pick|revert|show)\s+([0-9a-f]{7,40})', re.I), 'git_cmd'),
    ]
    
    # Get files to scan
    files_to_scan = []
    workspaces = get_dotcursor_workspaces()
    if args.workspace:
        workspaces = [ws for ws in workspaces if args.workspace in ws["name"]]
    
    for ws in workspaces:
        trans_dir = os.path.join(ws["path"], "agent-transcripts")
        if os.path.isdir(trans_dir):
            for fname in os.listdir(trans_dir):
                if fname.endswith('.txt'):
                    if args.composer and not fname.startswith(args.composer):
                        continue
                    files_to_scan.append(os.path.join(trans_dir, fname))
    
    matches = []
    seen_commits = set()
    
    for fpath in files_to_scan:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except:
            continue
        
        for i, line in enumerate(lines):
            line_stripped = line.rstrip('\n\r')
            lineno = i + 1
            
            for regex, commit_type in commit_patterns:
                for match in regex.finditer(line_stripped):
                    sha = match.group(1)
                    # Skip if looks like a UUID or other non-commit hash
                    if '-' in sha:
                        continue
                    # Dedupe
                    if sha[:12] in seen_commits:
                        continue
                    seen_commits.add(sha[:12])
                    
                    context_preview = line_stripped[:100]
                    
                    matches.append({
                        "path": fpath,
                        "line": lineno,
                        "sha": sha[:12],
                        "full_sha": sha if len(sha) == 40 else None,
                        "type": commit_type,
                        "context": context_preview
                    })
                    
                    if len(matches) >= args.limit:
                        break
            
            if len(matches) >= args.limit:
                break
        if len(matches) >= args.limit:
            break
    
    # Output
    if args.yaml:
        print(yaml.dump({"commits": matches, "count": len(matches)}, 
                       default_flow_style=False, sort_keys=False))
    elif args.json:
        print(json.dumps({"commits": matches, "count": len(matches)}, indent=2))
    elif args.refs_only:
        for m in matches:
            print(f"{m['path']}:{m['line']}-{m['line']} # {m['type']} | {m['sha']}")
    else:
        print(f"# Git Commits Found: {len(matches)}")
        print()
        for m in matches:
            print(f"{m['path']}:{m['line']} # {m['type']} | {m['sha']} | {m['context'][:60]}")

