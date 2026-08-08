# Semble Integration

Role: token-efficient code retrieval.

Repository:

https://github.com/MinishLab/semble

## Why it exists

Token-Efficient Spec Kit keeps project/document context small. Semble extends that principle to source-code discovery.

Instead of repeatedly doing:

```text
grep
→ open large file
→ search again
→ open another large file
```

prefer targeted retrieval:

```text
natural-language/code query
→ relevant code chunks only
→ open full files only when implementation context requires it
```

## Recommended role

```text
Token-Efficient Spec Kit
→ decides WHAT context is needed

Semble
→ finds the smallest useful CODE context
```

Semble is not a planner, architecture owner or source of project truth.

## Default installation

Semble is part of the Recommended profile.

The setup agent must verify current official upstream instructions before installing because integration syntax may change.

At the time this integration was documented, upstream recommends a user-level install such as:

```bash
uv tool install semble
```

and supports an installer that detects coding agents.

For unattended setup, upstream supports agent/type flags. Prefer MCP integration when supported because it avoids adding duplicate planning/instruction content to project files.

Conceptually:

```text
semble install --agent <active-agent> --type mcp --yes
```

Do not hardcode the agent ID without detecting the active harness and checking current upstream documentation.

If `uv` or another required runtime/package manager is missing, use a currently supported safe user-level alternative when available. Ask only if installing a missing global/system runtime requires user approval.

## Usage policy

Use Semble first when:

- exploring an unfamiliar/non-trivial codebase;
- finding implementation by behavior rather than exact symbol name;
- locating relevant code across many files;
- searching for a feature, flow, responsibility or related implementation;
- broad grep/read cycles would load excessive source context.

Do not force Semble when:

- the exact file is already known and small;
- an exact local symbol/search is cheaper;
- only a few lines need inspection;
- the repository is tiny enough that retrieval overhead provides no benefit.

After Semble returns relevant snippets, read only the files/ranges needed to implement or verify the task.

## Indexing / privacy

Semble is local-first and should respect repository ignore rules. Preserve `.gitignore` behavior and add `.sembleignore` only when the project needs Semble-specific exclusions.

Never intentionally index secrets, credentials, generated vendor trees or sensitive files excluded by project policy.

## Verification

After installation verify:

```text
- semble executable/tool is available;
- active coding agent can access the configured integration;
- a small semantic search returns relevant code locations;
- the integration does not overwrite canonical AGENTS/Constitution rules;
- no secrets are exposed or committed.
```

If MCP integration cannot be configured safely for the active harness, keep the workflow functional without Semble and record `DEGRADED / manual action required` in `docs/project/TOOLING_STATUS.md`.

## Savings reporting

Semble can expose estimated retrieval savings. Treat these as directional estimates, not guaranteed reductions in the total LLM bill.
