# agents-structure

`agents-structure` is a reusable project scaffold for teams working with Codex. It gives contributors and agents a shared place to find project instructions, implementation and review workflows, engineering standards, and release procedures. Adopt it in a new or existing software repository and fill in the commands, owners, and controls for that project.

## Quick start

1. Clone the scaffold and open it for inspection.

   ```sh
   git clone https://github.com/izrrachgz/agents-structure.git
   cd agents-structure
   ```

2. For an existing project, copy or merge `AGENTS.md`, `CODEX.md`, `.agents/`, `.codex/`, and `docs/standards/` into the project root. Keep the hidden directories and applicable license notices. Review any existing instructions, hooks, and ignore rules before merging them with the scaffold.
3. Fill in the project's purpose, owning team, component boundaries, supported consumers, and runbook in [AGENTS.md](AGENTS.md). Record the working directory and exact commands for setup, a focused check, and the full CI check. Identify generated files and where their inputs live.
4. Review the project's configuration, rules, and shell hook. Open the project as trusted and start a Codex session once those settings are ready. See the activation steps and hook review instructions in the [Codex setup guide](CODEX.md#activate-the-project-configuration).
5. Use one critical user operation to verify the setup. Link its expected result to a focused test, the applicable controls, and the release or recovery evidence an operator will use. See the [adoption example](CODEX.md#adopting-the-scaffold-for-a-real-system).

## Repository layout

| Path | What it contains |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Project instructions for agents, including the checks and standards to use before making changes. |
| [CODEX.md](CODEX.md) | Setup and trust instructions, a Claude Code migration map, and guidance on project configuration. |
| [.agents/skills/](.agents/skills/) | Reusable workflows for implementation, diagnosis, review, and deployment. |
| [.codex/config.toml](.codex/config.toml) | Shared project settings and commented examples for connecting Model Context Protocol (MCP) servers. |
| [.codex/agents/](.codex/agents/) | Read-only code review and security audit roles for authorized delegation. |
| [.codex/rules/](.codex/rules/) and [.codex/hooks.json](.codex/hooks.json) | Execution policy rules and a registered shell hook for selected destructive commands. |
| [docs/standards/](docs/standards/) | Guidance for code, tests, interfaces, operations, and security and privacy adoption. |

## Choose a workflow

| Codex skill | When to use it |
| --- | --- |
| [`$ub-mode`](.agents/skills/ub-mode/SKILL.md) | The primary workflow for writing or changing code. Establish the expected behavior, keep changes small, and verify behavior as you simplify the implementation. |
| [`$fix-issue`](.agents/skills/fix-issue/SKILL.md) | Reproduce a failure and isolate the cause. Use UB Mode to implement and verify the fix. |
| [`$review-change`](.agents/skills/review-change/SKILL.md) | Review a diff for correctness, security, regressions, compatibility, and missing coverage. |
| [`$deploy`](.agents/skills/deploy/SKILL.md) | Prepare and verify a release. Fill in the [deployment contract](.agents/skills/deploy/references/deploy-config.md) with exact destinations, approvals, checks, health signals, and rollback procedures before making environment changes. |

For example, ask Codex to `Use $ub-mode to fix the duplicate import and verify that retrying the same batch preserves the record count.` For a review, ask it to `Use $review-change to review this branch against main and report any behavior regressions.`

## Security and privacy when adopting the scaffold

Adopting projects must implement and verify the software controls applicable under ISO/IEC 27001:2022, including its 2024 amendment, and ISO/IEC 27701:2025. Use the [security and privacy adoption standard](docs/standards/security-privacy.md) to define scope, assign owners, assess risks, record which controls apply, and retain verification evidence. Link the applicable checks and approved exceptions to the production release. The adopting organization assesses conformity for its documented management system scope.

Keep credentials outside version control and reference them by environment variable or approved secret store. Document what an MCP integration can access and verify a read-only operation using a non-production identity. See the [MCP configuration guidance](CODEX.md#add-an-mcp-server).

## Check the scaffold

The scaffold provides configuration and documentation. Each adopting project supplies its own build, test, and CI commands. For a scaffold change, check the diff with `git diff --check`, verify any edited links, and exercise changes to hooks or rules directly.

To verify the shell hook from the repository root, pass it two sample tool events using Python 3. These commands feed JSON to the handler. The shell commands in the event body are sample data.

```sh
echo '{"tool_input":{"command":"git status"}}' | python .codex/hooks/validate_shell.py
echo '{"tool_input":{"command":"format-volume"}}' | python .codex/hooks/validate_shell.py
```

The first sample produces no output. The second returns JSON with `permissionDecision` set to `deny`. Use `python3` if that is the name of your Python executable. See the [hook registration](.codex/hooks.json) and [execution policy rules](.codex/rules/default.rules) for how the checks are wired into the project.

When contributing, keep changes focused and include the checks you ran in the pull request. Put frequently used project instructions in `AGENTS.md` and detailed procedures in a standard or skill.

## License

The scaffold is available under the [MIT License](LICENSE). The bundled UB Mode skill includes [Robert C. Martin's MIT license and copyright notice](.agents/skills/ub-mode/LICENSE).
