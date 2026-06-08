---
name: "workspace-lint"
description: "Use when the user asks to lint, validate, check, or run deterministic structural checks on a WireNet/Codex workspace."
---

# Workspace Lint

Use this skill for deterministic workspace validation.

Run:

```bash
python3 ../../scripts/workspace_tool.py lint <workspace>
```

Use JSON output when another script or a precise report needs it:

```bash
python3 ../../scripts/workspace_tool.py lint <workspace> --json
```

Remove an empty top-level `tmp/` scratch folder during linting when the user
asks for cleanup:

```bash
python3 ../../scripts/workspace_tool.py lint <workspace> --clean-tmp
```

The linter checks required folders, required identity files, legacy folder
names, workflow fields, review checklist shape, folder-level READMEs, misplaced
facet overview documents or folders, generic catch-all shelves, low-value
generic source folders such as `sources/topics/`, `sources/steering/`, and
`sources/watchlist/`, unknown root folders, and top-level `tmp/` scratch
folders. Empty `tmp/` folders can be removed with `--clean-tmp`; non-empty
`tmp/` folders and other findings are reported for review and are not deleted
automatically.

After linting, explain failures in workspace language and avoid over-fixing
unless the user asked for implementation.
