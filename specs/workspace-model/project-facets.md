# Project Facets

Use three dot-suffix facets when a knowledge-work project spans human-readable
context, deterministic tooling, and shareable artifacts:

```text
project.docs/
project.code/
project.drive/
```

## project.docs/

The `.docs` facet is the Obsidian-compatible Markdown workspace. It is the
human-agent source of truth for:

- `README.md`
- `AGENTS.md`
- `identity/`
- `playbooks/`
- `sources/`
- `outputs/`
- `reviews/`

Use this facet for standing context, workflow instructions, source shelves,
draft records, and review guardrails.

## project.code/

The `.code` facet is the deterministic tooling surface. Use it for:

- CLI tools agents can call from workflows;
- validators and linters;
- rendering and export scripts;
- tests;
- structured state;
- generated caches;
- templates that need compilation.

Every recurring CLI tool should be documented in `AGENTS.md` and referenced from
the relevant workflow.

## project.drive/

The `.drive` facet is the shareable artifact surface. Use it for Google
Drive-oriented outputs:

- Google Docs-ready documents;
- Slides decks;
- Sheets workbooks;
- PDFs and exports;
- client or partner handoff folders;
- shared review artifacts.

The `.drive` facet is for collaboration and sharing. It should not replace the
durable workspace source of truth in `.docs`.

