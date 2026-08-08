# Visual Guide

Короткая визуальная карта Token-Efficient Spec Kit.

Эти схемы объясняют workflow без необходимости читать всю техническую документацию.
Для точных правил источником истины остаются [`WORKFLOW.md`](WORKFLOW.md),
[`integrations/PROFILES.md`](../integrations/PROFILES.md) и system docs.

---

# 1. Путь пользователя

```text
┌───────────────────────────────┐
│         ТВОЯ ИДЕЯ             │
│  «Хочу приложение, которое…»  │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      START_NEW_PROJECT        │
│ AI читает правила repository │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      PRODUCT DIRECTION        │
│ варианты → рекомендация       │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ BRIEF → ARCHITECTURE → ROADMAP│
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│        CURRENT PHASE          │
│       1–3 связанные задачи    │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ IMPLEMENT → VERIFY → CONVERGE │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      NEXT SESSION PROMPT      │
└───────────────┬───────────────┘
                │
                └────► новая AI-сессия ────► CURRENT PHASE
```

Для пользователя основной цикл после первого запуска обычно сводится к:

```text
START_NEW_PROJECT
        ↓
NEXT SESSION PROMPT
        ↓
NEXT SESSION PROMPT
        ↓
...
        ↓
PROJECT COMPLETE
```

---

# 2. Core architecture

```text
                         TOKEN-EFFICIENT SPEC KIT
                              ORCHESTRATOR
                                   │
           ┌───────────────────────┼───────────────────────┐
           │                       │                       │
           ▼                       ▼                       ▼
        Semble                  Serena                    RTK
   intent-based search      symbol semantics         compact output
   «где логика X?»         refs / rename / edit      tests/build/git
           │                       │                       │
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
                                   review / browser QA
                                         │
                                         ▼
                                     convergence
                                         │
                                         ▼
                                NEXT SESSION PROMPT
```

Context7 находится сбоку от execution path и вызывается только когда нужны свежие
API/library docs:

```text
implementation needs current external docs
                 │
                 ▼
              Context7
                 │
                 ▼
        decision-relevant docs only
```

GitHub Spec Kit не входит в обычный execution path. Это optional Advanced Spec
Mode для отдельных сложных фаз.

---

# 3. Tool Router — какой инструмент выбрать

```text
                         НУЖЕН CONTEXT / ACTION
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │ Что именно неизвестно? │
                    └────────────┬────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼
 «Где логика X?»        «Кто вызывает X?»       «Команда слишком
 незнакомая область     symbol/refactor          много выводит?»
          │                      │                      │
          ▼                      ▼                      ▼
       SEMBLE                  SERENA                   RTK
          │                      │                      │
          └──────────────┬───────┘                      │
                         ▼                              │
                нужный code context                    │
                         │                              │
                         ▼                              │
                 SUPERPOWERS / NATIVE ◄────────────────┘
                         │
                         ▼
                    IMPLEMENTATION
```

Правило:

```text
One question → one cheapest adequate tool.
```

Не нужно запускать Semble, Serena, RTK, gstack и Context7 только потому, что они
установлены.

---

# 4. Semble + Serena без конфликта

```text
Вопрос по смыслу
«Где проверяется entitlement после webhook?»
                    │
                    ▼
                  SEMBLE
        relevant files / snippets / symbols
                    │
                    ▼
        exact area / symbol уже известен
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
  простая локальная      нужны references,
       правка            diagnostics/refactor
          │                   │
          ▼                   ▼
    NATIVE EDIT              SERENA
                              │
                              ▼
                       semantic edit/rename
```

И наоборот:

```text
«Кто вызывает refreshSession?»
            │
            ▼
          SERENA

Semble сначала не нужен: вопрос уже symbol-shaped.
```

Главное правило — **no-double-discovery**: если один инструмент уже нашёл точный
контекст, второй не должен повторять широкий поиск без причины.

---

# 5. Session Handoff

```text
┌──────────────────────────────┐
│     IMPLEMENTATION SESSION   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      VERIFY / CONVERGE       │
└──────────────┬───────────────┘
               │
               ▼
      ┌───────────────────┐
      │   CURRENT STATE?  │
      └───────┬───────────┘
              │
      ┌───────┼────────────────────┐
      │       │                    │
      ▼       ▼                    ▼
IN PROGRESS  PHASE COMPLETE   PROJECT COMPLETE
      │       │                    │
      ▼       ▼                    ▼
same phase   next phase       release / audit /
 next work    prompt           future change
      │       │                    │
      └───────┴─────────┬──────────┘
                        ▼
              ROADMAP marker update
                        +
                NEXT_SESSION.md
                        +
              NEXT SESSION PROMPT
                        │
                        ▼
                  FRESH SESSION
```

Пользователь не обязан сам определять следующий инженерный шаг.

---

# 6. Context budget

```text
┌──────────────────────────────────────────────────────┐
│              NORMAL SESSION CONTEXT                  │
│                                                      │
│  canonical project state                             │
│  + current phase                                     │
│  + relevant ADR only if needed                       │
│  + targeted source/tests                             │
└──────────────────────────────────────────────────────┘
                         │
                         ▼
                smallest useful context
```

По умолчанию не грузим:

```text
all old chats
all completed phases
all ADRs
the whole repository
raw research dumps
all installed tool instructions
```

Token-efficiency layers:

```text
Project/docs context         → Token-Efficient Spec Kit
Intent-based code discovery  → Semble
Symbol semantics/refactoring → Serena
Shell/tool output            → RTK
Fresh external docs          → Context7 on demand
```

---

# 7. Complexity routing

```text
                         PROJECT
                            │
                            ▼
                 ┌────────────────────┐
                 │ Complexity / Risk? │
                 └──────┬─────┬───────┘
                        │     │
              ┌─────────┘     └──────────┐
              ▼                          ▼
          S / SMALL                   M / MEDIUM
              │                          │
              ▼                          ▼
 Brief → Tasks → Verify       Brief → Architecture
                              → Roadmap → Phases
                                       │
                                       ▼
                                  L / HIGH-RISK
                                       │
                                       ▼
                              smaller phases
                              stronger evidence
                              negative tests
                              selective reviews
                              optional Advanced
                              Spec Mode if useful
```

High Risk означает больше доказательств качества, а не автоматически больше
frameworks и инфраструктуры.

---

# 8. Maintenance router

```text
                 «Что мне сейчас нужно?»
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
 «Не понимаю        «Framework         «Хочу обновить
 состояние»          противоречит?»      workflow»
        │                 │                 │
        ▼                 ▼                 ▼
 PROJECT_DOCTOR      AUDIT_WORKFLOW     UPDATE_WORKFLOW
        │                 │                 │
        ▼                 ▼                 ▼
 plain-language      consistency        safe framework
 project status      findings           update + audit
```

Для обслуживания используй [`MAINTENANCE.md`](MAINTENANCE.md).

---

# 9. Источник истины

```text
                    REPOSITORY
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼
 PROJECT_BRIEF     ARCHITECTURE       ROADMAP
                                          │
                                          ▼
                                     CURRENT PHASE
                                          │
                                          ▼
                                      code / tests
```

External tools помогают работать с этим состоянием, но не создают параллельный
Project Brief, Architecture или Roadmap.

---

## Куда дальше

- [Usage Guide](USAGE_GUIDE.md) — пошаговое использование.
- [End-to-End Workflow](WORKFLOW.md) — точная техническая модель.
- [Integrations](../integrations/README.md) — роли и настройка инструментов.
- [Maintenance](MAINTENANCE.md) — Doctor, audit и safe updates.
