# Руководство по использованию Token-Efficient Spec Kit

> Практическое руководство для человека, который может вообще не разбираться в разработке.

Если после чтения остаётся вопрос **«что мне теперь делать?»**, открой [`project/NEXT_SESSION.md`](project/NEXT_SESSION.md) или запусти [`../prompts/PROJECT_DOCTOR.md`](../prompts/PROJECT_DOCTOR.md).

---

# Самая короткая версия

```text
1. Клонировать repository
2. Открыть его в AI coding agent
3. Запустить prompts/START_NEW_PROJECT.md
4. Заменить <WHAT_I_WANT> на своё описание продукта
5. Дальше копировать NEXT SESSION PROMPT, который AI выдаёт в конце каждой сессии
```

Например:

```text
Хочу приложение для дизайнеров, где можно хранить,
искать и автоматически тегировать локальные 3D-ассеты.
```

После этого AI самостоятельно:

```text
понимает продукт
→ выбирает stack
→ проектирует architecture
→ создаёт roadmap
→ делит работу на phases
→ выполняет 1–3 задачи
→ проверяет результат
→ определяет следующий шаг
→ даёт prompt для новой сессии
```

Тебе не нужно заранее выбирать framework, database, auth, hosting или знать, какая фаза должна идти следующей.

---

# 1. Кто за что отвечает

| Пользователь | AI-agent |
|---|---|
| Объясняет желаемый результат | Понимает продукт и пользователей |
| Даёт реальные business constraints | Выбирает stack |
| Даёт feedback | Проектирует architecture |
| Принимает важные product/business decisions | Создаёт roadmap и phases |
| Даёт login/credentials при необходимости | Делит работу на tasks |
| Подтверждает destructive/high-impact actions | Пишет код/tests |
| Может переопределить решение AI | Делает review / QA |
| | **Определяет следующий шаг и пишет следующий prompt** |

> **Ты управляешь продуктом. AI управляет инженерным исполнением и навигацией.**

---

# 2. Новый проект

## Шаг 1 — клонировать шаблон

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
```

Для реального продукта лучше затем привязать папку к своему новому Git repository.

## Шаг 2 — открыть в AI coding agent

Подойдёт repository-aware agent: Codex, Claude Code, Cursor или другой совместимый harness.

## Шаг 3 — запустить START_NEW_PROJECT

Открой:

```text
prompts/START_NEW_PROJECT.md
```

Замени `<WHAT_I_WANT>` на обычное описание того, что хочешь получить.

Можно коротко:

```text
Хочу сервис для генерации коммерческих предложений для архитекторов.
```

Не придумывай технические ограничения, если они тебе не важны.

---

# 3. Что происходит автоматически

AI создаёт и поддерживает:

```text
docs/project/PROJECT_BRIEF.md   → что строим
docs/project/ARCHITECTURE.md    → как строим
docs/project/ROADMAP.md         → в каком порядке
docs/phases/                    → текущие этапы
docs/project/NEXT_SESSION.md    → что делать дальше
```

Обычный цикл:

```text
Current Phase
→ 1–3 tasks
→ Implementation
→ Tests / Review / QA
→ Converge
→ NEXT SESSION PROMPT
→ Fresh Session
```

---

# 4. Recommended tooling

Token-Efficient Spec Kit работает **самостоятельно** и является core workflow.

Default external tooling:

```text
Superpowers
+ gstack
+ Context7
```

Роли:

```text
Token-Efficient Spec Kit
→ WHAT + orchestration + architecture + phases + handoff

Superpowers
→ HOW: TDD, implementation, debugging, verification

gstack
→ challenge / review / browser QA / release checks

