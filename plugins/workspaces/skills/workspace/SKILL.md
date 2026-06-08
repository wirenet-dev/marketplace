---
name: "workspace"
description: "Use when the user explicitly asks for the workspace skill, or asks to set up, audit, refactor, or align a Codex knowledge-work workspace using Florian's identity, playbooks, sources, outputs, and reviews conventions."
---

# Workspace Skill

## When To Use

Use this skill when the user says "workspace skill" or asks to:

- set up a new Codex workspace for a kind of work,
- audit whether the current workspace follows the conventions,
- refactor an existing project into the standard structure,
- explain or apply the `identity/`, `playbooks/`, `sources/`, `outputs/`, and
  `reviews/` model.

## Core Model

Default workspace shape:

```text
project.docs/  Obsidian-compatible Markdown workspace
project.code/  deterministic CLI tools, scripts, tests, and machine state
project.drive/ shareable Docs, Slides, Sheets, PDFs, exports, and handoffs
```

Inside `project.docs/`:

```text
identity/    context files: who, what, preferences, and rules
playbooks/   process: repeatable workflows and reusable instructions
sources/     source shelf: inputs, evidence, references, and key links
outputs/     drafts, finished artifacts, reports, and preserved work
reviews/     quality checks, guardrails, and review checklists
```

Use the bundled reference for the full setup guide:

`references/codex-workspace-setup.md`

Read it before creating files, auditing a real workspace, or making structural
recommendations beyond a short answer.

## Related Workspace Skills

This skill is the core/router skill. Prefer the narrower skill when the user
asks for a specific workspace operation:

- `workspace-bootstrap`: create a new workspace or fill in a partial one.
- `workspace-audit`: inspect a workspace and recommend structural fixes.
- `workspace-lint`: run deterministic checks with the bundled CLI.
- `workspace-extend`: add a new area, source shelf, output type, or paired repo.
- `workspace-workflow`: create or refine `playbooks/workflows/`.
- `workspace-method`: create reusable `playbooks/methods/`.
- `workspace-review`: create `reviews/` checklists.
- `workspace-agent`: create optional `playbooks/agents/` personas.

## Setup Workflow

1. Inspect the current folder first: existing files, naming patterns, project
   purpose, and whether `.docs`, `.code`, or `.drive` facets exist.
2. Identify the smallest useful structure. Avoid empty scaffolding unless the
   user explicitly wants a reusable template.
3. Create or update:
   - `README.md` for humans,
   - `AGENTS.md` for agent entry instructions,
   - `identity/context.md`, `identity/preferences.md`, `identity/rules.md`,
   - only real workflows in `playbooks/workflows/`,
   - only useful methods or personas in `playbooks/methods/` and
     `playbooks/agents/` when the workspace needs those extensions,
   - domain-specific source folders,
   - output folders that match actual outputs,
   - only real review checklists in `reviews/`.
4. Create one root `README.md` by default. Add folder-level READMEs only for a
   human-facing handoff surface, an intentionally empty placeholder, or local
   rules that would otherwise be unclear. Keep them to a title plus one or two
   sentences.
5. Keep source-of-truth rules explicit, especially for generated files,
   structured state, approvals, and `.docs`/`.code`/`.drive` boundaries.
6. When a `.code` facet exists, prefer small, named CLI tools for recurring
   workflow steps that benefit from deterministic execution, such as parsing,
   validation, rendering, compilation, state updates, scraping, API calls, or
   report generation. Document these commands in `AGENTS.md` and reference them
   from `playbooks/workflows/`.
7. When a `.drive` facet exists, use it for shareable Docs, Slides, Sheets,
   PDFs, exports, and handoff artifacts. Keep durable steering in `.docs`.
8. Do not delete or overwrite existing user material without explicit approval.

## Audit Workflow

1. Read `README.md` and `AGENTS.md` if present.
2. Inspect top-level folders and representative files.
3. Check for clear separation of concerns:
   - identity/context vs process,
   - sources vs outputs,
   - human-readable docs vs machine state,
   - playbooks vs review checklists.
4. Check whether the README is human-facing and concise.
5. Check whether `AGENTS.md` contains operational details, boundaries, and read
   order.
6. If a `.code` facet exists, check whether recurring deterministic work is
   exposed through documented CLI tools instead of fragile one-off procedures.
7. If a `.drive` facet exists, check whether shareable artifacts are kept
   separate from durable `.docs` context and `.code` automation internals.
8. Report findings as practical cleanup recommendations, ordered by importance.
9. If the user asked for implementation, make the smallest coherent changes and
   validate by scanning for stale path references.

## Naming Rules

- Use `identity/`, not `depeche/`, for context files.
- Use `playbooks/`, not `vademecum/`, for workflows and reusable process.
- Use `reviews/`, not `controle/`, for quality checks and guardrails.
- Keep `sources/key-links.md` for stable recurring links the agent should know.
- Keep `sources/sources/` and `outputs/outputs/` only as temporary uncategorized
  shelves.

## Output Style

For setup or refactor work, summarize:

- what was created or changed,
- where the main entry points are,
- what still needs human decisions,
- what validation was run.

For audits, lead with the most important mismatches or risks, then give a short
cleanup path.
