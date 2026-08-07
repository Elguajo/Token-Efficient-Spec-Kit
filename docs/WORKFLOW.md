# Token-Efficient Spec Kit — End-to-End Workflow

> Техническая карта: какие состояния проходит проект, какой контекст читает AI и какой инструмент отвечает за каждый слой.

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
1–3 TASKS
    ↓
IMPLEMENTATION
    ↓
VERIFICATION / REVIEW / QA
    ↓
CONVERGENCE
    ↓
PHASE STATE?
    ├── IN PROGRESS ──► handoff for same phase
    ├── COMPLETE ─────► handoff for next roadmap phase
    └── PROJECT COMPLETE ─► release/audit/deploy handoff
                              ↓
                     NEXT SESSION PROMPT
                              ↓
                        FRESH SESSION
```

Chat — временный execution context. Repository — долговременная память проекта.

---

# 2. Кто является core

**Token-Efficient Spec Kit — самостоятельный project orchestration layer.**

Он владеет:

```text
User Intent
Project Brief
Architecture
Roadmap
Phases
Phase Tasks
Acceptance Criteria
Context Routing
Quality Routing
Convergence
Session Handoff
```

Внешние инструменты не становятся вторым project-level source of truth.

---

# 3. Tool ownership

```text
Token-Efficient Spec Kit
= WHAT + orchestration + project memory + handoff

Superpowers
= HOW: TDD, implementation discipline, systematic debugging, verification

gstack
= challenge / review / browser QA / release checks

Context7
= fresh technical documentation on demand

GitHub Spec Kit
= OPTIONAL Advanced Spec Mode for formal deep specification inside a difficult phase
```

Если два инструмента пытаются создать competing project-level plans, Token-Efficient canonical docs побеждают.

---

# 4. Состояния проекта

## STATE 0 — TEMPLATE

```text
PROJECT_BRIEF  → not initialized
ARCHITECTURE   → not initialized
ROADMAP        → not initialized
TOOLING_STATUS → not initialized / ready
NEXT_SESSION   → not initialized
```

Entry point:

```text
prompts/START_NEW_PROJECT.md
```

---

## STATE 1 — TOOLING BOOTSTRAP

Default Recommended profile:

```text
Superpowers
gstack
Context7
```

GitHub Spec Kit не устанавливается по умолчанию.

Output:

```text
docs/project/TOOLING_STATUS.md
```

Tooling bootstrap не повторяется в каждой сессии.

---

## STATE 2 — PRODUCT DEFINITION

AI превращает пользовательское описание в compact canonical truth.

Writes:

```text
docs/project/PROJECT_BRIEF.md
```

Содержит только decision-critical product truth, assumptions и blockers.

---

## STATE 3 — ARCHITECTURE

AI выбирает один практичный recommended architecture.

Writes:

```text
docs/project/ARCHITECTURE.md
```

ADR создаётся только для consequential hard-to-reverse решений.

---

## STATE 4 — ROADMAP

AI создаёт independently verifiable phases:

```text
docs/project/ROADMAP.md
docs/phases/00-....md
docs/phases/01-....md
...
```

Roadmap depth адаптируется к сложности проекта.

---

## STATE 5 — CURRENT PHASE

Canonical input:

```text
current phase file
```

Token-Efficient Spec Kit определяет:

```text
Goal
Context
In scope
Out of scope
Tasks
Acceptance Criteria
Negative/security tests where relevant
Verification
```

Recommended implementation batch:

```text
1–3 cohesive tasks
```

### Optional Advanced Spec Mode

Если текущая фаза materially ambiguous, cross-cutting или high-risk, AI может подключить GitHub Spec Kit для formal deep specification.

Примеры:

```text
payments
complex authorization
multi-tenancy boundaries
critical migrations
public API contracts
large cross-system integrations
```

GitHub Spec Kit работает **внутри текущей фазы** и не заменяет Project Brief, Architecture, Roadmap или Session Handoff.

---

## STATE 6 — IMPLEMENTATION

Superpowers/native coding harness отвечает за HOW.

Agent reads only:

```text
Constitution
PROJECT_BRIEF
ARCHITECTURE
ENGINEERING_RULES
current phase
relevant ADR
relevant source/tests
```

Avoid:

```text
all completed phases
all ADRs
full chat history
entire repository without need
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

