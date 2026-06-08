---
name: "workspace-agent"
description: "Use when the user asks to create or improve a human-readable workspace agent persona under playbooks/agents."
---

# Workspace Agent

Use this skill for optional human-readable agent personas under
`playbooks/agents/`.

Create from the bundled template when useful:

```bash
python3 ../../scripts/workspace_tool.py create-agent <workspace> --name "<name>"
```

Agent personas should be narrow, inspectable, and tied to real workflows.

Define:

- when to use the persona
- responsibilities
- read-first material
- working style
- boundaries
- output style

Do not create personas that merely rename the general agent. Use them when a
workflow benefits from a narrower stance such as evidence checker, company
researcher, draft reviewer, or inbox triage agent.
