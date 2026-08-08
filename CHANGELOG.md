# Changelog

Все заметные изменения Token-Efficient Spec Kit фиксируются здесь.

Формат основан на принципах Keep a Changelog, версии следуют Semantic Versioning.

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
