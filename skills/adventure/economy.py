#!/usr/bin/env python3
"""
economy.py — MOOTAL DISTORTION Economy Analyzer

Analyzes character wealth from YAML files or compiled world.json.
Can be run standalone or called as a module.

Usage:
    python3 economy.py                          # Analyze from world.json
    python3 economy.py --yaml examples/adventure-4  # Analyze from YAML
    python3 economy.py --json                   # Output as JSON
    python3 economy.py --brief                  # Short summary only
"""

import argparse
import json
import random
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def load_characters_from_json(world_path: Path) -> list:
    """Load characters from compiled world.json"""
    with open(world_path) as f:
        world = json.load(f)
    
    chars = []
    for id, obj in world.get('registry', {}).items():
        if id.startswith('character/'):
            chars.append({
                'id': id,
                'name': obj.get('name', id.split('/')[-1]),
                'gold': obj.get('gold', 0),
                'moolah': obj.get('moolah', 0),
                'tags': obj.get('tags', []),
                'species': obj.get('species', 'unknown')
            })
    return chars


def load_characters_from_yaml(adventure_path: Path) -> list:
    """Load characters directly from CHARACTER.yml files"""
    if yaml is None:
        print("Error: PyYAML not installed. Run: pip install pyyaml")
        sys.exit(1)
    
    chars = []
    for char_file in adventure_path.rglob('CHARACTER.yml'):
        try:
            with open(char_file) as f:
                data = yaml.safe_load(f)
            
            # Extract character data
            char_data = data.get('character', data.get('player', {}))
            ontology = data.get('ontology', {})
            
            # Generate currency if not present (same logic as compiler)
            gold = data.get('gold', char_data.get('gold', random.randint(50, 500)))
            moolah = data.get('moolah', char_data.get('moolah', random.randint(100, 1000)))
            
            chars.append({
                'id': str(char_file.relative_to(adventure_path)),
                'name': char_data.get('name', char_file.parent.name),
                'gold': gold,
                'moolah': moolah,
                'tags': ontology.get('tags', []),
                'species': ontology.get('species', 'unknown')
            })
        except Exception as e:
            print(f"Warning: Could not load {char_file}: {e}", file=sys.stderr)
    
    return chars


def calculate_gini(values: list) -> float:
    """Calculate Gini coefficient (0 = equality, 1 = inequality)"""
    if not values or sum(values) == 0:
        return 0.0
    
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    total = sum(sorted_vals)
    
    numerator = sum((2 * (i + 1) - n - 1) * val for i, val in enumerate(sorted_vals))
    return round(numerator / (n * total), 3)


