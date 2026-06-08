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

The linter checks required folders, required identity files, legacy folder
names, workflow fields, and review checklist shape.

After linting, explain failures in workspace language and avoid over-fixing
unless the user asked for implementation.

