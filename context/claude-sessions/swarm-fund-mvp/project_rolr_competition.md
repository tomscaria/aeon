---
name: project-rolr-competition
description: ROLR freeplay paper competition — public tRPC API mirrors Polymarket; $0 scanner cron live; phase-2 execution via positions.buy + session cookie pending
metadata: 
  node_type: memory
  type: project
  originSessionId: 5fc03df3-4b62-47f2-b75a-b1298de97449
---

ROLR paper-trading competition (freeplay.rolr.com). Discovered 2026-06-10: **no scraping needed** — public unauthenticated tRPC `GET /api/trpc/markets.list` (limit≤50, cursor pagination, volume-sorted, ~2,000 markets) mirrors Polymarket: outcome `externalId` = gamma market id (binary markets use `<id>-yes`/`<id>-no` stems), full shape also carries CLOB `tokenId` (lite shape omits it — alternates between responses). `staleness`/`fetchedAt` fields expose ROLR's own cache lag = the edge.

Shipped commit `910c654a`: `python/scanner/rolr_client.py` + `scripts/rolr_arb_scan.py` + LaunchAgent `ai.rswarm.rolr-arb` (300s, LIVE since 2026-06-10). Gamma batch quotes primary, CLOB `/prices` fallback (CLOB WAF 403s without browser User-Agent — not a geoblock). History in `data/rolr_scan.jsonl` (run_id per line, for edge-decay/cadence tuning), report `outputs/YYYY-MM-DD_rolr_arb.md`, Telegram ≥4% edge with 30-min slug dedupe. First live scan: 9 executable edges, max 41.5%.

**Official Rules read 2026-06-11 ($25M Challenge, Jun 2–Aug 12 2026):** real cash prizes ($1k/wk, $5k/mo, $25M grand via 7-question final, $75k season champion fallback). **Eligibility is residency-based, not IP** — SF/CA eligible (excluded: AZ IL MD MA MI NV NJ OH WA); NYC IP irrelevant; KYC required for Finalists by Jul 31. **Hard cap: 10 predictions/day** (resets 12:00 AM EST); leaderboard = weekly Delta Points (mark-to-market, updated ~24h); weekly cutoff Sun 12:00 PM EST; weekly top-3 become Finalists. Site ToS bans "automated means, including bots or scrapers"; Official Rules §20 allows DQ for "tampering" at sole discretion. **Phase 2 auto-execution via positions.buy KILLED** — DQ risk with real prizes + 10/day cap makes manual execution from Telegram alerts strictly better. Scanner = decision support; founder places trades by hand. Related: [[polymarket-datacenter-ban]].
