---
name: "workspace-audit"
description: "Use when the user asks to audit, inspect, review, assess, or diagnose whether a workspace follows WireNet/Codex workspace conventions."
---

# Workspace Audit

Use this skill to inspect a workspace and produce practical cleanup
recommendations.

Read `../workspace/references/codex-workspace-setup.md` for the canonical model.

## Audit Checks

Check:

- `README.md` is human-facing and concise.
- `AGENTS.md` gives read order, boundaries, paired repo details, and commands.
- `identity/` contains context, preferences, and rules.
- `playbooks/` contains process, not source material or finished work.
- `sources/` contains inputs and evidence.
- `outputs/` contains records, drafts, reports, or finished artifacts.
- `reviews/` contains concrete checklist-style guardrails.
- `.docs` is Obsidian-compatible and holds durable workspace context.
- `.code` holds deterministic CLI tools, scripts, tests, and machine state.
- `.drive` holds shareable Docs, Slides, Sheets, PDFs, exports, and handoffs.
- machine-only state lives in `.code` or a state store.
- deterministic recurring steps are exposed through documented CLI tools.

## Workflow

1. Read `README.md` and `AGENTS.md` if present.
2. Inspect top-level folders and representative files.
3. Run the bundled linter when useful:

```bash
python3 ../../scripts/workspace_tool.py lint <workspace>
```

4. Lead with the most important mismatches or risks.
5. Give a short cleanup path. If the user asked for implementation, make the
   smallest coherent changes and validate again.
