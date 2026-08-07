# Project Doctor

Purpose: give a non-developer a short, truthful answer to:

> **What is the state of my project, is anything wrong, and what should I do next?**

Project Doctor is diagnostic. It does not implement features by default.

---

## What it inspects

Read the smallest useful set:

```text
VERSION
PROJECT_BRIEF
ARCHITECTURE
ROADMAP
TOOLING_STATUS
NEXT_SESSION
current phase
relevant ADRs only when needed
current git/repository state
relevant build/test status when available
```

Do not automatically load every completed phase or the entire source tree.

---

## Health categories

```text
HEALTHY
Project state is coherent and the next action is clear.

NEEDS ATTENTION
Work can continue, but there are failing checks, drift, stale state or unresolved issues.

BLOCKED
A real blocker prevents safe progress.

UNKNOWN
There is not enough repository evidence to determine health reliably.
```

---

## Doctor checks

### Project state

- Is Project Brief initialized and still consistent with the product?
- Is Architecture initialized?
- Is Roadmap initialized?
- Is one current phase identifiable?
- Is NEXT_SESSION current enough to be useful?

### Phase state

- What acceptance criteria are done?
- What remains?
- Are there unresolved blockers?
- Is the phase being expanded beyond its intended scope?

### Engineering checks

When practical, inspect existing evidence for:

```text
build
lint
typecheck
tests
e2e/browser QA
security negatives
```

Do not invent a passing status if checks were not run.

### Workflow health

Check for obvious contradictions such as:

- duplicate canonical plans;
- stale tool ownership;
- GitHub Spec Kit treated as required default;
- missing session handoff;
- stale/broken NEXT_SESSION;
- project docs that disagree materially.

For deep workflow consistency, route to `AUDIT_WORKFLOW.md` instead of performing a full framework audit every time.

### Tooling

Report only materially useful tooling problems.
Do not fail the whole project merely because an optional tool is absent.

---

## Human-friendly output

The Doctor should avoid framework jargon where possible.

Prefer:

```text
Project health: NEEDS ATTENTION

What this means:
The current phase is mostly complete, but two tests are failing.
Do not start the next phase yet.
```

instead of a long internal-state dump.

---

## Next action

Project Doctor must always recommend one concrete next action when possible.

It should also provide a ready-to-copy `NEXT SESSION PROMPT` unless the project is genuinely blocked and requires human input first.

Doctor may update `docs/project/NEXT_SESSION.md` when the current handoff is clearly stale or missing and the next action can be determined safely.

It must not modify product requirements, architecture or application code merely to make the health report look better.
