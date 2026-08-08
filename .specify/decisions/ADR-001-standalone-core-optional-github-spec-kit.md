# ADR-001 — Token-Efficient Spec Kit as Standalone Core

Status: Accepted

Scope: framework decision. Lives in `.specify/decisions/` so that framework updates
can maintain it and so that it does not consume a number in the product's own
`docs/decisions/` sequence.

## Context

The project originally evolved as a lightweight workflow layered on top of GitHub Spec Kit.

Over time Token-Efficient Spec Kit gained its own project-level capabilities:

```text
User Intent
Project Brief
Architecture
Roadmap
Phases
Phase Tasks
Acceptance Criteria
Context Routing
Quality Routing
Convergence
Session Handoff
NEXT SESSION PROMPT
```

Keeping GitHub Spec Kit mandatory would duplicate specification/planning artifacts for many ordinary projects and increase setup/context overhead.

This conflicts with the project's primary goal: use the smallest amount of process and context that still preserves engineering quality.

## Decision

Token-Efficient Spec Kit becomes the standalone canonical project workflow.

This ADR deliberately does **not** list the Recommended tooling profile. The profile
changes between minor versions; a copy here would go stale and contradict the
canonical source. The profile and the ownership matrix live in
`integrations/TOOLING_POLICY.md`.

What this decision fixes, and what remains true regardless of the profile:

```text
Token-Efficient Spec Kit
= WHAT + project orchestration + project memory + phases + convergence + handoff
= the project-level source of truth

every external tool
= an optional capability, never a second canonical planning system
```

GitHub Spec Kit is moved to Optional Advanced Spec Mode.

It may be enabled for individual phases when formal deep specification clearly improves quality, such as:

- payments;
- complex authorization;
- multi-tenant isolation;
- critical migrations;
- public API contracts;
- large ambiguous cross-system features.

A Spec Kit ↔ Superpowers bridge is optional and relevant only when Advanced Spec Mode enables both tools.

## Consequences

### Positive

- fewer mandatory dependencies;
- lower setup overhead;
- fewer duplicate specs/plans/tasks;
- lower context/token cost;
- simpler mental model for non-developers;
- Token-Efficient Spec Kit has clear independent product identity;
- formal Spec Kit rigor remains available when actually useful.

### Tradeoffs

- the project must maintain its own phase/spec/convergence conventions;
- it does not inherit every GitHub Spec Kit CLI command by default;
- Advanced Spec Mode requires an explicit install/activation step;
- optional integration paths must be kept compatible with upstream changes.

## Revisit when

Reconsider this decision if:

- GitHub Spec Kit gains a near-zero-overhead embedded mode that no longer duplicates project-level artifacts;
- Token-Efficient core becomes unable to express required formal specification needs cleanly;
- maintaining independent workflow conventions becomes materially more expensive than delegating them to an external framework.

Until then, GitHub Spec Kit remains optional.
