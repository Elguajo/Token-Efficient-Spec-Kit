# Continue Project

````text
Continue the current project autonomously.

Read only the Default Read Set defined in `docs/system/TOKEN_EFFICIENCY.md`.

Do not read all completed phases or full project history.

Resolve the current phase from the status markers in `docs/project/ROADMAP.md`
(the phase marked `[>]`), then inspect repository state and determine its status.

If the current phase is still in progress:
- implement the next 1–3 cohesive unfinished tasks;
- do not start unrelated future phases.

If the current phase has already satisfied all acceptance criteria:
- do not silently keep adding work;
- run/confirm phase review as needed;
- determine the next roadmap phase.

If an implementation detail is unspecified, choose the best professional default, verify current official docs when needed, and proceed unless it is a true blocker.

Run relevant verification.
Update persistent docs only when requirements, important architecture, ADRs, migrations/env, phase state, or next-session navigation changed.

Before responding:
1. determine whether status is IN PROGRESS, PHASE COMPLETE, or PROJECT COMPLETE;
2. update docs/project/NEXT_SESSION.md according to docs/system/SESSION_HANDOFF.md;
3. prepare a ready-to-copy prompt for the user's next fresh AI session.

Return compactly:

DONE / NOT DONE / PHASE COMPLETE / PROJECT COMPLETE

Implemented:
- ...

Important decision:
- ... or None

Verification:
- ...

Remaining current phase:
- ... or None

Next action:
- ...

NEXT SESSION PROMPT

```text
<ready-to-copy prompt for a fresh AI session>
```

The NEXT SESSION PROMPT is mandatory. The user should never need to invent the next engineering prompt.
````
