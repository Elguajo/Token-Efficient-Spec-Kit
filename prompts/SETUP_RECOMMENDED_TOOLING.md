# Setup Recommended Tooling

Use this prompt once after cloning/copying Token-Efficient Spec Kit into a project.

```text
Set up the Recommended Tooling Profile for this project.

Recommended profile:

Token-Efficient Spec Kit
+ GitHub Spec Kit
+ Superpowers
+ Superpowers Implementation Bridge
+ gstack
+ Context7

Your job is to install/configure these tools for the CURRENT coding harness and project without creating overlapping planning systems.

FIRST read:

1. .specify/memory/constitution.md
2. integrations/README.md
3. integrations/PROFILES.md
4. integrations/TOOLING_POLICY.md
5. integrations/SPEC_KIT.md
6. integrations/SUPERPOWERS.md
7. integrations/GSTACK.md
8. integrations/CONTEXT7.md

Then detect:

- operating system;
- current coding harness/agent when possible;
- existing installations;
- repository state;
- required runtimes/tools already installed.

IMPORTANT:

Installation methods for these projects change over time.
Before installing EACH external tool, check its CURRENT OFFICIAL documentation/repository.
Do not rely only on installation commands written in this repository when upstream has changed.

Do not ask me to choose normal technical setup details.
Choose the current recommended native integration for my harness.

Ask only when:

- authentication requires me to complete OAuth/login;
- a system runtime/package manager is missing and installing it changes my machine globally;
- an installer needs destructive overwrite permission;
- the active coding harness cannot be determined reliably.

STEP 1 — GitHub Spec Kit

- Verify current official installation instructions.
- Install/update the Specify CLI through the recommended supported method.
- Verify with `specify version` or its current equivalent.
- Initialize/integrate Spec Kit into the current project for the active coding harness.
- Preserve the existing custom `.specify/memory/constitution.md` exactly unless an explicit migration is needed.
- If init would overwrite it, back it up and restore it.
- Do not delete existing project docs.

STEP 2 — Superpowers

- Read current official `obra/superpowers` installation instructions for the active harness.
- Use the native plugin/skills mechanism currently recommended upstream.
- Do not install a second unrelated planning framework.
- Verify Superpowers skills are discoverable in a new/current session as far as the harness allows.

STEP 3 — Spec Kit ↔ Superpowers bridge

- Search the current Spec Kit extension catalog for the Superpowers Implementation Bridge.
- If `speckit-superpowers-bridge` is still the current accepted extension ID, install it through Spec Kit.
- If the extension was renamed/replaced, use the current official catalog entry instead and document the change.
- Verify the bridge does not replace Spec Kit as the canonical spec/plan/task source.

STEP 4 — gstack

- Read the current official `garrytan/gstack` installation/setup instructions.
- Install for the active coding harness using the upstream-supported host mode.
- Prefer namespaced gstack commands when practical because Superpowers/Spec Kit are also installed.
- Do not vendor a large gstack checkout into application code unless current upstream team-mode instructions require it.
- Check for duplicate skill registrations after setup.
- Do not activate gstack autoplan as the canonical planning flow.

STEP 5 — Context7

- Read the current official `upstash/context7` installation instructions.
- Configure Context7 using the best native mode for this harness: MCP or CLI/Skills.
- Never commit credentials/API keys.
- If OAuth/login is required, pause only for that interaction and then continue.

STEP 6 — Project policy

Ensure the effective workflow remains:

User outcome
→ Token-Efficient project brief/architecture
→ Spec Kit specification + plan + tasks
→ gstack challenge/review only when useful
→ Superpowers implementation discipline
→ project tests
→ gstack review/browser QA/release checks where relevant
→ Spec Kit convergence

Do not create parallel canonical plans from Superpowers or gstack.

STEP 7 — Verification

Verify as much as the active harness supports:

- Specify CLI available;
- Spec Kit integration detected;
- existing Constitution preserved;
- Superpowers installed/discoverable;
- bridge installed if supported;
- gstack installed/discoverable without duplicate skill names;
- Context7 configured without committed secrets.

Do not modify application/business code during this setup task.

At the end create/update:

`docs/project/TOOLING_STATUS.md`

Keep it concise and include:

- active harness;
- OS;
- installed tools;
- versions where available;
- installation mode;
- verification status;
- manual action still required, if any;
- date checked.

Final response format:

RECOMMENDED TOOLING READY

Harness:
- ...

Installed:
- Spec Kit — ...
- Superpowers — ...
- Superpowers bridge — ...
- gstack — ...
- Context7 — ...

Verification:
- ...

Manual action required:
- None
or only genuine login/runtime/restart steps

Do not start product implementation automatically after tooling setup.
```
