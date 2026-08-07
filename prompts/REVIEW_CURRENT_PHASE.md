# Review / Converge Current Phase

```text
Review the current implementation against the current phase spec.

Read only:
- .specify/memory/constitution.md
- docs/project/PROJECT_BRIEF.md
- docs/project/ARCHITECTURE.md
- docs/project/ROADMAP.md
- docs/system/ENGINEERING_RULES.md
- docs/system/SESSION_HANDOFF.md
- current phase
- relevant ADR(s)
- relevant source/tests

Do not start the next phase during this review.

Check:
1. acceptance criteria;
2. build/typecheck/lint/tests;
3. security negative cases where relevant;
4. data integrity;
5. user-facing error/loading/empty states;
6. accessibility/performance where relevant;
7. unnecessary complexity;
8. accidental future scope.

Fix only gaps required to complete the current phase.
If Spec Kit converge is available, use equivalent converge behavior: compare code against spec and execute only missing work.

Then determine one state:

A. PHASE NOT COMPLETE
- identify the next 1–3 unfinished tasks;
- keep the next session in the same phase.

B. PHASE COMPLETE
- inspect docs/project/ROADMAP.md;
- identify the next phase;
- do not implement it now;
- prepare a fresh-session prompt that starts that phase.

C. PROJECT COMPLETE
- identify the appropriate final release/audit/deployment step, or route future features through prompts/CHANGE_REQUEST.md.

Before responding:
- update docs/project/NEXT_SESSION.md according to docs/system/SESSION_HANDOFF.md.

Return:

PHASE COMPLETE
or
PHASE NOT COMPLETE
or
PROJECT COMPLETE

Evidence:
- ...

Next action:
- ...

NEXT SESSION PROMPT
```text
<ready-to-copy prompt for a fresh AI session>
```

The NEXT SESSION PROMPT is mandatory.
Do not make the user figure out which phase or prompt to run next.
```
