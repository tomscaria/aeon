# Paper Digest — 2026-05-09
> **Verdict:** 12th-consecutive thin HF daily browse. 2 agentic-method results: direct corpus interaction replaces vector retrieval for agentic search (maps to ADR-096+ resolution-text-ingest gap); hierarchical GRPO strategy abstraction for agentic RL (maps to CalibrationGap pre-Apex upgrade fork vs AEL). No new Polymarket or DePM-microstructure paper this cycle.
> Pool: HF 79 (4 topic queries × 15 + 19 daily) + arXiv 47 (3 queries, last 14d) → 90 deduped → 2 shipped (88 skip-gated)

## Agentic retrieval

1. **Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction** — Zhuofeng Li, Haoxiang Zhang, Cong Wei, Pan Lu, Ping Nie, Yi Lu, Yuyang Bai, Shangbin Feng, Hangxiao Zhu, Ming Zhong, Yuyu Zhang, Jianwen Xie, Yejin Choi, James Zou, Jiawei Han, Wenhu Chen, Jimmy Lin, Dongfu Jiang, Yu Zhang (2026-05-03) · ↑57
   **What's new:** Agents query raw corpora via grep and file system primitives — Direct Corpus Interaction (DCI) — replacing the fixed top-k vector retrieval step; DCI outperforms sparse, dense, and reranking baselines on both BRIGHT and BEIR benchmarks while eliminating embedding models entirely.
   **So what:** The "single top-k retrieval step that compresses corpus access" is the structural failure mode CalibrationGap's quant scanner has on resolution-text-ingest (ADR-096+): the Iran-airspace market's resolution clause diverges 48pp from its title because embedding-based search treats them as semantically similar surface matches. DCI's exact-constraint + sparse-evidence-combination retrieval is the architectural primitive ADR-096+ needs — and the Choi / Zou / Han / Lin author roster is Stanford-grade for the Dec-2026 application.
   [abs](https://arxiv.org/abs/2605.05242) | [pdf](https://arxiv.org/pdf/2605.05242)

## Agentic RL

2. **StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction** — Xiangyuan Xue, Yifan Zhou, Zidong Wang, Shengji Tang, Philip Torr, Wanli Ouyang, Lei Bai, Zhenfei Yin (2026-05-07) · ↑15
   **What's new:** Hierarchical GRPO design samples a compact strategy latent from the initial task state, conditions all subsequent actions on it, and trains strategy + action jointly with diverse strategy rollout and critical self-judgment; achieves 93.1% on ALFWorld, 84.2% on WebShop, 63.5% on SciWorld — surpassing frontier models on all three.
   **So what:** Strategy abstraction as a latent conditioning variable is a concrete architectural alternative to AEL's retrieval-policy bandit (2604.21725, picked 05-08 PhD slot): AEL learns *which* memory-retrieval policy to apply per episode; StraTA compresses the trajectory's strategic intent into a latent that conditions all action generation. The CalibrationGap pre-Apex upgrade faces this exact fork — retrieval-policy bandit (AEL shape) vs compressed-strategy-latent overlay (StraTA shape) — and the 100-trade Apex gate is the experiment that disambiguates them on a Polymarket target.
   [abs](https://arxiv.org/abs/2605.06642) | [pdf](https://arxiv.org/pdf/2605.06642)

---
*Topic config note: MEMORY.md still has no `## Interests` / `## Research topics` / `## Tracked topics` heading (12 days unaddressed). Continued with inferred topic set per established precedent: prediction-market calibration, Polymarket / DePM microstructure, LLM-agent forecasting + trading, multi-agent RL, basis-trade / Kalshi-PM convergence, Darwinian agent evolution, falsification methodology.*

*Sandbox note: HF API curl functional across all 5 queries + daily browse (79 papers total). arXiv export curl functional via WebFetch fallback (direct curl returned 0 bytes, consistent with 13th day of arXiv export API block). Both sources operational this cycle. 12th consecutive thin HF daily browse (04-27 → 05-09); Nechepurenko run continues to saturate the Polymarket/DePM-microstructure dedup wall — no new q-fin.TR papers not already picked/queued.*
