# Руководство по использованию Token-Efficient Spec Kit

> Практическое руководство: что делать пользователю, что делает AI-агент и как вести проект от одной идеи до production.

---

## Короткая версия

Для нового проекта тебе достаточно трёх действий:

```text
1. Клонировать Token-Efficient Spec Kit
2. Открыть repository в Codex / Claude Code / Cursor / другом coding agent
3. Запустить prompts/START_NEW_PROJECT.md и заменить <WHAT_I_WANT>
```

Например:

```text
Хочу приложение для дизайнеров, где можно хранить,
искать и автоматически тегировать локальные 3D-ассеты.
```

После этого агент должен самостоятельно:

```text
проверить tooling
→ понять продукт
→ выбрать лучший практичный stack
→ спроектировать architecture
→ создать roadmap
→ разбить проект на phases
→ начать первые 1–3 задачи
→ проверить результат
```

Тебе не нужно заранее выбирать framework, database, auth, hosting и другие обычные инженерные детали.

---

# 1. Что находится в этом шаблоне

Token-Efficient Spec Kit состоит из нескольких уровней.

```text
Constitution
    ↓
System Rules
    ↓
Project Brief + Architecture + Roadmap
    ↓
Current Phase
    ↓
Implementation
    ↓
Verification / Review
```

Основные файлы:

```text
.specify/memory/constitution.md
    Постоянные принципы работы AI-агента.

docs/system/
    Как агент принимает решения, выбирает stack,
    контролирует complexity и расход контекста.

docs/project/
    Текущее состояние конкретного проекта.

docs/phases/
    Маленькие этапы разработки.

docs/decisions/
    Только важные architecture decisions (ADR).

integrations/
    Правила работы Spec Kit, Superpowers,
    gstack и Context7 без конфликтов.

prompts/
    Готовые entry points для разных ситуаций.
```

---

# 2. Новый проект

## Шаг 1 — создать repository из шаблона

Самый простой вариант:

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
```

После этого желательно создать собственный новый Git repository / remote для реального проекта, чтобы история самого шаблона не смешивалась с историей продукта.

Если проект уже существует, можно перенести workflow-файлы в существующий repository вместо клонирования как нового приложения.

---

## Шаг 2 — открыть repository в AI coding agent

Workflow рассчитан на repository-aware agent, например:

```text
Codex
Claude Code
Cursor
Gemini CLI
OpenCode
другой совместимый coding harness
```

Не требуется постоянно использовать один и тот же model/provider.

Canonical project knowledge хранится в repository, а не только в истории конкретного чата.

---

## Шаг 3 — запустить START_NEW_PROJECT

Открой:

```text
prompts/START_NEW_PROJECT.md
```

Замени:

```text
<WHAT_I_WANT>
```

на описание желаемого результата.

Можно писать очень коротко:

```text
Хочу сервис для генерации коммерческих предложений для архитекторов.
```

Или подробно:

```text
Хочу web app для небольших архитектурных студий.
Пользователь загружает Excel со сметой, выбирает фирменный шаблон,
а система генерирует аккуратное PDF-коммерческое предложение.
Нужны аккаунты, история документов и платная подписка.
```

Чем больше у тебя реальных бизнес-ограничений, тем полезнее их сразу указать.

Не нужно придумывать технические ограничения, если они тебе не важны.

---

# 3. Что происходит после первого prompt

## Step 0 — Tooling bootstrap

Агент читает:

```text
docs/project/TOOLING_STATUS.md
```

Если Recommended tooling ещё не настроен для текущего coding harness, агент должен самостоятельно запустить setup-процесс.

Recommended profile:

```text
GitHub Spec Kit
+ Superpowers
+ Superpowers Implementation Bridge
+ gstack
+ Context7
```

Агент использует актуальные upstream installation instructions, потому что способы установки AI tooling быстро меняются.

После успешной настройки он обновляет:

```text
docs/project/TOOLING_STATUS.md
```

Tooling не должен переустанавливаться в каждой сессии.

### Когда потребуется твоё участие

Агент может остановиться, если требуется:

- OAuth/login;
- API key, который он не может получить сам;
- установка system runtime с твоим разрешением;
- destructive overwrite;
- выбор между двумя реально разными бизнес-сценариями.

Обычные engineering decisions не являются поводом для вопроса.

---

## Step 1 — понимание продукта

Агент создаёт:

```text
docs/project/PROJECT_BRIEF.md
```

В нём фиксируются только важные вещи:

```text
Desired outcome
Primary users
Core jobs
Must-have requirements
Explicit constraints
Assumptions
Out of scope
Success criteria
Project type
Complexity: S / M / L
Risk: Low / Medium / High
```

Это компактная canonical версия того, **что именно мы строим**.

Не нужно создавать несколько PRD с одинаковой информацией.

---

## Step 2 — выбор технологий

Агент самостоятельно исследует только те технологии, где актуальность действительно имеет значение.

Например:

```text
framework APIs
payment providers
auth libraries
deployment limits
AI SDK
current pricing/licensing
security-sensitive integrations
```

Для свежей library/API documentation может использоваться Context7.

Результат исследования не превращается в огромный research document.

Агент сохраняет только решения, влияющие на проект.

---

## Step 3 — architecture

Агент создаёт:

```text
docs/project/ARCHITECTURE.md
```

Он должен выбрать **один рекомендуемый stack**, если нет реальной причины оставить несколько вариантов.

Например:

```text
Frontend: Next.js
Backend: Next.js server layer
Database: PostgreSQL
Auth: Better Auth
Storage: Cloudflare R2
Hosting: Vercel
Testing: Vitest + Playwright
```

Но никакой stack не зафиксирован глобально — другой проект может получить совершенно другую архитектуру.

В Architecture также фиксируются:

- system diagram;
- sources of truth;
- security boundaries;
- operational assumptions;
- причины, при которых решение нужно пересмотреть.

---

## Step 4 — roadmap

Агент создаёт:

```text
docs/project/ROADMAP.md
```

и отдельные файлы:

```text
docs/phases/00-...
docs/phases/01-...
docs/phases/02-...
```

Каждый phase должен давать проверяемый результат.

Хорошо:

```text
Phase 01 — Authentication
Phase 02 — Asset library
Phase 03 — Search
Phase 04 — Payments
```

Плохо:

```text
Phase 01 — Frontend
Phase 02 — Backend
Phase 03 — Database
```

если такие этапы невозможно нормально проверить как пользовательский результат.

---

# 4. Как проходит обычная разработка

После инициализации проекта начинается повторяющийся цикл.

```text
Current Phase
    ↓
