# Руководство по использованию Token-Efficient Spec Kit

> Практическое руководство для человека, который может вообще не разбираться в разработке.

Если после чтения этого файла остаётся вопрос **«что мне теперь делать?»**, открой [`project/NEXT_SESSION.md`](project/NEXT_SESSION.md). Там AI должен хранить готовый следующий шаг и copy-paste prompt.

---

# Самая короткая версия

Для нового проекта достаточно:

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

После этого AI должен самостоятельно:

```text
проверить tooling
→ понять продукт
→ выбрать практичный stack
→ спроектировать architecture
→ создать roadmap
→ разбить работу на phases
→ выполнить первые 1–3 задачи
→ проверить результат
→ определить следующий шаг
→ дать prompt для новой сессии
```

Тебе не нужно заранее выбирать framework, database, auth, hosting или знать, какая фаза должна идти следующей.

---

# 1. Что делает пользователь, а что делает AI

| Пользователь | AI-agent |
|---|---|
| Объясняет, что хочет получить | Понимает продукт и пользователей |
| Даёт реальные business constraints | Выбирает stack |
| Даёт feedback | Проектирует architecture |
| Принимает важные product/business decisions | Создаёт roadmap и phases |
| Даёт login/credentials при необходимости | Делит работу на tasks |
| Подтверждает destructive/high-impact actions | Пишет код и tests |
| Может переопределить решение AI | Делает review / QA |
| | **Определяет следующий шаг и пишет следующий prompt** |

Главный принцип:

> **Ты управляешь продуктом. AI управляет инженерным исполнением и навигацией по проекту.**

---

# 2. Новый проект

## Шаг 1 — клонировать шаблон

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
```

Для реального продукта лучше затем привязать папку к своему новому Git repository, чтобы история шаблона не смешивалась с историей продукта.

Если проект уже существует, workflow-файлы можно перенести в существующий repository.

---

## Шаг 2 — открыть repository в AI coding agent

Workflow рассчитан на repository-aware coding agent, например:

```text
Codex
Claude Code
Cursor
Gemini CLI
OpenCode
другой совместимый coding harness
```

Главная память проекта хранится в repository, а не только в истории конкретного чата.

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

на желаемый результат.

Можно написать одну строку:

```text
Хочу сервис для генерации коммерческих предложений для архитекторов.
```

Или подробнее:

```text
Хочу web app для небольших архитектурных студий.
Пользователь загружает Excel со сметой, выбирает фирменный шаблон,
а система генерирует PDF-коммерческое предложение.
Нужны аккаунты, история документов и платная подписка.
```

Указывай реальные ограничения, если они есть. Не придумывай технические решения только потому, что считаешь, что их «надо указать».

---

# 3. Что AI делает после первого prompt

## 3.1 Tooling bootstrap

AI проверяет:

```text
docs/project/TOOLING_STATUS.md
```

Если Recommended profile ещё не готов для текущего coding harness, `START_NEW_PROJECT.md` запускает setup автоматически.

Recommended profile:

```text
GitHub Spec Kit
+ Superpowers
+ Superpowers Implementation Bridge
+ gstack
+ Context7
```

Tooling не должен переустанавливаться в каждой сессии.

AI может остановиться только если действительно требуется твоё участие, например:

- OAuth/login;
- API key;
- установка system runtime с разрешением;
- destructive overwrite;
- важный business/product выбор, который нельзя безопасно предположить.

---

## 3.2 Project Brief

AI создаёт:

```text
docs/project/PROJECT_BRIEF.md
```

Там хранится компактный ответ на вопрос:

> **Что именно мы строим?**

Обычно:

```text
Desired outcome
Primary users
Core jobs
Must-have requirements
Constraints
Assumptions
Out of scope
Success criteria
Project type
Complexity: S / M / L
Risk: Low / Medium / High
```

---

## 3.3 Architecture

AI выбирает **один рекомендуемый stack**, если нет реальной причины оставить несколько вариантов, и записывает его в:

```text
docs/project/ARCHITECTURE.md
```

Он учитывает:

- requirement fit;
- simplicity;
- maintainability;
- security;
- operational burden;
- cost;
- near-term growth.

Никакой stack не зафиксирован глобально. Для каждого проекта решение может быть другим.

---

## 3.4 Roadmap и phases

AI создаёт:

```text
docs/project/ROADMAP.md
docs/phases/00-....md
docs/phases/01-....md
...
```

Проект делится на проверяемые фазы.

Хороший пример:

```text
Phase 00 — Foundation
Phase 01 — Authentication
Phase 02 — Asset Library
Phase 03 — Search
Phase 04 — Payments
Phase 05 — Production Hardening
```

Phase должен давать понятный проверяемый результат, а не быть просто техническим слоем вроде «Frontend» или «Database», если это не оправдано задачей.

---

# 4. Как проходит обычная работа

Основной цикл:

```text
Current Phase
    ↓
