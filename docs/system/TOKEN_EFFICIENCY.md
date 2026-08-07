# Token Efficiency Protocol

## Context pyramid
Always: constitution, project brief, compact architecture, engineering rules, current phase, relevant code.
Sometimes: specific ADR, specific API docs, directly related prior phase output.
Rarely: master spec, all ADRs, all completed phases, full chat history.

## Canonical ownership
- Product truth -> PROJECT_BRIEF
- Chosen stack/system -> ARCHITECTURE
- Why a major decision -> ADR
- Current work -> phase spec
- Global principles -> Constitution
Do not duplicate the same explanation across files.

## Phase format
Keep: Goal, Context, In scope, Out of scope, Tasks, Acceptance criteria, Security/negative tests if relevant, Verification.

## Granularity
Implement 1–3 related tasks per run.

## Research notes
Save only conclusions and links that influence implementation.

## Load larger context only when
- compact docs conflict;
- cross-phase invariant is unclear;
- a major change affects architecture;
- debugging spans several subsystems.
