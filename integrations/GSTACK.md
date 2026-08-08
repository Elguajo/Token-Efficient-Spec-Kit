# gstack Integration

Role: independent challenge, review, browser QA and release-quality layer.

Repository:

https://github.com/garrytan/gstack

## Recommended responsibilities

Use gstack primarily for:

```text
engineering plan review
design review
code review
investigation
browser QA
release / ship checks
cross-model second opinion where available
```

## Recommended gates

### Before risky implementation

Use an engineering-plan review to challenge assumptions, edge cases and architecture.

### UI/design-heavy feature

Use design review after the first coherent implementation, not before every component.

### After implementation

Use review to find correctness, security and maintainability issues.

### Web application flow

Use browser QA for real interaction paths when relevant.

### Before release

Use ship/release checks after the project's own tests/build have passed.

## Avoid duplicate planning

Token-Efficient Spec Kit remains the canonical project planning layer. GitHub Spec
Kit may add formal phase-level planning only when Optional Advanced Spec Mode is
explicitly enabled.

Do not use gstack `autoplan` or equivalent planning workflows by default when an accepted Spec Kit plan already exists.

Do not regenerate product requirements in gstack unless:

- the user explicitly requests a rethink;
- a review finds a material flaw in the accepted specification;
- project constraints have changed.

## Installation

gstack supports multiple coding-agent hosts and its installation layout evolves.

The setup agent must inspect the current upstream README/setup instructions immediately before installation.

Prefer namespaced skill commands where gstack supports them if another skill pack is installed, because this reduces command-name collisions.

Do not vendor the full gstack repository into application source unless the upstream team-mode instructions specifically require it.

## Prerequisites

gstack may require tools such as Bun/Node and browser dependencies for some skills. Detect prerequisites before installation; do not silently install system-level runtimes without informing the user.

## Windows

Use the current upstream Windows guidance. Some gstack browser/build flows have historically required Git Bash/WSL or specific Node/Bun handling; verify current support instead of assuming Unix behavior.

## Verification

After setup:

- verify skills are discoverable by the selected harness;
- verify there are no duplicate skill registrations;
- verify a basic review skill works;
- for web projects, verify browser QA only when its browser prerequisites are available.
