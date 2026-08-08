# Update Token-Efficient Spec Kit Safely

```text
Update the Token-Efficient Spec Kit framework in this project without overwriting project-owned state.

Read first:
1. `.token-efficient-spec-kit/VERSION` when it exists; otherwise `VERSION`
2. docs/system/WORKFLOW_UPDATE_POLICY.md
3. docs/system/WORKFLOW_SELF_AUDIT.md
4. .specify/memory/constitution.md
5. AGENTS.md

Upstream framework repository:
https://github.com/Elguajo/Token-Efficient-Spec-Kit

Your job:
- determine the installed local workflow version;
- determine the target upstream version, preferring a release/tag, then a pinned
  commit SHA, then the moving default branch; record which one you used;
- read the target upstream release notes/changelog and migration notes;
- compare framework-managed files;
- detect local customizations;
- apply the smallest safe framework update;
- preserve all project-owned state.

FILE SAFETY:

Framework-managed, update with review:
- docs/system/*
- integrations/*
- templates/*
- prompts/*

Merge-sensitive, NEVER blindly replace:
- .specify/memory/constitution.md
- AGENTS.md

Source-repository metadata:
- `VERSION` and `CHANGELOG.md` exist only in the upstream framework source repository.
- In a downstream Starter, record the completed update by changing only
  `.token-efficient-spec-kit/VERSION`; never create, overwrite or merge a root
  `VERSION` or `CHANGELOG.md`, because those names belong to the product.

Project-owned, NEVER automatically overwrite:
- docs/project/*
- docs/phases/*
- docs/decisions/*
- application source code
- tests
- migrations
- credentials/secrets
- project-specific README/product documentation

Before changing anything:
1. produce a compact update plan;
2. identify any breaking/migration-sensitive changes;
3. report the exact update source: release/tag name, or commit SHA, or default branch;
4. stop for approval only if the update requires destructive/ambiguous changes to project-owned state.

For normal compatible framework updates, proceed autonomously.

After applying:
1. run `python3 tools/audit.py` and quote its verdict; it must exit 0 before the
   update can be called successful, then run prompts/AUDIT_WORKFLOW.md for the
   judgement checks;
2. verify internal paths used by main prompts;
3. verify NEXT_SESSION / Session Handoff behavior still exists;
4. verify the target release's documented Recommended profile against that release's own `integrations/PROFILES.md`; the canonical list travels with the release, so never compare against a profile hardcoded in this prompt;
5. verify Semble remains intent-based code-discovery-only;
6. verify Serena remains symbol/refactor-only and does not reintroduce generic search/shell/memory ownership when the overlap policy can be applied;
7. verify RTK remains shell/tool-output-only;
8. verify Semble/Serena/RTK graceful fallback still exists;
9. verify the no-double-discovery rule still routes a code-context question to one cheapest adequate tool first;
10. verify GitHub Spec Kit remains optional unless the target release explicitly documents a deliberate architecture change;
11. record the installed workflow version only after successful application;
12. do not modify application/business code merely to complete a framework update.

This is framework-only work. Do not change `docs/project/ROADMAP.md` or
`docs/project/NEXT_SESSION.md` as a session handoff side effect. End with a
ready-to-copy `NEXT SESSION PROMPT` for any remaining framework action; if none
remains, preserve the existing product continuation or route an uninitialized
template to `prompts/START_NEW_PROJECT.md`.

Do not silently install new global hooks or system runtimes merely because a newer framework version added an integration. Follow the target release's tooling setup policy and request approval when a global change affects unrelated projects.

Return:

WORKFLOW UPDATE COMPLETE
or
WORKFLOW UPDATE BLOCKED

Previous version:
- ...

Target version:
- ...

Update source:
- release / tag / default branch

Updated framework files:
- ...

Merged sensitive files:
- None / ...

Project-owned files modified:
- NONE
(or stop and explain why approval is required)

Tooling migration:
- None / ...

Migration:
- None / ...

Self-audit:
- HEALTHY / NEEDS ATTENTION / UNSAFE

Manual action required:
- None / ...

NEXT SESSION PROMPT

<copy-paste prompt>
```
> Canonical profile definition: [`../integrations/PROFILES.md`](../integrations/PROFILES.md). This listing is a copy for reading convenience — if the two disagree, PROFILES.md wins.
