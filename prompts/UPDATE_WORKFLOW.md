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
- determine the latest appropriate upstream release/tag/version;
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
- VERSION
- CHANGELOG.md

Merge-sensitive, NEVER blindly replace:
- .specify/memory/constitution.md
- AGENTS.md

Project-owned, NEVER automatically overwrite:
- docs/project/*
- docs/phases/*
- docs/decisions/*
- application source code
- tests
- migrations
- credentials/secrets
- project-specific product documentation

Before changing anything:
1. produce a compact update plan;
2. identify any breaking/migration-sensitive changes;
3. stop for approval only if the update requires destructive/ambiguous changes to project-owned state.

For normal compatible framework updates, proceed autonomously.

After applying:
1. run the equivalent of prompts/AUDIT_WORKFLOW.md;
2. verify internal paths used by main prompts;
3. verify NEXT_SESSION / Session Handoff behavior still exists;
4. verify Recommended profile remains Token-Efficient Spec Kit + Superpowers + gstack + Context7 unless the target release intentionally changes it;
5. verify GitHub Spec Kit remains optional unless the target release explicitly documents a deliberate architecture change;
6. update VERSION only after successful application;
7. do not modify application/business code merely to complete a framework update.

Return:

WORKFLOW UPDATE COMPLETE
or
WORKFLOW UPDATE BLOCKED

Previous version:
- ...

Target version:
- ...

Updated framework files:
- ...

Merged sensitive files:
- None / ...

Project-owned files modified:
- NONE
(or stop and explain why approval is required)

Migration:
- None / ...

Self-audit:
- HEALTHY / NEEDS ATTENTION / UNSAFE

Manual action required:
- None / ...
```
