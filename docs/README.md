# Документация Token-Efficient Spec Kit

Если ты впервые открыл repository, начни с [`../README.md`](../README.md).

Дальше выбирай документ по задаче.

---

## Для пользователя

### [USAGE_GUIDE.md](USAGE_GUIDE.md)

Пошаговое руководство:

- как начать новый проект;
- что написать AI;
- что AI решает самостоятельно;
- как автоматически настраивается Recommended tooling;
- как работать по phases;
- как переносить работу между сессиями;
- как менять требования и исправлять bugs.

### [project/NEXT_SESSION.md](project/NEXT_SESSION.md)

Самый простой ответ на вопрос:

> **Что мне делать дальше?**

AI хранит здесь disposable-навигацию и готовый copy-paste prompt. Канонический
phase status остаётся в marker'е [`project/ROADMAP.md`](project/ROADMAP.md); product
handoff обновляет оба файла и final prompt вместе.

### [system/PROJECT_DOCTOR.md](system/PROJECT_DOCTOR.md)

Используй, если хочешь понять состояние проекта человеческим языком.

Entry point: [`../prompts/PROJECT_DOCTOR.md`](../prompts/PROJECT_DOCTOR.md).

---

## Как система работает внутри

### [WORKFLOW.md](WORKFLOW.md)

Полная end-to-end модель:

```text
User Intent
→ Product Directions (normally 3)
→ Recommended Direction (default)
→ Project Brief
→ Architecture
→ Roadmap
→ Scoped Tooling Bootstrap
→ Current Phase
→ Targeted Code Retrieval
→ 1–3 Tasks
→ Implementation
→ Compact Verification Output
→ Review / QA
→ Convergence
→ Session Handoff
→ Fresh Session
```

### [system/SESSION_HANDOFF.md](system/SESSION_HANDOFF.md)

Правила автоматического перехода между sessions и phases.

---

## Maintenance

### [MAINTENANCE.md](MAINTENANCE.md)

Здесь собраны функции обслуживания workflow:

```text
Project Doctor
Workflow Self-Audit
Safe Workflow Update
Versioning
Optional Advanced Spec Mode
Open-source maintenance
```

Основные entry points:

```text
prompts/PROJECT_DOCTOR.md
prompts/AUDIT_WORKFLOW.md
prompts/UPDATE_WORKFLOW.md
prompts/ENABLE_ADVANCED_SPEC_MODE.md
```

---

## Project state

| Файл | Что хранит |
|---|---|
| [`project/PROJECT_BRIEF.md`](project/PROJECT_BRIEF.md) | Что строим |
| [`project/ARCHITECTURE.md`](project/ARCHITECTURE.md) | Как строим |
| [`project/ROADMAP.md`](project/ROADMAP.md) | В каком порядке |
| [`project/TOOLING_STATUS.md`](project/TOOLING_STATUS.md) | Какие дополнительные tools настроены |
| [`project/NEXT_SESSION.md`](project/NEXT_SESSION.md) | Что делать дальше |
| `phases/` | Текущие и будущие этапы |
| `decisions/` | Важные ADR |

---

## Основные prompts

| Ситуация | Prompt |
|---|---|
| Новый проект | [`../prompts/START_NEW_PROJECT.md`](../prompts/START_NEW_PROJECT.md) |
| Продолжить работу | [`../prompts/CONTINUE_PROJECT.md`](../prompts/CONTINUE_PROJECT.md) |
| Проверить/закрыть phase | [`../prompts/REVIEW_CURRENT_PHASE.md`](../prompts/REVIEW_CURRENT_PHASE.md) |
| Не знаю следующий шаг | [`../prompts/GENERATE_NEXT_SESSION_PROMPT.md`](../prompts/GENERATE_NEXT_SESSION_PROMPT.md) |
| Понять состояние проекта | [`../prompts/PROJECT_DOCTOR.md`](../prompts/PROJECT_DOCTOR.md) |
| Изменились требования | [`../prompts/CHANGE_REQUEST.md`](../prompts/CHANGE_REQUEST.md) |
| Исправить bug | [`../prompts/BUG_FIX.md`](../prompts/BUG_FIX.md) |

---

## Интеграции

Default external tooling:

```text
Superpowers
+ Semble
+ Serena
+ RTK
+ gstack
+ Context7
```
> Канонический источник профиля: [`../integrations/PROFILES.md`](../integrations/PROFILES.md).

Token-efficiency layers:

```text
Project/docs context         → Token-Efficient Spec Kit
Intent-based code discovery  → Semble
Symbol semantics/refactoring → Serena
Shell/tool output            → RTK
Fresh external docs          → Context7 on demand
```

Harness/status проверяются рано, но profile выбирается после Product Brief,
Architecture и Roadmap. Superpowers/Context7 можно настроить сразу; Semble,
Serena, RTK и gstack откладываются до появления кода и реальной пользы. Tier S может
остаться на Minimal profile.

GitHub Spec Kit — optional Advanced Spec Mode.

Подробнее: [`../integrations/README.md`](../integrations/README.md).

---

## Самый короткий путь

```text
START_NEW_PROJECT
→ Product Brief / Architecture / Roadmap
→ scoped tooling bootstrap when useful
→ AI выполняет работу
→ NEXT SESSION PROMPT
→ новая session
→ вставить prompt
→ повторять до PROJECT COMPLETE
```

Если потерялся в проекте — запусти `PROJECT_DOCTOR.md`.
