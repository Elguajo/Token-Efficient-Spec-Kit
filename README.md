<div align="center">

# Token-Efficient Spec Kit

### Универсальный workflow для разработки с AI-агентами

**Ты описываешь, что хочешь получить. Агент сам выбирает стек, проектирует архитектуру, разбивает работу на этапы и реализует проект небольшими проверяемыми шагами.**

`Цель → Спецификация → Архитектура → Задачи → Код → Проверка`

[English](README_EN.md) · [Руководство](docs/USAGE_GUIDE.md) · [Как работает workflow](docs/WORKFLOW.md) · [Интеграции](integrations/README.md)

</div>

---

## Что это такое

**Token-Efficient Spec Kit** — это компактный набор правил, prompts и документации для repository-aware AI coding agents.

Главная идея очень простая:

> **Пользователь отвечает за желаемый результат. AI-агент отвечает за инженерные решения.**

Вместо такого диалога:

```text
— React или Vue?
— PostgreSQL или MongoDB?
— REST или GraphQL?
— Vercel или AWS?
— Как разбить проект на этапы?
```

ты можешь написать:

```text
Хочу приложение, где дизайнеры смогут продавать digital assets.
```

А агент самостоятельно:

1. поймёт продукт и пользователей;
2. определит, что действительно нужно уточнить;
3. выберет рекомендуемый стек;
4. спроектирует архитектуру и данные;
5. оценит сложность и риски;
6. создаст roadmap;
7. начнёт разработку небольшими задачами;
8. проверит результат тестами и quality gates.

Если решение можно профессионально принять без тебя — агент **не должен перекладывать этот выбор на пользователя**.

---

# Быстрый старт — 30 секунд

### 1. Клонируй шаблон

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
```

### 2. Открой проект в своём AI coding agent

Подойдут repository-aware агенты, способные читать и изменять файлы проекта.

### 3. Запусти

```text
prompts/START_NEW_PROJECT.md
```

Замени только:

```text
<WHAT_I_WANT>
```

на свою идею.

Например:

```text
Хочу desktop-приложение для Windows и macOS,
которое автоматически сортирует мои 3D-модели,
создаёт превью и позволяет искать их по тегам.
```

**Всё.**

`START_NEW_PROJECT.md` дальше сам проверит tooling, подготовит проектную документацию, выберет архитектуру и начнёт первый этап разработки, если нет реального блокера.

> Отдельно запускать setup обычно не нужно. При необходимости стартовый prompt сам вызывает `SETUP_RECOMMENDED_TOOLING.md`.

📖 Более подробная инструкция: **[docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md)**

---

## Что произойдёт автоматически

```text
ТВОЯ ИДЕЯ
   │
   ▼
Проверка инструментов
   │
   ▼
Понимание продукта
   │
   ▼
PROJECT_BRIEF.md
   │
   ▼
Выбор стека и архитектуры
   │
   ▼
ARCHITECTURE.md
   │
   ▼
ROADMAP.md + phase specs
   │
   ▼
1–3 связанные задачи
   │
   ▼
Реализация
   │
   ▼
Тесты / Review / QA
   │
   ▼
Сверка: spec ↔ code ↔ tests
   │
   ▼
Следующий этап
```

Тебе не нужно каждый раз заново объяснять проект: его устойчивый контекст хранится в компактных canonical-файлах внутри репозитория.

---

## Почему Token-Efficient

Большие AI-проекты часто начинают тратить контекст на повторное чтение:

```text
всей истории чата
+ всех завершённых этапов
+ всех решений
+ огромного master spec
+ повторяющихся research notes
+ дублирующих PRD
```

Здесь обычная coding-сессия читает только то, что действительно нужно сейчас:

```text
Constitution
+ Project Brief
+ Architecture
+ Engineering Rules
+ Current Phase
+ нужный ADR — если он относится к задаче
+ релевантный код и тесты
```

### Два основных правила

> **Один факт → одно canonical место хранения.**

> **Один implementation run → обычно 1–3 связанные задачи.**

Это уменьшает лишний контекст и помогает агенту не терять принятые архитектурные решения по мере роста проекта.

---

## Как распределена ответственность

### Ты определяешь

- какой результат нужен;
- обязательные функции и ограничения;
- бизнес-решения, которые нельзя вывести технически;
- субъективные предпочтения, если они для тебя важны.

### AI-агент определяет

- стек;
- архитектуру;
- database/storage/auth подход;
- структуру проекта;
- API и data model;
- roadmap;
- порядок реализации;
- testing strategy;
- технические оптимизации;
- разумные UX/engineering решения, которые не были заданы явно.

### Агент спрашивает тебя только когда

- существуют два существенно разных продукта под одним описанием;
- решение необратимо или разрушительно;
- нужны OAuth/login/credentials;
- стоимость радикально меняет архитектуру;
- нужен юридический или бизнес-выбор;
- невозможно безопасно продолжить без уточнения.

---

# Recommended AI Engineering Profile

Для production-oriented проектов используется следующий набор:

```text
Token-Efficient Spec Kit
        │
        ├── GitHub Spec Kit
        ├── Superpowers
        ├── Spec Kit ↔ Superpowers Bridge
        ├── gstack
        └── Context7
