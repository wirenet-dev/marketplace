# WireNet Marketplace

WireNet Marketplace is the home for WireNet plugins, skills, and workflow
extensions for coding agents.

The first supported platform is Codex. The repository root is the Codex
marketplace root, so it can be installed directly from GitHub.

## Layout

```text
.agents/
  plugins/
    marketplace.json
plugins/
  workspaces/
tools/
```

## Codex Marketplace

The Codex marketplace root is this repository root.

```text
.
```

Its marketplace manifest is:

```text
.agents/plugins/marketplace.json
```

The first plugin is `workspaces`, which gives Codex modular capabilities for
setting up, auditing, linting, extending, and working in WireNet-style knowledge
workspaces.

The Workspaces plugin owns its own doctrine, fixtures, skills, scripts, and
assets under:

```
plugins/workspaces/
```

## Development

Use the Codex validation helper to check the local Codex marketplace:

```bash
python3 tools/validate-codex-marketplace.py .
```

Use the Workspaces plugin CLI to inspect or lint a workspace:

```bash
python3 plugins/workspaces/scripts/workspace_tool.py lint /path/to/workspace
```

Install the marketplace from GitHub:

```bash
codex plugin marketplace add wirenet-dev/marketplace
```
