# Tooling Ownership Policy

Purpose: prevent duplicate planning, duplicate context and conflicting agent instructions.

## Core rule

**Token-Efficient Spec Kit is the canonical orchestration and specification layer.**

External tools may strengthen implementation, review or research, but they do not become the project source of truth.

## Ownership matrix

| Concern | Owner | Supporting tool |
|---|---|---|
| User outcome | Token-Efficient Project Brief | — |
| Global principles | Constitution | — |
| Architecture | Token-Efficient Architecture | gstack may review |
| Roadmap / phases | Token-Efficient Roadmap + phase files | — |
| Phase scope / tasks | Current phase | optional GitHub Spec Kit in Advanced Spec Mode |
| Acceptance criteria / convergence | Token-Efficient current phase | gstack review where useful |
| Context routing | Token-Efficient Spec Kit | — |
| Session handoff | Token-Efficient Spec Kit | — |
| Implementation discipline | Superpowers | native coding agent |
| TDD | Superpowers | project test tooling |
| Systematic debugging | Superpowers | gstack investigation may assist |
| Fresh library/API docs | Context7 | official primary docs when critical |
| Product/design critique | gstack | project UI specs |
| Code review | gstack / native agent review | Superpowers verification |
| Browser QA | gstack | Playwright/project E2E |
| Release readiness | Token-Efficient gates + gstack | CI |
| Formal deep specification | Optional GitHub Spec Kit | only Advanced Spec Mode |
| Final source of truth | repository canonical docs + code/tests | never external skill output alone |

## Default workflow

```text
User outcome
→ Project Brief
→ Architecture
→ Roadmap
→ Current Phase
→ 1–3 tasks
→ Superpowers/native implementation
→ tests
→ selective gstack review/QA
→ convergence
→ NEXT SESSION PROMPT
```

## Superpowers owns HOW

Use for:

```text
TDD
execution discipline
systematic debugging
verification
```

Do not let it silently replace accepted Project Brief, Architecture, Roadmap or phase scope with a second canonical planning system.

## gstack is a challenge layer

Recommended use:

```text
risky design → engineering review
UI-heavy work → design review
after important implementation → code review
web flows → browser QA
before release → ship/release checks
```

Do not run every gstack skill after every tiny task.
Do not use gstack autoplan as a parallel canonical roadmap unless the user explicitly requests a rethink.

## Context7 is on-demand

Use when implementation depends on current library/framework/provider APIs.
Do not fetch docs for stable language basics or every trivial edit.
For security/payment/production-critical decisions, verify primary official sources when needed.

## GitHub Spec Kit — Optional Advanced Spec Mode

GitHub Spec Kit is **not required by the default workflow**.

Enable it only when formal feature-level specification adds clear value, such as:

```text
payments
complex authorization
multi-tenancy boundaries
public APIs
critical migrations
large ambiguous features
cross-system high-risk integrations
```

When enabled:

```text
Token-Efficient Spec Kit
= project-level intent, architecture, roadmap, phase boundaries, handoff

GitHub Spec Kit
= optional deep specification inside the current phase

Superpowers
= implementation discipline
```

If a Spec Kit ↔ Superpowers bridge is used, it exists only to coordinate that optional Advanced Spec Mode.

## Token rule

A tool being installed does **not** mean its instructions should be loaded in every session.
Invoke only the capability that benefits the current task.
