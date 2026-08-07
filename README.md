<div align="center">

# Token-Efficient Spec Kit

### Универсальный AI engineering workflow: меньше контекста, меньше токенов, сильнее результат.

**Опиши, что хочешь получить. Пусть AI-агент сам выберет стек, архитектуру, roadmap и лучший путь реализации.**

`Цель → Решения → Спеки → Маленькие задачи → Код → Проверка`

[English version](README_EN.md)

</div>

---

## Что это

**Token-Efficient Spec Kit** — лёгкий engineering layer для repository-aware AI coding agents.

Вместо того чтобы каждый раз объяснять агенту весь проект или самому выбирать framework, database, auth, hosting и десятки других технических решений, ты задаёшь **желаемый результат**.

Например:

```text
Хочу приложение, где дизайнеры смогут продавать digital assets.
```

Дальше агент должен профессионально определить сам:

- тип продукта;
- пользователей и ключевые сценарии;
- что можно разумно предположить, а что действительно требует вопроса;
- рекомендуемый стек;
- архитектуру и data model;
- security boundaries;
- сложность и риск проекта;
- roadmap;
- testing/deployment strategy;
- следующие 1–3 задачи для реализации.

> **Пользователь задаёт результат. Агент принимает инженерные решения. Спеки сохраняют намерение. Маленький контекст экономит токены. Проверка сохраняет качество.**

---

## Главный workflow

```text
                    ┌──────────────────────┐
                    │   ЖЕЛАЕМЫЙ РЕЗУЛЬТАТ │
                    │    «Хочу сделать…»   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      UNDERSTAND      │
                    │ users · jobs · scope │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   CLASSIFY & ASSESS  │
                    │ type · risk · size   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   SENIOR DECISIONS   │
                    │ stack · architecture │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       ROADMAP        │
                    │ verifiable phases   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    CURRENT PHASE     │
                    │  1–3 cohesive tasks │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      IMPLEMENT       │
                    │ code · migrate · test│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       CONVERGE       │
                    │ spec ↔ code ↔ tests │
                    └──────────┬───────────┘
                               │
                               └──────► следующий этап
```

---

## Почему это экономит токены

Обычная рабочая сессия агента читает только:

```text
constitution
+ project brief
+ compact architecture
+ engineering rules
+ current phase
+ relevant ADR — только если нужен
+ relevant code/tests
```

И **не перечитывает по умолчанию**:

```text
все завершённые phases
+ все ADR
+ всю историю чата
+ giant master specs
+ repeated research dumps
+ duplicate PRDs
```

Основное правило:

> **Один факт — одно canonical место хранения. Один run — обычно 1–3 связанные задачи.**

---

## Senior autonomy

AI-agent не должен перекладывать обычные engineering decisions обратно на пользователя.

Он не должен спрашивать:

```text
React или Vue?
Postgres или MongoDB?
Vercel или AWS?
REST или GraphQL?
```

если это можно профессионально решить из требований проекта.

Вместо этого агент:

1. понимает задачу;
2. проверяет текущий repository state;
3. при необходимости сверяет актуальную официальную документацию;
4. рассматривает реальные альтернативы;
5. выбирает **один рекомендуемый вариант**;
6. фиксирует решение только если оно действительно важно для будущей разработки.

Вопрос пользователю нужен только если неизвестный параметр существенно меняет продукт, стоимость, compliance, security или требует необратимого действия.

---

## Creative autonomy

Агенту разрешено проявлять инициативу там, где пользователь не зафиксировал детали.

Он может самостоятельно предложить и выбрать:

- UX flows;
- information architecture;
- feature organization;
- visual patterns;
- API ergonomics;
- data models;
- onboarding;
- loading / empty / error states;
- developer tooling;
- небольшие high-value improvements.

Но креативность не даёт права незаметно менять явные требования пользователя.

---

# Recommended AI Engineering Stack

Для большинства серьёзных проектов используется **Recommended profile**:

```text
Token-Efficient Spec Kit
        │
        ├── GitHub Spec Kit
        ├── Superpowers
        ├── Superpowers Implementation Bridge
        ├── gstack
        └── Context7
```

Каждый инструмент имеет **отдельную ответственность**, чтобы они не создавали четыре параллельных workflow.

### GitHub Spec Kit — WHAT

Canonical source для:

```text
specification
clarification
plan
tasks
analysis
convergence
```

### Superpowers — HOW

Используется для:

```text
TDD
systematic debugging
implementation discipline
verification
```

### Superpowers Implementation Bridge

Разделяет ответственность:

```text
Spec Kit = WHAT
Superpowers = HOW
```

и предотвращает дублирование planning/execution layer.

### gstack — Challenge & QA Layer

Используется выборочно для:

```text
engineering review
design review
code review
investigation
browser QA
release / ship checks
cross-model challenge where available
```

По умолчанию **gstack не заменяет Spec Kit plan**.

### Context7 — Fresh Documentation

Подтягивает актуальную документацию библиотек/API тогда, когда она действительно нужна.

Он не должен вызываться на каждое тривиальное изменение.

Подробнее: [`integrations/README.md`](integrations/README.md)

---

## Tooling Profiles

### Minimal

```text
Token-Efficient Spec Kit
+ GitHub Spec Kit
```

Для небольших проектов и быстрых prototypes.

### Recommended — default

