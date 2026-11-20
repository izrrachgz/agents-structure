# Codex project structure

This folder is a Codex-native equivalent of a Claude Code project scaffold.

## Adopting the scaffold for a real system

Start with one critical operation, such as submitting an order, importing a dataset or applying a configuration change. Identify who initiates it, who owns its durable result and who responds when it fails. Use that same operation to populate the files below. This keeps the implementation rule, test and release decision traceable to the same outcome.

| Decision | Where to maintain it | Example entry |
| --- | --- | --- |
| What a contributor needs on day one | [AGENTS.md](AGENTS.md) | Owning team, supported components, generated paths, setup and check commands |
| How state and consumers are protected | [Code style](docs/standards/code-style.md) and [interface conventions](docs/standards/api-conventions.md) | A batch has a stable identity. Replaying it preserves totals. A published view defines when the batch is complete. |
| How to demonstrate the promise | [Testing](docs/standards/testing.md) | Interrupt the importer after its first checkpoint, resume it and compare reconciled totals |
| How an operator makes a release decision | [Deployment contract](.agents/skills/deploy/references/deploy-config.md) | Name the signal owner, observation window, acceptable lag and recovery action |
| How the team detects and recovers from failure | [Operational readiness](docs/standards/operational-readiness.md) | Compare the age of the last reconciled batch with the freshness objective and rehearse recovery from its checkpoint |

Record numeric targets, escalation contacts, tool versions and exception expiry dates from the owning team's actual commitments. For a time-limited exception, identify the affected requirement, compensating measure, decision owner and review date. Keep the decision with the requirement so its next maintainer can find it.

## Specification baseline

Publisher references checked on 2026-11-19. Choose the edition supported by your consumers and record it with the component. Recheck publisher status, errata and tooling support when changing that edition.

| Area | Reference | Evidence of application |
| --- | --- | --- |
| HTTP descriptions and errors | [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html), [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457) | A validated description and a tested error example |
| Messaging | [AsyncAPI 3.1.0](https://www.asyncapi.com/docs/reference/specification/v3.1.0) | A message example validated against the published contract |
| Web accessibility | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Target level, applicable criteria and evidence for a complete user journey |
| Secure development | [NIST SSDF](https://csrc.nist.gov/projects/ssdf) | A selected practice, its owner and evidence from the development process |
| Artifact provenance | [SLSA 1.2](https://slsa.dev/spec/v1.2/) | Evidence linking the released artifact to its expected source and builder |

```text
.
|-- AGENTS.md                         Durable project instructions
|-- CODEX.md                          Human-facing setup and structure guide
|-- .codex/
|   |-- config.toml                   Trusted project configuration and MCP examples
|   |-- agents/                       Custom subagent roles
|   |-- rules/default.rules           Command approval and deny rules
|   |-- hooks.json                    Lifecycle hook registration
|   `-- hooks/validate_shell.py       Shell safety hook
|-- .agents/skills/                   Discoverable, reusable workflows
|   |-- review-change/SKILL.md
|   |-- fix-issue/SKILL.md
|   `-- deploy/SKILL.md
`-- docs/standards/                   Detailed conventions referenced by AGENTS.md
```

## Mapping from Claude Code

| Claude Code | Codex equivalent |
| --- | --- |
| `CLAUDE.md` | `AGENTS.md` |
| `CLAUDE.local.md` | Personal `~/.codex/AGENTS.md` or a deliberate `AGENTS.override.md` |
| `.mcp.json` | `[mcp_servers.<name>]` in `.codex/config.toml` |
| `claude/settings*.json` | `.codex/config.toml` plus personal `~/.codex/config.toml` |
| Markdown rule files | Referenced standards or nested `AGENTS.md` files |
| `.claude/rules/*.md` for shell policy | `.codex/rules/*.rules` |
| Slash commands | Skills in `.agents/skills/<name>/SKILL.md` |
| Reusable skills | Skills in `.agents/skills/<name>/SKILL.md` |
| Agent Markdown files | `.codex/agents/<name>.toml` |
| Hooks | `.codex/hooks.json` and hook scripts |

`AGENTS.override.md` is not an additive local file: in the same directory it replaces `AGENTS.md`. Keep personal defaults in `~/.codex/AGENTS.md` unless replacement behavior is intentional.

Codex `.rules` files control commands outside the sandbox; they are not prose coding standards. The prose standards therefore live under `docs/standards/` and are routed from `AGENTS.md`.

## Activate the project configuration

1. Open the folder as a trusted Codex project. Untrusted projects do not load project `.codex/` configuration, hooks, or command rules.
2. Start a new Codex session after changing `AGENTS.md`, configuration, hooks, or rules.
3. Open `/hooks`, review the checked-in hook, and trust it if its behavior is appropriate for your environment.
4. Invoke a workflow explicitly with `$review-change`, `$fix-issue`, or `$deploy`, or let Codex select it when the request matches its description.

The scaffold does not pin a model, approval policy, or sandbox mode. Those values inherit from each developer's account and personal `~/.codex/config.toml`.

## Add an MCP server

Add a table to `.codex/config.toml` using one of the commented examples. Keep credentials in environment variables or an OAuth flow; never commit secrets to this repository.
