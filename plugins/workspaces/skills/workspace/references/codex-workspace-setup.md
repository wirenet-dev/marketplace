# Codex Workspace Setup

Use this guide to set up a clear human-agent workspace for recurring knowledge
work: applications, research, operations, writing, reporting, fundraising,
recruiting, support, planning, or personal administration.

The point of the workspace is simple: keep identity, playbooks, sources,
outputs, and reviews in predictable places so an agent can help without being
re-briefed from scratch each time. When the project needs code or shared
artifacts, split it into `.docs`, `.code`, and `.drive` facets.

## Core Principle

A good workspace follows the "Codex for Knowledge Work" structure from Every
and separates five things:

- Identity: standing context about the human, project, preferences, and rules.
- Playbooks: repeatable workflows and process instructions.
- Sources: what the work is grounded in.
- Outputs: what the process produces and preserves.
- Reviews: how finished work is checked before it is trusted or shared.

The Every article keeps the default `.docs` structure intentionally small:
context files, repeatable playbooks, source shelves, outputs, and review
checklists. Extra folders are useful only when they make recurring work easier
to run.

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
scheduled runs, structured state, tests, generated files, reusable scripts, or
deterministic CLI tools for agents.

Use `project.drive/` for artifacts that are meant to be shared or edited through
Google Drive surfaces, such as Docs, Slides, Sheets, PDFs, exports, and shared
handoff folders. Do not make Drive-only files the only source of project
context; preserve durable steering and review rules in `project.docs/`.

When `project.code/` exists, use it to expose small, composable CLI tools for
workflow steps that benefit from deterministic execution. These commands give
the agent repeatable methods for work such as parsing, validation, rendering,
compilation, state updates, scraping, API calls, and report generation.

## Recommended Structure

```text
project.docs/
  README.md
  AGENTS.md
  identity/
    context.md
    preferences.md
    rules.md
  playbooks/
    workflows/
      <workflow>.md
    <short-playbook>.md
  sources/
    key-links.md
    recurring-docs.md
    sources/
    <domain-source>/
  outputs/
    drafts/
    reports/
    <output-type>/
    outputs/
  reviews/
    <review-checklist>.md

project.code/
  AGENTS.md
  scripts/
  tests/
  templates/

project.drive/
  docs/
  slides/
  sheets/
  exports/
```

Use domain-specific names wherever possible. Keep generic
`sources/sources/` and `outputs/outputs/` shelves only as temporary homes for
material that has not earned a clearer category yet.

## Folder Roles

### README.md

The README is for humans. It should explain, briefly:

- what the workspace is for,
- what each top-level folder contains,
- what workflows exist,
- what sources are used,
- what outputs are produced,
- how reviews function as the quality-check layer.

Do not make the README a long agent manual. Put operational instructions,
paired-repo details, commands, and hard agent boundaries in `AGENTS.md`.

### AGENTS.md

`AGENTS.md` is the agent entry point. It should be short and explicit:

- startup read order,
- docs/code/drive split if the project uses multiple facets,
- source-of-truth rules,
- commands to run,
- CLI tools available for workflow steps,
- approval boundaries,
- things the agent must never do.

If humans do not need to read a detail during normal use, it probably belongs
in `AGENTS.md`, not the README.

### identity/

`identity/` contains the standing context files. It should let the agent answer:
who the workspace is for, what is being worked on, which tools and people
matter, how work should be handled, and what the agent may or may not do.

Use these files by default:

- `context.md`: role, active projects, tools, collaborators, decision context.
- `preferences.md`: writing style, communication preferences, decision style.
- `rules.md`: hard boundaries, approval rules, allowed actions, forbidden actions.

Keep workflow instructions out of `identity/`. If a file says how to perform a
recurring process, it belongs in `playbooks/`.

#### Optional Overview Tables

Overview tables are a local extension, not part of the Every article's minimal
structure. Use them only when Obsidian Bases or similar lightweight tables make
the existing workspace easier to scan.

Rules for overviews:

