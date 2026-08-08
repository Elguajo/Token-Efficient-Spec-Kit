#!/usr/bin/env python3
"""Token-Efficient Spec Kit - machine-checkable workflow self-audit.

Produces evidence, not an opinion. Constitution section 9 requires evidence before
claims, so prompts/AUDIT_WORKFLOW.md and prompts/UPDATE_WORKFLOW.md must cite this
script's output instead of asserting HEALTHY on their own.

Usage: python3 tools/audit.py    (exit 0 = HEALTHY, 1 = NEEDS ATTENTION)
"""
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
os.chdir(ROOT)
FAIL = []

def sect(t): print("\n" + t)
def ok(t):   print("  ok    " + t)
def bad(t, detail=None):
    print("  FAIL  " + t)
    for d in (detail or []): print("          " + d)
    FAIL.append(t)

MD = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
def rel(p): return str(p.relative_to(ROOT))
def text(p): return p.read_text(encoding="utf-8", errors="replace")
def fenced_blocks(body): return re.findall(r"```[a-z]*\n(.*?)```", body, re.S | re.I)

# ------------------------------------------------------------- 1. links
sect("1. Internal markdown links resolve")
broken = []
for p in MD:
    for m in re.finditer(r"\]\(([^)]+?\.md)(?:#[^)]*)?\)", text(p)):
        link = m.group(1)
        if link.startswith("http"): continue
        if not (p.parent / link).exists() and not (ROOT / link).exists():
            broken.append(f"{rel(p)} -> {link}")
ok("no broken internal links") if not broken else bad("broken internal links", broken)

# ---------------------------------------------------------- 2. versions
sect("2. Version is consistent across VERSION, both READMEs and CHANGELOG")
V = (ROOT / "VERSION").read_text().strip()
def find(p, rx):
    m = re.search(rx, text(ROOT / p))
    return m.group(1) if m else None
for f, rx in [("README.md", r"\*\*v(\d+\.\d+\.\d+)\*\*"),
              ("README_EN.md", r"\*\*v(\d+\.\d+\.\d+)\*\*"),
              ("CHANGELOG.md", r"^## \[(\d+\.\d+\.\d+)\]")]:
    got = re.search(rx, text(ROOT / f), re.M)
    got = got.group(1) if got else None
    ok(f"{f} = {V}") if got == V else bad(f"{f} = {got!r}, VERSION = {V}")

# ------------------------------------------- 3. one Default Read Set
sect("3. Default Read Set is defined in exactly one file")
CANON = "docs/system/TOKEN_EFFICIENCY.md"
RS = ["docs/project/PROJECT_BRIEF.md", "docs/project/ARCHITECTURE.md",
      "docs/project/ROADMAP.md", "docs/system/ENGINEERING_RULES.md",
      ".specify/memory/constitution.md"]
RS_CONCEPTS = [r"\bconstitution\b", r"project[_ ]brief", r"\barchitecture\b",
               r"\broadmap\b", r"engineering[_ ]rules", r"current phase"]
# These prompts intentionally define task-specific initialization/diagnostic reads,
# not the normal product Default Read Set.
RS_SCOPED_EXEMPT = {
    "docs/system/PROJECT_DOCTOR.md",
    "prompts/AUDIT_WORKFLOW.md",
    "prompts/PROJECT_DOCTOR.md",
    "prompts/START_NEW_PROJECT.md",
    "prompts/UPDATE_WORKFLOW.md",
}
dupes = []
for p in MD:
    if rel(p) == CANON or rel(p) in RS_SCOPED_EXEMPT: continue
    lines = text(p).splitlines()
    for i, ln in enumerate(lines):
        # Catch both path lists and prose aliases; the old check missed variants
        # such as "Constitution, Project Brief, Architecture, current phase".
        if not re.match(
                r"\s*(?:\d+\.\s+|[-*]\s+)?"
                r"(?:read\b|agent reads\b|before coding\b|чита(?:й|ть)\b)",
                ln, re.I):
            continue
        end = min(len(lines), i + 16)
        for j in range(i + 1, end):
            if re.match(r"^#{1,6}\s", lines[j]):
                end = j
                break
        window = "\n".join(lines[i:end])
        if CANON in window or "TOKEN_EFFICIENCY.md" in window:
            continue
        path_hits = sum(1 for item in RS if item in window)
        concept_hits = sum(1 for rx in RS_CONCEPTS if re.search(rx, window, re.I))
        if max(path_hits, concept_hits) >= 4:
            dupes.append(
                f"{rel(p)}:{i+1} restates {max(path_hits, concept_hits)} "
                "Default Read Set concepts without the canonical pointer")
            break
