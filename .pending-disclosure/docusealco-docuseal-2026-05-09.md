---
repo: docusealco/docuseal
version: 2.5.2
detected_at: 2026-05-09T00:00:00Z
contact: security@docuseal.com
channel: email
status: pending
pvr_attempted: true
pvr_result: 403 (token lacks repository_advisories:write on target repo)
---

To: security@docuseal.com
Subject: [Security] SSRF via webhook URL on self-hosted instances (DocuSeal ≤ 2.5.2)

Hi DocuSeal security team,

I am reporting a Server-Side Request Forgery (SSRF) vulnerability affecting self-hosted DocuSeal installations. This was discovered via automated code review.

---

**Severity:** Medium
**CWE:** CWE-918 (Server-Side Request Forgery)
**Affected versions:** All versions tested against ≤ 2.5.2 (self-hosted deployments)
**Cloud/multitenant:** Not affected (protection is in place)

---

## Summary

In self-hosted deployments, DocuSeal makes outbound HTTP requests to user-configured webhook URLs without any network destination restrictions. The localhost/HTTPS enforcement is gated on `Docuseal.multitenant?`, which is `false` in every self-hosted installation.

## Location

`lib/send_webhook_request.rb:24-28`

```ruby
if Docuseal.multitenant?
  raise HttpsError, 'Only HTTPS is allowed.' if (uri.scheme != 'https' || [443, nil].exclude?(uri.port)) &&
                                                !AccountConfig.exists?(key: :allow_http, ...)
  raise LocalhostError, "Can't send to localhost." if uri.host.in?(LOCALHOSTS)
end
```

The entire protection block is skipped when `multitenant?` is false (i.e., in all self-hosted installs).

## Impact

An authenticated admin or account-owner can configure a webhook URL pointing to any reachable host, including:
- Cloud provider instance metadata endpoints: `http://169.254.169.254/latest/meta-data/` (AWS), `http://metadata.google.internal/` (GCP), `http://169.254.169.254/metadata/` (Azure)
- Internal VPC services: Redis, internal admin APIs, sidecar containers
- Docker bridge gateway: `172.17.0.1`

The webhook fires automatically on form.completed, form.started, submission.created, and other events — no manual trigger needed after initial configuration.

Exploitation enables blind port scanning of internal infrastructure, interacting with internal services that trust the DocuSeal server's IP, and on AWS without IMDSv2 enforcement, reaching IAM role metadata endpoints.

Note: response bodies are not stored in the UI for HTTP 200 responses, so this is a blind SSRF. Timing-based port enumeration and side-effect triggering on internal APIs are the primary exploitation paths. Cloud credential exfiltration would require an additional out-of-band channel.

## Proof of exploitation

1. Deploy self-hosted DocuSeal (any version, default config).
2. As admin: Settings → Webhooks → add URL `http://169.254.169.254/latest/meta-data/` (or any internal address on your test network).
3. Submit any form to fire `form.completed`.
4. Observe via host-level traffic capture that the server POST-ed to that address.

## Secondary gap

`DownloadUtils::LOCALHOSTS` (shared with the webhook check and used for URL-based file uploads) covers loopback aliases but omits RFC-1918 private ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) and link-local (169.254.0.0/16). The file-upload callers use `validate: true` which adds an HTTPS requirement, so cloud metadata services (HTTP-only) are blocked there. But internal HTTPS services on private IPs would still be reachable via `DownloadUtils.call`.

## Suggested fix

Remove the `Docuseal.multitenant?` gate so protection applies to all deployment modes. Operators who need HTTP webhooks to controlled internal endpoints can be given an explicit override mechanism:

```ruby
# lib/send_webhook_request.rb — apply unconditionally
unless AccountConfig.exists?(key: :allow_http, account_id: webhook_url.account_id)
  raise HttpsError, 'Only HTTPS is allowed.' if uri.scheme != 'https' || [443, nil].exclude?(uri.port)
end
raise LocalhostError, "Can't send to localhost." if uri.host.in?(LOCALHOSTS) || private_address?(uri.host)
```

Also consider adding `private_address?` to cover RFC-1918 + 169.254/16 in both `SendWebhookRequest` and `DownloadUtils`.

---

This disclosure was prepared responsibly. I have not published these findings publicly. Happy to coordinate a CVE assignment if needed.

Reported by: Aeon (autonomous security scanner, aeonframework)
