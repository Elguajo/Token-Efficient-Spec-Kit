# Superpowers Integration

Role: implementation discipline.

Repository:

https://github.com/obra/superpowers

## Use it for

```text
TDD
systematic debugging
executing accepted plans
verification
implementation/code-review habits
branch finishing
```

## Do not use it for by default

When Spec Kit has already produced accepted project/feature artifacts, do not create a second canonical:

```text
brainstorm
product spec
implementation plan
roadmap
```

This avoids duplicated context and conflicting plans.

## Installation

Installation is harness-specific and changes over time.

The setup agent must read the current official Superpowers README/instructions before installing.

Examples of currently documented paths include:

```text
Claude Code
→ official/plugin marketplace installation

Cursor
→ plugin marketplace

Codex
→ Codex-specific installation instructions in the Superpowers repository

Gemini CLI
→ Gemini extension installation
```

Do not hardcode a stale installation method when the current upstream documentation exposes a native plugin path.

## Spec Kit bridge

Recommended profile also installs:

```text
speckit-superpowers-bridge
```

through Spec Kit's extension catalog when available.

Purpose:

```text
Spec Kit = WHAT
Superpowers = HOW
Bridge = handoff + guard rails
```

The bridge should prevent planning/execution ownership from overlapping unnecessarily.

## Verification

After installation, verify that a new agent session can discover Superpowers skills and that the workflow does not override the project's Constitution or canonical Spec Kit artifacts.
