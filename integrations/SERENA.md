# Serena Integration

Role: **SYMBOL / REFACTOR layer**.

Repository:
https://github.com/oraios/serena

Official docs:
https://oraios.github.io/serena/

Serena complements Semble; it must not become a second general code-search or project-memory system.

## Responsibility split

```text
Semble
→ intent/semantic discovery: WHERE is the relevant logic?

Serena
→ symbol semantics: WHAT symbol is this, WHO references it, and HOW can it be changed safely?

Native agent tools
→ tiny exact reads/edits and non-code files when cheaper

RTK
→ compact terminal/test/build/git output
```

The core rule is **do not ask two tools the same question**.

---

## Use Serena for

Prefer Serena when the task is symbol-shaped:

```text
find a declaration
find implementations
find referencing symbols
inspect top-level symbols in a known file
get symbol/file diagnostics
cross-file symbol rename
replace a function/class/method body
insert before/after a known symbol
safe symbol deletion where supported
```

These operations use language-server/IDE semantics and are especially useful after the relevant area has already been identified.

---

## Do not use Serena for by default

Do not use Serena as a duplicate of Semble or Token-Efficient project memory.

Avoid Serena for:

```text
broad natural-language discovery across an unfamiliar repository
project planning / roadmap / architecture
session memory
reading arbitrary full files
regex/text search when Semble or an exact native search is better
shell commands
terminal output filtering
```

For tiny known edits, a direct native edit may also be cheaper than a symbol round-trip.

---

## Routing with Semble

### Question is intent-based

Example:

```text
Where is subscription entitlement checked after a webhook?
```

Route:

```text
Semble
→ identify relevant files/snippets/symbol names
→ Serena only if symbol references/refactor/diagnostics are then needed
```

### Question is symbol-based

Example:

```text
Who calls refreshSession?
Rename refreshSession to rotateSession across the codebase.
```

Route directly to Serena.

Do **not** run Semble first just because it is installed.

### Candidate is already known

If Semble already returned the exact relevant symbol/file:

```text
DO NOT repeat broad discovery with Serena.
Use Serena directly for symbol relationships or semantic editing.
```

### Serena cannot answer reliably

If the current language/backend is unsupported, indexing is stale, or a symbol operation fails:

```text
Serena
→ Semble/native targeted fallback
```

Do not block implementation merely because Serena is degraded.

---

## Recommended project configuration

Serena supports per-project configuration in `.serena/project.yml`.

The setup agent must first inspect the **current** Serena tool list, for example with the current equivalent of:

```bash
serena tools list --all
```

Then configure Serena so overlapping generic tools are excluded when those tool names still exist upstream.

Preferred policy:

```yaml
ignore_all_files_in_gitignore: true
read_only: false

# Verify current upstream tool names before writing this list.
excluded_tools:
  # Generic discovery / file operations — Semble or native tools own these.
  - search_for_pattern
  - list_dir
  - find_file
  - read_file
  - execute_shell_command
  - replace_content
  - replace_in_files
  - replace_lines

  # Project memory — Token-Efficient canonical docs own long-lived memory.
  - list_memories
  - read_memory
  - write_memory
  - edit_memory
  - delete_memory
  - rename_memory

  # Serena onboarding/memory-oriented discovery is unnecessary when the
  # Token-Efficient project state already exists.
  - onboarding

initial_prompt: |
  Token-Efficient Spec Kit owns project truth and planning.
  Semble owns broad semantic code discovery.
  Use Serena only for symbol navigation, references, diagnostics and semantic refactoring.

# Keep symbol-info enrichment bounded. Raise only if the language server
# consistently needs more time.
symbol_info_budget: 8
```

This is a **policy template**, not a command to blindly write unsupported keys/tool names. The bootstrap agent must validate the current Serena version before applying it.

---

## Expected active Serena capability

After overlap reduction, the useful Serena surface should be primarily symbol tools such as:

```text
find_declaration
find_implementations
find_referencing_symbols
find_symbol
get_symbols_overview
get_diagnostics_for_file
rename_symbol
replace_symbol_body
insert_before_symbol
insert_after_symbol
safe_delete_symbol
```

Exact availability depends on the current Serena version, language server and backend.

Optional/BETA tools should not be enabled automatically just because they exist.

---

## Installation

Installation changes over time.

The setup agent must read the current official Serena Quick Start rather than using an MCP/plugin marketplace command that upstream does not recommend.

Prefer:

```text
current official Serena installation
→ MCP integration for the active coding harness
→ project creation/indexing if required
→ project-specific overlap-reduction configuration
→ verification with one symbol lookup/reference query
```

Do not require Serena for tiny projects where no supported source language exists yet.

---

## Verification

After setup verify:

1. Serena connects to the active coding harness.
2. The current project is recognized/indexed where required.
3. A known symbol can be found.
4. References/overview work for a supported source file.
5. Generic file/search/shell/memory tools are excluded according to the overlap policy when supported.
6. Semble still remains the preferred broad semantic-discovery layer.
7. No Serena memory becomes a competing Project Brief / Architecture / Roadmap / NEXT_SESSION source of truth.

If any of these fail, mark Serena `DEGRADED` and use Semble/native tools instead of blocking product work.
