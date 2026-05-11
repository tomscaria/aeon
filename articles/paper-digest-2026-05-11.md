# Paper Digest — 2026-05-11
> **Verdict:** 1 high-upvote agentic orchestration framework (Eywa ↑209), 1 Bayesian forecaster that beats GPT-5 and Grok 4.20 on ForecastBench binaries, 1 controlled prediction-market trading experiment with a hard complexity-degrades-aggregation finding; no new ILS or Polymarket microstructure paper this cycle
> Pool: HF 63 (4 topic searches × 15 + 15 daily) + arXiv 32 (web fallback; arXiv API 429) → 82 deduped → 79 skip-gated → 3 shipped
> Note: arXiv API unavailable (HTTP 429 throughout) — arXiv data via web search fallback (partial: 1/2 sources)

## Agentic Systems

1. **Heterogeneous Scientific Foundation Model Collaboration (Eywa)** — Zihao Li, Jiaru Zou et al. (UIUC, 2026) · ↑209
   **What's new:** Eywa introduces a three-tier heterogeneous framework — EywaAgent (single-agent drop-in), EywaMAS (multi-agent integration), EywaOrchestra (planning-based dynamic orchestration) — that routes non-linguistic scientific inputs to specialized predictive foundation models while keeping an LLM as the coordination layer, with empirical gains across physical, life, and social science domain tasks.
   **So what:** The orchestrator-over-specialist architecture is the direct shape of CalibrationGap's next planned upgrade (LLM-head routing over the Polymarket quant-scanner + Kalshi CLOB ingestion layer); with 209 HF upvotes this is the highest-signal agentic framework surfaced by paper-digest in 14 days and is the concrete PhD-slot candidate that supersedes the narrower EvoScientist/CORAL framing in the Stanford application's multi-agent section.
   [abs](https://arxiv.org/abs/2604.27351) | [pdf](https://arxiv.org/pdf/2604.27351) | [project](https://www.zihao.website/eywa.github.io/) | [code](https://github.com/Violet24K/Eywa)

## LLM Forecasting

2. **Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs** — Kevin Murphy (2026) · ↑0 HF / v3
   **What's new:** Bayesian Linguistic Forecaster (BLF) combines a linguistic belief state (numerical probability fused with natural-language evidence summary, updated iteratively via tool use), logit-space hierarchical aggregation with a data-dependent prior, and Platt-scaled calibration with a hierarchical prior — together these outperform GPT-5, Grok 4.20, Cassi, and Foresight-32B on 400 ForecastBench binary questions with a backtesting leakage rate held below 1.5%.
   **So what:** BLF is the first published agentic forecaster to beat GPT-5 at the per-binary-question level on a standardized benchmark — directly comparable to CalibrationGap's 76% live win rate — and its logit-space aggregation + Platt calibration steps are the closest published analogue to CalibrationGap's confidence-weighted entry-decision logic, making BLF the top methodological baseline the Apex gate (100-trade sample) needs to falsify or confirm.
   [abs](https://arxiv.org/abs/2604.18576) | [pdf](https://arxiv.org/pdf/2604.18576)

## Prediction Markets

3. **Information Aggregation with AI Agents** — Spyros Galanis (2026) · ↑0 HF / revised 2026-05-07
   **What's new:** Galanis runs a controlled double-auction prediction-market experiment where AI agents receive private signals and trade with each other, finding that median markets aggregate dispersed information well under simple conditions but complexity has "a significant and negative impact" — confirmed across 64 pages of experimental evidence spanning multiple market designs, with "smarter" agents dominating profitability and feedback on past performance yielding zero improvement in aggregation.
   **So what:** This is the first experimental (not simulation-only) falsifier for the confidence-weighted Bayesian fusion step inside CalibrationGap's multi-agent aggregation design: easy Polymarket markets should aggregate, hard multi-condition geopolitical markets likely degrade — the complexity threshold the paper identifies is the calibration gap CalibrationGap needs to map before the Apex gate closes; the "feedback has no effect" finding also cuts against the reflection-log improvement thesis unless the Aeon retrieval-policy bandit (ADR-???-retrieval-policy-bandit seed from AEL `2604.21725`) picks the right feedback to surface.
   [abs](https://arxiv.org/abs/2604.20050) | [pdf](https://arxiv.org/pdf/2604.20050)
