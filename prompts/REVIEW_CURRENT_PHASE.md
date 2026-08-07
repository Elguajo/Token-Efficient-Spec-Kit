# Review / Converge Current Phase

```text
Review the current implementation against the current phase spec.
Read only Constitution, Project Brief, Architecture, Engineering Rules, current phase, relevant ADR and relevant source/tests.
Do not start the next phase.

Check acceptance criteria, build/type/lint/tests, security negative cases, data integrity, user-facing error/loading/empty states, accessibility/performance where relevant, unnecessary complexity and accidental future scope.

Fix only gaps required to complete the current phase.
If Spec Kit converge is available, use equivalent converge behavior: compare code against spec and append/execute only missing work.

Return exactly:
PHASE COMPLETE
or
PHASE NOT COMPLETE
Then concise evidence.
```
