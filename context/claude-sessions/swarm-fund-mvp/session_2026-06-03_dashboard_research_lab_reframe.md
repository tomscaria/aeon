---
name: session_2026-06-03_dashboard_research_lab_reframe
description: "Dashboard reframed to research-lab data-funnel + live portfolio drill-down; ADR-117 drawdown gates live-only. Uncommitted working tree, demoable on localhost:3000."
metadata: 
  node_type: memory
  type: project
  originSessionId: 74da5b6b-3235-4d49-99ec-e591087c9209
---

# Session 2026-06-03 — Dashboard research-lab reframe + live drill-down + ADR-117

Founder direction: "we are a live research lab — highlight shots-on-goal / strategy harvesting / data volume, NOT paper-trade P&L. Live portfolio = real performance with wallet→venue→strategy→trade drill-down + external links. The loop should never pause; graduations are automatic." Built autonomously while founder prepped for a meeting; goal was a demoable dashboard.

## Shipped (ALL UNCOMMITTED in working tree — `commit only when asked`)
- **`GET /api/lab/funnel`** (`python/api/server.py`, near `/api/status`) — research funnel: strategies_harvested(48), agents_total(183), lifecycle{birth160/canary23/apex0/revenant0}, shots_on_goal(=total trades, ~4923), closed/open, paper/live, trades_24h, kb_concepts(29 = dashboard/public/knowledge-graph.json node count, NOT the 3204 DB concepts), regime. Read-only, never raises.
- **`GET /api/live/breakdown`** — real-money pivot. Portfolio(NAV $364.07, realized $68.08 from HL userFills, wallet 0x83F4…89e3) → venues → strategies(by agent_id; strategy = `agent_type`) → trades[:200]. `_venue_of()` prioritizes `hl_order_id`→Hyperliquid (calibration-gap fills carry a PM market_id signal-source but execute as real HL perps). HL explorer URL `https://app.hyperliquid.xyz/explorer/address/{wallet}`. PM slug NOT stored (live PM≈0, link deferred).
- **`ResearchLabFunnel.tsx`** — PAPER view of Command Center (`(shell)/page.tsx`: PAPER→funnel, LIVE→existing cards). Module-level `_funnelCache` avoids dash-flash on toggle.
- **`FundHUD.tsx`** — PAPER header reframed: NAV/Total-P&L → Shots / 24h (keeps "Live: $364" subref). LIVE header unchanged.
- **`(shell)/portfolio/page.tsx`** + Sidebar "Portfolio" nav (Wallet icon, top-level) — expandable strategy→trade pivot, external HL links per fill.
- **ADR-117** (`DECISIONS.md`) + `_drawdown_should_halt(dd_action, live_mode)` in `python/main.py` + `tests/test_drawdown_paper_never_halts.py` (5/5 green). Halting actions (hard_stop/halt) now gated on `live_mode`; paper mode never halts. **Live-money behavior byte-unchanged** (`and live_mode`). Phase 2 (decouple paper data-gen from a *live* drawdown halt) DEFERRED — needs founder supervision.

## Critical state notes
- **Trading loop (main.py) NOT restarted** — running PID predates the ADR-117 edit, so the no-pause change is INERT until next loop restart. `live_mode` is currently TRUE (real $364, 41 real fills) so the change would be inert anyway until a paper run.
- **API WAS restarted** (`launchctl kickstart -k gui/$UID/ai.rswarm.api`) → both new endpoints live on :8000.
- Dashboard `npx tsc --noEmit` clean; loop not paused; `/api/lab/funnel` + `/api/live/breakdown` verified returning real data.
- Demoable: `cd dashboard && npm run dev` → localhost:3000 (preview-managed this session). `dashboard/.claude/launch.json` created for preview tool.
- Lifecycle naming: internal shadow/canary/live/demoted ↔ public birth/canary/apex/revenant (ADR-045).

## Not done / next
- Commit (held — founder didn't ask). Vercel deploy if they want it live on rswarm.ai.
- ADR-117 Phase 2 (supervised). PM external links (need Gamma slug lookup). Time-series funnel (volume/day) needs historical snapshots.
