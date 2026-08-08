#!/usr/bin/env python3
"""Token-Efficient Spec Kit - machine-checkable workflow self-audit.

Produces evidence, not an opinion. Constitution section 9 requires evidence before
claims, so prompts/AUDIT_WORKFLOW.md and prompts/UPDATE_WORKFLOW.md must cite this
script's output instead of asserting HEALTHY on their own.

Usage: python3 tools/audit.py    (exit 0 = HEALTHY, 1 = NEEDS ATTENTION)
"""
import os, re, sys, pathlib

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
RS = ["docs/project/PROJECT_BRIEF.md", "docs/project/ARCHITECTURE.md",
      "docs/project/ROADMAP.md", "docs/system/ENGINEERING_RULES.md",
      ".specify/memory/constitution.md"]
CANON = "docs/system/TOKEN_EFFICIENCY.md"
dupes = []
for p in MD:
    if rel(p) == CANON: continue
    lines = text(p).splitlines()
    for i, ln in enumerate(lines):
        # a read instruction followed by an enumerated block
        if not re.search(r"\bread\b", ln, re.I): continue
        window = "\n".join(lines[i:i + 14])
        hits = sum(1 for r in RS if r in window)
        if hits >= 4:
            dupes.append(f"{rel(p)}:{i+1} enumerates {hits}/5 read-set paths")
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
    if not any(all(t in b for t in TOOLS) for b in re.findall(r"```[a-z]*\n(.*?)```", body, re.S)):
        continue
    if "PROFILES.md" not in body:
        orphans.append(f"{rel(p_)} enumerates the profile without pointing at {PROF_CANON}")
ok(f"all profile listings reference {PROF_CANON}") if not orphans else bad(
    "profile enumerated with no pointer to canonical; ADR-001 went stale this way", orphans)

# ------------------------------------------------- 5. phase file names
sect("5. Phase files follow docs/phases/NN-kebab-name.md")
bad_names = [rel(f) for f in (ROOT / "docs/phases").glob("*.md")
             if f.name != "README.md"
             and not re.fullmatch(r"\d{2}-[a-z0-9]+(-[a-z0-9]+)*\.md", f.name)]
ok("phase file names valid") if not bad_names else bad(
    "phase file names violate the convention", bad_names)

# --------------------------------------------- 6. current-phase marker
sect("6. ROADMAP marks exactly one current phase")
rm = text(ROOT / "docs/project/ROADMAP.md")
if "Not initialized" in rm:
    ok("roadmap not initialized yet (template repository)")
else:
    cur = len(re.findall(r"^\s*-\s*\[>\]", rm, re.M))
    pend = len(re.findall(r"^\s*-\s*\[ \]", rm, re.M))
    if cur == 1: ok("exactly one [>] phase")
    elif cur == 0 and pend == 0: ok("all phases complete")
    else: bad(f"{cur} phases marked [>]; expected exactly 1")

# ----------------------------------------------- 7. ownership boundary
sect("7. Framework files are outside project-owned directories")
stray = [rel(f) for f in (ROOT / "docs/decisions").glob("ADR-*.md")
         if "Scope: framework decision" in text(f)]
ok("framework ADRs live in .specify/decisions/") if not stray else bad(
    "framework ADR sits in project-owned docs/decisions/ and cannot be updated", stray)

# --------------------------------------------------- 8. required files
sect("8. Repository hygiene")
for f in ["LICENSE", ".gitignore", "docs/phases/README.md",
          "docs/decisions/README.md", "tools/audit.py"]:
    ok(f"{f} present") if (ROOT / f).exists() else bad(f"{f} missing")

# ------------------------------------------------------------ verdict
print("\n" + "-" * 44)
if FAIL:
    print(f"WORKFLOW SELF-AUDIT: NEEDS ATTENTION ({len(FAIL)} failing)")
    sys.exit(1)
print("WORKFLOW SELF-AUDIT: HEALTHY")
