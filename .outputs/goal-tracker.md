*Goal Tracker — 2026-05-10* (stale trading context: last-sync 31h ago)

Summary: 16 goals — 0 at risk, 1 needs attention, 12 on track, 3 blocked, 4 done (→ flat)

NEEDS ATTENTION
• swarm-fund-mvp 72h merge-cadence test — deadline 05-09 passed, 0d idle (→ flat; queue stagnation confirmed by two heartbeats today)
  → Archive this falsifier; open queue-stagnation mitigation in next self-improve pass.

BLOCKED
• chain-runner.yml dispatch_skill() — Day 14 idle, waiting on operator workflow patch
  → Operator applies dispatch_skill() echo patch (add echo before each gh workflow run in chain-runner.yml).
• Add Trusted Authors to memory/watched-repos.md — waiting on operator edit
  → Operator adds aaronjmars (+ optionally tomscaria) to Trusted Authors; unblocks auto-merge.
• Operator config sweep — waiting on operator
  → Populate memory/on-chain-watches.yml with one address; add var: to list-digest in aeon.yml.

ON TRACK
• Open ADR-096 for resolution-text-ingest — 0d idle, heavy evidence build (→ flat) [14+ days no ADR slot; SCI sci-entry-gate ADR now ships first per 05-10 paper-pick]
• Cost-discipline sonnet downgrade pass — 0d idle (→ flat) [still ~$2,696/mo vs $40/wk; no downgrade action taken]
• monitor-runners DEEP-LIQ floor patch — 0d idle, 8+ evidence runs ready for self-improve (→ flat)
• swarm-fund-mvp tick-broker falsifier — 0d idle, 7 days to 2026-05-17 deadline (→ flat)
• Pre-Apex push: monitor-polymarket + polymarket-comments — 0d idle, both ran today (→ flat) [Revenant 29/100 stale; no fresh revenant_agents data]
• Hermes-arb gate adjustment: min-gap 7pp → ~7.5-8pp — 0d idle (→ flat)
• swarm-fund-mvp OLLAMA_FULL=1 rollout falsifier — 0d idle, 11 days to 2026-05-21 deadline (→ flat)
• skill-evals key fixes (PR #5) — 0d idle, PR stalled ~13d (→ flat)
• code-health Day-7 carry — 1d idle (→ flat)
• ISS-018/ISS-019 prompt-bug fixes — 0d idle (→ flat)
• paper-pick daily / build PhD reading list — 0d idle, SCI picked today (→ improving; 4-paper Nechepurenko stack complete)
• cite stack for next grant / Stanford application — 0d idle, SCI added (→ improving)

DONE
• PR #156 reply-maker XAI prefetch — completed 2026-05-08T01:18Z
• 5 ACT NOW Vercel-failure PRs — completed 2026-05-03
• Land code-health fix (secrets-route) — completed 2026-05-03
• ISS-004 / ISS-006 resolved — completed 2026-05-03

Sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok(empty), cron-state=ok, revenant-snapshot=stale(empty ~31h), agents-summary=ok(canary=9/shadow=158, no revenant lifecycle), costs-summary=ok, last-sync=stale(31h)

