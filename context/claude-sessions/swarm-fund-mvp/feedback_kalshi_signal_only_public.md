---
name: feedback_kalshi_signal_only_public
description: "On public surfaces, Kalshi is a read-only signal source only — never an execution/arb/paper-trade venue. Pitching Polymarket + Anthropic."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: fd4cedc2-cdec-4ff5-a856-6c969bf197ee
---

Founder directive 2026-06-03: when writing public materials (changelog, /research articles, landing copy), **Kalshi may be named only as a read-only signal source** ("a second public prediction-market feed we cross-check calibration against"). Never frame it as a venue we execute on — no arb, no cross-venue spread trade, no "paper only" on Kalshi, no "size cap required."

**Why:** we are actively pitching Polymarket (Kalshi's direct competitor) and Anthropic. Kalshi-as-execution framing undercuts the PM pitch and reads as "considering execution" the founder explicitly wants absent.

**How to apply:** scrubbed 2026-06-03 in `swarm-lab-site/src/content/` — `cross-venue.tsx` (3rd pair → "a second public prediction-market feed (read-only)"), `hermes-family.tsx` (hermes-arb reframed: trades only the PM leg), `copy.tsx` (3C subpillar → "Cross-venue PM ↔ HL"; dropped "Kalshi vs Polymarket" from fragmentation lists; swapped Kalshi out of the execution-venue example), `swarm-registry.ts` (removed 'KALSHI' from MARKET_SYMBOLS = "venues the swarm trades across"), `venue-router.tsx` (Kalshi-only event → "recorded as signal and never routed to a trade"). Acceptable residual mentions kept: registry `description` listing venues where prices differ (observational signal), and `copy.tsx:847` pro-Polymarket competitive note. Related: [[feedback_no_compliance_in_public]].
