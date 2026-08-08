# Generate Next Session Prompt

Use this only when you want the AI agent to tell you exactly what to do in a fresh session without implementing more code now.

````text
Determine the correct next step for this project and generate a ready-to-copy prompt for a fresh AI session.

Do NOT implement new product work in this task.

Read only the Default Read Set defined in `docs/system/TOKEN_EFFICIENCY.md`,
plus directly relevant verification/task state.

Resolve the current phase from the `[>]` marker in `docs/project/ROADMAP.md`.
This marker is canonical, which is why this prompt still works when
`docs/project/NEXT_SESSION.md` has been lost or is stale.

Inspect repository state and determine one status:

- IN PROGRESS — current phase still has unmet acceptance criteria;
- PHASE COMPLETE — current phase is done and the next roadmap phase should start;
- PROJECT COMPLETE — implementation roadmap is complete.

The usual 1–3-task batch is a planning guideline, not a completion gate. Use
verified acceptance criteria to choose the status. If an external blocker prevents
verification, name that blocker and the affected criterion as the reason for
`IN PROGRESS`.

Then:
1. choose the correct next action yourself;
2. verify/correct the markers in `docs/project/ROADMAP.md` so exactly one phase is
   `[>]`, or all are `[x]` when the project is complete;
3. update `docs/project/NEXT_SESSION.md`;
4. return only a concise status summary and the next-session prompt.

If IN PROGRESS:
- continue the same phase;
- name the next 1–3 cohesive tasks.

If PHASE COMPLETE:
- identify the next roadmap phase;
- do not start it now;
- generate a prompt that starts it in a clean session.

If PROJECT COMPLETE:
- route to final audit/release if still needed;
- otherwise explain that new functionality should begin through `prompts/CHANGE_REQUEST.md`.

Return:

STATUS: IN PROGRESS / PHASE COMPLETE / PROJECT COMPLETE

NEXT ACTION:
<one short description>

NEXT SESSION PROMPT

```text
<ready-to-copy prompt>
```

The prompt must be self-sufficient but token-efficient: reference canonical repository files instead of repeating their contents.
````
