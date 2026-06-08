# Workflow Canvas

Use this shape for recurring workflows under `playbooks/workflows/`.

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

Every workflow should answer what starts it, what it reads, what it writes, what
must be checked, which CLI tools make recurring steps deterministic, and what
requires explicit approval.
