---
name: session-2026-06-11-execution-station
description: Execution Station (ADR-139..142) + colima root-cause + acceptance caught stale-mark cap bug; DD VM holds 58k-trade history hostage
metadata: 
  node_type: memory
  type: project
  originSessionId: 7fe69a3a-1549-4be5-b269-dbeb215704e3
---

# Session 2026-06-11 — ops-hardening + Execution Station (brick 2)

- **Infra truth: the stack runs on colima** (all volumes), NOT Docker
  Desktop. Reboots killed it silently (no autostart — now fixed via
  `brew services start colima`). Kafka producer logs "published" even when
  the broker is dead — never trust those lines without a consumer-side check.
- **Docker Desktop VM is wedged** (won't boot headless) and holds the
  58k-trade QuestDB history + old RedPanda retention. Rescue = founder opens
  DD GUI once, then migrate volume into colima. Two QuestDB schema
  generations exist (`ts` init-SQL vs `timestamp` DD) — sources.py detects
  at runtime ([[session-2026-06-10-microstructure-station]] said 'timestamp
  is the deployed schema' — that was DD's; colima uses `ts`).
- **Execution Station shipped paper-only** (python/execution_station/,
  ADR-139..142, 121 tests): A-S quoting, Hawkes kill-switch w/ sparse
  fallback, dual-mode L1 fill sim (gate on conservative), inventory
  caps/bands, cycle mark-out labels → existing backtest backbone,
  /api/execution/*. Live quoting venue-blocked (PM Global read-only, PM US
  sports-only).
- **Acceptance experiments work**: first real replay caught the cap pricing
  inventory at a stale book mid through a 0.11→0.62 gap (−$498). Fix:
  mark_px from tape prints + print-triggered requotes (b7d793d5). Post-fix
  capture +$1.93, worst notional $66.
- **Dune tap is LIVE in production** (pipeline/run_all.py runs
  consume_forever; 972 markets in dune_tap.json) — informed-flow feature no
  longer dead in live mode.
- Kalshi WS returns 401 since the stack revival (new manual/investigate).
