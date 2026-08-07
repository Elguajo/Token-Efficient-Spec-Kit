# Интеграции

Token-Efficient Spec Kit теперь является **самостоятельным core workflow**.

Дополнительные инструменты усиливают отдельные части процесса, но не управляют проектом целиком.

## Recommended profile — default

```text
Token-Efficient Spec Kit
+ Superpowers
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

gstack
→ challenge / review / browser QA / release checks

Context7
→ fresh library/API docs on demand
```

## Optional Advanced Spec Mode

GitHub Spec Kit больше не является обязательным dependency.

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

Ни Superpowers, ни gstack, ни Context7, ни GitHub Spec Kit не должны создавать второй project-level source of truth.

## Установка

Default tooling устанавливается через:

```text
prompts/SETUP_RECOMMENDED_TOOLING.md
```

Он настраивает:

```text
Superpowers
gstack
Context7
```

GitHub Spec Kit устанавливается отдельно только при включении Advanced Spec Mode.

AI-agent должен использовать текущие официальные upstream instructions для активного coding harness.