---

## STATE 8 — CHALLENGE / QA

gstack используется выборочно:

```text
engineering review
design review
code review
investigation
browser QA
release review
```

Trigger only when expected quality improvement justifies extra context/cost.

---

## STATE 9 — CONVERGENCE

Compare:

```text
PHASE SPEC
↕
CODE
↕
TESTS
↕
ACCEPTANCE CRITERIA
```

Missing work становится маленьким follow-up task.

Result:

```text
IN PROGRESS
PHASE COMPLETE
PROJECT COMPLETE
```

---

## STATE 10 — SESSION HANDOFF

At the end of every meaningful implementation/review session AI must:

1. determine phase/project state;
2. decide the correct next action;
3. update `docs/project/NEXT_SESSION.md`;
4. create a ready-to-copy `NEXT SESSION PROMPT`;
5. stop before starting the next phase in the old session.

This is mandatory because the user may not know the correct engineering next step.

---

## STATE 11 — RELEASE

Production-oriented flow may include:

```text
acceptance criteria
→ full relevant tests
→ migration review
→ security checks
→ browser/E2E QA
→ observability/config review
→ gstack release checks where useful
→ deploy
→ smoke test
```

High-risk destructive actions may require explicit human approval.

---

# 5. Complexity routing

## Tier S

```text
Brief
→ Tasks
→ Implement
→ Verify
→ Handoff
```

Examples: landing page, CLI, small script, simple automation.

## Tier M

```text
Brief
→ Architecture
→ Roadmap
→ Phases
→ Implementation batches
→ Converge
→ Handoff
```

Examples: SaaS MVP, ecommerce, internal dashboard, plugin + backend.

## Tier L / High Risk

Adds stronger quality gates, not automatically more infrastructure:

```text
smaller phases
negative tests
architecture review
more explicit acceptance criteria
selective Advanced Spec Mode
stronger release review
```

---

# 6. Risk routing

High-risk triggers include:

```text
payments
authentication
authorization
private files
PII/sensitive data
financial records
destructive migrations
public APIs
production infrastructure
```

Use more evidence:

```text
negative tests
idempotency tests
permission tests
review
rollback/recovery planning
```

Do not answer risk by automatically introducing microservices or more frameworks.

---

# 7. Context routing

## Normal implementation session

Read:

```text
Constitution
PROJECT_BRIEF
ARCHITECTURE
ENGINEERING_RULES
Current Phase
Relevant ADR
Relevant source/tests
```

## Bug fix

Start with:

```text
symptom
relevant code
relevant tests
```

Load broader architecture only if needed.

## Change request

Read:

```text
PROJECT_BRIEF
ARCHITECTURE
ROADMAP
affected phases/ADRs/code only
```

## Advanced Spec Mode

Load GitHub Spec Kit instructions only when the current phase explicitly enables it.

---

# 8. Persistent state vs chat state

Durable truth lives in:

```text
PROJECT_BRIEF
ARCHITECTURE
ROADMAP
Current Phase
ADRs where justified
code/tests
NEXT_SESSION as navigation only
```

Do not depend on old chats to remember critical project truth.
Do not copy every chat message into repository docs either.

---

# 9. Token budget principles

Keep:

```text
compact canonical files
small phase specs
1–3 task batches
selective research
selective reviews
optional tooling only when useful
```

Avoid:

```text
duplicate PRDs
parallel roadmaps
raw research dumps
reading the whole repo every run
loading installed tools just because they exist
```

Token efficiency means giving the agent the **smallest context that still contains all decision-critical information**.

---

# 10. Healthy workflow test

At any moment AI should be able to answer:

```text
1. What are we building?
   → PROJECT_BRIEF

2. How is it built?
   → ARCHITECTURE

3. What are we doing now?
   → CURRENT PHASE

4. What proves it is done?
   → ACCEPTANCE CRITERIA + TESTS

5. What should the user do next?
   → NEXT_SESSION
```

If these five answers are clear, the workflow is healthy.
