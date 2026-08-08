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
→ project/docs context
→ convergence
→ session handoff

Semble
→ targeted code retrieval

RTK
→ compact shell/tool output

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

Flag any file that:

- reintroduces GitHub Spec Kit as a default dependency;
- removes Semble/RTK from the documented Recommended profile without a deliberate versioned change;
- lets Semble/RTK become project-level truth or planning owners;
- creates duplicate canonical planning ownership.

### 2. User journey consistency

A non-developer should be able to follow:

```text
README
→ START_NEW_PROJECT
→ automatic tooling bootstrap when needed
→ AI performs work
→ NEXT SESSION PROMPT
→ fresh session
→ repeat
```

Flag instructions that make the user manually install ordinary Recommended tools, manually choose routine engineering steps, or determine the next phase themselves when the agent can do it safely.

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
- broad grep + full-file exploration when Semble/targeted retrieval would be appropriate;
- verbose terminal/test/build output when RTK can safely preserve the required signal;
- running every installed tool on every task;
- saving verbose status reports after every small action.

Also flag the opposite failure: token-saving tools must not hide decision-critical source context, failures or diagnostics.

### 5. Tooling bootstrap consistency

Recommended default should remain:

```text
Token-Efficient Spec Kit
+ Superpowers
+ Semble
+ RTK
+ gstack
+ Context7
```

unless a deliberate versioned framework change says otherwise.

Check that:

- `START_NEW_PROJECT.md` invokes setup automatically when needed;
- `TOOLING_STATUS.md` tracks Semble and RTK;
- Semble/RTK have graceful fallback;
- global RTK hooks/instructions are not silently applied when they affect unrelated projects and no safe project-scoped option exists;
- installer success is followed by real verification.

### 6. Project-state safety

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

### 7. Documentation accuracy

Check that README, Usage Guide and Workflow describe the actual current behavior of prompts and tooling.

### 8. Prompt completeness

Check that each main prompt has:

- clear read set;
- scope boundary;
- verification requirement;
- user-blocker rule;
- session handoff when applicable.

### 9. Version hygiene

When framework behavior changes materially:

- update `VERSION`;
- update `CHANGELOG.md`;
- update migration/update notes when compatibility changes.

### 10. Link / path integrity

Verify referenced repository paths exist and internal documentation links are not stale.

### 11. Complexity creep

Flag framework features that add more permanent context or ceremony than value.

Ask:

> Could this be an on-demand prompt/tool instead of always-loaded project state?

---

## Severity

```text
CRITICAL
Workflow can cause data loss, security regression or destructive overwrite.

HIGH
Core ownership/session/phase/tooling behavior is contradictory.

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
Recommended profile aligned
small normal read set
targeted code retrieval
compact but recoverable tool output
safe project-state boundaries
mandatory useful handoff
no contradictory user instructions
version/changelog aligned
```

The audit should propose the **smallest coherent fixes**, not redesign the workflow automatically.
