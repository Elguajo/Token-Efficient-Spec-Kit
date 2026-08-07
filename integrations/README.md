# Интеграции

Этот каталог описывает дополнительные инструменты, которые усиливают Token-Efficient Spec Kit, не превращая workflow в набор конкурирующих фреймворков.

## Recommended profile

По умолчанию рекомендуется:

```text
Token-Efficient Spec Kit
+ GitHub Spec Kit
+ Superpowers
+ Superpowers Implementation Bridge
+ gstack
+ Context7
```

Роли разделены жёстко:

```text
Token-Efficient Spec Kit
→ правила проекта, контекст, архитектурная дисциплина

GitHub Spec Kit
→ WHAT: spec, clarify, plan, tasks, analyze, converge

Superpowers
→ HOW: TDD, systematic debugging, execution discipline, verification

Superpowers Implementation Bridge
→ не даёт Spec Kit и Superpowers создавать два параллельных planning workflow

gstack
→ challenge/review layer: engineering review, design review, code review, browser QA, release checks

Context7
→ актуальная документация библиотек/API по требованию
```

## Главный принцип

Ни один дополнительный инструмент не становится вторым source of truth.

Canonical project intent остаётся в:

```text
.specify/memory/constitution.md
docs/project/PROJECT_BRIEF.md
docs/project/ARCHITECTURE.md
docs/project/ROADMAP.md
docs/phases/
```

## Установка

Для установки Recommended profile используй:

```text
prompts/SETUP_RECOMMENDED_TOOLING.md
```

AI-agent должен сначала определить текущий coding harness, затем сверить актуальные официальные инструкции каждого инструмента и только после этого выполнять установку.

Это сделано намеренно: способы установки Claude Code, Codex, Cursor и других harnesses меняются быстрее, чем сам шаблон.
