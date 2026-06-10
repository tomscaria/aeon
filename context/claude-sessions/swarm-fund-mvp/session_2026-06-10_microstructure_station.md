---
name: session-2026-06-10-microstructure-station
description: Microstructure Signal Station shipped (ADR-134..137) — first assembly-line brick; Dune gets its first consumer; frontend TS contract published
metadata: 
  node_type: memory
  type: project
  originSessionId: 7fe69a3a-1549-4be5-b269-dbeb215704e3
---

# Session 2026-06-10 — Microstructure Signal Station (assembly-line brick 1)

Commits `95adb944..d67f49fb` on main. 65/65 new tests; full regression green.

- **Assembly-line ontology now in code** (ADR-134): `python/microstructure/` —
  Stage Protocols + frozen+slots handoffs (`Bar → FeatureVector →
  MicrostructureSignal → LabeledSignal`); `LabeledSignal` is the exact
  duck-typed contract `python/backtest/` consumes (`entry_ts` + `forward_return`).
- **Features (ADR-135)**: OFI (L1 flow variant — QuestDB persists best-quote
  only), Stoikov microprice + dislocation, Glosten-Milgrom MVP split
  (adverse ∝ |ofi|), informed-flow (Dune skew × OFI sign agreement, 12h
  staleness ceiling, no-future-Dune raises), VPN thinness. **regime_hint is
  metadata-only** — regime-as-router is a later seam.
- **DuneSmartMoneyTap = first consumer of `events.canonical.derived`**
  (ADR-137) — flips Dune off NOT_YET_PLUMBED once paper signals flow
  (scan_fn stamps `data_source: "dune"`; verify after loop restart).
- **Strategy**: `microstructure-signal` (PAPER) in `build_registry()`;
  deliberately NOT runner-swarm-wrapped; TASKS.md entry per ADR-086.
- **Frontend contract**: `dashboard/app/lib/microstructure-types.ts` + spec
  `docs/superpowers/specs/2026-06-10-microstructure-frontend-ia-schema.md`
  — 6 planned `/api/microstructure/*` endpoints, 5-tab IA under
  `/microstructure`. Frontend builds against mocks first.
- **Learn-hub loop live**: mermaid renders client-side (Concept.astro
  matches shiki `data-language="mermaid"`); 6 hand pages in
  kb/topics/microstructure/.
- **ADR numbering**: DECISIONS.md head was 129 but code referenced 130-133
  (never landed) — reserved stub added, new ADRs start at 134. Check
  `grep -o 'ADR-1[0-9][0-9]' DECISIONS.md` AND code before numbering.

Next: [[project-microstructure-next-slices]] — /api endpoints, real-history
DSR report, Container B PG attach, then Avellaneda-Stoikov + Hawkes
execution station. Plan file: ~/.claude/plans/twinkly-tinkering-stonebraker.md.
