# AGENTS.md — Token-Efficient Spec Kit

## Core ownership

Token-Efficient Spec Kit is the canonical project workflow.
It owns:

```text
intent
Project Brief
Architecture
Roadmap
phases
phase tasks
acceptance criteria
context routing
quality routing
convergence
session handoff
```

External tools are optional capabilities, not project-level sources of truth.

## Default read set

For normal implementation read only:

```text
.specify/memory/constitution.md
docs/project/PROJECT_BRIEF.md
docs/project/ARCHITECTURE.md
docs/system/ENGINEERING_RULES.md
docs/system/SESSION_HANDOFF.md
current phase
relevant ADR only if needed
relevant code/tests
```

Never load all project documentation automatically.

## Decision autonomy

Make normal engineering decisions yourself.
Ask only true blockers or irreversible/high-impact approvals.
Choose one recommended default instead of making the user select routine technologies.

## Creative autonomy

Improve unspecified UX, product and implementation details when this supports the requested outcome.
Never override explicit user constraints.

## Complexity

Prefer the simplest safe architecture that satisfies current requirements and realistic near-term growth.
Do not introduce sophisticated infrastructure without evidence.

## Freshness

For fast-changing libraries, providers, coding tools, security APIs and installation procedures, consult current official documentation before implementation.

## Scope

Work on one current phase.
Usually implement only 1–3 cohesive tasks per run.

## Recommended tooling profile

```text
Token-Efficient Spec Kit
→ CORE: WHAT + orchestration + context + handoff

Superpowers
→ HOW: implementation discipline, TDD, systematic debugging, verification

gstack
→ challenge/review layer: engineering/design review, code review, browser QA, release checks

Context7
→ fresh library/API documentation on demand
```

### Optional Advanced Spec Mode

GitHub Spec Kit is not part of the default profile.
Enable it only when the current phase benefits from formal deep specification.

Examples:

```text
payments
complex authorization
multi-tenancy boundaries
public API contracts
critical migrations
large ambiguous cross-system features
```

When enabled:

```text
Token-Efficient Spec Kit = project-level source of truth
GitHub Spec Kit = optional deep phase-level spec/planning
Superpowers = HOW
Spec Kit ↔ Superpowers bridge = optional coordination only
```

Do not create a second project roadmap or duplicate canonical project docs.

## Tooling policy

Read `integrations/TOOLING_POLICY.md` only when configuring/invoking integrations or when ownership is ambiguous.

Installed does not mean always loaded.
Invoke a tool only when the task benefits from it.

## Security-sensitive work

For auth, payments, private files, permissions, destructive migrations or external webhooks:

- verify current primary documentation;
- validate inputs;
- keep privileged state server-authoritative;
- add negative tests;
- preserve idempotency/data integrity where relevant.

## Completion

Evidence before claims.
Run relevant:

```text
lint
typecheck
tests
build
e2e/manual QA
```

Do not weaken tests, access control or security just to achieve green status.

## Session handoff — mandatory

At the end of every meaningful coding/review session:

1. classify status as `IN PROGRESS`, `PHASE COMPLETE`, or `PROJECT COMPLETE`;
2. decide the next action from current acceptance criteria and roadmap;
3. update `docs/project/NEXT_SESSION.md`;
4. end with a ready-to-copy `NEXT SESSION PROMPT` for a fresh AI session.

If the phase is incomplete, continue the same phase.
If complete, start the next roadmap phase in the new session.
If project complete, route to release/audit or future `CHANGE_REQUEST` work.

The user must not be forced to invent the next engineering prompt.
