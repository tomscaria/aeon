`on-chain-watches.yml` has `watches: []` — no addresses configured.

Per the skill spec: log `ON_CHAIN_NO_CONFIG`, no notification, exit cleanly. Log entry appended to `memory/logs/2026-05-12.md`.

## Summary

- Read `skills/on-chain-monitor/SKILL.md` and `memory/on-chain-watches.yml`.
- Config contains `watches: []` — operator has not populated any addresses.
- Skill exited with `ON_CHAIN_NO_CONFIG` per spec. No notification sent.
- Logged to `memory/logs/2026-05-12.md`.

To activate this skill, populate `memory/on-chain-watches.yml` with one or more watch entries (see the config schema in the skill file).
