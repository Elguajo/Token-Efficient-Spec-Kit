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

Defined once in `docs/system/TOKEN_EFFICIENCY.md`. Read it from there; it is not
restated here, so there is no second copy to drift.

The current phase is resolved from the status markers in `docs/project/ROADMAP.md`,
never by scanning `docs/phases/`.

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
Normally plan 1–3 cohesive tasks per implementation batch. This is a planning
guideline, not a completion gate: determine phase status only from verified
acceptance criteria, never from the number of tasks in a run. If an external
blocker prevents verification, name that concrete blocker rather than blaming the
batch guideline.

## Recommended tooling profile

```text
Token-Efficient Spec Kit
→ CORE: WHAT + orchestration + project/docs context + handoff

Semble
→ CODE DISCOVERY: intent-based semantic/hybrid retrieval

Serena
→ SYMBOL / REFACTOR: references, implementations, diagnostics, semantic edits

RTK
→ TOOL OUTPUT: compact terminal/test/build/git output

Superpowers
→ HOW: implementation discipline, TDD, systematic debugging, verification

gstack
→ challenge/review layer: engineering/design review, code review, browser QA, release checks

Context7
→ fresh library/API documentation on demand
```
> Canonical profile definition: [`integrations/PROFILES.md`](integrations/PROFILES.md). This listing is a copy for reading convenience — if the two disagree, PROFILES.md wins.


### Token-efficiency routing

Use the smallest context source that can answer the current question.

```text
Project/docs context
→ canonical Token-Efficient project files

Intent question / unfamiliar code area / “where is X implemented?”
→ Semble

Known symbol / references / implementations / diagnostics / semantic rename or edit
→ Serena

Semble already found the exact relevant symbol
→ do NOT repeat broad discovery in Serena
→ use Serena only for the distinct symbol-level operation

Known tiny file/string edit
→ native exact search/read/edit is fine

Verbose supported shell output
→ prefer RTK when verified safe

Fresh external API/library behavior
→ Context7 / current primary docs on demand
```

Do not independently call Semble + Serena + grep for the same discovery question.
A second tool is justified when it answers a different question, verifies an ambiguous result, or provides a fallback after failure.

Serena should be configured according to `integrations/SERENA.md` so generic file/search/shell/memory tools are excluded when current upstream supports that configuration.
Serena memory must not compete with Project Brief / Architecture / Roadmap / NEXT_SESSION.

Do not use Semble just because it is installed when a direct small read is cheaper.
Do not use RTK when raw output is needed or filtering may remove critical diagnostics.
Correctness outranks token savings.

If Semble, Serena or RTK is unavailable or unsafe, degrade gracefully to native targeted tools. They must not block product work.

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

Installed does not mean always loaded or always called.
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
3. update the phase markers in `docs/project/ROADMAP.md` so exactly one phase is
   `[>] IN PROGRESS`, or all are `[x]` when the project is complete;
4. update `docs/project/NEXT_SESSION.md`;
5. end with a ready-to-copy `NEXT SESSION PROMPT` for a fresh AI session.

If the phase is incomplete, continue the same phase.
If complete, start the next roadmap phase in the new session.
If project complete, route to release/audit or future `CHANGE_REQUEST` work.

The user must not be forced to invent the next engineering prompt.

Exception: if the template is not initialized, or the task is a framework-only
audit/update, do not initialize or modify `docs/project/*`. Still provide a
ready-to-copy `NEXT SESSION PROMPT`: route an uninitialized template to
`prompts/START_NEW_PROJECT.md`; for framework-only work, name the next framework
action or preserve the existing product handoff. The full contract is in
`docs/system/SESSION_HANDOFF.md`.

## Project Doctor

Use `prompts/PROJECT_DOCTOR.md` when the user wants a human-friendly status explanation or when the current next action is unclear.

Project Doctor is diagnostic by default. It must not implement unrelated product work merely to improve the health report.

## Workflow Self-Audit

Use `prompts/AUDIT_WORKFLOW.md` after significant framework changes or when framework instructions appear contradictory.

Self-Audit checks the workflow itself, not normal application code.
Do not load it into every implementation session.

## Framework versioning

In this source repository, the current framework version lives in:

```text
VERSION
```

The generated Starter keeps its installed workflow version in:

```text
.token-efficient-spec-kit/VERSION
```

Material framework behavior changes in this source repository must update:

```text
VERSION
CHANGELOG.md
```

Use Semantic Versioning principles.

## Safe framework updates

Framework updates must follow:

```text
docs/system/WORKFLOW_UPDATE_POLICY.md
prompts/UPDATE_WORKFLOW.md
```

Never blindly overwrite project-owned state.

Project-owned includes:

```text
docs/project/*
docs/phases/*
docs/decisions/*
application source code
tests
migrations
credentials/secrets
```

Merge-sensitive files include:

```text
.specify/memory/constitution.md
AGENTS.md
```

After a framework update, run Workflow Self-Audit before considering the update healthy.
