# AGENTS.md — Token-Efficient Spec Kit

## Default read set

For normal implementation read only:

```text
.specify/memory/constitution.md
docs/project/PROJECT_BRIEF.md
docs/project/ARCHITECTURE.md
docs/system/ENGINEERING_RULES.md
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

Improve unspecified UX, product and implementation details when this improves the requested outcome.
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

When the Recommended profile is installed, responsibilities are separated:

```text
Token-Efficient Spec Kit
→ project intent, architecture, context discipline

GitHub Spec Kit
→ canonical specification, plan, tasks, analysis, convergence

Superpowers
→ implementation discipline, TDD, systematic debugging, verification

Superpowers Implementation Bridge
→ prevents duplicate planning/execution ownership

gstack
→ engineering/design challenge, code review, browser QA, release checks

Context7
→ fresh library/API documentation on demand
```

Read `integrations/TOOLING_POLICY.md` only when the current task invokes or configures one of these tools.

### Important ownership rule

Do not create parallel canonical plans.

If an accepted Spec Kit spec/plan/tasks already exist:

- do not replace them with Superpowers brainstorming/planning;
- do not replace them with gstack autoplan;
- use gstack as a review/challenge layer;
- use Superpowers for implementation discipline;
- use Context7 only when fresh docs are useful.

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
