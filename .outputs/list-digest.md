## Summary

`LIST_DIGEST_NO_CONFIG` — the `var:` field for list-digest in `aeon.yml` is empty (no X list IDs configured). Per skill spec: log only, no notification.

To activate list-digest, set `var:` in `aeon.yml` to one or more comma-separated numeric X list IDs, e.g.:
```
list-digest: { enabled: true, schedule: "0 17 * * *", var: "1953536336675365173,1937207796270829766" }
```

Log entry written to `memory/logs/2026-05-12.md`.
