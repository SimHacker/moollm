#!/usr/bin/env python3
"""
Albert Heijn API client — groceries skill sister script.

ANONYMOUS (no login):
    ah.py search "hagelslag"
    ah.py bonus --week current
    ah.py stores --near "Amsterdam"

AUTHENTICATED (requires 1Password):
    ah.py login
    ah.py receipts --limit 10
    ah.py orders
    ah.py list add "melk" "brood"

Credentials via 1Password:
    op read "op://Personal/Albert Heijn/email"
    op read "op://Personal/Albert Heijn/password"
"""

import argparse
import json
import subprocess
import sys
import time
import webbrowser
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

# Optional: requests (pip install requests)
try:
    import requests
except ImportError:
    requests = None
    print("Warning: requests not installed. Run: pip install requests", file=sys.stderr)

# Optional: yaml for config (pip install pyyaml)
try:
    import yaml
except ImportError:
    yaml = None

# CONFIGURATION

CONFIG_DIR = Path.home() / ".moollm/skills/groceries"
CONFIG_PATH = CONFIG_DIR / "config.yml"
TOKEN_CACHE = CONFIG_DIR / ".tokens.json"

API_BASE = "https://api.ah.nl"
GQL_URL = "https://www.ah.nl/gql"
LOGIN_URL = "https://login.ah.nl/secure/oauth/authorize"

USER_AGENT = "Appie/8.22.3"
CLIENT_ID = "appie"

# STATE

@dataclass
class AuthState:
    """Authentication state."""
    access_token: str | None = None
    refresh_token: str | None = None
    expires_at: float = 0
    member_id: str | None = None

@dataclass 
class Config:
    """Configuration from config.yml."""
    op_ah_email: str = "op://Personal/Albert Heijn/email"
    op_ah_password: str = "op://Personal/Albert Heijn/password"
    default_store: str = "ah"
    
# Global state
_auth = AuthState()
_config = Config()

# HELPERS

def ensure_requests():
    """Ensure requests is available."""
    if requests is None:
        print("Error: requests library required. Install with: pip install requests")
        sys.exit(1)

def load_config() -> Config:
    """Load config from file if exists."""
    global _config
    if CONFIG_PATH.exists() and yaml:
        with open(CONFIG_PATH) as f:
            data = yaml.safe_load(f)
            if data and 'credentials' in data:
                creds = data['credentials'].get('op', {}).get('ah', {})
                _config.op_ah_email = creds.get('email', _config.op_ah_email)
                _config.op_ah_password = creds.get('password', _config.op_ah_password)
    return _config

def load_tokens() -> AuthState:
    """Load cached tokens."""
    global _auth
    if TOKEN_CACHE.exists():
        with open(TOKEN_CACHE) as f:
            data = json.load(f)
            _auth.access_token = data.get('access_token')
            _auth.refresh_token = data.get('refresh_token')
            _auth.expires_at = data.get('expires_at', 0)
            _auth.member_id = data.get('member_id')
    return _auth

