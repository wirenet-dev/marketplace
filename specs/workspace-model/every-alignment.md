# Every Alignment

The baseline WireNet workspace model is aligned with Every's "Codex for
Knowledge Work" structure:

- `identity/` for context files.
- `playbooks/` for process and repeatable workflows.
- `sources/` for the source shelf and inputs.
- `outputs/` for finished work.
- `reviews/` for quality checks and guardrails.

WireNet extensions are allowed when they keep recurring work easier to run:

- `playbooks/methods/` for reusable methods.
- `playbooks/agents/` for optional human-readable agent personas.
- overview tables for scan surfaces.
- paired code repos for scripts, validation, rendering, structured state, and
  deterministic CLI tools.

Extensions should be labeled as extensions. The default workspace should remain
small enough that a human can understand it quickly.

