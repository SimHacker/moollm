#!/usr/bin/env python3
"""
moopmap.py — MOOLLM Semantic Mipmap Analyzer

Analyzes the GLANCE.yml semantic compression pyramid across the MOOLLM repo.
Measures how much context is captured at each resolution level.

Usage:
    python3 moopmap.py                    # Run from moollm repo root
    python3 moopmap.py /path/to/moollm    # Specify repo path
    python3 moopmap.py --output analysis.yml  # Custom output file

Output: YAML analysis file (default: designs/glance-mipmap-analysis.yml)

The "moopmap" is a semantic mipmap — like image pyramids in computer graphics,
but for meaning. GLANCE files compress directories into fast-loading summaries.
This script measures that compression. The name is a portmanteau of MOO + mipmap,
honoring the LambdaMOO heritage. It sounds funnier than "moomap".

Key metrics:
- Width: top-level files + dirs (branching factor at each node)
- Direct text: bytes of .md/.yml/.yaml/.txt files in dir (not recursive)
- Compression: ratio of direct text to GLANCE bytes
"""

import os
import subprocess
import statistics
import sys
import yaml
from datetime import datetime
from pathlib import Path


def get_file_size(path: str) -> int:
    """Get file size in bytes, 0 if not exists."""
    try:
        return os.path.getsize(path)
    except (OSError, IOError):
        return 0


def get_line_count(path: str) -> int:
    """Count lines in file, 0 if not exists."""
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except (OSError, IOError):
        return 0


def get_width(dir_path: str) -> dict:
    """Count top-level files and dirs (not recursive) — the branching factor."""
    try:
        entries = os.listdir(dir_path)
        files = [e for e in entries if os.path.isfile(os.path.join(dir_path, e))]
        dirs = [e for e in entries if os.path.isdir(os.path.join(dir_path, e))]
        return {'files': len(files), 'dirs': len(dirs), 'total': len(entries)}
    except (OSError, IOError):
        return {'files': 0, 'dirs': 0, 'total': 0}


def get_direct_text_size(dir_path: str) -> int:
    """Sum of text files directly in this dir (not recursive)."""
    total = 0
    text_extensions = ('.md', '.yml', '.yaml', '.txt')
    try:
        for f in os.listdir(dir_path):
            fp = os.path.join(dir_path, f)
            if os.path.isfile(fp) and f.endswith(text_extensions):
                total += get_file_size(fp)
    except (OSError, IOError):
        pass
    return total


def categorize_path(glance_path: str) -> str:
    """Determine category from GLANCE path."""
    if '/skills/' in glance_path:
        return 'skill'
    elif '/characters/' in glance_path:
        return 'character'
    elif any(x in glance_path for x in [
        '/pub/', '/maze/', '/street/', '/garden/', '/kitchen/', 
        '/coatroom/', '/forest/', '/home/', '/end/', '/basement/',
        '/stage/', '/attic/', '/lobby/', '/rooftop/'
    ]):
        return 'room'
    return 'other'


def compute_stats(entries: list) -> dict:
    """Compute statistics for a list of entries."""
    if not entries:
        return {}
    
    def safe_stats(values):
        return {
            'min': min(values),
            'max': max(values),
            'mean': round(statistics.mean(values)),
            'median': round(statistics.median(values)),
        }
    
    return {
        'count': len(entries),
        'glance_bytes': {
            'total': sum(e['glance_bytes'] for e in entries),
            **safe_stats([e['glance_bytes'] for e in entries]),
        },
        'glance_lines': {
            'total': sum(e['glance_lines'] for e in entries),
            'min': min(e['glance_lines'] for e in entries),
            'max': max(e['glance_lines'] for e in entries),
            'mean': round(statistics.mean([e['glance_lines'] for e in entries]), 1),
            'median': round(statistics.median([e['glance_lines'] for e in entries]), 1),
        },
        'width_files': {
            'min': min(e['width_files'] for e in entries),
            'max': max(e['width_files'] for e in entries),
            'mean': round(statistics.mean([e['width_files'] for e in entries]), 1),
            'median': round(statistics.median([e['width_files'] for e in entries]), 1),
        },
        'width_dirs': {
            'min': min(e['width_dirs'] for e in entries),
            'max': max(e['width_dirs'] for e in entries),
            'mean': round(statistics.mean([e['width_dirs'] for e in entries]), 1),
            'median': round(statistics.median([e['width_dirs'] for e in entries]), 1),
        },
        'direct_text_bytes': {
            'total': sum(e['direct_text_bytes'] for e in entries),
            'mean': round(statistics.mean([e['direct_text_bytes'] for e in entries])),
            'median': round(statistics.median([e['direct_text_bytes'] for e in entries])),
        },
    }