Spec / Plan / Tasks
    ↓
1–3 связанные задачи
    ↓
Implementation
    ↓
Tests / Review / QA
    ↓
Converge
    ↓
Определение состояния phase
    ↓
NEXT SESSION PROMPT
    ↓
Новая AI-сессия
```

Одна сессия обычно делает **1–3 связанные задачи**, а не весь проект сразу.

Это уменьшает контекст, делает ошибки локальнее и упрощает проверку.

---

# 5. Главное: тебе не нужно знать, что делать дальше

В конце каждой meaningful implementation/review session AI обязан определить одно из трёх состояний:

```text
IN PROGRESS
PHASE COMPLETE
PROJECT COMPLETE
```

После этого он обязан:

1. решить следующий инженерный шаг;
2. обновить `docs/project/NEXT_SESSION.md`;
3. дать в ответе блок `NEXT SESSION PROMPT`;
4. сделать prompt готовым для copy-paste в новую сессию.

## Если phase ещё не закончен

AI продолжает тот же phase и выбирает следующие 1–3 задачи.

## Если phase завершён

AI сам читает `ROADMAP.md`, находит следующий phase и готовит prompt для его старта.

Ты **не должен** вручную решать:

```text
какая фаза следующая?
что нужно прочитать?
какие задачи брать?
нужно ли сначала тестировать?
нужно ли запускать review?
```

## Если весь roadmap завершён

AI должен определить правильный финальный шаг:

```text
release audit
deployment
security review
browser/E2E QA
documentation/release notes
или отсутствие дальнейшей работы
```

Если продукт уже выпущен, новые функции идут через `CHANGE_REQUEST.md`.

Полный протокол: [`system/SESSION_HANDOFF.md`](system/SESSION_HANDOFF.md).

---

# 6. Как начать следующую сессию

Нормальный путь — **не придумывать новый prompt самому**.

В конце предыдущей сессии AI должен дать:

```text
NEXT SESSION PROMPT

<готовый prompt>
```

Ты:

```text
1. создаёшь новую AI-сессию;
2. вставляешь этот prompt;
3. запускаешь;
4. в конце снова получаешь следующий prompt.
```

Так продолжается до завершения проекта.

`CONTINUE_PROJECT.md` остаётся универсальным fallback/entry point, но при нормальной работе handoff prompt точнее, потому что уже знает текущий state.

Если предыдущая сессия закончилась без handoff, используй:

```text
prompts/GENERATE_NEXT_SESSION_PROMPT.md
```

AI восстановит состояние из repository и создаст правильный следующий prompt.

---

# 7. Как закрыть текущий phase

Для явной проверки используй:

```text
prompts/REVIEW_CURRENT_PHASE.md
```

AI сравнит:

```text
Phase Spec
↕
Implementation
↕
Tests
↕
Acceptance Criteria
```

Результат:

```text
PHASE NOT COMPLETE
```

или:

```text
PHASE COMPLETE
```

или, если roadmap завершён:

```text
PROJECT COMPLETE
```

Но ответ на этом не заканчивается — AI обязан также дать **NEXT SESSION PROMPT**.

---

# 8. Если изменились требования

Используй:

```text
prompts/CHANGE_REQUEST.md
```

Например:

```text
Теперь нужно добавить workspace и приглашение нескольких пользователей.
```

AI должен определить impact только на затронутые части:

```text
PROJECT_BRIEF?
ARCHITECTURE?
ROADMAP?
CURRENT PHASE?
DATABASE?
AUTH?
MIGRATIONS?
SECURITY?
```

и не переписывать весь проект без необходимости.

После работы он также должен подготовить handoff для следующей сессии.

---

# 9. Если появился bug

Используй:

```text
prompts/BUG_FIX.md
```

Передай симптом, например:

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
→ Next session handoff if work remains
```

Обычный локальный bug не должен заставлять AI перечитывать весь проект.

---

# 10. Кто за что отвечает в Recommended profile

