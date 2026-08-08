# Update Token-Efficient Spec Kit Safely

```text
Update the Token-Efficient Spec Kit framework in this project without overwriting project-owned state.

Read first:
1. VERSION
2. CHANGELOG.md
3. docs/system/WORKFLOW_UPDATE_POLICY.md
4. docs/system/WORKFLOW_SELF_AUDIT.md
5. .specify/memory/constitution.md
6. AGENTS.md

Upstream framework repository:
https://github.com/Elguajo/Token-Efficient-Spec-Kit

Your job:
- determine the installed local workflow version;
- determine the target upstream version, preferring a release/tag, then a pinned
  commit SHA, then the moving default branch; record which one you used;
- read upstream changelog/migration notes;
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
- VERSION
- CHANGELOG.md

For VERSION and CHANGELOG.md:
- if they clearly still belong only to Token-Efficient Spec Kit, update them normally;
- if the downstream product has repurposed or extended them, preserve product history and merge instead of replacing.

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
4. verify the target release's documented Recommended profile; for v0.7.x this is Token-Efficient Spec Kit + Superpowers + Semble + Serena + RTK + gstack + Context7;
5. verify Semble remains intent-based code-discovery-only;
6. verify Serena remains symbol/refactor-only and does not reintroduce generic search/shell/memory ownership when the overlap policy can be applied;
7. verify RTK remains shell/tool-output-only;
8. verify Semble/Serena/RTK graceful fallback still exists;
9. verify the no-double-discovery rule still routes a code-context question to one cheapest adequate tool first;
10. verify GitHub Spec Kit remains optional unless the target release explicitly documents a deliberate architecture change;
11. record the installed workflow version only after successful application;
12. do not modify application/business code merely to complete a framework update.

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
```
> Canonical profile definition: [`../integrations/PROFILES.md`](../integrations/PROFILES.md). This listing is a copy for reading convenience — if the two disagree, PROFILES.md wins.