ok(f"only {CANON} defines it") if not dupes else bad(
    "the read set is restated elsewhere and will drift", dupes)

# ------------------------------- 4. profile enumerations point at canonical
sect("4. Every file enumerating the Recommended profile links to the canonical one")
TOOLS = ["Superpowers", "Semble", "Serena", "RTK", "gstack", "Context7"]
PROF_CANON = "integrations/PROFILES.md"
orphans = []
for p_ in MD:
    if rel(p_) in (PROF_CANON, "CHANGELOG.md"): continue
    body = text(p_)
    if not any(all(t in b for t in TOOLS) for b in fenced_blocks(body)):
        continue
    if "PROFILES.md" not in body:
        orphans.append(f"{rel(p_)} enumerates the profile without pointing at {PROF_CANON}")
ok(f"all profile listings reference {PROF_CANON}") if not orphans else bad(
    "profile enumerated with no pointer to canonical; ADR-001 went stale this way", orphans)

# ------------------------------ 5. late/scoped bootstrap and complete profile
sect("5. Documentation matches late/scoped tooling bootstrap")
BOOTSTRAP_DOCS = ["README.md", "README_EN.md", "docs/README.md",
                  "docs/USAGE_GUIDE.md", "docs/WORKFLOW.md",
                  "integrations/README.md"]
bootstrap_drift = []

def has_ordered_bootstrap_flow(body):
    for block in fenced_blocks(body):
        normalized = re.sub(r"[_-]+", " ", block).lower()
        positions = [normalized.find(term) for term in
                     ("project brief", "architecture", "roadmap",
                      "scoped tooling bootstrap")]
        if all(pos >= 0 for pos in positions) and positions == sorted(positions):
            return True
    return False

for name in BOOTSTRAP_DOCS:
    body = text(ROOT / name)
    missing = [tool for tool in TOOLS if tool not in body]
    if missing:
        bootstrap_drift.append(f"{name} omits Recommended tools: {', '.join(missing)}")
    if "PROFILES.md" not in body:
        bootstrap_drift.append(f"{name} does not point to {PROF_CANON}")
    if not re.search(r"scoped[ -]tooling bootstrap", body, re.I):
        bootstrap_drift.append(f"{name} does not describe a scoped tooling bootstrap")
    if not has_ordered_bootstrap_flow(body):
        bootstrap_drift.append(
            f"{name} does not show Project Brief -> Architecture -> Roadmap -> "
            "Scoped Tooling Bootstrap")

start = text(ROOT / "prompts/START_NEW_PROJECT.md")
steps = [start.find(label) for label in ("STEP 1 — UNDERSTAND", "STEP 4 — CHOOSE",
                                         "STEP 5 — CREATE ROADMAP",
                                         "STEP 6 — TOOLING BOOTSTRAP")]
if not all(pos >= 0 for pos in steps) or steps != sorted(steps):
    bootstrap_drift.append("START_NEW_PROJECT does not bootstrap after product/architecture/roadmap")
for tool in ("Semble", "Serena", "RTK", "gstack"):
    if tool not in start[start.find("Defer until a codebase"):start.find("Rules:")]:
        bootstrap_drift.append(f"START_NEW_PROJECT does not explicitly defer {tool}")

if "<WHAT_I_WANT>" in start:
    bootstrap_drift.append("START_NEW_PROJECT still requires a user-edited placeholder")
for required in ("normally three", "**Recommended**", "same session"):
    if required not in start:
        bootstrap_drift.append(
            f"START_NEW_PROJECT omits conversational product framing: {required!r}")

entry_docs = {
    "README.md": "Не открывай файл и не заменяй плейсхолдеры",
    "README_EN.md": "Do not edit the prompt or replace a placeholder",
    "docs/USAGE_GUIDE.md": "Не открывай prompt и не ищи в нём ничего для замены",
}
for name, marker in entry_docs.items():
    if marker not in text(ROOT / name):
        bootstrap_drift.append(
            f"{name} does not document the conversational new-project entry point")

ok("public/integration docs and START_NEW_PROJECT agree on scoped late bootstrap") \
    if not bootstrap_drift else bad("tooling bootstrap/profile documentation drift", bootstrap_drift)

