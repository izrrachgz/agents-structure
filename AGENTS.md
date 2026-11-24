# Repository instructions

This repository uses Codex-native project guidance. Keep this file concise and put detailed standards in `docs/standards/` or a focused skill under `.agents/skills/`.

## Working agreements

When adopting this scaffold, fill in the project purpose, owning team, component
boundaries, supported consumers, and location of the operational runbook here.
Include the exact working directory and command for local setup, a focused
check, and the full CI check. Link to the maintained source when these differ
by component. Identify which paths are generated and where their inputs live.
Keep environment-specific thresholds and release steps in the deployment contract.

- Read the applicable `AGENTS.md` files and the files directly relevant to the task before editing.
- Preserve user changes and keep each patch focused on the requested outcome.
- Prefer the repository's existing tools and conventions. Do not add a production dependency without explaining why it is needed.
- Run the narrowest meaningful validation after a change, then expand validation when the risk justifies it.
- Report changed files, validation performed, and any unresolved risks.

## Standards routing

- For implementation work, read `docs/standards/code-style.md`.
- For changes to durable state, production dependencies or service health, read `docs/standards/operational-readiness.md`.
- For test changes or behavior fixes, read `docs/standards/testing.md`.
- For changes to a consumer contract (HTTP, events, files, commands, datasets, or shared libraries), read `docs/standards/api-conventions.md`.

## Security and operations

- Never commit credentials, access tokens, private keys, or populated local environment files.
- Treat production changes, destructive data operations, releases, and deployments as approval-gated actions.
- Do not weaken security checks merely to make validation pass.

## Code review rules

- Prioritize correctness, security, behavior regressions, compatibility, and missing tests.
- Lead with actionable findings tied to concrete files and behavior.
- Avoid style-only findings when an automated formatter or linter should enforce them.

## Reusable workflows

Use the repository skills when their descriptions match the task:

- `$review-change` for read-only change review.
- `$fix-issue` for reproducing and fixing a defect.
- `$ub-mode` for test-first implementation and behavior-preserving refactoring.
- `$deploy` for deployment preparation or execution.

Custom read-only agent roles are defined in `.codex/agents/`. Use subagents when the user asks for delegation or when an approved workflow explicitly calls for independent parallel review.
