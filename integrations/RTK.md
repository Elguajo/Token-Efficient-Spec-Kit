# RTK Integration

Role: reduce noisy terminal/tool output before it enters AI context.

Repository:

https://github.com/rtk-ai/rtk

## Why it exists

Even when project and code context are small, terminal output can waste large amounts of context:

```text
test logs
git diff/status output
build output
linters
Docker logs
package-manager noise
```

RTK filters supported commands into compact, decision-relevant output.

## Recommended role

```text
Token-Efficient Spec Kit
→ controls project/document context

Semble
→ controls code retrieval context

RTK
→ controls shell/tool output context
```

RTK is not a source of project truth and must never hide failures merely to save tokens.

## Default installation

RTK is part of the Recommended profile.

The setup agent must check the current official RTK documentation for the active OS and coding harness before installation/configuration.

Prefer:

1. an official pre-built/user-level package/install method;
2. the current agent-specific RTK integration;
3. project-scoped configuration when the harness supports it;
4. the narrowest safe scope that still provides transparent filtering.

Some harness integrations may modify global user-level hooks/instructions. If the only supported integration changes behavior for all projects, request one-time user approval before applying that global configuration. Installing/configuring the current project must not silently rewrite unrelated global agent settings.

## Verification is mandatory

Do not consider RTK ready merely because installation returned success.

Verify:

```text
- `rtk --version` or current equivalent works;
- active harness integration is detected where supported;
- a representative command is filtered correctly;
- command semantics are unchanged;
- failures remain visible/actionable;
- full/raw output can still be recovered when debugging requires it.
```

If automatic rewriting corrupts or changes a command, disable that integration immediately and fall back to normal shell output or selective/manual RTK use.

Record degraded status rather than breaking the coding workflow.

## Usage policy

Prefer RTK filtering for verbose supported commands such as:

```text
git status / diff / log
unit/integration test runners
linters/typecheckers
build commands
Docker/process listings/logs
other commands explicitly supported upstream
```

Do not route through RTK when:

- raw output is required for root-cause analysis;
- the command/filter is unsupported;
- filtering would remove decision-critical diagnostics;
- an active known integration bug affects the current harness/command.

## Failure/debug policy

Token efficiency must never outrank correctness.

If compact output is insufficient:

```text
compact result
→ inspect saved/raw/full output
→ diagnose
→ return to compact mode afterward
```

Do not repeatedly rerun a failing command only to recover details that RTK already saved or can expose.

## Savings reporting

RTK reports savings in shell-output tokens/bytes. This is not the same as reducing the user's total LLM bill by the same percentage. Treat reported savings as tool-output efficiency metrics.

## Graceful fallback

If RTK cannot be installed or safely integrated:

```text
Workflow continues normally
→ use native shell commands
→ keep outputs scoped manually
→ record RTK as DEGRADED / NOT AVAILABLE
```

RTK must never be a blocker for starting or continuing the product.
