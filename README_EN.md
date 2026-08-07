<div align="center">

# Token-Efficient Spec Kit

### A standalone workflow for building software with AI coding agents

**Describe the outcome. The AI chooses the stack, designs the architecture, works phase by phase, verifies quality, and tells you exactly what to do next.**

`Idea → Architecture → Phases → 1–3 Tasks → Code → Verification → Next Prompt`

**Current version: `0.5.0`**

[Русская версия](README.md) · [Usage Guide](docs/USAGE_GUIDE.md) · [Workflow](docs/WORKFLOW.md) · [Integrations](integrations/README.md) · [Changelog](CHANGELOG.md)

</div>

---

## What it is

**Token-Efficient Spec Kit is the core workflow itself.**

You can start with:

```text
I want a marketplace where designers can sell digital assets.
```

The AI should then:

1. understand the product and users;
2. ask only true blocking questions;
3. choose one recommended stack;
4. design architecture and data boundaries;
5. create a roadmap and verifiable phases;
6. implement only 1–3 cohesive tasks per session;
7. run relevant tests/reviews/QA;
8. converge against acceptance criteria;
9. decide the next engineering step;
10. produce a ready-to-copy prompt for the next fresh AI session.

> **The user owns the desired outcome. The AI owns engineering decisions and project navigation.**

---

# Quick Start

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
```

Open the repository in a repository-aware AI coding agent, then run:

```text
prompts/START_NEW_PROJECT.md
```

Replace only:

```text
<WHAT_I_WANT>
```

with your desired product.

---

## How work flows

```text
User Outcome
→ Project Brief
→ Architecture
→ Roadmap
→ Current Phase
→ 1–3 Tasks
→ Implementation
→ Tests / Review / QA
→ Convergence
→ NEXT SESSION PROMPT
→ Fresh Session
```

Project knowledge lives in the repository, so you do not need to retell the whole project in every session.

---

# The key feature: the AI tells you what to do next

At the end of every meaningful implementation/review session the AI must classify the state as:

```text
IN PROGRESS
PHASE COMPLETE
PROJECT COMPLETE
```

Then it must update:

```text
docs/project/NEXT_SESSION.md
```

and return a ready-to-copy:

```text
NEXT SESSION PROMPT
```

If the phase is incomplete, the next prompt continues it.
If complete, the AI finds the next roadmap phase itself.
If the project is complete, it routes to release/audit/deployment or a future change request.

Fallback:

```text
prompts/GENERATE_NEXT_SESSION_PROMPT.md
```

---

## Why it saves tokens

A normal session reads only:

```text
Constitution
+ Project Brief
+ Architecture
+ Engineering Rules
+ Current Phase
+ Relevant ADR
+ Relevant code/tests
```

It should not automatically reload all completed phases, all ADRs, full chat history, giant master specs, or raw research dumps.

> **One fact, one canonical location. One session, usually 1–3 cohesive tasks.**

---

# Recommended AI Engineering Profile

Default:

```text
Token-Efficient Spec Kit
├── Superpowers
├── gstack
└── Context7
```

| Tool | Responsibility |
|---|---|
| **Token-Efficient Spec Kit** | **CORE** — intent, architecture, roadmap, phases, tasks, context, convergence, handoff |
| **Superpowers** | **HOW** — TDD, implementation discipline, systematic debugging |
| **gstack** | Challenge / review / browser QA / release checks |
| **Context7** | Fresh library/API documentation on demand |

---

# GitHub Spec Kit is optional

GitHub Spec Kit is **not required for normal operation**.

Token-Efficient Spec Kit already owns project-level Brief, Architecture, Roadmap, Phases, Tasks, Acceptance Criteria, Convergence and Session Handoff.

GitHub Spec Kit can be enabled as **Optional Advanced Spec Mode** for difficult phases where deeper formal specification adds clear value, such as payments, complex authorization, multi-tenancy boundaries, public APIs, critical migrations, or large ambiguous integrations.

Use:

```text
prompts/ENABLE_ADVANCED_SPEC_MODE.md
```

---

# Daily use

| Situation | Use |
|---|---|
| Start a project | [`START_NEW_PROJECT.md`](prompts/START_NEW_PROJECT.md) |
| Continue | Paste the previous **NEXT SESSION PROMPT** |
| Generic continuation fallback | [`CONTINUE_PROJECT.md`](prompts/CONTINUE_PROJECT.md) |
| Review/close a phase | [`REVIEW_CURRENT_PHASE.md`](prompts/REVIEW_CURRENT_PHASE.md) |
| Lost the handoff | [`GENERATE_NEXT_SESSION_PROMPT.md`](prompts/GENERATE_NEXT_SESSION_PROMPT.md) |
| Understand project health | [`PROJECT_DOCTOR.md`](prompts/PROJECT_DOCTOR.md) |
| Requirements changed | [`CHANGE_REQUEST.md`](prompts/CHANGE_REQUEST.md) |
| Fix a bug | [`BUG_FIX.md`](prompts/BUG_FIX.md) |
| Audit the workflow itself | [`AUDIT_WORKFLOW.md`](prompts/AUDIT_WORKFLOW.md) |
| Safely update the workflow | [`UPDATE_WORKFLOW.md`](prompts/UPDATE_WORKFLOW.md) |

---

# Project Doctor

If you do not understand the current repository state, run:

```text
prompts/PROJECT_DOCTOR.md
```

It explains in plain language:

```text
HEALTHY / NEEDS ATTENTION / BLOCKED / UNKNOWN
current phase
what is already done
what remains
known build/test status
workflow/tooling concerns
best next action
NEXT SESSION PROMPT
```

Project Doctor is diagnostic by default and should not implement unrelated product work.

---

# Workflow Self-Audit

After material changes to Token-Efficient Spec Kit itself, run:

```text
prompts/AUDIT_WORKFLOW.md
```

It checks ownership consistency, default-vs-optional tooling, Session Handoff, token efficiency, paths/links, safe update boundaries, and VERSION/CHANGELOG alignment.

It reports findings first instead of automatically redesigning the framework.

---

# Safe workflow updates

To update Token-Efficient Spec Kit inside an existing product repository, use:

```text
prompts/UPDATE_WORKFLOW.md
```

The updater distinguishes:

```text
Framework-managed
→ system docs / prompts / integrations / templates

Merge-sensitive
→ Constitution / AGENTS.md

Project-owned
→ project docs / phases / ADRs / code / tests / migrations
```

**Project-owned files must never be blindly replaced with template defaults.**

After an update, Workflow Self-Audit is required.

---

# Versioning

Current framework version:

```text
VERSION
```

History and migration context:

```text
CHANGELOG.md
```

The project follows Semantic Versioning principles.

---

## Documentation

- [Usage Guide](docs/USAGE_GUIDE.md)
- [End-to-End Workflow](docs/WORKFLOW.md)
- [Session Handoff](docs/system/SESSION_HANDOFF.md)
- [Project Doctor](docs/system/PROJECT_DOCTOR.md)
- [Workflow Self-Audit](docs/system/WORKFLOW_SELF_AUDIT.md)
- [Safe Workflow Update Policy](docs/system/WORKFLOW_UPDATE_POLICY.md)
- [Current Next Step](docs/project/NEXT_SESSION.md)
- [Integrations](integrations/README.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

---

<div align="center">

### Describe the outcome. Let the agent handle the engineering and the next step.

**[Start a new project →](prompts/START_NEW_PROJECT.md)**

<br />

Built with ♥ by [Elguajo](https://github.com/Elguajo)

</div>
