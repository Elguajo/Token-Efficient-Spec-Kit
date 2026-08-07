# Token-Efficient Spec Kit — End-to-End Workflow

> Техническая карта процесса: какие состояния проходит проект, какой контекст загружает агент и какой инструмент включается на каждом этапе.

---

# 1. Общая модель

```text
USER INTENT
    ↓
TOOLING READY?
    ↓
PROJECT BRIEF
    ↓
ARCHITECTURE
    ↓
ROADMAP
    ↓
CURRENT PHASE
    ↓
SPEC / PLAN / TASKS
    ↓
IMPLEMENTATION BATCH
    ↓
VERIFICATION
    ↓
CONVERGE
    ↓
PHASE COMPLETE?
    ├── no  → fix gaps → verify again
    └── yes → next phase
                    ↓
                 RELEASE
```

Процесс циклический, но контекст остаётся локальным.

---

# 2. Состояния проекта

## STATE 0 — TEMPLATE

Repository содержит workflow, но конкретный product ещё не инициализирован.

Canonical status:

```text
docs/project/PROJECT_BRIEF.md      → not initialized
docs/project/ARCHITECTURE.md       → not initialized
docs/project/ROADMAP.md            → not initialized
docs/project/TOOLING_STATUS.md     → not initialized / ready
```

Entry point:

```text
prompts/START_NEW_PROJECT.md
```

---

## STATE 1 — TOOLING BOOTSTRAP

Trigger:

```text
TOOLING_STATUS != ready for active harness
```

Agent loads:

```text
prompts/SETUP_RECOMMENDED_TOOLING.md
integrations/PROFILES.md
integrations/TOOLING_POLICY.md
only required integration docs
```

Recommended target:

```text
GitHub Spec Kit
Superpowers
Superpowers Implementation Bridge
gstack
Context7
```

Output:

```text
docs/project/TOOLING_STATUS.md
```

Exit condition:

```text
Recommended tooling verified
or
explicit documented limitation
```

Tooling bootstrap is not repeated on every session.

---

## STATE 2 — PRODUCT DEFINITION

Agent converts the user's outcome into compact product truth.

Reads:

```text
constitution
OPERATING_MODEL
DECISION_FRAMEWORK
ENGINEERING_RULES
CREATIVE_AUTONOMY
user request
```

Writes:

```text
docs/project/PROJECT_BRIEF.md
```

Output must distinguish:

```text
facts
explicit constraints
reasonable assumptions
true blockers
```

Do not ask technical preference questions that the agent can decide itself.

---

## STATE 3 — ARCHITECTURE

Agent chooses the simplest mature architecture that safely satisfies the product.

Research is selective.

Context7 or web/current official docs are used only when freshness materially matters.

Writes:

```text
docs/project/ARCHITECTURE.md
```

Potential ADR:

```text
docs/decisions/ADR-XXX-....md
```

ADR only for consequential cross-cutting or hard-to-reverse decisions.

Exit condition:

```text
One recommended default architecture exists
and critical security/source-of-truth boundaries are clear.
```

---

## STATE 4 — ROADMAP

Agent creates independently verifiable product phases.

Writes:

```text
docs/project/ROADMAP.md
docs/phases/00-....md
docs/phases/01-....md
...
```

Roadmap depth adapts to complexity.

```text
S → minimal
M → normal phased roadmap
L → smaller phases + stronger risk gates
```

Exit condition:

```text
The first phase is actionable and verifiable.
```

---

## STATE 5 — CURRENT PHASE PLANNING

Canonical input:

```text
current phase file
```

GitHub Spec Kit owns WHAT:

```text
specify
clarify — only if ambiguity matters
plan
tasks
analyze — only if risk/consistency warrants it
```

Superpowers must not create a competing product plan.

Recommended task size:

```text
1–3 cohesive implementation tasks per run
```

Exit condition:

```text
The next implementation batch is small, clear and testable.
```

---

## STATE 6 — IMPLEMENTATION

Superpowers / coding harness owns HOW.

Agent reads only:

```text
constitution
PROJECT_BRIEF
ARCHITECTURE
ENGINEERING_RULES
current phase
specific relevant ADR
relevant source/tests
```

Agent should not load all completed phase files.

During implementation:

- use current stable APIs;
- validate external inputs;
- preserve security boundaries;
- add tests with behavior;
- avoid opportunistic future-scope work;
- avoid unrelated refactors.

Exit condition:

```text
Current batch implemented.
```

---

## STATE 7 — VERIFICATION

Relevant checks may include:

```text
lint
typecheck
unit tests
integration tests
build
E2E/browser tests
security negative tests
manual QA
```

The exact set depends on project type and risk.

A written feature without verification is not considered done.

---

## STATE 8 — CHALLENGE / QA

gstack is used selectively here.

Possible jobs:

```text
engineering review
design review
code review
investigation
browser QA
release review
cross-model challenge
```

Trigger gstack when the expected quality improvement justifies extra context/cost.

Do not run every gstack skill after every tiny change.

---

## STATE 9 — CONVERGENCE

Compare:

```text
SPEC
↕
CODE
↕
TESTS
↕
ACCEPTANCE CRITERIA
```

Missing work becomes a small follow-up task.

Do not rewrite the whole roadmap because one criterion failed.

Result:

```text
PHASE COMPLETE
```

or:

```text
PHASE NOT COMPLETE
```

---

## STATE 10 — NEXT PHASE

After `PHASE COMPLETE`:

1. mark persistent state only where needed;
2. switch current phase;
3. do not preload completed phase details;
4. repeat planning → implementation → verification → converge.

---

## STATE 11 — RELEASE

Before release, choose gates by project risk.

