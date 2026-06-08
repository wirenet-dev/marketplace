---
name: "workspace-review"
description: "Use when the user asks to create, improve, or apply a workspace review checklist under reviews."
---

# Workspace Review

Use this skill for `reviews/*.md`.

Create from the bundled template when useful:

```bash
python3 ../../scripts/workspace_tool.py create-review <workspace> --name "<name>"
```

Review checklists are guardrails and failure detectors. They should be concrete
enough to pass or fail.

Good review checklist families include:

- data accuracy
- writing quality
- source coverage
- confidentiality
- external sharing
- generated artifact quality
- workflow retirement or revision

After creating a review checklist, link it from any workflow that should use it.

