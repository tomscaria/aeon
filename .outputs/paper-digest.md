Paper Digest — 2026-05-09
12th-consecutive thin HF daily browse. 2 agentic-method results — no new Polymarket/DePM paper.

1. "Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction" — Li, Zhang, Choi, Zou, Han, Lin et al. (↑57) — DCI lets agents grep raw corpora instead of top-k vectors; outperforms sparse+dense+reranking on BRIGHT+BEIR. Maps to ADR-096+ resolution-text-ingest gap: the Iran-airspace clause diverges 48pp from its title precisely because embedding search sees them as surface-similar.

2. "StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction" — Xue, Zhou, Torr, Ouyang et al. (↑15) — Hierarchical GRPO samples a strategy latent at init, conditions all actions on it; 93.1% ALFWorld / 84.2% WebShop / 63.5% SciWorld. Architectural fork vs AEL (2604.21725): AEL learns which retrieval policy per episode; StraTA compresses trajectory intent into a latent. 100-trade Apex gate disambiguates the two on a Polymarket target.

Full: articles/paper-digest-2026-05-09.md