Spec / Plan / Tasks
    ↓
1–3 cohesive tasks
    ↓
Implementation
    ↓
Tests
    ↓
Review / QA
    ↓
Converge
    ↓
Phase Complete
    ↓
Next Phase
```

Главное правило:

> **Одна рабочая сессия обычно делает 1–3 связанные задачи, а не пытается реализовать весь проект.**

Так агент держит маленький context и реже ломает уже принятые решения.

---

# 5. Как продолжить работу завтра или в новой сессии

Не нужно снова объяснять агенту весь проект.

Запусти:

```text
prompts/CONTINUE_PROJECT.md
```

Он должен прочитать только:

```text
Constitution
Project Brief
Architecture
Engineering Rules
Current Phase
Relevant ADR
Relevant source code/tests
```

После этого он определяет следующие 1–3 незавершённые задачи и продолжает работу.

### Что НЕ должно происходить

Агент не должен каждый раз перечитывать:

```text
все старые phases
все ADR
всю историю чатов
все research documents
весь repository без необходимости
```

---

# 6. Как завершить текущий phase

Запусти:

```text
prompts/REVIEW_CURRENT_PHASE.md
```

Агент сравнит:

```text
Phase Spec
↕
Implementation
↕
Tests
↕
Acceptance Criteria
```

Если есть gaps — он исправляет только их.

Результат должен быть одним из:

```text
PHASE COMPLETE
```

или:

```text
PHASE NOT COMPLETE
```

После `PHASE COMPLETE` можно переходить к следующему phase.

---

# 7. Если ты захотел изменить продукт

Например в середине проекта решил:

```text
Добавить multi-user teams.
```

Не нужно вручную редактировать все specs.

Используй:

```text
prompts/CHANGE_REQUEST.md
```

и опиши изменение.

Например:

```text
Нужно добавить workspace и приглашение нескольких пользователей.
У каждого workspace должен быть владелец и участники.
```

Агент должен сначала определить impact:

```text
PROJECT_BRIEF?
ARCHITECTURE?
DATABASE?
AUTH?
ROADMAP?
CURRENT PHASE?
MIGRATIONS?
SECURITY?
```

и изменить только затронутые canonical docs.

---

# 8. Если появился баг

Используй:

```text
prompts/BUG_FIX.md
```

Передай симптом:

```text
После refresh пользователь иногда становится logged out.
```

Bug workflow:

```text
Reproduce
→ Root cause
→ Smallest correct fix
→ Regression test
→ Verification
```

Для обычного бага агент не должен загружать всю архитектуру проекта, если проблема локальная.

---

# 9. Как используются дополнительные инструменты

Recommended profile специально разделяет ответственность.

## Token-Efficient Spec Kit

Отвечает за:

```text
intent
architecture discipline
context budget
project state
phase boundaries
```

## GitHub Spec Kit

Отвечает за **WHAT**:

```text
specify
clarify when necessary
plan
tasks
analyze when necessary
converge
```

## Superpowers

Отвечает за **HOW**:

```text
TDD
systematic implementation
debugging
verification discipline
```

## Superpowers Implementation Bridge

Не даёт Spec Kit и Superpowers создавать два параллельных planning workflow.

Основная модель:

```text
Spec Kit = WHAT
Superpowers = HOW
```

## gstack

Это challenge / QA layer.

Он используется там, где даст реальную пользу:

```text
engineering review
design review
code review
browser QA
investigation
release / ship checks
```

Он не должен автоматически запускаться после каждой маленькой правки.

## Context7

Используется для актуальной документации library/API.

Он не нужен для каждой функции или каждой строки кода.

---

# 10. Когда какой quality gate нужен

## Обычная feature

```text
spec
→ plan
→ tasks
→ implement
→ tests
→ converge
```

## Неоднозначная feature

Добавляется:

```text
clarify
```

## Security / payments / permissions

Добавляются:

```text
negative tests
review
analyze
```

## Сложный UI

Полезны:

```text
gstack design review
browser QA
Playwright / E2E
```

## Перед production release

Полезны:

```text
full relevant test suite
security review
gstack ship/release checks
migration review
observability verification
```

Не нужно использовать все quality gates для каждого изменения.

---

# 11. Как общаться с агентом после старта

Ты можешь продолжать говорить обычным языком.

### Новый проект

```text
Хочу приложение для ...
```

### Новая функция

```text
Добавь возможность делиться проектом по публичной ссылке.
```

### Изменение требований

```text
Теперь нужен не только Google login, но и email/password.
```

### Баг

```text
После удаления файла счётчик storage не обновляется.
```

### UX feedback

```text
Мне не нравится текущая product page. Сделай её визуально проще,
но не меняй checkout flow.
```

### Архитектурный вопрос

```text
Проверь, не пора ли вынести background jobs из основного приложения.
```

Агент сам должен определить, какой workflow применить и какие docs нужно обновить.

---

# 12. Что должен делать пользователь, а что агент

| Пользователь | AI-agent |
|---|---|
| Определяет желаемый продукт | Выбирает stack |
| Даёт реальные business constraints | Проектирует architecture |
| Принимает важные product decisions | Создаёт specs и roadmap |
| Даёт feedback по результату | Делит работу на tasks |
| Даёт credentials/login при необходимости | Пишет код |
| Подтверждает destructive/high-impact actions | Пишет tests |
| Может переопределить любое решение | Делает review / QA |

Пользователь остаётся владельцем продукта.

Engineering autonomy агента означает не отсутствие контроля, а отсутствие необходимости вручную управлять каждым техническим выбором.

---

# 13. Как работать с уже существующим проектом

Не запускай workflow так, будто repository пустой.

Перед planning агент должен:

1. изучить текущую структуру;
2. определить существующий stack;
3. найти реальные conventions;
4. понять current architecture;
5. сохранить совместимость;
6. создать Project Brief / Architecture как описание существующей системы;
7. только после этого планировать изменения.

Нельзя переписывать работающий проект на любимый stack агента без необходимости.

---

# 14. Когда нужно создавать ADR

ADR нужен только для существенного и трудно обратимого решения.

Например:

```text
PostgreSQL как primary database
Multi-tenant data isolation strategy
Object storage provider
Event-driven processing boundary
Authentication architecture
```

ADR обычно НЕ нужен для:

```text
названия React component
utility function
иконки
CSS property
маленькой package
```

Меньше лишней документации = меньше лишнего контекста.

---

# 15. Что делать перед release

Перед production агент должен проверить релевантные пункты:

```text
Acceptance criteria
Build
Typecheck
Lint
Unit tests
Integration tests
E2E/browser tests
Security negative tests
Database migrations
Secrets/configuration
Backups where relevant
Monitoring / error tracking
Critical user flow
Rollback/recovery where relevant
```

Не каждый проект требует каждый пункт, но high-risk части не должны выпускаться только потому, что happy path работает.

---

# 16. Полный пример одного проекта

Ты начинаешь с:

```text
Хочу веб-приложение, которое позволяет загружать PDF,
задавать вопросы по документу и сохранять историю чатов.
```

Агент создаёт:

```text
PROJECT_BRIEF.md
ARCHITECTURE.md
ROADMAP.md
```

Например roadmap:

```text
Phase 00 — Foundation
Phase 01 — Authentication
Phase 02 — PDF upload and storage
Phase 03 — Document processing
Phase 04 — Q&A chat
Phase 05 — History
Phase 06 — Production hardening
```

В текущей сессии агент делает только:

```text
Phase 00
Task 1
Task 2
Task 3
```

На следующий день ты запускаешь:

```text
CONTINUE_PROJECT.md
```

После завершения Phase 00:

```text
REVIEW_CURRENT_PHASE.md
```

Получаешь:

```text
PHASE COMPLETE
```

и переходишь к Authentication.

Если потом говоришь:

```text
Нужна командная работа над документами.
```

используется Change Request, roadmap и architecture корректируются только там, где это необходимо.

---

# 17. Главный принцип

Не пытайся управлять AI-agent как junior-разработчиком через тысячи микроинструкций.

Опиши:

```text
что нужно получить
почему это нужно
какие реальные ограничения существуют
```

А Token-Efficient Spec Kit должен заставить агента самостоятельно определить:

```text
как лучше это построить
как разбить работу
что проверить
какой контекст нужен сейчас
```

> **Ты управляешь продуктом. Агент управляет инженерным исполнением. Repository хранит общую память.**
