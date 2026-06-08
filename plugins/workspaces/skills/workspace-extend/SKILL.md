---
name: "workspace-extend"
description: "Use when the user asks to extend a workspace with a new area, source shelf, output type, workflow family, review layer, overview, .code facet, or .drive facet."
---

# Workspace Extend

Use this skill to add a coherent new part to an existing workspace.

Read `../workspace/references/codex-workspace-setup.md` before changing
structure.

## Extension Rules

- Add the smallest structure that supports real work.
- Prefer domain-specific folder names over generic shelves.
- Prefer flat `sources/*.md` topic maps and `sources/key-links.md` watchlists
  over generic source folders such as `topics/`, `steering/`, or `watchlist/`.
- Keep sources, outputs, reviews, playbooks, and machine state separate.
- Add optional root-level `overviews/` only after there are files worth
  tabulating.
- Use optional root-level `inbox/` for loose human notes and untriaged mixed
  material.
- Use `sources/_sources/` for new source material when the user has not named a
  destination.
- Use `outputs/_outputs/` for produced artifacts that do not fit a more specific
  output shelf.
- Add a `.code` facet only when automation, validation, rendering, scheduled
  runs, structured state, tests, or CLI tools are useful.
- Add a `.drive` facet only when shareable Docs, Slides, Sheets, PDFs, exports,
  or handoff artifacts are useful.
- Put facet boundaries, sibling paths, commands, and source-of-truth rules in
  `AGENTS.md`.
- Update `README.md` and `AGENTS.md` when the extension changes how the
  workspace should be used.

Run the linter after structural changes:

```bash
python3 ../../scripts/workspace_tool.py lint <workspace>
```
