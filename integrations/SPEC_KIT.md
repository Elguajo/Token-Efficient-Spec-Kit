# GitHub Spec Kit Integration — Optional Advanced Spec Mode

GitHub Spec Kit is **not required by the default Token-Efficient workflow**.

Token-Efficient Spec Kit already owns project-level:

```text
intent
Project Brief
Architecture
Roadmap
phases
tasks
acceptance criteria
convergence
session handoff
```

GitHub Spec Kit is an optional capability for phases that benefit from deeper formal specification.

## Good triggers

Use Advanced Spec Mode when a phase is materially ambiguous, cross-cutting or high-risk, for example:

- payments;
- complex authorization;
- multi-tenant isolation;
- critical migrations;
- public API contracts;
- large cross-system integrations;
- difficult requirements where consistency analysis is valuable.

Do not enable it just because a project is large.

## Ownership when enabled

```text
Token-Efficient Spec Kit
= project-level source of truth, architecture, roadmap, phase boundary, handoff

GitHub Spec Kit
= formal specification/planning support INSIDE the current phase

Superpowers
= implementation discipline

gstack
= challenge/review/QA
```

Do not generate a second project roadmap or replace existing project-level docs.

## Typical Advanced flow

Use only the gates justified by the phase:

```text
current Token-Efficient phase
→ specify
→ clarify if consequential ambiguity exists
→ plan
→ checklist if risk justifies it
→ tasks
→ analyze if consistency/risk warrants it
→ implementation
→ converge
→ Token-Efficient NEXT SESSION handoff
```

For ordinary features, stay with the native Token-Efficient phase workflow.

## Installation

Installation changes over time. Before installing, use the current official GitHub Spec Kit documentation.

If both GitHub Spec Kit and Superpowers are enabled, a current supported bridge may be added to prevent duplicate planning/execution ownership. The bridge is optional and belongs only to Advanced Spec Mode.

## Important rule

Do not install or load GitHub Spec Kit in every project/session merely because integration support exists.

Token efficiency wins when formal tooling is activated only where its additional rigor is worth the context cost.

Official project:
https://github.com/github/spec-kit
