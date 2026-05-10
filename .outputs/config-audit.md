Config Audit — 2026-05-10 — Grade: B (89/100)
0 critical, 0 high, 2 medium, 1 low

Top findings:
M1: 5 skills missing Sandbox note (reflect, self-improve, code-health, external-feature, aixbt-pulse) — fallback pattern undocumented, silent failures on sandbox-blocked curl
M2: 26 active skills missing Constraints stub — self-improve/autoresearch could mutate tags or var semantics breaking cron dispatch
L1: Abbreviated wallet address in aeon.yml monitor-polymarket var field — non-functional but documents a risky pattern

Pre-existing (not re-scored): ISS-015 (messages.yml repository_dispatch toJson injection, HIGH, still open)

Auto-fixes applied: 31 files — PR #12 https://github.com/tomscaria/aeon/pull/12
Issues filed: none (ISS-015 already covers the only HIGH vector)

Remaining: ~25 inactive skills need second-pass Constraints; firecrawl-* family (13 skills) needs operator-reviewed Sandbox stubs
