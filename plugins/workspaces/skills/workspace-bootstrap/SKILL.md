---
name: "workspace-bootstrap"
description: "Use when the user asks to bootstrap, initialize, set up, scaffold, or fill in a WireNet/Codex knowledge-work workspace with identity, playbooks, sources, outputs, and reviews."
---

# Workspace Bootstrap

Use this skill to create or complete a workspace.

Read `../workspace/references/codex-workspace-setup.md` before making structural
changes.

## Workflow

1. Inspect the target folder first.
2. Create the smallest useful structure:
   - `README.md`
   - `AGENTS.md`
   - `identity/context.md`
   - `identity/preferences.md`
   - `identity/rules.md`
   - `playbooks/`
   - `sources/`
   - `outputs/`
   - `reviews/`
3. Avoid empty scaffolding unless the user wants a reusable template.
4. If the project needs an Obsidian-compatible docs facet, use `project.docs/`
   as the workspace folder.
5. If a `.code` facet exists or is clearly useful, document it in `AGENTS.md`.
6. If deterministic workflow steps are needed, prefer named CLI tools in
   `project.code/` and reference them from `playbooks/workflows/`.
7. If shareable Google Drive artifacts are needed, use `project.drive/` for
   Docs, Slides, Sheets, PDFs, exports, and handoff artifacts.
8. Do not overwrite user material without explicit approval.

## Validation

After setup, run:

```bash
python3 ../../scripts/workspace_tool.py lint <workspace>
```

Summarize what was created, where the entry points are, and which human
decisions remain.
