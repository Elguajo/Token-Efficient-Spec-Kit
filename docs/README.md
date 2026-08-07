# Документация Token-Efficient Spec Kit

Если ты впервые открыл этот repository, начни отсюда.

## Для пользователя

### [USAGE_GUIDE.md](USAGE_GUIDE.md)

Полное практическое руководство:

- как начать новый проект;
- что нужно написать AI-агенту;
- что агент делает самостоятельно;
- как происходит tooling bootstrap;
- как продолжать проект в новой сессии;
- как закрывать phase;
- как добавлять новые требования;
- как исправлять баги;
- как подготовить release.

Если нужен ответ на вопрос **«что мне теперь делать?»** — открывай этот файл.

---

## Как работает система внутри

### [WORKFLOW.md](WORKFLOW.md)

End-to-end карта процесса:

```text
User Intent
→ Tooling
→ Brief
→ Architecture
→ Roadmap
→ Phase
→ Spec / Plan / Tasks
→ Implementation
→ Verification
→ Converge
→ Release
```

Также описывает:

- state machine проекта;
- context routing;
- complexity tiers;
- risk routing;
- tool ownership;
- quality gates;
- persistent project memory.

Если нужен ответ на вопрос **«что именно делает агент на каждом этапе?»** — открывай этот файл.

---

# Project state

Эти файлы создаются/обновляются для конкретного проекта:

- [`project/PROJECT_BRIEF.md`](project/PROJECT_BRIEF.md) — что строим;
- [`project/ARCHITECTURE.md`](project/ARCHITECTURE.md) — как строим;
- [`project/ROADMAP.md`](project/ROADMAP.md) — в каком порядке;
- [`project/TOOLING_STATUS.md`](project/TOOLING_STATUS.md) — какие AI engineering tools настроены;
- `phases/` — что делаем сейчас;
- `decisions/` — только важные ADR.

---

# System rules

Внутренние правила для AI-agent:

- [`system/OPERATING_MODEL.md`](system/OPERATING_MODEL.md)
- [`system/DECISION_FRAMEWORK.md`](system/DECISION_FRAMEWORK.md)
- [`system/ENGINEERING_RULES.md`](system/ENGINEERING_RULES.md)
- [`system/TOKEN_EFFICIENCY.md`](system/TOKEN_EFFICIENCY.md)
- [`system/CREATIVE_AUTONOMY.md`](system/CREATIVE_AUTONOMY.md)

Пользователю не нужно перечитывать их перед каждой работой.

---

# Main prompts

| Ситуация | Prompt |
|---|---|
| Новый проект | [`../prompts/START_NEW_PROJECT.md`](../prompts/START_NEW_PROJECT.md) |
| Настройка Recommended tooling | [`../prompts/SETUP_RECOMMENDED_TOOLING.md`](../prompts/SETUP_RECOMMENDED_TOOLING.md) |
| Продолжить разработку | [`../prompts/CONTINUE_PROJECT.md`](../prompts/CONTINUE_PROJECT.md) |
| Проверить/закрыть текущий phase | [`../prompts/REVIEW_CURRENT_PHASE.md`](../prompts/REVIEW_CURRENT_PHASE.md) |
| Изменились требования | [`../prompts/CHANGE_REQUEST.md`](../prompts/CHANGE_REQUEST.md) |
| Исправить баг | [`../prompts/BUG_FIX.md`](../prompts/BUG_FIX.md) |

---

# Recommended Tooling

Интеграции описаны в [`../integrations/README.md`](../integrations/README.md).

Default Recommended profile:

```text
Token-Efficient Spec Kit
+ GitHub Spec Kit
+ Superpowers
+ Superpowers Implementation Bridge
+ gstack
+ Context7
```

Главное правило — каждый инструмент имеет свою ответственность и не должен создавать параллельный дублирующий workflow.

---

# Самый короткий путь

```text
1. Прочитать USAGE_GUIDE.md
2. Открыть START_NEW_PROJECT.md
3. Заменить <WHAT_I_WANT>
4. Передать prompt coding-agent
5. Дальше использовать CONTINUE_PROJECT.md
```

В обычной работе пользователю не требуется вручную управлять всей системой документации.