# ------------------------------------------------- 6. phase file names
sect("6. Phase files follow docs/phases/NN-kebab-name.md")
bad_names = [rel(f) for f in (ROOT / "docs/phases").glob("*.md")
             if f.name != "README.md"
             and not re.fullmatch(r"\d{2}-[a-z0-9]+(-[a-z0-9]+)*\.md", f.name)]
ok("phase file names valid") if not bad_names else bad(
    "phase file names violate the convention", bad_names)

# --------------------------------------------- 7. current-phase marker
sect("7. ROADMAP marks exactly one current phase")
rm = text(ROOT / "docs/project/ROADMAP.md")
if "Not initialized" in rm:
    ok("roadmap not initialized yet (template repository)")
else:
    cur = len(re.findall(r"^\s*-\s*\[>\]", rm, re.M))
    pend = len(re.findall(r"^\s*-\s*\[ \]", rm, re.M))
    if cur == 1: ok("exactly one [>] phase")
    elif cur == 0 and pend == 0: ok("all phases complete")
    else: bad(f"{cur} phases marked [>]; expected exactly 1")

# ----------------------------------------------- 8. complete handoff contract
sect("8. Product and framework handoff rules are complete")
HANDOFF_FILES = [
    ".specify/memory/constitution.md",
    "AGENTS.md",
    "docs/WORKFLOW.md",
    "docs/system/SESSION_HANDOFF.md",
    "prompts/BUG_FIX.md",
    "prompts/CHANGE_REQUEST.md",
    "prompts/CONTINUE_PROJECT.md",
    "prompts/ENABLE_ADVANCED_SPEC_MODE.md",
    "prompts/GENERATE_NEXT_SESSION_PROMPT.md",
    "prompts/PROJECT_DOCTOR.md",
    "prompts/REVIEW_CURRENT_PHASE.md",
    "prompts/SETUP_RECOMMENDED_TOOLING.md",
    "prompts/START_NEW_PROJECT.md",
]
handoff_drift = []
for name in HANDOFF_FILES:
    body = text(ROOT / name)
    for required in ("docs/project/ROADMAP.md", "docs/project/NEXT_SESSION.md",
                     "NEXT SESSION PROMPT"):
        if required not in body:
            handoff_drift.append(f"{name} handoff omits {required}")

for name in (".specify/memory/constitution.md", "AGENTS.md",
             "docs/system/SESSION_HANDOFF.md"):
    body = text(ROOT / name)
    if not re.search(r"uninitialized|not initialized", body, re.I):
        handoff_drift.append(f"{name} omits the uninitialized-template exception")
    if not re.search(r"framework-only", body, re.I):
        handoff_drift.append(f"{name} omits the framework-only exception")

for name in ("prompts/AUDIT_WORKFLOW.md", "prompts/UPDATE_WORKFLOW.md"):
    body = text(ROOT / name)
    if "framework-only" not in body or "NEXT SESSION PROMPT" not in body:
        handoff_drift.append(f"{name} does not implement the framework-only handoff")
    if "docs/project/ROADMAP.md" not in body or "docs/project/NEXT_SESSION.md" not in body:
        handoff_drift.append(f"{name} does not protect both project handoff files")

for name in ("docs/system/PROJECT_DOCTOR.md", "prompts/PROJECT_DOCTOR.md"):
    if "Serena" not in text(ROOT / name):
        handoff_drift.append(f"{name} omits Serena from tooling health")

ok("ROADMAP marker + NEXT_SESSION + next prompt, with explicit exceptions") \
    if not handoff_drift else bad("handoff contract drift", handoff_drift)

# ----------------------------------------------- 9. ownership boundary
sect("9. Framework files are outside project-owned directories")
stray = [rel(f) for f in (ROOT / "docs/decisions").glob("ADR-*.md")
         if "Scope: framework decision" in text(f)]
ok("framework ADRs live in .specify/decisions/") if not stray else bad(
    "framework ADR sits in project-owned docs/decisions/ and cannot be updated", stray)

# -------------------------------------------------- 10. required files
sect("10. Repository hygiene")
for f in ["LICENSE", ".gitignore", "docs/phases/README.md",
          "docs/decisions/README.md", "tools/audit.py"]:
    ok(f"{f} present") if (ROOT / f).exists() else bad(f"{f} missing")

# ------------------------------------------------------------ verdict
print("\n" + "-" * 44)
if FAIL:
    print(f"WORKFLOW SELF-AUDIT: NEEDS ATTENTION ({len(FAIL)} failing)")
    sys.exit(1)
print("WORKFLOW SELF-AUDIT: HEALTHY")
