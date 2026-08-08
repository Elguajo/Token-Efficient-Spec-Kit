# Tooling Ownership Policy

Purpose: prevent duplicate planning, duplicate context and conflicting agent instructions.

## Core rule

**Token-Efficient Spec Kit is the canonical orchestration and specification layer.**

External tools may strengthen implementation, retrieval, refactoring, review or research, but they do not become the project source of truth.

## Ownership matrix

| Concern | Owner | Supporting tool |
|---|---|---|
| User outcome | Token-Efficient Project Brief | — |
| Global principles | Constitution | — |
| Architecture | Token-Efficient Architecture | gstack may review |
| Roadmap / phases | Token-Efficient Roadmap + phase files | — |
| Phase scope / tasks | Current phase | optional GitHub Spec Kit in Advanced Spec Mode |
| Acceptance criteria / convergence | Token-Efficient current phase | gstack review where useful |
| Context routing | Token-Efficient Spec Kit | — |
| Intent-based code discovery | Semble when useful | native targeted search fallback |
| Symbol navigation / references / semantic refactor | Serena when useful | native IDE/agent fallback |
| Shell/tool output compression | RTK when safe/useful | native shell fallback |
| Session handoff | Token-Efficient Spec Kit | — |
| Implementation discipline | Superpowers | native coding agent |
| TDD | Superpowers | project test tooling |
| Systematic debugging | Superpowers | gstack investigation may assist |
| Fresh library/API docs | Context7 | official primary docs when critical |
| Product/design critique | gstack | project UI specs |
| Code review | gstack / native agent review | Superpowers verification |
| Browser QA | gstack | Playwright/project E2E |
| Release readiness | Token-Efficient gates + gstack | CI |
| Formal deep specification | Optional GitHub Spec Kit | only Advanced Spec Mode |
| Final source of truth | repository canonical docs + code/tests | never external skill output alone |

## Default workflow

```text
User outcome
→ Project Brief
→ Architecture
→ Roadmap
→ Current Phase
→ route code question to Semble OR Serena OR native tools
→ 1–3 tasks
→ Superpowers/native implementation
→ RTK for compact shell output when safe
→ tests
→ selective gstack review/QA
→ convergence
→ NEXT SESSION PROMPT
```

---

## Code-context router — Semble vs Serena

The two tools are complementary only if they answer **different questions**.

### Semble owns intent-based discovery

Use Semble when the relevant code location is not yet known.

Typical question:

```text
Where is entitlement checked after a subscription webhook?
Which part of the codebase controls image preview generation?
```

Preferred flow:

```text
semantic/hybrid query
→ relevant snippets/locations/symbol names
→ stop broad discovery
```

Do not force Semble for tiny repositories, known small files, exact string/config edits or already-known symbols.

Semble never owns project decisions or architecture.

### Serena owns symbol semantics and semantic refactoring

Use Serena when the symbol or candidate file is already known, or when the operation depends on language semantics.

Typical operations:

```text
find declaration
find implementations
find referencing symbols
symbol overview
diagnostics
cross-file symbol rename
replace symbol body
insert before/after symbol
safe symbol deletion where supported
```

Serena must be configured so that overlapping generic file search/read, shell and memory tools are excluded when the current upstream version supports that configuration.

See `SERENA.md`.

### No-double-discovery rule

Do not do this by default:

```text
Semble broad discovery
→ Serena broad discovery of the same question
→ native grep of the same question
```

Instead:

```text
Semble finds exact candidate symbol
→ Serena inspects references / performs semantic edit
```

or:

```text
User names exact symbol
→ Serena directly
```

or:

```text
Tiny exact edit
→ native tools directly
```

A second retrieval layer is justified only when:

- the first result is ambiguous/incomplete;
- Serena needs the symbol discovered by Semble for a distinct symbol-level operation;
- the language server/backend is degraded and fallback is needed;
- verification requires an independent exact check.

### Serena fallback

If Serena's language backend is unavailable, stale or unreliable:

```text
Serena DEGRADED
→ Semble/native targeted search/read/edit
```

Do not block product work.

---

## RTK owns terminal-output compression

Use RTK only when its filter preserves the command's semantics and decision-critical diagnostics.

Correctness outranks token savings.

If compact output is insufficient or an integration is unreliable:

```text
RTK compact output
→ recover raw/full output if needed
→ or disable/fallback to native command
```

Do not let RTK hide failures or block debugging.

---

## Superpowers owns HOW

Use for:

```text
TDD
execution discipline
systematic debugging
verification
```

Do not let it silently replace accepted Project Brief, Architecture, Roadmap or phase scope with a second canonical planning system.

---

## gstack is a challenge layer

Recommended use:

```text
risky design → engineering review
UI-heavy work → design review
after important implementation → code review
web flows → browser QA
before release → ship/release checks
```

Do not run every gstack skill after every tiny task.
Do not use gstack autoplan as a parallel canonical roadmap unless the user explicitly requests a rethink.

---

## Context7 is on-demand

Use when implementation depends on current library/framework/provider APIs.
Do not fetch docs for stable language basics or every trivial edit.
For security/payment/production-critical decisions, verify primary official sources when needed.

---

## GitHub Spec Kit — Optional Advanced Spec Mode

GitHub Spec Kit is **not required by the default workflow**.

Enable it only when formal feature-level specification adds clear value, such as:

```text
payments
complex authorization
multi-tenancy boundaries
public APIs
critical migrations
large ambiguous features
cross-system high-risk integrations
```

When enabled:

```text
Token-Efficient Spec Kit
= project-level intent, architecture, roadmap, phase boundaries, handoff

GitHub Spec Kit
= optional deep specification inside the current phase

Superpowers
= implementation discipline
```

If a Spec Kit ↔ Superpowers bridge is used, it exists only to coordinate that optional Advanced Spec Mode.

---

## Token rule

A tool being installed does **not** mean its instructions should be loaded or its tools called in every session.

Recommended token-efficiency layers:

```text
project/docs context          → Token-Efficient Spec Kit
intent-based code discovery   → Semble
symbol semantics/refactoring  → Serena
shell/tool output              → RTK
fresh external docs           → Context7 on demand
```

The router should choose the **single cheapest adequate capability first**, then escalate only when the next tool answers a different question or the first one fails.
