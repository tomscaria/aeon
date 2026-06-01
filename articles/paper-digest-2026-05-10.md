# Paper Digest — 2026-05-10
> **Verdict:** 1 prediction-market microstructure diagnostic, 1 multi-agent quant trading framework, 1 perpetual-DEX market-making result adjacent to Hermes-arb; 13th consecutive thin HF daily browse, no new ILS or LLM-forecasting paper this cycle
> Pool: HF 80 (4 topic queries × 15 + 20 daily) + arXiv 52 (4 queries, last 14d) → deduped ~92 → skip-gated 89 → shipped 3

## Prediction Markets / Calibration / Market Microstructure

1. **The Signal Credibility Index for Prediction Markets** — Nechepurenko (2026) · ↑0
   **What's new:** Four methodological advances over naive price-move monitoring: (1) a logit-transformed short-window persistence metric, (2) a weighted Cobb-Douglas formulation with flow-based concentration measures, (3) a real-time monitoring spec, and (4) Monte Carlo validation across manipulation stress tests; validation reveals the index underdetects concentrated whale repricing and overdetects coordinated multi-wallet manipulation — it measures coordination credibility, not pure information quality.
   **So what:** This is the CalibrationGap entry-decision complement to the 3-paper Nechepurenko ILS arc — where ForesightFlow measures what fraction of the terminal move was priced in before the event, SCI answers whether the current repricing is Bayesian updating or wash/manipulation; the Russia-Ukraine 99.95% spike and Iran-peace -10pp slide from 05-09 are precisely the "durable vs. liquidity-pressure" classification this diagnostic addresses, and it pairs with the ILS trio as the price-move-credibility axis for the ADR-096+ resolution-text-ingest framing.
   [abs](https://arxiv.org/abs/2604.27041) | [pdf](https://arxiv.org/pdf/2604.27041)

## Multi-Agent / Agentic Finance

2. **AlphaCrafter: A Full-Stack Multi-Agent Framework for Cross-Sectional Quantitative Trading** — Yuan et al. (2026) · ↑0
   **What's new:** Three-agent pipeline — Miner (LLM-guided factor discovery), Screener (regime-adaptive factor assembly for current market conditions), Trader (risk-constrained execution) — tested on CSI 300 and S&P 500; consistently outperforms SOTA baselines in risk-adjusted returns with the lowest cross-trial variance in the comparison, attributed to regime-conditioned factor selection rather than static ensembles.
   **So what:** The Screener is the concrete implementation of the regime-adaptive layer CalibrationGap's quant scanner lacks — same "which factor combination fits today's regime" problem the entry-decision logic solves by hand; AlphaCrafter's LLM-guided Miner + regime-switching Screener architecture is the direct pattern for the quant-scanner upgrade the operator has been deferring to post-Apex.
   [abs](https://arxiv.org/abs/2605.05580) | [pdf](https://arxiv.org/pdf/2605.05580)

## Perpetual Markets / Hermes-arb Adjacent

3. **Funding-Aware Optimal Market Making for Perpetual DEXs** — Le (2026) · ↑0
   **What's new:** Extends Avellaneda-Stoikov market making by treating funding payments as a state-dependent cash flow coupled to inventory; solved via monotone-finite-difference HJB; backtested on Hyperliquid ETH/BTC/SOL perpetual data — funding-aware HJB improves ETH and BTC performance and reduces inventory volatility vs. the AS benchmark (SOL shows no Pareto gain under risk-adjusted comparison, attributed to heavy-tailed funding not captured by the Gaussian OU baseline).
   **So what:** Hermes-arb's Kalshi KXBTC leg is a basis trade whose exit timing is sensitive to exactly this inventory-funding coupling; the Dynamic Collateral paper (2605.05089, picked 05-07) seeded the asymmetric entry/exit threshold idea — this paper gives the HJB upgrade path and concretely shows the SOL-class heavy-tail failure mode that Hermes-arb's `min-gap` 7→7.5-8pp adjustment implicitly hedges against.
   [abs](https://arxiv.org/abs/2605.06405) | [pdf](https://arxiv.org/pdf/2605.06405)
