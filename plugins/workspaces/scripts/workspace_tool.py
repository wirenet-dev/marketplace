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
        "has_readme": (root / "README.md").is_file(),
        "has_agents": (root / "AGENTS.md").is_file(),
    }


def lint_workspace(root: Path) -> list[dict[str, str]]:
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

    facets = project_facets(root)
    if root.name.endswith(".docs"):
        if facets["code_exists"]:
            code_agents = Path(str(facets["code"])) / "AGENTS.md"
            if not code_agents.is_file():
                findings.append(
                    finding("warning", ".code facet exists but is missing AGENTS.md", code_agents)
                )
        if facets["drive_exists"]:
            drive_readme = Path(str(facets["drive"])) / "README.md"
            if not drive_readme.is_file():
                findings.append(
                    finding("warning", ".drive facet exists but is missing README.md", drive_readme)
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
    title = name.strip() or slug.replace("-", " ").title()
    text = text.replace("Workflow Name", title)
    text = text.replace("Method Name", title)
    text = text.replace("Review Name", title)
    text = text.replace("Agent Persona", title)
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

    for command in ["inspect", "lint"]:
        child = sub.add_parser(command)
        child.add_argument("path")
        child.add_argument("--json", action="store_true")

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
        findings = lint_workspace(root)
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
