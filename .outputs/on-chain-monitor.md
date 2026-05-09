`ON_CHAIN_NO_CONFIG` — `memory/on-chain-watches.yml` exists but `watches: []`. No events fetched, no notification sent.

To activate this skill, populate `memory/on-chain-watches.yml` with real addresses (the template is already in the file — uncomment and edit the Treasury/Ops/Solana-Hot entries). This is flagged in MEMORY.md under "Operator config sweep (BLOCKED)."

## Summary

- Ran `on-chain-monitor` 2026-05-09.
- Outcome: `ON_CHAIN_NO_CONFIG`. Config file present but `watches: []`.
- No data fetched, no notification sent.
- Logged to `memory/logs/2026-05-09.md`.
- Follow-up: operator must add real addresses to `memory/on-chain-watches.yml` to enable monitoring.
