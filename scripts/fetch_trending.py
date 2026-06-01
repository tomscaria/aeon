import sys, json, urllib.request

url = "https://api.coingecko.com/api/v3/search/trending"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.load(r)

coins = data.get('coins', [])[:7]
print("--- TRENDING ---")
for item in coins:
    c = item.get('item', {})
    name = c.get('name', '?')
    sym = (c.get('symbol') or '?').upper()
    rank = c.get('market_cap_rank', '?')
    price = c.get('data', {}).get('price', '?')
    pct = c.get('data', {}).get('price_change_percentage_24h', {})
    if isinstance(pct, dict):
        pct24 = pct.get('usd', None)
    else:
        pct24 = None
    pct_str = f"{pct24:+.1f}%" if pct24 is not None else "?"
    print(f"{sym} ({name}) | rank#{rank} | price:{price} | 24h:{pct_str}")
