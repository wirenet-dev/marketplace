# Workspaces

Workspaces is a Codex plugin for setting up and maintaining WireNet-style
knowledge-work folders. It gives agents a shared workspace model, a set of
focused skills, reusable templates, and a small deterministic command-line
helper.

Use it when a folder should become a durable working place for a human and an
agent: not just a pile of notes, prompts, reports, and source material, but a
workspace with clear context, process, evidence, outputs, and review checks.

## What The Plugin Provides

Workspaces provides four things:

- **Skills** for setup, audit, linting, extension, workflow writing, method
  writing, review checklists, agent personas, and session mining.
- **A deterministic helper** at `scripts/workspace_tool.py` for inspect, lint,
  cleanup of empty top-level `tmp/`, and template-based document creation.
- **Templates** for common workspace documents such as workflows, methods,
  reviews, and agent personas.
- **Model notes and fixtures** that keep the plugin testable and explain the
  conventions behind it.

The plugin keeps general workspace doctrine inside the plugin. Individual
workspaces should only document what is local to that workspace: purpose, read
order, boundaries, commands, source-of-truth rules, and exceptions.

## Workspace Model

A standard docs workspace is plain Markdown and Obsidian-friendly:

```text
identity/    standing context, preferences, and rules
playbooks/   repeatable workflows, reusable methods, prompts, and personas
sources/     source material, references, evidence, and recurring links
outputs/     drafts, reports, finished artifacts, and preserved work
reviews/     concrete quality checks and guardrails
```

Two optional root-level folders are supported when they are useful:

```text
inbox/       untriaged notes, snippets, prompts, and ideas
overviews/   Obsidian Bases or similar scan views
```

Larger projects can use sibling facets:

```text
project.docs/   human-agent source of truth
project.code/   deterministic tools, validation, rendering, tests, state
project.drive/  shareable Docs, Slides, Sheets, PDFs, exports, handoffs
```

The default write boundary is conservative: agents may read across the system
for relevant context, but may write or edit only inside the active workspace
unless the user explicitly says otherwise. In faceted projects, the workspace
instructions should state whether paired `.code` or `.drive` facets are
writable for a workflow.

## Core Conventions

- Keep one workspace-root `README.md` for human-facing local context.
- Keep one workspace-root `AGENTS.md` for local agent read order, boundaries,
  commands, approvals, and exceptions.
- Do not create folder-level READMEs by default.
- Keep `sources/` mostly flat: use `sources/key-links.md`,
  `sources/recurring-docs.md`, flat `sources/*.md` topic maps, and
  `sources/_sources/` for unplaced source material.
- Use `outputs/_outputs/` for produced artifacts that do not yet fit a named
  output shelf.
- Put Obsidian Bases and similar scan views in root `overviews/`.
- Let Markdown filenames carry document titles in Obsidian; content can start
  with the first useful section.

## Skill Guide

The plugin exposes ten skills. Codex can choose them automatically from the
task, and the user can also ask for a skill by name.

### `workspace`

The core skill and router. Use it for general setup, audit, refactor, or
alignment work when the user says "workspace" without naming a narrower task.

It explains the main folder model, chooses the right narrower skill when
possible, and keeps setup or audit work grounded in the plugin's conventions.

### `workspace-bootstrap`

Creates or completes the smallest useful workspace structure. It is for new
folders, partial workspaces, or old folders that need the basic workspace
shape:
`README.md`, `AGENTS.md`, `identity/`, `playbooks/`, `sources/`, `outputs/`,
and `reviews/`.

The skill avoids empty scaffolding unless the user explicitly wants a reusable
template. It also adds the default write boundary and documents facet rules
when `.docs`, `.code`, or `.drive` facets are involved.

### `workspace-audit`

Reviews an existing workspace and produces practical cleanup recommendations.
It checks whether the README is useful for humans, whether agent instructions
are operational and local, whether sources and outputs are separated, whether
facets are clear, and whether recurring deterministic work should be moved into
documented commands.

When the user asks for implementation, the skill applies the smallest coherent
fixes and validates again.

### `workspace-lint`

Runs deterministic structural checks with `scripts/workspace_tool.py`.

The linter reports missing required structure, legacy folder names, missing
identity files, folder-level READMEs, misplaced overview/facet files, old
generic shelves such as `sources/sources/`, low-value generic source folders,
unknown root folders, top-level `tmp/`, incomplete workflows, and review
checklist shape issues.

