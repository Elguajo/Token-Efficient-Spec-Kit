# Token-Efficient Bug Fix

````text
Fix the reported bug.

Inspect the failing behavior and directly relevant code/tests first.
Read project-wide architecture only if the bug crosses subsystem boundaries.
Do not load every phase.

Process:
1. reproduce or establish evidence;
2. find root cause;
3. implement the smallest correct fix;
4. add a regression test;
5. run relevant checks;
6. avoid unrelated refactors.

If the bug exposes a broken architectural invariant, update the canonical architecture/ADR after fixing it.

Before responding:
- determine whether the fix changes the current phase status;
- update the phase markers in `docs/project/ROADMAP.md` so exactly one phase is
  `[>]`, or all are `[x]` when the project is complete;
- update `docs/project/NEXT_SESSION.md` according to `docs/system/SESSION_HANDOFF.md`;
- generate a ready-to-copy next-session prompt.

Return:
- root cause;
- fix;
- regression test;
- verification;
- follow-up risk;
- next action.

NEXT SESSION PROMPT

```text
<ready-to-copy prompt for a fresh AI session>
```

The next prompt should continue the correct current phase or start the next phase if the fix completed it.
````
