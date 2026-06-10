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

**Phase 2 (not built):** auto-execution via tRPC `positions.buy` mutation — needs founder to copy session cookie from logged-in browser (`ROLR_SESSION_COOKIE`) + one manual buy with devtools open to capture payload shape. Check competition rules for automated-trading clause first. Geo (NYC IP / SF registration) is ToS-level only — free paper comp, no money moves. Related: [[polymarket-datacenter-ban]].
