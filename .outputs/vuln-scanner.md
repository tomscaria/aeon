The workspace clone is large — I'll leave cleanup to the GH Actions post-run step since `rm -rf` on the clone directory is blocked. The key outputs are all written. Let me do a final check of what was produced.

## Summary

**Skill: vuln-scanner — docusealco/docuseal v2.5.2**

**Target selected:** `docusealco/docuseal` — Ruby on Rails document-signing platform, ~16k stars, trending 59× baseline on 2026-05-08. Has SECURITY.md with `security@docuseal.com`. PVR endpoint accessible but returned 403 (token lacks `repository_advisories:write` on the target repo).

**Scanner results:**
- semgrep=fail, trufflehog=fail, osv-scanner=fail — all three blocked by GitHub Actions sandbox
- manual code review = ok (controllers, services, jobs, lib/, JS frontend)

**12 candidates reviewed. 1 confirmed finding.**

---

**Finding: SSRF via Webhook URL on Self-Hosted Instances**  
Severity: Medium | CWE-918  
File: `lib/send_webhook_request.rb:24-28`

The localhost/HTTPS protection block is gated on `Docuseal.multitenant?`. Self-hosted installs have `multitenant? = false` → no URL restrictions → any host is reachable including `http://169.254.169.254/` (AWS IMDS), internal VPC services, Docker bridge. Webhooks fire automatically on any form event. Blind SSRF (200-response bodies not stored), but enables port scanning and side-effect triggering on internal APIs. Requires admin-level access to configure.

Secondary gap: `DownloadUtils::LOCALHOSTS` omits RFC-1918 private ranges and link-local (169.254.0.0/16).

**Disclosure channel:** PVR returned 403 → email draft saved to `.pending-disclosure/docusealco-docuseal-2026-05-09.md` for manual send to `security@docuseal.com`.

**Files produced:**
- `articles/vuln-scan-2026-05-09.md` — local report
- `.pending-disclosure/docusealco-docuseal-2026-05-09.md` — email draft
- `memory/vuln-scanned.json` — dedup state (skip docuseal until 2026-06-08)
- `.pending-notify/vuln-scanner-2026-05-09.md` — notification queued
- `memory/logs/2026-05-09.md` — log entry appended
