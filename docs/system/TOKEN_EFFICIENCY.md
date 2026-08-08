# Token Efficiency Protocol

This file is the **canonical definition of the Default Read Set**.
No other file may restate it. Other files must link here.

---

## Default Read Set

After project initialization, read exactly this for normal implementation, review,
bug fix, change request and project handoff work:

```text
1. .specify/memory/constitution.md
2. docs/project/PROJECT_BRIEF.md
3. docs/project/ARCHITECTURE.md
4. docs/project/ROADMAP.md
5. docs/system/ENGINEERING_RULES.md
6. the current phase file
7. only the ADRs, source files and tests directly relevant to the current tasks
```

`ROADMAP.md` is mandatory for product work because its marker is the canonical
current-phase pointer and one of the three project handoff outputs (see below).

An uninitialized template has no product state to read or hand off. Framework-only
audits and framework updates use their own explicitly scoped read instructions and
must not initialize or rewrite `docs/project/*`. See
[`SESSION_HANDOFF.md`](SESSION_HANDOFF.md#non-product-handoff-exceptions).

Deliberately NOT in the Default Read Set:

```text
docs/system/SESSION_HANDOFF.md    -> the handoff contract is already in AGENTS.md;
                                     read only when the handoff format is unclear
docs/system/TOKEN_EFFICIENCY.md   -> this file; read only when routing is unclear
docs/system/OPERATING_MODEL.md    -> project initialization only
docs/system/DECISION_FRAMEWORK.md -> material technology decisions only
docs/system/CREATIVE_AUTONOMY.md  -> project initialization only
integrations/*                    -> configuring or invoking an integration only
completed phases, all ADRs, full chat history
```

---

## Resolving the current phase

`docs/project/ROADMAP.md` carries a status marker on every phase and is the single
source of truth for which phase is current:

```text
- [x] Phase 00 - Foundation - COMPLETE
- [>] Phase 01 - Authentication - IN PROGRESS
- [ ] Phase 02 - Asset Library - PLANNED
```

Rules:

- exactly one phase may be marked `[>] IN PROGRESS`;
- the phase marked `[>]` is the current phase;
- if every phase is `[x]`, the project is complete;
- the marker is updated as part of the session handoff.

Never scan `docs/phases/` to guess which phase is current, and never rely on
`docs/project/NEXT_SESSION.md` for this. `NEXT_SESSION.md` is disposable navigation;
`ROADMAP.md` is canonical state. If the two disagree, `ROADMAP.md` wins and
`NEXT_SESSION.md` must be regenerated.

---

## Context pyramid

Always: the Default Read Set above.

Sometimes: a specific ADR, specific API docs, directly related prior phase output.

Rarely: master spec, all ADRs, all completed phases, full chat history.

---

## Canonical ownership

- Product truth -> PROJECT_BRIEF
- Chosen stack/system -> ARCHITECTURE
- Phase order and current-phase pointer -> ROADMAP
- Why a major decision -> ADR
- Current work -> phase spec
- Global principles -> Constitution
- Default Read Set and context routing -> this file

Do not duplicate the same explanation across files. A fact with two homes will
eventually have two different values.

---

## Phase format

Keep: Goal, Context, In scope, Out of scope, Tasks, Acceptance criteria,
Security/negative tests if relevant, Verification.

Phase files live at `docs/phases/NN-kebab-name.md`. See `docs/phases/README.md`.

---

## Granularity

Normally plan 1–3 related tasks per implementation batch. This is a planning
guideline, not a completion gate: a phase is `PHASE COMPLETE` exactly when its
acceptance criteria have been verified, regardless of batch size. An external
blocker that prevents verification must be reported as the actual reason the phase
remains in progress.

---

## Research notes

Save only conclusions and links that influence implementation.

---

## Load larger context only when

- compact docs conflict;
- cross-phase invariant is unclear;
- a major change affects architecture;
- debugging spans several subsystems.
