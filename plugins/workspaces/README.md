# Workspaces

Workspaces is the first plugin in the WireNet marketplace. It gives Codex
skills and deterministic helper scripts for setting up, auditing, linting,
extending, and operating knowledge-work workspaces.

## Model

The base model follows Every's "How to Use Codex for Knowledge Work" structure:

```text
identity/    standing context, preferences, and rules
playbooks/   repeatable workflows and reusable methods
sources/     source shelves, inputs, references, and recurring links
outputs/     drafts, reports, finished artifacts, and preserved work
reviews/     concrete quality checks and guardrails
```

WireNet extends that model with project facets when a knowledge-work project
needs more than a Markdown workspace:

```text
project.docs/   human-agent source of truth
project.code/   deterministic CLI tools, validation, rendering, tests, state
project.drive/  shareable Docs, Slides, Sheets, PDFs, exports, and handoffs
```

The `.code` facet should expose small, composable CLI tools agents can call from
workflows. The `.drive` facet should hold shareable artifacts, while durable
steering and review rules remain in `.docs`.

## Layout

```text
.codex-plugin/plugin.json
skills/
scripts/
assets/
specs/
fixtures/
```

Use `specs/workspace-model/` for the durable doctrine and `fixtures/` for
validation examples. Keep marketplace-level files at the repository root.
