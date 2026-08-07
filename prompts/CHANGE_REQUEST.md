# Change Request

Replace `<CHANGE>`.

````text
The project requirements changed:

<CHANGE>

Do not rewrite the whole project.

Read:
- Constitution;
- Project Brief;
- Architecture;
- Roadmap;
- Session Handoff protocol;
- only directly affected phases/ADRs/code.

Assess:
1. product intent impact;
2. architecture impact;
3. invalidated ADRs;
4. affected phases;
5. migration/backward compatibility;
6. security/cost impact.

Prefer the smallest coherent change.
Update only canonical docs whose truth changed.
Create an ADR only if a consequential architecture decision changed.
Implement only the first 1–3 required tasks and verify them.

Before responding:
- determine the resulting current phase/status;
- update `docs/project/NEXT_SESSION.md` according to `docs/system/SESSION_HANDOFF.md`;
- generate a ready-to-copy next-session prompt.

Return:
- impact summary;
- docs/code/migrations changed;
- verification;
- remaining work;
- next action.

NEXT SESSION PROMPT

```text
<ready-to-copy prompt for a fresh AI session>
```

The user should not need to decide how the changed roadmap continues.
````
