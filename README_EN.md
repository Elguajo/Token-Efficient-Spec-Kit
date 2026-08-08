<div align="center">

<sub>AI ENGINEERING WORKFLOW</sub>

# Token-Efficient Spec Kit

**From idea to verified result.**

[Start a new project](prompts/START_NEW_PROJECT.md) · [How to use it](docs/USAGE_GUIDE.md) · [Visual Guide](docs/VISUAL_GUIDE.md) · [Русская версия](README.md)

<sub>**v0.9.0** · [Workflow](docs/WORKFLOW.md) · [Maintenance](docs/MAINTENANCE.md) · [Changelog](CHANGELOG.md)</sub>

</div>

---

## What it does

Token-Efficient Spec Kit is a workflow for repository-aware AI agents such as
Codex, Claude Code, Cursor, and compatible tools. It records decisions in the
repository—not in one chat—so a fresh AI session can continue without you
re-explaining the project.

You do not need to decide in advance:

```text
Which framework or database should I use?
How should the work be phased?
What needs checking before release?
What should I ask the AI next?
```

You own the desired outcome and real constraints. The AI owns routine engineering
decisions, planning, implementation, verification, and project navigation.

In a typical session, the AI:

- understands the users, outcome, and constraints;
- asks a question only when it cannot proceed safely without the answer;
- chooses one practical stack and explains consequential decisions;
- splits work into verifiable phases and takes usually 1–3 cohesive tasks;
- runs appropriate tests, review, or QA and prepares the next prompt.

---

# Start a new project

## 1. Download the clean Starter

