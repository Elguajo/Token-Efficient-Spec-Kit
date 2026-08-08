# Audit Token-Efficient Workflow

```text
Audit the Token-Efficient Spec Kit workflow itself.

This is a framework consistency audit, not an application feature review.

STEP 0 — RUN THE MACHINE CHECKS FIRST, AND QUOTE THE OUTPUT

```bash
python3 tools/audit.py
```

This is the evidence for this audit. Constitution section 9 forbids claiming a
result without it, and an agent grading its own prose is not evidence. Paste the
script's verdict verbatim into your report.

If it exits non-zero, the workflow is NEEDS ATTENTION regardless of how the prose
reads. Fix what it reports before assessing anything by hand.

The script covers: internal link resolution, version consistency across
VERSION/READMEs/CHANGELOG, single definition of the Default Read Set, canonical
pointer on every profile listing, phase file naming, exactly one current-phase
marker, framework/project ownership boundaries, and required files.

Everything below is the judgement layer the script cannot check.

Read:
1. tools/audit.py output from STEP 0
2. CHANGELOG.md
3. .specify/memory/constitution.md
4. AGENTS.md
5. README.md
6. docs/README.md
7. docs/USAGE_GUIDE.md
8. docs/WORKFLOW.md
9. docs/system/WORKFLOW_SELF_AUDIT.md
10. docs/system/TOKEN_EFFICIENCY.md
11. docs/system/SESSION_HANDOFF.md
12. docs/system/WORKFLOW_UPDATE_POLICY.md if present
13. integrations/README.md
14. integrations/PROFILES.md
15. integrations/TOOLING_POLICY.md
16. integrations/SEMBLE.md if present
17. integrations/SERENA.md if present
18. integrations/RTK.md if present
19. all main files under prompts/
20. templates only where needed to validate current workflow behavior

Do NOT inspect all application source code unless a framework instruction directly depends on it.

Check:
- ownership contradictions;
- default-vs-optional tooling contradictions;
- stale references to GitHub Spec Kit as a required default;
- stale Recommended profiles that omit/misassign Semble, Serena or RTK;
- duplicate planning/specification systems;
- Semble and Serena overlapping as broad discovery owners;
- Serena memory becoming a competing project-memory/source-of-truth layer;
- inconsistent phase/session handoff behavior;
- places where the user is forced to manually install ordinary Recommended tooling without a real blocker;
- places where the user is forced to decide routine engineering next steps;
- instructions that cause unnecessary full-project context loading;
- broad grep/full-file exploration where routed retrieval should be preferred;
- Semble + Serena + grep being used for the same discovery question without failure/ambiguity/verification justification;
- verbose shell/test/build output where safe compact output is available;
- any token-saving instruction that could hide critical diagnostics or change command semantics;
- unsafe workflow-update behavior;
- stale/nonexistent paths or documentation links;
- VERSION / CHANGELOG inconsistency;
- prompt instructions that conflict with Constitution or AGENTS.md;
- unnecessary permanent documentation/context creep.

Verify the current default token-efficiency architecture:

Project/docs context         → Token-Efficient Spec Kit
Intent-based code discovery  → Semble
Symbol semantics/refactoring → Serena
Shell/tool output            → RTK
Fresh external docs          → Context7 on demand

Verify Recommended profile unless a deliberate versioned change says otherwise:

Token-Efficient Spec Kit
+ Superpowers
+ Semble
+ Serena
+ RTK
+ gstack
+ Context7

Verify:
- Semble owns intent-based discovery;
- Serena owns symbol navigation/relationships/refactoring;
- Serena generic file/search/shell/memory overlap is excluded when supported;
- Semble/Serena/RTK all have graceful fallback and do not become blockers or sources of project truth;
- one code-context capability is chosen first, rather than stacking all installed tools.

Classify findings:
CRITICAL / HIGH / MEDIUM / LOW.

Do not automatically redesign the framework.
For each finding give the smallest coherent fix.

If no material problems exist, say so explicitly.

Return:

WORKFLOW AUDIT

Version:
- ...

Overall status:
- HEALTHY / NEEDS ATTENTION / UNSAFE

Critical:
- None / ...

High:
- None / ...

Medium:
- None / ...

Low:
- None / ...

Token-efficiency findings:
- ...

Tooling-bootstrap findings:
- ...

Documentation/path findings:
- ...

Recommended fixes in priority order:
1. ...
2. ...

Do not modify files unless the user explicitly asks to apply the audit fixes.
```
