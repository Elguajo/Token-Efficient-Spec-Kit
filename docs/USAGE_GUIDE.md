# Руководство по использованию Token-Efficient Spec Kit

> Практическое руководство для человека, который может вообще не разбираться в разработке.

Если после чтения остаётся вопрос **«что мне теперь делать?»**, открой [`project/NEXT_SESSION.md`](project/NEXT_SESSION.md) или запусти [`../prompts/PROJECT_DOCTOR.md`](../prompts/PROJECT_DOCTOR.md).

---

# Самая короткая версия

```text
1. Клонировать repository
2. Открыть его в AI coding agent
3. Одним сообщением сказать AI, что хочешь создать, и попросить запустить prompts/START_NEW_PROJECT.md
4. AI предложит product-направления и продолжит с рекомендованным
5. После определения stack/tier AI сам scoped-настроит полезную часть tooling profile
6. Дальше копировать NEXT SESSION PROMPT, который AI выдаёт в конце каждой сессии
```

Например:

```text
Запусти prompts/START_NEW_PROJECT.md.
Хочу приложение для дизайнеров, где можно хранить, искать и автоматически
тегировать локальные 3D-ассеты.
```

После этого AI самостоятельно:

```text
понимает продукт
→ предлагает несколько product-направлений
→ выбирает рекомендуемое
→ выбирает stack
→ проектирует architecture
→ создаёт roadmap
→ scoped-проверяет и настраивает tooling
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

## Шаг 2 — открыть в AI coding agent

Подойдёт repository-aware agent: Codex, Claude Code, Cursor или другой совместимый harness.

## Шаг 3 — одним сообщением опиши идею

В чате с AI-agent напиши:

```text
Запусти prompts/START_NEW_PROJECT.md.
Хочу сервис для генерации коммерческих предложений для архитекторов.
```

Не открывай prompt и не ищи в нём ничего для замены. Не придумывай технические
ограничения, если они тебе не важны.

Сначала AI обычно предложит три product-направления, отметит рекомендуемое и
продолжит с ним автоматически. Он попросит выбрать вариант, только когда без этого
нельзя безопасно разрешить существенный product/business trade-off.

---

# 3. Что происходит автоматически

## Scoped tooling bootstrap

При первом старте AI рано проверяет harness и существующий status:

```text
docs/project/TOOLING_STATUS.md
```

Но профиль выбирается только после Product Brief, Architecture и Roadmap, когда
уже известны stack и tier. При необходимости AI использует
`prompts/SETUP_RECOMMENDED_TOOLING.md` и scoped-настраивает:

```text
Project Brief → Architecture → Roadmap → Scoped Tooling Bootstrap
```

```text
Superpowers  → implementation discipline / TDD / debugging
Semble       → intent-based code discovery
Serena       → symbols / references / diagnostics / semantic refactoring
RTK          → compact terminal/test/build/git output
gstack       → review / QA / release checks
Context7     → fresh library/API docs
```
> Канонический источник профиля: [`../integrations/PROFILES.md`](../integrations/PROFILES.md). Здесь копия для удобства чтения — при расхождении верен PROFILES.md.


Superpowers и Context7 можно установить сразу, когда это безопасно. Semble, Serena,
RTK и gstack обычно откладываются до появления codebase, поддерживаемого language
backend, достаточно шумных build/test команд или реального review/QA gate. Tier S может остаться на Minimal profile;
Tier M/L обычно достигает полного Recommended profile после появления кода.

После проверки installed/deferred/skipped состояние сохраняется в
`TOOLING_STATUS.md`, поэтому setup не повторяется в каждой сессии.

Тебе может понадобиться вмешаться только если реально нужен login/OAuth, отсутствующий system runtime или глобальная настройка, которая затронет другие проекты.

Semble, Serena и RTK имеют graceful fallback: если их нельзя безопасно использовать, проект продолжает работу обычными средствами.

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
→ routed code context
→ 1–3 tasks
→ Implementation
→ compact verification output
→ Tests / Review / QA
→ Converge
→ NEXT SESSION PROMPT
→ Fresh Session
```

---

# 4. Как Semble, Serena и RTK работают вместе

Это важно: **AI не запускает все инструменты подряд.**

Он сначала определяет тип вопроса.

| Вопрос / действие | Что использовать |
|---|---|
| «Где находится логика оплаты подписки?» | **Semble** |
| «Кто вызывает `refreshSession`?» | **Serena** |
| «Какие implementations у этого interface?» | **Serena** |
| «Переименуй symbol во всём проекте безопасно» | **Serena** |
| «Измени одну известную строку в config» | native tools |
| Запустить tests / build / git и не засорить context | **RTK** |

Типичный совместный flow:

```text
Semble
→ нашёл file/snippet/symbol
→ broad discovery закончен
→ Serena только если нужны references / diagnostics / semantic refactor
→ implementation
→ RTK только для shell/test/build output
```

### Почему они не конфликтуют

Serena настраивается как **symbol/refactor layer**.

По возможности у неё отключаются overlapping generic tools:

```text
file reading/search
regex search/replace
shell execution
Serena memory
```

Долговременная память проекта остаётся в Token-Efficient canonical docs, а broad semantic discovery остаётся за Semble.

Главное правило:

> **Не задавай Semble и Serena один и тот же discovery-вопрос без причины.**

Если Semble уже нашёл exact symbol, Serena получает его как вход для отдельной symbol-level задачи, а не начинает поиск заново.

Подробнее: [`../integrations/SERENA.md`](../integrations/SERENA.md).

---

# 5. Recommended tooling

Token-Efficient Spec Kit работает **самостоятельно** и является core workflow.

Default external tooling:

```text
Superpowers
+ Semble
+ Serena
+ RTK
+ gstack
+ Context7
```

Token-efficiency модель:

```text
Project/docs context         → Token-Efficient Spec Kit
Intent-based code discovery  → Semble
Symbol semantics/refactoring → Serena
Shell/tool output            → RTK
External docs                → Context7 on demand
```

Correctness всегда важнее token savings. Не нужно использовать внешний tool, если native operation дешевле и надёжнее.

---

# 6. Нужен ли GitHub Spec Kit?

**Нет, не по умолчанию.**

Наш core уже делает project-level Brief, Architecture, Roadmap, Phases, Tasks, Acceptance Criteria, Convergence и Session Handoff.

GitHub Spec Kit можно подключить как **Optional Advanced Spec Mode** только для сложных фаз, где formal specification реально полезна.

Подробнее: [`../integrations/SPEC_KIT.md`](../integrations/SPEC_KIT.md).

---

# 7. Как работать по сессиям

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

Product handoff всегда обновляется как единое целое:

```text
docs/project/ROADMAP.md marker
+ docs/project/NEXT_SESSION.md
+ NEXT SESSION PROMPT
```

Исключения: неинициализированный template и framework-only audit/update не должны
инициализировать или менять `docs/project/*`, но всё равно заканчиваются готовым
следующим prompt.

Если handoff потерялся:

```text
prompts/GENERATE_NEXT_SESSION_PROMPT.md
```

---

# 8. Ежедневные entry points

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

---

# 9. Почему это экономит токены

```text
1. Не загружает весь project history
2. Держит current work в маленькой phase
3. Использует Semble только для broad intent-based discovery
4. Использует Serena только для точных symbol-level операций
5. Использует RTK для compact shell output
6. Подтягивает Context7 только когда нужны свежие docs
```

> **Один факт — одно canonical место. Одна сессия — 1–3 связанные задачи. Один вопрос — сначала один подходящий tool.**

---

# 10. Если изменились требования

Используй `prompts/CHANGE_REQUEST.md`. AI сам определит, какие canonical docs, phases, migrations или security rules затронуты.

---

# 11. Если появился bug

Используй `prompts/BUG_FIX.md`.

Workflow:

```text
Reproduce
→ Root cause
→ Smallest correct fix
→ Regression test
→ Verification
→ NEXT SESSION PROMPT
```

Если root cause требует понимания call/reference graph, Serena полезнее повторных grep/read циклов. Если для debugging нужен полный лог, RTK должен уступить raw output.

---

# 12. Перед release

AI выбирает релевантные quality gates по риску проекта: acceptance criteria, build, typecheck, lint, tests, E2E/browser, security negatives, migrations, secrets/config, monitoring и critical flows.

---

# 13. Project Doctor

Если не понимаешь состояние проекта, запусти:

```text
prompts/PROJECT_DOCTOR.md
```

Doctor объясняет состояние проекта простыми словами и даёт следующий безопасный шаг.

---

# 14. Workflow Self-Audit

После значимых изменений самого framework используй:

```text
prompts/AUDIT_WORKFLOW.md
```

Self-Audit должен также проверять, что Semble и Serena не получили overlapping default ownership.

---

# 15. Версии и обновление

Текущая версия хранится в `VERSION`, история — в `CHANGELOG.md`.

Для безопасного обновления workflow используй:

```text
prompts/UPDATE_WORKFLOW.md
```

Не копируй новую версию шаблона поверх проекта целиком.

---

# Главный принцип

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
какой tool дешевле и точнее для текущего вопроса
что проверить
что делать дальше
```

> **Ты управляешь продуктом. AI управляет инженерным исполнением. Repository хранит общую память.**
