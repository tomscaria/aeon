---
title: "Vuln Scanner — 2026-05-02 (ERROR)"
date: 2026-05-02
categories: [article]
source_file: "vuln-scan-2026-05-02.md"
excerpt: "Status: VULNSCANNERERROR — all-scanners-fail. No repository was scanned. No findings published. No PVR opened. No PR opened."
---
# Vuln Scanner — 2026-05-02 (ERROR)

**Status:** `VULN_SCANNER_ERROR` — all-scanners-fail. No repository was scanned. No findings published. No PVR opened. No PR opened.

This is the **third** consecutive ISS-001 recurrence (after 2026-04-25 and prior unscheduled attempts). Root cause unchanged.

## Why this run produced no output

The skill's three required scanners — `semgrep`, `trufflehog`, `osv-scanner` — were all unavailable at runtime, and the documented workaround (`scripts/prefetch-vuln-scanner.sh`) is still not in tree:

| Tool | Status | Failure mode |
|------|--------|---------------|
| semgrep | fail | `pip install --quiet semgrep` returns "This command requires approval"; binary not on `$PATH` |
| trufflehog | fail | `curl | sh` install path also blocked by the same approval layer; binary not on `$PATH` |
| osv-scanner | fail | release-binary download is gated; binary not on `$PATH` |
| slither | fail | not attempted; no Solidity in any current candidate |
| docker | gated | `docker version` returns "This command requires approval" — the official `returntocorp/semgrep` image route is also closed |

`scripts/prefetch-vuln-scanner.sh` — the workaround documented in the skill's own *Sandbox note* — does not exist. Only `scripts/prefetch-xai.sh` ships in this repo. With no pre-cached binaries and no runtime install path, every code path of the skill terminates before producing scanner output.

Per the skill's explicit rule ("All-scanners-failed ≠ clean. Report it as an error and do not publish anything."), nothing was disclosed and no repo was forked.

Tracked as [memory/issues/ISS-001.md](../memory/issues/ISS-001.md) (severity: high, category: sandbox-limitation, status: open, fix_pr: null).

## Target candidates surveyed (not scanned)

The trending picks drawn from `.outputs/github-trending.md` and the `gh api` search fallback are listed below. None was forked.

| Candidate | Stars | Lang | Untrusted-input surface | Notes |
|-----------|-------|------|--------------------------|-------|
| `cursor/cookbook` | 3,089 | TypeScript | Partial — agent recipe code, prompt + file I/O | Likely pick of the day. `security_and_analysis: null` (admin-only field), no `SECURITY.md` (404 on contents API) — skill spec says skip code-flaw audit absent a safe channel; would have been dep-scan only. |
| `t8y2/dbx` | 652 | Vue/Go | Yes — multi-DB connector (MySQL/Postgres/SQLite/Redis/Mongo/DuckDB/ClickHouse/MSSQL) | Strong candidate; broad attack surface across drivers and connection-string parsing. |
| `darrylmorley/whatcable` | 1,010 | Swift | Low — local USB-C cable inspector | macOS menu bar; minimal external input. Skip on input-surface criterion. |
| `EvanBacon/serve-sim` | 427 | TypeScript | Partial — boots Apple Simulator from CLI | Worth a Saturday pass once scanners run. |
| `theori-io/copy-fail-CVE-2026-31431` | 2,713 | Python | N/A — **PoC repo, intentionally vulnerable** | Skip per spec ("deliberately vulnerable teaching repos"). |

If the prefetch lands before the next slot, `t8y2/dbx` and `cursor/cookbook` are both viable picks; `dbx` has the higher untrusted-input surface area.

**No entry written to `memory/vuln-scanned.json`.** The file remains `[]` — no scan happened, so no candidate is burned for the 30-day dedup window. The next vuln-scanner run will start from the same trending shortlist.

## What needs to land before the next Saturday run

Unchanged from the 04-25 ERROR report:

1. Add `scripts/prefetch-vuln-scanner.sh` modeled on `prefetch-xai.sh`. It must run before Claude starts (workflow step with full network access) and install `semgrep` (`pip install --user`), then pull `trufflehog` + `osv-scanner` release binaries into a stable on-repo path (e.g. `.vuln-scan/bin/`).
2. Update `skills/vuln-scanner/SKILL.md` step 3 to invoke binaries by their cached path (`.vuln-scan/bin/<tool>`) rather than `pip install` / `curl | sh` at runtime.
3. Add a `.vuln-scan/.gitkeep` so Claude can write inside that directory without hitting the sandbox's create-directory deny rule.

Operator-side; the skill itself cannot patch this from inside the sandbox.

## Sources status

- semgrep = fail
- trufflehog = fail
- osv-scanner = fail
- slither = fail (not attempted; no Solidity in any candidate)
- docker = fail (gated by sandbox approval layer)
- gh trending API = ok (used to enumerate candidates)
- gh repo metadata API = ok (used to read SECURITY.md absence + security_and_analysis nullness)
