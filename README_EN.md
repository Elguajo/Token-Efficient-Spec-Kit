<div align="center">

# Token-Efficient Spec Kit

### A universal workflow for building software with AI coding agents

**Describe the outcome. The AI chooses the stack, designs the architecture, works phase by phase, verifies quality, and tells you what to do next.**

`Idea → Architecture → Phases → 1–3 Tasks → Code → Verification → Next Prompt`

**v0.5.0**

[Русская версия](README.md) · [Usage Guide](docs/USAGE_GUIDE.md) · [Workflow](docs/WORKFLOW.md) · [Maintenance](docs/MAINTENANCE.md) · [Changelog](CHANGELOG.md)

</div>

---

## What it is

**Token-Efficient Spec Kit is a standalone AI Engineering Workflow.**

You describe the product you want. The AI should then:

- understand the product and users;
- ask only true blocking questions;
- choose one recommended stack;
- design the architecture and roadmap;
- split work into verifiable phases;
- implement usually 1–3 cohesive tasks per session;
- run relevant tests/reviews/QA;
- decide the next engineering step;
- generate a ready-to-copy prompt for the next fresh session.

> **You own the product outcome. The AI owns engineering execution and project navigation.**

---

# Quick Start

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
```

Open the repository in a repository-aware AI coding agent such as Codex, Claude Code, or Cursor, then run:

```text
prompts/START_NEW_PROJECT.md
```

Replace only:

```text
<WHAT_I_WANT>
```

with the product you want to build.

---

## How work flows

```text
User Outcome
→ Project Brief
→ Architecture
→ Roadmap
→ Current Phase
→ 1–3 Tasks
→ Implementation + Tests
→ Convergence
→ NEXT SESSION PROMPT
→ Fresh Session
```

Project knowledge lives in the repository, so each new session does not need the full project history.

---

# The AI tells you what to do next

At the end of every meaningful implementation/review session, the AI must classify the state as:

```text
IN PROGRESS
PHASE COMPLETE
PROJECT COMPLETE
```

Then it updates:

```text
docs/project/NEXT_SESSION.md
```

and returns a ready-to-copy:

```text
NEXT SESSION PROMPT
```

If the handoff is ever lost, use:

```text
prompts/GENERATE_NEXT_SESSION_PROMPT.md
```

[Session Handoff details →](docs/system/SESSION_HANDOFF.md)

---

## Why it saves tokens

A normal session reads only the smallest useful context:

```text
Constitution
+ Project Brief
+ Architecture
+ Current Phase
+ relevant ADR
+ relevant code/tests
```

It should not automatically reload every completed phase, every ADR, full chat history, or giant master specs.

> **One fact, one canonical location. One session, usually 1–3 cohesive tasks.**

---

## Recommended profile

Token-Efficient Spec Kit is the **core**.

Recommended external tooling:

| Tool | Role |
|---|---|
| **Superpowers** | TDD, implementation discipline, systematic debugging |
| **gstack** | Engineering/design review, browser QA, release checks |
| **Context7** | Fresh library/API documentation on demand |

GitHub Spec Kit is **optional** and can be enabled as [Advanced Spec Mode](integrations/SPEC_KIT.md) for difficult phases that benefit from deeper formal specification.

[Integration details →](integrations/README.md)

---

# Main entry points

| Situation | Use |
|---|---|
| Start a new project | [`START_NEW_PROJECT.md`](prompts/START_NEW_PROJECT.md) |
| Continue normally | Previous **NEXT SESSION PROMPT** |
| Review/close a phase | [`REVIEW_CURRENT_PHASE.md`](prompts/REVIEW_CURRENT_PHASE.md) |
| Understand project health | [`PROJECT_DOCTOR.md`](prompts/PROJECT_DOCTOR.md) |
| Lost the next step | [`GENERATE_NEXT_SESSION_PROMPT.md`](prompts/GENERATE_NEXT_SESSION_PROMPT.md) |
| Requirements changed | [`CHANGE_REQUEST.md`](prompts/CHANGE_REQUEST.md) |
| Fix a bug | [`BUG_FIX.md`](prompts/BUG_FIX.md) |

Normal workflow:

```text
START_NEW_PROJECT
→ NEXT SESSION PROMPT
→ NEXT SESSION PROMPT
→ ...
→ PROJECT COMPLETE
```

---

## Documentation

| I want to understand... | Open |
|---|---|
| How to use the workflow | [Usage Guide](docs/USAGE_GUIDE.md) |
| How it works internally | [End-to-End Workflow](docs/WORKFLOW.md) |
| What to do next right now | [NEXT_SESSION.md](docs/project/NEXT_SESSION.md) |
| External tooling | [Integrations](integrations/README.md) |
| Doctor, Self-Audit, Updates and Versioning | [Maintenance](docs/MAINTENANCE.md) |
| Version history | [Changelog](CHANGELOG.md) |
| How to contribute | [Contributing](CONTRIBUTING.md) |

---

<div align="center">

### Describe the outcome. Let the agent handle the engineering and the next step.

**[Start a new project →](prompts/START_NEW_PROJECT.md)**

<br />

Built with ♥ by [Elguajo](https://github.com/Elguajo)

</div>
