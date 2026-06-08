# Workflow Canvas

Use this shape for recurring workflows under `playbooks/workflows/`.

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

Every workflow should answer what starts it, what it reads, what it writes, what
must be checked, which CLI tools make recurring steps deterministic, and what
requires explicit approval.

