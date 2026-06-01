# Swarm Fund Wallet Inventory

**Last verified:** 2026-06-01 (this session). Verified against repo `.env` + live on-chain queries (HL info API, PM data API).

**Use this as the single source of truth.** If `.env` and this file disagree, `.env` wins — update this file. Previous sessions kept re-deriving the address ledger from MEMORY.md fragments; that pattern wasted ~30 min per "what's our address for X" question.

## Swarm-controlled operational wallets

| # | Address | Chain | Role | Env var | Funding state (verified) |
|---|---|---|---|---|---|
| 1 | `0x83F4c49cF459cAbEDE08228FC471Ab89D0B189e3` | Hyperliquid | HL trading wallet — perp + spot | `HYPERLIQUID_WALLET_ADDRESS` | **$115.82 spot USDC** (verified 2026-06-01 via `spotClearinghouseState`). $0 perp account value. $60 USDC deposited 2026-04-20 from Arbitrum bridge (ledger entry confirmed). Net +$55 since deposit, source unclear (spot trades? bridge top-up?). |
| 2 | `0xda510fce8d79da3095363d7230877f7900708d84` | Polygon | Polymarket signing EOA — signs orders on behalf of proxy | `POLY_USER_EOA` | No USDC held directly. Signs orders for #3. |
| 3 | `0x52EB75Ec04bA5C9AfF93BA65ef2078Eee6D8f0bD` | Polygon | Polymarket proxy — holds CTF shares, registered Builders Program profile | `POLY_FUNDER`, `POLY_BUILDER_PROFILE_ADDRESS` | **1 open position** (verified 2026-06-01 via `data-api.polymarket.com/positions`): "Will Mexico win the 2026 FIFA World Cup?" — 100 size YES @ 0.011, currently $-0.05 PnL. PM `/trades` endpoint returned only 1 trade for this wallet despite agent ledgers claiming 26 real PM trades over 30d — **reconciliation gap, see "Open issues" below**. |
| 4 | `0x97E246193a7fB9A1EAb6e017edEAb85ec761ca06` | Base | Bankr x402 micropayment wallet | `BANKR_X402_WALLET` | $50 USDC funded 2026-04-25 (per MEMORY.md). Funds AgenticBets / Alchemy / Quotient calls per-request. First Python-controlled agent x402 micropayment settled 2026-04-25 (receipt `rcpt_1764b016…`). |

## Shared infrastructure (NOT swarm-controlled, NEVER send tx FROM here)

| # | Address | What it is |
|---|---|---|
| 5 | `0x0a10e315183EcbecD2E5CF08DAD6E9d0535752B1` | Polymarket cross-chain deposit aggregator. Receive-only; `.env` comment marks it "for deposits only." |
| 6 | `0xcddc4ba3af4eaf360e52e18c676a827ca0bdea4681a135a47e8e802dcee8286f` | Polymarket Builder code (`POLY_BUILDER_CODE`) — 64-char identifier, NOT a wallet. Earns builder fees on orders signed with the Builders API keys. |
| 7 | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` | USDC token contract on Base. Standard, not ours. |

## Founder personal (separate, do NOT use for swarm)

| # | Address | Role |
|---|---|---|
| 8 | `0x84C6ed12B6fec50B4d4C89D379aFb8CfeF5b4e73` | Founder's personal wallet (`PERSONAL_WALLET_ADDRESS` in `dashboard/.env.local`). Read-only views in `/personal` dashboard route. NOT a swarm operational wallet. |

## Secrets in `.env` — security state

- **`.env` is gitignored** (line 23 of `.gitignore`) and has **never been committed**. Verified 2026-06-01.
- The strings `POLY_BUILDER_SECRET`, `BANKR_X402_PRIVATE_KEY` appear in 5 historical commits — these are env-var-name references in `.env.example` / docs, NOT the secret values themselves. Spot-verified.
- Cleartext private keys in `.env` include: `BANKR_X402_PRIVATE_KEY`, `POLY_BUILDER_SECRET`, `POLY_BUILDER_PASSPHRASE`. These are real keys with real funds attached. If the laptop is ever compromised these are at risk. Mitigations: 1Password integration is the obvious next step; current bridge is acceptable for prototype but should not survive past first material grant.

## Open issues (Codex follow-ups)

1. **PM trade reconciliation gap.** Agent ledgers (`data/agents/*.json`) show 26 `is_paper=false` PM trades over 30d. PM public data API `/trades` returns only 1 trade for proxy `0x52EB75…`. Possible causes: API pagination/limit; agent code recording trades that didn't fill on-chain; mismatch between agent-internal state and PM proxy reality. **Critical to resolve before the next grants pitch** — the founder's "production receipts" claim depends on reconciling these.

2. **HL spot $115.82 vs $60 deposit ledger.** Only one ledger entry (the +$60 from 2026-04-20). Where did the additional $55 come from? Possibly spot trades that don't show in `userNonFundingLedgerUpdates`. Codex: query `userFunding` or `userFills` for spot to confirm.

3. **PM proxy real-trade size.** The 1 verified open position is $1.10 of notional. If the historical 26-trade claim is real, total notional ever-deployed is probably <$50. Worth quantifying for Wednesday pitch sizing.

4. **Wallet env values in `dashboard/.env.local`** (live, not example) couldn't be read from this session — file appears to not exist OR be permission-restricted. If `PERSONAL_WALLET_ADDRESS` is wired into dashboard but `.env.local` is missing, the `/personal` route is silently broken. Codex check.

5. **No `kelly_paper_simulation_wallet` distinction.** Paper-mode trades have a simulated NAV ($112M aggregate across 180 agents per current `/api/portfolio`); live trades use the $115.82 unified HL NAV. These are tracked separately in the code but they share the same RiskGate `_DEFAULT_MIN_SIZE_USD = 5.0` floor — meaning paper trades are also silently dying at sub-$5 sizes on agents with small notional sims. Less critical than the live case but worth surfacing in the dashboard.

## How this file gets updated

- Whenever `.env` changes a wallet env var, update the matching row here.
- When a wallet is funded / drained / closed, update the "Funding state" column with the verification source (which API call, which timestamp).
- When founder rotates a key, remove the row's environmental detail and replace with the new key's first verification.
- Never paste private keys here. Only addresses.
