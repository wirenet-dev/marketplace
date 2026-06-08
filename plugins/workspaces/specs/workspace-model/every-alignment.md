# Every Alignment

The baseline WireNet workspace model is aligned with Every's "How to Use Codex
for Knowledge Work: A Power User's Guide":

https://every.to/p/how-to-use-codex-for-knowledge-work-a-power-user-s-guide

The base `.docs` workspace stays intentionally small:

- `identity/` for context files.
- `playbooks/` for process and repeatable workflows.
- `sources/` for the source shelf and inputs.
- `outputs/` for finished work.
- `reviews/` for quality checks and guardrails.

WireNet extensions are allowed when they keep recurring work easier to run and
make the boundary between human context, machine tooling, and shareable
artifacts clearer:

- `playbooks/methods/` for reusable methods.
- `playbooks/agents/` for optional human-readable agent personas.
- overview tables for scan surfaces.
- `.code` facets for scripts, validation, rendering, structured state, tests,
  and deterministic CLI tools.
- `.drive` facets for shareable Docs, Slides, Sheets, PDFs, exports, and
  handoff artifacts.

Extensions should be labeled as extensions. The default workspace should remain
small enough that a human can understand it quickly.
