# Tooling Ownership Policy

Purpose: prevent duplicate planning, duplicate context and conflicting agent instructions.

## Ownership matrix

| Concern | Owner | Supporting tool |
|---|---|---|
| User outcome | Project Brief | — |
| Global principles | Constitution | — |
| Architecture | Token-Efficient Spec Kit project docs | Spec Kit plan may reference it |
| Feature specification | GitHub Spec Kit | gstack may challenge/review |
| Implementation plan | GitHub Spec Kit | gstack engineering review |
| Task decomposition | GitHub Spec Kit | — |
| Implementation discipline | Superpowers | Spec Kit tasks are input |
| TDD | Superpowers | project test tooling |
| Systematic debugging | Superpowers | gstack investigate may assist |
| Fresh library/API docs | Context7 | official primary docs when needed |
| Product/design critique | gstack | project UI specs |
| Code review | gstack / native agent review | Superpowers verification |
| Browser QA | gstack | Playwright/project E2E |
| Release readiness | gstack + project checks | CI |
| Final source of truth | repository canonical docs + code/tests | never external skill output alone |

## Rules

### Spec Kit owns WHAT

Canonical workflow:

```text
specify
→ clarify when needed
→ plan
→ checklist/analyze when risk justifies it
→ tasks
→ implementation handoff
→ converge
```

### Superpowers owns HOW

When Spec Kit artifacts already exist, do not ask Superpowers to create a second product brainstorm or second canonical plan.

Use Superpowers for:

```text
TDD
execution discipline
systematic debugging
verification
branch finishing / implementation review where available
```

### gstack is a challenge layer

Recommended use:

```text
before risky implementation
→ engineering review

for UI/design-heavy work
→ design review

after implementation
→ code review

for web flows
→ browser QA

before release
→ ship/release checks
```

Avoid by default:

```text
gstack autoplan replacing Spec Kit plan
gstack-generated parallel canonical specs
re-running product discovery after requirements are already accepted
```

These may be used only if the user explicitly wants a rethink or the current spec is materially flawed.

### Context7 is on-demand

Use Context7 when implementation depends on current library/framework/provider APIs.

Do not fetch documentation for stable language basics or every trivial code edit.

When Context7 and official provider documentation disagree, verify the official primary source before a security/payment/production-critical decision.

## Token rule

A tool being installed does **not** mean its entire instructions must be loaded in every session.

Only invoke a skill/tool when the current task benefits from it.
