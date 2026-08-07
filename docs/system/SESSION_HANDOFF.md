# Session Handoff Protocol

Purpose: make the workflow usable even for someone who does not know what the next engineering step should be.

The user should never have to invent the next coding prompt after a phase or session.

---

## Core rule

At the end of every meaningful implementation/review session, the AI agent must:

1. determine the current project/phase state from canonical repository docs and code;
2. decide the correct next action;
3. update `docs/project/NEXT_SESSION.md`;
4. include a ready-to-copy **NEXT SESSION PROMPT** in the final response.

The user can then open a fresh AI session, paste that prompt, and continue without re-explaining the project.

---

## Why this exists

A non-developer often does not know whether the correct next step is:

```text
continue current implementation
run tests
review the phase
fix a migration
start the next phase
perform QA
prepare release
```

That decision belongs to the engineering agent.

The agent must not end with vague statements such as:

```text
Next: continue development.
```

It must provide an actionable handoff.

---

## State A — Phase is still in progress

If acceptance criteria are not yet satisfied:

```text
Phase status: IN PROGRESS
```

The handoff must:

- keep the same phase;
- name the next 1–3 cohesive unfinished tasks;
- reference the current phase file;
- avoid re-reading unrelated completed phases;
- request relevant verification;
- ask the next agent to generate another handoff at the end.

Example:

```text
Continue Phase 03 — Authentication.

Read only the Constitution, Project Brief, Architecture, Engineering Rules,
current Phase 03 spec, relevant ADRs and directly relevant auth code/tests.

Current phase is not complete. Implement the next unfinished tasks:
1. email verification;
2. password reset;
3. negative authorization tests.

Do not start Phase 04.
Run relevant lint/typecheck/tests/build.
At the end update docs/project/NEXT_SESSION.md and give me a ready-to-copy
NEXT SESSION PROMPT.
```

---

## State B — Phase is complete

If all acceptance criteria pass:

```text
Phase status: COMPLETE
```

The agent must inspect `docs/project/ROADMAP.md` and identify the next phase.

The handoff must:

- explicitly state that the previous phase is complete;
- name the next phase;
- reference the next phase spec;
- tell the next agent to inspect current repository state before coding;
- start with only the first 1–3 cohesive tasks;
- preserve token-efficient context rules.

Example:

```text
Phase 03 — Authentication is complete.
Start Phase 04 — Asset Library.

Read only:
1. .specify/memory/constitution.md
2. docs/project/PROJECT_BRIEF.md
3. docs/project/ARCHITECTURE.md
4. docs/system/ENGINEERING_RULES.md
5. docs/phases/04-asset-library.md
6. directly relevant ADRs and source/tests

Do not reread all completed phases unless a real cross-phase dependency requires it.
Inspect the repository first, then identify and implement the first 1–3 cohesive
Phase 04 tasks.

Use Spec Kit for WHAT, Superpowers for HOW, gstack selectively for review/QA,
and Context7 only when fresh library/API docs are needed.

Run relevant verification.
At the end update docs/project/NEXT_SESSION.md and give me the next ready-to-copy
NEXT SESSION PROMPT.
```

---

## State C — Project is complete

If the roadmap's implementation phases are complete:

```text
Phase status: PROJECT COMPLETE
```

The agent should choose the appropriate next action:

- final release audit;
- production deployment checklist;
- security review;
- browser/E2E QA;
- documentation/release notes;
- or no further work.

If the product is already released and verified, the handoff should explain that future functionality starts through:

```text
prompts/CHANGE_REQUEST.md
```

---

## Required final-response block

Every implementation/review session must end with:

```text
NEXT SESSION PROMPT

<copy-paste prompt>
```

Do not make the user reconstruct the prompt from a task list.

---

## Token-efficiency requirements

A handoff should not retell the entire project.

Prefer references:

```text
Read docs/project/PROJECT_BRIEF.md
Read docs/project/ARCHITECTURE.md
Read current phase
```

instead of copying those documents into the prompt.

The prompt should contain only information that the next agent cannot reliably recover from canonical files.

---

## Handoff is navigation, not duplicate state

Canonical product truth remains in:

```text
PROJECT_BRIEF.md
ARCHITECTURE.md
ROADMAP.md
current phase spec
ADRs
code/tests
```

`NEXT_SESSION.md` only answers:

```text
Where are we now?
What should happen next?
What prompt should I paste?
```

This keeps the handoff small and disposable while preserving a simple experience for non-developers.
