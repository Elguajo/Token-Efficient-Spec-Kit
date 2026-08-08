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
+ Semble
+ Serena
+ RTK
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

**Semble — CODE DISCOVERY**

```text
semantic/hybrid code retrieval
intent-based discovery
small relevant snippets
less grep + full-file reading
```

Use when the question is essentially **“where is the logic related to X?”** or code discovery would otherwise require broad search/read cycles.

Do not force it for tiny repositories, known small files or already-known symbols.

**Serena — SYMBOL / REFACTOR**

```text
symbol navigation
references / implementations
diagnostics
semantic rename
symbol-aware editing/refactoring
```

Use when the question is essentially **“what symbol is this, who uses it, or how can I change it safely?”**.

Serena must not duplicate Semble's broad semantic discovery, shell execution or Token-Efficient project memory. See `SERENA.md` for the overlap-reduction policy.

**RTK — TOOL OUTPUT**

```text
compact shell output
filtered test/build/lint/git output
recoverable raw diagnostics when needed
```

RTK must preserve command semantics and failures. Disable/fallback if filtering is unsafe for the active harness or command.

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
→ Minimal when external tooling adds little value

Tier M
→ Recommended

Tier L / High Risk
→ Recommended + stronger quality gates
→ add Advanced Spec Mode only when formal specification provides clear value
```

The scoped bootstrap may install the capabilities selected for the known stack/tier
once even if a particular later session does not invoke all of them. Deferred or
skipped capabilities are not installed speculatively.

**Installed does not mean always loaded, always queried or queried together.**

For code work route by question type:

```text
Intent / “where is this logic?”
→ Semble

Known symbol / references / implementations / rename / semantic edit
→ Serena

Tiny exact file/string edit
→ native agent tools

Verbose terminal output
→ RTK
```

Do not make Semble and Serena independently rediscover the same code unless the first tool failed or the second tool needs the discovered symbol for a different operation.

High Risk means stronger evidence and review, not automatically more frameworks.
