# Интеграции

Token-Efficient Spec Kit является **самостоятельным core workflow**.

Дополнительные инструменты усиливают отдельные части процесса, но не управляют проектом целиком.

## Recommended profile — default

```text
Token-Efficient Spec Kit
+ Superpowers
+ Semble
+ RTK
+ gstack
+ Context7
```

Роли:

```text
Token-Efficient Spec Kit
→ intent, Project Brief, Architecture, Roadmap, phases, tasks,
  acceptance criteria, context routing, convergence, session handoff

Superpowers
→ HOW: TDD, implementation discipline, systematic debugging, verification

Semble
→ CODE CONTEXT: находить только релевантные куски codebase

RTK
→ TOOL OUTPUT: сокращать шум terminal/test/build/git output

gstack
→ challenge / review / browser QA / release checks

Context7
→ fresh library/API docs on demand
```

Таким образом token-efficiency работает на нескольких уровнях:

```text
Project/docs context → Token-Efficient Spec Kit
Code retrieval       → Semble
Terminal output      → RTK
External docs        → Context7 on demand
```

## Автоматическая установка

При первом `START_NEW_PROJECT.md` агент проверяет `docs/project/TOOLING_STATUS.md`.

Если Recommended profile ещё не настроен, он автоматически запускает:

```text
prompts/SETUP_RECOMMENDED_TOOLING.md
```

и пытается установить/настроить:

```text
Superpowers
Semble
RTK
gstack
Context7
```

После успешной настройки состояние записывается в `docs/project/TOOLING_STATUS.md`, поэтому установка не повторяется в каждой сессии.

Для Semble предпочтительна MCP-интеграция, когда active harness её поддерживает.

Для RTK setup должен выбрать самый безопасный текущий agent-specific integration. Если единственный рабочий вариант меняет глобальные user-level hooks/instructions для всех проектов, требуется одноразовое подтверждение пользователя перед такой глобальной настройкой.

Любой внешний token-saving tool должен иметь graceful fallback: если интеграция сломана или недоступна, проект продолжает работу обычными средствами coding agent.

Подробнее:

- [`SEMBLE.md`](SEMBLE.md)
- [`RTK.md`](RTK.md)
- [`SUPERPOWERS.md`](SUPERPOWERS.md)
- [`GSTACK.md`](GSTACK.md)
- [`CONTEXT7.md`](CONTEXT7.md)

## Optional Advanced Spec Mode

GitHub Spec Kit не является обязательным dependency.

Подключай его только для фаз, где formal specification действительно улучшает качество:

```text
payments
complex permissions
multi-tenancy
critical migrations
public API contracts
large ambiguous features
high-risk integrations
```

Тогда модель такая:

```text
Token-Efficient Spec Kit
→ project-level source of truth

GitHub Spec Kit
→ optional deep feature/phase specification

Superpowers Bridge
→ optional coordination only when both Spec Kit and Superpowers are enabled
```

Подробнее: [`SPEC_KIT.md`](SPEC_KIT.md).

## Canonical project state

Остаётся в:

```text
.specify/memory/constitution.md
docs/project/PROJECT_BRIEF.md
docs/project/ARCHITECTURE.md
docs/project/ROADMAP.md
docs/phases/
docs/project/NEXT_SESSION.md
code/tests
```

Ни один внешний tool не должен создавать второй project-level source of truth.
