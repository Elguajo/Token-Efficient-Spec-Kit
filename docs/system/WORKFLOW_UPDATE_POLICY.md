# Safe Workflow Update Policy

Purpose: allow a project to update Token-Efficient Spec Kit framework files without destroying project-specific knowledge, code or decisions.

---

## Core principle

> **Framework updates may update the workflow. They must not overwrite the product.**

A project built from this template eventually contains two different kinds of files:

```text
FRAMEWORK LAYER
Reusable Token-Efficient Spec Kit behavior.

PROJECT LAYER
The concrete product's truth, code, phases and decisions.
```

They must be treated differently during updates.

---

## File ownership classes

### A. Framework-managed — safe to update with review

Typical files:

```text
docs/system/*
integrations/*
templates/*
prompts/*
.specify/decisions/*
tools/*
.github/workflows/*
```

These may be replaced by newer upstream framework versions after comparing local changes.

`.specify/decisions/*` holds ADRs about the framework itself. They are listed here
precisely so they stay maintainable: an earlier layout put a framework ADR inside
the project-owned `docs/decisions/`, where the updater was forbidden to touch it and
it silently went stale.

### B. Merge-sensitive framework files

```text
.specify/memory/constitution.md
AGENTS.md
VERSION
CHANGELOG.md
```

`VERSION` and `CHANGELOG.md` are framework metadata in the template repository, but a downstream product may later repurpose or extend root-level version/changelog files.

Therefore:

- if they still clearly belong to Token-Efficient Spec Kit, update them normally;
- if local project-specific changes exist, merge/review instead of blindly replacing;
- never erase product release history merely to update the workflow.

For all merge-sensitive files, use a three-way or semantic merge when practical:

```text
old framework version
vs
local current file
vs
new framework version
```

Preserve intentional local rules/history unless incompatible with the new framework.

### C. Project-owned — never overwrite automatically

```text
docs/project/*
docs/phases/*
docs/decisions/*        product ADRs only; framework ADRs live in .specify/decisions/
application source code
tests
migrations
.env / credentials / secrets
project-specific README or product docs
```

An updater may read these only to detect compatibility issues.
It must not replace them with template defaults.

---

## Update source

Default upstream:

```text
https://github.com/Elguajo/Token-Efficient-Spec-Kit
```

Update source, in order of preference:

```text
1. a published release or annotated tag        -> preferred
2. a pinned commit SHA on the default branch   -> acceptable, must be recorded
3. the moving default branch                   -> last resort, must be reported
```

Whichever is used, the updater records the exact source in the project's
`docs/project/TOOLING_STATUS.md` so the next update has a real baseline to diff
against. Never report "updated to latest" without a tag or SHA: that is a claim
without evidence, which Constitution section 9 forbids.

Do not update from an untrusted fork unless the user explicitly selects it.

---

## Safe update flow

```text
1. Read local VERSION / identify installed workflow version
2. Determine target upstream version/source
3. Read CHANGELOG / migration notes
4. Compare framework-managed files
5. Detect local modifications
6. Protect project-owned files
7. Merge sensitive files
8. Apply only framework changes
9. Run Workflow Self-Audit
10. Verify key internal links/paths
11. Record the installed workflow version safely
12. Report exactly what changed
```

---

## Compatibility check

Before applying an update, identify whether the target version changes:

- project-state file formats;
- phase conventions;
- handoff format;
- tooling ownership;
- required runtimes;
- integration behavior;
- protected file boundaries.

If a migration touches project-owned truth, generate a migration plan and ask before destructive or ambiguous changes.

---

## Never do this

```text
git checkout upstream -- .
rsync --delete template/ project/
copy every template file over the current repo
reset docs/project/*
reset docs/phases/*
reset docs/decisions/*
replace local Constitution without merge
erase a project-specific CHANGELOG
```

These approaches can destroy real project knowledge.

---

## Update result

A successful update should report:

```text
Previous workflow version
Target workflow version
Update source: release/tag/default branch
Framework files updated
Merge-sensitive files changed
Project-owned files touched: NONE
Migration required: yes/no
Self-audit result
Manual follow-up
```

If project-owned files were changed unintentionally, the update is not considered successful.
