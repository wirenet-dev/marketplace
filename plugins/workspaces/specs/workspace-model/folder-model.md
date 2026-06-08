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

Agents may read across the system for relevant context, but may write or edit
only inside the workspace unless the user explicitly says otherwise.

Use `project.code/` when the workspace needs automation, validation, rendering,
scheduled runs, structured state, tests, or deterministic CLI tools for agents.

Use `project.drive/` for artifacts that are meant to be shared or edited through
Google Drive surfaces, such as Docs, Slides, Sheets, PDFs, exports, and shared
handoff folders. Do not make Drive-only files the only source of project
context; preserve durable steering and review rules in `project.docs/`.

## Docs Folder Model

Inside `project.docs/`, follow the "Codex for Knowledge Work" structure from
Every and keep the five core concerns separate. WireNet also allows optional
root-level `inbox/` and `overviews/` extensions:

```text
inbox/       optional untriaged catch-all for notes, prompts, snippets, ideas
identity/    context files: who, what, preferences, and rules
overviews/   optional Obsidian Bases and scan views
playbooks/   process: repeatable workflows and reusable instructions
sources/     source shelf: inputs, evidence, references, and key links
outputs/     drafts, finished artifacts, reports, and preserved work
reviews/     quality checks, guardrails, and review checklists
```

Use underscore shelves for deliberate generic intake inside existing root
folders: `sources/_sources/` for source material without a more specific home,
and `outputs/_outputs/` for produced artifacts without a more specific output
shelf.

Unknown root-level folders should be treated as cleanup findings. Move their
contents into the existing model, use `inbox/` while they are untriaged, or make
an explicit convention before keeping a new top-level folder.

## inbox/

Use optional root-level `inbox/` as the single catch-all for mixed, untriaged
material. It is temporary and not a source of truth. Sweep items into
`playbooks/prompts/`, `playbooks/methods/`, `playbooks/workflows/`, named
`sources/` folders, or `outputs/drafts/` when their role becomes clear.

## identity/

Use `identity/` for the standing context files an agent should read before
acting:

- `context.md`: role, active projects, tools, collaborators, decision context.
- `preferences.md`: writing style, communication preferences, decision style.
- `rules.md`: hard boundaries, approval rules, allowed actions, forbidden
  actions.

Keep workflow steps out of `identity/`.

## overviews/

Use optional root-level `overviews/` for Obsidian Bases or similar scan views.
Overviews are views, not source of truth.

## playbooks/

Use `playbooks/` for repeatable process:

- `playbooks/workflows/`: end-to-end recurring workflows.
- `playbooks/methods/`: reusable methods that appear inside multiple workflows.
- `playbooks/agents/`: optional human-readable task personas.
- Direct files such as `inbox-sweep.md` are fine for small workspaces.

## sources/

Use `sources/` for inputs and source material:

- `key-links.md`: stable recurring links and watchlists.
- `recurring-docs.md`: recurring local inputs and what to read before common
  artifact types.
- Flat `*.md` files: lightweight topic maps and compact steering notes.
- `_sources/`: default shelf for raw, imported, source-specific, or otherwise
  unplaced source material.
- Named folders such as `evidence/`, `templates/`, or `reference/` only when a
  durable source category has enough material to deserve a shelf.

Avoid low-value generic folders such as `topics/`, `steering/`, and
`watchlist/` unless the workspace has made a deliberate local convention for
them.

## outputs/

Use `outputs/` for produced and preserved work:

- `drafts/`
- `reports/`
- `_outputs/`: default shelf for produced artifacts that do not yet fit a more
  specific output shelf.

Do not treat outputs as the source of truth. If an output creates a reusable
idea, move it back into `identity/`, `playbooks/`, or `sources/`.

## reviews/

Use `reviews/` for checklist-style quality checks and guardrails.

Review checklists should be short, concrete, and tied to real failure modes.
Add checks when mistakes repeat; remove checks that no longer catch problems.
