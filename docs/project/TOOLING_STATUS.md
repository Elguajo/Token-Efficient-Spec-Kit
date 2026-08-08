# Tooling Status

Status: Not initialized.

Run automatically from:

```text
prompts/START_NEW_PROJECT.md
```

or manually:

```text
prompts/SETUP_RECOMMENDED_TOOLING.md
```

The setup agent should replace this file with a concise record:

```text
Checked at:
OS:
Active coding harness:
Profile: Recommended / Minimal / Custom

Core:
Token-Efficient Spec Kit: READY

Recommended external tooling:
Superpowers:
Semble:
Semble integration mode:
Serena:
Serena backend/integration mode:
Serena overlap policy: ACTIVE / PARTIAL / N/A
RTK:
RTK integration scope:
gstack:
Context7:

Token-efficiency verification:
Intent-based code discovery: Semble READY / DEGRADED / N/A
Symbol/refactor layer: Serena READY / DEGRADED / PENDING / N/A
Shell/tool output: RTK READY / DEGRADED / N/A

Optional Advanced Spec Mode:
GitHub Spec Kit: NOT ENABLED / ENABLED
Spec Kit ↔ Superpowers bridge: NOT ENABLED / ENABLED / N/A

Verification:
Manual action required:
```

Rules:

- Tooling bootstrap runs once per relevant environment/harness state, not every session.
- Semble, Serena and RTK are Recommended capabilities but must degrade gracefully if unavailable or unsafe for the active harness/project language.
- Semble owns broad intent-based code discovery; Serena owns symbol semantics/refactoring. Do not use both to rediscover the same code by default.
- Serena generic file/search/shell/memory tools should be excluded according to `integrations/SERENA.md` when current upstream supports it.
- GitHub Spec Kit and its bridge are optional and must not be treated as missing dependencies when Advanced Spec Mode is disabled.
- Never store API keys, tokens, OAuth secrets or other credentials here.