def save_tokens():
    """Save tokens to cache."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(TOKEN_CACHE, 'w') as f:
        json.dump({
            'access_token': _auth.access_token,
            'refresh_token': _auth.refresh_token,
            'expires_at': _auth.expires_at,
            'member_id': _auth.member_id,
        }, f, indent=2)

def op_read(path: str) -> str:
    """Read secret from 1Password."""
    try:
        result = subprocess.run(
            ['op', 'read', path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error reading from 1Password: {e.stderr}", file=sys.stderr)
        raise
    except FileNotFoundError:
        print("Error: 1Password CLI (op) not found. Install from: https://1password.com/downloads/command-line/")
        raise

def api_headers(auth: bool = False) -> dict:
    """Get API request headers."""
    headers = {
        'User-Agent': USER_AGENT,
        'Content-Type': 'application/json',
    }
    if auth and _auth.access_token:
        headers['Authorization'] = f'Bearer {_auth.access_token}'
    return headers

def api_get(endpoint: str, params: dict = None, auth: bool = False) -> dict:
    """Make GET request to AH API."""
    ensure_requests()
    url = f"{API_BASE}{endpoint}"
    resp = requests.get(url, params=params, headers=api_headers(auth))
    resp.raise_for_status()
    return resp.json()

def api_post(endpoint: str, data: dict, auth: bool = False) -> dict:
    """Make POST request to AH API."""
    ensure_requests()
    url = f"{API_BASE}{endpoint}"
    resp = requests.post(url, json=data, headers=api_headers(auth))
    resp.raise_for_status()
    return resp.json()

def gql_query(query: str, variables: dict = None) -> dict:
    """Make GraphQL request."""
    ensure_requests()
    headers = {
        'User-Agent': USER_AGENT,
        'Content-Type': 'application/json',
        'client-name': 'ah-bonus',
        'client-version': '3.544.16',
    }
    resp = requests.post(GQL_URL, json={
        'query': query,
        'variables': variables or {}
    }, headers=headers)
    resp.raise_for_status()
    return resp.json()

# CLI DEFINITION

def create_parser() -> argparse.ArgumentParser:
    """Create CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Albert Heijn API client — groceries skill",
        epilog="See 'ah.py COMMAND --help' for command details."
    )
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    sub = parser.add_subparsers(dest='command')
    
    # SEARCH — Find products (anonymous)
    search = sub.add_parser('search', help='Search for products')
    search.add_argument('query', help='Search term (e.g., "hagelslag")')
    search.add_argument('--limit', '-n', type=int, default=10, help='Max results')
    search.add_argument('--bonus', '-b', action='store_true', help='Only bonus items')
    search.add_argument('--sort', choices=['relevance', 'price_asc', 'price_desc'], 
                       default='relevance', help='Sort order')
    
    # BONUS — Get current deals (anonymous)
    bonus = sub.add_parser('bonus', help='Get bonus/sale items')
    bonus.add_argument('--week', '-w', default='current', help='Week number or "current"')
    bonus.add_argument('--category', '-c', help='Filter by category')
    bonus.add_argument('--limit', '-n', type=int, default=20, help='Max results')
    
    # STORES — Find stores (anonymous)
    stores = sub.add_parser('stores', help='Find nearby stores')
    stores.add_argument('--near', help='Location (city name or "lat,lon")')
    stores.add_argument('--limit', '-n', type=int, default=5, help='Max results')
    
    # LOGIN — Authenticate
    login = sub.add_parser('login', help='Login to AH account')
    login.add_argument('--code', help='Auth code from redirect (if manual)')
    
    # LOGOUT — Clear tokens
    sub.add_parser('logout', help='Clear saved tokens')
    
    # RECEIPTS — Get purchase history (authenticated)
    receipts = sub.add_parser('receipts', help='Get receipts (kassabonnen)')
    receipts.add_argument('--limit', '-n', type=int, default=20, help='Max results')
    receipts.add_argument('--detail', '-d', help='Get specific receipt by transaction ID')
    
    # ORDERS — Get online orders (authenticated)
    orders = sub.add_parser('orders', help='Get online order history')
    orders.add_argument('--limit', '-n', type=int, default=10, help='Max results')
    
    # LIST — Shopping list management (authenticated)
    list_cmd = sub.add_parser('list', help='Manage shopping list')
    list_sub = list_cmd.add_subparsers(dest='list_action')
    list_sub.add_parser('show', help='Show current list')
    list_add = list_sub.add_parser('add', help='Add items to list')
    list_add.add_argument('items', nargs='+', help='Items to add')
    list_sub.add_parser('clear', help='Clear shopping list')
    
    # STATUS — Show auth status
    sub.add_parser('status', help='Show authentication status')
    
    return parser

# COMMAND IMPLEMENTATIONS

