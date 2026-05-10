`memory/on-chain-watches.yml` exists with `watches: []` — no `type: wallet` entries. Skill exited clean per spec: no notification sent, logged `TREASURY_INFO_OK — no wallets configured` to `memory/logs/2026-05-10.md`.

To activate treasury-info, edit `memory/on-chain-watches.yml` to add real wallet addresses under `watches:` with `type: wallet`.

## Summary

- Read `memory/on-chain-watches.yml`: file exists, `watches: []`, zero wallet entries.
- Per skill spec (file exists, zero `type: wallet` entries): log and exit 0, no notification.
- Logged `TREASURY_INFO_OK — no wallets configured` to `memory/logs/2026-05-10.md`.
- Follow-up: populate `memory/on-chain-watches.yml` with real addresses to enable treasury monitoring. This is already flagged in MEMORY.md Next Priorities under "Operator config sweep."
