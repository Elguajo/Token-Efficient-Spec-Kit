<div align="center">

<sub>AI ENGINEERING WORKFLOW</sub>

# Token-Efficient Spec Kit

**От идеи до проверенного результата.**

[Начать новый проект](prompts/START_NEW_PROJECT.md) · [Как пользоваться](docs/USAGE_GUIDE.md) · [Visual Guide](docs/VISUAL_GUIDE.md) · [English](README_EN.md)

<sub>**v0.8.2** · [Workflow](docs/WORKFLOW.md) · [Maintenance](docs/MAINTENANCE.md) · [Changelog](CHANGELOG.md)</sub>

</div>

---

## Что это даёт

Token-Efficient Spec Kit — workflow для repository-aware AI-агентов: Codex,
Claude Code, Cursor и совместимых инструментов. Он хранит решения в репозитории,
а не в памяти одного чата, поэтому новый AI-сеанс может продолжить работу без
повторного объяснения проекта.

Тебе не нужно заранее решать:

```text
Какой framework или database использовать?
Как разбить работу на этапы?
Что проверить перед релизом?
Какой prompt отправить AI следующим?
```

Ты отвечаешь за желаемый результат и реальные ограничения. AI отвечает за обычные
инженерные решения, план, реализацию, проверку и навигацию по проекту.

---

# Старт нового проекта

## 1. Подготовь копию шаблона

```bash
git clone https://github.com/Elguajo/Token-Efficient-Spec-Kit.git my-project
cd my-project
rm -rf .git && git init
```

Последняя строка нужна только для свежей копии шаблона: она убирает связь с этим
репозиторием, чтобы случайно не отправить свой проект сюда. Если добавляешь
workflow в существующий repository, смотри [Usage Guide](docs/USAGE_GUIDE.md).

## 2. Открой папку в AI coding agent

Агент должен уметь читать и изменять файлы проекта.

## 3. Отправь одно сообщение с идеей

Не открывай prompt вручную и не заменяй плейсхолдеры. В чате с AI-agent отправь,
например:

```text
Запусти prompts/START_NEW_PROJECT.md.
Хочу desktop-приложение для Windows и macOS, которое сортирует мои 3D-ассеты,
создаёт previews и позволяет искать их по тегам.
```

Достаточно описать желаемый результат. Не нужно заранее выбирать stack, framework,
database или хостинг.

## Что произойдёт дальше

1. AI обычно предложит три содержательно разные product-направления.
2. Он объяснит рекомендацию и продолжит с ней без отдельного выбора.
3. Он попросит тебя выбрать вариант только при существенном business, budget,
   safety, compliance или другом необратимом trade-off.
4. AI создаст `PROJECT_BRIEF.md`, `ARCHITECTURE.md`, `ROADMAP.md` и фазы.
5. Подключит только полезный tooling и возьмёт первые 1–3 связанные задачи.
6. В конце проверит результат и вернёт готовый `NEXT SESSION PROMPT`.

### Путь от идеи до следующей сессии

```text
┌───────────────────────────────┐
│           ТВОЯ ИДЕЯ           │
└───────────────┬───────────────┘
                ▼
      Product Directions
                ↓
      Recommended Direction
                ↓
 Project Brief → Architecture → Roadmap
                ↓
       Scoped Tooling Bootstrap
                ↓
┌───────────────────────────────┐
│        CURRENT PHASE          │
│       1–3 связанные задачи    │
└───────────────┬───────────────┘
                ▼
      Implement → Verify
                ↓
       NEXT SESSION PROMPT
                │
                └────► новая AI-сессия ────► Current Phase
```

[Все визуальные схемы →](docs/VISUAL_GUIDE.md)

---

# Продолжение работы

После каждой meaningful coding/review session AI обязан синхронно обновить:

```text
ROADMAP current-phase marker
          +
NEXT_SESSION.md
          +
NEXT SESSION PROMPT
```

### Session Handoff

```text
       IMPLEMENT / REVIEW
              │
              ▼
       VERIFY / CONVERGE
              │
              ▼
       ┌──────────────┐
       │   STATUS?    │
       └───┬────┬─────┘
           │    │
    ┌──────┘    └──────────────┐
    ▼                          ▼
IN PROGRESS              PHASE COMPLETE
    │                          │
    ▼                          ▼
same phase                 next phase
    │                          │
    └──────────┬───────────────┘
               ▼
       NEXT SESSION PROMPT
               │
               ▼
          FRESH SESSION
```

Если завершён весь roadmap, статус становится `PROJECT COMPLETE`, а следующий шаг
ведёт в release/audit или future change request.

В большинстве случаев просто скопируй последний prompt в новую сессию. Не нужно
самому решать, закончена ли фаза, пора ли запускать QA или какой этап открывать.