Typical production-oriented flow:

```text
all current acceptance criteria
→ full relevant tests
→ migration review
→ security checks
→ browser/E2E QA
→ observability/config review
→ release/ship review
→ deploy
→ production smoke test
```

High-risk projects may require explicit human approval before destructive migration or release.

---

# 3. Tool ownership

The most important integration rule is that tools do not own the same job.

```text
Token-Efficient Spec Kit
    = project memory, architecture discipline, context budget

GitHub Spec Kit
    = WHAT to build

Superpowers
    = HOW to implement/debug/test

Superpowers Implementation Bridge
    = handoff between WHAT and HOW

gstack
    = challenge / review / browser QA / ship layer

Context7
    = fresh technical documentation on demand
```

If two tools attempt to create duplicate planning artifacts, the Token-Efficient ownership model wins.

---

# 4. Context routing

## New project initialization

Read:

```text
constitution
system operating docs
tooling status
user goal
```

Do not read irrelevant integration docs if tooling is already ready.

---

## Normal implementation session

Read:

```text
constitution
PROJECT_BRIEF
ARCHITECTURE
ENGINEERING_RULES
current phase
relevant ADR only
relevant source/tests
```

---

## Bug fix

Start with:

```text
bug symptoms
relevant code
relevant tests
```

Load architecture only if the bug crosses architectural boundaries.

---

## Change request

Read:

```text
PROJECT_BRIEF
ARCHITECTURE
ROADMAP
affected phases/ADRs/code only
```

Do not reread unrelated project history.

---

## Production incident

Prioritize:

```text
symptoms
logs/errors
production diff/recent changes
relevant subsystem
```

Do not begin with full project replanning.

---

# 5. Complexity routing

## Tier S

Examples:

```text
landing page
small script
CLI
single feature
simple automation
```

Workflow:

```text
Brief
→ short plan
→ tasks
→ implement
→ verify
```

Avoid architecture ceremony unless needed.

---

## Tier M

Examples:

```text
SaaS MVP
ecommerce
internal dashboard
plugin + backend
mobile MVP
```

Workflow:

```text
Brief
→ Architecture
→ Roadmap
→ Current Phase
→ Spec/Plan/Tasks
→ Implementation batches
→ Converge
```

---

## Tier L

Examples:

```text
marketplace
multi-role SaaS
complex multi-tenancy
critical migrations
financial workflows
sensitive data
```

Workflow adds selective gates:

```text
risk model
clarification where consequential
architecture review
negative tests
analysis
stronger release review
```

Tier L does not mean microservices by default.

---

# 6. Risk routing

Risk is separate from project size.

A small feature can still be High Risk.

High-risk triggers include:

```text
payments
authentication
authorization
private user files
PII/sensitive data
financial records
destructive migrations
public API compatibility
security controls
production infrastructure
```

For high-risk changes use more evidence:

```text
negative tests
idempotency tests
permission tests
review
rollback/recovery planning
```

Do not respond to risk by automatically introducing architectural complexity.

---

# 7. Standard user interactions

## Start

User:

```text
Хочу сделать ...
```

Entry:

```text
START_NEW_PROJECT
```

---

## Continue

User:

```text
Продолжай разработку.
```

Entry:

```text
CONTINUE_PROJECT
```

---

## Review current phase

User:

```text
Проверь текущий этап и закрой его, если всё выполнено.
```

Entry:

```text
REVIEW_CURRENT_PHASE
```

---

## Change requirements

User:

```text
Теперь нужно добавить ...
```

Entry:

```text
CHANGE_REQUEST
```

---

## Bug

User:

```text
Вот ошибка / неправильное поведение ...
```

Entry:

```text
BUG_FIX
```

---

# 8. Persistent state vs chat state

Chat is temporary execution context.

Repository is durable project memory.

Important durable truth must live in:

```text
PROJECT_BRIEF
ARCHITECTURE
ROADMAP
current phase
ADR when justified
source code/tests
```

Do not depend on an old chat session to remember critical architecture.

But do not copy every chat message into repository docs either.

Only persistent truth should survive.

---

# 9. Token budget principles

## Keep

```text
compact canonical files
small phase specs
small implementation batches
selective research
selective reviews
```

## Avoid

```text
duplicate PRDs
repeated architecture summaries
raw research dumps
reading the whole repo every run
four parallel planning frameworks
large status reports saved after every task
```

Token efficiency is not about giving the model too little context.

It is about giving it **the smallest context that still contains all decision-critical information**.

---

# 10. Example complete lifecycle

```text
USER:
"Хочу marketplace digital assets."

↓ START_NEW_PROJECT

Tooling check
↓
Project Brief
↓
Architecture
↓
Roadmap

Phase 00 — Foundation
↓
Spec Kit plan/tasks
↓
Superpowers implementation
↓
Tests/build
↓
Converge
↓
PHASE COMPLETE

Phase 01 — Catalog
↓
...

Phase 05 — Payments (High Risk)
↓
Spec
↓
Plan
↓
Negative-test requirements
↓
Implementation
↓
Review
↓
Webhook/payment tests
↓
Converge

...

Release Candidate
↓
gstack QA/review
↓
Full relevant tests
↓
Deploy
↓
Smoke test
↓
Production
```

---

# 11. Final operating rule

At any moment the agent should be able to answer four questions without loading the entire project:

```text
1. What product are we building?
   → PROJECT_BRIEF

2. How is it built?
   → ARCHITECTURE

3. What are we doing now?
   → CURRENT PHASE

4. What proves it is done?
   → ACCEPTANCE CRITERIA + TESTS
```

If these four answers are clear, the workflow is healthy.
