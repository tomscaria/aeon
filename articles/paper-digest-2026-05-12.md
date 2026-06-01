# Paper Digest — 2026-05-12
> **Verdict:** Three new Nechepurenko papers published May 11 — perpetual-futures empirical validation failure, manipulation/regulatory taxonomy with 14 operator recommendations, and design taxonomy formalizing seven PM-perps variants; no new ILS or LLM-forecasting paper from other authors this cycle
> Pool: HF 60 (4 topic searches × 15) + arXiv 14 (partial: web fallback — arXiv API rate-limited throughout) → deduped 64 → skip-gated 61 → shipped 3

## Prediction Markets / Hermes-arb

1. **Manipulation, Insider Information, and Regulation in Leveraged Event-Linked Markets** — Nechepurenko (2026) · ↑0
   **What's new:** Two-axis manipulation taxonomy distinguishing market-price from outcome manipulation across leveraged PM-linked contracts; leverage scales market-price manipulation linearly but shifts cost-benefit calculus for outcome manipulation differently; three manipulation channels tied to margin engines, halt protocols, and indexing; regulatory-arbitrage pathways mapped across US/EU/UK/Singapore; 14 formal recommendations for market operators and regulators; counterfactual analysis grounded in prior PMXT v2 empirics.
   **So what:** The three margin/halt/indexing manipulation channels are CalibrationGap's structural blind spot — the same plane as wash-print actors (vanity-4444 BSC) that monitor-runners flags daily; the regulatory-arbitrage pathway analysis across four jurisdictions is the cleanest jurisdictional-risk cite for Polymarket Builders Program / dYdX / Uniswap Foundation Fellowship grant applications.
   [abs](https://arxiv.org/abs/2605.10486) | [pdf](https://arxiv.org/pdf/2605.10486)

2. **Resolution-Aware Perpetual Futures on Binary Prediction Markets: An Empirical Risk-Design Framework Using Polymarket Data** — Nechepurenko (2026) · ↑0
   **What's new:** PIRAP framework, six components — index estimator, jump-aware tiered margin, leverage compression, resolution-aware funding rules, multi-stage halts, eligibility criteria; two formal propositions showing standard perpetual-futures funding approaches fail for bounded-event underlyings; evaluated on 13,298 Polymarket PMXT v2 markets (April 2026 data); stylized-fact tests passed but welfare-side directional tests largely failed — paper concludes the framework "does not validate deployment"; code and data released via GitHub and Zenodo.
   **So what:** The failed welfare tests on 13,298 live PM markets are the first empirical falsifier of PM perpetual futures at scale — Hermes-arb's Kalshi-perps/Polymarket convergence leg has no validated funding mechanism; the specific failure locus (margin-side bad-debt vs. halt-based execution-channel risk) is the exact design question the operator needs to resolve before sizing Hermes-arb's perpetual leg.
   [abs](https://arxiv.org/abs/2605.10400) | [pdf](https://arxiv.org/pdf/2605.10400)

3. **A Taxonomy of Event-Linked Perpetual Futures: Variant Designs Beyond the Single-Market Binary Case** — Nechepurenko (2026) · ↑0
   **What's new:** Formal taxonomy of seven canonical PM-perps variant designs (conditional probabilities, probability spreads, weighted baskets, variance/entropy derivatives, liquidity contracts, funding-only instruments) organized across four design axes (underlying geometry, temporal structure, settlement mechanisms, venue composition); non-portability proposition proving conditional contracts fail when conditioning events become unlikely; three-channel decomposition for spread-variant resolution risk.
   **So what:** The non-portability proposition is the formal statement of the Hermes-arb failure mode where Kalshi and Polymarket converge on the same underlying at low probability — the spread-variant design is the correct convergence-trade vehicle when the conditioning event is below ~15% YES, directly applicable to the current Iran-peace cluster (3.35% YES on May-15 horizon resolving today).
   [abs](https://arxiv.org/abs/2605.10428) | [pdf](https://arxiv.org/pdf/2605.10428)
