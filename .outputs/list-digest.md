## Summary

`list-digest` exited with `LIST_DIGEST_NO_CONFIG`. The `var:` field is absent from the `list-digest` entry in `aeon.yml` — no X list IDs are configured. No `.xai-cache` exists, and no `XAI_API_KEY` path is available, so there is no fallback fetch path either.

Per the skill spec: log only, no notification sent.

To activate this skill, add numeric X list IDs to `aeon.yml` under `list-digest`:
```yaml
list-digest: { enabled: true, schedule: "0 17 * * *", var: "LIST_ID1,LIST_ID2" }
```
This is already flagged in MEMORY.md under the Operator config sweep (`add var: to digest/list-digest/refresh-x/remix-tweets in aeon.yml`).