- An overview is a view, not a source of truth.
- Add only enough frontmatter to the underlying notes to make useful rows.
- Do not duplicate full source content inside the overview.
- If an overview reveals a mismatch, fix the underlying source or output file.

Good overview candidates:

- active projects or applications,
- watched companies or accounts,
- dated reports or digests,
- source inventories,
- review checklists,
- open decisions.

### sources/

`sources/` is the source shelf: the input material the work is grounded in.
Sources are not only raw inputs; they can include evidence, templates, reference
notes, canonical PDFs, datasets, saved links, transcripts, and steering
documents.

Use named subfolders for durable source categories:

```text
sources/
  key-links.md
  recurring-docs.md
  evidence/
  templates/
  watchlist/
  reference/
  sources/
```

Use `sources/key-links.md` for recurring links the agent should know about by
default: newsletters, databases, dashboards, key authors, source directories,
reference docs, or other stable web surfaces. Keep it compact and curated.

Use `sources/recurring-docs.md` to list what the agent should read before common
artifact types or workflows.

For human-steered automation, keep a compact Markdown steering layer here. If
the automation needs structured data, compile that Markdown into YAML or JSON
in the code repo. The structured file adds value when it enables validation,
deduplication, deterministic parsing, or repeatable automation. If humans are
the only readers and no automation depends on it, Markdown alone is usually
enough.

### playbooks/

`playbooks/` is the workspace's process shelf. It contains repeatable workflows
and reusable instructions that make recurring work easier to run consistently.

Use `playbooks/workflows/` for end-to-end processes with a trigger, inputs,
steps, outputs, and review step. Examples:

- weekly report,
- inbox sweep,
- application drafting,
- research brief,
- customer feedback digest.

Simple workspaces may also keep short playbooks directly under `playbooks/`,
such as `inbox-sweep.md` or `research-brief.md`.

As a local extension, use `playbooks/methods/` for reusable methods that can
appear inside multiple workflows. Examples:

- interview synthesis method,
- evidence audit method,
- cover-letter refinement method,
- source reliability method,
- executive-summary method.

Use `playbooks/agents/` for optional human-readable agent personas. These are
role definitions the user can inspect in Obsidian and the agent can use when a
workflow needs a narrower stance. Examples:

- evidence checker,
- company researcher,
- draft reviewer,
- inbox triage agent.

The distinction is:

- a workflow says what happens from trigger to finished output;
- a method says how to perform one reusable move inside a workflow.
- an agent persona says which temporary role the agent should adopt.

### outputs/

`outputs/` holds generated, drafted, sent, published, or otherwise preserved
work. Outputs are records. They should be easy to browse by date, status, or
artifact type.

Use named subfolders:

```text
outputs/
  drafts/
  sent/
  reports/
  digests/
  outputs/
```

Do not mix machine-only state into outputs. If a file exists only so automation
can remember what it has seen, put it in `project.code/` or a state store. If an
artifact exists mainly for Google Drive sharing or external handoff, keep it in
`project.drive/`.

### reviews/

`reviews/` contains checklist-style quality checks and guardrails. Reviews are
the test layer of a knowledge workspace.

Use review checklists before:

- trusting a digest,
- sending or publishing a draft,
- preserving a final record,
- changing the workspace structure,
- relying on factual claims or metrics.

A review checklist should be specific enough to catch real errors, but short
enough that it actually gets used. Add checks when failures repeat; remove checks
that no longer prevent mistakes.

## Optional Code And Drive Facets

Use `project.code/` when the workspace needs:

- scheduled automation,
- scraping or API calls,
- validation,
- structured state,
- rendering or compilation,
- tests,
- generated files,
- reusable scripts,
- composable CLI tools for deterministic workflow steps.

Recommended split:

```text
project.docs/
  human-readable identity, playbooks, sources, outputs, reviews

project.code/
  automation code, tests, templates, compiled state, build commands

project.drive/
  shareable Docs, Slides, Sheets, PDFs, exports, and handoff artifacts
```