| Инструмент | Роль |
|---|---|
| **Token-Efficient Spec Kit** | Intent, architecture discipline, phases, context budget, handoff |
| **GitHub Spec Kit** | **WHAT** — specification, plan, tasks, convergence |
| **Superpowers** | **HOW** — implementation, TDD, systematic debugging |
| **Superpowers Bridge** | Разделяет ownership между Spec Kit и Superpowers |
| **gstack** | Engineering/design review, browser QA, release checks |
| **Context7** | Свежая документация libraries/API по необходимости |

Главное правило: инструменты не должны создавать несколько параллельных canonical plans.

---

# 11. Почему workflow экономит токены

Обычная coding-сессия читает только:

```text
Constitution
+ Project Brief
+ Architecture
+ Engineering Rules
+ Current Phase
+ Relevant ADR if needed
+ Relevant source/tests
```

Она не перечитывает автоматически:

```text
все старые phases
все ADR
всю историю чатов
гигантские master specs
сырые research dumps
```

`NEXT_SESSION.md` тоже остаётся маленьким: это navigation layer, а не копия всей спецификации.

---

# 12. Когда нужны дополнительные quality gates

## Обычная feature

```text
spec → plan → tasks → implement → tests → converge
```

## Неоднозначная feature

Добавляется clarification.

## Auth / payments / permissions / private files

Добавляются релевантные:

```text
negative tests
security review
analysis
idempotency/permission tests
```

## Сложный UI

Полезны:

```text
gstack design review
browser QA
Playwright / E2E
```

## Перед production

Полезны:

```text
full relevant tests
security review
migration review
browser QA
observability/config review
release checks
smoke test
```

Не все gates нужны для каждой маленькой задачи.

---

# 13. Если проект уже существует

AI сначала должен изучить существующую систему:

1. stack;
2. architecture;
3. conventions;
4. database/data model;
5. tests;
6. deployment constraints.

После этого `PROJECT_BRIEF.md` и `ARCHITECTURE.md` описывают **реальную существующую систему**, а не повод переписать её на любимый stack агента.

---

# 14. Что такое ADR

ADR создаётся только для существенного и трудно обратимого решения.

Например:

```text
primary database
multi-tenant isolation
object storage strategy
auth architecture
event-processing boundary
```

ADR обычно не нужен для:

```text
названия component
CSS property
маленькой utility function
локальной package без архитектурного эффекта
```

---

# 15. Полный пример

Ты начинаешь:

```text
Хочу веб-приложение, которое позволяет загружать PDF,
задавать вопросы по документу и сохранять историю чатов.
```

AI создаёт примерно такой roadmap:

```text
Phase 00 — Foundation
Phase 01 — Authentication
Phase 02 — PDF Upload
Phase 03 — Document Processing
Phase 04 — Q&A Chat
Phase 05 — History
Phase 06 — Production Hardening
```

Первая сессия:

```text
Phase 00
→ первые 1–3 tasks
→ verification
→ NEXT SESSION PROMPT
```

Если Phase 00 ещё не готов, следующий prompt продолжает Phase 00.

Когда Phase 00 закрыт:

```text
PHASE COMPLETE
```

AI сам определяет:

```text
Next: Phase 01 — Authentication
```

и выдаёт готовый prompt.

Ты открываешь новую сессию, вставляешь его — и работа продолжается.

Тебе не нужно вручную читать roadmap и решать, что спросить у AI.

---

# 16. Какой файл открыть, если потерялся

| Вопрос | Файл |
|---|---|
| Что мы строим? | `docs/project/PROJECT_BRIEF.md` |
| Как это устроено? | `docs/project/ARCHITECTURE.md` |
| Какие этапы впереди? | `docs/project/ROADMAP.md` |
| Что делаем сейчас? | текущий файл в `docs/phases/` |
| **Что мне делать дальше?** | **`docs/project/NEXT_SESSION.md`** |
| Как работает весь процесс? | `docs/WORKFLOW.md` |
| Как устроен handoff? | `docs/system/SESSION_HANDOFF.md` |

---

# 17. Главный принцип

Не нужно управлять AI-agent как junior-разработчиком через сотни микроинструкций.

Опиши:

```text
что хочешь получить
зачем это нужно
какие реальные ограничения существуют
```

Система должна помочь AI самостоятельно определить:

```text
как лучше это построить
как разбить работу
что реализовать сейчас
что проверить
какой контекст нужен
какой следующий шаг
какой prompt дать пользователю для новой сессии
```

> **Ты управляешь продуктом. AI управляет инженерным исполнением. Repository хранит память. NEXT_SESSION.md ведёт тебя дальше.**
