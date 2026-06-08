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
checklists. WireNet adds optional root-level `inbox/` and `overviews/`
extensions only when they make recurring work easier to run.

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
  inbox/
  identity/
    context.md
    preferences.md
    rules.md
  overviews/
    <scan-view>.base
  playbooks/
    workflows/
      <workflow>.md
    <short-playbook>.md
  sources/
    key-links.md
    recurring-docs.md
    _sources/
    <domain-source>/
  outputs/
    _outputs/
    drafts/
    reports/
    <output-type>/
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

Use domain-specific names wherever possible. Use root-level `inbox/` for loose
human notes and untriaged mixed material. Use `sources/_sources/` as the default
home for new source material when the user has not named a destination. Use
`outputs/_outputs/` as the default home for produced artifacts that do not fit a
specific output shelf.

## Folder Roles

### README.md

The README is for humans. It should explain, briefly:

- what the workspace is for,
- the local areas, workflows, sources, outputs, and reviews that matter for this
  workspace,
- where a human should start reading,
- open decisions or current operating notes.

Do not make the README a generic explanation of the Workspaces model. The
plugin already defines folder roles, workflow templates, method templates, and
review shapes. The README should add local meaning, not repeat plugin doctrine.
Put operational instructions, paired-repo details, commands, and hard agent
boundaries in `AGENTS.md`.

Do not create folder-level READMEs. If the information matters to a human, keep
it in the root `README.md`. If it matters only to agents, keep it in
`AGENTS.md`. Folder READMEs are too easy to scatter and forget.

### AGENTS.md

`AGENTS.md` is the agent entry point. It should be short and explicit:

- startup read order,
- docs/code/drive split if the project uses multiple facets,
- paired facet paths and source-of-truth boundaries,
- read/write boundary: the agent may read across the system for relevant
  context, but may write or edit only inside the workspace unless the user
  explicitly says otherwise; in faceted projects, state whether paired facets
  are writable for the current workflow,
- source-of-truth rules,
- commands to run,
- CLI tools available for workflow steps,
- approval boundaries,
- things the agent must never do.

Do not paste generic Workspaces plugin instructions into `AGENTS.md`. The plugin
already knows the core folder model, workflow fields, method shape, review
shape, and Markdown style conventions. `AGENTS.md` should contain only the local
operating contract: project-specific read order, boundaries, commands, facets,
source-of-truth rules, approvals, and exceptions.

If humans do not need to read a detail during normal use, it probably belongs
in `AGENTS.md`, not the README.

### inbox/ (Optional)

`inbox/` is the one sanctioned junk drawer for mixed, untriaged material:
scratch notes, copied snippets, prompt ideas, rough links, and half-formed
thoughts that do not yet belong anywhere else.

Rules for `inbox/`:

- Use it only when the workspace needs a catch-all.
- Treat it as temporary, not a source of truth.
- Keep it root-level so the mess is visible and easy to sweep.
- Move reusable prompts to `playbooks/prompts/`.
- Move reusable methods or procedures to `playbooks/methods/` or
  `playbooks/workflows/`.
- Move remembered ideas, notes, links, and evidence to named `sources/` files or
  folders.
- Move material becoming deliverable work to `outputs/drafts/` or another named
  output folder.

### identity/

`identity/` contains the standing context files. It should let the agent answer:
who the workspace is for, what is being worked on, which tools and people
matter, how work should be handled, and what the agent may or may not do.

Use these files by default:

- `context.md`: role, active projects, tools, collaborators, decision context.
- `preferences.md`: writing style, communication preferences, decision style.
- `rules.md`: hard boundaries, approval rules, allowed actions, forbidden actions.

Keep workflow instructions out of `identity/`. If a file says how to perform a
recurring process, it belongs in `playbooks/`. Facet boundaries, sibling paths,
commands, and source-of-truth rules belong in `AGENTS.md` so the human
interface stays clean.

### overviews/ (Optional)

`overviews/` is an optional root-level folder for Obsidian Bases or similar
scan views. It is a local extension, not part of the Every article's minimal
structure. Use it only when the existing workspace has enough files to make a
view useful.

Rules for overviews:

- An overview is a view, not a source of truth.
- Keep overview files in root-level `overviews/`.
- Add only enough frontmatter to the underlying notes to make useful rows.
- Do not duplicate full source content inside the overview.
- Do not create overviews for docs/code/drive facet maps or agent routing.
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

Keep `sources/` mostly flat:

```text
sources/
  key-links.md
  recurring-docs.md
  topic-map.md
  _sources/
  durable-category/
```

Use `sources/key-links.md` for recurring links the agent should know about by
default: newsletters, databases, dashboards, key authors, source directories,
reference docs, watchlists, or other stable web surfaces. Keep it compact and
curated.

Use `sources/recurring-docs.md` to list recurring local inputs and what the
agent should read before common artifact types or workflows.

