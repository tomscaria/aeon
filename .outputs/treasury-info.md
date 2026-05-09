## Summary

`memory/on-chain-watches.yml` exists with `watches: []` — no `type: wallet` entries configured. Per the skill spec, no notification is sent and no snapshot is written.

Logged `TREASURY_INFO_OK — no wallets configured` to `memory/logs/2026-05-09.md`. To enable treasury tracking, add real wallet addresses to `memory/on-chain-watches.yml` under the `watches:` key.
