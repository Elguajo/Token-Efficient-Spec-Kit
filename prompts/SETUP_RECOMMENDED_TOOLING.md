# Setup Recommended Tooling

Use this prompt when the default external tooling is not initialized for the active coding harness.

```text
Set up the Recommended Tooling Profile for this project.

IMPORTANT:
Token-Efficient Spec Kit is already the core workflow and MUST remain the canonical orchestration/specification layer.

Recommended external tooling:

Superpowers
+ gstack
+ Context7

GitHub Spec Kit is NOT part of the default installation.
Do not install GitHub Spec Kit or the Spec Kit ↔ Superpowers bridge unless Optional Advanced Spec Mode is explicitly requested or the current project/phase has a documented need for formal deep specification.

FIRST read:
1. .specify/memory/constitution.md
2. integrations/README.md
3. integrations/PROFILES.md
4. integrations/TOOLING_POLICY.md
5. integrations/SUPERPOWERS.md
6. integrations/GSTACK.md
7. integrations/CONTEXT7.md

Then detect:
- operating system;
- active coding harness/agent when possible;
- existing installations;
- repository state;
- required runtimes/tools already installed.

Before installing EACH external tool, verify its CURRENT OFFICIAL upstream installation instructions.
Do not rely on stale commands when upstream changed.

Ask the user only when:
- OAuth/login requires user interaction;
- a missing global runtime/package manager needs approval;
- an installer requires destructive overwrite permission;
- the active coding harness cannot be determined reliably.

STEP 1 — Superpowers
- install using the current native/recommended mechanism for the active harness;
- verify skills are discoverable;
- ensure it does not replace Token-Efficient Project Brief / Architecture / Roadmap / phase docs with a competing canonical planning system.

STEP 2 — gstack
- install using the current upstream-supported host mode;
- verify discoverability;
- prefer it as challenge/review/QA tooling;
- do not enable a parallel canonical roadmap/planning flow by default.

STEP 3 — Context7
- configure using the best current native mode for the harness (MCP, CLI/skills or current equivalent);
- never commit API keys, tokens or credentials;
- verify access to fresh library/API docs.

STEP 4 — Verify workflow ownership

Effective workflow must remain:

User outcome
→ Token-Efficient Project Brief
→ Architecture
→ Roadmap
→ Current Phase
→ 1–3 tasks
→ Superpowers/native implementation
→ project tests
→ selective gstack review/browser QA/release checks
→ Token-Efficient convergence
→ NEXT SESSION PROMPT

STEP 5 — Record status

Create/update `docs/project/TOOLING_STATUS.md` with:
- date checked;
- OS;
- active harness;
- profile;
- Superpowers status/version/mode if known;
- gstack status/version/mode if known;
- Context7 status/mode;
- GitHub Spec Kit: Not installed by default / Advanced Mode enabled if applicable;
- verification;
- manual action still required.

Do not modify application/business code during tooling setup.

Final response:

RECOMMENDED TOOLING READY

Core:
- Token-Efficient Spec Kit — READY

External tooling:
- Superpowers — ...
- gstack — ...
- Context7 — ...

Optional Advanced Spec Mode:
- GitHub Spec Kit — NOT ENABLED / ENABLED: ...

Verification:
- ...

Manual action required:
- None
or only genuine login/runtime/restart steps

Do not start product implementation automatically after this setup-only task.
```