| Ситуация | Что отправить AI |
|---|---|
| Новый проект | Сообщение из шага 3 выше |
| Продолжить работу | Последний **NEXT SESSION PROMPT** |
| Не понимаю состояние проекта | [`PROJECT_DOCTOR.md`](prompts/PROJECT_DOCTOR.md) |
| Изменить требования | [`CHANGE_REQUEST.md`](prompts/CHANGE_REQUEST.md) |
| Исправить ошибку | [`BUG_FIX.md`](prompts/BUG_FIX.md) |
| Проверить и закрыть фазу | [`REVIEW_CURRENT_PHASE.md`](prompts/REVIEW_CURRENT_PHASE.md) |
| Потерял следующий шаг | [`GENERATE_NEXT_SESSION_PROMPT.md`](prompts/GENERATE_NEXT_SESSION_PROMPT.md) |
| Нужна глубокая formal-spec для сложной фазы | [`ENABLE_ADVANCED_SPEC_MODE.md`](prompts/ENABLE_ADVANCED_SPEC_MODE.md) |

---

# Для опытных пользователей

AI маршрутизирует инструменты, а не запускает всё подряд.

### Core architecture

```text
                         TOKEN-EFFICIENT SPEC KIT
                              ORCHESTRATOR
                                   │
           ┌───────────────────────┼───────────────────────┐
           │                       │                       │
           ▼                       ▼                       ▼
        Semble                  Serena                    RTK
   find relevant code       symbols / references      compact output
           │                  safe refactoring            │
           └──────────────┬────────┘                       │
                          ▼                                │
                    Superpowers                            │
                 implementation / TDD                      │
                          │                                │
                          └──────────────┬─────────────────┘
                                         ▼
                                  tests / evidence
                                         │
                                         ▼
                                       gstack
                                         │
                                         ▼
                                     convergence
                                         │
                                         ▼
                                NEXT SESSION PROMPT
```

`Context7` подключается сбоку только когда нужны свежие API/library docs. GitHub
Spec Kit не входит в обычный execution path и используется только как optional
Advanced Spec Mode для отдельных сложных фаз.

### Как выбирается инструмент

| Задача | Предпочтительный инструмент |
|---|---|
| «Где реализована логика X?» / незнакомая область кода | **Semble** |
| Известный symbol, references, diagnostics или безопасный rename | **Serena** |
| Маленькая правка в известном файле | native tools агента |
| Tests, build, git или шумный terminal output | **RTK** |
| Нужны свежие API/library docs | **Context7** |
| Implementation / TDD / systematic debugging | **Superpowers** |
| Review / browser QA / release checks | **gstack** |

```text
One question → one cheapest adequate tool.
```

Semble заканчивает broad discovery, как только найдена нужная область. Serena
подключается только для symbol-level задачи. Одну и ту же область не нужно заново
искать Semble, Serena и text search без причины.

Project Brief, Architecture, Roadmap и phase-файлы остаются долговременной памятью
проекта; внешние инструменты не создают второй источник правды.

[Полная карта tool routing →](docs/VISUAL_GUIDE.md#3-tool-router--какой-инструмент-выбрать)

---

# Инструменты: что нужно знать пользователю

AI не должен заставлять тебя вручную настраивать обычные инструменты. Сначала он
понимает продукт и tier, затем подключает только полезное. Недоступный инструмент
не блокирует работу: агент использует безопасный fallback.

```text
Superpowers  → реализация, TDD и отладка
Semble       → найти логику по смыслу в незнакомом коде
Serena       → symbols, references и безопасный рефакторинг
RTK          → компактный terminal/test/build/git output
gstack       → review, browser QA и release checks
Context7     → свежая документация API и libraries
```

> Канонический профиль: [`integrations/PROFILES.md`](integrations/PROFILES.md).
> Superpowers и Context7 могут быть полезны сразу; остальные инструменты обычно
> подключаются после появления кода и подтверждённой необходимости.

AI сохраняет установленные, отложенные и пропущенные инструменты в
`docs/project/TOOLING_STATUS.md`. Твоё участие обычно нужно только для login/OAuth,
отсутствующего system runtime или глобальной настройки, которая затрагивает другие
проекты.

GitHub Spec Kit не является обязательным: он включается только как
[Advanced Spec Mode](integrations/SPEC_KIT.md) для сложных фаз.

---

# Где искать подробности

| Нужно… | Открыть |
|---|---|
| Пошаговое руководство со всеми сценариями | [Usage Guide](docs/USAGE_GUIDE.md) |
| Быстро понять систему по схемам | [Visual Guide](docs/VISUAL_GUIDE.md) |
| Понять внутреннюю модель workflow | [End-to-End Workflow](docs/WORKFLOW.md) |
| Посмотреть следующий шаг текущего проекта | [NEXT_SESSION.md](docs/project/NEXT_SESSION.md) |
| Настроить или понять интеграции | [Integrations](integrations/README.md) |
| Запустить doctor, self-audit или update | [Maintenance](docs/MAINTENANCE.md) |
| Посмотреть историю изменений | [Changelog](CHANGELOG.md) |

## Проверка целостности workflow

```bash
python3 tools/audit.py
```

Проверяет ссылки, версии, handoff, tooling profile и границы между framework и
проектом. Та же проверка запускается в CI.

<div align="center">

### Не обязательно знать, как это программировать. Достаточно ясно описать результат.

**[Начать новый проект →](prompts/START_NEW_PROJECT.md)**

MIT — см. [LICENSE](LICENSE) · Built with ♥ by [Elguajo](https://github.com/Elguajo)

</div>
