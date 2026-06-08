#!/usr/bin/env python3
"""Inspect, lint, and scaffold WireNet-style workspaces."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_DIRS = ["identity", "playbooks", "sources", "outputs", "reviews"]
REQUIRED_IDENTITY_FILES = ["context.md", "preferences.md", "rules.md"]
TMP_DIR_NAME = "tmp"
INBOX_DIR_NAME = "inbox"
OVERVIEWS_DIR_NAME = "overviews"
LEGACY_DIRS = {
    "depeche": "identity",
    "vademecum": "playbooks",
    "controle": "reviews",
    "review": "reviews",
}
WORKFLOW_FIELDS = [
    "Purpose:",
    "Trigger or cadence:",
    "Input sources:",
    "Output artifact:",
    "Machine state:",
    "CLI tools:",
    "Steps:",
    "Approval rules:",
    "What the agent may do without asking:",
    "What the agent must ask before doing:",
    "Verification steps:",
    "Review checklist:",
    "Where the final output lives:",
    "When to retire or revise this workflow:",
]
GENERIC_SHELVES = [
    ("sources/sources", "sources/_sources"),
    ("outputs/outputs", "outputs/_outputs"),
]
LOW_VALUE_SOURCE_FOLDERS = [
    (
        "sources/topics",
        "topic maps usually belong as flat sources/*.md files unless the folder has enough durable material",
    ),
    (
        "sources/steering",
        "source steering usually belongs in a compact sources/*.md file unless the folder has enough durable material",
    ),
    (
        "sources/watchlist",
        "watchlist links usually belong in sources/key-links.md unless the folder has enough durable material",
    ),
]
ALLOWED_ROOT_DIRS = set(REQUIRED_DIRS) | {INBOX_DIR_NAME, OVERVIEWS_DIR_NAME, TMP_DIR_NAME}
KNOWN_ROOT_DIRS = ALLOWED_ROOT_DIRS | set(LEGACY_DIRS)


def project_facets(root: Path) -> dict[str, str | bool]:
    """Return sibling project facet paths for a .docs/.code/.drive project."""
    name = root.name
    parent = root.parent
    suffixes = [".docs", ".code", ".drive"]
    base = name
    active = ""
    for suffix in suffixes:
        if name.endswith(suffix):
            base = name[: -len(suffix)]
            active = suffix[1:]
            break
    return {
        "base": base,
        "active": active,
        "docs": str(parent / f"{base}.docs"),
        "docs_exists": (parent / f"{base}.docs").is_dir(),
        "code": str(parent / f"{base}.code"),
        "code_exists": (parent / f"{base}.code").is_dir(),
        "drive": str(parent / f"{base}.drive"),
        "drive_exists": (parent / f"{base}.drive").is_dir(),
    }


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "untitled"


def template_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "templates"


def read_template(name: str) -> str:
    path = template_dir() / name
    return path.read_text(encoding="utf-8")


def finding(level: str, message: str, path: Path | None = None) -> dict[str, str]:
    item = {"level": level, "message": message}
    if path is not None:
        item["path"] = str(path)
    return item


def tmp_status(root: Path) -> dict[str, object]:
    path = root / TMP_DIR_NAME
    exists = path.exists()
    is_dir = path.is_dir()
    item_count = 0
    sample_items: list[str] = []
    if is_dir:
        items = sorted(path.iterdir(), key=lambda item: item.name)
        item_count = len(items)
        sample_items = [item.name for item in items[:10]]
    return {
        "exists": exists,
        "is_dir": is_dir,
        "item_count": item_count,
        "sample_items": sample_items,
    }


def folder_status(root: Path, name: str) -> dict[str, object]:
    path = root / name
    exists = path.exists()
    is_dir = path.is_dir()
    item_count = 0
    sample_items: list[str] = []
    if is_dir:
        items = sorted(path.iterdir(), key=lambda item: item.name)
        item_count = len(items)
        sample_items = [item.name for item in items[:10]]
    return {
        "exists": exists,
        "is_dir": is_dir,
        "item_count": item_count,
        "sample_items": sample_items,
    }


def folder_readmes(root: Path) -> list[str]:
    root_readme = (root / "README.md").resolve()
    readmes: list[str] = []
    for path in sorted(root.rglob("README.md")):
        if path.resolve() == root_readme:
            continue
        readmes.append(str(path))
    return readmes


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if any(part.startswith(".") for part in relative.parts):
            continue
        files.append(path)
    return files


def facet_overview_files(root: Path) -> list[str]:
    files: list[str] = []
    for path in markdown_files(root):
        relative = path.relative_to(root)
        parts = [part.lower() for part in relative.parts]
        if "facet" not in path.stem.lower():
            continue
        if "identity" in parts or any("overview" in part for part in parts):
            files.append(str(path))
    return files


def misplaced_overview_paths(root: Path) -> list[str]:
    paths: list[str] = []
    for name in [OVERVIEWS_DIR_NAME, "overview"]:
        path = root / "identity" / name
        if path.exists():
            paths.append(str(path))
    return paths


def unknown_root_dirs(root: Path) -> list[str]:
    if not root.is_dir():
        return []
    dirs: list[str] = []
    for path in sorted(root.iterdir(), key=lambda item: item.name):
        if not path.is_dir():
            continue
        if path.name.startswith("."):
            continue
        if path.name in KNOWN_ROOT_DIRS:
            continue
        dirs.append(str(path))
    return dirs


def inspect_workspace(root: Path) -> dict[str, object]:
    root = root.resolve()
    return {
        "path": str(root),
        "exists": root.exists(),
        "project_facets": project_facets(root),
        "required_dirs": {name: (root / name).is_dir() for name in REQUIRED_DIRS},
        "identity_files": {
            name: (root / "identity" / name).is_file() for name in REQUIRED_IDENTITY_FILES
        },
        "legacy_dirs": {
            old: (root / old).is_dir() for old in LEGACY_DIRS
        },
        "facet_overview_files": facet_overview_files(root),
        "folder_readmes": folder_readmes(root),
        "inbox": folder_status(root, INBOX_DIR_NAME),
        "has_overviews": (root / OVERVIEWS_DIR_NAME).is_dir(),
        "misplaced_overviews": misplaced_overview_paths(root),
        "tmp": tmp_status(root),
        "unknown_root_dirs": unknown_root_dirs(root),
        "has_readme": (root / "README.md").is_file(),
        "has_agents": (root / "AGENTS.md").is_file(),
    }


def lint_workspace(root: Path, clean_tmp: bool = False) -> list[dict[str, str]]:
    root = root.resolve()
    findings: list[dict[str, str]] = []

    if not root.exists():
        return [finding("error", "workspace path does not exist", root)]

    for name in REQUIRED_DIRS:
        path = root / name
        if not path.is_dir():
            findings.append(finding("error", f"missing required folder: {name}/", path))

    for old, new in LEGACY_DIRS.items():
        path = root / old
        if path.is_dir():
            findings.append(finding("error", f"legacy folder {old}/ should be {new}/", path))

    for name in REQUIRED_IDENTITY_FILES:
        path = root / "identity" / name
        if not path.is_file():
            findings.append(finding("error", f"missing identity file: identity/{name}", path))

    if not (root / "README.md").is_file():
        findings.append(finding("warning", "missing human-facing README.md", root / "README.md"))
    if not (root / "AGENTS.md").is_file():
        findings.append(finding("warning", "missing agent-facing AGENTS.md", root / "AGENTS.md"))

    for readme in folder_readmes(root):
        findings.append(
            finding(
                "warning",
                "folder-level README should be moved into root README.md or AGENTS.md",
                Path(readme),
            )
        )

    for overview in facet_overview_files(root):
        findings.append(
            finding(
                "warning",
                "facet map should live in AGENTS.md, not an identity or overview document",
                Path(overview),
            )
        )

    for overview_path in misplaced_overview_paths(root):
        findings.append(
            finding(
                "warning",
                "move identity overview folder to root-level overviews/",
                Path(overview_path),
            )
        )

    for relative, replacement in GENERIC_SHELVES:
        path = root / relative
        if path.exists():
            findings.append(
                finding(
                    "warning",
                    f"generic catch-all shelf should be triaged into {replacement}",
                    path,
                )
            )

    for relative, guidance in LOW_VALUE_SOURCE_FOLDERS:
        path = root / relative
        if path.is_dir():
            findings.append(finding("warning", guidance, path))

    for path in unknown_root_dirs(root):
        findings.append(
            finding(
                "warning",
                "unknown root folder; triage into inbox/, sources/, playbooks/, outputs/, reviews/, or overviews/",
                Path(path),
            )
        )

    tmp_path = root / TMP_DIR_NAME
    if tmp_path.exists():
        if not tmp_path.is_dir():
            findings.append(
                finding("warning", "tmp exists but is not a folder; inspect before removing", tmp_path)
            )
        else:
            tmp_items = sorted(tmp_path.iterdir(), key=lambda item: item.name)
            if tmp_items:
                findings.append(
                    finding(
                        "warning",
                        f"tmp/ contains {len(tmp_items)} scratch item(s); review and delete when no longer needed",
                        tmp_path,
                    )
                )
            elif clean_tmp:
                tmp_path.rmdir()
                findings.append(finding("info", "removed empty tmp/ scratch folder", tmp_path))
            else:
                findings.append(
                    finding(
                        "warning",
                        "empty tmp/ scratch folder can be removed with lint --clean-tmp",
                        tmp_path,
                    )
                )

    facets = project_facets(root)
    if root.name.endswith(".docs"):
        if facets["code_exists"]:
            code_agents = Path(str(facets["code"])) / "AGENTS.md"
            if not code_agents.is_file():
                findings.append(
                    finding("warning", ".code facet exists but is missing AGENTS.md", code_agents)
                )

    workflows_dir = root / "playbooks" / "workflows"
    if workflows_dir.is_dir():
        for workflow in sorted(workflows_dir.glob("*.md")):
            text = workflow.read_text(encoding="utf-8")
            for field in WORKFLOW_FIELDS:
                if field not in text:
                    findings.append(
                        finding("warning", f"workflow missing field {field}", workflow)
                    )

    reviews_dir = root / "reviews"
    if reviews_dir.is_dir():
        for review in sorted(reviews_dir.glob("*.md")):
            text = review.read_text(encoding="utf-8")
            if "Use this before:" not in text:
                findings.append(
                    finding("warning", "review checklist missing 'Use this before:'", review)
                )

    return findings


def write_file(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def create_from_template(root: Path, section: str, name: str, template: str, force: bool) -> Path:
    slug = slugify(name)
    path = root.resolve() / section / f"{slug}.md"
    text = read_template(template)
    write_file(path, text, force)
    return path


def print_result(payload: object, as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    elif isinstance(payload, list):
        if not payload:
            print("No findings.")
        else:
            for item in payload:
                path = f" ({item['path']})" if "path" in item else ""
                print(f"[{item['level']}] {item['message']}{path}")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    inspect = sub.add_parser("inspect")
    inspect.add_argument("path")
    inspect.add_argument("--json", action="store_true")

    lint = sub.add_parser("lint")
    lint.add_argument("path")
    lint.add_argument("--json", action="store_true")
    lint.add_argument(
        "--clean-tmp",
        action="store_true",
        help="remove an empty top-level tmp/ scratch folder before reporting",
    )

    create_commands = {
        "create-workflow": ("playbooks/workflows", "workflow.md"),
        "create-method": ("playbooks/methods", "method.md"),
        "create-review": ("reviews", "review-checklist.md"),
        "create-agent": ("playbooks/agents", "agent-persona.md"),
    }
    for command in create_commands:
        child = sub.add_parser(command)
        child.add_argument("path")
        child.add_argument("--name", required=True)
        child.add_argument("--force", action="store_true")
        child.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    root = Path(args.path)

    if args.command == "inspect":
        print_result(inspect_workspace(root), args.json)
        return 0
    if args.command == "lint":
        findings = lint_workspace(root, clean_tmp=args.clean_tmp)
        print_result(findings, args.json)
        return 1 if any(item["level"] == "error" for item in findings) else 0

    section, template = create_commands[args.command]
    try:
        created = create_from_template(root, section, args.name, template, args.force)
    except FileExistsError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    payload = {"created": str(created)}
    print_result(payload, args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
