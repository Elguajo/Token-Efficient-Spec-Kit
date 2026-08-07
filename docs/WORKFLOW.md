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
SPEC / PLAN / TASKS
    ↓
IMPLEMENTATION BATCH
    ↓
VERIFICATION / REVIEW / QA
    ↓
CONVERGE
    ↓
PHASE STATE?
    ├── IN PROGRESS ──► create handoff for same phase
    ├── COMPLETE ─────► create handoff for next roadmap phase
    └── PROJECT COMPLETE ─► release/audit/deploy handoff
                              ↓
                     NEXT SESSION PROMPT
                              ↓
                        FRESH SESSION
```

Процесс циклический. Chat — временный execution context. Repository — долговременная память проекта.

---

# 2. Главный navigation rule

Пользователь не обязан знать, какой engineering step должен быть следующим.

В конце каждой meaningful implementation/review session AI обязан:

1. определить состояние текущей фазы;
2. решить правильный следующий шаг;
3. обновить `docs/project/NEXT_SESSION.md`;
4. выдать готовый `NEXT SESSION PROMPT`;
5. остановиться, не начиная новую фазу автоматически в старой сессии.

Это позволяет переносить работу в новый контекст без пересказа истории и без необходимости пользователю понимать roadmap.

Полные правила: [`system/SESSION_HANDOFF.md`](system/SESSION_HANDOFF.md).

---

# 3. Состояния проекта

## STATE 0 — TEMPLATE

Конкретный product ещё не инициализирован.

```text
PROJECT_BRIEF      → not initialized
ARCHITECTURE       → not initialized
ROADMAP            → not initialized
TOOLING_STATUS     → not initialized / ready
NEXT_SESSION       → not initialized
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

Recommended profile:

```text
GitHub Spec Kit
Superpowers
Superpowers Implementation Bridge
gstack
Context7
```

AI читает только нужные integration docs и использует актуальные upstream installation instructions.

Output:

```text
docs/project/TOOLING_STATUS.md
```

Tooling bootstrap не повторяется в каждой сессии.

---

## STATE 2 — PRODUCT DEFINITION

AI превращает пользовательское описание результата в compact canonical truth.

Writes:

```text
docs/project/PROJECT_BRIEF.md
```

Файл отвечает на вопрос:

> What are we building?

Он разделяет:

```text
facts
explicit constraints
reasonable assumptions
true blockers
```

AI не спрашивает framework/database/hosting preferences, если может принять решение профессионально.

---

## STATE 3 — ARCHITECTURE

AI выбирает самый простой зрелый вариант архитектуры, который безопасно удовлетворяет требованиям.

Writes:

```text
docs/project/ARCHITECTURE.md
```

При необходимости:

```text
docs/decisions/ADR-XXX-....md
```

ADR создаётся только для consequential / cross-cutting / hard-to-reverse решений.

Research selective: Context7 или актуальные official docs используются только там, где freshness действительно влияет на решение.

---

## STATE 4 — ROADMAP

AI создаёт независимо проверяемые product phases.

Writes:

```text
docs/project/ROADMAP.md
docs/phases/00-....md
docs/phases/01-....md
...
```

Depth адаптируется под проект:

```text
S → minimal
M → normal phased roadmap
L → smaller phases + stronger selective gates
```

---

## STATE 5 — CURRENT PHASE PLANNING

Canonical input:

```text
current phase file
```

Tool ownership:

```text
GitHub Spec Kit = WHAT
Superpowers     = HOW
```

Spec Kit может выполнять:

```text
specify
clarify — только если ambiguity consequential
plan
tasks
analyze — только если risk/consistency оправдывает
```

Recommended batch:

```text
1–3 cohesive tasks
```

---

## STATE 6 — IMPLEMENTATION

AI читает минимальный контекст:

```text
constitution
PROJECT_BRIEF
ARCHITECTURE
ENGINEERING_RULES
current phase
relevant ADR if needed
relevant source/tests
```

Не читает автоматически все завершённые phases.

Во время реализации:

- current stable APIs;
- input validation;
- security boundaries;
- behavior-focused tests;
- no accidental future scope;
- no unrelated refactors.

---

## STATE 7 — VERIFICATION

В зависимости от проекта:

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

Written code without relevant verification is not done.

---

## STATE 8 — CHALLENGE / QA

gstack используется выборочно как challenge layer:

```text
engineering review
design review
code review
investigation
browser QA
release review
cross-model challenge where available
```

Не нужно запускать все gstack skills после каждой маленькой правки.

---

## STATE 9 — CONVERGENCE

Сравнение:

```text
SPEC
↕
CODE
↕
TESTS
↕
ACCEPTANCE CRITERIA
```

Результат должен быть одним из:

```text
IN PROGRESS
PHASE COMPLETE
PROJECT COMPLETE
```

Missing work превращается в маленькие follow-up tasks, а не в переписывание всего roadmap.

---

## STATE 10 — SESSION HANDOFF

Это обязательное состояние после meaningful implementation/review work.

### A. Phase IN PROGRESS

AI:

```text
same phase
→ next 1–3 unfinished tasks
→ verification requirements
→ NEXT SESSION PROMPT
```

### B. PHASE COMPLETE

AI:

```text
inspect ROADMAP
→ find next phase
→ do NOT implement it in old session
→ create fresh-session prompt for next phase
```

### C. PROJECT COMPLETE

AI выбирает подходящий следующий шаг:

```text
final audit
release
deployment
security/browser QA
documentation
or no further work
```

Если продукт уже released, новая functionality начинается через `CHANGE_REQUEST.md`.

AI пишет:

```text
docs/project/NEXT_SESSION.md
```

и возвращает:

```text
NEXT SESSION PROMPT

<ready-to-copy prompt>
```

