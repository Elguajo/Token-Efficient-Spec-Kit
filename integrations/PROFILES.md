# Tooling Profiles

Token-Efficient Spec Kit is the core workflow. External tools are capabilities, not foundations.

## 1. Minimal

```text
Token-Efficient Spec Kit
```

Use for:
- landing pages;
- small scripts/CLI;
- simple automations;
- tiny features;
- prototypes where extra tooling adds little value.

---

## 2. Recommended — default

```text
Token-Efficient Spec Kit
+ Superpowers
+ gstack
+ Context7
```

Use for most production-oriented projects.

### Responsibilities

**Token-Efficient Spec Kit — CORE**

```text
user intent
project brief
architecture
roadmap
phases
phase tasks
acceptance criteria
context routing
quality routing
convergence
session handoff
next-session prompt
```

**Superpowers — HOW**

```text
TDD
implementation discipline
systematic debugging
verification
```

**gstack — Challenge / QA**

```text
engineering review
design review
code review
browser QA
investigation
release / ship checks
```

Use selectively. It must not become a second canonical planner.

**Context7 — Fresh Docs**

Use on demand for current library/API documentation.

---

## 3. Advanced Spec Mode — optional

```text
Recommended profile
+ GitHub Spec Kit
+ Spec Kit ↔ Superpowers bridge when currently supported/useful
```

Enable only when a phase benefits from formal deep specification, for example:

- payments;
- complex authorization;
- multi-tenant data isolation;
- difficult migrations;
- public API contracts;
- large ambiguous features;
- high-risk cross-system integrations.

Typical optional flow:

```text
phase definition from Token-Efficient Spec Kit
→ Spec Kit specify / clarify / plan / checklist / tasks / analyze as justified
→ implementation
→ converge
→ Token-Efficient session handoff
```

GitHub Spec Kit does not replace the project-level Brief, Architecture, Roadmap, phase boundaries or handoff system.

---

## Automatic selection

```text
Tier S + Low Risk
→ Minimal

Tier M
→ Recommended

Tier L / High Risk
→ Recommended + stronger quality gates
→ add Advanced Spec Mode only when formal specification provides clear value
```

High Risk means stronger evidence and review, not automatically more frameworks.
