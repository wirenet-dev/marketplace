# WireNet Marketplace - Agent Entry Point

This repo hosts WireNet marketplace plugins for coding agents.

## Read Order

1. `README.md`
2. `specs/workspace-model/folder-model.md`
3. `specs/workspace-model/project-facets.md`
4. `.agents/plugins/marketplace.json`
5. The relevant plugin manifest and skills

## Repo Rules

- Keep the active Codex marketplace packaging at the repository root so GitHub
  installs work with `codex plugin marketplace add wirenet-dev/marketplace`.
- Keep cross-agent doctrine under `specs/`.
- Model knowledge-work projects as `.docs`, `.code`, and `.drive` facets when
  all three surfaces are useful.
- Keep test fixtures under `fixtures/`.
- Keep repository maintenance scripts under `tools/`.
- Do not duplicate the full workspace model in every skill. Put shared doctrine
  in references or specs and link to it.
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
