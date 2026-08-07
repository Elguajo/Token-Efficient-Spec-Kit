# GitHub Spec Kit Integration

Role: canonical specification/planning layer.

## Responsibilities

Spec Kit owns:

```text
constitution integration
feature specification
clarification
implementation plan
quality checklist when needed
task decomposition
cross-artifact analysis
convergence
```

## Install

Use current official installation instructions.

Current supported pattern:

```bash
uv tool install specify-cli
specify version
```

Initialize the current project with the appropriate agent integration:

```bash
specify init . --integration <agent>
```

Modern Spec Kit supports many agent integrations, including Codex and Claude Code. Always verify the currently supported integration key before automation.

## Existing template files

Token-Efficient Spec Kit already ships a custom:

```text
.specify/memory/constitution.md
```

During initialization, preserve this Constitution. If the installer needs `--force`, back up the existing Constitution and restore it afterward unless the user explicitly requests regeneration.

## Recommended workflow

Small/normal feature:

```text
specify
→ plan
→ tasks
→ implement/handoff
→ converge
```

Risky/ambiguous feature:

```text
specify
→ clarify
→ plan
→ checklist
→ tasks
→ analyze
→ implementation handoff
→ converge
```

Do not run every quality gate for every trivial task.

## Superpowers bridge

Recommended profile should install the community extension:

```bash
specify extension add speckit-superpowers-bridge
```

The bridge keeps Spec Kit as the design source of truth and Superpowers as implementation discipline.

Before installation, verify that the extension still exists in the current Spec Kit community catalog and read its current requirements.

Official references:

- https://github.github.com/spec-kit/
- https://github.github.com/spec-kit/installation.html
- https://github.github.com/spec-kit/reference/integrations.html
- https://github.github.com/spec-kit/reference/extensions.html
