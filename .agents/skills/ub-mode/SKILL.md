---
name: ub-mode
description: Implement behavior changes and behavior-preserving refactors with test-first development and small, verified steps. Use when the user invokes $ub-mode or requests this workflow for a code change.
---

# UB Mode

This workflow draws on Robert C. Martin's [UB Mode](https://github.com/unclebob/ub-mode/blob/master/SKILL.md), published under the [MIT license](https://github.com/unclebob/ub-mode/blob/master/LICENSE). Follow the applicable [project instructions](../../../AGENTS.md), [code style](../../../docs/standards/code-style.md), and [testing standard](../../../docs/standards/testing.md).

## Establish the behavior

- State the starting condition, the action through a supported entry point, and the observable result. Include relevant changes to state and side effects. For a defect, use [$fix-issue](../fix-issue/SKILL.md) to reproduce the failure and locate its cause.
- For a behavior change, add or extend a focused test and run it before editing production code. Confirm it fails for the expected reason. For a behavior-preserving refactor, run a passing test that captures the contract. Reuse existing coverage when it exercises the behavior at risk.
- When a faithful automated test is impractical, use the strongest available check at the affected boundary and report what it leaves unverified.

## Implement and simplify

- Make the smallest coherent change that satisfies one observable outcome, then rerun the focused check. For changes with several outcomes, repeat this cycle with the next outcome.
- Keep each decision with the component that owns it. When a patch strains an existing boundary, consider where the behavior would belong in a fresh design and move toward that design in steps the checks can verify. Share logic when callers need the same rule.
- Simplify the changed code while its behavior is covered. Rerun the focused check after each meaningful restructuring.

## Verify and report

Use the affected component's documented validation commands. Start with the focused check and expand validation when the change affects a shared interface, existing data, or another material risk. Report the initial failure or passing baseline, the final checks, and any verification limits.
