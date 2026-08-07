# Contributing to Token-Efficient Spec Kit

Спасибо за интерес к проекту.

Token-Efficient Spec Kit — это не набор случайных prompts. Это компактный AI engineering workflow, поэтому изменения должны сохранять четыре свойства:

```text
clarity
+ token efficiency
+ engineering autonomy
+ safe project-state boundaries
```

---

## Перед изменением

Сначала прочитай:

- `README.md`;
- `docs/WORKFLOW.md`;
- `.specify/memory/constitution.md`;
- `AGENTS.md`;
- `docs/system/WORKFLOW_SELF_AUDIT.md`.

Для изменений tooling/integrations также прочитай:

- `integrations/README.md`;
- `integrations/TOOLING_POLICY.md`.

---

## Главные правила

### Не создавай второй canonical workflow

Default core уже владеет:

```text
Project Brief
Architecture
Roadmap
Phases
Task batches
Convergence
Session Handoff
```

Новый инструмент должен усиливать конкретную capability, а не создавать параллельную систему планирования.

### Не увеличивай контекст без причины

Новая документация должна иметь понятного владельца и назначение.

Перед добавлением нового постоянно читаемого файла спроси:

> Можно ли сделать это on-demand prompt/tool вместо постоянного context layer?

### Защищай project-owned state

Нельзя проектировать update/setup flows, которые без явной необходимости перезаписывают:

```text
docs/project/*
docs/phases/*
docs/decisions/*
application code
tests
migrations
credentials
```

### Сохраняй non-developer UX

Пользователь не обязан понимать инженерный roadmap.
После meaningful work AI должен уметь выдать следующий понятный шаг и `NEXT SESSION PROMPT`.

---

## Типы изменений

Хорошие contributions:

- уменьшают token/context overhead;
- улучшают качество AI implementation/review;
- делают workflow понятнее для non-developers;
- улучшают session handoff;
- добавляют безопасные optional capabilities;
- исправляют противоречия между docs/prompts;
- улучшают update/migration safety;
- добавляют evals или quality checks.

Изменения, которые требуют особого обоснования:

- новый обязательный AI framework/tool;
- новый всегда-читаемый документ;
- новый parallel planning layer;
- усложнение default workflow;
- изменение file ownership boundaries;
- изменение handoff contract.

---

## Версионирование

Проект использует Semantic Versioning.

При изменении framework behavior:

1. обнови `VERSION`;
2. добавь запись в `CHANGELOG.md`;
3. при breaking migration обнови `docs/system/WORKFLOW_UPDATE_POLICY.md` или добавь migration notes.

---

## Self-Audit перед PR

Перед предложением значимого изменения запусти логику:

```text
prompts/AUDIT_WORKFLOW.md
```

Минимально проверь:

- нет ownership contradictions;
- default/optional tooling описан одинаково во всех местах;
- session handoff не сломан;
- README соответствует реальному workflow;
- нет лишнего full-context loading;
- project-owned files остаются защищены;
- paths/links актуальны.

---

## Стиль

- Пиши конкретно и коротко.
- Не создавай role-play personas без необходимости.
- Не сохраняй длинные research dumps в canonical docs.
- Выбирай один recommended default, когда альтернативы не имеют реального product/business tradeoff.
- Сложные детали выноси в system/integration docs, а README держи понятным.

---

## Commit messages

Предпочтительный стиль:

```text
feat: add project doctor
fix: preserve project state during workflow update
docs: clarify advanced spec mode
chore: bump workflow version
```

---

## Security

Не публикуй credentials, API keys, private tokens или реальные пользовательские секреты в issue/PR.

Для потенциальных security problems см. `SECURITY.md`.
