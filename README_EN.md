<div align="center">

# Token-Efficient Spec Kit

### A universal workflow for building software with AI coding agents

**Describe the outcome. The AI chooses the technical path, works phase by phase, keeps context small, and tells you what to do next.**

`Idea → Architecture → Phases → 1–3 Tasks → Code → Verification → Next Prompt`

**v0.8.0**

[Русская версия](README.md) · [Usage Guide](docs/USAGE_GUIDE.md) · [Workflow](docs/WORKFLOW.md) · [Maintenance](docs/MAINTENANCE.md) · [Changelog](CHANGELOG.md)

</div>

---

## What it is

**Token-Efficient Spec Kit is a standalone AI Engineering Workflow.**

You describe the product you want. The AI should then understand the product, choose one practical stack, create architecture and roadmap, split work into verifiable phases, use only the code/context needed now, implement usually 1–3 cohesive tasks per session, verify the result, and generate a ready-to-copy prompt for the next fresh session.

> **You own the product outcome. The AI owns engineering execution and project navigation.**

---

# Quick Start

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
rm -rf .git && git init
```

The last line matters: without it `origin` still points at this repository and your
first `git push` goes to the wrong place.

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
Semble       → intent-based semantic code discovery
Serena       → symbol navigation / references / semantic refactoring
RTK          → compact terminal/test/build/git output
gstack       → review / browser QA / release checks
Context7     → fresh library/API documentation
```
> Canonical profile definition: [`integrations/PROFILES.md`](integrations/PROFILES.md). This listing is a copy for reading convenience — if the two disagree, PROFILES.md wins.


You do not need to install each tool manually.

If Semble, Serena, or RTK cannot be used safely, the workflow degrades gracefully to native tools instead of blocking product work.

---

## How work flows

```text
User Outcome
→ Tooling Bootstrap
→ Project Brief
→ Architecture
→ Roadmap
→ Current Phase
→ Routed Code Context
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

At the end of every meaningful implementation/review session, the AI must classify the state as `IN PROGRESS`, `PHASE COMPLETE`, or `PROJECT COMPLETE`, update `docs/project/NEXT_SESSION.md`, and return a ready-to-copy `NEXT SESSION PROMPT`.

---

## When Semble, Serena and RTK are already installed

The agent should **route**, not stack, the tools.

| Question / operation | Preferred tool |
|---|---|
| “Where is the logic for X?” / unfamiliar area | **Semble** |
| Known symbol, references, implementations, diagnostics, rename/refactor | **Serena** |
| Tiny known file/string edit | native agent tools |
| Tests/build/git/verbose shell output | **RTK** |

Typical flow:

```text
Semble
→ finds relevant file/snippet/symbol
→ broad discovery stops
→ Serena only if symbol references/diagnostics/refactoring are needed
→ implementation
→ RTK only for terminal output
```

**No-double-discovery rule:** do not make Semble, Serena and grep independently rediscover the same code unless the first result failed, is ambiguous, or independent verification is justified.

---

## Token-efficiency layers

```text
Project/docs context         → Token-Efficient Spec Kit
Intent-based code discovery  → Semble
Symbol semantics/refactoring → Serena
Shell/tool output            → RTK
Fresh external docs          → Context7 on demand
```

Correctness always outranks token savings.

---

## Recommended profile

| Tool | Role |
|---|---|
| **Token-Efficient Spec Kit** | Core orchestration, project/docs context, phases, convergence, handoff |
| **Superpowers** | TDD, implementation discipline, systematic debugging |
| **Semble** | Intent-based semantic/hybrid code discovery |
| **Serena** | Symbol navigation, references, diagnostics, semantic refactoring |
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

---

<div align="center">

## License

MIT — see [LICENSE](LICENSE).

## Workflow integrity check

```bash
python3 tools/audit.py
```

Checks internal links, version consistency, a single Default Read Set definition, the
current-phase marker and the framework/product boundary. CI runs the same script.

---

### Describe the outcome. Let the agent handle the engineering and the next step.

**[Start a new project →](prompts/START_NEW_PROJECT.md)**

<br />

Built with ♥ by [Elguajo](https://github.com/Elguajo)

</div>
