# Project Code Facet

Add a paired `project.code/` folder only when the workspace needs automation,
validation, rendering, scheduled runs, structured state, tests, generated files,
reusable scripts, or deterministic CLI tools.

Recommended split:

```text
project.docs/
  human-readable identity, playbooks, sources, outputs, reviews

project.code/
  automation code, tests, templates, compiled state, build commands

project.drive/
  shareable Docs, Slides, Sheets, PDFs, exports, and handoff artifacts
```

When useful, expose code-repo behavior through named CLI commands rather than
requiring an agent to reconstruct one-off shell procedures. Good CLI tools are
small, composable, documented, and testable. They should accept clear inputs,
produce predictable outputs, and be safe to call from multiple workflows.

Document these commands in the paired code repo's `AGENTS.md`, including what
each command reads, writes, validates, and whether it requires approval.
Reference the relevant commands from `playbooks/workflows/`.

Keep generated shareable artifacts in `project.drive/` when they are intended
for Google Drive or external collaboration. Keep durable source context and
workflow rules in `project.docs/`, and keep automation internals in
`project.code/`.
