# Changelog

Все заметные изменения Token-Efficient Spec Kit фиксируются здесь.

Формат основан на принципах Keep a Changelog, версии следуют Semantic Versioning.

## [0.8.2] — 2026-08-08

### Changed

- новый проект теперь запускается разговорно: пользователь отправляет AI одну
  фразу с желаемым результатом и просьбой открыть `START_NEW_PROJECT.md`; ручной
  поиск и замена `<WHAT_I_WANT>` больше не требуются;
- перед инициализацией AI обычно формирует три содержательно разных product-направления,
  рекомендует одно и продолжает с ним автоматически. Выбор запрашивается только
  при существенном business, compliance, safety, budget или необратимом scope
  trade-off;
- `PROJECT_BRIEF.md` фиксирует рассмотренные направления, выбранный вариант и
  важные допущения.

### Migration

Ручная миграция не требуется. Для нового проекта отправь AI обычное описание идеи
вместе с просьбой запустить `prompts/START_NEW_PROJECT.md`.

## [0.8.1] — 2026-08-08

Компактный consistency-fix по результатам framework-аудита v0.8.0.

### Fixed

- повторные prose-варианты Default Read Set в engineering/workflow/change-request
  инструкциях заменены ссылками на канонический
  `docs/system/TOKEN_EFFICIENCY.md`;
- product handoff унифицирован как атомарная тройка: marker в `ROADMAP.md` +
  `NEXT_SESSION.md` + `NEXT SESSION PROMPT`;
- добавлены явные исключения: неинициализированный template и framework-only
  audit/update не создают и не изменяют `docs/project/*`, но всё равно возвращают
  готовый следующий prompt;
- README.md, README_EN.md, docs/README.md, docs/USAGE_GUIDE.md, docs/WORKFLOW.md и
  integrations/README.md синхронизированы с фактическим порядком Product Brief →
  Architecture → Roadmap → scoped tooling bootstrap; профиль везде включает Serena;
- tooling setup теперь явно поддерживает `INSTALL NOW` / `DEFERRED` /
  `SKIPPED FOR TIER`, а Semble, Serena, RTK и gstack не устанавливаются заранее в
  пустой codebase без подтверждённой пользы;
- Constitution, Project Doctor и product/setup entry points используют тот же
  атомарный handoff и полный Semble/Serena/RTK health profile;
- `tools/audit.py` теперь ловит prose-рестейты Default Read Set, неполные public
  profile listings, возврат к раннему/eager bootstrap, неполный handoff и потерю
  template/framework-only исключений.

### Migration

Обратная совместимость сохранена. Project-owned state и существующая `.serena/` не
изменяются; ручная миграция не требуется.

## [0.8.0] — 2026-08-08

Релиз консистентности. Правки по результатам внешнего аудита: устранены места, где
framework противоречил сам себе или требовал от агента невыполнимого действия.

### Added

- `tools/audit.py` — машинно-проверяемый self-audit: разрешение внутренних ссылок,
  консистентность версии, единственность Default Read Set, канонический указатель у
  каждого перечисления профиля, имена файлов фаз, ровно один маркер текущей фазы,
  границы framework/project, обязательные файлы;
- `.github/workflows/audit.yml` — тот же скрипт в CI на push и pull request;
- `LICENSE` (MIT) — до этого репозиторий формально нельзя было использовать и форкать;
- `.gitignore` — репозиторий клонируется корнем продукта, секреты и артефакты сборки
  больше не попадают в untracked-шум;
- статус-маркеры фаз (`[ ]` / `[>]` / `[x]`) в `templates/ROADMAP.template.md`;
- `docs/phases/README.md` и `docs/decisions/README.md` — соглашение об именах и
  граница между ADR продукта и ADR framework'а.

### Changed

- **Default Read Set определяется ровно в одном месте** — `docs/system/TOKEN_EFFICIENCY.md`.
  Раньше набор был перечислен в шести файлах в четырёх разных вариантах; `ROADMAP.md`
  входил в одни и отсутствовал в других, из-за чего агент, следующий `AGENTS.md`
  буквально, не мог выполнить handoff;
- **`docs/project/ROADMAP.md` стал каноническим указателем текущей фазы.** Раньше
  указателя не существовало: единственным носителем был disposable `NEXT_SESSION.md`,
  а промпт восстановления зависел от того, что он же и искал;
- **`prompts/START_NEW_PROJECT.md` переставлен**: харнес → продукт и классификация →
  архитектура → roadmap → и только потом tooling bootstrap. Раньше шесть инструментов
  ставились до того, как становились известны язык, стек и tier. Semble, Serena и RTK
  теперь откладываются до появления кода — в пустом репозитории обнаруживать нечего;
- ADR-001 переехал в `.specify/decisions/`. В project-owned `docs/decisions/` апдейтеру
  запрещено что-либо трогать, поэтому framework-ADR там молча устарел — он до сих пор
  описывал профиль без Semble/Serena/RTK. Заодно освободил номер ADR-001 для продукта;
