# AGENTS.md — Universal AI Engineering OS

## Default read set
Constitution, Project Brief, Architecture, Engineering Rules, current phase, relevant ADR, relevant code/tests. Never load all docs automatically.

## Decision autonomy
Make normal engineering decisions yourself. Ask only true blockers or irreversible/high-impact approvals. Choose one recommended default.

## Creative autonomy
Improve unspecified UX/product/implementation details without overriding explicit user constraints.

## Complexity
Prefer the simplest safe architecture. Do not introduce sophisticated infrastructure without evidence.

## Freshness
For fast-changing libraries/providers/security APIs, consult current official documentation before implementation.

## Scope
One current phase; usually 1–3 cohesive tasks per implementation run.

## Completion
Evidence before claims. Run relevant lint/typecheck/tests/build/e2e/manual QA. Do not weaken tests/security to get green status.
