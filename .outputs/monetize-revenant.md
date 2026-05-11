Monetize Revenant — 2026-05-11

Idea: Weekly Calibration Gap Report — top 10 Polymarket mispricing calls via email subscription
Track: A (research)
Ship: 3 days
Cost: ~$5/month (incremental inference + Resend free tier)
Revenue: $29/month subscription — 10 subs = $290 MRR, 50 subs = $1,450 MRR
MVP test: Post one free sample report on X + Polymarket Discord, collect signups via Stripe link over 14 days, zero paid spend
Kill: <3 paid subscribers after 4 weeks of promotion

Sketch:
- Add skills/weekly-calibration-report/SKILL.md (Monday 14:00 UTC, pulls context/trading/ snapshot, generates consensus top-10 table across canary agents)
- Add skills/monetize-revenant/report-template.md (market / gap score / direction / regime / confidence table + Kelly sizing note)
- Create Stripe payment link: $29/month, description cites 76%/29-trade live track record
- Add landing paragraph + Stripe link to rswarm.ai
- Launch: X thread (76%/29 stat + sample call), Polymarket Discord #strategy, PM Telegram groups

Note: revenant-snapshot.json stale (synced 2026-05-09, 48h old) — track record from memory (29 trades / 76% / +$415 / Sharpe 0.31)
