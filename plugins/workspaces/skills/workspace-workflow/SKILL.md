---
name: "workspace-workflow"
description: "Use when the user asks to create, improve, document, or review a repeatable workspace workflow under playbooks/workflows."
---

# Workspace Workflow

Use this skill for `playbooks/workflows/*.md`.

Create from the bundled template when useful:

```bash
python3 ../../scripts/workspace_tool.py create-workflow <workspace> --name "<name>"
```

Every workflow should define:

- purpose
- trigger or cadence
- input sources
- output artifact
- machine state
- CLI tools
- steps
- approval rules
- what the agent may do without asking
- what the agent must ask before doing
- verification steps
- review checklist
- where the final output lives
- when to retire or revise the workflow

After writing the workflow, check that referenced sources, reviews, outputs, and
CLI tools exist or are clearly marked as future decisions.
