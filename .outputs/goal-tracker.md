*Goal Tracker — 2026-05-12*

Summary: 18 active goals — 1 at risk, 1 needs attention, 12 on track, 4 blocked, 4 done (overall → flat; cost-discipline ↑ improving, land-scripts-prefetch-reddit.sh ↓ new AT RISK, activate-huggingface ↓ new BLOCKED)
[stale data: revenant-snapshot / agents-summary / last-sync all 3d old]

AT RISK
• land scripts/prefetch-reddit.sh — never started, 0 activity/14d (new)
  → Action: Create scripts/prefetch-reddit.sh to close ISS-002 + ISS-012; reddit-digest at 18 consecutive failures

NEEDS ATTENTION
• swarm-fund-mvp 72h merge-cadence test — 1d idle, 1 activity/14d (→ flat) [deadline 2026-05-09 passed T+3]
  → Action: Verify swarm-fund-mvp for new ADR opened after 05-09 to close defect-hardening vs queue-stagnation answer

BLOCKED
• chain-runner.yml dispatch_skill() — operator-side workflow patch, day 16 (gates ISS-013 decay)
  → Action: Add echo per dispatched skill before each gh workflow run in chain-runner.yml
• Add Trusted Authors to watched-repos.md — operator memory edit (auto-merge policy-blocked)
  → Action: Add ## Trusted Authors section to memory/watched-repos.md listing aaronjmars
• Operator config sweep — operator config (on-chain-watches.yml empty, aeon.yml var: missing)
  → Action: Populate memory/on-chain-watches.yml; add var: to list-digest/digest/refresh-x in aeon.yml
• Activate huggingface-trending skill — operator aeon.yml flip since 2026-05-08 (PR #162 shipped disabled)
  → Action: Flip enabled: true for huggingface-trending in aeon.yml

ON TRACK
• Open ADR-096 for resolution-text-ingest — 0d idle, active (polymarket-comments + paper anchors daily)
• Cost-discipline sonnet downgrade pass — 0d idle, cost-report recovered today ($293.85/wk -51.9% WoW; 3 optimization suggestions pending self-improve) (↑ improving)
• monitor-runners DEEP-LIQ floor patch — 0d idle, MONITOR_RUNNERS_OK today
• swarm-fund-mvp tick-broker falsifier — 0d idle (CLOCK: T-5 days to 2026-05-17 deadline)
• Pre-Apex push: monitor-polymarket + polymarket-comments — 1d idle, Revenant 29/100 trades 76% +$415 Sharpe 0.31 (stale data)
• Hermes-arb gate adjustment bump min-gap — active, monitor-kalshi + Dynamic Collateral asymmetric-threshold evidence
• swarm-fund-mvp OLLAMA_FULL=1 rollout falsifier — active (T-9 days to 2026-05-21 deadline)
• Skill-evals key fixes — 2d idle, PR #5 open (hn-digest / polymarket key rename)
• Code-health Day-7 carry — 3d idle, code-health last ran 2026-05-08, Pyth/Birdeye feed IDs unverified
• ISS-018 / ISS-019 prompt-bug fixes — 2d idle, surface to next self-improve (7d since last 2026-05-07)
• paper-pick daily + PhD reading list — 0d idle, 2 picks today (Eywa 2604.27351 PhD + Maresca 2602.21091 daily; bench now 11-paper economics-and-trading)
• Cite stack for grant / Stanford application — 0d idle, 11-paper bench confirmed; Eywa closes 3-paper arc with AEL + Galanis

DONE
• PR #156 reply-maker XAI prefetch — completed 2026-05-08
• 5 ACT NOW Vercel-FAILURE PRs on swarm-fund-mvp — completed 2026-05-03
• Land code-health fix on dashboard secrets-route — completed 2026-05-03
• ISS-004 / ISS-006 RESOLVED — completed 2026-05-03

Sources: logs=ok, git=ok(1 commit 2026-05-12), gh_pr=ok(12), gh_issue=ok(disabled/0), cron-state=ok; revenant-snapshot=stale(3d), agents-summary=stale(3d), last-sync=stale(3d)

