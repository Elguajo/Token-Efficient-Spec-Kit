<div align="center">

# Token-Efficient Spec Kit

### A universal workflow for building software with AI coding agents

**Describe the outcome. The AI chooses the technical path, works phase by phase, keeps context small, and tells you what to do next.**

`Idea → Architecture → Phases → 1–3 Tasks → Code → Verification → Next Prompt`

**v0.6.0**

[Русская версия](README.md) · [Usage Guide](docs/USAGE_GUIDE.md) · [Workflow](docs/WORKFLOW.md) · [Maintenance](docs/MAINTENANCE.md) · [Changelog](CHANGELOG.md)

</div>

---

## What it is

**Token-Efficient Spec Kit is a standalone AI Engineering Workflow.**

You describe the product you want. The AI should then:

- understand the product and users;
- ask only true blocking questions;
- choose one recommended stack;
- design architecture and roadmap;
- split work into verifiable phases;
- use only the code/context needed now;
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

Open the repository in Codex, Claude Code, Cursor, or another repository-aware AI coding agent, then run:

```text
prompts/START_NEW_PROJECT.md
```

Replace only `<WHAT_I_WANT>` with the product you want to build.

On the first run, the agent checks `docs/project/TOOLING_STATUS.md` and automatically bootstraps Recommended tooling when needed.

---

## Automatic Recommended tooling

```text
Superpowers  → implementation discipline / TDD / debugging
Semble       → token-efficient code retrieval
RTK          → compact terminal/test/build/git output
gstack       → review / browser QA / release checks
Context7     → fresh library/API documentation
```

You do not need to install each tool manually.

If a tool is already configured, it is not reinstalled. If Semble or RTK cannot be safely integrated, the workflow continues with native search/read/shell tools instead of blocking the project.

---

## How work flows

```text
User Outcome
→ Tooling Bootstrap
→ Project Brief
→ Architecture
→ Roadmap
→ Current Phase
→ Targeted Code Retrieval
→ 1–3 Tasks
→ Implementation
→ Compact Verification Output
→ Review / QA
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

Then it updates `docs/project/NEXT_SESSION.md` and returns a ready-to-copy `NEXT SESSION PROMPT`.

If the handoff is ever lost, use `prompts/GENERATE_NEXT_SESSION_PROMPT.md`.

---

## Token-efficiency layers

```text
Project/docs context → Token-Efficient Spec Kit
Code retrieval       → Semble
Shell/tool output     → RTK
Fresh external docs  → Context7 on demand
```

Semble should not be forced for a known tiny file. RTK should not be used when raw output is required for debugging. Correctness always outranks token savings.

> **One fact, one canonical location. One session, usually 1–3 cohesive tasks.**

---

## Recommended profile

| Tool | Role |
|---|---|
| **Token-Efficient Spec Kit** | Core orchestration, project/docs context, phases, convergence, handoff |
| **Superpowers** | TDD, implementation discipline, systematic debugging |
| **Semble** | Semantic/hybrid code retrieval with small relevant snippets |
| **RTK** | Compact terminal/test/build/git output |
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
