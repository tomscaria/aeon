# Watched Repos

Source of truth for which repos Aeon's repo-aware skills act on. Sub-bullets give skills per-repo focus when they need it (pr-review reads these; weekly-shiplog reads these for narrative angle).

- tomscaria/swarm-fund-mvp
  - pr-review focus: review parallel-session PRs against ADRs in DECISIONS.md and conventions in CLAUDE.md. Block on: untested logic, hardcoded secrets, schema changes without migration, removal of risk gates.
  - weekly-shiplog focus: LP/grant-committee narrative — milestones, lifecycle counts (Birth/Canary/Apex/Revenant), trade tape highlights.

- tomscaria/thomas-os
  - pr-review focus: data integrity in committed JSON (resume bullets, opportunities, pipelines), no PII leaks (emails/phones outside contact card), frontend regressions in src/. Block on: hardcoded credentials in scripts/, broken vite build, schema-incompatible edits to data/*.json.
  - weekly-shiplog focus: job-search progress — interviews active, opportunities added, resumes shipped, pipelines moved.

- tomscaria/lore-financial-teaser
  - pr-review focus: marketing copy correctness, broken external links, no broken builds. Block on: unverifiable financial claims, leaked unreleased product names.

- tomscaria/lore-sdk-product
  - pr-review focus: API contract stability (no silent breaking changes), test coverage on new endpoints, sane error responses. Block on: removed-without-deprecation public methods, unhandled secrets in committed configs.
  - weekly-shiplog focus: SDK adoption signals — installs, integrations, public examples shipped.
  - NOTE: assumed mapping for "lore-as-a-service" — confirm this is the right repo.

- tomscaria/prysm_alpha
  - pr-review focus: trading-loop correctness, no hardcoded API keys, idempotency of order placement. Block on: removed risk checks, untested execution paths.
  - weekly-shiplog focus: strategy progress — signals fired, P&L delta, regime shifts.
  - NOTE: assumed mapping for "prysm-squads-mvp" — confirm this is the right repo.

- aaronjmars/aeon
  - read-only — upstream observation. Not a PR target. Skills should skip PR-creating steps for this entry. The weekly upstream-sync workflow handles merging upstream changes into the fork via a separate channel.
