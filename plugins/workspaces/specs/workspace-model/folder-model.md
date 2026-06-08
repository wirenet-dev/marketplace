# Workspace Folder Model

This is the shared WireNet workspace model for coding-agent plugins.

The workspace model has two layers:

- project facets: `.docs`, `.code`, and `.drive`;
- the internal `.docs` folder model from "Codex for Knowledge Work".

## Project Facets

Use dot-suffix folders when a project needs more than one working surface:

```text
project.docs/    Obsidian-compatible Markdown workspace
project.code/    deterministic CLI tools, scripts, tests, and machine state
project.drive/   shareable artifacts mirrored through Google Drive
```

Use `project.docs/` as the human-agent source of truth. It should be plain
Markdown, readable in Obsidian, and organized around identity, playbooks,
sources, outputs, and reviews.

Use `project.code/` when the workspace needs automation, validation, rendering,
scheduled runs, structured state, tests, or deterministic CLI tools for agents.

Use `project.drive/` for artifacts that are meant to be shared or edited through
Google Drive surfaces, such as Docs, Slides, Sheets, PDFs, exports, and shared
handoff folders. Do not make Drive-only files the only source of project
context; preserve durable steering and review rules in `project.docs/`.

## Docs Folder Model

Inside `project.docs/`, follow the "Codex for Knowledge Work" structure from
Every and keep five concerns separate:

```text
identity/    context files: who, what, preferences, and rules
playbooks/   process: repeatable workflows and reusable instructions
sources/     source shelf: inputs, evidence, references, and key links
outputs/     drafts, finished artifacts, reports, and preserved work
reviews/     quality checks, guardrails, and review checklists
```

## identity/

Use `identity/` for the standing context files an agent should read before
acting:

- `context.md`: role, active projects, tools, collaborators, decision context.
- `preferences.md`: writing style, communication preferences, decision style.
- `rules.md`: hard boundaries, approval rules, allowed actions, forbidden
  actions.

Keep workflow steps out of `identity/`.

## playbooks/

Use `playbooks/` for repeatable process:

- `playbooks/workflows/`: end-to-end recurring workflows.
- `playbooks/methods/`: reusable methods that appear inside multiple workflows.
- `playbooks/agents/`: optional human-readable task personas.
- Direct files such as `inbox-sweep.md` are fine for small workspaces.

## sources/

Use `sources/` for inputs and source material:

- `key-links.md`: stable recurring links.
- `recurring-docs.md`: what to read before common artifact types.
- `sources/`: uncategorized or canonical source shelf.
- Domain folders such as `evidence/`, `templates/`, `reference/`, or
  `watchlist/` when useful.

## outputs/

Use `outputs/` for produced and preserved work:

- `drafts/`
- `reports/`
- `outputs/` as a temporary uncategorized shelf.

Do not treat outputs as the source of truth. If an output creates a reusable
idea, move it back into `identity/`, `playbooks/`, or `sources/`.

## reviews/

Use `reviews/` for checklist-style quality checks and guardrails.

Review checklists should be short, concrete, and tied to real failure modes.
Add checks when mistakes repeat; remove checks that no longer catch problems.
