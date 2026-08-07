# Tooling Profiles

## 1. Minimal

```text
Token-Efficient Spec Kit
+ GitHub Spec Kit
```

Использовать для:

- небольших проектов;
- быстрых prototypes;
- landing pages;
- CLI;
- простых automations.

Плюс: минимум инструментов и минимальный context overhead.

---

## 2. Recommended — default

```text
Token-Efficient Spec Kit
+ GitHub Spec Kit
+ Superpowers
+ Superpowers Implementation Bridge
+ gstack
+ Context7
```

Использовать для большинства production-oriented проектов.

### Что даёт каждый слой

**GitHub Spec Kit**

```text
specification
planning
tasks
consistency analysis
convergence
```

**Superpowers**

```text
TDD
systematic debugging
implementation discipline
verification
code-review habits
```

**Superpowers Implementation Bridge**

```text
Spec Kit owns WHAT
Superpowers owns HOW
```

Bridge нужен, чтобы два methodology layer не генерировали конкурирующие планы и не расходовали лишний контекст.

**gstack**

В Recommended profile использовать преимущественно:

```text
engineering plan review
design review
code review
browser QA
investigation
release/ship checks
cross-model challenge where available
```

Не использовать gstack как второй canonical planning system по умолчанию.

**Context7**

Использовать только когда нужны актуальные library/API docs.

Не вызывать автоматически на каждой задаче.

---

## 3. Full / Experimental

Не является default.

Может включать дополнительные orchestration/review systems, multi-model review, governance extensions или project-specific MCP servers.

Добавлять только после отдельного решения, потому что несколько overlapping methodology frameworks быстро увеличивают token usage и могут конфликтовать.

---

## Automatic profile selection

Если пользователь явно не выбрал профиль:

```text
Tier S + Low Risk
→ Minimal

Tier M
→ Recommended

Tier L / High Risk
→ Recommended + selective project-specific quality gates
```

High Risk не означает автоматически «установить больше framework'ов».

High Risk означает более строгие проверки, negative tests и review gates.
