<div align="center">

# Token-Efficient Spec Kit

### An autonomous, senior-level AI engineering workflow that keeps context small and decisions sharp.

**Describe the outcome. Let the agent choose the stack, architecture, roadmap, and implementation path.**

`Outcome → Decisions → Specs → Small Tasks → Code → Verification`

[Русская версия](README.md)

</div>

---

## Why this exists

AI coding agents are powerful, but large projects often become expensive and inconsistent because every session reloads too much context, repeats decisions, and asks the user to choose technical details they should not need to choose.

**Token-Efficient Spec Kit** is a lightweight engineering operating system built around a simple idea:

> **The user defines the outcome. The agent owns engineering decisions. Specs preserve intent. Small context preserves tokens. Verification preserves quality.**

You can start with something as small as:

```text
I want a web app where photographers can sell Lightroom presets.
```

The agent is expected to determine the rest professionally:

- what kind of product this is;
- what needs clarification and what can be assumed;
- the recommended stack;
- architecture and data model;
- security boundaries;
- project complexity and risk;
- implementation phases;
- testing strategy;
- deployment approach;
- the next 1–3 tasks to implement.

It should **not** make you answer questions like “React or Vue?”, “Postgres or MongoDB?”, or “Vercel or AWS?” unless your business constraints genuinely make the choice depend on you.

---

## Core workflow

```text
                    ┌──────────────────────┐
                    │     USER OUTCOME     │
                    │  "I want to build…" │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      UNDERSTAND      │
                    │ users · jobs · scope │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   CLASSIFY & ASSESS  │
                    │ type · risk · size   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   SENIOR DECISIONS   │
                    │ stack · architecture │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       ROADMAP        │
                    │ verifiable phases   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    CURRENT PHASE     │
                    │  1–3 cohesive tasks │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      IMPLEMENT       │
                    │ code · migrate · test│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       CONVERGE       │
                    │ spec ↔ code ↔ tests │
                    └──────────┬───────────┘
                               │
                               └──────► next phase
```

---

## The token-efficient part

A typical agent session should **not** reread the entire project.

It loads only the smallest useful context:

```text
constitution
+ project brief
+ compact architecture
+ engineering rules
+ current phase
+ relevant ADR (only if needed)
+ relevant source files/tests
```

It normally does **not** load:

```text
all completed phases
+ every decision record
+ full chat history
+ giant master specs
+ repeated research notes
+ duplicated PRDs
```

This keeps the agent focused and reduces both token usage and architectural drift.

---

## Adaptive process — not every project needs the same ceremony

### S — Small

For landing pages, small CLIs, isolated features, simple automations:

```text
Brief → Plan → Tasks → Implement → Verify
```

### M — Medium

For SaaS MVPs, ecommerce, plugins with backends, internal tools:

```text
Brief → Architecture → Roadmap → Phase Specs → Implement → Converge
```

### L — Large / High-risk

For marketplaces, multi-role systems, payments, sensitive data, critical migrations:

```text
Brief
→ Architecture
→ Risk model
→ Roadmap
→ Small independent specs
→ Selective quality gates
→ Implementation batches
→ Converge
```

The system deliberately avoids heavyweight documentation when it does not add value.

---

## Senior-agent behavior

The included Constitution instructs the agent to:

- make normal engineering decisions autonomously;
- choose **one recommended default**, not dump ten options on the user;
- research current official documentation when technology freshness matters;
- prefer simple, mature technology over novelty when both solve the problem;
- ask questions only when the answer materially changes the product, cost, security, compliance, or an irreversible action;
- treat security as architecture, not a later checklist;
- add complexity only when a concrete requirement justifies it;
- verify before claiming completion.

---

## Creative autonomy

This workflow is not intended to make the agent rigid.

When details are unspecified, the agent is explicitly allowed to propose and choose:

- product and feature organization;
- UX flows;
- information architecture;
- visual patterns;
- API ergonomics;
- data models;
- onboarding;
- loading, empty and error states;
- developer tooling;
- small high-value product improvements.

Creative choices must support the requested outcome and must never silently override explicit constraints.

---

## Repository structure

```text
.
├── .specify/
│   └── memory/
│       └── constitution.md
│
├── docs/
│   ├── system/
│   │   ├── OPERATING_MODEL.md
│   │   ├── DECISION_FRAMEWORK.md
│   │   ├── ENGINEERING_RULES.md
│   │   ├── TOKEN_EFFICIENCY.md
│   │   └── CREATIVE_AUTONOMY.md
│   │
│   ├── project/
│   │   ├── PROJECT_BRIEF.md
│   │   ├── ARCHITECTURE.md
│   │   └── ROADMAP.md
│   │
│   ├── phases/
│   └── decisions/
│
├── templates/
│   ├── PROJECT_BRIEF.template.md
│   ├── ARCHITECTURE.template.md
│   ├── ROADMAP.template.md
│   ├── PHASE.template.md
│   └── ADR.template.md
│
├── prompts/
│   ├── START_NEW_PROJECT.md
│   ├── CONTINUE_PROJECT.md
│   ├── REVIEW_CURRENT_PHASE.md
│   ├── CHANGE_REQUEST.md
│   └── BUG_FIX.md
│
├── AGENTS.md
├── README.md
└── README_EN.md
```