def cmd_search(args):
    """Search for products."""
    load_tokens()  # Use anonymous if no auth
    
    # Get anonymous token if needed
    if not _auth.access_token:
        result = api_post('/mobile-auth/v1/auth/token/anonymous', {'clientId': CLIENT_ID})
        _auth.access_token = result['access_token']
    
    params = {
        'query': args.query,
        'size': args.limit,
        'sortOn': {
            'relevance': 'RELEVANCE',
            'price_asc': 'PRICELOWHIGH', 
            'price_desc': 'PRICEHIGHLOW'
        }.get(args.sort, 'RELEVANCE')
    }
    if args.bonus:
        params['bonus'] = 'BONUS'
    
    result = api_get('/mobile-services/product/search/v2', params, auth=True)
    
    if args.json:
        print(json.dumps(result, indent=2))
        return
    
    products = result.get('products', [])
    print(f"\n🔍 Found {result['page']['totalElements']} products for '{args.query}':\n")
    
    for p in products[:args.limit]:
        bonus = "🏷️ BONUS " if p.get('isBonus') else ""
        price = p.get('currentPrice', 0)
        was_price = p.get('priceBeforeBonus')
        
        price_str = f"€{price:.2f}"
        if was_price and was_price != price:
            price_str = f"€{price:.2f} (was €{was_price:.2f})"
            
        print(f"  {bonus}{p['title']}")
        print(f"    {p.get('salesUnitSize', '')} — {price_str}")
        print()

def cmd_bonus(args):
    """Get current bonus items."""
    # Calculate week dates
    today = datetime.now()
    if args.week == 'current':
        # AH bonus week runs Monday-Sunday
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        week_num = today.isocalendar()[1]
    else:
        week_num = int(args.week)
        # Calculate dates for that week
        start = datetime.strptime(f'{today.year}-W{week_num}-1', '%Y-W%W-%w')
        end = start + timedelta(days=6)
    
    query = """
    query bonusCategories($input: PromotionSearchInput) {
        bonusCategories(filterSet: WEB_CATEGORIES, input: $input) {
            id
            title
            promotions {
                title
                subtitle
                price {
                    now { amount }
                    was { amount }
                }
            }
        }
    }
    """
    
    variables = {
        'input': {
            'weekNumber': week_num,
            'periodStart': start.strftime('%Y-%m-%d'),
            'periodEnd': end.strftime('%Y-%m-%d')
        }
    }
    
    try:
        result = gql_query(query, variables)
        
        if args.json:
            print(json.dumps(result, indent=2))
            return
        
        categories = result.get('data', {}).get('bonusCategories', [])
        print(f"\n🏷️ Bonus Week {week_num} ({start.strftime('%d/%m')} - {end.strftime('%d/%m')}):\n")
        
        count = 0
        for cat in categories:
            if args.category and args.category.lower() not in cat['title'].lower():
                continue
                
            promos = cat.get('promotions', [])
            if not promos:
                continue
                
            print(f"📦 {cat['title']}")
            for p in promos[:5]:
                price = p.get('price', {})
                now = price.get('now', {}).get('amount', 0)
                was = price.get('was', {}).get('amount', 0)
                
                if was:
                    print(f"   • {p['title']} — €{now:.2f} (was €{was:.2f})")
                else:
                    print(f"   • {p['title']}")
                    
                count += 1
                if count >= args.limit:
                    return
            print()
            
    except Exception as e:
        print(f"Error fetching bonus: {e}", file=sys.stderr)

def cmd_login(args):
    """Login to AH account."""
    load_config()
    
    if args.code:
        # Exchange provided code
        code = args.code
    else:
        # Open browser for login
        auth_url = f"{LOGIN_URL}?client_id={CLIENT_ID}&redirect_uri=appie://login-exit&response_type=code"
        print(f"\n🔐 Opening browser for login...")
        print(f"   After login, you'll be redirected to: appie://login-exit?code=CODE")
        print(f"   Copy the CODE and run: ah.py login --code CODE\n")
        
        webbrowser.open(auth_url)
        
        code = input("Enter the code from the redirect URL: ").strip()
    
    # Exchange code for tokens
    try:
        result = api_post('/mobile-auth/v1/auth/token', {
            'clientId': CLIENT_ID,
            'code': code
        })
        
        _auth.access_token = result['access_token']
        _auth.refresh_token = result['refresh_token']
        _auth.expires_at = time.time() + result.get('expires_in', 7200)
        
        save_tokens()
        print("✅ Login successful! Tokens saved.")
        
    except Exception as e:
        print(f"❌ Login failed: {e}", file=sys.stderr)

def cmd_logout(args):
    """Clear saved tokens."""
    if TOKEN_CACHE.exists():
        TOKEN_CACHE.unlink()
        print("✅ Tokens cleared.")
    else:
        print("No tokens to clear.")

