# Testing

## Specify evidence for each material risk

Write each acceptance case as a starting state, action and observable outcome. Name the test boundary and the command or CI job that exercises it. A useful check for an interrupted update observes both the answer returned to the caller and the state a second caller can read. Select cases from the following table according to the change.

| Change | Representative case | Observable pass condition |
| --- | --- | --- |
| User workflow | Complete the critical path using a keyboard, trigger an input error, then correct it | Focus stays usable, the error identifies the field, and completion is perceivable. Map the result to applicable [WCAG 2.2 criteria](https://www.w3.org/TR/WCAG22/). |
| Access or ownership | Two synthetic principals with different scopes request the same record | The authorized principal succeeds and the denied request discloses no protected fields or state changes |
| Data evolution | Upgrade a representative previous schema containing missing and legacy values, interrupt the backfill, then resume | Counts, constraints and domain totals reconcile. Readers supported during rollout still work. |
| Concurrent or retried work | Deliver the same logical operation twice, including after its first response is lost | The final state and externally visible side effects satisfy the documented duplicate-delivery contract |
| Operational change | Apply the proposed configuration in an isolated environment, then exercise recovery | The intended resources change, the health probe observes a real operation and the recovery procedure restores the stated service level |

Record the revision, fixture or seed, relevant environment differences, expected result and actual result. Use synthetic or sanitized fixtures. Where mocks replace an important boundary, identify the integration or contract check covering that boundary. For performance claims, compare equivalent workloads and report sample size, tail latency, errors and resource use alongside the baseline.

For a flaky failure, preserve the first failure evidence, repeated-run count and suspected dependency. Give a quarantined case an owner, a restoration condition and a record of the coverage gap. For accessibility, combine automation with manual checks for focus order, accessible names and status announcements where applicable.

## Running the checks

- Reproduce a defect before fixing it when practical, then add or update a test that fails for the original behavior.
- Test externally observable behavior and meaningful invariants rather than private implementation details.
- Cover important success, failure, authorization, and boundary paths in proportion to risk.
- Keep tests deterministic. Control time, randomness, network access, and shared state at their boundaries.
- Run the narrowest affected tests first. Run broader suites when shared code, public contracts, or high-risk paths change.
- Never delete or weaken a valid assertion only to make a suite pass; explain genuine contract changes.