```text
Token-Efficient Spec Kit
+ GitHub Spec Kit
+ Superpowers
+ Superpowers Bridge
+ gstack
+ Context7
```

Для production-oriented разработки.

### Full / Experimental

Дополнительные review/orchestration/governance инструменты подключаются только после отдельного решения.

Больше инструментов ≠ автоматически выше качество. Overlapping frameworks быстро начинают тратить больше токенов, чем экономят.

---

## Adaptive process

Не каждому проекту нужен одинаковый уровень ceremony.

### S — Small

```text
Brief → Plan → Tasks → Implement → Verify
```

Landing pages, CLI, simple automations, small features.

### M — Medium

```text
Brief → Architecture → Roadmap → Phase Specs → Implement → Converge
```

SaaS MVP, ecommerce, plugin + backend, internal tools.

### L — Large / High-risk

```text
Brief
→ Architecture
→ Risk model
→ Roadmap
→ Small independent specs
→ Selective quality gates
→ Implementation batches
→ Converge
```

Marketplaces, multi-role systems, payments, sensitive data, critical migrations.

High Risk означает **больше проверок**, а не автоматически более сложную архитектуру.

---

## Структура

```text
.
├── .specify/
│   └── memory/
│       └── constitution.md
│
├── docs/
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

---

# Быстрый старт

## 1. Клонируй шаблон

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
```

## 2. Установи Recommended tooling

Открой AI coding agent в repository и дай ему содержимое:

```text
prompts/SETUP_RECOMMENDED_TOOLING.md
```

Setup-agent сам должен:

- определить текущий coding harness;
- сверить **актуальные upstream installation docs**;
- установить Spec Kit;
- установить Superpowers;
- подключить Spec Kit ↔ Superpowers bridge;
- установить gstack;
- настроить Context7;
- сохранить существующий Constitution;
- проверить отсутствие конфликтующих/duplicate skills;
- записать состояние в `docs/project/TOOLING_STATUS.md`.

Некоторые шаги могут потребовать только OAuth/login или установки отсутствующего system runtime — это единственные ситуации, где setup может остановиться и попросить пользователя вмешаться.

## 3. Запусти новый проект

Используй:

```text
prompts/START_NEW_PROJECT.md
```

Замени:

```text
<WHAT_I_WANT>
```

на описание желаемого результата.

Например:

```text
Хочу desktop-приложение для Windows и macOS,
которое автоматически организует мои CGI/3D assets,
создаёт previews и позволяет искать их по тегам.
```

## 4. Продолжай маленькими batches

Следующий run:

```text
prompts/CONTINUE_PROJECT.md
```

Проверка текущего phase:

```text
prompts/REVIEW_CURRENT_PHASE.md
```

Изменение требований:

```text
prompts/CHANGE_REQUEST.md
```

Bug fix:

```text
prompts/BUG_FIX.md
```

---

## Как выбираются технологии

Для важных технических решений агент оценивает примерно такие факторы:

| Критерий | Базовый вес |
|---|---:|
| Соответствие требованиям | 25% |
| Простота | 20% |
| Поддерживаемость | 15% |
| Экосистема / зрелость | 10% |
| Безопасность | 10% |
| Operational burden | 10% |
| Стоимость | 5% |
| Developer productivity | 5% |

Вес адаптируется под задачу.

Для prototype важнее скорость.

Для financial/sensitive system безопасность и data integrity доминируют.

Основной принцип:

> **Не самый модный стек. Самый простой зрелый стек, который правильно решает реальную задачу.**

---

## Quality gates

Код не считается готовым только потому, что агент его написал.

В зависимости от проекта нужны доказательства:

```text
lint
+ typecheck
+ tests
+ build
+ security negative tests
+ browser/e2e QA
+ acceptance criteria
```

Для auth, payments, permissions, private files, webhooks и destructive migrations negative tests обязательны там, где они релевантны.

---

## 10 принципов за минуту

1. **Outcome first** — пользователь описывает результат, не стек.
2. **Senior autonomy** — агент принимает обычные technical decisions сам.
3. **Ask only blockers** — не превращать разработку в анкету.
4. **Simplicity first** — никакой premature distributed architecture.
5. **Current information** — fast-changing APIs проверяются по свежим docs.
6. **Small context** — только контекст текущей задачи.
7. **Small batches** — обычно 1–3 связанные задачи за run.
8. **Canonical docs** — один факт, одно основное место.
9. **Security by design** — server authority, least privilege, negative tests.
10. **Verification before completion** — spec ↔ code ↔ tests должны сходиться.

---

## Чем этот проект не является

Это **не**:

- fixed technology stack;
- giant PRD generator;
- multi-agent role-play framework;
- повод документировать каждое мелкое решение;
- автоматическая гарантия качества AI-generated code;
- система, где пять AI-frameworks одновременно управляют проектом.

Это компактный operating layer, который даёт каждому инструменту чёткую роль и сохраняет project context управляемым.

---

<div align="center">

### Опиши результат. Держи контекст маленьким. Пусть агент занимается инженерией.

Начни с [`prompts/SETUP_RECOMMENDED_TOOLING.md`](prompts/SETUP_RECOMMENDED_TOOLING.md), затем [`prompts/START_NEW_PROJECT.md`](prompts/START_NEW_PROJECT.md).

<br />

Built with ♥ by [Elguajo](https://github.com/Elguajo)

</div>
