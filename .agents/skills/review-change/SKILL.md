---
name: review-change
description: Review a working tree, commit, branch, or pull-request diff for concrete defects and missing tests. Use for read-only code review; do not use when the user asks to implement fixes.
---

# Review Change

Record the comparison base, candidate and affected consumer. For a working tree, include staged and unstaged changes and identify relevant new files. Read both sides of a changed boundary, including a deployed reader or old data shape when versions may overlap.

Select checks by consequence. For interaction changes, follow focus, error feedback and recovery. For state changes, trace ownership, commit and retry behavior. For infrastructure changes, inspect intended resource scope, drift and recovery. State which contract is at risk and what a user or operator would observe.

A finding should contain a location in the change, a realistic starting state, the action that exposes the issue, expected and observed behavior, and supporting evidence. Rank findings by impact and reach. If evidence depends on an unknown deployment setting, name the setting and give the maintainer the smallest check that resolves the uncertainty.

Establish the requested comparison and inspect the full affected execution paths, not only isolated diff fragments.

Prioritize correctness, regressions, security, compatibility, data loss, race conditions, and missing tests. Ignore cosmetic preferences unless they hide a material risk.

Return findings first, ordered by severity. Each finding should identify the relevant file and location, explain the failure mode, and give a concise reproduction or triggering scenario. Distinguish confirmed defects from questions or residual risks.

Do not edit files during this workflow. If the user also wants fixes, finish the review and then use the `$fix-issue` workflow for the approved findings.
