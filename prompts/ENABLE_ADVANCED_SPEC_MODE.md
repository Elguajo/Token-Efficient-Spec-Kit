# Enable Optional Advanced Spec Mode

Use this only when the CURRENT phase clearly benefits from formal deep specification.

```text
Evaluate and, if justified, enable Optional Advanced Spec Mode for the current phase.

IMPORTANT:
Token-Efficient Spec Kit remains the project-level source of truth.
Do not replace or duplicate:
- docs/project/PROJECT_BRIEF.md
- docs/project/ARCHITECTURE.md
- docs/project/ROADMAP.md
- existing phase boundaries
- docs/project/NEXT_SESSION.md

First read:
1. .specify/memory/constitution.md
2. docs/project/PROJECT_BRIEF.md
3. docs/project/ARCHITECTURE.md
4. docs/project/ROADMAP.md
5. current phase file
6. integrations/TOOLING_POLICY.md
7. integrations/SPEC_KIT.md
8. docs/project/TOOLING_STATUS.md

STEP 1 — JUSTIFY

Determine whether GitHub Spec Kit adds clear value for THIS phase.
Strong triggers include:
- payments;
- complex authorization;
- multi-tenancy boundaries;
- public API contracts;
- critical migrations;
- large ambiguous cross-system features;
- requirements whose consistency is difficult to verify manually.

If the phase is ordinary and existing phase spec/tasks are sufficient, do NOT enable Advanced Spec Mode.
Return `ADVANCED SPEC MODE NOT NEEDED` and continue with the normal Token-Efficient workflow.

STEP 2 — INSTALL ONLY IF NEEDED

If justified:
- verify current official GitHub Spec Kit installation/integration instructions;
- install/configure it for the active coding harness;
- preserve the existing Constitution and canonical project docs;
- do not regenerate the project-level roadmap;
- if Superpowers is installed, add a current supported Spec Kit ↔ Superpowers bridge only if it materially prevents workflow overlap;
- record the enabled mode in docs/project/TOOLING_STATUS.md.

STEP 3 — SCOPE IT TO THE CURRENT PHASE

Use GitHub Spec Kit only for the depth justified by the phase, for example:

current Token-Efficient phase
→ formal specification
→ clarify if consequential ambiguity exists
→ plan
→ checklist if risk justifies it
→ tasks
→ analyze if consistency/risk warrants it
→ implementation
→ convergence

Do not run every gate automatically.
Do not create a second project roadmap.

STEP 4 — HAND BACK TO THE CORE WORKFLOW

After phase-level formal artifacts are ready:
- implementation remains governed by the current Token-Efficient phase;
- Superpowers/native agent handles HOW;
- gstack may review/QA selectively;
- final phase status and NEXT SESSION PROMPT are still produced by Token-Efficient Session Handoff.

Final response:

ADVANCED SPEC MODE ENABLED
or
ADVANCED SPEC MODE NOT NEEDED

Reason:
- ...

Scope:
- current phase only

Tooling changes:
- ...

Canonical project docs preserved:
- YES / NO

Next action:
- ...
```
