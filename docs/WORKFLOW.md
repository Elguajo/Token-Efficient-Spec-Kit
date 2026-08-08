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
CODE-CONTEXT ROUTER
    ├── intent / unknown location → Semble
    ├── known symbol / references / refactor → Serena
    └── tiny exact edit → native tools
    ↓
1–3 TASKS
    ↓
IMPLEMENTATION
    ↓
COMPACT VERIFICATION OUTPUT
    ↓
REVIEW / QA
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
= WHAT + orchestration + project/docs context + handoff

Semble
= CODE DISCOVERY: intent-based semantic/hybrid retrieval

Serena
= SYMBOL / REFACTOR: symbols, references, implementations,
  diagnostics and semantic refactoring

RTK
= TOOL OUTPUT: compact terminal/test/build/git output

Superpowers
= HOW: TDD, implementation discipline, systematic debugging, verification

gstack
= challenge / review / browser QA / release checks

Context7
= fresh technical documentation on demand

GitHub Spec Kit
= OPTIONAL Advanced Spec Mode for formal deep specification inside a difficult phase
```

Token-efficiency layers:

```text
Project/docs context         → Token-Efficient Spec Kit
Intent-based code discovery  → Semble
Symbol semantics/refactoring → Serena
Shell/tool output            → RTK
Fresh external docs          → Context7 on demand
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
Semble
Serena
RTK
gstack
Context7
```

Bootstrap запускается автоматически из `START_NEW_PROJECT.md`, если `TOOLING_STATUS.md` показывает, что environment не готов.

Rules:

- использовать current official installation docs;
- предпочитать безопасный user/project scope;
- Semble подключать через MCP, когда active harness это поддерживает;
- Serena устанавливать через current official Quick Start, а не stale marketplace recipe;
- Serena project config ограничивать symbol/refactor ролью и отключать generic file/search/shell/memory overlap, когда upstream это поддерживает;
- RTK реально проверять после install, а не доверять только success installer;
- если RTK требует global hooks/instructions для всех проектов и нет безопасного project-scoped пути — запросить одноразовое подтверждение;
- Semble/Serena/RTK имеют graceful fallback и не блокируют продукт.

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

## STATE 5 — CURRENT PHASE + CODE-CONTEXT ROUTER

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

### Routing rule

**Do not call every code-context tool. Choose one first.**

```text
Unknown area / natural-language intent
“Where is X implemented?”
→ Semble

Known symbol / declaration / references / implementations
cross-file rename / semantic edit / symbol diagnostics
→ Serena

Known tiny file/string/config edit
→ native tools
```

Typical combined flow:

```text
Semble
→ finds candidate file/snippet/symbol
→ broad discovery stops
→ Serena only if references / diagnostics / semantic refactor are needed
```

Do not repeat the same discovery via Semble → Serena → grep unless the first result failed, is ambiguous, or independent verification is justified.

If Serena language-server/backend support is unavailable or stale:

```text
Serena DEGRADED
→ Semble/native targeted fallback
```

### Optional Advanced Spec Mode

Если текущая фаза materially ambiguous, cross-cutting или high-risk, AI может подключить GitHub Spec Kit для formal deep specification.

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

## STATE 7 — VERIFICATION / TOOL OUTPUT

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

When RTK is installed and verified safe for the active command/harness, use it to reduce verbose output before it enters AI context.

Correctness outranks compression. If compact output is insufficient:

```text
compact result
→ recover raw/full diagnostics
→ diagnose
→ return to compact mode afterward
```

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

For very small projects, Minimal profile may be sufficient even if Recommended tools are installed globally.

## Tier M

```text
Brief
→ Architecture
→ Roadmap
→ Phases
→ Routed code context
→ Implementation batches
→ Converge
→ Handoff
```

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

Use more evidence, not automatically more frameworks.

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
```

Then choose the cheapest adequate code-context route:

```text
Semble → unknown semantic area
Serena → known symbol / semantic relationship or refactor
native → exact local edit
```

## Bug fix

Start with:

```text
symptom
relevant code
relevant tests
```

Use Serena when root cause requires call/reference/implementation relationships. Use raw diagnostics when RTK compression is insufficient.

## Change request

Read only affected canonical state and code.

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

Semble indexes, Serena indexes/config/memory, and RTK analytics/output caches are **operational tooling state**, not canonical product truth.

Serena memory tools should remain disabled under the Recommended overlap policy so they do not duplicate project memory.

---

# 9. Token budget principles

Keep:

```text
compact canonical files
small phase specs
1–3 task batches
single routed code-context query first
symbol-aware operations when semantics matter
compact tool output
selective research
selective reviews
```

Avoid:

```text
duplicate PRDs
parallel roadmaps
raw research dumps
reading the whole repo every run
Semble + Serena + grep for the same question
full-file/refactor loops when symbol tools can do the job safely
verbose terminal logs when compact output preserves the signal
loading installed tools just because they exist
```

Token efficiency means giving the agent the **smallest context and tool surface that still contains all decision-critical information**.

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

4. Which code-context capability is cheapest for this question?
   → Semble / Serena / native

5. What proves it is done?
   → ACCEPTANCE CRITERIA + TESTS

6. What should the user do next?
   → NEXT_SESSION
```

If these answers are clear and tooling is routed rather than stacked, the workflow is healthy.
