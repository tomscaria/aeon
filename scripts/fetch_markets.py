import sys, json, urllib.request

STABLES = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','frax','usdc','busd','usdt','nusd','usdp','usdn','gusd'}
WRAPS = {'wbtc','weth','steth','cbeth','reth'}

def is_stable(c):
    if c['id'] in STABLES: return True
    sym = (c.get('symbol') or '').upper()
    if sym.startswith(('USD','EUR','GBP')): return True
    if 'stablecoin' in (c.get('name') or '').lower(): return True
    if c['id'] in WRAPS: return True
    return False

def vol(c): return c.get('total_volume') or 0
def pct24(c): return c.get('price_change_percentage_24h') or 0

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.load(r)

filtered = [c for c in data if not is_stable(c) and vol(c) >= 1_000_000]

winners = sorted(filtered, key=pct24, reverse=True)[:10]
losers  = sorted(filtered, key=pct24)[:10]

top100 = filtered[:100]
green = sum(1 for c in top100 if pct24(c) > 0)
med50_vals = sorted([pct24(c) for c in filtered[:50]])
med50 = med50_vals[25] if len(med50_vals) > 25 else 0

print(f"PULSE: {green}/100 green, median50={med50:.1f}%")
print()

def tags_for(c):
    p24 = pct24(c)
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    mcr = c.get('market_cap_rank') or 999
    mc = c.get('market_cap') or 0
    v = vol(c)
    vol_mc_ratio = v / max(mc, 1)
    tags = []
    if mcr <= 20: tags.append('MAJOR')
    if p24 > 15 and p7d > 25: tags.append('BREAKOUT')
    elif p24 > 20 and p7d < 0: tags.append('FADE')
    if mcr > 150 and p24 > 30: tags.append('PUMP-RISK')
    if mc < 50_000_000: tags.append('MICROCAP')
    if p24 < -10 and vol_mc_ratio > 0.25: tags.append('CAPITULATION')
    return tags[:2]

def fmt(c):
    p1h = c.get('price_change_percentage_1h_in_currency') or 0
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    p24 = pct24(c)
    mcr = c.get('market_cap_rank') or 999
    vol_m = vol(c) / 1e6
    mc_b = (c.get('market_cap') or 0) / 1e9
    price = c.get('current_price') or 0
    tag_str = ' '.join(f'[{t}]' for t in tags_for(c))
    sym = (c.get('symbol') or '').upper()
    name = c.get('name') or ''
    if price >= 1000:
        price_fmt = f"${price:,.0f}"
    elif price >= 1:
        price_fmt = f"${price:.4g}"
    elif price >= 0.01:
        price_fmt = f"${price:.4f}"
    else:
        price_fmt = f"${price:.6f}"
    return f"{sym} ({name}) | rank#{mcr} | {price_fmt} | 24h:{p24:+.1f}% 7d:{p7d:+.1f}% 1h:{p1h:+.1f}% | vol:${vol_m:.1f}M mc:${mc_b:.2f}B | {tag_str}"

print("--- WINNERS ---")
for c in winners:
    print(fmt(c))

print()
print("--- LOSERS ---")
for c in losers:
    print(fmt(c))
