# Интеграции

Token-Efficient Spec Kit является **самостоятельным core workflow**.

Дополнительные инструменты усиливают отдельные части процесса, но не управляют проектом целиком.

## Recommended profile — default

```text
Token-Efficient Spec Kit
+ Superpowers
+ Semble
+ Serena
+ RTK
+ gstack
+ Context7
```
> Canonical profile definition: [`PROFILES.md`](PROFILES.md). This listing is a copy for reading convenience — if the two disagree, PROFILES.md wins.


Роли:

```text
Token-Efficient Spec Kit
→ intent, Project Brief, Architecture, Roadmap, phases, tasks,
  acceptance criteria, context routing, convergence, session handoff

Superpowers
→ HOW: TDD, implementation discipline, systematic debugging, verification

Semble
→ CODE DISCOVERY: найти релевантную логику по смыслу

Serena
→ SYMBOL / REFACTOR: symbols, references, implementations,
  diagnostics и semantic refactoring

RTK
→ TOOL OUTPUT: сокращать шум terminal/test/build/git output

gstack
→ challenge / review / browser QA / release checks

Context7
→ fresh library/API docs on demand
```

Таким образом token-efficiency работает на нескольких уровнях:

```text
Project/docs context         → Token-Efficient Spec Kit
Intent-based code discovery  → Semble
Symbol semantics/refactoring → Serena
Terminal output              → RTK
External docs                → Context7 on demand
```

## Semble + Serena: не два поисковика

Они не должны независимо искать одно и то же.

```text
«Где находится логика X?»
→ Semble

«Кто вызывает этот symbol?»
«Переименуй его безопасно во всём проекте»
«Какие implementations у interface?»
→ Serena

«Я уже знаю конкретный маленький файл/строку»
→ native agent tools
```

Типичный совместный flow:

```text
Semble
→ находит релевантный file/snippet/symbol
→ broad discovery заканчивается
→ Serena
→ references / diagnostics / semantic refactor при необходимости
```

Подробнее: [`SERENA.md`](SERENA.md) и [`TOOLING_POLICY.md`](TOOLING_POLICY.md).

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
Serena
RTK
gstack
Context7
```

После успешной настройки состояние записывается в `docs/project/TOOLING_STATUS.md`, поэтому установка не повторяется в каждой сессии.

Для Semble предпочтительна MCP-интеграция, когда active harness её поддерживает.

Для Serena setup должен использовать **актуальный официальный Quick Start**, подключить MCP для active harness и применить project-level overlap policy: generic file/search/shell/memory tools Serena отключаются, когда текущая версия позволяет это сделать. Serena остаётся symbol/refactor layer.

Для RTK setup должен выбрать самый безопасный текущий agent-specific integration. Если единственный рабочий вариант меняет глобальные user-level hooks/instructions для всех проектов, требуется одноразовое подтверждение пользователя перед такой глобальной настройкой.

Любой внешний tool должен иметь graceful fallback: если интеграция сломана или недоступна, проект продолжает работу обычными средствами coding agent.

Подробнее:

- [`SEMBLE.md`](SEMBLE.md)
- [`SERENA.md`](SERENA.md)
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

Ни Serena memory, ни Semble, ни любой другой внешний tool не должны создавать второй project-level source of truth.