- ADR-001 больше не дублирует профиль, а ссылается на `integrations/PROFILES.md`;
- каждое перечисление профиля теперь несёт указатель на канонический источник, и это
  проверяется скриптом;
- пример handoff в `docs/system/SESSION_HANDOFF.md` переписан: он был реликтом
  дореализационной версии — упоминал «Spec Kit for WHAT» и не знал про Semble/Serena/RTK,
  оставаясь при этом единственным копируемым образцом в репозитории;
- `AUDIT_WORKFLOW`, `WORKFLOW_SELF_AUDIT` и `UPDATE_WORKFLOW` обязаны цитировать вывод
  `tools/audit.py`. Вердикт `HEALTHY` без доказательства нарушал §9 самой Конституции;
- источник обновления: релиз/тег → закреплённый SHA → движущаяся ветка. Прежняя
  формулировка требовала предпочитать тег, которого в апстриме не существует.

### Migration

Обратная совместимость сохранена, ручных действий не требуется. Для существующих
проектов рекомендуется:

1. проставить маркеры `[ ]` / `[>]` / `[x]` в своём `docs/project/ROADMAP.md`;
2. переименовать файлы фаз в `docs/phases/NN-kebab-name.md`, если формат отличался;
3. запустить `python3 tools/audit.py`.

## [0.7.0] — 2026-08-08

### Added

- Serena как Recommended symbol/refactor capability;
- `integrations/SERENA.md` с project-level overlap policy;
- автоматическая установка/настройка Serena во время первого tooling bootstrap;
- явный code-context router между Semble, Serena и native agent tools;
- graceful fallback при unsupported/stale Serena language backend.

### Changed

- Recommended profile теперь: Token-Efficient Spec Kit + Superpowers + Semble + Serena + RTK + gstack + Context7;
- Semble отвечает за intent-based discovery: «где находится логика X?»;
- Serena отвечает за symbol semantics: declarations, references, implementations, diagnostics и semantic refactoring;
- Serena generic file/search/shell/memory tools должны исключаться на project level, когда текущая upstream-версия это поддерживает;
- добавлено правило `no-double-discovery`: Semble и Serena не должны независимо переискать один и тот же code context без причины.

## [0.6.0] — 2026-08-08

### Added

- Semble как Recommended capability для token-efficient code retrieval;
- RTK как Recommended capability для сокращения terminal/test/build/git output;
- автоматическая установка/настройка Semble и RTK во время первого `START_NEW_PROJECT` tooling bootstrap;
- отдельные integration policies `integrations/SEMBLE.md` и `integrations/RTK.md`;
- graceful fallback, если Semble/RTK недоступны или небезопасны для активного coding harness.

### Changed

- Recommended profile теперь: Token-Efficient Spec Kit + Superpowers + Semble + RTK + gstack + Context7;
- token-efficiency разделена на уровни: project/docs context, code retrieval, shell/tool output и fresh external docs;
- RTK должен проходить реальную post-install verification и не считается готовым только по success-ответу installer;
- глобальные RTK hooks/instructions не должны применяться без одноразового подтверждения, если нет безопасного project-scoped варианта;
- Semble предпочтительно подключается через MCP, когда active harness это поддерживает.

## [0.5.0] — 2026-08-08

### Added

- самостоятельный Token-Efficient Spec Kit core без обязательной зависимости от GitHub Spec Kit;
- Recommended profile: Superpowers + gstack + Context7;
- Optional Advanced Spec Mode с GitHub Spec Kit для сложных фаз;
- обязательный Session Handoff и `NEXT SESSION PROMPT`;
- `docs/project/NEXT_SESSION.md` как human-friendly navigation state;
- русское и английское README;
- `docs/USAGE_GUIDE.md` и `docs/WORKFLOW.md`;
- tooling profiles и ownership policy;
- ADR о переводе GitHub Spec Kit в optional capability;
- versioning layer;
- Workflow Self-Audit;
- Project Doctor;
- безопасный workflow update protocol;
- open-source contribution/security documentation.

### Changed

- Token-Efficient Spec Kit теперь владеет Project Brief, Architecture, Roadmap, phases, task batches, convergence и handoff;
- GitHub Spec Kit больше не входит в default installation;
- Superpowers используется как implementation discipline, а не как второй canonical planning system;
- gstack используется выборочно как challenge/review/QA layer;
- Context7 используется по требованию для свежей технической документации.

## [0.4.0] — 2026-08-08

### Added

- Recommended AI engineering tooling profile;
- GitHub Spec Kit, Superpowers, gstack и Context7 integrations;
- tooling bootstrap и ownership rules.

## [0.3.0] — 2026-08-08

### Added

- phase/session handoff protocol;
- автоматическая генерация следующего copy-paste prompt;
- `NEXT_SESSION.md`.

## [0.2.0] — 2026-08-08

### Added

- универсальные Project Brief, Architecture, Roadmap, phase и ADR templates;
- token-efficient context rules;
- adaptive S/M/L workflow.

## [0.1.0] — 2026-08-08

### Added

- первоначальный универсальный Token-Efficient Spec Kit workflow;
- Constitution;
- core prompts для старта, продолжения, review, bug fix и change request.
