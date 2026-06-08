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
- `AGENTS.md` gives read order, boundaries, paired repo details, and commands,
  including the default rule that the agent may read across the system but may
  write or edit only inside the workspace unless the user explicitly says
  otherwise.
- README and `AGENTS.md` add local context instead of restating plugin-provided
  folder roles, workflow templates, method templates, review templates, or
  generic workspace doctrine.
- `inbox/`, if present, is the single temporary catch-all and not a source of
  truth.
- `identity/` contains context, preferences, and rules.
- `overviews/`, if present, is root-level and contains scan views, not source
  of truth or agent routing.
- `playbooks/` contains process, not source material or finished work.
- `sources/` contains inputs and evidence.
- `sources/` stays mostly flat: recurring links live in `key-links.md`,
  recurring local inputs live in `recurring-docs.md`, and generic folders such
  as `topics/`, `steering/`, or `watchlist/` are avoided unless deliberate.
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