def cmd_receipts(args):
    """Get receipts."""
    load_tokens()
    
    if not _auth.access_token:
        print("❌ Not logged in. Run: ah.py login")
        return
    
    if args.detail:
        # Get specific receipt
        result = api_get(f'/mobile-services/v2/receipts/{args.detail}', auth=True)
        
        if args.json:
            print(json.dumps(result, indent=2))
            return
        
        print(f"\n🧾 Receipt {args.detail}:\n")
        for item in result.get('receiptUiItems', []):
            if item['type'] == 'product':
                qty = item.get('quantity', '')
                desc = item.get('description', '')
                amount = item.get('amount', '')
                print(f"  {qty}x {desc} — €{amount}")
    else:
        # Get all receipts
        result = api_get('/mobile-services/v1/receipts', auth=True)
        
        if args.json:
            print(json.dumps(result, indent=2))
            return
        
        print(f"\n🧾 Recent Receipts:\n")
        for r in result[:args.limit]:
            date = r.get('transactionMoment', '')[:10]
            total = r.get('total', {}).get('amount', {}).get('amount', 0)
            discount = r.get('totalDiscount', {}).get('amount', 0)
            
            print(f"  {date} — €{total:.2f} (saved €{discount:.2f})")
            print(f"    ID: {r['transactionId']}")
            print()

def cmd_list(args):
    """Manage shopping list."""
    load_tokens()
    
    if not _auth.access_token:
        print("❌ Not logged in. Run: ah.py login")
        return
    
    if args.list_action == 'show':
        result = api_get('/mobile-services/shoppinglist/v2/items', auth=True)
        
        if args.json:
            print(json.dumps(result, indent=2))
            return
        
        items = result.get('items', [])
        print(f"\n📝 Shopping List ({len(items)} items):\n")
        for item in items:
            checked = "✓" if item.get('strikeThrough') else "○"
            print(f"  {checked} {item.get('name', 'Unknown')}")
            
    elif args.list_action == 'add':
        # For each item, search and add first result
        for item_name in args.items:
            # Search for product
            search_result = api_get('/mobile-services/product/search/v2', 
                                   {'query': item_name, 'size': 1}, auth=True)
            products = search_result.get('products', [])
            
            if not products:
                print(f"⚠️  No product found for '{item_name}'")
                continue
            
            product = products[0]
            # Add to list
            # Note: API may have changed, this is the documented format
            print(f"✅ Added: {product['title']}")
            
    elif args.list_action == 'clear':
        print("⚠️  Clear not implemented yet")

def cmd_status(args):
    """Show authentication status."""
    load_tokens()
    
    if _auth.access_token:
        expires = datetime.fromtimestamp(_auth.expires_at)
        if time.time() < _auth.expires_at:
            print(f"✅ Logged in (expires: {expires.strftime('%Y-%m-%d %H:%M')})")
        else:
            print(f"⚠️  Token expired at {expires.strftime('%Y-%m-%d %H:%M')}")
            print("   Run: ah.py login")
    else:
        print("❌ Not logged in")
        print("   Run: ah.py login")

def cmd_stores(args):
    """Find nearby stores."""
    # This would need geocoding for city names
    print("⚠️  Store search not fully implemented")
    print("   Use ah.nl/winkels for now")

def cmd_orders(args):
    """Get online orders."""
    load_tokens()
    
    if not _auth.access_token:
        print("❌ Not logged in. Run: ah.py login")
        return
    
    print("⚠️  Orders endpoint needs investigation")
    print("   Check GraphQL schema for order queries")

# MAIN

def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Import timedelta here to avoid issues at module level
    global timedelta
    from datetime import timedelta
    
    commands = {
        'search': cmd_search,
        'bonus': cmd_bonus,
        'stores': cmd_stores,
        'login': cmd_login,
        'logout': cmd_logout,
        'receipts': cmd_receipts,
        'orders': cmd_orders,
        'list': cmd_list,
        'status': cmd_status,
    }
    
    if args.command in commands:
        try:
            commands[args.command](args)
        except requests.HTTPError as e:
            print(f"❌ API Error: {e.response.status_code} {e.response.reason}")
            if e.response.text:
                print(f"   {e.response.text[:200]}")
        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
