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
   - optional `inbox/` only when a single catch-all is useful
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
5. Keep README and `AGENTS.md` local. Do not copy generic plugin conventions,
   folder role explanations, workflow templates, method templates, or review
   templates into them.
6. Add the default write boundary to `AGENTS.md`: the agent may read across the
   system for relevant context, but may write or edit only inside the workspace
   unless the user explicitly says otherwise.
7. If a `.code` or `.drive` facet exists or is clearly useful, document the
   facet split, sibling paths, and source-of-truth rules in `AGENTS.md`.
8. If deterministic workflow steps are needed, prefer named CLI tools in
   `project.code/` and reference them from `playbooks/workflows/`.
9. If shareable Google Drive artifacts are needed, use `project.drive/` for
   Docs, Slides, Sheets, PDFs, exports, and handoff artifacts.
10. Do not overwrite user material without explicit approval.

## Validation

After setup, run:

```bash
python3 ../../scripts/workspace_tool.py lint <workspace>
```

Summarize what was created, where the entry points are, and which human
decisions remain.