def analyze_moollm(base_path: str) -> dict:
    """Run the full moomap analysis."""
    base = Path(base_path).resolve()
    
    # Find all GLANCE.yml files
    result = subprocess.run(
        ['find', '.', '-name', 'GLANCE.yml', '-type', 'f'],
        capture_output=True, text=True, cwd=base
    )
    glance_files = [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]
    
    # Repo-wide text stats
    total_text_bytes = 0
    total_text_files = 0
    exclude_dirs = {'temp', '.git', 'node_modules', 'dist', '__pycache__', '.moollm'}
    text_extensions = ('.md', '.yml', '.yaml', '.txt')
    
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in files:
            if f.endswith(text_extensions):
                fp = os.path.join(root, f)
                total_text_bytes += get_file_size(fp)
                total_text_files += 1
    
    # Analyze each GLANCE
    all_entries = []
    skill_entries = []
    room_entries = []
    char_entries = []
    
    for glance_path in glance_files:
        dir_path = os.path.dirname(glance_path)
        full_dir = base / dir_path
        full_glance = base / glance_path
        
        glance_bytes = get_file_size(full_glance)
        glance_lines = get_line_count(full_glance)
        width = get_width(full_dir)
        direct_text = get_direct_text_size(full_dir)
        
        # Related files
        card_bytes = get_file_size(full_dir / 'CARD.yml')
        skill_md_bytes = get_file_size(full_dir / 'SKILL.md')
        readme_bytes = get_file_size(full_dir / 'README.md')
        
        category = categorize_path(glance_path)
        
        entry = {
            'path': dir_path,
            'category': category,
            'glance_bytes': glance_bytes,
            'glance_lines': glance_lines,
            'width_files': width['files'],
            'width_dirs': width['dirs'],
            'width_total': width['total'],
            'direct_text_bytes': direct_text,
            'card_bytes': card_bytes,
            'skill_md_bytes': skill_md_bytes,
            'readme_bytes': readme_bytes,
        }
        
        all_entries.append(entry)
        if category == 'skill':
            skill_entries.append(entry)
        elif category == 'room':
            room_entries.append(entry)
        elif category == 'character':
            char_entries.append(entry)
    
    # Skill pyramid stats
    skill_with_card = [e for e in skill_entries if e['card_bytes'] > 0]
    skill_with_skill_md = [e for e in skill_entries if e['skill_md_bytes'] > 0]
    skill_with_readme = [e for e in skill_entries if e['readme_bytes'] > 0]
    
    # Sort for top-N lists
    sorted_by_width = sorted(all_entries, key=lambda x: x['width_total'], reverse=True)
    sorted_skills_by_direct = sorted(skill_entries, key=lambda x: x['direct_text_bytes'], reverse=True)
    
    # Compute skill pyramid ratios
    avg_glance = statistics.mean([e['glance_bytes'] for e in skill_entries]) if skill_entries else 1
    
    # Build output
    output = {
        'meta': {
            'description': 'GLANCE.yml semantic mipmap analysis — the moomap',
            'generated': datetime.now().strftime('%Y-%m-%d'),
            'methodology': 'Direct file counts only (no recursive du -s). Width = top-level files + dirs.',
            'script': 'skills/moollm/scripts/moopmap.py',
        },
        'repo_summary': {
            'total_text_files': total_text_files,
            'total_text_mb': round(total_text_bytes / 1024 / 1024, 1),
            'total_glance_files': len(glance_files),
            'total_glance_kb': round(sum(e['glance_bytes'] for e in all_entries) / 1024, 1),
            'glance_percent_of_text': round(100 * sum(e['glance_bytes'] for e in all_entries) / total_text_bytes, 2) if total_text_bytes else 0,
        },
        'by_category': {
            'skills': compute_stats(skill_entries),
            'rooms': compute_stats(room_entries),
            'characters': compute_stats(char_entries),
            'all': compute_stats(all_entries),
        },
        'skill_pyramid': {
            'description': 'Average bytes per semantic resolution level (direct files only)',
            'count': len(skill_entries),
            'avg_glance_bytes': round(avg_glance),
            'avg_card_bytes': round(statistics.mean([e['card_bytes'] for e in skill_with_card])) if skill_with_card else 0,
            'avg_skill_md_bytes': round(statistics.mean([e['skill_md_bytes'] for e in skill_with_skill_md])) if skill_with_skill_md else 0,
            'avg_readme_bytes': round(statistics.mean([e['readme_bytes'] for e in skill_with_readme])) if skill_with_readme else 0,
            'avg_direct_text_bytes': round(statistics.mean([e['direct_text_bytes'] for e in skill_entries])) if skill_entries else 0,
            'ratios': {
                'direct_to_glance': round(statistics.mean([e['direct_text_bytes'] for e in skill_entries]) / avg_glance, 1) if skill_entries else 0,
                'card_to_glance': round(statistics.mean([e['card_bytes'] for e in skill_with_card]) / avg_glance, 1) if skill_with_card else 0,
                'skill_md_to_glance': round(statistics.mean([e['skill_md_bytes'] for e in skill_with_skill_md]) / avg_glance, 1) if skill_with_skill_md else 0,
            }
        },
        'top_10_widest_dirs': [
            {
                'path': e['path'],
                'files': e['width_files'],
                'dirs': e['width_dirs'],
                'total': e['width_total'],
                'glance_lines': e['glance_lines']
            }
            for e in sorted_by_width[:10]
        ],
        'top_10_skills_by_content': [
            {
                'path': e['path'].replace('./skills/', ''),
                'direct_text_bytes': e['direct_text_bytes'],
                'glance_bytes': e['glance_bytes'],
                'width': e['width_total']
            }
            for e in sorted_skills_by_direct[:10]
        ],
    }
    
    return output


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='MOOLLM Semantic Mipmap Analyzer (moopmap)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('repo_path', nargs='?', default='.',
                        help='Path to moollm repo (default: current dir)')
    parser.add_argument('--output', '-o', 
                        help='Output file (default: designs/glance-mipmap-analysis.yml)')
    
    args = parser.parse_args()
    
    # Resolve paths
    base = Path(args.repo_path).resolve()
    if not (base / 'skills').exists():
        print(f"Error: {base} doesn't look like a moollm repo (no skills/ dir)")
        sys.exit(1)
    
    output_path = args.output or (base / 'designs' / 'glance-mipmap-analysis.yml')
    
    # Run analysis
    print(f"Analyzing GLANCE mipmap in {base}...")
    result = analyze_moollm(base)
    
    # Write output
    with open(output_path, 'w') as f:
        yaml.dump(result, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=120)
    
    # Print summary
    print(f"\nMoopmap complete!")
    print(f"  Text files: {result['repo_summary']['total_text_files']}")
    print(f"  Text size: {result['repo_summary']['total_text_mb']} MB")
    print(f"  GLANCE files: {result['repo_summary']['total_glance_files']}")
    print(f"  GLANCE size: {result['repo_summary']['total_glance_kb']} KB")
    print(f"  Compression: {result['repo_summary']['glance_percent_of_text']:.2f}% of text")
    print(f"\nWritten to: {output_path}")


if __name__ == '__main__':
    main()
