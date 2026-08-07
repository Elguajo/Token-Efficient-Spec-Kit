# Maintenance — здоровье и обновление Token-Efficient Spec Kit

Этот раздел нужен не для ежедневной разработки продукта, а для обслуживания самого workflow и диагностики проекта.

Если ты впервые используешь Token-Efficient Spec Kit, сначала прочитай [`../README.md`](../README.md) и [`USAGE_GUIDE.md`](USAGE_GUIDE.md).

---

## Project Doctor — понять состояние проекта

Если непонятно, что сейчас происходит с repository, используй:

```text
prompts/PROJECT_DOCTOR.md
```

Doctor должен объяснить человеческим языком:

```text
Health: HEALTHY / NEEDS ATTENTION / BLOCKED / UNKNOWN
Current phase
Что уже сделано
Что осталось
Какие проверки проходят или падают
Есть ли проблемы с workflow/tooling
Что лучше делать дальше
NEXT SESSION PROMPT
```

Doctor по умолчанию диагностирует, а не начинает новую feature-разработку.

Подробный protocol: [`system/PROJECT_DOCTOR.md`](system/PROJECT_DOCTOR.md).

---

## Workflow Self-Audit — проверить сам framework

После значимых изменений Token-Efficient Spec Kit используй:

```text
prompts/AUDIT_WORKFLOW.md
```

Audit проверяет:

- согласованность Constitution, AGENTS, docs и prompts;
- duplicate ownership и competing planning flows;
- default vs optional tooling;
- Session Handoff;
- token/context creep;
- stale paths и links;
- safe-update boundaries;
- VERSION / CHANGELOG consistency.

Self-Audit сначала показывает проблемы и минимальные исправления. Он не должен самовольно переделывать весь framework.

Подробный protocol: [`system/WORKFLOW_SELF_AUDIT.md`](system/WORKFLOW_SELF_AUDIT.md).

---

## Safe Workflow Update — обновить framework без потери проекта

Для обновления Token-Efficient Spec Kit внутри существующего продукта используй:

```text
prompts/UPDATE_WORKFLOW.md
```

Основной принцип:

> **Framework можно обновить. Product state нельзя перезаписывать template defaults.**

Updater различает три группы файлов.

### Framework-managed

```text
docs/system/*
integrations/*
templates/*
prompts/*
```

Их можно обновлять после сравнения локальных изменений.

### Merge-sensitive

```text
.specify/memory/constitution.md
AGENTS.md
VERSION
CHANGELOG.md
```

Их нельзя слепо заменять — нужно сохранять осознанные локальные изменения.

### Project-owned

```text
docs/project/*
docs/phases/*
docs/decisions/*
source code
tests
migrations
credentials / secrets
product-specific docs
```

Их updater не должен автоматически перезаписывать.

После framework update необходимо прогнать Workflow Self-Audit.

Полная политика: [`system/WORKFLOW_UPDATE_POLICY.md`](system/WORKFLOW_UPDATE_POLICY.md).

---

## Versioning

Текущая версия framework хранится в:

```text
../VERSION
```

История изменений:

```text
../CHANGELOG.md
```

Используется схема:

```text
MAJOR.MINOR.PATCH
```

- **PATCH** — совместимые исправления;
- **MINOR** — новые совместимые capabilities;
- **MAJOR** — breaking изменения workflow/file contracts.

При изменении поведения framework нужно обновить `VERSION` и `CHANGELOG.md` согласованно.

---

## Optional Advanced Spec Mode

GitHub Spec Kit не входит в default profile.

Если конкретная фаза действительно требует более формальной глубокой спецификации, используй:

```text
prompts/ENABLE_ADVANCED_SPEC_MODE.md
```

Примеры подходящих случаев:

```text
payments
complex authorization
multi-tenancy
public API contracts
critical migrations
large ambiguous cross-system integrations
```

Подробности: [`../integrations/SPEC_KIT.md`](../integrations/SPEC_KIT.md).

---

## Open-source maintenance

Для публичной разработки repository также содержит:

- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — правила contributions;
- [`../SECURITY.md`](../SECURITY.md) — security policy;
- [`../CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md) — правила взаимодействия;
- [`../CHANGELOG.md`](../CHANGELOG.md) — история изменений;
- [`../VERSION`](../VERSION) — текущая версия;
- `.github/ISSUE_TEMPLATE/` — шаблоны issues;
- `.github/PULL_REQUEST_TEMPLATE.md` — checklist pull requests.

---

## Быстрая памятка

| Нужно | Используй |
|---|---|
| Понять состояние проекта | `prompts/PROJECT_DOCTOR.md` |
| Проверить целостность самого workflow | `prompts/AUDIT_WORKFLOW.md` |
| Безопасно обновить framework | `prompts/UPDATE_WORKFLOW.md` |
| Включить formal deep-spec режим | `prompts/ENABLE_ADVANCED_SPEC_MODE.md` |
| Посмотреть историю framework | `CHANGELOG.md` + `VERSION` |