The `.docs` facet remains the human workspace. The `.code` facet remains the
machine workspace. The `.drive` facet remains the shareable artifact surface. If
something is prose, evidence, or a preserved record, keep it in `.docs`. If
something is a script, state ledger, generated cache, build template, or
validator, keep it in `.code`. If something is a Google Docs-ready document,
Slides deck, Sheets workbook, PDF export, or handoff artifact, keep it in
`.drive`.

When useful, expose code-repo behavior through named CLI commands rather than
requiring the agent to reconstruct one-off shell procedures. Good CLI tools are
small, composable, documented, and testable. They should accept clear inputs,
produce predictable outputs, and be safe to call from multiple workflows.

Document these commands in the `.code` facet's `AGENTS.md`, including what
each command reads, writes, validates, and whether it requires approval. Reference
the relevant commands from `playbooks/workflows/` so recurring work has stable
execution points as well as human-readable instructions.

## Workflow File Template

Use this shape for each file in `playbooks/workflows/`:

```markdown
# Workflow Name

Purpose:

Trigger or cadence:

Input sources:

Output artifact:

Machine state:

CLI tools:

Steps:

Approval rules:

What the agent may do without asking:

What the agent must ask before doing:

Verification steps:

Review checklist:

Where the final output lives:

When to retire or revise this workflow:
```

Every workflow should answer:

- What starts this?
- What does it read?
- What does it write?
- Which CLI tools make recurring steps deterministic?
- What must be checked?
- What may the agent do without asking?
- What requires explicit approval?

## Review Checklist Template

Use this shape for each file in `reviews/`:

```markdown
# Review Name

Use this before:

- check one
- check two
- check three
- command or validation step, if any
```

Write review checklists as failure detectors, not advice. A good item is
concrete: it can be checked, passed, or failed.

## Setup Procedure

1. Create the top-level folders.
2. Write the README for a human reader.
3. Write `AGENTS.md` with read order, boundaries, and commands.
4. Fill `identity/context.md`, `identity/preferences.md`, and `identity/rules.md`.
5. Add the first real source folders, not a maze of empty scaffolding.
6. Create only the workflows that already exist or are about to be used.
7. Add one review checklist per real handoff point.
8. Add overview tables only after there are files worth tabulating.
9. Add a `.code` facet only when automation or validation needs it.
10. Add a `.drive` facet only when Google Drive sharing or external handoff
    needs it.
11. Run one real workflow manually and update the workspace based on what broke.

## Maintenance Rules

- Keep the README short and current.
- Keep `AGENTS.md` operational and explicit.
- Keep `identity/` stable; do not bury workflow steps there.
- Keep `playbooks/` practical; workflows, methods, and agent personas should be
  easy to scan and run.
- Keep source folders human-readable.
- Keep outputs as records, not scratch space.
- Keep overviews as views, not duplicate databases.
- Keep reviews aligned with actual risks.
- Delete empty scaffolding when it stops helping.
- Prefer one compact steering file over many small files when a human needs to
  scan and edit the information.
- Prefer structured state only when automation benefits from it.

## Good Starting Prompt

```text
Set up this folder as a Codex workspace for [kind of work].

Use this structure:
- identity/ for context, preferences, and rules
- playbooks/ for repeatable workflows and reusable process
- sources/ for source material and evidence
- outputs/ for produced and preserved work
- reviews/ for quality checks and guardrails

First inspect any existing files. Then propose the smallest useful structure,
avoiding empty scaffolding. Create README.md for humans and AGENTS.md for
agents. Make the source-of-truth rules explicit, including what requires my
approval.
```

## Definition Of Done

A workspace is ready when:

- a human can open `README.md` and understand the system in one minute,
- an agent can open `AGENTS.md` and know where to read, write, and stop,
- every top-level folder has a distinct purpose,
- sources, outputs, and machine state are not mixed together,
- workflows have review steps,
- risky actions require explicit approval,
- the first real workflow can run without re-explaining the whole project.
