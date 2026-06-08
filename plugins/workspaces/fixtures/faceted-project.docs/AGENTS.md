# Faceted Project Docs Fixture - Agent Entry Point

Read `identity/context.md`, then use workflows from `playbooks/`.

The paired code facet is `../faceted-project.code`.
The paired drive facet is `../faceted-project.drive`.
Keep durable steering in this `.docs` facet. Use the `.code` facet for
deterministic scripts and the `.drive` facet for shareable artifacts.

The agent may read across the system for relevant context, but may write or edit
only inside this docs workspace unless the user explicitly says otherwise.
