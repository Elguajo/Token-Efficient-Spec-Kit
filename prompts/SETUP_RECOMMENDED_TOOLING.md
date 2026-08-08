# Setup Recommended Tooling

Use this prompt when the default external tooling is not initialized for the active coding harness.

```text
Set up the Recommended Tooling Profile for this project.

IMPORTANT:
Token-Efficient Spec Kit is already the core workflow and MUST remain the canonical orchestration/specification layer.

Recommended external tooling:

Superpowers
+ Semble
+ RTK
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
6. integrations/SEMBLE.md
7. integrations/RTK.md
8. integrations/GSTACK.md
9. integrations/CONTEXT7.md

Then detect:
- operating system;
- active coding harness/agent when possible;
- existing installations;
- repository state;
- required runtimes/tools already installed;
- whether the harness supports project-scoped MCP/hooks/instructions.

Before installing EACH external tool, verify its CURRENT OFFICIAL upstream installation instructions.
Do not rely on stale commands when upstream changed.

AUTOMATION PRINCIPLE:
Install/configure Recommended tooling automatically when it can be done safely at user/project scope.
Do not ask the user to run ordinary installation commands manually.

Ask only when:
- OAuth/login requires user interaction;
- a missing global/system runtime or package manager needs approval;
- an installer requires destructive overwrite permission;
- the active coding harness cannot be determined reliably;
- the only supported RTK integration would modify global agent hooks/instructions for ALL projects and no safe project-scoped equivalent exists.

STEP 1 — Superpowers
- install using the current native/recommended mechanism for the active harness;
- verify skills are discoverable;
- ensure it does not replace Token-Efficient Project Brief / Architecture / Roadmap / phase docs with a competing canonical planning system.

STEP 2 — Semble
- verify current official `MinishLab/semble` installation instructions;
- install it using the current recommended safe user-level package method;
- prefer MCP integration for the active harness when supported;
- prefer unattended/non-interactive setup once the active agent is known;
- do NOT let its installer overwrite or duplicate canonical AGENTS/Constitution rules;
- if MCP is unavailable, use the smallest supported CLI/instruction integration that preserves project rules;
- run one small semantic code search to verify retrieval;
- record a graceful fallback if Semble cannot be integrated safely.

Semble role:
CODE CONTEXT ONLY — targeted code retrieval, not planning or architecture.

STEP 3 — RTK
- verify current official `rtk-ai/rtk` installation and active-agent setup instructions;
- install using the safest supported user-level package/binary method;
- prefer project-scoped integration when currently supported;
- if only a global hook/instruction integration exists, ask once before changing global agent behavior;
- verify the integration with a representative supported command;
- confirm command semantics and failures remain intact;
- confirm raw/full output remains recoverable for debugging;
- if command rewriting is unreliable or changes command semantics, disable auto-rewrite and mark RTK DEGRADED instead of breaking the workflow.

RTK role:
TOOL OUTPUT ONLY — compact terminal/test/build/git output, not project truth.

STEP 4 — gstack
- read the current official `garrytan/gstack` setup instructions;
- install for the active harness using the upstream-supported mode;
- verify discoverability;
- use it as challenge/review/QA tooling;
- do not enable a parallel canonical roadmap/planning flow by default.

STEP 5 — Context7
- configure using the best current native mode for the harness (MCP, CLI/skills or current equivalent);
- never commit API keys, tokens or credentials;
- verify access to fresh library/API docs.

STEP 6 — Verify token-efficiency architecture

Effective workflow must remain:

User outcome
→ Token-Efficient Project Brief / Architecture / Roadmap / Current Phase
→ Semble for targeted code retrieval when useful
→ 1–3 tasks
→ Superpowers/native implementation
→ RTK for compact shell output when safe
→ project tests
→ selective gstack review/browser QA/release checks
→ Context7 only for fresh external docs when needed
→ Token-Efficient convergence
→ NEXT SESSION PROMPT

Graceful fallback is mandatory:
- Semble unavailable → native targeted search/read;
- RTK unavailable/unsafe → native shell output with manual scoping;
- any external tool failure must NOT block starting the product unless the product itself depends on it.

STEP 7 — Record status

Create/update `docs/project/TOOLING_STATUS.md` with:
- date checked;
- OS;
- active harness;
- profile;
- Superpowers status/version/mode if known;
- Semble status/version/integration mode;
- RTK status/version/integration scope;
- gstack status/version/mode if known;
- Context7 status/mode;
- GitHub Spec Kit: Not installed by default / Advanced Mode enabled if applicable;
- verification;
- manual action still required.

Do not modify application/business code during this setup task.

Final response:

RECOMMENDED TOOLING READY

Core:
- Token-Efficient Spec Kit — READY

External tooling:
- Superpowers — ...
- Semble — ...
- RTK — ...
- gstack — ...
- Context7 — ...

Token-efficiency:
- Project/docs context — Token-Efficient Spec Kit
- Code retrieval — Semble: READY / DEGRADED
- Shell output — RTK: READY / DEGRADED

Optional Advanced Spec Mode:
- GitHub Spec Kit — NOT ENABLED / ENABLED: ...

Verification:
- ...

Manual action required:
- None
or only genuine login/runtime/global-hook/restart steps

Do not start product implementation automatically after this setup-only task.
```
