# Code style

## What the component owner should record

Describe the component in terms of the outcome it owns, its callers, and its durable state. Identify its source of truth, the unit of change, and the rule that must hold after every successful change. Include one local example. For an import job, that rule might be “replaying an accepted batch preserves the number of accepted records.” Link to the implementation and the check that establishes the rule.

| When the component owns | Record the design decision | Evidence a maintainer can inspect |
| --- | --- | --- |
| A user interaction | Entry and completion states, keyboard and focus behavior, pending and interrupted work, and how the user recovers their input | An interaction example covering a failed save and a successful retry |
| Shared behavior or a service | Which layer validates input, authorizes the actor, commits state, and reports failure | A caller-to-commit trace showing when success becomes observable |
| Persistent data | Stable identity, units, null semantics, uniqueness, transaction boundary, retention owner and deletion behavior for derived copies | A schema constraint or equivalent invariant plus the migration that preserves existing records |
| A job or integration | Ordering assumptions, deadlines, retry owner, duplicate detection and the checkpoint used after interruption | A worked example of a partial batch resumed after a restart |
| Infrastructure or configuration | Source of desired state, scope of the change, treatment of drift and how operators recover previous state | A reviewed plan or equivalent before-and-after comparison |

For consequential tradeoffs, record the alternatives considered, the measurement that informed the choice, and the condition that would justify revisiting it. For a latency or capacity target, specify the operation, workload, percentile and measurement window. Decide which diagnostics operators need and which fields must be redacted before collection.

When a component processes sensitive data, identify the minimum fields each consumer needs, who may read or change them, where copies persist, and how a retention or deletion decision propagates. For security-sensitive dependencies, record their source, update owner and the check used to accept an update. The [NIST SSDF](https://csrc.nist.gov/projects/ssdf) provides a framework for selecting secure development practices.

## Implementation conventions

- Follow the conventions already established in the nearest production and test files.
- Prefer clear domain names and small, cohesive units over abstractions introduced for hypothetical reuse.
- Keep public behavior explicit. Document non-obvious invariants and tradeoffs, not syntax the code already states.
- Handle errors at the layer that has enough context to recover or produce an actionable message.
- Avoid unrelated formatting, renaming, and cleanup in a behavioral patch.
- Use the repository formatter and linter when they exist; do not hand-format against generated output.
