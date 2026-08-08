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
RTK:
RTK integration scope:
gstack:
Context7:

Token-efficiency verification:
Code retrieval: Semble READY / DEGRADED / N/A
Shell/tool output: RTK READY / DEGRADED / N/A

Optional Advanced Spec Mode:
GitHub Spec Kit: NOT ENABLED / ENABLED
Spec Kit ↔ Superpowers bridge: NOT ENABLED / ENABLED / N/A

Verification:
Manual action required:
```

Rules:

- Tooling bootstrap runs once per relevant environment/harness state, not every session.
- Semble and RTK are Recommended capabilities but must degrade gracefully if unavailable or unsafe for the active harness.
- GitHub Spec Kit and its bridge are optional and must not be treated as missing dependencies when Advanced Spec Mode is disabled.
- Never store API keys, tokens, OAuth secrets or other credentials here.
