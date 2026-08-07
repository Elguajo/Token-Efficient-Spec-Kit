# Context7 Integration

Role: fetch current, version-relevant library and API documentation only when needed.

Repository:

https://github.com/upstash/context7

## Why it is included

Coding agents often know an older version of a framework or invent APIs that no longer exist.

Context7 provides a dedicated documentation lookup layer without forcing large documentation dumps into every session.

## Recommended behavior

Use Context7 when:

- installing/configuring a current library;
- using framework/provider APIs that change frequently;
- implementing auth, deployment, storage, payments or SDK integration;
- the agent is uncertain about a method/signature/version;
- current official examples materially reduce implementation risk.

Do not use it for:

- basic language syntax;
- code already fully described by local types/tests;
- every trivial edit.

## Installation

Current upstream setup supports an interactive installer:

```bash
npx ctx7 setup
```

It can configure CLI/Skills or MCP modes and supports multiple coding harnesses.

The setup agent must read the current Context7 README before installation and choose the native path for the active harness where available.

For Codex and other MCP-capable clients, Context7 can also be configured as an MCP server. Prefer credentials via environment/header configuration; never commit API keys to the repository.

## Security

Never add a real Context7 API key to:

```text
README
AGENTS.md
tracked .env
MCP config committed with secrets
```

## Context rule

Installed does not mean always invoked.

Only retrieve the narrow documentation needed for the current decision or implementation task.

For critical security/payment behavior, verify important claims against the primary official provider documentation as well.