Context7
→ fresh library/API docs on demand
```

`START_NEW_PROJECT.md` проверяет tooling status и может автоматически запустить setup.

---

# 5. Нужен ли GitHub Spec Kit?

**Нет, не по умолчанию.**

Наш core уже делает project-level:

```text
Brief
Architecture
Roadmap
Phases
Tasks
Acceptance Criteria
Convergence
Session Handoff
```

GitHub Spec Kit можно подключить как **Optional Advanced Spec Mode** только для сложных фаз, где formal specification реально полезна:

```text
payments
complex permissions
multi-tenancy
critical migrations
public API contracts
large ambiguous integrations
```

В таком режиме он углубляет спецификацию внутри текущей фазы, но не заменяет Project Brief, Architecture, Roadmap или Session Handoff.

Подробнее: [`../integrations/SPEC_KIT.md`](../integrations/SPEC_KIT.md).

---

# 6. Как работать по сессиям

В конце каждой meaningful session AI обязан определить:

```text
IN PROGRESS
PHASE COMPLETE
PROJECT COMPLETE
```

И выдать:

```text
NEXT SESSION PROMPT
```

### IN PROGRESS
Следующий prompt продолжает ту же фазу.

### PHASE COMPLETE
AI сам находит следующую фазу в `ROADMAP.md` и готовит prompt для её старта.

### PROJECT COMPLETE
AI направляет в final audit / release / deployment либо в `CHANGE_REQUEST` для новой функции.

Текущий handoff всегда должен быть записан в:

```text
docs/project/NEXT_SESSION.md
```

Если handoff потерялся:

```text
prompts/GENERATE_NEXT_SESSION_PROMPT.md
```

---

# 7. Ежедневные entry points

| Ситуация | Prompt |
|---|---|
| Новый проект | `prompts/START_NEW_PROJECT.md` |
| Продолжить работу | `prompts/CONTINUE_PROJECT.md` |
| Проверить/закрыть phase | `prompts/REVIEW_CURRENT_PHASE.md` |
| Не понимаю следующий шаг | `prompts/GENERATE_NEXT_SESSION_PROMPT.md` |
| Хочу понять состояние проекта | `prompts/PROJECT_DOCTOR.md` |
| Изменились требования | `prompts/CHANGE_REQUEST.md` |
| Bug | `prompts/BUG_FIX.md` |
| Проверить сам workflow | `prompts/AUDIT_WORKFLOW.md` |
| Обновить framework | `prompts/UPDATE_WORKFLOW.md` |

В идеальном процессе после первого запуска тебе чаще всего достаточно просто копировать `NEXT SESSION PROMPT`.

---

# 8. Почему это экономит токены

Обычная сессия читает:

```text
Constitution
Project Brief
Architecture
Engineering Rules
Current Phase
relevant ADR
relevant code/tests
```

И не перечитывает весь проект без необходимости.

> **Один факт — одно canonical место. Одна сессия — 1–3 связанные задачи.**

---

# 9. Если изменились требования

Используй:

```text
prompts/CHANGE_REQUEST.md
```

AI сам определит, какие canonical docs, phases, migrations или security rules затронуты.

---

# 10. Если появился bug

Используй:

```text
prompts/BUG_FIX.md
```

Workflow:

```text
Reproduce
→ Root cause
→ Smallest correct fix
→ Regression test
→ Verification
→ NEXT SESSION PROMPT
```

---

# 11. Перед release

AI выбирает релевантные quality gates по риску проекта:

```text
Acceptance criteria
Build
Typecheck
Lint
Unit / Integration tests
E2E/browser tests
Security negative tests
Migrations
Secrets/config
Monitoring
Critical user flow
Rollback/recovery where relevant
```

Не каждый проект требует каждый пункт, но high-risk части не должны выпускаться только потому, что happy path работает.

---

# 12. Project Doctor — если ты не понимаешь состояние проекта

Запусти:

```text
prompts/PROJECT_DOCTOR.md
```

Doctor не начинает новую feature-разработку. Он диагностирует repository и объясняет простыми словами:

```text
HEALTHY / NEEDS ATTENTION / BLOCKED / UNKNOWN
какая сейчас фаза
что уже завершено
что осталось
какие checks проходят или падают
есть ли проблема с tooling/workflow
какое одно действие лучше сделать следующим
```

В конце он также даёт `NEXT SESSION PROMPT`, если безопасный следующий шаг можно определить.

Это полезно, если:

- давно не открывал проект;
- другая AI-сессия закончилась непонятно;
- не уверен, завершён ли текущий phase;
- видишь ошибки, но не понимаешь насколько они критичны.

---

# 13. Workflow Self-Audit — проверить сам framework

Project Doctor проверяет **проект**.

Workflow Self-Audit проверяет **наши правила и prompts**.

Запусти:

```text
prompts/AUDIT_WORKFLOW.md
```

Он ищет:

```text
противоречия между Constitution / AGENTS / README / prompts
stale documentation
duplicate planning ownership
лишний context loading
сломанный Session Handoff
небезопасный update behavior
несовпадение VERSION / CHANGELOG
```

Обычно Self-Audit нужен после значимого изменения самого Token-Efficient Spec Kit, а не после каждой feature.

---

# 14. Версии

Текущая версия workflow:

```text
VERSION
```

История:

```text
CHANGELOG.md
```

Используется Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

Это помогает понять, насколько далеко конкретный проект от актуальной версии workflow и нужны ли migration steps.

---

# 15. Как безопасно обновить Token-Efficient Spec Kit

Не копируй новую версию шаблона поверх проекта целиком.

Используй:

```text
prompts/UPDATE_WORKFLOW.md
```

Updater должен разделять файлы на:

### Framework-managed

```text
docs/system/*
integrations/*
templates/*
prompts/*
VERSION
CHANGELOG.md
```

### Merge-sensitive

```text
.specify/memory/constitution.md
AGENTS.md
```

### Project-owned — нельзя автоматически перезаписывать

```text
docs/project/*
docs/phases/*
docs/decisions/*
source code
tests
migrations
credentials
```

После обновления обязательно выполняется Workflow Self-Audit.

Подробнее: [`system/WORKFLOW_UPDATE_POLICY.md`](system/WORKFLOW_UPDATE_POLICY.md).

---

# Главный принцип

Не управляй AI как junior-разработчиком через тысячи микроинструкций.

Опиши:

```text
что хочешь получить
зачем это нужно
какие реальные ограничения есть
```

А workflow должен определить:

```text
как лучше построить
как разбить работу
что проверить
какой инструмент нужен
что делать дальше
```

> **Ты управляешь продуктом. AI управляет инженерным исполнением. Repository хранит общую память.**
