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
5. AI сам установит/настроит Recommended tooling, если это нужно
6. Дальше копировать NEXT SESSION PROMPT, который AI выдаёт в конце каждой сессии
```

Например:

```text
Хочу приложение для дизайнеров, где можно хранить,
искать и автоматически тегировать локальные 3D-ассеты.
```

После этого AI самостоятельно:

```text
проверяет tooling
→ понимает продукт
→ выбирает stack
→ проектирует architecture
→ создаёт roadmap
→ делит работу на phases
→ получает только нужный code/context
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

## Tooling bootstrap

При первом старте AI проверяет:

```text
docs/project/TOOLING_STATUS.md
```

Если Recommended tooling ещё не готов для активного coding harness, AI запускает `prompts/SETUP_RECOMMENDED_TOOLING.md` и пытается самостоятельно установить/настроить:

```text
Superpowers  → implementation discipline / TDD / debugging
Semble       → token-efficient code retrieval
RTK          → compact terminal/test/build/git output
gstack       → review / QA / release checks
Context7     → fresh library/API docs
```

После проверки состояние сохраняется в `TOOLING_STATUS.md`, поэтому setup не повторяется в каждой сессии.

Тебе может понадобиться вмешаться только если реально нужен login/OAuth, отсутствующий system runtime или глобальная настройка hooks/instructions, которая затронет другие проекты.

Semble и RTK имеют graceful fallback: если их нельзя безопасно подключить, проект продолжает работу обычными search/read/shell средствами.

## Project state

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
→ targeted code retrieval
→ 1–3 tasks
→ Implementation
→ compact verification output
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
+ Semble
+ RTK
+ gstack
+ Context7
```

Роли:

```text
Token-Efficient Spec Kit
→ WHAT + orchestration + project/docs context + architecture + phases + handoff

Semble
→ CODE CONTEXT: находит только релевантные chunks/locations

RTK
→ TOOL OUTPUT: сокращает verbose shell/test/build/git output

Superpowers
→ HOW: TDD, implementation, debugging, verification

gstack
→ challenge / review / browser QA / release checks

Context7
→ fresh library/API docs on demand
```

Главная token-efficiency модель:

```text
Project/docs context → Token-Efficient Spec Kit
Code retrieval       → Semble
Shell/tool output     → RTK
External docs        → Context7 on demand
```

Semble не нужно насильно использовать для известного маленького файла. RTK не нужно использовать, если для debugging требуется полный raw output. Correctness всегда важнее token savings.

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
| Продолжить работу | предыдущий `NEXT SESSION PROMPT` |
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

Token-Efficient Spec Kit экономит контекст на нескольких уровнях:

```text
1. Не загружает весь project history
2. Держит current work в маленькой phase
3. Использует Semble для targeted code retrieval
4. Использует RTK для compact shell output
5. Подтягивает Context7 только когда нужны свежие docs
```

> **Один факт — одно canonical место. Одна сессия — 1–3 связанные задачи. Загружай только decision-critical context.**

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

При debugging Semble/RTK не должны скрывать нужную информацию: AI может перейти к точечному raw/full context, если это необходимо для root cause.

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

---

# 13. Workflow Self-Audit — проверить сам framework

Project Doctor проверяет **проект**.

Workflow Self-Audit проверяет **наши правила и prompts**.

Запусти:

```text
prompts/AUDIT_WORKFLOW.md
```

Он ищет противоречия, stale docs/prompts, duplicate ownership, лишний context loading, broken handoff, unsafe update behavior и VERSION/CHANGELOG drift.

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

Используется Semantic Versioning: `MAJOR.MINOR.PATCH`.

---

# 15. Как безопасно обновить Token-Efficient Spec Kit

Не копируй новую версию шаблона поверх проекта целиком.

Используй:

```text
prompts/UPDATE_WORKFLOW.md
```

Updater различает framework-managed, merge-sensitive и project-owned files. `docs/project/*`, phases, ADRs, application code, tests и migrations нельзя автоматически перезаписывать template defaults.

После обновления выполняется Workflow Self-Audit.

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
какой context нужен
что проверить
какой инструмент нужен
что делать дальше
```

> **Ты управляешь продуктом. AI управляет инженерным исполнением. Repository хранит общую память.**
