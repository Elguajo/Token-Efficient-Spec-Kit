# Документация Token-Efficient Spec Kit

Если ты впервые открыл этот repository, начни отсюда.

## Для пользователя

### [USAGE_GUIDE.md](USAGE_GUIDE.md)

Практическое руководство от идеи до production:

- как начать новый проект;
- что написать AI-агенту;
- что агент решает самостоятельно;
- как происходит tooling bootstrap;
- как работать по phases;
- как продолжать проект в новой сессии;
- как закрывать phase;
- как менять требования;
- как исправлять bugs;
- как подготовить release.

### [project/NEXT_SESSION.md](project/NEXT_SESSION.md)

Самый простой файл для человека, далёкого от разработки.

Он отвечает на три вопроса:

```text
Где сейчас проект?
Что нужно делать дальше?
Какой prompt скопировать в новую AI-сессию?
```

AI-agent обязан обновлять его после meaningful implementation/review sessions.

### [system/SESSION_HANDOFF.md](system/SESSION_HANDOFF.md)

Правила автоматического перехода между сессиями и phases.

Если текущий phase не закончен — следующий prompt продолжает его.
Если phase завершён — агент сам находит следующий phase в Roadmap и создаёт prompt для новой сессии.
Если проект завершён — агент ведёт в release/audit либо `CHANGE_REQUEST`.

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
→ Current Phase
→ Spec / Plan / Tasks
→ Implementation
→ Verification
→ Converge
→ Session Handoff
→ Next Phase
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

---

# Project state

Canonical state конкретного проекта:

- [`project/PROJECT_BRIEF.md`](project/PROJECT_BRIEF.md) — что строим;
- [`project/ARCHITECTURE.md`](project/ARCHITECTURE.md) — как строим;
- [`project/ROADMAP.md`](project/ROADMAP.md) — в каком порядке;
- [`project/TOOLING_STATUS.md`](project/TOOLING_STATUS.md) — какие AI engineering tools настроены;
- [`project/NEXT_SESSION.md`](project/NEXT_SESSION.md) — что делать человеку дальше;
- `phases/` — текущие и будущие этапы;
- `decisions/` — только важные ADR.

`NEXT_SESSION.md` — это navigation layer, а не дубликат project spec.

---

# System rules

Внутренние правила для AI-agent:

- [`system/OPERATING_MODEL.md`](system/OPERATING_MODEL.md)
- [`system/DECISION_FRAMEWORK.md`](system/DECISION_FRAMEWORK.md)
- [`system/ENGINEERING_RULES.md`](system/ENGINEERING_RULES.md)
- [`system/TOKEN_EFFICIENCY.md`](system/TOKEN_EFFICIENCY.md)
- [`system/CREATIVE_AUTONOMY.md`](system/CREATIVE_AUTONOMY.md)
- [`system/SESSION_HANDOFF.md`](system/SESSION_HANDOFF.md)

Пользователю не нужно перечитывать их перед каждой работой.

---

# Main prompts

| Ситуация | Prompt |
|---|---|
| Новый проект | [`../prompts/START_NEW_PROJECT.md`](../prompts/START_NEW_PROJECT.md) |
| Продолжить разработку | [`../prompts/CONTINUE_PROJECT.md`](../prompts/CONTINUE_PROJECT.md) |
| Проверить/закрыть текущий phase | [`../prompts/REVIEW_CURRENT_PHASE.md`](../prompts/REVIEW_CURRENT_PHASE.md) |
| Не знаю, что делать дальше | [`../prompts/GENERATE_NEXT_SESSION_PROMPT.md`](../prompts/GENERATE_NEXT_SESSION_PROMPT.md) |
| Изменились требования | [`../prompts/CHANGE_REQUEST.md`](../prompts/CHANGE_REQUEST.md) |
| Исправить bug | [`../prompts/BUG_FIX.md`](../prompts/BUG_FIX.md) |
| Ручная настройка Recommended tooling | [`../prompts/SETUP_RECOMMENDED_TOOLING.md`](../prompts/SETUP_RECOMMENDED_TOOLING.md) |

В нормальном workflow агент должен сам выдавать `NEXT SESSION PROMPT`, поэтому отдельный generator нужен только как fallback.

---

# Recommended Tooling

Интеграции: [`../integrations/README.md`](../integrations/README.md)

Default Recommended profile:

```text
Token-Efficient Spec Kit
+ GitHub Spec Kit
+ Superpowers
+ Superpowers Implementation Bridge
+ gstack
+ Context7
```

Каждый инструмент имеет отдельную ответственность и не должен создавать параллельный дублирующий workflow.

---

# Самый короткий путь

```text
1. Клонировать repository
2. Открыть START_NEW_PROJECT.md
3. Заменить <WHAT_I_WANT>
4. Передать prompt AI coding agent
5. Получить результат + NEXT SESSION PROMPT
6. Открыть новую сессию и вставить этот prompt
7. Повторять до завершения проекта
```

Пользователю не требуется вручную разбираться в roadmap, выбирать следующий phase или придумывать новый engineering prompt.
