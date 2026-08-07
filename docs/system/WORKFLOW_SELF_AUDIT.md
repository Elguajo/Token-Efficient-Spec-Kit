# Workflow Self-Audit

Purpose: periodically verify that Token-Efficient Spec Kit remains internally consistent, token-efficient and understandable after framework changes.

This audit checks the **workflow itself**, not application code quality.

---

## What to compare

Audit these layers against each other:

```text
VERSION / CHANGELOG
↓
Constitution
↓
AGENTS.md
↓
README / USAGE_GUIDE / WORKFLOW
↓
System Rules
↓
Prompts
↓
Integrations / Tooling Profiles
↓
Templates
↓
Project navigation / Session Handoff
```

---

## Required checks

### 1. Ownership consistency

There must be one clear owner for each responsibility.

Default model:

```text
Token-Efficient Spec Kit
→ product intent
→ architecture
→ roadmap
→ phases
→ task batches
→ convergence
→ session handoff

Superpowers
→ implementation discipline
→ TDD
→ systematic debugging

gstack
→ challenge / review / browser QA / release checks

Context7
→ current library/API documentation

GitHub Spec Kit
→ optional Advanced Spec Mode only
```

Flag any file that reintroduces GitHub Spec Kit as a default dependency or creates duplicate canonical planning ownership.

### 2. User journey consistency

A non-developer should be able to follow:

```text
README
→ START_NEW_PROJECT
→ AI performs work
→ NEXT SESSION PROMPT
→ fresh session
→ repeat
```

Flag instructions that make the user manually choose routine engineering steps or determine the next phase themselves.

### 3. Session Handoff consistency

All meaningful implementation/review entry points should preserve the rule:

```text
IN PROGRESS / PHASE COMPLETE / PROJECT COMPLETE
→ decide next action
→ update NEXT_SESSION.md
→ output NEXT SESSION PROMPT
```

### 4. Token-efficiency consistency

Flag instructions that unnecessarily require:

- reading all phases;
- reading all ADRs;
- reading full chat history;
- generating duplicate PRDs/specs/plans;
- running every installed tool on every task;
- saving verbose status reports after every small action.

### 5. Project-state safety

Framework maintenance must never casually overwrite:

```text
docs/project/*
docs/phases/*
docs/decisions/*
application source code
tests
migrations
user secrets/configuration
```

See `WORKFLOW_UPDATE_POLICY.md`.

### 6. Documentation accuracy

Check that README, Usage Guide and Workflow describe the actual current behavior of prompts and tooling.

### 7. Prompt completeness

Check that each main prompt has:

- clear read set;
- scope boundary;
- verification requirement;
- user-blocker rule;
- session handoff when applicable.

### 8. Version hygiene

When framework behavior changes materially:

- update `VERSION`;
- update `CHANGELOG.md`;
- update migration/update notes when compatibility changes.

### 9. Link / path integrity

Verify referenced repository paths exist and internal documentation links are not stale.

### 10. Complexity creep

Flag framework features that add more permanent context or ceremony than value.

Ask:

> Could this be an on-demand prompt/tool instead of always-loaded project state?

---

## Severity

```text
CRITICAL
Workflow can cause data loss, security regression or destructive overwrite.

HIGH
Core ownership/session/phase behavior is contradictory.

MEDIUM
Documentation or prompt behavior is stale or inefficient.

LOW
Clarity, naming or navigation improvement.
```

---

## Pass condition

A healthy workflow should satisfy:

```text
one canonical core
clear optional tooling
small normal read set
safe project-state boundaries
mandatory useful handoff
no contradictory user instructions
version/changelog aligned
```

The audit should propose the **smallest coherent fixes**, not redesign the workflow automatically.
