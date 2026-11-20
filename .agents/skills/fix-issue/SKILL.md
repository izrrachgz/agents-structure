---
name: fix-issue
description: Reproduce, diagnose, implement, and verify a focused software defect fix. Use when the user asks to fix a bug, regression, failing test, or concrete issue.
---

# Fix Issue

Capture the contract that failed, the first observable symptom, the affected revision and the smallest sanitized input that shows the difference. When the issue is intermittent, record frequency, ordering and environment. Use traces, state transitions or existing test results to narrow the first incorrect value.

Choose a regression case that discriminates among causes. For example, a duplicate record after a timeout could originate in the caller's retry, the worker's checkpoint or the storage uniqueness rule. Locate where one logical operation first becomes two and test the invariant at that boundary. For a presentation defect, exercise the actual interaction and verify that the user can recover their state.

Include previously stored values, supported older callers and partially completed work when the fix affects their behavior. State whether the patch also repairs existing affected state. Treat any needed historical data repair as a separate, explicitly scoped operation.

Read the applicable repository instructions and trace the real execution path before changing code. Reproduce the issue with the smallest reliable command, test, or input when practical.

Identify the root cause and make the smallest coherent fix that preserves surrounding contracts. Avoid unrelated refactors and do not weaken validation or tests to hide the failure.

Add or update regression coverage for the original failure when the repository has a suitable test layer. Validate narrowly first, then run broader checks when shared or public behavior changed.

Report the cause, the fix, validation performed, and any remaining risk or unverified environment dependency.
