#!/usr/bin/env python3
"""Validate the local shape of a Codex marketplace root."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate-codex-marketplace.py <marketplace-root>", file=sys.stderr)
        return 2

    root = Path(argv[1]).expanduser().resolve()
    marketplace_path = root / ".agents" / "plugins" / "marketplace.json"
    errors: list[str] = []

    if not marketplace_path.exists():
        errors.append(f"missing marketplace manifest: {marketplace_path}")
    else:
        try:
            marketplace = load_json(marketplace_path)
        except json.JSONDecodeError as exc:
            errors.append(f"invalid marketplace JSON: {exc}")
            marketplace = {}

        if isinstance(marketplace, dict):
            if not marketplace.get("name"):
                errors.append("marketplace is missing name")
            plugins = marketplace.get("plugins")
            if not isinstance(plugins, list):
                errors.append("marketplace plugins must be a list")
                plugins = []

            for index, entry in enumerate(plugins):
                if not isinstance(entry, dict):
                    errors.append(f"plugins[{index}] is not an object")
                    continue
                name = entry.get("name")
                source = entry.get("source")
                policy = entry.get("policy")
                category = entry.get("category")
                if not isinstance(name, str) or not name:
                    errors.append(f"plugins[{index}] is missing name")
                if not isinstance(source, dict):
                    errors.append(f"plugins[{index}] is missing source object")
                    continue
                if source.get("source") != "local":
                    errors.append(f"plugins[{index}] source.source must be local")
                source_path = source.get("path")
                if not isinstance(source_path, str) or not source_path.startswith("./"):
                    errors.append(f"plugins[{index}] source.path must be relative and start with ./")
                    continue
                plugin_root = (root / source_path).resolve()
                plugin_manifest = plugin_root / ".codex-plugin" / "plugin.json"
                if not plugin_manifest.exists():
                    errors.append(f"missing plugin manifest for {name}: {plugin_manifest}")
                    continue
                try:
                    plugin = load_json(plugin_manifest)
                except json.JSONDecodeError as exc:
                    errors.append(f"invalid plugin JSON for {name}: {exc}")
                    continue
                if isinstance(plugin, dict) and plugin.get("name") != name:
                    errors.append(
                        f"plugin manifest name mismatch: marketplace={name} plugin={plugin.get('name')}"
                    )
                if not isinstance(policy, dict):
                    errors.append(f"plugins[{index}] is missing policy")
                else:
                    if policy.get("installation") not in {"AVAILABLE", "NOT_AVAILABLE", "INSTALLED_BY_DEFAULT"}:
                        errors.append(f"plugins[{index}] has invalid policy.installation")
                    if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                        errors.append(f"plugins[{index}] has invalid policy.authentication")
                if not isinstance(category, str) or not category:
                    errors.append(f"plugins[{index}] is missing category")
        else:
            errors.append("marketplace manifest root must be an object")

    if errors:
        print("Codex marketplace validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Codex marketplace OK: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