Linting is non-destructive by default. The only cleanup flag is `--clean-tmp`,
which removes an empty top-level `tmp/` folder and leaves non-empty scratch
folders for review.

### `workspace-extend`

Adds a coherent new part to an existing workspace. Use it for a new source
shelf, output type, workflow family, review layer, overview folder, `.code`
facet, or `.drive` facet.

The skill prefers the smallest structure that supports real work. It uses
domain-specific names when a durable folder is justified, flat `sources/*.md`
topic maps when a folder would be too much, and `_sources` or `_outputs` only
as generic intake shelves.

### `workspace-workflow`

Creates or improves repeatable procedures under `playbooks/workflows/`.

A workflow should explain its purpose, trigger or cadence, input sources,
output artifact, machine state, commands, steps, approval rules, verification,
review checklist, final output location, and retirement conditions.

Use this skill when a task is not just a one-off action but a repeatable way of
working.

### `workspace-method`

Creates or improves reusable methods under `playbooks/methods/`.

Methods are smaller than workflows. A method captures one reusable move that
can appear inside several workflows, such as an evidence audit, source check,
or drafting pattern. The skill avoids creating methods for one-off
instructions.

### `workspace-review`

Creates, improves, or applies checklist-style guardrails under `reviews/`.

Review checklists should be concrete enough to pass or fail. Good checklist
families include data accuracy, writing quality, source coverage,
confidentiality, external sharing, generated artifact quality, and workflow
retirement.

### `workspace-agent`

Creates optional human-readable agent personas under `playbooks/agents/`.

Personas should be narrow and tied to real workflows, such as evidence checker,
company researcher, draft reviewer, or inbox triage agent. The skill avoids
personas that merely rename the general agent.

### `workspace-session-mining`

Mines recent sessions for durable workspace memory. It looks for recurring user
instructions, cleanup commands, restructuring preferences, approval rules,
workflow steps, and review checks.

This skill is review-first. It collects candidate updates, proposes where they
belong, and asks for user approval before writing anything into preferences,
rules, agent instructions, playbooks, or reviews.

## Helper Commands

Run commands from the repository root while developing the plugin, or adapt the
path when using the installed plugin.

Inspect a workspace:

```bash
python3 plugins/workspaces/scripts/workspace_tool.py inspect /path/to/workspace
```

Lint a workspace:

```bash
python3 plugins/workspaces/scripts/workspace_tool.py lint /path/to/workspace
```

Use JSON output for precise reports or scripts:

```bash
python3 plugins/workspaces/scripts/workspace_tool.py lint /path/to/workspace --json
```

Remove an empty top-level `tmp/` scratch folder during lint cleanup:

```bash
python3 plugins/workspaces/scripts/workspace_tool.py lint /path/to/workspace --clean-tmp
```

Create common workspace documents from the bundled templates:

```bash
python3 plugins/workspaces/scripts/workspace_tool.py create-workflow /path/to/workspace --name "Weekly Report"
python3 plugins/workspaces/scripts/workspace_tool.py create-method /path/to/workspace --name "Evidence Audit"
python3 plugins/workspaces/scripts/workspace_tool.py create-review /path/to/workspace --name "Source Check"
python3 plugins/workspaces/scripts/workspace_tool.py create-agent /path/to/workspace --name "Research Agent"
```

## Plugin Directory

```text
.codex-plugin/plugin.json   Codex plugin manifest
skills/                     skills exposed by this plugin
scripts/                    deterministic workspace helper CLI
assets/templates/           document templates used by the CLI
specs/workspace-model/      durable workspace model notes
fixtures/                   example workspaces for validation
```

## Validation

Validate the marketplace from the repository root:

```bash
python3 tools/validate-codex-marketplace.py .
```

Validate the plugin with the bundled plugin-creator validator when available:

```bash
python3 /Users/gitt/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/workspaces
```

Useful smoke checks while changing the linter:

```bash
python3 plugins/workspaces/scripts/workspace_tool.py lint plugins/workspaces/fixtures/valid-workspace --json
python3 plugins/workspaces/scripts/workspace_tool.py lint plugins/workspaces/fixtures/faceted-project.docs --json
```
