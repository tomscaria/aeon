---
name: session-2026-06-11-exit-engine-redesign
description: "Exit-engine 4-layer redesign spec committed + research-verified; corpus got FTS5, full-text, 23 new exit-design papers; PDF-ingest gap confirmed"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3dedf189-bba1-45d9-8eab-db9425609833
---

# Session 2026-06-11 — Exit Engine redesign (first-principles SL/TP)

**Spec committed:** `docs/superpowers/specs/2026-06-11-exit-engine-redesign-design.md` (commits `465f3b3f` + `2c7a82f9`). **BUILT same session — ADR-143** (note: DECISIONS.md has duplicate ADR-139s; exit engine took 143). Six commits `85a67561..ac253dde` on main: manual-PDF harvester (data/manual_pdfs/ live); python/risk/ package (realized_vol EWMA hourly sigma, exit_policy YAML+JSON store w/ Leung–Li coupling, shadow_recorder, exit_engine L0+L2, e_detector L1, agent_budget L3, kelly_constrained stub, policy_promotion nightly sweep); main.py per-iteration pass; /api/exits + Telegram /exit_status. **No policy is apex → runtime effect is shadow recording only; canary→apex is IC-MANUAL ONLY.** ADR-097 replay test reproduces static-stop negative result on real CG book. Full regression 2502 passed/3 skipped. Loop NOT restarted — new code inert in the running PID until restart.

**Architecture (4 layers, priority order):** L0 data-fidelity sentinel (always-on protective: degraded→tighten, blind→shrink); L1 thesis-vitality (posterior-edge exits, e-detector triggers w/ ARL≥1/α; PM via bridge-process stopping — Ekström–Vaicenavicius 1705.00369 unknown pinning point, Leung–Li–Li randomized Brownian bridge; [0,1] mapping is in-house novel/publishable); L2 regime-GATED (Kaminski–Lo: stops negative-EV under random walk) vol-scaled triple-barriers replacing fixed 24h close, SL/TP coupled per Leung–Li (higher stop ⇒ lower TP; entry-veto near stop), σ-multiples swept in-house (open problem in literature — mlfinlab pt_sl×EWMA-vol parameterization + GA/grid); L3 per-agent drawdown budgets via risk-constrained Kelly (Busseti–Ryu–Boyd convex). Dormant CG_STOP_LOSS_PCT subsumed as a losing shadow policy; ADR-097 sweep = first historical shadow run. Refuted, never use: arXiv 1609.00869 histogram-argmax stop selection (killed 2-1 adversarial).

**Corpus upgrades shipped in-session:** FTS5 `papers_fts` (title/abstract/full_text, sync triggers) on data/papers.db; 23 papers ingested `source='deep_research'` (2 rounds, deep-research workflow 103 agents 24/25 claims verified + targeted agent for 4 open questions); 9 arXiv full texts fetched via pypdf (now installed in venv). Corpus: 3,772 papers, 52 with full text.

**Confirmed gap:** founder-dropped session PDFs NEVER reached the corpus — no manual-PDF harvester exists. Planned: `data/manual_pdfs/` + `harvest_manual_pdfs.py` (in spec §6 build order step 1).

Related: [[session_2026-06-10_microstructure_station]], [[feedback_codex_handoff_queue]]
