# Новый проект

Этот repository уже содержит Token-Efficient Spec Kit: правила для AI-agent,
шаблоны проектного состояния и prompts для ведения работы.

## Начать

1. Открой эту папку в repository-aware AI coding agent.
2. Одним сообщением опиши желаемый продукт и попроси запустить
   `prompts/START_NEW_PROJECT.md`.

Например:

```text
Запусти prompts/START_NEW_PROJECT.md.
Хочу сервис для подготовки коммерческих предложений для архитекторов.
```

Не нужно заранее выбирать stack, database или хостинг. AI определит обычные
инженерные решения, создаст project state и вернёт готовый prompt для следующей
сессии.

## Состав workflow

- `AGENTS.md` — обязательные правила для AI-agent.
- `prompts/` — входные точки для нового проекта, продолжения, review и fixes.
- `docs/project/` — состояние конкретного продукта; после старта оно принадлежит
  только этому проекту.
- `docs/system/`, `integrations/`, `templates/` — переносимый workflow.

Версия установленного workflow находится в
`.token-efficient-spec-kit/VERSION`. Подробности безопасного обновления — в
`prompts/UPDATE_WORKFLOW.md`.