---

## STATE 11 — FRESH SESSION

Пользователь создаёт новую AI-сессию и вставляет handoff prompt.

Новый agent не должен перечитывать историю старого чата.

Prompt ссылается на canonical files и содержит только то, что нельзя надёжно восстановить из repository.

Normal loop:

```text
Session N
→ implementation/review
→ handoff
→ Session N+1
```

Если handoff потерян:

```text
prompts/GENERATE_NEXT_SESSION_PROMPT.md
```

восстанавливает следующий шаг по repository state.

---

## STATE 12 — RELEASE

После реализации roadmap выбираются gates по risk.

Typical production-oriented flow:

```text
acceptance criteria
→ full relevant tests
→ migration review
→ security checks
→ browser/E2E QA
→ observability/config review
→ release/ship review
→ deploy
→ production smoke test
```

High-risk destructive/release actions могут требовать human approval.

---

# 4. Tool ownership

```text
Token-Efficient Spec Kit
    = intent + architecture discipline + context budget + phase/session navigation

GitHub Spec Kit
    = WHAT to build

Superpowers
    = HOW to implement / test / debug

Superpowers Implementation Bridge
    = boundary between WHAT and HOW

gstack
    = challenge / review / browser QA / ship layer

Context7
    = fresh technical documentation on demand
```

Если два инструмента пытаются создать competing canonical plans, ownership rules Token-Efficient Spec Kit имеют приоритет.

---

# 5. Context routing

## New project

```text
constitution
system operating docs
tooling status
user goal
```

## Normal implementation

```text
constitution
PROJECT_BRIEF
ARCHITECTURE
ENGINEERING_RULES
current phase
relevant ADR only
relevant source/tests
```

## New session after handoff

```text
NEXT SESSION PROMPT
+ canonical files referenced by that prompt
+ relevant source/tests
```

Не нужно загружать old chat history.

## Bug fix

Start with:

```text
symptoms
relevant code
relevant tests
```

Architecture загружается только если bug пересекает subsystem boundaries.

## Change request

```text
PROJECT_BRIEF
ARCHITECTURE
ROADMAP
affected phases/ADRs/code only
```

## Production incident

```text
symptoms
logs/errors
recent production changes
relevant subsystem
```

Не начинать incident с полного replanning проекта.

---

# 6. Complexity routing

## Tier S

```text
Brief → short plan → tasks → implement → verify → handoff if more work remains
```

Examples:

```text
landing page
small script
CLI
single feature
simple automation
```

## Tier M

```text
Brief
→ Architecture
→ Roadmap
→ Current Phase
→ Spec/Plan/Tasks
→ Implementation batches
→ Converge
→ Session Handoff
```

Examples:

```text
SaaS MVP
ecommerce
internal dashboard
plugin + backend
mobile MVP
```

## Tier L / High-risk

Добавляются selective gates:

```text
risk model
clarification where consequential
architecture review
negative tests
analysis
stronger release review
```

Tier L не означает microservices by default.

---

# 7. Risk routing

Risk отделён от project size.

High-risk triggers:

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

Для таких changes требуется больше evidence:

```text
negative tests
idempotency tests
permission tests
review
rollback/recovery planning
```

Больше risk ≠ автоматически больше architectural complexity.

---

# 8. Standard user interactions

## Start

```text
prompts/START_NEW_PROJECT.md
```

## Normal next session

Использовать **NEXT SESSION PROMPT**, который дал предыдущий AI.

Это preferred path.

## Continue fallback

```text
prompts/CONTINUE_PROJECT.md
```

Используется, если нужен generic continuation entry point.

## Review current phase

```text
prompts/REVIEW_CURRENT_PHASE.md
```

## Lost / no handoff

```text
prompts/GENERATE_NEXT_SESSION_PROMPT.md
```

## Change requirements

```text
prompts/CHANGE_REQUEST.md
```

## Bug

```text
prompts/BUG_FIX.md
```

---

# 9. Persistent state vs chat state

Chat — temporary execution context.

Repository — durable memory.

Persistent truth:

```text
PROJECT_BRIEF
ARCHITECTURE
ROADMAP
current phase
ADRs when justified
source/tests
```

Navigation state:

```text
NEXT_SESSION.md
```

`NEXT_SESSION.md` не должен дублировать спецификацию. Он отвечает только:

```text
Where are we?
What is next?
What prompt should the user paste?
```

---

# 10. Token budget principles

Keep:

```text
compact canonical files
small phase specs
small implementation batches
selective research
selective reviews
small handoffs
```

Avoid:

```text
duplicate PRDs
repeated architecture summaries
raw research dumps
reading the whole repo every run
full old chat history
multiple competing planning frameworks
huge handoff prompts
```

Token efficiency = **smallest context that still contains all decision-critical information**.

---

# 11. Complete lifecycle example

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
↓
NEXT SESSION PROMPT: start Phase 01

--- new AI session ---

Phase 01 — Catalog
↓
1–3 tasks
↓
...
↓
NEXT SESSION PROMPT

--- new AI session ---

Phase 05 — Payments [High Risk]
↓
Spec / plan
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
↓
NEXT SESSION PROMPT

...

PROJECT COMPLETE
↓
Release/audit handoff
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

# 12. Four canonical questions + one navigation question

В любой момент AI должен отвечать без загрузки всего проекта:

```text
1. What product are we building?
   → PROJECT_BRIEF

2. How is it built?
   → ARCHITECTURE

3. What is the roadmap?
   → ROADMAP

4. What are we doing now and what proves it is done?
   → CURRENT PHASE + ACCEPTANCE CRITERIA + TESTS

5. What should the user do next?
   → NEXT_SESSION
```

Если эти пять ответов ясны, workflow находится в здоровом состоянии.
