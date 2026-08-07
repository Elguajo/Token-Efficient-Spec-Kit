# Документация Token-Efficient Spec Kit

Если ты впервые открыл repository, начни с [`../README.md`](../README.md), затем при необходимости переходи сюда.

## Для пользователя

### [USAGE_GUIDE.md](USAGE_GUIDE.md)

Практическое руководство:
- как начать проект;
- что написать AI;
- что AI решает самостоятельно;
- как работать по phases;
- как переносить работу между сессиями;
- как менять требования и чинить bugs;
- когда нужны дополнительные инструменты.

### [project/NEXT_SESSION.md](project/NEXT_SESSION.md)

Самый простой ответ на вопрос:

```text
Где сейчас проект?
Что делать дальше?
Какой prompt вставить в новую AI-сессию?
```

AI обязан обновлять этот файл после meaningful implementation/review sessions.

### [system/PROJECT_DOCTOR.md](system/PROJECT_DOCTOR.md)

Диагностика проекта человеческим языком:

```text
здоров ли проект?
какая сейчас фаза?
что уже сделано?
что сломано или неизвестно?
что делать дальше?
```

Entry point: [`../prompts/PROJECT_DOCTOR.md`](../prompts/PROJECT_DOCTOR.md).

### [system/SESSION_HANDOFF.md](system/SESSION_HANDOFF.md)

Правила автоматического перехода между фазами и сессиями.

---

## Как работает система внутри

### [WORKFLOW.md](WORKFLOW.md)

End-to-end модель:

```text
User Intent
→ Project Brief
→ Architecture
→ Roadmap
→ Current Phase
→ 1–3 Tasks
→ Implementation
→ Verification / QA
→ Convergence
→ Session Handoff
→ Fresh Session
```

Token-Efficient Spec Kit является самостоятельным core workflow.

### [system/WORKFLOW_SELF_AUDIT.md](system/WORKFLOW_SELF_AUDIT.md)

Проверяет сам framework на:

- противоречия;
- stale docs/prompts;
- duplicate ownership;
- token/context creep;
- broken handoff;
- unsafe update rules;
- version/changelog drift.

Entry point: [`../prompts/AUDIT_WORKFLOW.md`](../prompts/AUDIT_WORKFLOW.md).

### [system/WORKFLOW_UPDATE_POLICY.md](system/WORKFLOW_UPDATE_POLICY.md)

Определяет безопасное обновление framework-файлов без уничтожения реального project state.

Entry point: [`../prompts/UPDATE_WORKFLOW.md`](../prompts/UPDATE_WORKFLOW.md).

---

# Project state

- [`project/PROJECT_BRIEF.md`](project/PROJECT_BRIEF.md) — что строим;
- [`project/ARCHITECTURE.md`](project/ARCHITECTURE.md) — как строим;
- [`project/ROADMAP.md`](project/ROADMAP.md) — в каком порядке;
- [`project/TOOLING_STATUS.md`](project/TOOLING_STATUS.md) — какие дополнительные tools настроены;
- [`project/NEXT_SESSION.md`](project/NEXT_SESSION.md) — что делать дальше;
- `phases/` — этапы;
- `decisions/` — важные ADR.

---

# Main prompts

| Ситуация | Prompt |
|---|---|
| Новый проект | [`../prompts/START_NEW_PROJECT.md`](../prompts/START_NEW_PROJECT.md) |
| Продолжить работу | [`../prompts/CONTINUE_PROJECT.md`](../prompts/CONTINUE_PROJECT.md) |
| Проверить/закрыть phase | [`../prompts/REVIEW_CURRENT_PHASE.md`](../prompts/REVIEW_CURRENT_PHASE.md) |
| Не знаю следующий шаг | [`../prompts/GENERATE_NEXT_SESSION_PROMPT.md`](../prompts/GENERATE_NEXT_SESSION_PROMPT.md) |
| Понять текущее состояние проекта | [`../prompts/PROJECT_DOCTOR.md`](../prompts/PROJECT_DOCTOR.md) |
| Изменились требования | [`../prompts/CHANGE_REQUEST.md`](../prompts/CHANGE_REQUEST.md) |
| Исправить bug | [`../prompts/BUG_FIX.md`](../prompts/BUG_FIX.md) |
| Проверить сам workflow | [`../prompts/AUDIT_WORKFLOW.md`](../prompts/AUDIT_WORKFLOW.md) |
| Безопасно обновить workflow | [`../prompts/UPDATE_WORKFLOW.md`](../prompts/UPDATE_WORKFLOW.md) |
| Включить Optional Advanced Spec Mode | [`../prompts/ENABLE_ADVANCED_SPEC_MODE.md`](../prompts/ENABLE_ADVANCED_SPEC_MODE.md) |
| Настроить default external tooling | [`../prompts/SETUP_RECOMMENDED_TOOLING.md`](../prompts/SETUP_RECOMMENDED_TOOLING.md) |

---

# Versioning

Текущая версия framework:

```text
../VERSION
```

История изменений:

```text
../CHANGELOG.md
```

Значимые изменения framework behavior должны обновлять оба файла.

---

# Recommended Tooling

Default:

```text
Token-Efficient Spec Kit — CORE
+ Superpowers
+ gstack
+ Context7
```

GitHub Spec Kit и Spec Kit ↔ Superpowers bridge — **Optional Advanced Spec Mode**, а не обязательные dependencies.

Подробнее: [`../integrations/README.md`](../integrations/README.md).

---

# Open-source project files

- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — как предлагать изменения;
- [`../SECURITY.md`](../SECURITY.md) — security policy;
- [`../CHANGELOG.md`](../CHANGELOG.md) — история изменений;
- [`../VERSION`](../VERSION) — текущая версия.

---

# Самый короткий путь

```text
1. Клонировать repository
2. Открыть START_NEW_PROJECT.md
3. Заменить <WHAT_I_WANT>
4. Передать prompt AI coding agent
5. Получить NEXT SESSION PROMPT
6. Открыть новую сессию и вставить его
7. Повторять до PROJECT COMPLETE
```

Если что-то непонятно:

```text
PROJECT_DOCTOR.md
```

Если кажется, что сам workflow начал противоречить себе:

```text
AUDIT_WORKFLOW.md
```

Пользователю не требуется самостоятельно выбирать следующий phase или придумывать engineering prompts.