---

## Quick start

### 1. Copy or clone this template

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
```

You can also merge these files into an existing repository.

### 2. Optional: initialize GitHub Spec Kit

If you use GitHub Spec Kit, initialize it for your coding agent according to the current Spec Kit documentation.

The workflow here is intentionally agent-agnostic and can be used with Codex, Claude Code, Cursor, or other repository-aware coding agents.

### 3. Open the starter prompt

Use:

```text
prompts/START_NEW_PROJECT.md
```

Replace:

```text
<WHAT_I_WANT>
```

with your desired outcome.

Example:

```text
I want a desktop application for Windows and macOS that automatically
organizes my CGI/3D assets, generates previews, and lets me search by tags.
```

### 4. Let the agent bootstrap the project

It should create/update:

```text
docs/project/PROJECT_BRIEF.md
docs/project/ARCHITECTURE.md
docs/project/ROADMAP.md
docs/phases/...
docs/decisions/...  # only when a real ADR is justified
```

Then it starts the first small implementation batch unless a genuine blocker exists.

### 5. Continue with a small context window

For later sessions use:

```text
prompts/CONTINUE_PROJECT.md
```

For phase verification:

```text
prompts/REVIEW_CURRENT_PHASE.md
```

For requirement changes:

```text
prompts/CHANGE_REQUEST.md
```

For focused bug fixing:

```text
prompts/BUG_FIX.md
```

---

## Example: what the agent should decide

You say:

```text
Build a marketplace where designers can sell digital templates.
```

You should **not** have to specify:

```text
framework
database
auth provider
object storage
hosting
API style
test runner
observability stack
```

The agent evaluates requirements, risk and current tooling, then records a single recommended architecture.

For consequential choices it may record an ADR like:

```text
docs/decisions/ADR-001-primary-database.md
```

For trivial implementation decisions it should not create documentation overhead.

---

## Decision philosophy

A material technical choice is evaluated roughly around:

| Criterion | Default weight |
|---|---:|
| Requirement fit | 25% |
| Simplicity | 20% |
| Maintainability | 15% |
| Ecosystem / maturity | 10% |
| Security | 10% |
| Operational burden | 10% |
| Cost | 5% |
| Developer productivity | 5% |

Weights are adapted to the project. For example, security and data integrity dominate in financial or sensitive systems.

The rule is not “always choose the most popular stack.” The rule is **choose the simplest mature stack that fits the actual product**.

---

## Quality gates

A feature is not complete just because code exists.

Relevant evidence may include:

```text
lint
+ typecheck
+ tests
+ build
+ security negative tests
+ manual QA
+ acceptance criteria
```

For high-risk areas such as auth, payments, private files, permissions, migrations, and external webhooks, negative tests are expected.

---

## Principles in one minute

1. **Outcome first.** The user describes what they want, not how to implement it.
2. **Senior autonomy.** The agent owns normal technical decisions.
3. **Ask only blockers.** Do not turn every engineering choice into a user questionnaire.
4. **Simplicity first.** No premature distributed architecture.
5. **Current information.** Verify fast-changing APIs and providers from official docs.
6. **Small context.** Read only what the current task needs.
7. **Small batches.** Usually 1–3 cohesive tasks per implementation run.
8. **Canonical docs.** One fact, one preferred home.
9. **Security by design.** Server authority, least privilege, negative tests.
10. **Verification before completion.** Spec ↔ code ↔ tests must converge.

---

## What this is not

This is **not**:

- a fixed technology stack;
- a giant PRD generator;
- a multi-agent role-play framework;
- a reason to create documentation for every trivial decision;
- a replacement for engineering judgment;
- a guarantee that AI-generated code is correct without verification.

It is a compact operating layer that makes repository-aware coding agents behave more consistently across projects.

---

## Designed for

- solo developers using AI coding agents;
- designers/founders who know the product they want but do not want to choose every technology;
- senior developers who want AI to respect architecture without rereading giant specs;
- prototypes that may grow into production systems;
- projects where context cost and drift become a problem over long sessions.

---

<div align="center">

### Describe the outcome. Keep the context small. Let the agent engineer.

Start with [`prompts/START_NEW_PROJECT.md`](prompts/START_NEW_PROJECT.md).

<br />

Built with ♥ by [Elguajo](https://github.com/Elguajo)

</div>
