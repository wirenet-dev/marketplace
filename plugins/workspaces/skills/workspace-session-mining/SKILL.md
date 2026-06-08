---
name: "workspace-session-mining"
description: "Use when the user asks to mine, review, analyze, or distill recent Codex/agent sessions, threads, chats, or work history for recurring cleanup instructions, restructuring commands, preferences, rules, or workspace conventions."
---

# Workspace Session Mining

Use this skill to turn repeated user instructions from recent sessions into
reviewed workspace memory.

## Principle

Mine sessions read-only first. Do not write preferences, rules, `AGENTS.md`, or
playbooks until the user approves the proposed changes.

This skill is for durable patterns, not one-off commands. Prefer fewer, clearer
updates over a large memory dump.

## Sources

Use the narrowest available source:

- Codex thread/session tools, when available and explicitly relevant.
- User-provided exports, summaries, or copied transcripts.
- The current thread, only when the user asks to mine current conversation
  context.

In the Codex app, discover thread list/read tools when they are not already
visible. Do not guess at private transcript file locations.

If the user gives no session count, default to the last 10 relevant sessions.
If relevance is unclear, prefer sessions from the same workspace, project, or
repository before broader account history.

## What To Extract

Look only for user-authored instructions that recur, correct prior behavior, or
define a durable convention:

- cleanup and restructuring rules;
- workspace folder conventions;
- source-of-truth boundaries;
- writing, communication, or decision preferences;
- approval rules and hard boundaries;
- recurring workflow steps;
- review checks that caught real problems.

Do not extract:

- secrets, credentials, private personal details, or transient names;
- one-off task instructions;
- stale instructions contradicted later;
- agent guesses that the user did not endorse;
- broad style preferences from a single weak signal.

## Classification

Propose each candidate for one destination:

- `identity/preferences.md`: how the user likes work handled or communicated.
- `identity/rules.md`: hard boundaries, approval requirements, forbidden
  actions.
- `AGENTS.md`: project operation, read order, commands, facet boundaries, source
  of truth rules, and agent-only details.
- `playbooks/workflows/`: recurring end-to-end procedures.
- `playbooks/methods/`: reusable smaller moves inside workflows.
- `reviews/`: concrete checks that can pass or fail.

Keep facet maps and agent routing in `AGENTS.md`. Keep human-facing summaries
in the root `README.md`. Do not create folder-level READMEs. Do not mine or
write generic Workspaces plugin doctrine, folder role explanations, workflow
templates, method templates, or review templates into README or `AGENTS.md`;
only preserve local rules, exceptions, and operating context.

## Workflow

1. Confirm the workspace path and session count. Use the last 10 relevant
   sessions when the user does not specify a count.
2. Collect only the session material needed for the request.
3. Extract user instructions with short evidence notes, grouped by theme.
4. Remove duplicates and resolve conflicts by preferring the newest explicit
   instruction.
5. Produce a candidate update table with:
   - proposed wording,
   - destination file,
   - reason,
   - confidence,
   - session/source reference when available.
6. Ask for approval before writing.
7. After approval, make the smallest coherent edits.
8. Run the workspace linter and report what changed.

## Output Shape

Before edits, report:

- high-confidence updates;
- uncertain candidates that need user judgment;
- rejected one-off instructions, briefly.

After edits, report:

- files changed;
- what each change preserves for future sessions;
- validation run.
