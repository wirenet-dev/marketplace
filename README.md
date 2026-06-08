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
specs/
  workspace-model/
fixtures/
  empty-workspace/
  valid-workspace/
  broken-workspace/
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

## Shared Model

The cross-agent workspace doctrine lives in `specs/workspace-model/`. Platform
plugins should adapt that model to each agent surface instead of redefining it
inside every marketplace.

The project facet model is:

```text
project.docs/    Obsidian-compatible Markdown workspace
project.code/    deterministic CLI tools and machine-side automation
project.drive/   shareable artifacts for Google Drive-style collaboration
```

Inside `project.docs/`, the baseline folder model is:

```text
identity/    context, preferences, and rules
playbooks/   workflows, methods, and optional agent personas
sources/     source shelf and recurring reading lists
outputs/     drafts, reports, finished work, and preserved artifacts
reviews/     quality checks and guardrails
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
