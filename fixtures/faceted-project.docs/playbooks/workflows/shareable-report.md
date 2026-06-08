# Shareable Report

Purpose:

Produce a report that can be shared as a document export.

Trigger or cadence:

Manual test run.

Input sources:

`sources/key-links.md`

Output artifact:

A report exported into `../faceted-project.drive/docs/`.

Machine state:

None.

CLI tools:

`../faceted-project.code/scripts/render-report`

Steps:

1. Read sources.
2. Draft in `.docs`.
3. Render or export through `.code`.
4. Place the shareable artifact in `.drive`.

Approval rules:

Ask before sharing externally.

What the agent may do without asking:

Draft and render local artifacts.

What the agent must ask before doing:

Sharing through Google Drive.

Verification steps:

Run the review checklist.

Review checklist:

`reviews/shareable-report.md`

Where the final output lives:

`../faceted-project.drive/docs/`

When to retire or revise this workflow:

Revise when the facet model changes.