```

Важно: инструменты **не должны выполнять одну и ту же работу параллельно**.

| Инструмент | Ответственность |
|---|---|
| **Token-Efficient Spec Kit** | Контекст, правила проекта, архитектурная дисциплина и routing workflow |
| **GitHub Spec Kit** | **WHAT** — specification, plan, tasks, анализ и convergence |
| **Superpowers** | **HOW** — TDD, systematic debugging и implementation discipline |
| **Spec Kit ↔ Superpowers Bridge** | Разделяет WHAT и HOW, чтобы planning не дублировался |
| **gstack** | Challenge layer: engineering/design/code review, browser QA, release checks |
| **Context7** | Свежая документация библиотек и API по необходимости |

Подробнее о ролях и установке: **[integrations/README.md](integrations/README.md)**

---

## Workflow адаптируется под размер проекта

Не каждый проект должен генерировать десятки документов.

| Уровень | Для чего | Процесс |
|---|---|---|
| **S — Small** | landing page, CLI, automation, небольшая feature | `Brief → Plan → Tasks → Implement → Verify` |
| **M — Medium** | SaaS MVP, ecommerce, plugin + backend, internal tool | `Brief → Architecture → Roadmap → Phases → Implement → Converge` |
| **L — Large / High-risk** | marketplace, payments, sensitive data, multi-role system | `Brief → Architecture → Risk → Roadmap → Small Specs → Quality Gates → Converge` |

**High-risk не означает автоматически сложную архитектуру.** Он означает более строгую проверку.

---

# Как пользоваться после первого запуска

Обычно тебе нужны всего несколько prompts:

| Ситуация | Что запускать |
|---|---|
| 🆕 Новый проект | [`prompts/START_NEW_PROJECT.md`](prompts/START_NEW_PROJECT.md) |
| ▶️ Продолжить работу | [`prompts/CONTINUE_PROJECT.md`](prompts/CONTINUE_PROJECT.md) |
| ✅ Проверить и закрыть текущий этап | [`prompts/REVIEW_CURRENT_PHASE.md`](prompts/REVIEW_CURRENT_PHASE.md) |
| 🔄 Изменить требования | [`prompts/CHANGE_REQUEST.md`](prompts/CHANGE_REQUEST.md) |
| 🐛 Исправить баг | [`prompts/BUG_FIX.md`](prompts/BUG_FIX.md) |
| 🛠 Настроить инструменты вручную | [`prompts/SETUP_RECOMMENDED_TOOLING.md`](prompts/SETUP_RECOMMENDED_TOOLING.md) |

### Например, на следующий день

Не нужно снова писать:

```text
Мы вчера делали приложение...
Стек был такой...
Мы закончили вот это...
Следующим хотели сделать...
```

Просто запускаешь:

```text
prompts/CONTINUE_PROJECT.md
```

Агент сам читает только текущий минимальный контекст и продолжает незавершённый phase.

---

## Как агент выбирает технологии

Он должен рекомендовать **один основной вариант**, а не отправлять пользователю меню из десяти стеков.

Для важных решений используются примерно такие критерии:

| Критерий | Базовый приоритет |
|---|---:|
| Соответствие требованиям | 25% |
| Простота | 20% |
| Поддерживаемость | 15% |
| Зрелость экосистемы | 10% |
| Безопасность | 10% |
| Операционная сложность | 10% |
| Стоимость | 5% |
| Скорость разработки | 5% |

Веса меняются в зависимости от проекта.

- для prototype важнее скорость и обратимость решений;
- для финансовых или чувствительных систем — security и data integrity;
- для небольшого проекта не нужна архитектура уровня enterprise.

> **Цель — не самый модный стек, а самое простое зрелое решение, которое правильно решает реальную задачу.**

---

## Creative autonomy

Агенту разрешено проявлять инициативу, если пользователь не зафиксировал деталь.

Он может самостоятельно предложить или улучшить:

- UX flows;
- information architecture;
- структуру функций;
- visual patterns;
- API ergonomics;
- data models;
- onboarding;
- loading / empty / error states;
- developer experience;
- небольшие high-value улучшения.

Но он не имеет права незаметно менять явные требования пользователя.

---

## Quality Gates

Код не считается готовым только потому, что агент его написал.

В зависимости от проекта проверяются:

```text
lint
+ typecheck
+ tests
+ build
+ security negative tests
+ browser / e2e QA
+ acceptance criteria
```

Для auth, payments, permissions, private files, webhooks и destructive migrations негативные сценарии обязательны там, где они релевантны.

---

## Структура репозитория

<details>
<summary><strong>Показать структуру</strong></summary>

<br />

```text
.
├── .specify/
│   └── memory/
│       └── constitution.md
│
├── docs/
│   ├── README.md
│   ├── USAGE_GUIDE.md
│   ├── WORKFLOW.md
│   │
│   ├── system/
│   │   ├── OPERATING_MODEL.md
│   │   ├── DECISION_FRAMEWORK.md
│   │   ├── ENGINEERING_RULES.md
│   │   ├── TOKEN_EFFICIENCY.md
│   │   └── CREATIVE_AUTONOMY.md
│   │
│   ├── project/
│   │   ├── PROJECT_BRIEF.md
│   │   ├── ARCHITECTURE.md
│   │   ├── ROADMAP.md
│   │   └── TOOLING_STATUS.md
│   │
│   ├── phases/
│   └── decisions/
│
├── integrations/
│   ├── README.md
│   ├── PROFILES.md
│   ├── TOOLING_POLICY.md
│   ├── SPEC_KIT.md
│   ├── SUPERPOWERS.md
│   ├── GSTACK.md
│   └── CONTEXT7.md
│
├── templates/
│   ├── PROJECT_BRIEF.template.md
│   ├── ARCHITECTURE.template.md
│   ├── ROADMAP.template.md
│   ├── PHASE.template.md
│   └── ADR.template.md
│
├── prompts/
│   ├── SETUP_RECOMMENDED_TOOLING.md
│   ├── START_NEW_PROJECT.md
│   ├── CONTINUE_PROJECT.md
│   ├── REVIEW_CURRENT_PHASE.md
│   ├── CHANGE_REQUEST.md
│   └── BUG_FIX.md
│
├── AGENTS.md
├── README.md
└── README_EN.md
```

</details>

---

## Документация

| Документ | Для чего |
|---|---|
| **[Руководство по использованию](docs/USAGE_GUIDE.md)** | Пошагово: как реально работать с системой |
| **[Workflow](docs/WORKFLOW.md)** | Что происходит внутри на каждом этапе |
| **[Навигация по документации](docs/README.md)** | Карта всех документов проекта |
| **[Integrations](integrations/README.md)** | Spec Kit, Superpowers, gstack и Context7 |
| **[Constitution](.specify/memory/constitution.md)** | Неизменяемые инженерные правила |

---

## 10 принципов

1. **Outcome first** — пользователь описывает результат, а не стек.
2. **Senior autonomy** — агент принимает обычные технические решения сам.
3. **Ask only blockers** — разработка не превращается в анкету.
4. **Simplicity first** — никакой преждевременной distributed architecture.
5. **Current information** — быстро меняющиеся API проверяются по актуальным docs.
6. **Small context** — только контекст текущей задачи.
7. **Small batches** — обычно 1–3 связанные задачи за один run.
8. **Canonical docs** — один факт хранится в одном основном месте.
9. **Security by design** — server authority, least privilege, negative tests.
10. **Verification before completion** — `spec ↔ code ↔ tests` должны сходиться.

---

## Чем этот проект не является

Это не:

- фиксированный technology stack;
- генератор огромных PRD;
- multi-agent role-play framework;
- повод документировать каждое мелкое решение;
- система, где пять AI-frameworks одновременно пытаются руководить проектом;
- гарантия качества AI-generated code без проверки.

Это **компактный orchestration layer**, который помогает AI coding agents работать последовательно, автономно и с управляемым контекстом.

---

<div align="center">

### Опиши результат. Остальное — инженерная работа агента.

**[Начать новый проект →](prompts/START_NEW_PROJECT.md)**

<br />

Built with ♥ by [Elguajo](https://github.com/Elguajo)

</div>