Download `token-efficient-spec-kit-starter.zip` from the appropriate
[GitHub Release](https://github.com/Elguajo/Token-Efficient-Spec-Kit/releases),
extract it, then create your Git repository:

```bash
cd token-efficient-spec-kit-starter-<version>
git init
```

The Starter omits the source framework repository's changelog, contribution and
maintenance documentation. To add the workflow to an existing repository, see the
[Usage Guide](docs/USAGE_GUIDE.md).

## 2. Open the folder in an AI coding agent

The agent must be able to read and edit the project files.

## 3. Send one message with your idea

Do not edit the prompt or replace a placeholder. In your AI agent, send something
like this:

```text
Start a new project using prompts/START_NEW_PROJECT.md.
My idea: a desktop app for Windows and macOS that organizes 3D assets,
generates previews, and makes them searchable by tags.
```

Describe the outcome you want. You do not need to choose a stack, framework,
database, or hosting provider first.

## What happens next

1. The AI normally proposes three meaningfully different product directions.
2. It explains its recommendation and continues with it without a separate choice.
3. It asks you to choose only when the alternatives have material budget, safety,
   compliance, or another irreversible product/business trade-off.
4. It creates `PROJECT_BRIEF.md`, `ARCHITECTURE.md`, `ROADMAP.md`, and phases, then
   starts the first 1–3 cohesive tasks.
5. At the end of the session, it verifies the result and returns a ready-to-copy
   `NEXT SESSION PROMPT`.

```text
Your idea
→ Product Directions (normally 3)
→ Recommended Direction (default)
→ Project Brief
→ Architecture
→ Roadmap
→ Scoped Tooling Bootstrap
→ Current Phase
→ 1–3 cohesive tasks
→ Implementation and verification
→ NEXT SESSION PROMPT
```

See the full [Visual Guide](docs/VISUAL_GUIDE.md) for the architecture, tool router,
session handoff, context budget, and maintenance diagrams.

---

# Continue working

After every meaningful coding or review session, the AI updates three connected
items: the current-phase marker in `docs/project/ROADMAP.md`,
`docs/project/NEXT_SESSION.md`, and the `NEXT SESSION PROMPT` in its response.

Usually, copy that prompt into a fresh session. You do not need to decide whether a
phase is complete, whether it is time for QA, or what should happen next.

| Situation | Send the AI |
|---|---|
| Start a project | The message from step 3 above |
| Continue normally | The last **NEXT SESSION PROMPT** |
| Understand project status | [`PROJECT_DOCTOR.md`](prompts/PROJECT_DOCTOR.md) |
| Change requirements | [`CHANGE_REQUEST.md`](prompts/CHANGE_REQUEST.md) |
| Fix a bug | [`BUG_FIX.md`](prompts/BUG_FIX.md) |
| Review and close a phase | [`REVIEW_CURRENT_PHASE.md`](prompts/REVIEW_CURRENT_PHASE.md) |
| Recover a lost next step | [`GENERATE_NEXT_SESSION_PROMPT.md`](prompts/GENERATE_NEXT_SESSION_PROMPT.md) |
| Create a deeper formal spec for a complex phase | [`ENABLE_ADVANCED_SPEC_MODE.md`](prompts/ENABLE_ADVANCED_SPEC_MODE.md) |

---

# For experienced users: how context stays small

The AI routes tools instead of running everything at once.

| Task | Preferred tool |
|---|---|
| “Where is logic X implemented?” / unfamiliar code | **Semble** |
| Known symbol, references, diagnostics, or safe rename | **Serena** |
| Tiny edit in a known file | native agent tools |
| Tests, build, git, or noisy terminal output | **RTK** |

```text
Semble finds the relevant logic
→ broad discovery stops
→ Serena joins only for a symbol-level task
→ RTK is used only for tool output
```

Do not rediscover the same code through Semble, Serena, and text search without a
reason. Project Brief, Architecture, Roadmap, and phase files remain the project's
long-term memory; tools do not create a second source of truth.

For the complete model, fallback behavior, and ownership boundaries, see the
[End-to-End Workflow](docs/WORKFLOW.md), [Visual Guide](docs/VISUAL_GUIDE.md), and
[Integrations](integrations/README.md).

---

# Tooling: what you need to know

The AI should not make you install ordinary tooling by hand. It first understands
the product and its tier, then enables only what is useful. If a tool is unavailable,
the workflow continues with a safe fallback.

```text
Superpowers  → implementation, TDD, and debugging
Semble       → find intent-relevant logic in unfamiliar code
Serena       → symbols, references, and safe refactoring
RTK          → compact terminal/test/build/git output
gstack       → review, browser QA, and release checks
Context7     → current API and library documentation
```

> Canonical profile: [`integrations/PROFILES.md`](integrations/PROFILES.md).
> Superpowers and Context7 may help immediately; the other tools are normally
> added after code exists and their value is clear.

The AI records installed, deferred, and skipped tooling in
`docs/project/TOOLING_STATUS.md`. You normally need to help only with login/OAuth,
a missing system runtime, or a global setting that would affect other projects.

For the detailed context-routing model, see [Workflow](docs/WORKFLOW.md); for
integration rules, see [Integrations](integrations/README.md). GitHub Spec Kit is
not required: enable it only as [Advanced Spec Mode](integrations/SPEC_KIT.md) for
complex phases.

---

# Find more detail

| I want to… | Open |
|---|---|
| Follow every workflow scenario step by step | [Usage Guide](docs/USAGE_GUIDE.md) |
| Understand the system visually | [Visual Guide](docs/VISUAL_GUIDE.md) |
| Understand the workflow model | [End-to-End Workflow](docs/WORKFLOW.md) |
| See the current project's next step | [NEXT_SESSION.md](docs/project/NEXT_SESSION.md) |
| Configure or understand integrations | [Integrations](integrations/README.md) |
| Run doctor, self-audit, or update | [Maintenance](docs/MAINTENANCE.md) |
| Review version history | [Changelog](CHANGELOG.md) |

## Workflow integrity check

```bash
python3 tools/audit.py
```

It checks links, versions, handoff, the tooling profile, and the boundary between
the framework and a project. CI runs the same check.

<div align="center">

### Describe the outcome. Let the agent handle the engineering and the next step.

**[Start a new project →](prompts/START_NEW_PROJECT.md)**

MIT — see [LICENSE](LICENSE) · Built with ♥ by [Elguajo](https://github.com/Elguajo)

</div>
