---
name: fix-issue
description: Reproduce a software defect and isolate its root cause. Use for bug diagnosis or to support UB Mode during a defect fix.
---

# Fix Issue

When implementing a fix, follow [UB Mode](../ub-mode/SKILL.md) for the code change and verification.

Capture the contract that failed, the first observable symptom, the affected revision and the smallest sanitized input that shows the difference. When the issue is intermittent, record frequency, ordering and environment. Use traces, state transitions or existing test results to narrow the first incorrect value.

Choose a regression case that discriminates among causes. For example, a duplicate record after a timeout could originate in the caller's retry, the worker's checkpoint or the storage uniqueness rule. Locate where one logical operation first becomes two and test the invariant at that boundary. For a presentation defect, exercise the actual interaction and verify that the user can recover their state.

Include previously stored values, supported older callers and partially completed work when the fix affects their behavior. State whether the patch also repairs existing affected state. Treat any needed historical data repair as a separate, explicitly scoped operation.

Read the applicable repository instructions and trace the real execution path before changing code. Reproduce the issue with the smallest reliable command, test, or input when practical.

Report the smallest reproduction, the root cause and its supporting evidence, and any remaining risk or unverified environment dependency.
