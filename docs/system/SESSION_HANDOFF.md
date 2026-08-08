# Session Handoff Protocol

Purpose: make the workflow usable even for someone who does not know what the next engineering step should be.

The user should never have to invent the next coding prompt after a phase or session.

---

## Core rule

At the end of every meaningful product implementation/review session, the AI agent must:

1. determine the current project/phase state from canonical repository docs and code;
2. decide the correct next action;
3. update the phase status markers in `docs/project/ROADMAP.md` so that exactly one
   phase is marked `[>] IN PROGRESS` (or all are `[x]` when the project is complete);
4. update `docs/project/NEXT_SESSION.md`;
5. include a ready-to-copy **NEXT SESSION PROMPT** in the final response.

Step 3 is what makes the handoff recoverable: `NEXT_SESSION.md` may be lost or go
stale, `ROADMAP.md` is canonical state.

The user can then open a fresh AI session, paste that prompt, and continue without re-explaining the project.

These three outputs are one atomic project handoff:

```text
ROADMAP marker + NEXT_SESSION.md + NEXT SESSION PROMPT
```

Do not update only one or two of them. If a phase completes, move `[>]` to the next
planned phase before writing `NEXT_SESSION.md`. If no planned phases remain, all
phases stay `[x]` and the status is `PROJECT COMPLETE`.

## Completion precedence and external blockers

The usual 1–3-task implementation batch is a planning guideline, not a completion
gate. Classify a phase solely from its verified acceptance criteria: mark it `PHASE
COMPLETE` when all pass, even if the work spanned more or fewer tasks than usual.

If an external blocker—such as unavailable staging credentials, a pending provider
integration, or inaccessible production infrastructure—prevents a required check,
the phase remains in progress. State that concrete blocker, the affected acceptance
criterion, and the required follow-up; never present the task-batch guideline as
the reason for non-completion.

---

## Non-product handoff exceptions

### Uninitialized template

If `docs/project/ROADMAP.md` still says `Not initialized`, do not invent a phase,
change its marker or create/update project state merely to satisfy the handoff rule.
Do not initialize `docs/project/*` outside `prompts/START_NEW_PROJECT.md`.

End with status `TEMPLATE UNINITIALIZED` and a ready-to-copy **NEXT SESSION PROMPT**
that routes the user to `prompts/START_NEW_PROJECT.md`.

### Framework-only audit or update

A workflow audit/update maintains the framework layer; it does not advance the
product roadmap. It must leave `docs/project/ROADMAP.md` and
`docs/project/NEXT_SESSION.md` unchanged, whether the template is uninitialized or
a downstream product already exists.

End with the framework audit/update status and a ready-to-copy **NEXT SESSION
PROMPT** for the next framework action. If no framework action remains, preserve or
route back to the existing product handoff; for an uninitialized template, route to
`prompts/START_NEW_PROJECT.md`.

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
Continue Phase 01 - Authentication.

Read only the Default Read Set from docs/system/TOKEN_EFFICIENCY.md, plus the
auth code and tests directly relevant to the tasks below.

docs/project/ROADMAP.md marks Phase 01 as [>] IN PROGRESS. Implement the next
unfinished tasks:
1. email verification;
2. password reset;
3. negative authorization tests.

Do not start Phase 02.
Route code questions through one tool: Semble if the location is unknown, Serena
if the symbol is known, native tools for a tiny exact edit. Do not rediscover the
same code twice.

Run relevant lint/typecheck/tests/build.
At the end update the ROADMAP marker and docs/project/NEXT_SESSION.md, then give
me a ready-to-copy NEXT SESSION PROMPT.
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
Phase 01 - Authentication is complete.
Start Phase 02 - Asset Library.

Read only the Default Read Set from docs/system/TOKEN_EFFICIENCY.md. The current
phase file is docs/phases/02-asset-library.md.

Do not reread all completed phases unless a real cross-phase dependency requires it.
Inspect the repository first, then identify and implement the first 1-3 cohesive
Phase 02 tasks.

Token-Efficient Spec Kit owns WHAT and orchestration. Superpowers owns HOW.
Route a code question to exactly one of Semble / Serena / native tools. Use gstack
selectively for review or QA, Context7 only when fresh library/API docs are needed.

Run relevant verification.
At the end mark Phase 02 as [>] in docs/project/ROADMAP.md, update
docs/project/NEXT_SESSION.md, and give me the next ready-to-copy NEXT SESSION PROMPT.
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

Every meaningful product or framework implementation/review session must end with:

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
PROJECT_BRIEF.md      product truth
ARCHITECTURE.md       chosen stack/system
ROADMAP.md            phase order AND the current-phase marker
current phase spec    scope and acceptance criteria
ADRs                  why a major decision was made
code/tests            the product itself
```

`NEXT_SESSION.md` only answers:

```text
Where are we now?
What should happen next?
What prompt should I paste?
```

This keeps the handoff small and disposable while preserving a simple experience for non-developers.
