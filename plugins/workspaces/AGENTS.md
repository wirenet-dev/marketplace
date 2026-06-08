# Workspaces Plugin - Agent Entry Point

This plugin provides WireNet workspace skills for Codex.

## Read Order

1. `README.md`
2. `.codex-plugin/plugin.json`
3. `specs/workspace-model/folder-model.md`
4. `specs/workspace-model/project-facets.md`
5. `specs/workspace-model/every-alignment.md`
6. The relevant skill under `skills/`

## Plugin Rules

- Keep Workspaces-specific doctrine under `specs/`.
- Keep Workspaces test fixtures under `fixtures/`.
- Keep deterministic helpers under `scripts/`.
- Keep generated skill templates under `assets/templates/`.
- Model knowledge-work projects as `.docs`, `.code`, and `.drive` facets when
  all three surfaces are useful.
- Keep the Every-inspired base model small: `identity/`, `playbooks/`,
  `sources/`, `outputs/`, and `reviews/`.
- Label WireNet extensions clearly, especially `.code` CLI tooling and `.drive`
  shareable artifacts.
- Do not duplicate the full workspace model in every skill. Put shared doctrine
  in references or specs and link to it.

## Validation

From the repository root:

```bash
python3 tools/validate-codex-marketplace.py .
python3 /Users/gitt/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/workspaces
```
