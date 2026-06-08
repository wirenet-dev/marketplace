# WireNet Marketplace

WireNet Marketplace is the public home for WireNet Codex plugins. It is kept
small on purpose: the marketplace root tells Codex where the plugins are, while
each plugin carries its own skills, scripts, templates, fixtures, and
documentation.

The first plugin is **Workspaces**, a knowledge-work plugin for turning loose
folders into durable human-agent workspaces.

## What Is Here

This repository currently provides:

- a Codex marketplace manifest at `.agents/plugins/marketplace.json`;
- the Workspaces plugin under `plugins/workspaces/`;
- validation helpers under `tools/`.

The marketplace itself does not define workspace doctrine. It points Codex to
the plugin, and the plugin explains its own model.

## Available Plugin

### Workspaces

`workspaces` helps agents set up, audit, lint, extend, and operate
WireNet-style knowledge-work folders.

Use it for work that needs a stable place for:

- identity and standing context;
- reusable workflows and methods;
- source material and recurring links;
- drafts, reports, and finished outputs;
- review checklists and guardrails.

The plugin documentation lives in:

```text
plugins/workspaces/README.md
```

## Install

Install this marketplace from GitHub with:

```bash
codex plugin marketplace add wirenet-dev/marketplace
```

After the marketplace is installed, Codex can install or update the plugins
listed in `.agents/plugins/marketplace.json`.

## Repository Layout

```text
.agents/
  plugins/
    marketplace.json        Codex marketplace manifest
plugins/
  workspaces/               Workspaces plugin bundle
tools/
  validate-codex-marketplace.py
```

The Workspaces plugin has its own manifest, skills, scripts, templates, specs,
and fixtures inside `plugins/workspaces/`.

## Development

When changing the marketplace manifest or plugin layout, validate the
marketplace from the repository root:

```bash
python3 tools/validate-codex-marketplace.py .
```

When changing the Workspaces plugin itself, also validate the plugin bundle:

```bash
python3 /Users/gitt/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/workspaces
```

For workspace-specific linting, use the helper shipped by the Workspaces
plugin:

```bash
python3 plugins/workspaces/scripts/workspace_tool.py lint /path/to/workspace
```

## Documentation

The root README documents the marketplace. Plugin READMEs document individual
plugins. Skill behavior lives with each plugin so the marketplace stays clean
and easy to scan.
