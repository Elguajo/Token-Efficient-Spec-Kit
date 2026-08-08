#!/usr/bin/env python3
"""Build the minimal Token-Efficient Spec Kit Starter release asset.

The source repository contains maintainer documentation, release history and
contribution files. A generated Starter must contain only the workflow needed by
a downstream project. The allowlist lives in starter/MANIFEST.txt so reviewing a
distribution change never requires inferring it from packaging code.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import sys
import tempfile
import zipfile


ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "starter" / "MANIFEST.txt"
STARTER_README = ROOT / "starter" / "README.md"
FORBIDDEN_PATHS = {
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "README_EN.md",
    "VERSION",
    "docs/MAINTENANCE.md",
    "docs/README.md",
    "docs/USAGE_GUIDE.md",
    "docs/VISUAL_GUIDE.md",
    "docs/WORKFLOW.md",
    ".github/ISSUE_TEMPLATE",
    ".github/PULL_REQUEST_TEMPLATE.md",
}
REQUIRED_PATHS = {
    "README.md",
    "AGENTS.md",
    ".specify/memory/constitution.md",
    ".token-efficient-spec-kit/VERSION",
    "prompts/START_NEW_PROJECT.md",
    "docs/project/ROADMAP.md",
    "docs/system/WORKFLOW_UPDATE_POLICY.md",
    "integrations/PROFILES.md",
    "templates/PROJECT_BRIEF.template.md",
    "tools/audit.py",
    ".github/workflows/audit.yml",
}


def read_version() -> str:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError(f"Invalid source VERSION: {version!r}")
    return version


def manifest_entries() -> list[str]:
    entries: list[str] = []
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        entry = raw.strip()
        if not entry or entry.startswith("#"):
            continue
        if entry.startswith("/") or ".." in pathlib.PurePosixPath(entry).parts:
            raise ValueError(f"Unsafe starter manifest entry: {entry}")
        if entry in entries:
            raise ValueError(f"Duplicate starter manifest entry: {entry}")
        entries.append(entry)
    if not entries:
        raise ValueError("Starter manifest is empty")
    return entries


def copy_entry(entry: str, destination: pathlib.Path) -> None:
    source = ROOT / entry.rstrip("/")
    if not source.exists():
        raise FileNotFoundError(f"Starter manifest path does not exist: {entry}")
    target = destination / source.relative_to(ROOT)
    if entry.endswith("/"):
        if not source.is_dir():
            raise ValueError(f"Starter manifest directory entry is not a directory: {entry}")
        shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))
    elif source.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    else:
        raise ValueError(f"Starter manifest file entry is not a file: {entry}")


def stage(destination: pathlib.Path, version: str) -> None:
    for entry in manifest_entries():
        copy_entry(entry, destination)

    shutil.copy2(STARTER_README, destination / "README.md")
    metadata = destination / ".token-efficient-spec-kit"
    metadata.mkdir(parents=True, exist_ok=True)
    (metadata / "VERSION").write_text(f"{version}\n", encoding="utf-8")


def validate_staged(staged: pathlib.Path) -> None:
    missing = sorted(path for path in REQUIRED_PATHS if not (staged / path).exists())
    if missing:
        raise ValueError("Starter is missing required paths: " + ", ".join(missing))
    leaked = sorted(path for path in FORBIDDEN_PATHS if (staged / path).exists())
    if leaked:
        raise ValueError("Starter contains source-only paths: " + ", ".join(leaked))


def write_zip(staged: pathlib.Path, output: pathlib.Path, version: str) -> None:
    prefix = f"token-efficient-spec-kit-starter-{version}"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(staged.rglob("*")):
            if path.is_file():
                archive.write(path, pathlib.Path(prefix) / path.relative_to(staged))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        help="Destination ZIP. Defaults to dist/token-efficient-spec-kit-starter-<version>.zip.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing destination ZIP.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    version = read_version()
    output = args.output or ROOT / "dist" / f"token-efficient-spec-kit-starter-{version}.zip"
    output = output if output.is_absolute() else ROOT / output
    if output.exists() and not args.overwrite:
        print(f"Refusing to overwrite existing artifact: {output}", file=sys.stderr)
        return 2
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="tesk-starter-") as temporary:
        staged = pathlib.Path(temporary) / "starter"
        staged.mkdir()
        stage(staged, version)
        validate_staged(staged)
        write_zip(staged, output, version)

    print(f"Starter artifact: {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError) as error:
        print(f"Starter build failed: {error}", file=sys.stderr)
        raise SystemExit(1)