def analyze_economy(chars: list) -> dict:
    """Analyze economy from character list"""
    if not chars:
        return {'error': 'No characters found'}
    
    # Add total wealth
    for c in chars:
        c['total'] = c['gold'] + c['moolah']
    
    # Basic stats
    total_gold = sum(c['gold'] for c in chars)
    total_moolah = sum(c['moolah'] for c in chars)
    total_wealth = total_gold + total_moolah
    
    # Sort by wealth
    by_wealth = sorted(chars, key=lambda c: c['total'], reverse=True)
    
    # Species breakdown
    species_wealth = {}
    for c in chars:
        sp = c['species'] or 'unknown'
        if sp not in species_wealth:
            species_wealth[sp] = {'gold': 0, 'moolah': 0, 'count': 0, 'names': []}
        species_wealth[sp]['gold'] += c['gold']
        species_wealth[sp]['moolah'] += c['moolah']
        species_wealth[sp]['count'] += 1
        species_wealth[sp]['names'].append(c['name'])
    
    # Category breakdown
    categories = {'animals': [], 'fictional': [], 'abstract': [], 'real-people': []}
    for c in chars:
        for cat in categories:
            if cat in c['tags'] or cat.replace('-', '_') in c['id']:
                categories[cat].append(c)
    
    # Wealth distribution stats
    wealth_values = [c['total'] for c in chars]
    avg_wealth = total_wealth // len(chars)
    median_wealth = by_wealth[len(chars) // 2]['total']
    gini = calculate_gini(wealth_values)
    
    # Currency preferences
    gold_lovers = sum(1 for c in chars if c['gold'] > c['moolah'])
    moolah_lovers = sum(1 for c in chars if c['moolah'] > c['gold'])
    
    return {
        'population': len(chars),
        'total_gold': total_gold,
        'total_moolah': total_moolah,
        'total_wealth': total_wealth,
        'avg_wealth': avg_wealth,
        'median_wealth': median_wealth,
        'gini_index': gini,
        'richest': by_wealth[:5],
        'poorest': by_wealth[-3:][::-1],
        'species_wealth': species_wealth,
        'categories': {k: len(v) for k, v in categories.items()},
        'category_wealth': {k: sum(c['total'] for c in v) for k, v in categories.items()},
        'gold_lovers': gold_lovers,
        'moolah_lovers': moolah_lovers,
        'all_chars': by_wealth
    }


def format_report(e: dict) -> str:
    """Format economy analysis as human-readable report"""
    report = f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  💰 MOOTAL DISTORTION ECONOMY REPORT 💰                                        ║
║  "Where gold becomes ale and ale becomes courage"                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝

📊 OVERVIEW
   Population: {e['population']} characters
   Total Gold: {e['total_gold']:,} 🪙
   Total Moolah: {e['total_moolah']:,} 💸
   Combined GDP: {e['total_wealth']:,}

📈 WEALTH DISTRIBUTION
   Average Wealth: {e['avg_wealth']:,} per character
   Median Wealth: {e['median_wealth']:,}
   Gini Index: {e['gini_index']} (0=equal, 1=unequal)
   Assessment: {'✨ Fairly equal society!' if e['gini_index'] < 0.3 else '⚖️ Moderate inequality' if e['gini_index'] < 0.5 else '⚠️ High inequality!'}

🏆 THE WEALTHY ELITE (Top 5)
"""
    for i, c in enumerate(e['richest'], 1):
        report += f"   {i}. {c['name']:<25} {c['gold']:>4} 🪙 + {c['moolah']:>4} 💸 = {c['total']:>5}\n"
    
    report += "\n😢 THE STRUGGLING (Bottom 3)\n"
    for c in e['poorest']:
        report += f"   • {c['name']:<25} {c['gold']:>4} 🪙 + {c['moolah']:>4} 💸 = {c['total']:>5}\n"
    
    report += "\n🐾 WEALTH BY SPECIES\n"
    species_sorted = sorted(
        e['species_wealth'].items(),
        key=lambda x: x[1]['gold'] + x[1]['moolah'],
        reverse=True
    )
    for species, data in species_sorted[:8]:
        total = data['gold'] + data['moolah']
        avg = total // data['count'] if data['count'] > 0 else 0
        report += f"   {species:<12} {data['count']:>2} chars, {total:>5} total (avg {avg:>4})\n"
    
    report += f"""
📂 WEALTH BY CATEGORY
   Animals: {e['category_wealth'].get('animals', 0):,} ({e['categories'].get('animals', 0)} chars)
   Fictional: {e['category_wealth'].get('fictional', 0):,} ({e['categories'].get('fictional', 0)} chars)
   Real People: {e['category_wealth'].get('real-people', 0):,} ({e['categories'].get('real-people', 0)} chars)
   Abstract: {e['category_wealth'].get('abstract', 0):,} ({e['categories'].get('abstract', 0)} chars)

💱 CURRENCY PREFERENCES
   Gold traditionalists: {e['gold_lovers']} characters prefer 🪙
   Moolah modernists: {e['moolah_lovers']} characters prefer 💸
   Economy type: {'📱 Modern/tech-forward!' if e['moolah_lovers'] > e['gold_lovers'] else '🏰 Traditional values!'}

═══════════════════════════════════════════════════════════════════════════════════
"""
    return report.strip()


def format_brief(e: dict) -> str:
    """Short summary for embedding in other outputs"""
    return f"""💰 Economy: {e['population']} characters | {e['total_gold']:,}🪙 + {e['total_moolah']:,}💸 = {e['total_wealth']:,} total
   Richest: {e['richest'][0]['name']} ({e['richest'][0]['total']}) | Gini: {e['gini_index']}"""


def main():
    parser = argparse.ArgumentParser(description='Analyze MOOTAL DISTORTION economy')
    parser.add_argument('--yaml', type=Path, help='Path to adventure YAML directory')
    parser.add_argument('--world', type=Path, default=Path(__file__).parent / 'dist/world.json',
                        help='Path to compiled world.json')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--brief', action='store_true', help='Short summary only')
    
    args = parser.parse_args()
    
    # Load characters
    if args.yaml:
        chars = load_characters_from_yaml(args.yaml)
        print(f"📁 Loaded {len(chars)} characters from YAML", file=sys.stderr)
    else:
        if not args.world.exists():
            print(f"Error: {args.world} not found. Run compiler first or use --yaml")
            sys.exit(1)
        chars = load_characters_from_json(args.world)
        print(f"📁 Loaded {len(chars)} characters from world.json", file=sys.stderr)
    
    # Analyze
    economy = analyze_economy(chars)
    
    # Output
    if args.json:
        # Remove non-serializable bits
        output = {k: v for k, v in economy.items() if k != 'all_chars'}
        print(json.dumps(output, indent=2))
    elif args.brief:
        print(format_brief(economy))
    else:
        print(format_report(economy))


if __name__ == '__main__':
    main()
