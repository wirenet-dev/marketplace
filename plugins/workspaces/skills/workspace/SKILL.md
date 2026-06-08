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
- `workspace-session-mining`: mine recent sessions for recurring preferences,
  rules, cleanup instructions, and workspace conventions.

## Setup Workflow

1. Inspect the current folder first: existing files, naming patterns, project
   purpose, and whether `.docs`, `.code`, or `.drive` facets exist.
2. Identify the smallest useful structure. Avoid empty scaffolding unless the
   user explicitly wants a reusable template.
3. Create or update:
   - `README.md` for humans,
   - `AGENTS.md` for agent entry instructions,
   - optional root-level `inbox/` only when the workspace needs one catch-all
     for untriaged notes, snippets, prompts, and ideas,
   - `identity/context.md`, `identity/preferences.md`, `identity/rules.md`,
   - only real workflows in `playbooks/workflows/`,
   - only useful methods or personas in `playbooks/methods/` and
     `playbooks/agents/` when the workspace needs those extensions,
   - flat `sources/*.md` topic maps or durable domain-specific source folders,
   - output folders that match actual outputs,
   - optional root-level `overviews/` only when Obsidian Bases or scan views
     make existing files easier to navigate,
   - only real review checklists in `reviews/`.
4. Create one root `README.md` by default. Do not create folder-level READMEs.
   If the detail matters to a human, put it in the root README. If it matters
   only to agents, put it in `AGENTS.md`.
   For Obsidian-readable Markdown, the filename already carries the document
   title.
5. Keep README and `AGENTS.md` local. Do not restate plugin-provided folder
   roles, workflow templates, method templates, review templates, or generic
   workspace doctrine.
6. Add a write boundary to `AGENTS.md`: the agent may read across the system
   for relevant context, but may write or edit only inside the workspace unless
   the user explicitly says otherwise. In faceted projects, state whether paired
   facets are writable for the current workflow.
7. Keep source-of-truth rules explicit, especially for generated files,
   structured state, approvals, and `.docs`/`.code`/`.drive` boundaries.
8. When a `.code` facet exists, prefer small, named CLI tools for recurring
   workflow steps that benefit from deterministic execution, such as parsing,
   validation, rendering, compilation, state updates, scraping, API calls, or
   report generation. Document these commands in `AGENTS.md` and reference them
   from `playbooks/workflows/`.
9. When a `.drive` facet exists, use it for shareable Docs, Slides, Sheets,
   PDFs, exports, and handoff artifacts. Keep durable steering in `.docs`.
10. Document facet boundaries, paired facet paths, and source-of-truth rules in
   `AGENTS.md`.
11. Do not delete or overwrite existing user material without explicit approval.

## Audit Workflow

1. Read `README.md` and `AGENTS.md` if present.
2. Inspect top-level folders and representative files.
3. Check for clear separation of concerns:
   - identity/context vs process,
   - overviews as scan views,
   - sources vs outputs,
   - human-readable docs vs machine state,
   - playbooks vs review checklists.
4. Check whether the README is human-facing and concise.
5. Check whether `AGENTS.md` contains operational details, boundaries, and read
   order.
6. Check whether README and `AGENTS.md` avoid restating plugin-provided folder
   roles, workflow templates, method templates, review templates, or generic
   workspace doctrine.
7. If a `.code` facet exists, check whether recurring deterministic work is
   exposed through documented CLI tools instead of fragile one-off procedures.
8. If a `.drive` facet exists, check whether shareable artifacts are kept
   separate from durable `.docs` context and `.code` automation internals.
9. Report findings as practical cleanup recommendations, ordered by importance.
10. If the user asked for implementation, make the smallest coherent changes and
   validate by scanning for stale path references.

## Naming Rules

- Use `identity/`, not `depeche/`, for context files.
- Use `playbooks/`, not `vademecum/`, for workflows and reusable process.
- Use `reviews/`, not `controle/`, for quality checks and guardrails.
- Use root-level `inbox/` for loose human notes and untriaged mixed material.
- Keep `sources/key-links.md` for stable recurring links and watchlists the
  agent should know.
- Keep `sources/recurring-docs.md` for recurring local inputs and read-before
  lists.
- Prefer flat `sources/*.md` topic maps over generic source folders such as
  `topics/`, `steering/`, or `watchlist/`.
- Use `sources/_sources/` for new source material when the user has not named a
  destination.
- Use `outputs/_outputs/` for produced artifacts that do not fit a more specific
  output shelf.
- Keep root-level folders limited to the workspace model. Unknown root folders
  should be moved into an existing top-level area or promoted into the model
  only after an explicit convention decision.
- The agent may read across the system for context, but may write or edit only
  inside the workspace unless the user explicitly says otherwise.
- For Obsidian-readable Markdown, the filename is enough title.
- README and `AGENTS.md` should add local context, not copy plugin doctrine or
  core templates.

## Output Style

For setup or refactor work, summarize:

- what was created or changed,
- where the main entry points are,
- what still needs human decisions,
- what validation was run.

For audits, lead with the most important mismatches or risks, then give a short
cleanup path.
