# WireNet Marketplace - Agent Entry Point

This repo hosts WireNet marketplace plugins for coding agents.

## Read Order

1. `README.md`
2. `.agents/plugins/marketplace.json`
3. The relevant plugin `AGENTS.md`
4. The relevant plugin manifest and skills

## Repo Rules

- Keep the active Codex marketplace packaging at the repository root so GitHub
  installs work with `codex plugin marketplace add wirenet-dev/marketplace`.
- Keep plugin-specific doctrine, fixtures, scripts, skills, and assets inside
  the owning plugin under `plugins/<plugin>/`.
- Keep repository maintenance scripts under `tools/`.
- For Codex plugins, keep `.codex-plugin/plugin.json` and
  `.agents/plugins/marketplace.json` valid.
- Prefer small deterministic scripts for linting, scaffolding, and path checks.
- Do not delete or overwrite user-authored plugin or spec material without
  explicit approval.

## Codex Marketplace

The active Codex marketplace root is:

`.`

The active Codex Workspaces plugin is:

`plugins/workspaces`

Validate the Codex marketplace after structural changes:

```bash
python3 tools/validate-codex-marketplace.py .
```

Validate the Workspaces plugin itself with the bundled plugin-creator validator
when it is available:

```bash
python3 /Users/gitt/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/workspaces
```