Use flat `sources/*.md` files for lightweight topic maps and compact steering
notes. Create named source folders such as `evidence/`, `templates/`, or
`reference/` only when a durable source category has enough material to deserve
a shelf. Avoid generic folders such as `topics/`, `steering/`, and
`watchlist/` unless the workspace has made a deliberate local convention for
them.

For human-steered automation, keep a compact Markdown steering layer in
`sources/`. If the automation needs structured data, compile that Markdown into
YAML or JSON in the code repo. The structured file adds value when it enables
validation, deduplication, deterministic parsing, or repeatable automation. If
humans are the only readers and no automation depends on it, Markdown alone is
usually enough.

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

Use `playbooks/prompts/` for reusable prompt templates the user wants to invoke
again. If a prompt describes a full recurring process, turn it into a workflow.
If it describes one reusable move, turn it into a method.

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

Use top-level `tmp/` only for disposable generated scratch work, preferably in a
`.code` facet. It is not a source of truth. The workspace linter may remove an
empty `tmp/` during cleanup, but non-empty scratch folders should be reviewed
before deletion.

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

The file does not need a title heading that repeats its filename. In Obsidian,
the filename already carries the document title.

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
Use this before:

- check one
- check two
- check three
- command or validation step, if any
```

The file does not need a title heading that repeats its filename. In Obsidian,
the filename already carries the document title.

Write review checklists as failure detectors, not advice. A good item is
concrete: it can be checked, passed, or failed.

## Setup Procedure

1. Create the top-level folders.
2. Write the README for a human reader, using local meaning instead of generic
   folder-role explanations.
3. Write `AGENTS.md` with read order, boundaries, commands, and the default
   read/write boundary. Do not copy plugin templates or generic workspace
   doctrine into it.
4. Add optional root-level `inbox/` only when the workspace needs a single
   catch-all for untriaged mixed material.
5. Fill `identity/context.md`, `identity/preferences.md`, and `identity/rules.md`.
6. Add the first real source folders, not a maze of empty scaffolding.
7. Create only the workflows that already exist or are about to be used.
8. Add one review checklist per real handoff point.
9. Add optional root-level `overviews/` only after there are files worth
   tabulating.
10. Add a `.code` facet only when automation or validation needs it.
11. Add a `.drive` facet only when Google Drive sharing or external handoff
    needs it.
12. Run one real workflow manually and update the workspace based on what broke.

## Maintenance Rules

- Keep the README short and current.
- Keep `AGENTS.md` operational and explicit.
- Keep README and `AGENTS.md` local; do not restate plugin-provided folder
  roles, workflow templates, method templates, or review templates.
- Keep `identity/` stable; do not bury workflow steps there.
- Keep facet boundaries and read/write boundaries in `AGENTS.md`.
- Keep `inbox/` as the only catch-all. Sweep it into prompts, playbooks,
  sources, or outputs when items become useful.
- Keep Obsidian Bases and scan views in root-level `overviews/`.
- Keep root-level folders limited to `inbox/`, `identity/`, `overviews/`,
  `playbooks/`, `sources/`, `outputs/`, `reviews/`, and disposable `tmp/`.
  Triage unknown root folders into the model or make an explicit convention
  before keeping them.
- Keep `playbooks/` practical; workflows, methods, and agent personas should be
  easy to scan and run.
- Keep source files and folders human-readable.
- Keep outputs as records, not scratch space.
- Keep overviews as views, not duplicate databases.
- Keep reviews aligned with actual risks.
- Delete empty scaffolding when it stops helping.
- Create one root `README.md` by default. Do not create folder-level READMEs;
  move human-facing details to the root README and agent-only details to
  `AGENTS.md`.
- Let Markdown filenames carry document titles in Obsidian; start content with
  the first useful section.
- When recent sessions contain repeated corrections or restructuring commands,
  mine them into proposed updates for `identity/preferences.md`,
  `identity/rules.md`, `AGENTS.md`, playbooks, or reviews. Apply only after
  user approval.
- Treat top-level `tmp/` as disposable scratch. Remove it when empty; review
  contents before deleting non-empty scratch artifacts.
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
agents. Do not repeat generic plugin conventions or templates in those files;
include only the local purpose, read order, boundaries, commands, source of
truth, approvals, and exceptions. The agent may read across the system for
context, but may write or edit only inside this workspace unless I explicitly
say otherwise.
```

## Definition Of Done

A workspace is ready when:

- a human can open `README.md` and understand the system in one minute,
- an agent can open `AGENTS.md` and know where to read, where it may write, and
  where it must stop,
- README and `AGENTS.md` add local context instead of restating plugin doctrine,
- every top-level folder has a distinct purpose,
- sources, outputs, and machine state are not mixed together,
- workflows have review steps,
- risky actions require explicit approval,
- the first real workflow can run without re-explaining the whole project.
