# Engineering Rules

1. Before coding read only Constitution, Project Brief, Architecture, current phase, relevant ADR/code/tests.
2. Use current stable dependencies; verify official docs for fast-changing/security-sensitive APIs.
3. Use strict typing where practical; do not hide type errors.
4. Secrets and privileged logic stay server-side.
5. Validate external input, API payloads, file metadata, env vars and provider/webhook payloads.
6. No empty catches; no stack traces/secrets to production clients.
7. Test core business rules, permissions, integrity, idempotency, important user flows and negative/security cases.
8. Persisted production schemas change via explicit migrations.
9. Do not log passwords, tokens, API keys, private signed URLs or full sensitive payloads.
10. User-facing apps include semantic UI, keyboard access, visible focus, labels, contrast and reduced motion where relevant.
11. Measure performance before exotic optimization; avoid obvious N+1, huge bundles/assets and unnecessary proxying.
12. Completion reports stay compact: DONE/NOT DONE, Implemented, Changed, Verification, Limitations, Next.
