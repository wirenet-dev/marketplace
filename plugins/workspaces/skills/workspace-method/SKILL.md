---
name: "workspace-method"
description: "Use when the user asks to create, improve, or document a reusable workspace method under playbooks/methods."
---

# Workspace Method

Use this skill for reusable methods under `playbooks/methods/`.

Methods are smaller than workflows. A method describes one reusable move that can
appear inside multiple workflows.

Create from the bundled template when useful:

```bash
python3 ../../scripts/workspace_tool.py create-method <workspace> --name "<name>"
```

A method should define:

- purpose
- when to use it
- inputs
- procedure
- output
- checks

Do not create a method for a one-off instruction. Put one-off steps inside the
workflow that uses them.

