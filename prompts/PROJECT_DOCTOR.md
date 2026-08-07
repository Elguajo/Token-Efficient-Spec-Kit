# Project Doctor

```text
Act as Project Doctor for this repository.

Goal: explain the real project state in plain language, identify anything blocking or risky, and tell the user exactly what to do next.

Read only what is needed:
1. VERSION
2. docs/project/PROJECT_BRIEF.md
3. docs/project/ARCHITECTURE.md
4. docs/project/ROADMAP.md
5. docs/project/TOOLING_STATUS.md
6. docs/project/NEXT_SESSION.md
7. docs/system/PROJECT_DOCTOR.md
8. current phase
9. relevant ADR(s) only if needed
10. relevant build/test/repository evidence when available

Do NOT read every completed phase or the whole source tree by default.
Do NOT implement product features during this diagnostic task.
Do NOT claim tests/build are healthy unless there is evidence.

Determine:
- current project health: HEALTHY / NEEDS ATTENTION / BLOCKED / UNKNOWN;
- current phase;
- what has actually been completed;
- what remains;
- whether NEXT_SESSION is current or stale;
- whether relevant tests/build/checks are passing, failing or unknown;
- whether there is obvious documentation/workflow drift;
- whether any optional tooling issue materially affects progress;
- the single best next action.

If a deep framework consistency problem is suspected, recommend `prompts/AUDIT_WORKFLOW.md` rather than loading the entire framework automatically.

If `docs/project/NEXT_SESSION.md` is stale or missing and the correct next action can be determined safely, update it with a concise handoff.

Return in plain language:

PROJECT DOCTOR

Health:
- HEALTHY / NEEDS ATTENTION / BLOCKED / UNKNOWN

Current phase:
- ...

What is already done:
- ...

What needs attention:
- None / ...

Checks:
- Build: PASS / FAIL / NOT RUN / UNKNOWN
- Tests: PASS / FAIL / NOT RUN / UNKNOWN
- Other relevant checks: ...

Tooling/workflow:
- OK / ...

What this means:
- <1–3 plain-language sentences>

Recommended next action:
- ...

NEXT SESSION PROMPT

```text
<ready-to-copy prompt>
```

If the project is blocked on a human decision/login/credential/destructive approval, explain that blocker instead of fabricating a next coding step.
```
