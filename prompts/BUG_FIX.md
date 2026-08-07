# Token-Efficient Bug Fix

```text
Fix the reported bug.
Inspect the failing behavior and directly relevant code/tests first.
Read project-wide architecture only if the bug crosses subsystem boundaries.
Do not load every phase.

1. reproduce/establish evidence;
2. find root cause;
3. implement smallest correct fix;
4. add regression test;
5. run relevant checks;
6. avoid unrelated refactors.

If the bug exposes a broken architectural invariant, update the canonical architecture/ADR after fixing it.
Return root cause, fix, test, verification and follow-up risk.
```
